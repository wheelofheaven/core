---
title: "Research question: should claim 0001 be split into four claims?"
status: draft
version: 0.1.0
last_reviewed: 2026-08-02
---

# Research question: should claim 0001 be split into four claims?

## Exact question

Should the Elohim-civilization hypothesis (`woh-claim-0001`) remain one
compound record, or be decomposed into separately versioned claims for (a) the
canonical contact report, (b) identifying its beings with biblical `Elohim`,
(c) the extraterrestrial-civilization proposition, and (d) the design of
terrestrial life?

## Why it matters

The record itself already lists this as a revision trigger ("the compound
proposition cannot be reviewed without splitting into stable subclaims"), and
its own evidence map is built around exactly these four subclaims (A–D). The
Anunnaki–Elohim identity claim (`woh-claim-0002`) depends on 0001; if 0001
splits, 0002 must be re-pointed at whichever sub-claim it actually needs
(almost certainly the identification and existence sub-claims, not the
design-of-life sub-claim). The publication-integration pilot (RFC 0002) binds
`wiki/elohim.md` to `woh-claim-0001` at `0.1.0`; a split is a MAJOR change that
would re-key that binding.

## Scope

- Texts: *The Book Which Tells the Truth* (canonical); Genesis, Deuteronomy 32,
  Psalm 82 (biblical identification); directed-panspermia and synthetic-genome
  literature (design/possibility).
- Distinctions: source report vs. interpretation vs. hypothesis vs. empirical
  possibility.
- Exclusion: this question is about record granularity, not about whether the
  hypothesis is true.

## Claim kinds involved

The compound record is filed as one `hypothesis`, but its parts are of
different kinds — and this is the core argument for splitting:

| Sub-claim | Natural claim kind | Natural evidence handling |
| --- | --- | --- |
| A. Canonical contact report | `source_report` | Textual; source-critical review of the Raëlian corpus |
| B. Biblical `Elohim` identification | `interpretation` | Philological + comparative review of Hebrew usage |
| C. Extraterrestrial civilization | `hypothesis` | Depends on A; historical/scientific discriminability |
| D. Design of terrestrial life | `hypothesis` | Depends on A + C; biological discriminability |

Keeping them in one record forces one `claim_kind`, one `evidence_status`
list, and one version onto four parts that will mature and be challenged on
different timelines and by different disciplines.

## Current basis

- Evidence map [`woh-claim-0001-evidence.md`](../evidence/woh-claim-0001-evidence.md)
  already separates A–D with locators (`TBWTT-1:53`, `TBWTT-2:5`,
  `GEN-WOH-1:26`, `GEN-WOH-3:22`, `GEN-WOH-6:2,4`, `DEU-32:8-9`, `PSA-82:1`,
  `GEN-WOH-2:7`).
- Claim `woh-claim-0003` was authored with an explicit five-layer
  decomposition and validates cleanly, demonstrating that the model and
  validator handle a decomposed foundational claim without strain.
- Access level: `project_digitization` for canonical and biblical text;
  `metadata_only`/conceptual for the scientific-possibility sources.

## Competing answers

1. **Split into four versioned claims** with a retained mapping from
   `woh-claim-0001`. Pros: each part gets the right claim kind and independent
   evidence status; 0002 can depend on precisely the sub-claim it needs;
   reviews can advance B (philology) without touching D (biology). Cons: four
   records plus a superseding-mapping record; more cross-links; a MAJOR version
   event that re-keys the RFC 0002 binding.
2. **Keep one compound record**, relying on the evidence map for internal
   structure. Pros: fewer records, stable IDs, no migration. Cons: the record
   already names its own compoundness as a revision trigger; a single
   `evidence_status` cannot honestly express "A is source-attested, C and D are
   contested and largely undiscriminated."
3. **Partial split** — separate the `source_report` (A) from the
   `interpretation/hypothesis` bundle (B–D), a two-record split. A middle
   option that isolates the load-bearing source-criticism question with the
   least churn.

## Discriminating evidence

The decision is architectural, not empirical, so "evidence" here is whether a
review can proceed cleanly under each option:

- If a reviewer cannot assign one `claim_kind` and one `evidence_status` to
  0001 without misdescribing at least one part, that favours a split.
- If 0002's dependency needs only B+C (identity + existence) and not D, that
  favours at least isolating D.
- If the RFC 0002 binding proves painful to re-key on a split, that favours
  deferring the split until the contract is accepted and stable.

## Method

1. Draft the four (or two) successor records as `proposed`, each with its own
   kind, scope, and evidence status, plus a mapping note from `woh-claim-0001`.
2. Re-point `woh-claim-0002.dependencies` at the successor sub-claims.
3. Follow the versioning rules for supersession (RFC + ADR, forward/backward
   links, retained history) — this is a MAJOR change and requires founder
   sign-off.
4. Re-key the RFC 0002 pilot binding on `wiki/elohim.md`.

## Outputs and compatibility

- Affected records: `woh-claim-0001` (superseded or extended),
  `woh-claim-0002` (dependency re-point), catalog, glossary.
- Affected specs: the framework spec, the evidence map, the conceptual
  architecture claim map.
- Affected derivatives: the RFC 0002 binding on `wiki/elohim.md`, and any
  future backfill.
- Requires: an RFC and an ADR (supersession is a breaking change).

## Status and review

- Owner: project founder (this is a `Changes requiring explicit human
  direction` item under `CLAUDE.md` — an agent must not split a foundational
  claim independently).
- **Preliminary recommendation (for the founder to accept or reject):** adopt
  option 3 now — split A (the `source_report`) out from B–D — because the
  source-criticism of the canonical report is the load-bearing question the
  evidence map identifies, and isolating it lets that review proceed without
  disturbing the philological and biological sub-questions. Move to the full
  four-way split (option 1) only when B or D is actually taken to `reviewed`,
  and do it after RFC 0002 is accepted so the binding is re-keyed once, not
  twice.
- Limitation: recommendation is based on record ergonomics and the existing
  evidence map, not on any completed systematic review.
