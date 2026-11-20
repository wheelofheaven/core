---
title: Flood concordance source audit
status: draft
version: 0.2.0
last_reviewed: 2026-11-20
---

# Flood concordance source audit

This research revision examines the eleven accounts in the public v1.1
Flood-Myth Concordance against named source representations.
It supplies 88 observations with individual references, records corrections,
and separates textual silence from damaged text and incomplete checking.
It is a review draft, not a replacement production release.

## Files and scope

- [Concordance and source register](concordance.json): the editable research
  record, with edition information, inspected scopes, qualifications,
  relationship records and separately qualified chronology records.
- [Observations](observations.csv): one row per field, with the old value,
  proposed value, evidence state, passage locator and source URL.
- [Chronology](chronology.csv): composition, physical witness, internal
  textual date and historical event date kept in distinct fields. Translation
  and edition provenance remain in the source register.
- [Baseline](baseline-1.1.json): the unmodified API working-copy dataset used
  for comparison; its SHA-256 is recorded in the concordance.
- [Independent review](review.md): source verification and the corrections
  arising from each review stage, with explicit coverage and limitations.

The unit is a textual account in a particular inspected representation.
It is not an entire culture, an independent historical event, or an assertion
that a tradition's every surviving version agrees with this account.
The eleven existing IDs are retained to make changes traceable.
The Andean ID now denotes the inspected Molina account; the older combined
Betanzos/Molina summary is preserved only in the baseline.

## What changed under inspection

| Account | Finding | Proposed treatment |
| --- | --- | --- |
| Sumerian Flood Story | The web presentation supplies narrative explanations inside lacunae and names the warning voice in a heading. Kramer calls the identification probable; Oxford's composite explicitly marks the gaps. | Retain the qualified attribution to Enki and distinguish the surviving text from editorial reconstruction. |
| Atrahasis | The SEAL editions distinguish noise, disease, deprivation and the later flood. Tablet III recalls the collective oath and has Enki address Nintu. | Cite the sequence by tablet and segment, disclose the mixed manuscript basis, and qualify restored words. |
| Gilgamesh XI | The selected translation specifies six decks forming seven levels. | Correct the seven-decked summary; retain exact locators for boat, birds and landing. |
| Genesis | The names and narrative functions vary by passage; the bow covenant follows the flood. | Cite the decision, instructions, birds and covenant separately; avoid treating a later promise as a prior oath to destroy. |
| Qur’an | Surah 11 supplies a bounded account with a named landing place and an excluded son. | Identify the inspected surah and verses instead of implying that three whole surahs were audited. |
| Apollodorus | 1.7.2 includes other mountain survivors and Zeus's instruction to throw stones. It does not contain the legacy phrase about a mother's bones. | Restore the other survivors and remove the unattributed phrase. |
| Berossus | Cronus predicts the disaster; the excerpt does not explicitly assign him its decree. | Separate warning from decreeing, and preserve the indirect transmission through Syncellus. |
| Śatapatha Brāhmaṇa | A fish warns Manu; no flood decreer is named in 1.8.1.1–6. The slope is Manu's descent. Fastening the ship to a tree is an instruction. | Remove later divine identifications, correct the descent label, and distinguish the instruction from a narrated action. |
| Leyenda de los Soles | Velázquez has Tata and Nene, warned by Titlacahuan. The episode does not separately state a decree by him. | Preserve edition-specific names and distinguish the warning from an attributed decree. |
| Molina | Markham p. 4 describes a box and clay figures; the combined old row adds sealed construction, stone creation and a giant-disobedience cause. | Narrow to Molina; retain Markham's place-name footnote; do not fill the missing cause from another episode or author. |
| Snorri | Brodeur translates the object as a ship but glosses it as a mill-bench or mortar. | Preserve that translation problem; withdraw the unqualified hollow-tree-trunk gloss. |

