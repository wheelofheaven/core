---
title: The canonical contact report
status: accepted
version: 0.2.0
last_reviewed: 2026-08-31
claim_id: woh-claim-0070
---

# The canonical contact report

## Exact proposition

*The Book Which Tells the Truth* explicitly reports that its speakers are
biological beings like terrestrial humans living on another planet
(`TBWTT-1:53`), glosses `Elohim` as "those who came from the sky," and
reports that the civilization's scientists selected Earth and artificially
created terrestrial life, including humanity (`TBWTT-2:5`).

This record asserts what the source reports, not that the reported events
occurred. It is a `source_report` with framework relation `foundational` and
public label `direct`.

## Why this record exists

The record was extracted from the Elohim-civilization hypothesis
([`woh-claim-0001`](elohim-civilization-hypothesis.md)) by the partial split
adopted in [RFC 0006](../../rfcs/0006-split-canonical-contact-report.md) and
[ADR 0007](../../decisions/0007-split-canonical-contact-report.md). The
hypothesis's own evidence map identifies source criticism of the canonical
report as the load-bearing question of the whole foundational claim; keeping
the report layer inside the compound hypothesis record forced one
`claim_kind` and one `evidence_status` onto parts that mature on different
timelines. Extracting the `source_report` lets that review proceed without
disturbing the philological and biological subquestions, which remain in
`woh-claim-0001`.

The division of labour among the neighbouring records:

- [`woh-claim-0020`](contact-reports-provenance.md) records that the contact
  reports exist — dates, publication sequence, movement founding — as
  documented fact. It deliberately excludes the content of the messages.
- **This record** carries the content layer: what the report says, at the two
  passages on which the foundational hypothesis stands.
- [`woh-claim-0001`](elohim-civilization-hypothesis.md) carries the
  hypothesis layer: that the reported beings, identified with biblical
  `Elohim`, were a real off-world civilization that designed terrestrial
  life.

The claim model's first invalid transition — source report to historical
occurrence — is the boundary between this record and `woh-claim-0001`. When
corpus prose states what the canon reports, it cites this record; when it
asserts that the reported events happened, it stands on `woh-claim-0001`'s
hypothesis discipline. Citing this record as if it established the
encounter is the record's one forbidden use, written into its revision
triggers exactly as in `woh-claim-0020`.

## Current basis

Three witnesses to *The Book Which Tells the Truth* have been compared: the
Wheel digitization (French base text), the 2005 French combined edition
*Le Message donné par les Extra-terrestres*, and the 2005 English combined
edition *Intelligent Design: Message from the Designers*.

- `TBWTT-1:53` — « Nous sommes des hommes comme vous et nous vivons sur une
  planète assez semblable à la Terre » (2005 French ed., p. 18); published
  English: "We are people like you, and we live on a planet similar to Earth"
  (*Intelligent Design*, p. 8). The report is qualified eight turns later at
  `TBWTT-1:61`, where the same speaker says a human could not live on that
  planet because the atmosphere is very different.
- `TBWTT-2:5` — the source's gloss of `Elohim` as « ceux qui sont venus du
  ciel » / "those who came from the sky", its insistence that the word is
  plural, the search for a suitable planet, and the artificial creation of
  life (2005 French ed., p. 20; *Intelligent Design*, p. 11).

**Quotation provenance.** The digitization's English is an AI-assisted
rendering generated in 2026, not a published translation, and is never quoted
here as the source's own English. See the
[source note](../../source-notes/the-book-which-tells-the-truth.md).

Collation against the 2005 editions is complete and found the digitization's
French faithful to them. The 1973 and 1974 first printings remain uncollated
and are the live case for the record's first revision trigger.

## Evidence status

`scoped`. See the [evidence map](../evidence/woh-claim-0070-evidence.md),
which carries the subclaim-A rows formerly held by the `woh-claim-0001`
map.

The status has **not** advanced despite a completed review. Two of the three
components the evidence map names were performed; the genre and
source-critical appraisal is blocked on holdings and remains outstanding, and
the advancement rule does not admit a partial review.

## Reviews

- [`woh-claim-0070-review-0001`](../reviews/woh-claim-0070-review-0001.md) —
  draft, unsigned. Edition collation and internal consistency performed;
  source-critical appraisal outstanding. Confirmed the record's substance
  against all three witnesses, rejected `alt-0070-misreading`, and rejected
  `alt-0070-edition-variance` for the French. Its one material correction was
  to quotation practice, not to the claim: English wordings previously
  presented as the source's words were the digitization's machine rendering.

## Dependencies

- `woh-claim-0020` — the contact reports as published texts; this record
  presupposes the documented reports whose provenance that record states.

## Revision triggers

As in the machine record.

## Public derivatives

None bound yet. Pages that render the report layer (rather than the
hypothesis) may be bound here under the RFC 0002 contract as backfill
proceeds.
