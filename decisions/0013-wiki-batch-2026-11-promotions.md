---
title: "ADR 0013: Promotion of woh-claim-0074 to 0079, revisions to 0024, 0038 and 0048, and two founder directions"
status: accepted
date: 2026-11-08
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0003-artifact-derivation-contract.md
---

# ADR 0013: Promotion of woh-claim-0074 to 0079, revisions to 0024, 0038 and 0048, and two founder directions

## Context

On 2026-11-08 the site removed links to 133 wiki entries that published
pages referred to but nobody had written. The founder commissioned six of
the most-linked as new `/wiki/` entries under the RFC 0003 contract:
Buddha, Xenobiology, Tabernacle, Mecca, Joseph Smith and Hebrews.

Grounding against the catalog found existing coverage for part of each
entry. Six load-bearing gaps remained, and three accepted records were
found to be wrong or incomplete:

- `woh-claim-0024` listed Schumm and Goldstein as the critical source for
  the measurement objection, although their analysis finds the early
  orientations consistent with aiming at Petra under Gibson's assumptions.
  The principal critic, David A. King, was absent.
- `woh-claim-0048` described the canon's re-reading of the Buddhist cycle
  as individual recreation and excluded a re-description of liberation.
  ETTMTTP-2:24 applies the cycle "not to the individual but to humanity
  entire" and equates awakening with the golden age of civilizations.
- `woh-claim-0038` cited only TBWTT-5:54, omitting the second Message's
  table scene and lineage passage and the third book's lists.

The six new records were drafted at 0.1.0 and the three revisions made on
the same day. The founder answered four questions before drafting and
reviewed the drafts afterwards.

## Decision drivers

- Six new public pages should bind accepted records, not drafts.
- Two of the six entries required an identification or a weighting that
  the canon does not itself supply. Under `CLAUDE.md` those need explicit
  founder direction rather than an agent's inference.
- One entry (Hebrews) states canon claims about a living people; its
  record had to carry containment strong enough to travel with every
  derivative.

## Decision

The founder directed, on 2026-11-08:

