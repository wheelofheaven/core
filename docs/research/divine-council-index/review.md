# Independent review: Divine-Council Index source audit (draft 0.1.0)

Reviewed 2026-11-21 against the sources named in `audit.json`, re-fetched for this review.
Downloads are kept in `scratchpad/dci/src/`.
No audit or repository file was edited.

## Overall verdict: **pass with corrections**

All ten high-impact findings hold against the sources. That includes the withdrawal recommendation for the Song of Emergence.
No proposed value was found to be wrong in a way that reverses a finding.
Some notes and justifications need correcting, though:

- One speaker attribution in Atrahasis goes against the edition's own commentary.
- One justification for Isaiah 6 rests on the accents, and the accents do not support it.
- The LXX reading of Deut 32:9 is misdescribed.
- One quotation in the Ugaritic row is attributed to the wrong restoration.
- The Egyptian row has a coverage gap that can be fixed. Gardiner 1931, which the audit says it could not open, is freely hosted by the Chester Beatty Library. It settles several of the `qualified` values.
- The README overstates coverage in one place: it says "one observation per row and field", but 21 row-field cells have no observation.

Integrity checks passed:

- The baseline SHA-256 matches (`53fcb667…4168`).
- All 98 `old_value`s equal the baseline.
- `observations.csv` matches `audit.json` field for field.
- All `source_keys` resolve to the register. Four register entries are never cited as a key, but they are referred to in notes: murray-iliad, bellows-edda, more-met, ugt-ktu3-corr.

## Items checked

Obs numbers are indexes into `audit.json` `observations` (0-based).
A = agree, D = disagree, P = partly agree.

### High-impact findings

