#!/usr/bin/env python3
"""Validate the flood review and reproduce its long-form CSV (standard library)."""

import argparse
import collections
import csv
import hashlib
import io
import json
from pathlib import Path

CORE = Path(__file__).resolve().parents[2]
DIRECTORY = CORE / "docs/research/flood-concordance"


def checked_data():
    data = json.loads((DIRECTORY / "concordance.json").read_text())
    baseline_raw = (DIRECTORY / "baseline-1.1.json").read_bytes()
    baseline = json.loads(baseline_raw)
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    require(hashlib.sha256(baseline_raw).hexdigest() == data["baseline_sha256"],
            "Baseline bytes differ from the recorded SHA-256")
    source_ids = [s["id"] for s in data["sources"]]
    require(len(set(source_ids)) == len(source_ids), "Duplicate source IDs")
    ids = [row["id"] for row in data["rows"]]
    require(len(ids) == len(set(ids)), "Duplicate row IDs")
    require(ids == [r["id"] for r in baseline["rows"]],
            "Legacy row IDs or ordering changed without reconciliation")
    for claim, version in data["core_bindings"].items():
        record = json.loads((CORE / "model/claims" / (claim + ".json")).read_text())
        require(record["version"] == version, f"Stale binding: {claim}")
    for source in data["sources"]:
        require(source["url"].startswith("https://"), f"Missing URL: {source['id']}")
        require(bool(source["edition"] and source["inspected_scope"] and source["limitations"]),
                f"Missing source provenance: {source['id']}")
    for row in data["rows"]:
        require(list(row["cells"]) == data["fields"], f"Missing/reordered cells: {row['id']}")
        require(bool(row["date_review"]), f"Date review not disclosed: {row['id']}")
        require(set(row["edition_source_ids"]) <= set(source_ids),
                f"Unknown edition source: {row['id']}")
        require(list(row["chronology"]) == ["composition", "witness", "internal_date", "event_date"],
                f"Missing chronology distinctions: {row['id']}")
        for kind, date in row["chronology"].items():
            key = f"{row['id']}.chronology.{kind}"
            require(date["status"] in data["chronology_state_definitions"],
                    f"Unknown chronology state: {key}")
            require(bool(date["note"]), f"Missing chronology qualification: {key}")
            unresolved = date["status"] in ("not_reassessed", "not_established", "not_audited", "not_assigned")
            if unresolved:
                require(date["value"] is None, f"Unverified date presented as a value: {key}")
            else:
                require(bool(date["value"] and date["references"]), f"Uncited date: {key}")
            for reference in date["references"]:
                require(reference["source_id"] in source_ids and bool(reference["locator"].strip()),
                        f"Invalid chronology reference: {key}")
        for field, cell in row["cells"].items():
            key = f"{row['id']}.{field}"
            require(cell["state"] in data["state_definitions"], f"Unknown state: {key}")
            require(bool(cell["references"]), f"Uncited cell: {key}")
            for reference in cell["references"]:
                require(reference["source_id"] in source_ids, f"Unknown source: {key}")
                require(bool(reference["locator"].strip()), f"Missing locator: {key}")
            if cell["state"] in ("not_stated", "text_damaged", "not_checked"):
                require(cell["value"] is None, f"Unknown cell contains a positive assertion: {key}")
            else:
                require(isinstance(cell["value"], str) and bool(cell["value"].strip()),
                        f"Empty attestation or qualification: {key}")
            if cell["state"] in ("uncertain", "text_damaged", "not_checked", "explicitly_absent"):
                require(bool(cell["note"]), f"Missing uncertainty/absence explanation: {key}")
    for relationship in data["relationships"]:
        require(set(relationship["members"]) <= set(ids), f"Unknown relationship member: {relationship['id']}")
        require(bool(relationship["basis"] and relationship["status"]),
                f"Unsupported relationship: {relationship['id']}")
    if errors:
        raise ValueError("\n".join(errors))
    return data, baseline


def csv_text(data, baseline):
    sources = {s["id"]: s for s in data["sources"]}
    previous = {row["id"]: row for row in baseline["rows"]}
    result = io.StringIO(newline="")
    writer = csv.writer(result, lineterminator="\n")
    writer.writerow(["row_id", "source_text", "field", "legacy_value", "revised_value",
                     "state", "references", "source_urls", "note"])
    for row in data["rows"]:
        for field, cell in row["cells"].items():
            refs = cell["references"]
            writer.writerow([row["id"], row["source_text"], field, previous[row["id"]][field],
                             cell["value"] if cell["value"] is not None else "",
                             cell["state"],
                             " | ".join(r["source_id"] + ": " + r["locator"] for r in refs),
                             " | ".join(sources[r["source_id"]]["url"] for r in refs), cell["note"]])
    return result.getvalue()


def chronology_csv_text(data):
    sources = {s["id"]: s for s in data["sources"]}
    result = io.StringIO(newline="")
    writer = csv.writer(result, lineterminator="\n")
    writer.writerow(["row_id", "legacy_date", "date_kind", "reviewed_value", "status",
                     "references", "source_urls", "note"])
    for row in data["rows"]:
        for kind, date in row["chronology"].items():
            refs = date["references"]
            writer.writerow([row["id"], row["legacy_date"], kind, date["value"] or "",
                             date["status"],
                             " | ".join(r["source_id"] + ": " + r["locator"] for r in refs),
                             " | ".join(sources[r["source_id"]]["url"] for r in refs), date["note"]])
    return result.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate both CSV exports after validation")
    args = parser.parse_args()
    data, baseline = checked_data()
    exports = {"observations.csv": csv_text(data, baseline),
               "chronology.csv": chronology_csv_text(data)}
    for filename, expected in exports.items():
        target = DIRECTORY / filename
        if args.write:
            target.write_text(expected)
        elif not target.exists() or target.read_text() != expected:
            raise ValueError(f"{filename} is missing or stale; rerun with --write")
    states = collections.Counter(cell["state"] for row in data["rows"] for cell in row["cells"].values())
    print(f"PASS: {len(data['rows'])} rows, {sum(states.values())} cited cells, {len(data['sources'])} source representations")
    print("Evidence states:", json.dumps(dict(sorted(states.items()))))
    print("Checks are structural; they do not certify historical truth, translation accuracy or publication readiness.")


if __name__ == "__main__":
    main()
