---
title: "RFC 0005: Source holdings registry"
status: accepted
authors:
  - project founder
  - Claude (drafting agent, at founder direction)
created: 2026-08-15
review_until: null
related_adrs:
  - ../decisions/0004-source-holdings-registry.md
supersedes: []
superseded_by: null
---

# RFC 0005: Source holdings registry

## Review question

Should the project keep a machine-readable registry of the **actual source
copies it holds** — purchased books, downloaded scans, borrowed volumes — so
that a claim's `access` level and a quotation's provenance are auditable, and
so that acquisition can be driven by what the research actually needs?

## Summary

Add a `holdings/` registry to the existing **private** `data-sources`
repository: one JSON record per held copy, keyed to the Wheel source ID
already used by `data-bibliography`, `www/data/sources.json`, and this
repository's `source_references[].source_id`.

The registry is **storage-agnostic by design**. It records the identity of a
copy — edition, ISBN, pagination basis, checksum, where it physically or
digitally lives — without requiring the file itself to be committed. In-copyright
purchased works default to `local_only`: their bytes stay on the founder's
disk, and only their metadata and verification history are versioned. Material
that is public domain, CC0, or explicitly permissioned may additionally be
stored in the repository through the LFS configuration already present there.

The registry's purpose is not archival. It is to make the core's `access`
levels **honest and improvable**: to answer "do we hold this, in which edition,
and which passages has anyone actually read?"

## Problem and scope

The core's evidence discipline depends on the `access` level attached to every
source reference: `full_text`, `project_digitization`, `excerpt`, `abstract`,
`metadata_only`, `secondary_citation`. That vocabulary bounds what a record may
assert from a source.

Across the four current claims, **10 of 18 source references are
`metadata_only`** — cited, load-bearing, and never actually opened:

| Claim | Uninspected references |
| --- | --- |
| `woh-claim-0003` | `hamlets-mill`, `neugebauer-history-astronomy`, `astronomical-algorithms`, `sendy-ere-du-verseau`, the Hamlet's-Mill critique |
| `woh-claim-0004` | Güterbock 1948, West 1997, Lord 1960, Lévi-Strauss 1955, Bigliardi |

This is the binding constraint on the whole research programme. An evidence map
cannot move from `scoped` to `reviewed` while its scholarly context is
uninspected, and the one time a source *was* actually read — Black & Green,
upgraded `metadata_only` → `excerpt` — the reading **constrained** the claim
rather than supporting it. That is the value: inspection changes conclusions,
and un-inspection hides that it hasn't happened.

Nothing currently records what the project holds. `data-sources` exists and is
private, but is scoped to the Raëlian PDFs that feed the digitization pipeline
(three files); `data-bibliography` records what a source *is*, not whether we
have a copy; neither records which passages have been verified by whom.

Scope: a registry format, its validation, its relationship to `access` levels,
and an acquisition wantlist derived from core. Non-goals: mass acquisition,
digitization of in-copyright works, any change to what the project publishes,
and any change to the reading site.

## Claim kinds and evidence

A repository-process proposal (`normative_recommendation`). The motivating
observations are the access-level census above and the Black & Green
precedent recorded in
[its source note](../source-notes/black-green-mesopotamia.md).

## Detailed proposal

### Record shape

`data-sources/holdings/{source-id}.json`, where `{source-id}` is the existing
Wheel source ID. Fields:

| Field | Purpose |
| --- | --- |
| `source_id` | Join key to bibliography, core, and the public registry |
| `edition` | Publisher, year, printing, ISBN, translator, series — *which* copy this is |
| `acquisition` | `purchased`, `downloaded`, `borrowed`, `institutional_access`, `gift`; date; provenance note |
| `holding_format` | `print`, `pdf`, `epub`, `djvu`, `scan_images`, `audio` |
| `storage` | `local_only`, `repo_lfs`, `external`, `print_only` |
| `file` | Optional: relative path, `sha256`, byte size, page count — recorded even when `local_only` |
| `pagination_basis` | Which printing's page numbers locators refer to |
| `access_level` | The core vocabulary value this holding supports |
| `verifications` | Log entries: date, who, locator checked, what was found |
| `rights_note` | Copyright status and the bounds on use |

