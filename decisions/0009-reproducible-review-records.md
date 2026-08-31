---
title: "ADR 0009: Adopt reproducible review records"
status: accepted
date: 2026-08-31
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0007-reproducible-review-records.md
---

# ADR 0009: Adopt reproducible review records

## Context

[`docs/methodology/evidence-status.md`](../docs/methodology/evidence-status.md)
has specified the advancement rule since the repository's first stage: a claim
moves beyond `scoped` only with a documented search protocol, inclusion
criteria, extraction record, appraisal, limitations, and dated reviewer
sign-off. The rule existed only as prose. No artifact carried it, no directory
held it, and `claim.schema.json` — which sets `additionalProperties: false` —
had no field that could point at review evidence.

The measurable consequence: 70 accepted claims, every one still at `scoped`,
none ever advanced. Stage 4 of the [roadmap](../ROADMAP.md) was blocked on a
missing file format rather than on missing research.

[RFC 0007](../rfcs/0007-reproducible-review-records.md) proposed the smallest
artifact that discharges the existing rule, and shipped a worked example
against it: the first review of
[`woh-claim-0070`](../docs/framework/canonical-contact-report.md).

## Decision drivers

- The advancement rule must become executable without changing what any
  evidence status *means*.
- A drafting agent must not be able to promote a claim by writing a confident
  document.
- Partial reviews are the expected early case and must be able to record
  findings without advancing a status.
- Acquisition needs discovered by a review must become visible to tooling, not
  just to prose.

## Options considered

### Option A — Adopt the RFC 0007 format

A `docs/reviews/` directory, an eight-section record, an optional `reviews`
array on the claim schema, and a validator that enforces the mechanical half of
the advancement rule while leaving the judgement to a human signature.

### Option B — Leave the rule in prose

No new format; reviewers write what seems right. This is the status quo, and
the status quo has produced no reviews in the life of the repository.

### Option C — Fold reviews into the evidence maps

Reuse an existing per-claim document instead of adding a class. Rejected in the
RFC: evidence maps are living documents, a review is a dated event, and merging
an append-only record into a mutable one destroys the audit trail that makes
`reviewed` mean anything.

## Decision

**Option A.** The review-record format, the schema binding, and the validator
rules are adopted as specified in RFC 0007.

Ratified sub-points:

- A signed review does **not** self-execute a status change. The validator
  enforces that a review-gated status is backed by a signed record with no
  outstanding components; granting the status remains a human act.
- `contested` is **not** review-gated. A credible conflict may be recorded
  without a formal review. The gated set is `reviewed`, `replicated`, and
  `unsupported`.
- Review records are append-only. A superseding review takes the next sequence
  number and links back; a signed record is never edited to reflect a later
  view.
- The feedback rule is binding: a review that establishes a need for a source
  the claim does not cite requires that source be added to `source_references`
  at an honest access level.

**`woh-claim-0070` does not advance.** Its review is unsigned and its
source-critical component is outstanding. The claim stays `scoped`. This ADR
adopts the instrument, not a finding.

## Consequences

### Enables

- Stage 4 can begin. The first review record exists and the format is no longer
  hypothetical.
- Review-gated statuses are now mechanically defended: the validator rejects a
  claim that claims `reviewed` without a signed record behind it.
- `scripts/wantlist.py` now sees claim 0070's critical-source need, because the
  feedback rule put `aliens-adored` and the Dericquebourg chapter into the
  record's `source_references` at `metadata_only`.

### Costs and risks

- Every advance requires the founder. This bottleneck is accepted deliberately;
  the alternative is automated epistemic promotion.
- An eight-section record is heavy for a small correction. The format is
  required only where a record bears on `evidence_status`.
- A signed review can still be wrong. Supersession, not revision, is the
  remedy.

## Compatibility and migration

- `model/schemas/claim.schema.json`: `schema_version` `0.1.0` → `0.2.0`; new
  optional `reviews` array with a `reviewReference` definition. **No migration**
  — the field is optional and all 70 existing records stay valid. Only records
  that use the field declare `0.2.0`.
- `scripts/validate.py`: `reviews` added to the allowed field set;
  `validate_claim_reviews()` added, enforcing the binding, the
  signed/`signed_by`/`signed_date` pairing, and the advancement rule. An
  `optional_field()` helper treats the repository's `null` frontmatter
  placeholder as absent — the line parser returns it as a truthy string.
- `woh-claim-0070`: `0.1.0` → `0.2.0` (MINOR — added evidence and an optional
  field; statement, kind, relation, label and dependencies unchanged). Two
  critical `source_references` added at `metadata_only`; the `reviews` binding
  added; the first revision trigger narrowed to name the uncollated first
  printings. Its specification and catalog entry move with it.
- **No public compatibility effect.** `woh-claim-0070` has no
  `public_derivatives` and no page binds it, so the version bump re-keys
  nothing in `data-content` or `www`. No reader-facing badge, URL, or
  translation changes.
- No existing identifier changes meaning; `review_id` is a new namespace.

## Validation and review

`scripts/validate.py` passes with `json_schema=checked` (70 claim records, 6
source notes, `external_sources=checked`,
`publication_integration=checked`).

The three new rules were negative-tested before adoption by temporarily
corrupting the record and confirming each error fires: advancing
`evidence_status` to `reviewed` against an unsigned review; marking a review
`signed` without `signed_by`/`signed_date`; and binding a `review_id` belonging
to a different claim. The repository was restored to green after each.

The real test is the first signed record that advances a status. When that
happens it should be reviewed as a process question rather than assumed to have
worked. Grounds for revision: if the format deters reviews instead of enabling
them, a format nobody uses is worse than prose.

## References

- [RFC 0007](../rfcs/0007-reproducible-review-records.md)
- [Review 0001 of woh-claim-0070](../docs/reviews/woh-claim-0070-review-0001.md)
- [Evidence status](../docs/methodology/evidence-status.md)
- [Versioning](../docs/methodology/versioning.md)
- [ADR 0007](0007-split-canonical-contact-report.md) — the split that created
  `woh-claim-0070`
