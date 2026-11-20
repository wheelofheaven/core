---
title: Flood concordance independent review
status: draft
version: 0.2.0
last_reviewed: 2026-11-20
---

# Flood concordance independent review

Verdict: all eleven rows and 88 observations pass source review at their
declared selected-source scope, after the corrections recorded below.
The five positive chronology entries also pass at their stated grades.
This is a bounded review of a research draft, not publication approval.

## Independence and coverage

The review read the concordance, baseline, CSV, validator and governing
records without the writer's README or reasoning narrative.
The first stage independently checked four rows and 32 cells against the
complete relevant cached passages and rendered source pages:

- Apollodorus, *Library* 1.7.2, Frazer's displayed translation.
- Molina, Markham 1873, pp. 4–5; printed p. 4 visually checked.
- Snorri, Brodeur 1916, *Gylfaginning* VII, p. 19, including its footnote.
- Gilgamesh XI, the identified Kovacs/Livius adaptation.

The four cached source hashes matched the source register. The remaining
56 cells were checked in the two subsequent stages described below.

## First-stage findings

Apollodorus supports the other mountain survivors and Zeus's stone-throwing
instruction. The legacy phrase about a mother's bones is absent from the
selected passage.

Molina supports the unnamed pair, box, place-name footnote and clay creation.
The inspected passage does not state a flood decree or a disobedience motive
for this flood. Narrowing the mixed row to this witness is justified.

Snorri supports the household/wife, blood inundation and giant ancestry.
Brodeur's footnote qualifies the ship rendering; uncertainty is appropriate.

Gilgamesh supports six decks forming seven levels and the referenced
decision, warning, birds, mountain and aftermath observations.
The draft's additional phrase about sealing with bitumen went beyond the
selected lines' explicit listing of construction supplies and plugs.

## First-stage correction applied

The vessel value now reads: “Equal-sided boat with six decks making seven
levels, divided into compartments.”
Its note records why listing bitumen as a supply was not treated as an
explicit statement of its sealing use.
The CSV was regenerated and the structural checker passed after this change.

## Second stage: five rows and 40 observations

The review independently inspected Genesis (Mechon-Mamre's JPS translation),
Qur’an 11 (Shakir/Livius), Berossus (Verbrugghe/Wickersham as adapted by
Livius), Śatapatha Brāhmaṇa (Eggeling via TITUS and Sacred Texts), and
Leyenda de los Soles (Velázquez, printed pp. 119–120).
All nine `not_stated` cells in this subset were justified within their cited
scopes. Six supplied cached-source hashes matched; the Manu sources were
also inspected directly online.

Two precision corrections were required and applied:

1. Genesis survivor now cites 8:18, the family's exit from the ark, alongside
   6:18, which concerns prospective boarding.
2. Manu's vessel now distinguishes the narrated attachment to the fish's
   horn from the instruction to fasten the ship to a tree.

The corrected Gilgamesh vessel wording was re-read and passed.

## Third stage: two rows and 16 observations

The Sumerian row was checked against its declared Jacobsen/Livius base,
Kramer 1963 pp. 163–164, and the Oxford ETCSL composite's gap structure.
Kramer expressly qualifies the identification of Enki. The Oxford composite
supports the cited gaps; it does not supply an inspected English translation.
The two damaged-text states remain justified. This review does not certify
the Livius adaptation against a complete printed Jacobsen edition.

The Atrahasis row was checked against SEAL I, II and the Sippar Tablet III
edition. The family, warning, retrospective collective oath, boat and door
bitumen, sacrifice and childbirth provisions are supported. Restored names
and damaged clauses are disclosed. The motivation summary is supported as a
sequence across a synoptic edition. The explicit flood oath at II G 49q–u
comes from X-MB; it is not represented as a preserved Sippar Tablet II passage.
The observations therefore retain the distinction between manuscript and
composite account.

All newly checked cached-source hashes matched the register. The previous
Genesis and Manu corrections were independently rechecked and passed.

## Chronology review and correction

Five positive entries were checked:

| Entry | Verified scope |
| --- | --- |
| Sumerian tablet, approximately 1650 BCE | Penn Museum's date for CBS10673; a physical-witness estimate. |
| Atrahasis, Ammī-ṣadūqa year 12 | SEAL's identification of a partly restored colophon formula. |
| Leyenda, 22 May 1558 | Date stated in the opening paragraph, not independent manuscript dating. |
| Molina, 1570–1584 | Markham's argument in introduction p. vii, explicitly attributed to that editor. |
| Norse manuscript dates | Brodeur's report in introduction p. xv, explicitly distinguished from a current census. |

One locator correction was required: the Atrahasis colophon belongs to
**C2** viii 26′–31′ in SEAL's transliteration. The draft had assigned it to C1.
This was corrected, and the partly restored basis of the year identification
was made explicit.

The generic null-composition note was also clarified: no independently
verified composition date is assigned, and inherited dating text remains
only in `legacy_date`. This avoids calling the Leyenda's old manuscript label
a composition estimate.

The remaining 39 chronology fields are marked unreassessed, unestablished,
unaudited or unassigned. Their null values are honest limits, not verified
negative assertions. Both CSV exports were regenerated after the fixes.

## Binding and limits

Claims 0010 and 0060 permit registering these textual features and divergences.
The reviewed rows do not establish a shared historical event, a universal
procedure, or independent attestations.
Source verification now covers all 88 observations. It does not establish
translation accuracy through original-language collation, a current manuscript
census, a complete composition chronology, or a newly demonstrated
Mesopotamian/Biblical transmission route. Multiple representations of the
same textual stream do not become independent evidence through review.

## Local publication projection review

The version 1.2 page, API JSON, account CSV, observations CSV and chronology
CSV were independently compared with the research record. All 88 observation
values, states, notes and locators, all 44 chronology fields, source
limitations and relationship records were preserved. The first thirteen
account columns retain their order. Site and API downloads matched byte for
byte. The public prose stays within claims 0010/0060 at version 0.1.0 and
discloses the changed `approx_date` and unknown-value semantics.

One metadata omission was found: the exported chronology policy referred to
`edition_source_ids`, but exported rows did not include it. The generator now
copies that field, and a focused export check requires valid source IDs on
every row. Source-access wording was also edited to remove tool-specific
details while preserving which text was inspected.

Projection drift checks and the three focused export/packaging tests pass.
The API and English site build; documentation checks pass with external links
excluded. The generated HTML contains eleven account disclosures, 88 evidence
states and four download links with versioned Dataset JSON-LD. Browser visual
inspection was unavailable because the computer-use connection could not be
opened. The broader core validator still reports its existing 27 errors;
this projection is not a claim that the whole repository passes validation.
External mirrors and production deployment were not inspected or changed.