| # | Row / field | Audit claim | Reviewer finding | Source + locator | A/D |
|---|---|---|---|---|---|
| 55–60 + verdict | Song of Emergence, all; `withdraw_recommended` | No assembly or council. Primeval gods invoked as listeners. Kingship passes by combat. | Confirmed. The German translation has no assembly or council term. §1–2 is a proem ("mögen zuhören"). §2–4: Alalu, then Anu, then Kumarbi, each by combat ("lieferte … einen Kampf"). §19'' has only a fragmentary "wir vernichten" and "Mach [ … ] zum König!" with no speakers or setting. The exemplar view confirms running line 9 = A Vs. I 8 and running line 25 = A Vs. I 18, and that karuiliyaš DINGIR.MEŠ-iš is printed at Vs. I 1–2. | hethport.net CTH 344 TRde 2009-08-31 §§1–4, 18''–20''; Expl. A view | A |
| 53 | Watchers, presiding_figure | "Lord of Spirits" is Similitudes-only (Charles p. 66). "Great Glory" is at 14:20. | Confirmed. p. 66: "Names of God found only in 37-71: 'Lord of Spirits' (passim)". 14:20: "the Great Glory sat thereon" (p. 34). | Charles 1912, pp. 34, 66 (PDF pp. 146, 178) | A |
| 52, 55 | Watchers, council_term / function | 14:22 "He needed no counsellor". | Confirmed. The sentence runs across pp. 34–35. Charles's note to 14:22 reads: "He needed no counsellor … As it stands it = 'He needed no counsel'". 14:23, "the most holy ones who were nigh to Him", supports the members field. | Charles 1912, pp. 34–35 and note | A |
| 26 | Deut 32, council_term | MT בני ישראל. 4QDeut^j "sons of God" (via Hendel). Göttingen LXX υἱῶν θεοῦ (reported). Common LXX ἀγγέλων θεοῦ. "bənê ʾēl" is a reconstruction. | Confirmed on every point. MAM: לְמִסְפַּ֖ר בְּנֵ֥י יִשְׂרָאֵֽל, and JPS 1917 "children of Israel". Ellopos prints κατὰ ἀριθμὸν ἀγγέλων Θεοῦ. The BAS sidebar says 4QDeut^j reads "Sons of God" (Symbol-font garble µyhwla ynb = בני אלוהים). Second secondary source, not in the audit: E. Tov, TheTorah.com (2023), notes that "Wevers daringly includes this reading in the critical text" (Septuaginta III.2, 1977). Tov also names MS 848 = P. Fouad Inv. 266, and calls בני אל a possible earlier form, so "bənê ʾēl" is a conjecture. The Göttingen page number (p. 347) is still not seen by anyone. One register note: the BAS sidebar speaks *about* Hendel in the third person, so its author is the BAR editors, not Hendel. | Sefaria MAM / JPS Deut 32:8; ellopos Deut 32:8; library.biblicalarchaeology.org/sidebar/deuteronomy-328/; thetorah.com/article/the-sons-of-israel-or-god-deuteronomy-32-8 (notes) | A (register attribution P) |
| 28 | Deut 32, members | "Jacob (MT) / Israel (LXX v.9)" | The LXX names **both**: λαὸς αὐτοῦ Ἰακώβ, σχοίνισμα κληρονομίας αὐτοῦ Ἰσραήλ. Under MT there are no divine members, and "one over each nation" is inference: agreed. | ellopos Deut 32:9 | P |
| 40 | Enūma Eliš, function | The assembly does not grant the Tablet of Destinies. Tiamat gives it to Kingu; Marduk seizes it. | Confirmed. King I c.137: "She gave him the Tablets of Destiny". IV c.121, p. 75: "He took from him the Tablets of Destiny". IV 14: "We give thee sovereignty over the whole world". IV 28–31: "Marduk is king!", sceptre, throne and ring, invincible weapon. III 129–138: the great gods "who decree [fate]" enter before Anšar and decree Marduk's fate. | King 1902 (archive.org djvu text) pp. 57, 75 and Tablet IV opening | A |
| 37, 39 | Enūma Eliš, council_term / members | puḫru at IV 15. Igigi lament III 126. Great gods III 130. | Line numbers confirmed in King's numbering (III 125 Laḫmu/Laḫamu, 126 Igigi, 130 great gods, 131 before Anšar). At IV 15 the OCR prints i-na pu-hur(?), and King renders it "Sit thou down in might". "ina puḫri" is the auditor's normalisation. | King 1902 III 123–138; IV 1–16 | A |
| 87–91 | Enlil & Ninlil | Ki-ur, not Ekur (54–64). No ukkin or Anuna. "Fifty great gods / seven gods who decide destinies". No trial narrated. | Confirmed. The composite has ki-ur3-ra at 54, 55 and 58. e2-kur occurs only at 37, in Nuska's title. A whole-file search finds no ukkin and no a-nun. 56–57 read dijir gal-gal 50-ne-ne / dijir nam-tar-ra 7-na-ne-ne. **But** the note to obs 91 says "At Nippur … goes beyond the text". The composition opens "Nibru was the city" (1–12), and Enlil "left the city" (59–60), so *at Nippur* **is** supported. Also, two manuscripts carry the imperative "leave the city!", which comes close to a banishment order. The proposed value itself is fine; the note overstates. | ETCSL tr121 1–12, 35–64; c121 37, 53–63 | A (note on obs 91: D) |
| 81, 79 | Ovid, function / reference | The gods assent to destruction (244–245). They grieve and ask questions (246–249). Jupiter alone chooses the flood (253–261). | Confirmed verbatim: *Dicta Iovis pars voce probant … alii partes adsensibus inplent* (244–245); *poena placet diversa, genus mortale sub undis perdere* (260–261). Also confirmed: *conciliumque vocat* (167), *plebs habitat diversa locis* (173), the semidei etc. outside heaven (192–195). Two small points. First, the obs 78 note says "'deorum' … does not occur at the passage", but *deorum* does occur at 1.171 (*deorum atria nobilium*), just not with *concilium*. Second, the TEI header does give Magnus 1892 (cert="low"), against the register's "TEI header not checked". | Perseus phi0959.phi006.perseus-lat2, Met. 1.163–262 | A (two wording fixes) |
| 69–71 | Iliad, members / function / term | Apollo absent. Athena silent. ἀγορή only at 20.4 and 20.16; Book 4 has ἠγορόωντο. | Confirmed. Apollo is not named in 4.1–72 or 20.1–32. 4.22: Ἀθηναίη ἀκέων ἦν οὐδέ τι εἶπε (Murray: "held her peace"). 4.37: ἕρξον ὅπως ἐθέλεις. 4.64–67: Hera proposes the oath-breaking. 20.4 / 20.16: θεοὺς ἀγορὴν. 20.7–8: rivers except Oceanus, and nymphs. One wording point: the README's "Book 4 ends in the truce broken" should say the *assembly* ends with Athena sent to provoke the breach. The breach itself (Pandarus) comes later in Book 4, outside 4.1–72. | Perseus grc2 and eng3 TEI | A |
| 93–97 | Mahābhārata | Ganguli XVII = CE 1.15.5–13. No devasabhā/sabhā. mantrayitum … samāgamya. No presider. | Confirmed. CE 1.15.9–13 is read in full. There is no sabhā. Nārāyaṇa addresses Brahmā (1.15.11). Ganguli XVII (p. 78): "held a conclave", "the celestial assembly". XVIII (pp. 79–81): "Vishnu and Brahma who were sitting". One correction: the obs 95 note says "Brahmā presides only in a rejected starred line (*262)". That line says only that the gods and daityas **approached** Brahmā (*brahmāṇam upatasthire*). It does not say he presides. | GRETIL mbh_01_u 1.15.1–1.16.4; Wikisource Ganguli §§17–18 | A (one note fix) |
| 62, 65 | LDS, council_term / function | "Council" is absent from Moses 4 and Abraham 3. D&C 121:32 is the nearest scripture. Offer and choice, not debate. | Confirmed. The verse text of Moses 4 and Abr 3 never says "council". "Council in Heaven" appears once per chapter, only in the Topical Guide footnote apparatus. D&C 121:32 is as quoted. Abr 3:27: "Whom shall I send? … I will send the first". **Addition:** Abr 4:26, "the Gods took counsel among themselves", is scriptural deliberation language close to the scene. The audit lists Abr 4–5 as not inspected; this verse should be noted in the row. | churchofjesuschrist.org Moses 4, Abr 3, Abr 4, D&C 121 | A (+ addition) |
| 32 | Isaiah 6, council_term | Seraphim stand "above him", not "before the throne". No council term. | Confirmed: שְׂרָפִ֨ים עֹמְדִ֤ים מִמַּ֙עַל֙ ל֔וֹ, and JPS 1917 "Above Him stood the seraphim". | Sefaria MAM / JPS Isa 6:2 | A |
| 33 | Isaiah 6, presiding_figure | "High and lifted up" qualifies the throne "in JPS 1917 and the accents". | The state is fine; the justification is not. In MAM the throne word כִּסֵּ֖א carries tipcha, a disjunctive accent, and רָ֣ם (munach) is joined to וְנִשָּׂ֑א (atnach). On my reading the accents group רָם וְנִשָּׂא as its own phrase rather than binding it to the throne. The better argument is agreement: the indefinite adjectives follow the indefinite כִּסֵּא, while אֲדֹנָי is definite. JPS English is consistent with "throne". Drop "and the accents", or replace it with the agreement argument. Keep `qualified`. | Sefaria MAM Isa 6:1 | P |
| 35 | Isaiah 6, function | לָנוּ attested; "council plural" is interpretation. | Confirmed (6:8 וּמִ֣י יֵֽלֶךְ־לָ֑נוּ). | MAM Isa 6:8 | A |

