---
title: "ADR 0008: Promotion of the pilot claims and the canonical contact report"
status: accepted
date: 2026-08-17
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0006-split-canonical-contact-report.md
---

# ADR 0008: Promotion of the pilot claims and the canonical contact report

## Context

ADR 0005 promoted claims 0005–0053 and explicitly excluded the pilots
0001–0004, which remained `draft` pending their own review. The review
dossier for the pilots was presented to the founder on 2026-08-16. Before
it was acted on, the founder adopted option 3 of the claim 0001
decomposition question (RFC 0006, ADR 0007), which extracted the report
layer as `woh-claim-0070` and revised `woh-claim-0001` to 0.2.0 with an
unchanged statement. The
[dossier addendum](../docs/research/pilot-promotion-dossier-addendum.md)
records the effect of that change on each pilot's promotion case and put
three options to the founder.

## Decision

The founder adopted the addendum's **option 1**: claims **woh-claim-0001,
woh-claim-0002, woh-claim-0003, woh-claim-0004, and woh-claim-0070** are
promoted from `draft` to `accepted` lifecycle, in one ruling.

Acceptance means what the claim model says it means: these records are the
current project specifications of what the framework claims — not
findings, not validations, not upgrades of any evidence status.

Explicitly ruled with the acceptance:

- **The dependency order is kept clean.** The hypothesis record (0001) and
  its foundational `source_report` dependency (0070) are accepted
  together; neither outranks the other in lifecycle.
- **The per-claim cases of the presented dossier stand** for 0002, 0003,
  and 0004, which are textually unchanged since presentation; for 0001 the
  addendum records the case as strengthened by the split.
- **0070 rides accepted precedent**: the `source_report` discipline and
  `direct` label follow `woh-claim-0020` (accepted under ADR 0006),
  applied to the content layer with the same one-forbidden-use trigger.

Unchanged by this decision: every record's version (page bindings at
`0001@0.2.0` and `0004@0.2.0` are unaffected), public label, evidence
status (`scoped`/`contested` stand — acceptance is not evidence), scope,
alternatives, and revision triggers. The deferred four-way split of claim
0001 remains a revision trigger, not a scheduled task. Evidence maps keep
`draft` status as living research artifacts, per the ADR 0005 convention.

## Consequences

### Enables

- The catalog carries no draft records for the first time: 70 claims, all
  `accepted`. The founding claims and the corpus distilled from them now
  share one lifecycle.
- The foundational layer (0001, 0003, 0023, 0070) is fully ratified;
  artifacts grounding against it no longer inherit pilot-era ambiguity.
- The first reproducible review (claim 0070's source criticism is the
  standing candidate) starts from an accepted record, so its outcome maps
  onto evidence status alone.

### Costs and risks

- As with ADR 0005: accepted status can misread as validation. Every
  record in this set remains `scoped` (0001 and 0002 also `contested`),
  and the claim model's "lifecycle is not truth" rule is the standing
  answer.
- The pilots' promotion rests on the presented dossier and the addendum
  rather than a per-record deep review; the revision triggers remain the
  correction mechanism, and any record can be individually reopened.

## Validation and review

The catalog validates end to end after the flip (70 records;
specifications synced to lifecycle; publication integration checked with
no version disagreement). Review this ADR if a pilot record accumulates
trigger-conditions without revision, or if the deferred four-way split of
claim 0001 fires — the successor records will need their own acceptance
path.

## References

- [Dossier addendum](../docs/research/pilot-promotion-dossier-addendum.md)
- [ADR 0005](0005-claim-catalog-acceptance.md) (promotion precedent and exclusion of the pilots)
- [RFC 0006](../rfcs/0006-split-canonical-contact-report.md) / [ADR 0007](0007-split-canonical-contact-report.md) (the split)
- [Claim model](../docs/methodology/claim-model.md) (lifecycle semantics)
