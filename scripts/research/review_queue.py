#!/usr/bin/env python3
"""Rank accepted claims for the review cycle proposed in RFC 0008.

Prints a Markdown table. The score is a triage aid, not a judgement of a
claim's truth: it favours claims that many others depend on, that cite
sources nobody has opened, that feed many public pages, and that have not
been reviewed or revised. Weights are deliberately simple and live here so a
change to them is a reviewable diff.

Usage: python3 scripts/research/review_queue.py [--top N]
"""

import argparse
import collections
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNREAD = {"metadata_only", "secondary_citation", "abstract"}
WEIGHTS = {"dependents": 2.0, "unread_share": 5.0, "derivatives": 0.3,
           "unreviewed": 2.0, "never_revised": 1.0, "age_per_30_days": 0.5}


def load():
    claims = {}
    for path in sorted((ROOT / "model/claims").glob("*.json")):
        record = json.loads(path.read_text())
        claims[record["id"]] = record
    return claims


def reviewed_ids():
    found = set()
    for path in (ROOT / "docs/reviews").glob("woh-claim-*-review-*.md"):
        found.add("-".join(path.stem.split("-")[:3]))
    return found


def score(claims, today):
    dependents = collections.Counter(d for c in claims.values() for d in c["dependencies"])
    reviewed = reviewed_ids()
    rows = []
    for cid, c in claims.items():
        refs = c["source_references"]
        unread = sum(r["access"] in UNREAD for r in refs) / len(refs) if refs else 1.0
        age = (today - date.fromisoformat(c["last_reviewed"])).days
        parts = {
            "dependents": dependents[cid] * WEIGHTS["dependents"],
            "unread_share": unread * WEIGHTS["unread_share"],
            "derivatives": len(c["public_derivatives"]) * WEIGHTS["derivatives"],
            "unreviewed": WEIGHTS["unreviewed"] if cid not in reviewed else 0.0,
            "never_revised": WEIGHTS["never_revised"] if c["version"] == "0.1.0" else 0.0,
            "age": age / 30 * WEIGHTS["age_per_30_days"],
        }
        rows.append((sum(parts.values()), cid, c, dependents[cid], unread, age, cid in reviewed))
    return sorted(rows, key=lambda r: (-r[0], r[1]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top", type=int, default=15)
    args = parser.parse_args()
    claims = load()
    rows = score(claims, date.today())
    print(f"Review queue, {date.today().isoformat()} ({len(claims)} claims)\n")
    print("| # | Claim | Title | Score | Dependents | Unread sources | Public pages | Version | Reviewed |")
    print("|---|---|---|---|---|---|---|---|---|")
    for n, (total, cid, c, deps, unread, age, rev) in enumerate(rows[:args.top], 1):
        print(f"| {n} | `{cid}` | {c['title']} | {total:.1f} | {deps} | {unread:.0%} | "
              f"{len(c['public_derivatives'])} | {c['version']} | {'yes' if rev else 'no'} |")


if __name__ == "__main__":
    main()