### Other non-attested observations re-checked

| # | Row / field | Audit claim | Reviewer finding | Source + locator | A/D |
|---|---|---|---|---|---|
| 0–1 | Baal Cycle, reference / term | 1.2 I not inspected. pḫr appears only in Smith's restoration at 1.1 IV 3. Steinberger "notes Smith's restoration lp[ḫr.il] as 'only a guess' (n. 9)". | Line 3 is confirmed: lrḥqm . lp[x…]. But in n. 9 the words "only a guess" are **Smith's** own, and they refer to **qb[ṣ]** in l. 2 ("Most tentatively qb[ṣ] has been reconstructed … but this is only a guess"). Smith prints lp[ḫr.il. (?)] with a query. Reword the note. | Steinberger KTU 1.1, IV 2–3 and n. 9 | P |
| 2, 4 | Baal Cycle, presider / function | El speaks and names Yw (IV 13–14). Throne clause at l. 24 is reconstruction. | Confirmed: 13 wyˁn . l⸢ṭp⸣n . il . d⸢p⸣[id]; 14 šm . bny . yw; 24 gršnn . l⸢k⸣[si . mlkh …] in the reconstruction column. | KTU 1.1 IV 4–24 | A |
| 3 | Baal Cycle, members | 1.3 V 3–4 kilm // kbn . aṯrt. | Confirmed: l. 4 [wḥẓ]⸢r⸣ . kbn . aṯrt. Seventy is not seen. 1.3 V 18 has bn . ilm only in the reconstruction column. | Steinberger KTU 1.3 V 4, 18 | A |
| 8, 10 | Ps 82, term / members | ʿădat-ʾēl; JPS "congregation of God", "judges", "godlike beings". | Confirmed. | MAM / JPS Ps 82:1, 6–7 | A |
| 22–23 | Job, members / function | "Accuser" is a gloss. No wager: challenge (1:9–11) and permission (1:12). | Confirmed. JPS renders the word as a name, "Satan". 1:12 / 2:6 give permission. The source note "2:2-7 checked in JPS 1917 only" is unnecessary: MAM serves 2:1–7. | MAM / JPS Job 1:6–12, 2:1–7 | A |
| 29 | Deut 32, function | Allotment depends on the variant. | Agree. | as above | A |
| 44 | Atrahasis, presiding | Anu king; Enlil counsellor, convenes; "presides" not textual. | Confirmed: I 7–8 "Anu, their father, was the king, their counsellor was the warrior Enlil"; I 101–104; II A 5 var., E 67; G 49q–u. **Omitted:** SEAL's commentary to I 8 says "As Enlil is usually the king of the gods, it is not excluded that the scribe plays with the word *malku* 'ruler'". The note should cite this. It qualifies the "not textual" claim. | SEAL Atra I, translation and commentary to l. 8 | P |
| 45 | Atrahasis, members | H 9–10: someone, "apparently Enlil since G 94 introduces his speech", proposes to bind Enki. | **Disagree.** SEAL's commentary to Segment H says: "These lines repeat in part Mama's speech in tablet I 240–243a. We assume that here too Mama is the speaker. Note that Ea/Enki's answer in Seg. H 11ff. is to the assembly of the gods." The audit should report the editors' attribution (Mama) or call the speaker unresolved, not Enlil. Also, H 13–16 is preserved in B vii 7–10 and partly in C0 iii 1–4. Only H 9–10 is substantially restored (D vii 9–10), so "heavily restored" overstates for 13–16. | SEAL Atra II Seg. H transliteration and commentary | D |
| 46 | Atrahasis, function | Flood oath in the MB witness (G 49q–u). Post-flood criticism at III vi 18–26. | G 49q–u is confirmed in X-MB. Two points need adding. First, the plague section already has the gods taking an oath (II E 11–12 // E 29–30, LB be / NA Q-NA), and Enlil's "All we, great Anunnaku, initiated a joint oath-taking" (G 28–29). So the procedure of deciding on oath is attested outside the MB witness, even though the flood-specific oath is MB. Second, the key words of III vi 20–22, "[how did you bring] the Flood [without deliberation?]", are restored. The audit flags restoration for H but not here. | SEAL Atra II Seg. E, G; SEAL Atra III C1 vi 7–27 | P |
| 47 | Atrahasis, woh_library | Project locators do not align with SEAL. | Not re-checked. | n/a | not checked |
| 50, 54 | Watchers, reference / function | chs 9–10, 12–16; archangels 9:1. | Confirmed: 9:1 "Michael, Uriel, Raphael, and Gabriel"; 10:1 "the Most High, the Holy and Great One"; 15:2 "Watchers of heaven" (half-bracketed). | Charles 1912 pp. 20–37 | A |
| 56–58 | CTH 344, presider / members / function | No presider. Throne-and-cupbearer pattern. | Confirmed (§§2–4). | hethport | A |
| 67 | Iliad, council_term | θόωκος absent. | Confirmed in the ranges read. | Monro TEI | A |
| 71–75 | Contendings, reference / term / presider / members | Gardiner, Lichtheim and Simpson "could not be opened". c. 1147 is uncited Wikipedia. Geb not named. psḏt unconfirmed. | **Gardiner 1931 is openly hosted** at chesterbeatty.ie (the PDF linked from the Wikipedia article's references). It gives: (a) date "fixes this down to [Ramesses V's] brief reign … roughly dated to 1160 B.C." (ch. I §1), so it supports 20th Dynasty / Ramesses V and does **not** support "c. 1147"; (b) eighty years "before the tribunal (2, 13; 13, 12)" (p. 12 n. 1); (c) presider rendered "the Master of the Universe" (not "Lord of All"; the web text's "Universal Lord" is a different rendering), with "The sun-god is conceived of as standing outside [the Ennead]" (p. 14 n. 3); (d) "'Ennead' is the accepted English equivalent of the Egyptian *psḏt*" and "In our tale the Ennead is a few times named 'the great Ennead'" (p. 14 n. 3); (e) Geb appears only in that note's list of the Heliopolitan Ennead. The audit's conclusions are therefore right, and they can now rest on a named edition with page/line locators. The Wikipedia statement is accurately described (infobox "c. 1147 BC", no citation). The audit's count of "the Ennead" (47) could not be reproduced: I count 57 "Ennead" strings, including "Great Ennead" and the glossary. This is cosmetic. | chesterbeatty.ie Gardiner 1931 PDF; Wayback reshafim page; en.wikipedia raw | A on substance; D on "could not be opened" |
| 73 | Contendings, source_text (`not_checked`) | No edition opened. | Can now be `attested` from Gardiner 1931 (title page; ch. I). | Gardiner 1931 | correction |
| 82, 85–86 | Norse, reference / members / function | Refrain at Vsp 6, 9, 23, 25 (GJ). Bellows 6, 9, 24, 25. St. 23 is tribute; st. 25 Óðs mey. | Confirmed. Heimskringla prints the refrain at 6, 9, 23 and 25. Bellows numbers them 6, 9, 24, 25 and translates "assembly-seats … and council held". The page carries the category "Guðni Jónsson", which supports the attribution (but not the year). | heimskringla.no Völuspá; Bellows OCR pp. 4–10 | A |
| 92 | Enlil & Ninlil, members | "Seven Anunna" not in text. | Confirmed (c121 57). | ETCSL | A |

### Spot-checks of `attested` observations (locator accuracy)

| # | Row / field | Locator | Finding | A/D |
|---|---|---|---|---|
| 6 | Ps 82 reference | 82:1–8 | Correct | A |
| 12–17 | 1 Kgs 22, all six | 22:19–23 | All correct. "kol" is printed. "one said … another said" is at v.20. | A |
| 18 | Job reference | 1:6–12; 2:1–7 | Correct | A |
| 20 | Job council_term | 1:6; 2:1 | בְּנֵ֣י הָאֱלֹהִ֔ים in both verses | A |
| 27 | Deut presiding | 32:8 | בְּהַנְחֵ֤ל עֶלְיוֹן֙ | A |
| 34 | Isa members | 6:2, 6 | Correct | A |
| 43 | Atrahasis council_term | I 218; II G 64/66; G 49r | I 218 *i-na pu-úḫ-ri i-pu-lu a-an-na* and G 64/66 *ana puḫrim ša ilī* are printed. The G 49r translation "in the assembly of all the gods" is confirmed. Witness-line sigla (A iv 10 etc.) were not individually checked. | A |
| 52 | Watchers members | 9:1; 15:2–3 | Correct | A |
| 54 | CTH 344 reference | A Vs. I 1–7, 8; line 25 = Vs. I 18 | Correct (exemplar view) | A |
| 63–64 | LDS presiding / members | Abr 3:22–24, 27; Moses 4:1–2 | Correct | A |
| 66, 68 | Iliad reference / presiding | 4.1; 20.4, 15–21 | Correct | A |
| 77–79 | Ovid reference / term / presiding | 1.167, 177, 178, 196, 205–208 | Correct | A |
| 83–84 | Norse term / presiding | Vsp refrains; Brodeur p. 25 | Correct. Brodeur's "seats of judgment" is at p. 26, quoting Vsp in Gylf. XIV; Allfather's high-seat is at p. 25. | A |
| 89 | Enlil presiding | 54–58 | Correct | A |
| 96 | Mbh members | CE 1.15.5, 9–10 | Correct (*surāḥ sarve*, *divaukasaḥ*) | A |
| 76 | Contendings function | (no locator) | Substance correct. Locators can now be supplied from Gardiner: 2, 13; 13, 12. | A |

## Required corrections

1. **Atrahasis obs 45** (members): replace "apparently Enlil since G 94 …" with SEAL's attribution (Mama is the presumed speaker of H 1–10, and Enki answers the assembly), or call the speaker unresolved. Restrict "heavily restored" to H 9–10.
2. **Atrahasis obs 44** (presiding): add SEAL's commentary to I 8 (the possible *malku* "ruler" pun on Enlil's counsellor title).
3. **Atrahasis obs 46** (function): flag that III C1 vi 20–22 "without deliberation" is restored. Note that pre-flood oath-taking by the gods is also attested in II E 11–12 / E 29–30 and G 28–29, while the flood-specific oath is MB only. Apply the same nuance to the README sentence.
4. **Deut obs 28**: the LXX v.9 names both Jacob and Israel. Re-attribute the `hendel-bar` register entry to the BAR editors (it reports Hendel's view). Optionally add Tov (TheTorah.com 2023) as a second secondary source for Wevers / 848.
5. **Isaiah obs 33**: remove "and the accents". Justify the throne reading by adjective agreement and JPS. Keep `qualified`.
6. **Baal obs 0/1**: "only a guess" is Smith's, about qb[ṣ]. Smith marks lp[ḫr.il.] with "(?)".
7. **Enlil & Ninlil obs 91 note**: "At Nippur" is supported (1–12, 59–60). Only "judges" and "for defiling Ninlil" go beyond the text. Mention the two-manuscript imperative.
8. **Mbh obs 95 note**: *262 says the gods "approached" Brahmā. It does not say he presides.
9. **Ovid obs 78 note / register**: *deorum* occurs at 1.171, not with *concilium*. The Magnus TEI header gives 1892 (cert low), so update the register's limitation.
10. **LDS row**: cite Abr 4:26, "the Gods took counsel among themselves", as the nearest scriptural deliberation wording.
11. **Egyptian row**:
    - Inspect Gardiner 1931 (chesterbeatty.ie).
    - Set obs 72 to `attested`.
    - Supply locators: eighty years 2, 13 and 13, 12; psḏt per p. 14 n. 3.
    - Record "Master of the Universe".
    - Record Gardiner's "roughly 1160 B.C." (Ramesses V) against "c. 1147".
    - Revise the README limits line that says Gardiner could not be opened.
12. **README**:
    - "one observation per row and field" is inaccurate. 21 cells have no observation: 7 `source_text`, 14 `woh_library`, and the `tradition` column is never audited. Either say so, or add the observations.
    - The claim "All `woh_library` links point at whole books" covers seven links the audit never observed (psalms, 1-kings, job-woh, deuteronomy, isaiah, book-of-enoch-woh, book-of-moses). Either check them or narrow the claim.
    - Iliad: say the 4.1–72 *assembly* ends with Athena sent to provoke the breach.

## Coverage and limits of this review

- **Fully re-read from source:** CTH 344 (translation and exemplar A); Charles 1912 (pp. 13–37, 66); MAM and JPS 1917 for all six Hebrew passages (Sefaria API; a Cloudflare challenge appeared only with a browser user-agent); ellopos LXX Deut 32; the BAS sidebar; King 1902 (Tablets I, III, IV and p. 75); SEAL Atrahasis I, II and III; ETCSL 1.2.1 (translation and composite); Perseus TEI for Ovid (Latin) and the Iliad (Greek and Murray); GRETIL CE 1.15–1.16.4; Ganguli §§17–18; LDS Moses 4, Abr 3–4 and D&C 121; heimskringla Völuspá; Bellows and Brodeur (OCR); the reshafim Wayback page; the Wikipedia raw text; Steinberger KTU 1.1 and 1.3.
- **Added sources not in the audit:** Gardiner 1931 (chesterbeatty.ie PDF) and Tov, TheTorah.com.
- **Not obtained:**
  - Heiser 2001: the core.ac.uk PDF returned 403 and an HTML page.
  - DJD XIV.
  - The Göttingen LXX itself. The "p. 347" locator remains unverified by anyone.
  - eBL / Lambert.
  - Hoffner, *Hittite Myths*.
  - Lichtheim and Wente.
  - KTU 1.2 and 1.4–1.6.
- **Not re-checked:**
  - The King "Tablet V fragment (K. 3,449a)" on Anu and the bow.
  - The Charles 9:3 half-bracket / homoioteleuton note.
  - SEAL witness-line sigla beyond those quoted.
  - The project library pages (woh_library HTTP 200 claims).
  - The More translation.
  - The Ugaritic "Verbesserungen" list.
- The Isaiah accent point is my reading of the printed accents. It is not a cited authority.
- I did not judge whether the row inclusion rule or the page-level consequences (claim-0010 wording, the identity claim) are right. The README's statements of them are consistent with the row findings.