The JSON and CSV give the exact references for these findings.
These are observations about inspected editions, not new translations of
Sumerian, Akkadian, Greek, Sanskrit, Nahuatl or Old Norse.

## How to read the evidence states

`attested` means that the selected representation states the feature.
It does not establish that the event occurred.
`not_stated` means silence within the declared scope, not absence throughout
a tradition.
`text_damaged` means that lacunae or missing portions obstruct the question;
it does not claim that the missing lines once contained the feature.
`uncertain` preserves a translation or attribution qualification.
`not_checked` means the necessary source passage was not inspected.
`explicitly_absent` is reserved for an actual textual denial and requires a
locator; no current observation uses it.

An empty CSV value must always be read with its state and note.
Do not turn empty values into false/zero, or count `not_stated` as a denial.
The source register separates the edition from its host and declares adapted
web excerpts as adapted excerpts.
Print pages were visually checked for Molina p. 4, Brodeur p. 19 and
Velázquez p. 120, and for the added checks in Kramer p. 163,
Molina's introduction p. vii and Brodeur's introduction p. xv.
PDF leaf numbers are also recorded.
The SEAL editions supply a critical apparatus for the inspected Atrahasis
passages; no complete printed critical edition or manuscript collation is
claimed. Oxford's English Sumerian translation could not be retrieved, so
the row still identifies the Jacobsen/Livius adaptation as its base.
The Oxford composite checks gap structure; Kramer's synopsis supports a
qualified speaker identification. Neither is presented as a newly inspected
line-by-line English edition.
Downloaded source text is not redistributed in this research package.

## What the dates now mean

The original date strings remain in `legacy_date` for comparison. They
are not endorsed by their continued presence. Every row now distinguishes
composition, physical witness, internal textual date and historical event.
Unverified estimates have no positive value in those reviewed fields.

Five positive entries have bounded support:

- The Penn Museum dates CBS10673 to approximately 1650 BCE. This dates
  a Sumerian tablet, not the composition.
- SEAL identifies Ammī-ṣadūqa's twelfth year from the partly restored
  Sippar Atrahasis III colophon (C2 viii 26′–31′).
  No absolute BCE conversion or composition date is inferred from it.
- The Leyenda opens with 22 May 1558. This is a date stated by the text,
  not independent evidence for the age of the surviving copy.
- Markham's introduction places Molina's report between 1570 and 1584.
  The record attributes that estimate to the 1873 editor; modern dating
  scholarship has not been adjudicated.
- Brodeur's introduction reports dates around 1300 and in the fourteenth
  century for named Edda manuscripts. This remains a report from the
  selected editor, not a current census or a date for the quoted verse.

Exact references are in the chronology export. Ten composition dates remain
unreassessed; the Molina estimate is qualified as above. Unknown values do
not invalidate the textual observations, but must not be used to sort these
accounts into a demonstrated historical sequence. No flood-event date is
assigned.

## Relationship and independence controls

The Mesopotamian/Biblical stream remains an inherited position from the
existing core records, explicitly marked as not independently reassessed
by this audit.
It is not a newly demonstrated linear genealogy.
Berossus's indirect preservation and Snorri's quotation inside his prose
receive separate relationship records.
The two passages in the Noah/Nuh comparison are not assigned a direct
borrowing route merely because they concern the same narrative figure.
No listed relationship does not mean independence: all unrecorded pairwise
relationships remain unassessed.

The original sample was curated, not randomly drawn.
Its selection rule favors accounts with enough comparable features to fill
columns, so neither coverage nor the fraction of filled cells estimates
how widespread a pattern is among all flood traditions.
This revision tests the existing sample; it does not add traditions.

## Grounding and implications for core