`access_level` is the load-bearing field: a holding of a physical book the
founder owns supports `full_text`; a partial scan supports `excerpt`; a record
with no copy supports nothing beyond `metadata_only`.

### Storage policy

- **Default `local_only`** for in-copyright works. The bytes are not uploaded;
  the checksum and location are recorded so the copy is identifiable and its
  integrity checkable.
- **`repo_lfs`** only for public-domain, CC0, or explicitly permissioned
  material — the existing narrow use of this repository.
- **`print_only`** for physical books with no digital copy. This is a
  first-class case, not a gap: a shelf copy fully supports `full_text` access
  and passage verification.

The registry is therefore useful whether or not any file is ever uploaded, and
the project takes on no new redistribution posture.

### Use bounds (explicit)

Holding a copy licenses **consultation, verification, and short quotation with
locators** — ordinary scholarly use, and the practice the corpus already
follows. It does not license republication, wholesale digitization of
in-copyright works into `data-library`, or redistribution of files. Records
carry a `rights_note` stating this per holding. The digitization track
(`data-library`) remains restricted to material the project may lawfully
publish; that boundary is unchanged by this RFC.

### The ingest pipeline

Recording that a copy exists is not enough to make it usable: a 350-page scan
is unsearchable until something extracts text from it. The obvious move —
OCR the book and commit the text — is rejected, because **OCR changes the file
format, not the copyright status**. A plain-text file of an in-copyright
monograph is the same protected work, smaller and more redistributable.

The pipeline therefore separates the *working artifact* from the *repository
artifact*, on the principle:

> OCR to find, page image to verify, short quote to cite.

Readable text is extracted (lifted from an existing text layer, or OCR'd when
the file is a pure scan) into a **git-ignored local working store**. What is
committed is the derived apparatus:

- a **page map** — PDF page ↔ printed folio, with the calibration confidence
  that supports it. Scans are frequently two-up, so PDF page and book page
  differ; a citation is only trustworthy once that offset is established.
- a **hashed search index** — one-way hashed tokens with book-page postings,
  no positions, no counts, order discarded. It answers "which pages mention
  this term" and cannot rebuild a sentence. This is a finding aid in the same
  sense as a back-of-book index.
- a **density profile** — characters per page, which identifies plates,
  blanks, and OCR failures.

Readable text is committed only when `licensing_status` is `public_domain`;
anything else, including `unknown`, stays local. This makes the licensing field
load-bearing, which surfaces a problem worth recording: the **live** source
registry carries no `licensing_status` at all, and the legacy
`data-bibliography` — which does — covers roughly a quarter of the corpus. A
holding may therefore declare its own status, so routing is a recorded decision
rather than an accident of which repo happens to hold a record.

One limitation deserves emphasis, because it constrains how the output may be
used. For this corpus — polytonic Greek, transliterated Akkadian and Hittite,
Hebrew, heavy diacritics — OCR is least reliable exactly where the argument is
most delicate. The extracted text is a finding aid only. **Quotations must be
read off the page image**, and the resulting finding logged in the holding's
`verifications[]`. That is also what keeps the access-level upgrade honest:
the log records what a human actually read, not what a tool guessed.

### Integration with the core

1. **Access-level provenance.** A source note's declared `source_access` should
   be supported by a holding record. Where a note claims `excerpt` or better,
   the registry says which copy was read.
2. **Verification log.** Source notes already end with a verification log; the
   registry is its machine-readable counterpart, keyed per locator.
3. **Acquisition wantlist.** A script derives, from core's claim records, every
   source reference at `metadata_only` or weaker, ranked by how many claims
   depend on it and whether the reference is load-bearing (`canonical_basis`
   and `primary_text` rank above `scholarly_context`). This turns acquisition
   from a browsing habit into a research instrument: it names the next book to
   buy and the claim it would unblock.

