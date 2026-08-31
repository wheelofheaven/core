---
title: "Evidence map: the canonical contact report"
status: draft
version: 0.1.0
last_reviewed: 2026-08-17
claim_id: woh-claim-0070
---

# Evidence map: the canonical contact report

This map serves claim
[`woh-claim-0070`](../framework/canonical-contact-report.md). It carries the
subclaim-A rows formerly held by the
[`woh-claim-0001` map](woh-claim-0001-evidence.md), moved here when the
report layer was extracted into its own `source_report` record
([RFC 0006](../../rfcs/0006-split-canonical-contact-report.md)).

The claim is `scoped`. What this map weighs is the report layer itself —
whether the record accurately states what the source says, and how the
report should be read as a text — not whether the reported events occurred.
That question belongs to `woh-claim-0001` and its map.

Locators use Wheel `refId`s: `TBWTT` = *The Book Which Tells the Truth*
(project digitization).

**Quotation provenance.** The source-language column quotes the French base
text, which
[review 0001](../reviews/woh-claim-0070-review-0001.md) collated against the
2005 printed French edition and found faithful. English wordings are quoted
from the published English edition (*Intelligent Design*, 2005) with printed
page numbers. The project digitization's own English is an AI-assisted
rendering generated in 2026 and is never quoted here as the source's words;
where it is shown for comparison it is labelled as such.

## The report layer

| Passage / locator | Source-language observation | Canonical interpretation | Mainstream / alternative reading | Critical / source-history explanation | Dependency note |
| --- | --- | --- | --- | --- | --- |
| `TBWTT-1:53` | French base: « Nous sommes des hommes comme vous et nous vivons sur une planète assez semblable à la Terre » (2005 French ed., p. 18). Published English: "We are people like you, and we live on a planet similar to Earth" (*Intelligent Design*, p. 8). Qualified eight turns later at `TBWTT-1:61`, where a human could not live there because the atmosphere is very different. | The interlocutor is a biological being of an off-world human-like civilization. | The passage is a 1970s contact-narrative testimony; genre-typical of the era's UFO-contactee literature. | Source-critical accounts read the report as revelatory, literary, psychological, or fictional composition, not documentary. | Primary and sole basis for the report; not independent of the framework. |
| `TBWTT-2:5` | The source glosses `Elohim` as « ceux qui sont venus du ciel » / "those who came from the sky", insists the word is plural, and narrates scientists selecting Earth and creating artificial life (2005 French ed., p. 20; *Intelligent Design*, p. 11). | The biblical creators were this civilization's scientists; creation was a laboratory programme. | An etymological folk-gloss laid over Genesis; not a philological derivation of the Hebrew. | The gloss post-dates and depends on the Hebrew text it interprets; it is interpretation of Genesis, not an independent witness to it. | Depends on the Genesis text (see the `woh-claim-0001` map, subclaim B); the two are not independent sources. |

## Review status

The `woh-claim-0001` independence summary identifies source criticism of
this report as the load-bearing question of the foundational hypothesis.
For this record specifically, a reproducible review needs three components.
[Review 0001](../reviews/woh-claim-0070-review-0001.md) performed two of
them; the claim remains `scoped`.

- **Edition collation** — *performed*. The project digitization's French was
  collated against the 2005 printed French and English combined editions:
  583 of 634 paragraphs match exactly and no genuine textual variant was
  found. The digitization's French is faithful to the 2005 text. Not reached:
  the 1973 and 1974 first printings, of which no copy is held.
- **Genre and source-critical appraisal** — *outstanding*. Where the report
  sits within 1970s contactee literature, and which of the composition-account
  explanations (literary, revelatory, psychological, sociological, fictional,
  mistaken) best accounts for the text as a text. Blocked on access: Palmer's
  *Aliens Adored* and the other critical studies are not held.
- **Internal-consistency check** — *performed*. Later canon does not alter
  either passage, but book two explicitly corrects a different passage of the
  first message as "wrongly transcribed", so the report layer cannot be
  treated as a stable transcript merely because the printed editions agree.

None of these outcomes would by itself move `woh-claim-0001`: establishing
what the source says, and even why it says it, is separated by the claim
model from whether the reported events occurred.
