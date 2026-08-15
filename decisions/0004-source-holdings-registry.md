---
title: "ADR 0004: Source holdings registry"
status: accepted
date: 2026-08-15
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0005-source-holdings-registry.md
---

# ADR 0004: Source holdings registry

## Context

The core's evidence discipline rests on the `access` level attached to every
source reference, which bounds what a claim may assert from a source. At the
time of this decision, **10 of 18 source references across the four claims sat
at `metadata_only`** — load-bearing, and never actually opened. That capped
every evidence map at `scoped`, and nothing in the project recorded which
copies of which sources it actually held.

RFC 0005 proposed a holdings registry in the private `data-sources` repository,
keyed to the same Wheel source IDs used by the bibliography and by this
repository, together with an ingest pipeline that makes a held scan searchable
without putting the work itself into version control.

## Decision drivers

- Make `access` levels verifiable and improvable rather than asserted.
- Give quotations an auditable provenance: which copy, which printing, which
  locator, read by whom and when.
- Take on no new redistribution posture, and add no storage cost that scales
  with the corpus.
- Drive acquisition from what the research needs instead of from browsing.

## Options considered

Recorded in RFC 0005: the status quo (no registry), holdings in the public
`data-bibliography`, holdings in `core`, and committing every payload to LFS in
the private repository. For the pipeline specifically, the rejected option was
OCR-and-commit — which fails because OCR changes the file format, not the
copyright status of the work.

## Decision

Accept RFC 0005 as proposed.

The registry lives at `data-sources/holdings/`, one record per held or
consulted copy, recording edition, acquisition and provenance, pagination
basis, checksum, rights note, and a per-locator `verifications[]` log.

Storage is decided per record and defaults conservatively: `local_only` for
in-copyright works, with `repo_lfs` reserved for public-domain, CC0, or
explicitly permissioned material. `print_only` and `external` are first-class
cases. The registry is therefore useful whether or not any payload is ever
uploaded.

The ingest pipeline operates on the principle **OCR to find, page image to
verify, short quote to cite**. Readable text goes to a git-ignored local
working store; what is versioned is the derived apparatus — page map, hashed
search index, density profile. Readable text is committed only when
`licensing_status` is `public_domain`.

Holding a copy licenses consultation, verification, and short quotation with
locators. It does not license republication, redistribution, or wholesale
digitization of in-copyright works into `data-library`; that boundary is
unchanged.

## Consequences

### Enables

- A source note's declared access level can be traced to a specific copy and a
  specific reading, rather than resting on assertion.
- `wantlist.py` derives acquisition priorities from the claim catalog,
  separating "already held, go read it" from "not held, acquire to unblock",
  with critical-role sources weighted up so the list does not systematically
  under-buy what would challenge the framework.
- A held scan becomes searchable at roughly 1.5% of the payload size, with no
  copyrighted text entering version control.

### Costs and risks

- Local-only payloads are not backed up by this design; durability remains the
  founder's arrangement, and a checksum detects corruption without repairing it.
- Recording a holding creates pressure to claim a higher access level than was
  exercised. Owning a book is not reading it: `access_level` records what a copy
  *affords*, the core reference records what was *used*, and the verification
  log is the bridge.
- Contributors without access to the private repository cannot inspect a
  holding's basis; the public source note remains the citable artifact.
- The search index matches exact hashed tokens, so transliteration variants
  must be tried. A zero result means a token is absent, not a topic.
- OCR is unreliable on this corpus's Greek, Akkadian, and Hebrew. The extracted
  text is a finding aid only, and quotations must be read off the page image.

## Compatibility and migration

Additive and private. No public repository, page, URL, schema, badge, or
identifier changes. The registry starts nearly empty and grows as holdings are
recorded; absence of a record is never an error.

The decision surfaced one structural fact worth carrying forward:
`data-bibliography` is legacy, covering roughly a quarter of the corpus, while
the live registry that is authoritative for source identity carries no
`licensing_status` field at all. Source-ID validation therefore runs against
the live registry, and a holding may declare its own `licensing_status` so that
routing is a recorded decision rather than a fallback. Determining the status of
the sources that currently have none is follow-on work, not a precondition.

## Open item not decided here

RFC 0005 records that the `data-sources` `LICENSE` file is a bare CC0
dedication, which contradicts the repository's own README and cannot apply to
third-party copyrighted material. **This ADR does not resolve that.** Selecting
a license is a separate founder decision; the recommendation on record is the
carve-out this repository uses — CC0 for original material only, with source
materials retaining their own rights.

## Validation and review

The pilot ran end to end: `black-green-mesopotamia` as a consulted-in-place
record, and West's *East Face of Helicon* through the full pipeline — a
346-page pure image scan OCR'd into 692 book pages with folio calibration at
0.951 confidence, 2.5 MB of apparatus committed against a 165 MB payload that
never entered git.

The real validation is still ahead: the first time a logged verification
changes a core access level, and through it an evidence map. West is now the
top of the wantlist's READ list and remains at `metadata_only` on
`woh-claim-0004` until its Hesiod chapters are actually read. Revisit this ADR
if holdings accumulate without verifications — that would mean the registry had
become inventory rather than research infrastructure.

## References

- [RFC 0005](../rfcs/0005-source-holdings-registry.md)
- [ADR 0002](0002-artifact-derivation-contract.md)
- [Evidence status](../docs/methodology/evidence-status.md)
- [Source note: Black & Green](../source-notes/black-green-mesopotamia.md)