Validation stays in `data-sources` (a standalone script, matching the
dependency-free style of this repository's validator). This RFC proposes no
new core-side validator behaviour; a later RFC may cross-check `access` against
holdings once the registry has coverage.

### Licensing correction (founder decision required)

`data-sources` currently carries a bare CC0 `LICENSE` while its README states
it is private and holds third-party copyrighted material. CC0 can only be
applied to material the project owns, so the file misstates the repository's
position. The recommended correction is the carve-out this repository already
uses: CC0 for original material, with source materials retaining their own
rights. **Selecting a license is a founder decision and is not performed by
an agent**; this RFC records the defect and the recommendation.

## Alternatives

### Status quo

Keep buying and downloading books with no registry. Costs nothing today; leaves
`access` levels unverifiable, quotations un-provenanced, duplicate purchases
undetected, and the `metadata_only` backlog invisible.

### Put holdings in `data-bibliography`

The join key is already there. Rejected: bibliography is **public** and
describes what a source *is*; holdings describe what the founder personally
owns, where the file sits on disk, and its checksum — private operational
facts that do not belong in a public record. Mixing them would also push
acquisition metadata into `/sources/` on the site.

### Put holdings in `core`

Rejected for the coupling reason established in RFC 0002: the core records
meaning and research state, not operational inventory. A verification *finding*
belongs in a source note; the copy it was read from does not.

### Commit every file to LFS in the private repo

Simplest mental model, and the repo is already LFS-configured. Rejected as the
default: it grows storage and bandwidth cost without bound, makes clones
expensive for a corpus that is mostly metadata, and uploads purchased
in-copyright books to a third-party service for no research benefit the
checksum-plus-locator record does not already provide. Retained as an opt-in
per record for material the project may lawfully store that way.

## Risks, limitations, and dissent

- **Local-only files are not backed up by this design.** The registry records
  identity and integrity, not durability; backup remains the founder's
  arrangement. A checksum tells you a file is corrupt, not where to get
  another.
- **Registry drift.** Records can claim holdings that no longer exist on disk.
  The validator can only check the metadata; a `--verify-files` mode is
  possible where the payloads are present.
- **Access inflation.** Recording a holding creates pressure to claim a higher
  `access` level than was actually exercised. Owning a book is not reading it;
  `access` must continue to reflect what was inspected, and the verification
  log is per locator for exactly this reason.
- **Private/public asymmetry.** Contributors without access to the private repo
  cannot check a holding's basis. The public source note remains the citable
  artifact; the registry is corroboration, not the record of record.
- **The wantlist can distort research.** Ranking by claim-dependency counts
  favours sources that existing claims already lean on, which is not the same
  as the sources most likely to challenge them. Critical-role references should
  be weighted deliberately, not merely counted.

## Compatibility and migration

Additive and private. No public repository, page, URL, schema, badge, or
identifier changes. Existing `data-sources` contents and the digitization
pipeline are untouched. The registry starts effectively empty and grows as
holdings are recorded; absence of a record is never an error, exactly as an
unbound page is never an error under RFC 0002.

## Validation plan

- Scaffold the registry with the schema, the validator, and one factually
  grounded exemplar (`black-green-mesopotamia`, the one source whose
  inspection is already documented).
- Run the wantlist against the current four claims and confirm it reproduces
  the ten-reference backlog with sensible ranking.
- Record holdings for the founder's existing library, then check whether any
  core `access` level can be honestly upgraded. The first upgrade that changes
  an evidence map is the real validation of this RFC.

## Resolution

Accepted by the project founder on 2026-08-15. Recorded in
[ADR 0004](../decisions/0004-source-holdings-registry.md).

Two items in this RFC are explicitly *not* closed by that acceptance. The
`data-sources` licensing correction remains a separate founder decision, and
determining `licensing_status` for the sources that currently carry none is
follow-on work rather than a precondition.
