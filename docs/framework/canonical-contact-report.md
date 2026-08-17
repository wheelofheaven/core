---
title: The canonical contact report
status: draft
version: 0.1.0
last_reviewed: 2026-08-17
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

The inspected Wheel digitization of *The Book Which Tells the Truth*
includes:

- `TBWTT-1:53`, reporting: "We are men like you, and we live on a planet
  quite similar to Earth";
- `TBWTT-2:5`, reporting the source's gloss of `Elohim`, the search for a
  suitable planet, and the artificial creation of life.

See the [source note](../../source-notes/the-book-which-tells-the-truth.md).
Edition and translation collation remain open review tasks; the record's
first revision trigger is a material change to these passages under
collation.

## Evidence status

`scoped`. See the [evidence map](../evidence/woh-claim-0070-evidence.md),
which carries the subclaim-A rows formerly held by the `woh-claim-0001`
map.

## Dependencies

- `woh-claim-0020` — the contact reports as published texts; this record
  presupposes the documented reports whose provenance that record states.

## Revision triggers

As in the machine record.

## Public derivatives

None bound yet. Pages that render the report layer (rather than the
hypothesis) may be bound here under the RFC 0002 contract as backfill
proceeds.