The governing records are
[`woh-claim-0010` version 0.1.0](../../../model/claims/woh-claim-0010.json)
and [`woh-claim-0060` version 0.1.0](../../../model/claims/woh-claim-0060.json),
with their controlling specifications and evidence maps inspected.
The former distinguishes the comparative procedural reading from the
canonical reset reading; the latter requires registration without treating
row count as evidence.
The revision implements these existing boundaries.
Its individual textual observations are source checks, not new cross-tradition
identity claims.
No claim proposition has been created, promoted or revised. The local
publication integration aligns 0010's controlling document with its existing
dataset registration; both governing versions remain 0.1.0.

The material warrants a further focused review of 0010's procedural wording.
Warning is not identical to dissent, a cause is not identical to a decree,
and a promise after the event is not the same feature as an oath before it.
The existing evidence map already records missing dissent in Genesis and
Watchers, but its overall convergence sentence can obscure those differences.
Do not treat this table as demonstrating the complete procedural sequence
in every row, or use the canonical reading to fill textual gaps.
The canonical account has not been recoded or tested as a historical event here.

## Scope and publication handoff

This revision retains eleven account IDs. Betanzos and a separately
inspected Vafþrúðnismál belong in future, independently sourced rows;
their details must not return through the existing Molina or Snorri cells.
The revised table can retain unresolved dates and the Sumerian edition
limitation, provided these qualifications travel with the data.

The local publication candidate now adapts the API JSON and CSV, the dataset
landing page and distribution packages together. It preserves per-cell
references and evidence states, including in exports; an empty value alone
is insufficient. The research JSON remains distinct from the production
format. Related Myth Index flood summaries have also been reconciled;
their other families and motif classifications were not reassessed.

Version 1.2 is generated by
`api.wheelofheaven.world/scripts/build_flood_concordance.py`. It writes four
API downloads, identical files in `www.wheelofheaven.world/static/datasets/`,
and the account/source portion of the page in the www content checkout.
The surrounding prose is hand-edited. Its `--check` mode detects drift.
The original thirteen account columns are retained; evidence columns are
appended. There are separate observation and chronology CSVs, and the JSON
retains the complete source and relationship records.

Hugging Face and Kaggle packages for the concordance and the corrected Myth
Index have been regenerated locally. Mirror uploads are a separate release action. Full external-link checking
and visual browser inspection are not certified by this handoff.
The git release includes content and theme changes before advancing the
consumer repositories' submodule pins, including the API's separate content
checkout. This keeps its generated wiki cross-link aligned with the site.

A stronger composition chronology and a line-by-line check of an identified
Sumerian English edition remain research extensions. No claim record is
promoted or revised by this handoff.

## Reproduction and validation

From `core/`:

```sh
python3 scripts/research/check_flood_concordance.py
python3 scripts/research/check_flood_concordance.py --write
```

The first command validates IDs, states, locators, source references,
chronology distinctions, governing versions and the baseline digest, and
checks that both CSV exports match the editable JSON.
The second regenerates both exports after the same validation.
It has no network dependency and does not touch production datasets.
Structural validation does not verify the truth of a historical claim or
the accuracy of a translation.

Checks on 2026-11-20: the audit validator passed with 62 attested,
20 not-stated, four damaged and two uncertain observations. No observation
remains in the not-checked state. This concerns the eight textual fields,
not the unresolved composition dates.
The baseline JSON matched the independently downloaded live v1.1 dataset.
Core document metadata, local links and whitespace checks passed.
The full core validator still reports the same 27 pre-existing registry and
page-version errors (nine unknown source IDs and eighteen derivative-version
mismatches), plus the optional missing `jsonschema` warning.
None concerns this audit's new files; the repository-wide check is not green.

## Editorial verdict

The research revision supplies a reproducible basis for a publication change,
with all eleven rows and 88 observations independently checked at their
declared selected-source scope. The five positive chronology entries were
also checked; 39 chronology fields remain explicitly unresolved or unassigned.
The source-review verdict and its corrections are recorded separately.
Publication must carry the uncertainty, edition scopes and chronology
qualifications; the table supplies no new historical validation of the
canonical reset reading.
