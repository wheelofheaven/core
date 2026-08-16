---
title: "ADR 0005: Acceptance of the distilled claim catalog"
status: accepted
date: 2026-08-16
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0003-artifact-derivation-contract.md
---

# ADR 0005: Acceptance of the distilled claim catalog

## Context

Under the artifact derivation contract (ADR 0002), six distillation
batches between 2026-08-15 and 2026-08-16 extracted the Wheel of Heaven
corpus's claim layer into records: claims 0005 through 0053, each
drafted with a controlling specification and a scoped evidence map,
each presented at a founder gate before its derivative pages were
bound. The founder reviewed the batches at those gates; this ADR
records the consolidated acceptance ruling.

## Decision

Claims **woh-claim-0005 through woh-claim-0053** are promoted from
`draft` to `accepted` lifecycle. Acceptance is the repository's own
category and means exactly what the claim model says it means: these
records are the **current project specifications** of what the
framework claims — not findings, not validations, not upgrades of any
evidence status.

Explicitly ruled with the acceptance:

- **The 0023 foundational placement is confirmed.** Fractal cosmology
  stands as the catalog's second foundational premise cluster-head,
  flagged at drafting and confirmed here.
- **The normative family's posture is ratified**: the four
  `normative_recommendation` records (0032, 0033, 0041, 0049) carry the
  canon's proposals as reportable and never as endorsed; the is/ought
  policing written into them is the project's position.
- **The posture rule of 0053 is ratified**: the global reading posture
  licenses no specific reading, and posture-laundering remains a named
  violation.
- **The systematization disclosures stand**: records whose objects are
  corpus constructs (0045, 0046, 0047, 0051, 0052 among them) keep that
  status disclosed inside the record.

Not promoted: claims **0001–0004** (the three founding pilots and the
reverse pilot), which remain `draft` pending their own review, exactly
as scoped by the founder's instruction.

Unchanged by this decision: every record's version, public label,
evidence status (`scoped`/`contested` stand — acceptance is not
evidence), scope, alternatives, and revision triggers. Two records
(0006, 0041) gained `contested` in the pre-promotion consistency sweep,
aligning them with the catalog's convention for externally
unendorsed labels.

## Consequences

### Enables

- Derivative pages now render claims whose records carry the
  repository's accepted status; the `claim_type` badges stand on
  ratified ground.
- Future artifacts ground against accepted records; the founder pause
  now prices only genuinely new claims.
- Revision becomes the governed path: changing an accepted record's
  meaning follows the versioning rules, with supersession machinery
  for breaking changes.

### Costs and risks

- Accepted status can read, to a careless reader, as validation; the
  claim model's "lifecycle is not truth" rule is the standing answer,
  and every record's own evidence status contradicts the misreading.
- Bulk acceptance rests on batch-gate review rather than per-record
  deep review; the revision triggers are the correction mechanism, and
  any record can be individually reopened.

## Validation and review

The catalog validates end to end (53 records; specifications synced;
publication integration checked across ~105 bound pages). Review this
ADR if accepted records accumulate trigger-conditions without
revision — that would mean acceptance had frozen what the triggers
were built to keep alive.

## References

- [ADR 0002](0002-artifact-derivation-contract.md) (the contract)
- [Claim model](../docs/methodology/claim-model.md) (lifecycle semantics)
- [Versioning](../docs/methodology/versioning.md) (the revision path)
