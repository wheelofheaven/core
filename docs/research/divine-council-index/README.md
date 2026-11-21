---
title: Divine-Council Index source audit
status: draft
version: 0.1.0
last_reviewed: 2026-11-21
---

# Divine-Council Index source audit

This research revision examines the seventeen rows of the public
Divine-Council Index 1.1 against named editions. It supplies 98
observations with individual references and evidence states, in the
manner of the [flood concordance audit](../flood-concordance/README.md).
It is a review draft. It changes no published dataset, page or claim
record.

## Files

- [Audit record](audit.json): source register (28 editions and
  translations, with inspected scope, access and limitations), one
  verdict per row, and one observation per row and field.
- [Observations](observations.csv): the same observations as a table:
  old value, proposed value, evidence state, locator, sources, note.
- [Baseline](baseline-1.1.json): the published 1.1 file from the API
  repository (commit `5c9b6a3`); its SHA-256 is recorded in the audit.

The unit is one attestation: a passage in an inspected edition. A row is
not a whole tradition.

## Findings by row

| Row | Verdict | Main finding |
| --- | --- | --- |
| Ugaritic, Baal Cycle | narrowed; core loci not checked | Only KTU 1.1 and 1.3 could be read in a line-numbered open edition. `pḫr mʿd` (KTU 1.2 I) and the seventy sons of Athirat (1.4 VI) remain unchecked. "puḫru môʿidi" is a modern vocalization the consonantal text cannot print. |
| Psalm 82 | corrected | Reference widened to 82:1–8. The terms are in the Masoretic text; their divine sense is a reading (JPS 1917: "congregation of God", "judges"). |
| 1 Kings 22 | unchanged | Every field attested, including deliberation ("one said… another said", 22:20). |
| Job 1–2 | corrected | 1:6–12; 2:1–7. There is no wager in the text: a challenge and a permission. "Accuser" is a gloss. |
| Deuteronomy 32:8–9 | corrected | The Masoretic text reads "children of Israel". "Sons of God" rests on 4QDeut^j and the Göttingen LXX, both reached only through secondary sources; the common LXX text reads "angels of God". "bənê ʾēl" is a reconstruction. "One over each nation" is inference. |
| Isaiah 6 | corrected | The seraphim stand above; they are not described as a council. "High and lifted up" describes the throne. "For us" (6:8) is attested; "council plural" is interpretation. |
| Enūma Eliš | corrected | The assembly does not grant the Tablet of Destinies (Tiamat gives it to Kingu; Marduk seizes it). It gives kingship, throne, sceptre and weapon. Reference narrowed to III–IV in King 1902; Tablet VI needs a modern edition. |
| Atrahasis | corrected | Anu is king and Enlil counsellor; Enlil convenes and speaks, but "presides" is not textual. The flood oath survives in a Middle Babylonian witness; Enki's pre-flood objection is restored; his explicit criticism follows the flood. |
| Book of the Watchers | corrected | "Lord of Spirits" belongs to the Similitudes (Charles p. 66) and is removed. "Great Glory" at 14:20. God "needed no counsellor" (14:22): a court, not a deliberating council. |
| Song of Emergence (CTH 344) | **withdrawal recommended** | The Mainz edition shows kingship passing by combat (Alalu → Anu → Kumarbi) and primeval gods invoked as listeners. No assembly or council. |
| Latter-day Saint | corrected | "Council in heaven" is not in Moses 4 or Abraham 3; it is a study-aid label. The nearest scripture is D&C 121:32, "the Council of the Eternal God of all other gods". "Debates" overstates an offer-and-choice scene. |
| Iliad 4 and 20 | corrected | The noun ἀγορή only at 20.4 and 20.16; Book 4 has the verb. Apollo not named; Athena silent. Book 4 ends in the truce broken, with Troy's sack conceded to Hera. |
| Contendings of Horus and Seth | corrected; weakly sourced | Checked only against an unattributed web translation. Geb not named; "eighty years" is the case's time before the tribunal; "c. 1147 BCE" has no traceable source. Needs Gardiner 1931 or Lichtheim. |
| Ovid, Metamorphoses 1 | corrected | *concilium* alone (1.167). The gods assent to destroying humankind (1.244–245) with grief and questions; Jupiter alone then chooses the flood (1.253–261). |
| Völuspá; Gylfaginning 14 | corrected | *rökstóla*, *regin*, *ginnheilög goð* confirmed at 6, 9, 23, 25 (Bellows: 6, 9, 24, 25). Neither translator says "seats of counsel". "Æsir" is inference. Allfather presides in Gylf. 14. |
| Enlil and Ninlil | corrected | The scene is in the Ki-ur (54–64), not the Ekur. *ukkin* and *Anuna* do not occur; "the fifty great gods and the seven gods who decide destinies" have Enlil arrested; no trial is narrated. |
| Mahābhārata, Ādiparvan | corrected | Ganguli XVII = critical edition 1.15.5–13. *devasabhā* does not occur; the text says the gods "assembled … began to deliberate". No presider is named. |

All `woh_library` links point at whole books, not passages. The Enūma
Eliš row can link the library's partial King 1902 text.

## Consequences for the published page

The page's inclusion rule says a row "depicts a deliberative assembly of
divine beings". Under inspection that rule fails for the *Song of
Emergence* (no assembly), Isaiah 6 (no council), and arguably the Book of
the Watchers (an explicit denial of counsel). A release should either
withdraw or reclassify those rows, or state a wider rule (assembly,
court or deliberation) and add a column that says which.

The page's reading section says the council "in the flood dataset, is
recorded deciding on the reset". Under `woh-claim-0010` 0.2.0 the
Council's decision is destruction; the reset is the outcome of its
circumvention. That sentence needs correcting regardless of the rows.

The same section reads the councils as "one and the same referent", the
Council of the Eternals. That is an identity claim. No record bound to
this page (`woh-claim-0011`, `woh-claim-0060`) states it; it should be
bound to a record that does, or reworded. This audit does not decide
which.

## Limits

- These are checks of inspected editions and translations, not new
  translations. Original-language terms were confirmed only where an
  inspected text prints them; otherwise they are `qualified`.
- Not inspected: KTU 1.2 and 1.4–1.6 in a line-numbered edition; DJD XIV
  (4QDeut^j); the Göttingen LXX apparatus; a modern Enūma Eliš edition
  (eBL did not respond); Gardiner 1931, Lichtheim and Wente for the
  Egyptian row; Hoffner's *Hittite Myths*; the Mahābhārata vulgate text
  Ganguli translated.
- Some sites refused automated requests (Perseus, sacred-texts,
  Mechon-Mamre); mirrors were used and are named in the source register.
- Two edition years are from memory and flagged: Magnus 1892, Guðni
  Jónsson 1949.
- Copies of Smith, Wyatt and Driver that appeared to be unauthorized
  uploads were not used.
- The sample was curated, not drawn. Coverage does not estimate how
  common divine councils are.

## Status

Not independently reviewed yet. No release, page or mirror change is
proposed until review and founder sign-off.
