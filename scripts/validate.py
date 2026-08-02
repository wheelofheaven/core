#!/usr/bin/env python3
"""Validate Wheel of Heaven Core without required third-party dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
MODEL = ROOT / "model"
CATALOG_PATH = MODEL / "catalog.json"

LIFECYCLES = {"draft", "proposed", "accepted", "deprecated", "superseded"}
CLAIM_KINDS = {
    "source_report",
    "empirical_observation",
    "model",
    "hypothesis",
    "interpretation",
    "normative_recommendation",
}
FRAMEWORK_RELATIONS = {
    "foundational",
    "derived",
    "comparative",
    "contextual",
    "critical",
}
EVIDENCE_STATUSES = {
    "unmapped",
    "scoped",
    "reviewed",
    "replicated",
    "contested",
    "unsupported",
}
PUBLIC_LABELS = {"direct", "framework", "inferred", "speculative"}
ACCESS_LEVELS = {
    "full_text",
    "project_digitization",
    "excerpt",
    "abstract",
    "metadata_only",
    "secondary_citation",
}
SOURCE_ROLES = {
    "canonical_basis",
    "primary_text",
    "scholarly_context",
    "scientific_context",
    "comparative",
    "critical",
}
SEMVER_RE = re.compile(r"^(0|[1-9][0-9]*)\.[0-9]+\.[0-9]+$")
CLAIM_ID_RE = re.compile(r"^woh-claim-[0-9]{4}$")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.error(message)


def load_json(path: Path, validation: Validation) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        validation.error(f"{path.relative_to(ROOT)}: cannot load JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        validation.error(f"{path.relative_to(ROOT)}: top-level JSON must be an object")
        return {}
    return value


def frontmatter(path: Path, validation: Validation) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        validation.error(f"{path.relative_to(ROOT)}: missing YAML front matter")
        return {}
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        validation.error(f"{path.relative_to(ROOT)}: unterminated YAML front matter")
        return {}
    fields: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^([a-z_]+):\s*(.+)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip('"\'')
    return fields


def validate_document_metadata(validation: Validation) -> None:
    for area in ("foundations", "framework", "evidence", "methodology", "research"):
        for path in sorted((ROOT / "docs" / area).glob("*.md")):
            if path.name.endswith("-template.md"):
                continue
            fields = frontmatter(path, validation)
            for key in ("title", "status", "version", "last_reviewed"):
                validation.require(bool(fields.get(key)), f"{path.relative_to(ROOT)}: missing {key}")
            if fields.get("status"):
                validation.require(
                    fields["status"] in LIFECYCLES,
                    f"{path.relative_to(ROOT)}: invalid status {fields['status']!r}",
                )
            if fields.get("version"):
                validation.require(
                    bool(SEMVER_RE.fullmatch(fields["version"])),
                    f"{path.relative_to(ROOT)}: invalid version {fields['version']!r}",
                )
            if fields.get("last_reviewed"):
                validation.require(
                    bool(DATE_RE.fullmatch(fields["last_reviewed"])),
                    f"{path.relative_to(ROOT)}: invalid last_reviewed {fields['last_reviewed']!r}",
                )


def validate_claim_record(
    record_path: Path,
    record: dict[str, Any],
    validation: Validation,
) -> set[str]:
    rel = record_path.relative_to(ROOT)
    required = {
        "schema_version",
        "id",
        "title",
        "version",
        "lifecycle",
        "statement",
        "claim_kind",
        "framework_relation",
        "evidence_status",
        "public_label",
        "scope",
        "source_references",
        "dependencies",
        "alternatives",
        "revision_triggers",
        "controlling_document",
        "public_derivatives",
        "last_reviewed",
    }
    for field in sorted(required):
        validation.require(field in record, f"{rel}: missing {field}")
    allowed = required | {"$schema"}
    for field in sorted(set(record) - allowed):
        validation.error(f"{rel}: unknown field {field}")

    claim_id = record.get("id")
    validation.require(isinstance(claim_id, str) and bool(CLAIM_ID_RE.fullmatch(claim_id)), f"{rel}: invalid id")
    validation.require(record_path.stem == claim_id, f"{rel}: filename must match id")
    validation.require(record.get("lifecycle") in LIFECYCLES, f"{rel}: invalid lifecycle")
    validation.require(record.get("claim_kind") in CLAIM_KINDS, f"{rel}: invalid claim_kind")
    validation.require(
        record.get("framework_relation") in FRAMEWORK_RELATIONS,
        f"{rel}: invalid framework_relation",
    )
    validation.require(record.get("public_label") in PUBLIC_LABELS, f"{rel}: invalid public_label")
    validation.require(
        isinstance(record.get("version"), str) and bool(SEMVER_RE.fullmatch(record["version"])),
        f"{rel}: invalid version",
    )
    validation.require(
        isinstance(record.get("schema_version"), str)
        and bool(SEMVER_RE.fullmatch(record["schema_version"])),
        f"{rel}: invalid schema_version",
    )
    validation.require(
        isinstance(record.get("last_reviewed"), str)
        and bool(DATE_RE.fullmatch(record["last_reviewed"])),
        f"{rel}: invalid last_reviewed",
    )

    evidence = record.get("evidence_status")
    validation.require(isinstance(evidence, list) and bool(evidence), f"{rel}: evidence_status must be non-empty")
    if isinstance(evidence, list):
        validation.require(len(evidence) == len(set(evidence)), f"{rel}: duplicate evidence_status")
        for value in evidence:
            validation.require(value in EVIDENCE_STATUSES, f"{rel}: invalid evidence status {value!r}")

    controlling = record.get("controlling_document")
    if isinstance(controlling, str):
        controlling_path = (record_path.parent / controlling).resolve()
        validation.require(controlling_path.is_file(), f"{rel}: missing controlling document {controlling}")
        if controlling_path.is_file():
            fields = frontmatter(controlling_path, validation)
            validation.require(fields.get("claim_id") == claim_id, f"{rel}: controlling document claim_id differs")
            validation.require(fields.get("version") == record.get("version"), f"{rel}: controlling document version differs")
            validation.require(fields.get("status") == record.get("lifecycle"), f"{rel}: controlling document status differs")

    source_ids: set[str] = set()
    refs = record.get("source_references")
    validation.require(isinstance(refs, list), f"{rel}: source_references must be an array")
    if isinstance(refs, list):
        for index, ref in enumerate(refs):
            prefix = f"{rel}: source_references[{index}]"
            validation.require(isinstance(ref, dict), f"{prefix} must be an object")
            if not isinstance(ref, dict):
                continue
            source_id = ref.get("source_id")
            validation.require(isinstance(source_id, str) and bool(source_id), f"{prefix}: missing source_id")
            if isinstance(source_id, str):
                source_ids.add(source_id)
            validation.require(bool(ref.get("locator")), f"{prefix}: missing locator")
            validation.require(ref.get("access") in ACCESS_LEVELS, f"{prefix}: invalid access")
            validation.require(ref.get("role") in SOURCE_ROLES, f"{prefix}: invalid role")
            for field in sorted(set(ref) - {"source_id", "locator", "role", "access", "note"}):
                validation.error(f"{prefix}: unknown field {field}")
            note = ref.get("note")
            if isinstance(note, str):
                note_path = (record_path.parent / note).resolve()
                validation.require(note_path.is_file(), f"{prefix}: missing note {note}")
                if note_path.is_file():
                    fields = frontmatter(note_path, validation)
                    validation.require(fields.get("source_id") == source_id, f"{prefix}: source note ID differs")
                    validation.require(fields.get("source_access") == ref.get("access"), f"{prefix}: source access differs from note")

    alternatives = record.get("alternatives")
    validation.require(isinstance(alternatives, list) and bool(alternatives), f"{rel}: alternatives must be non-empty")
    triggers = record.get("revision_triggers")
    validation.require(isinstance(triggers, list) and bool(triggers), f"{rel}: revision_triggers must be non-empty")
    return source_ids


def validate_catalog(validation: Validation) -> tuple[dict[str, dict[str, Any]], set[str]]:
    catalog = load_json(CATALOG_PATH, validation)
    for field in sorted(set(catalog) - {"$schema", "catalog_version", "status", "last_reviewed", "claims"}):
        validation.error(f"model/catalog.json: unknown field {field}")
    validation.require(bool(SEMVER_RE.fullmatch(str(catalog.get("catalog_version", "")))), "model/catalog.json: invalid catalog_version")
    validation.require(catalog.get("status") in LIFECYCLES, "model/catalog.json: invalid status")
    validation.require(bool(DATE_RE.fullmatch(str(catalog.get("last_reviewed", "")))), "model/catalog.json: invalid last_reviewed")

    entries = catalog.get("claims")
    validation.require(isinstance(entries, list), "model/catalog.json: claims must be an array")
    if not isinstance(entries, list):
        return {}, set()

    records: dict[str, dict[str, Any]] = {}
    source_ids: set[str] = set()
    for index, entry in enumerate(entries):
        prefix = f"model/catalog.json: claims[{index}]"
        validation.require(isinstance(entry, dict), f"{prefix} must be an object")
        if not isinstance(entry, dict):
            continue
        allowed = {"id", "title", "version", "lifecycle", "claim_kind", "framework_relation", "record", "specification"}
        for field in sorted(set(entry) - allowed):
            validation.error(f"{prefix}: unknown field {field}")
        claim_id = entry.get("id")
        validation.require(isinstance(claim_id, str) and bool(CLAIM_ID_RE.fullmatch(claim_id)), f"{prefix}: invalid id")
        if not isinstance(claim_id, str):
            continue
        validation.require(claim_id not in records, f"{prefix}: duplicate claim id {claim_id}")
        record_value = entry.get("record")
        spec_value = entry.get("specification")
        validation.require(isinstance(record_value, str), f"{prefix}: missing record")
        validation.require(isinstance(spec_value, str), f"{prefix}: missing specification")
        if not isinstance(record_value, str) or not isinstance(spec_value, str):
            continue
        record_path = (MODEL / record_value).resolve()
        spec_path = (MODEL / spec_value).resolve()
        validation.require(record_path.is_file(), f"{prefix}: missing record {record_value}")
        validation.require(spec_path.is_file(), f"{prefix}: missing specification {spec_value}")
        if not record_path.is_file():
            continue
        record = load_json(record_path, validation)
        records[claim_id] = record
        source_ids.update(validate_claim_record(record_path, record, validation))
        for field in ("id", "title", "version", "lifecycle", "claim_kind", "framework_relation"):
            validation.require(entry.get(field) == record.get(field), f"{prefix}: {field} differs from claim record")

    registered_files = {(MODEL / entry["record"]).resolve() for entry in entries if isinstance(entry, dict) and isinstance(entry.get("record"), str)}
    actual_files = {path.resolve() for path in (MODEL / "claims").glob("*.json")}
    for path in sorted(actual_files - registered_files):
        validation.error(f"{path.relative_to(ROOT)}: claim record missing from catalog")
    for path in sorted(registered_files - actual_files):
        validation.error(f"{path}: catalog record does not exist")

    for claim_id, record in records.items():
        dependencies = record.get("dependencies", [])
        if isinstance(dependencies, list):
            for dependency in dependencies:
                validation.require(dependency in records, f"model/claims/{claim_id}.json: unknown dependency {dependency}")
                validation.require(dependency != claim_id, f"model/claims/{claim_id}.json: self dependency")
    return records, source_ids


def validate_source_notes(validation: Validation) -> set[str]:
    source_ids: set[str] = set()
    for path in sorted((ROOT / "source-notes").glob("*.md")):
        if path.name in {"README.md", "source-note-template.md"}:
            continue
        fields = frontmatter(path, validation)
        for key in ("title", "source_id", "note_status", "source_access", "last_reviewed"):
            validation.require(bool(fields.get(key)), f"{path.relative_to(ROOT)}: missing {key}")
        source_id = fields.get("source_id")
        if source_id:
            source_ids.add(source_id)
            validation.require(path.stem == source_id, f"{path.relative_to(ROOT)}: filename must match source_id")
        validation.require(fields.get("note_status") in LIFECYCLES, f"{path.relative_to(ROOT)}: invalid note_status")
        validation.require(fields.get("source_access") in ACCESS_LEVELS, f"{path.relative_to(ROOT)}: invalid source_access")
        validation.require(bool(DATE_RE.fullmatch(fields.get("last_reviewed", ""))), f"{path.relative_to(ROOT)}: invalid last_reviewed")
    return source_ids


def validate_local_links(validation: Validation) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            resolved = (path.parent / file_part).resolve()
            validation.require(resolved.exists(), f"{path.relative_to(ROOT)}: broken local link {target}")


def find_source_registry(wheel_root: Path) -> Path | None:
    candidate = wheel_root / "www.wheelofheaven.world" / "data" / "sources.json"
    return candidate if candidate.is_file() else None


def validate_external_sources(
    source_ids: set[str],
    wheel_root: Path,
    validation: Validation,
) -> bool:
    registry_path = find_source_registry(wheel_root)
    if registry_path is None:
        validation.warn(
            "Wheel source registry unavailable; skipped external source-ID validation "
            f"(looked under {wheel_root})"
        )
        return False
    try:
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
        registry_ids = {entry["id"] for entry in payload.get("sources", []) if isinstance(entry, dict) and entry.get("id")}
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        validation.error(f"Cannot load source registry {registry_path}: {exc}")
        return False
    for source_id in sorted(source_ids):
        validation.require(source_id in registry_ids, f"unknown Wheel source ID: {source_id}")
    return True


def optional_json_schema_validation(validation: Validation) -> bool:
    claim_schema = load_json(MODEL / "schemas" / "claim.schema.json", validation)
    load_json(MODEL / "schemas" / "catalog.schema.json", validation)
    try:
        import jsonschema  # type: ignore[import-not-found]
    except ImportError:
        validation.warn("jsonschema not installed; structural cross-file validation still ran")
        return False

    for record_path in sorted((MODEL / "claims").glob("*.json")):
        record = load_json(record_path, validation)
        try:
            jsonschema.Draft202012Validator(claim_schema, format_checker=jsonschema.FormatChecker()).validate(record)
        except jsonschema.ValidationError as exc:
            validation.error(f"{record_path.relative_to(ROOT)}: schema validation failed: {exc.message}")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--wheel-root",
        type=Path,
        default=ROOT.parent,
        help="Path containing sibling Wheel repositories (default: core parent)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validation = Validation()
    validate_document_metadata(validation)
    _, claim_source_ids = validate_catalog(validation)
    note_source_ids = validate_source_notes(validation)
    validate_local_links(validation)
    external_checked = validate_external_sources(claim_source_ids | note_source_ids, args.wheel_root.resolve(), validation)
    schema_checked = optional_json_schema_validation(validation)

    for warning in validation.warnings:
        print(f"WARN: {warning}")
    for error in validation.errors:
        print(f"ERROR: {error}")

    if validation.errors:
        print(f"FAILED: {len(validation.errors)} error(s), {len(validation.warnings)} warning(s)")
        return 1

    claim_count = len(list((MODEL / "claims").glob("*.json")))
    note_count = len([path for path in (ROOT / "source-notes").glob("*.md") if path.name not in {"README.md", "source-note-template.md"}])
    print(
        "OK: "
        f"{claim_count} claim record(s), {note_count} source note(s); "
        f"external_sources={'checked' if external_checked else 'skipped'}; "
        f"json_schema={'checked' if schema_checked else 'skipped'}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