1. **Promotion** of `woh-claim-0074` (the canon's biochemical layer),
   `0075` (the tent of meeting as the creators' residence), `0076` (Israel
   as the creators' chosen and descended people), `0077` (the canon's
   named messengers and their expected return), `0078` (the address to the
   traditions' expectations) and `0079` (LDS cosmology and the canon:
   resemblance), each at 0.1.0, from `draft` to `accepted`.
2. **Revisions** of `woh-claim-0024` to 0.1.1 (source roles corrected;
   King added as the critical source), `woh-claim-0038` to 0.1.1
   (locators only) and `woh-claim-0048` to 0.2.0 (statement and scope
   brought into line with ETTMTTP-2:24; the individual-recreation layer
   kept on its own passages).
3. **The Buddha identification.** The corpus identifies the canon's "the
   one whom, on Earth, one remembers under the name of Buddha"
   (ETTMTTP-2:64) with Siddhārtha Gautama (Śākyamuni). This is the
   corpus's identification, not the canon's, and `woh-claim-0077` records
   it as such. The name Maitreya is **not** adopted: the canon's "new
   Buddha … born in the West" (ETTMTTP-3:228) is carried in its own
   words, read in context as pointing at Raël (`woh-claim-0078`).
4. **The commentary-voice rule.** Raël's own commentary voice in *Let's
   Welcome the Extraterrestrials* (the reader questions he answers and
   his signed essays) is canon, and every use labels it as his commentary,
   distinct from the dictated Messages. Joseph Smith is therefore "named
   by Raël among the envoys" (LWTE-3:27). He has no seat at the table and
   no ordinal.

Also directed, as defaults for this batch: no record for a sequence of
reception sites from the Tabernacle to the Embassy; no glory-as-craft
reading at Exodus 40:34–38; no identification of Moroni or Kolob; no
forerunner classing of Joseph Smith; no record for the Abrahamic
restoration reading of Mecca; no census-tier record.

Unchanged by this decision: each record's public label, evidence status,
alternatives and revision triggers as drafted. Evidence maps keep `draft`
status as living research artifacts, per the ADR 0005 convention. The
title of `woh-claim-0048` is kept for continuity.

## Consequences

### Enables

- The six wiki entries can be written and published bound to accepted
  records.
- Live pages that misstate the canon can be corrected against a record:
  "genetic descendants" (`wiki/hebrew.md`, `wiki/hebrew-bible.md`), the
  ordinal prophets (`wiki/muhammad.md`), the Maitreya identification
  (`wiki/rael.md`) and "the level of DNA" (`wiki/life-engineering.md`).

### Costs and risks

- No Buddhist primary text is in the project library. The strongest
  objection to `woh-claim-0078` (that the classical Metteyya texts do not
  place the future Buddha in the West) is recorded but unchecked against
  the sutta.
- Several counter-sources lack registry ids (Haran, Homan, Ritner, the
  King Follett discourse, the Book of Moses). The alternatives that rely
  on them say so.
- The canon quotation at TBWTT-3:37 remains unlocated; no clause depends
  on it.
- `woh-claim-0076` carries canon statements about a living people. Its
  exclusions (no genetic, superiority or individual-worth claims; the
  canon's own « peut-être »; Deuteronomy 7:6–8 in its own voice) are
  conditions on every derivative, and prose that drifts past them is a
  revision trigger.

## Amendment (2026-11-08, after review)

Independent review of the six derived wiki entries found three wording
errors in the records promoted above. The founder directed wording-only
revisions to 0.1.1: `woh-claim-0074` (the dictated messages' one genetic
term, « gènes », is now stated), `woh-claim-0075` (locator TBWTT-3:32–33)
and `woh-claim-0076` (the LWTE-1:17–18 harmonization labelled as Raël's
commentary voice, applying decision 4). The founder also confirmed that the
Hebrews entry keeps the canon's "jealously" (ETTMTTP-2:124) inside the
custody clause.

## Amendment 2 (2026-11-08, source registration)

At the founder's direction the counter-sources named under "Costs and
risks" were registered and cited, as wording and source revisions with
no change to any statement, label, status or scope:

- `woh-claim-0078` to 0.1.1. The Buddhist primary-text check is done
  against the Pāli account, DN 26 in Bhikkhu Sujato's CC0 translation
  (`digha-nikaya-26-sujato`, full text). Metteyya arises in Ketumatī,
  the renamed Varanasi, and nothing places him in the West, so
  `alt-0078-no-western-birth` holds for that text. Later Buddhist
  literature is not checked. The exclusions (no Maitreya; no statement
  of what Buddhist scripture predicts) are unchanged.
- `woh-claim-0079` to 0.1.1. The Book of Moses (`book-of-moses`) and
  Ritner's edition of the papyri (`ritner-joseph-smith-egyptian-papyri`)
  are registered and cited.
- `woh-claim-0076` to 0.1.2. Kaminsky, Levenson and Novak are cited as
  scholarly context for the covenant-election alternative.
- `woh-claim-0075` to 0.1.2. Haran and Homan are cited. The TBWTT-3:37
  quotation is also uncited in the 1974 French edition, so the
  digitization is faithful; the Dhorme Exodus is still the open check.

Not registered: the King Follett discourse, because no verifiable
edition URL was found.

The same pass found "direct genetic descendants" in the Eden and Genesis
wiki entries (all ten languages). They are corrected to the 0076 wording
and now bind `woh-claim-0076`. The *Age of Cancer* timeline chapter still
argues a biological and cognitive basis for the "chosen people" clause,
which 0076 excludes. That is held for founder direction and is not edited
here.

## Validation and review

The catalog validates after the flip. Review this ADR when a Buddhist
primary source on the future Buddha is registered, when first printings
of the third book are collated (in particular whether later editions keep
the LWTE-3:27 list), or when the commentary-voice rule is revisited.

## References

- [The canon's biochemical layer](../docs/framework/canon-biochemical-layer.md)
- [The tent of meeting as the creators' residence](../docs/framework/tent-of-meeting-residence.md)
- [Israel as the creators' chosen and descended people](../docs/framework/israel-chosen-descended-people.md)
- [The canon's named messengers](../docs/framework/named-messengers-return.md)
- [The address to the traditions' expectations](../docs/framework/traditions-expectations-address.md)
- [LDS cosmology and the canon](../docs/framework/lds-cosmology-resemblance.md)
- [Source note: Let's Welcome the Extraterrestrials](../source-notes/lets-welcome-the-extraterrestrials.md)
- [ADR 0012](0012-dragons-passage-promotion.md) (promotion precedent)
