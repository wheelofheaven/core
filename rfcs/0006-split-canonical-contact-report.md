---
title: "RFC 0006: Split the canonical contact report out of claim 0001"
status: accepted
authors:
  - project founder
  - Claude (drafting agent, at founder direction)
created: 2026-08-17
review_until: null
related_adrs:
  - ../decisions/0007-split-canonical-contact-report.md
supersedes: []
superseded_by: null
---

# RFC 0006: Split the canonical contact report out of claim 0001

## Review question

Should the Elohim-civilization hypothesis (`woh-claim-0001`) be partially
decomposed by extracting its report layer — what *The Book Which Tells the
Truth* explicitly reports at `TBWTT-1:53` and `TBWTT-2:5` — into a new
`source_report` claim, while the interpretive identification and the
civilization/design hypotheses remain bundled in `woh-claim-0001`?

## Summary

Adopt option 3 of the research question
[Should claim 0001 be split into four claims?](../docs/research/decompose-claim-0001.md):
a two-record partial split. A new claim, `woh-claim-0070` (the canonical
contact report), records the report layer as a `source_report` with public
label `direct`; `woh-claim-0001` is revised to depend on it, keeping
subclaims B–D (biblical identification, off-world civilization, design of
life) as one bundle. The full four-way decomposition is explicitly deferred.

## Problem and scope

`woh-claim-0001` is filed as one `hypothesis`, but its evidence map
decomposes it into four subclaims of different kinds, and the record names
its own compoundness as a revision trigger ("the compound proposition cannot
be reviewed without splitting into stable subclaims"). One record forces one
`claim_kind`, one `evidence_status` list, and one version onto parts that
mature on different timelines and answer to different disciplines. The map's
independence summary identifies source criticism of the canonical report as
the load-bearing question of the whole foundational claim; while the report
layer is fused into the hypothesis record, that review cannot proceed
independently.

Scope: one new claim record and specification, a revision of
`woh-claim-0001` and its specification and evidence map, the catalog, the
conceptual-architecture claim map, the TBWTT source note, and the RFC 0002
binding re-key on the seven bound derivative pages. Non-goals: the full
four-way split; any change to `woh-claim-0002`; any change to public URLs,
badges, or templates; any judgement on whether the reported events occurred.

## Claim kinds and evidence

This is a repository-process decision about record granularity
(`normative_recommendation` territory), not evidence for or against any
substantive Wheel claim. Supporting observations:

- the `woh-claim-0001` evidence map already separates subclaims A–D with
  locators, so the extraction moves existing rows rather than authoring new
  content;
- `woh-claim-0020` (the contact reports as the canon's provenance)
  demonstrates the `source_report` discipline this record follows, and
  deliberately excludes the content layer this record carries;
- claim `woh-claim-0004`'s dependency re-point (0.1.0 → 0.2.0) is the
  version-bump precedent for the `woh-claim-0001` revision.

## Detailed proposal

1. **New record `woh-claim-0070`** — "The canonical contact report."
   `source_report`, framework relation `foundational`, public label
   `direct`, lifecycle `draft` (it advances with the pilot dossier that
   governs 0001–0004). Statement: the source explicitly reports off-world
   human-like speakers (`TBWTT-1:53`) and the artificial creation of
   terrestrial life by the civilization's scientists (`TBWTT-2:5`); the
   record asserts the report, not the occurrence. Depends on
   `woh-claim-0020` (the reports as published texts). Controlling document:
   `docs/framework/canonical-contact-report.md`. Its evidence map receives
   the subclaim-A rows from the `woh-claim-0001` map.
2. **Revision of `woh-claim-0001`** (0.1.0 → 0.2.0, a breaking change under
   the versioning rules: new dependency, narrowed scope). The statement is
   unchanged — the record keeps its ID because its proposition is not
   materially different; the report layer was implicit basis, not asserted
   content. Changes: dependency on `woh-claim-0070`; scope exclusion of the
   report layer; the compoundness trigger replaced by the deferred-split
   trigger; the edition trigger re-pointed through the dependency.
3. **`woh-claim-0002` unchanged.** Its needed subclaims (identification and
   existence) remain in `woh-claim-0001`, so its dependency still points at
   the right record; the report layer reaches it transitively through
   0001 → 0070. The full four-way split will re-point it precisely.
4. **Binding re-key.** The seven pages bound to `woh-claim-0001` at `0.1.0`
   (`method.md`, `about.md`, `wiki/elohim.md`, `wiki/elohim-home-planet.md`,
   `wiki/message-from-the-designers.md`, `wiki/intelligent-design.md`,
   `wiki/ancient-astronaut-hypothesis.md`) update `core_versions` to
   `0.2.0`. No page declares `woh-claim-0070` yet; binding pages that render
   the report layer is left to backfill.
5. **Deferred full split.** The four-way decomposition (option 1) triggers
   when a review of the biblical-identification or design-of-life subclaims
   actually advances toward `reviewed`; the trigger is written into
   `woh-claim-0001`.

## Alternatives

- **Full four-way split now (option 1).** Each part gets the right kind and
  independent status immediately, but it multiplies records and re-keys the
  binding before any review of B or D exists to justify the churn.
- **Keep the compound record (option 2, status quo).** No migration, but the
  record's own revision trigger stands unaddressed, and a single
  `evidence_status` continues to misdescribe at least one part.
- **Treat `woh-claim-0020` as the extracted report.** Rejected: 0020
  deliberately records the reports' existence and provenance and excludes
  their content; collapsing the content layer into it would erase exactly
  the distinction it was built to hold.

## Risks, limitations, and dissent

- A two-record split leaves B–D compound; the misdescription cost is reduced,
  not eliminated, and is accepted until a real review forces the full split.
- The partial split re-keys the binding once now and once again at the full
  split; the deferral is a bet that the second re-key is far away.
- The recommendation adopted here was based on record ergonomics and the
  existing evidence map, not on a completed systematic review.

## Compatibility and migration

- New: `model/claims/woh-claim-0070.json`,
  `docs/framework/canonical-contact-report.md`,
  `docs/evidence/woh-claim-0070-evidence.md`.
- Revised: `model/claims/woh-claim-0001.json` (0.2.0),
  `docs/framework/elohim-civilization-hypothesis.md`,
  `docs/evidence/woh-claim-0001-evidence.md`, `model/catalog.json`,
  `docs/foundations/conceptual-architecture.md`,
  `source-notes/the-book-which-tells-the-truth.md`,
  `docs/research/decompose-claim-0001.md`.
- Publication: seven `data-content` pages re-key `core_versions` for
  `woh-claim-0001` to `0.2.0`; no URL, badge, or template changes.
- Identifiers: no ID is retired or reused; `woh-claim-0001` retains its ID
  with an unchanged statement.

## Validation plan

`python3 scripts/validate.py` (schema, catalog, cross-file consistency, and
the RFC 0002 publication-integration check against the sibling checkouts)
must pass after the change; the binding check must report no version
disagreement on the seven re-keyed pages.

## Resolution

Accepted by founder direction on 2026-08-17; recorded in
[ADR 0007](../decisions/0007-split-canonical-contact-report.md).
