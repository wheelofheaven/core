#!/usr/bin/env python3
"""Instruments for the research programme proposed in RFC 0009.

  kernel           list the claims research takes as given
  status           scoreboard of expectations by ruling, discrimination, novelty
  next-id          print the next free woh-exp id
  brief ID         print the Locator's brief for one expectation
  assess ID        print record, criteria and finding path for the Recorder

The brief prints the question, target and protocol only. The statement,
derivation, criteria and rival predictions are withheld on purpose: the
Locator reports what a source contains without knowing which answer the
programme expects. See docs/methodology/research-programme.md.
"""

import argparse
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTATIONS = ROOT / "model" / "expectations"
CLAIMS = ROOT / "model" / "claims"


def load(directory):
    records = {}
    if directory.is_dir():
        for path in sorted(directory.glob("*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            records[record["id"]] = record
    return records


def cmd_kernel(_args):
    claims = load(CLAIMS)
    dependents = collections.Counter()
    for record in claims.values():
        for dependency in record.get("dependencies", []):
            dependents[dependency] += 1
    print("| Claim | Version | Kind | Dependents | Title |")
    print("| --- | --- | --- | --- | --- |")
    for claim_id, record in claims.items():
        if record["lifecycle"] == "accepted" and record["framework_relation"] == "foundational":
            print(f"| {claim_id} | {record['version']} | {record['claim_kind']} "
                  f"| {dependents[claim_id]} | {record['title']} |")
    return 0


def outcome(record):
    if record["status"] == "withdrawn":
        return "withdrawn"
    if record["ruling"]:
        return record["ruling"]["outcome"]
    return f"unruled ({record['status']})"


def cmd_status(args):
    records = load(EXPECTATIONS)
    if args.claim:
        records = {k: v for k, v in records.items() if v["claim_id"] == args.claim}
    if args.cycle:
        records = {k: v for k, v in records.items() if v["cycle"] == args.cycle}
    if not records:
        print("No expectations registered.")
        return 0

    print("| Expectation | Claim | Kind | Discrimination | Novelty | Assessment | Outcome | Title |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for exp_id, r in records.items():
        print(f"| {exp_id} | {r['claim_id'][-4:]} | {r['kind']} | {r['discrimination']} "
              f"| {r['novelty']} | {r['assessment'] or '—'} | {outcome(r)} | {r['title']} |")

    ruled = [r for r in records.values() if r["ruling"]]
    tally = collections.Counter(
        (r["discrimination"] != "none", r["novelty"] == "unrecorded", r["ruling"]["outcome"])
        for r in ruled
    )

    def count(discriminating, unrecorded, result):
        return tally[(discriminating, unrecorded, result)]

    print()
    print(f"Registered: {len(records)}; ruled: {len(ruled)}; "
          f"awaiting ruling: {sum(1 for r in records.values() if not r['ruling'] and r['status'] != 'withdrawn')}.")
    print()
    print("| Class | hit | miss | narrowed | open | void |")
    print("| --- | --- | --- | --- | --- | --- |")
    for label, disc, unrec in (
        ("Discriminating, unrecorded (progress class)", True, True),
        ("Discriminating, retrodiction", True, False),
        ("Non-discriminating, unrecorded", False, True),
        ("Non-discriminating, retrodiction", False, False),
    ):
        cells = " | ".join(str(count(disc, unrec, o)) for o in ("hit", "miss", "narrowed", "open", "void"))
        print(f"| {label} | {cells} |")
    print()
    print("The table measures the programme's yield. It is not a probability that a claim is true.")
    return 0


def cmd_next_id(_args):
    numbers = [int(i.rsplit("-", 1)[1]) for i in load(EXPECTATIONS)]
    print(f"woh-exp-{(max(numbers) + 1 if numbers else 1):04d}")
    return 0


def get(exp_id):
    records = load(EXPECTATIONS)
    if exp_id not in records:
        sys.exit(f"unknown expectation {exp_id}")
    return records[exp_id]


def cmd_brief(args):
    r = get(args.id)
    target = r["target"]
    lines = [
        f"# Locator brief: {r['id']}",
        "",
        "## Question",
        "",
        r["question"],
        "",
        "## Target",
        "",
        f"- Source: {target['description']}",
    ]
    if target.get("source_id"):
        lines.append(f"- Wheel source id: `{target['source_id']}`")
    lines.append(f"- Scope: {target['locator_scope']}")
    if target.get("holding"):
        lines.append(f"- Where to find it: {target['holding']}")
    lines += ["", "## Protocol", ""]
    lines += [f"{n}. {step}" for n, step in enumerate(r["protocol"], 1)]
    lines += [
        "",
        "## Report to",
        "",
        f"`docs/research/programme/{r['cycle']}/{r['id']}-finding.md`",
    ]
    print("\n".join(lines))
    return 0


def cmd_assess(args):
    r = get(args.id)
    print(json.dumps({k: r[k] for k in ("id", "statement", "criteria", "finding", "assessment")},
                     indent=2, ensure_ascii=False))
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("kernel").set_defaults(func=cmd_kernel)
    status = sub.add_parser("status")
    status.add_argument("--claim")
    status.add_argument("--cycle")
    status.set_defaults(func=cmd_status)
    sub.add_parser("next-id").set_defaults(func=cmd_next_id)
    for name, func in (("brief", cmd_brief), ("assess", cmd_assess)):
        p = sub.add_parser(name)
        p.add_argument("id")
        p.set_defaults(func=func)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
