---
title: "ADR 0007: Split the canonical contact report out of claim 0001 (option 3)"
status: accepted
date: 2026-08-17
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0006-split-canonical-contact-report.md
---

# ADR 0007: Split the canonical contact report out of claim 0001 (option 3)

## Context

The research question
[Should claim 0001 be split into four claims?](../docs/research/decompose-claim-0001.md)
laid out three options for decomposing the compound Elohim-civilization
hypothesis, whose evidence map separates four subclaims (A: canonical
report, B: biblical identification, C: off-world civilization, D: design of
life) and whose record listed its own compoundness as a revision trigger.
The preliminary recommendation was option 3 — split the `source_report`
layer (A) out and keep B–D bundled — because source criticism of the
canonical report is the load-bearing question the map identifies.

## Decision drivers

- A single `claim_kind` and `evidence_status` cannot honestly describe four
  parts that mature under different disciplines.
- The source-critical review of the canonical report should be able to
  proceed without disturbing the philological and biological subquestions.
- Churn on records, bindings, and dependent claims should be paid when a
  review actually needs it, not in advance.

## Options considered

### Option A — full four-way split

Four versioned claims with a mapping from `woh-claim-0001`. Epistemically
cleanest; rejected for now because no review of B or D exists yet to justify
the record multiplication and double binding re-key.

### Option B — keep the compound record

Rely on the evidence map for internal structure. Rejected: the record's own
revision trigger names the compoundness, and the misdescription it causes is
exactly what the claim model exists to prevent.

### Option C — partial split (A out, B–D retained)

Extract the report layer as a `source_report`; revise `woh-claim-0001` to
depend on it. Selected.

## Decision

Adopt option C, as proposed in
[RFC 0006](../rfcs/0006-split-canonical-contact-report.md):

- `woh-claim-0070` "The canonical contact report" is created as a
  `foundational` `source_report` (public label `direct`, lifecycle `draft`,
  advancing with the 0001–0004 pilot dossier), depending on
  `woh-claim-0020`.
- `woh-claim-0001` moves to 0.2.0 with an unchanged statement, a dependency
  on `woh-claim-0070`, the report layer excluded from scope, and the full
  four-way decomposition recorded as a revision trigger instead of executed.
- `woh-claim-0002` is not re-pointed; its needed subclaims remain in
  `woh-claim-0001`.

Unresolved: the timing of the full four-way split, deliberately deferred
until a review of the biblical-identification or design-of-life subclaims
advances toward `reviewed`.

## Consequences

### Enables

- An independent source-critical review programme for the canonical report,
  the load-bearing question of the foundational claim.
- Honest per-layer evidence status: the report layer no longer inherits
  `contested` from the hypothesis bundle, and the bundle no longer borrows
  the report's textual attestation.
- Corpus prose can cite "what the canon reports" (`woh-claim-0070`,
  `direct`) separately from "what the framework claims happened"
  (`woh-claim-0001`, `framework`).

### Costs and risks

- B–D remain compound until the deferred split; one more binding re-key is
  owed when it lands.
- A fourth `foundational` claim enters the catalog; foundational additions
  are founder-gated, and this one was founder-directed.

## Compatibility and migration

See RFC 0006's compatibility section for the full file inventory. No claim
ID is retired or reused; `woh-claim-0001`'s statement is unchanged; seven
bound pages re-key `core_versions` to `0.2.0`; no public URL, badge, or
template changes.

## Validation and review

`python3 scripts/validate.py` passes after the change, including the RFC
0002 publication-integration check against the sibling checkouts with no
version disagreement on the re-keyed pages.
