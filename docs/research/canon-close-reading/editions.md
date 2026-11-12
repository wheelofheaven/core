# Editions: what text the project actually holds

Status: **draft research note, awaiting founder review.** No claim record, specification or evidence map is changed by this note.

Date: 2026-11-12. Method: the three PDFs in the private `data-sources` repository were converted with `pdftotext -layout` and compared mechanically with the `data-library` text used by the other notes in this package (`tools/dump_canon.py`). Scripts and outputs are small and reproducible; the comparisons are described in each section. Quotations marked `QUOTE[REF]` are from the library text and are checked by `tools/verify_quotes.py`; quotations from the PDFs carry a printed page number and are not machine-checked.

Labels: **TEXT** = what a held copy prints. **ANALYSIS** = my inference. **OPEN** = not settled.

## 1. The held copies

**TEXT.** Three files, none a first printing.

| File (`data-sources/pdf/…`) | What it says it is | Evidence in the file |
|---|---|---|
| `_combined/le-message-donne-par-les-extra-terrestres.pdf` (228 pp.) | French, books 1 and 2 in one volume | "Copyright © La Fondation Raëlienne 1998"; PDF produced 12 August 2016 |
| `lets-welcome-the-extraterrestrials/…-fr.pdf` (154 pp.) | French, book 3 | "Edité par Nova Distribution … © by Nova Distribution - 2001"; PDF produced December 2004 |
| `_combined/intelligent-design-en.pdf` | English, all three books | "Copyright © The Raelian Foundation 2005"; ISBN 2-940252-20-3; self-described as "a newly combined re-translation and updated edition" |

The repository's sidecar metadata dates the French combined volume "2005"; the file's own copyright line says 1998. The folders for the separate first and second books are empty.

## 2. Which text the library carries

**TEXT (measured).**

- French: every library paragraph of 14 words or more shares a six-word run with the corresponding PDF (TBWTT 537 of 537, ETTMTTP 447 of 447, LWTE 641 of 641). The French in `data-library` is the 1998 and 2001 text.
- English, book 3: 630 of 631 library paragraphs share an eight-word run with the 2005 English PDF. The library's English for *Let's Welcome the Extra-Terrestrials* is the 2005 edition's translation, not a project translation.
- English, books 1 and 2: 260 of 544 and 236 of 453 paragraphs share an eight-word run with the 2005 PDF. **OPEN:** I did not separate shared Bible quotations from shared prose, so this figure does not say how far the project's English for books 1 and 2 depends on the 2005 text.

**ANALYSIS.** Two consequences for the rest of this package.

1. Every statement in the other notes about "the French" is a statement about the 1998 and 2001 editions. This was already flagged as a limit; it is now exact.
2. For book 3 the English column is an independent edition, so French and English can be collated against each other (section 5).

**For the founder (not a research finding):** the library publishes the 2005 English of book 3, which the PDF marks as copyright The Raelian Foundation. I do not know what permission or licence covers it. The dataset-eligibility rule in project memory ("by license/status") may need this fact.

## 3. Editorial layers visible in the held French

**TEXT.**

- A publisher's notice (*Avertissement*) at the head of the 1998 volume: the two books were originally separate, "puiblié en 1974" and "pubilié en 1975" (sic).
- One editor's footnote, repeated on nine pages of the 1998 volume: "N.D.L.R. : Le 15 mai 1976 : dernière réunion du "MADECH", constitution du "MOUVEMENT RAELIEN", puis dès le 6 août 53 (1998) de la "Religion Raëlienne"."
- In the 2001 book 3, a recurring footnote "(*) Depuis 1998 les deux premiers livres de Raël sont regroupés en un volume…", and page references to "le deuxième message(*)" that point into the combined volume.
- Material in the 1998 volume that is later than both books and is not in the library: "Message du 13 décembre 52 (1997)" (pp. 207–210), "Post-scriptum de l'auteur – 52 (1997)" (p. 211), "Informations additionnelles" (p. 219), "Addendum" (p. 220), and photo captions.
- Acknowledgements (p. 218): "Les références des textes bibliques ont été reprises de La Bible, traduction d'Édouard Dhorme, Bibliothèque de la Pléiade (NRF)".

**ANALYSIS.** The body text may also have been revised between 1974 and 1998; nothing in the held copy shows whether it was. The marked layers above are the only ones that can be separated without a first printing.

## 4. Three things the held copies settle

### 4.1 *Évolution ou Création* is identified

`science-dated.md` (finding 5) left the book Raël recommends in LWTE-1:28 as "probable, not confirmed", pending the printed bibliography.

QUOTE[LWTE-1:28]: je veux parler de Evolution ou Création (voir bibliographie en fin d'ouvrage) ENDQUOTE

**TEXT.** The 2001 French prints that bibliography (p. 154): "Evolution ou Création, Jean FIORI et Henti RASOLOFOMASOANDRO, Edition S.D.T., 77190 Dammarie-les-lys (France)" and "Soumission à l'autorité, S. Milgram, Paris, 1974". The 2005 English bibliography (p. 380) has "Fiori, Jean, Evolution ou Creation, Published by Editions S.D.T., 77190, Dammarlie-les-Lys, France".

**ANALYSIS.** Publisher, town and second author match Flori and Rasolofomasoandro, *Évolution ou création ?*, Éditions SDT, 1974. "Fiori" and "Henti" are misprints carried by both editions. The identification is now confirmed by the book's own bibliography. What that book says about radiometric dating is still unread.

### 4.2 The Bible used is stated by the editions themselves

**TEXT.** The 1998 French names Dhorme's Pléiade translation as the source of its Bible references (section 3). The 2005 English editor's notes (pp. 378–379, headed "The notes shown below are that of the editor and not of the author") say the English uses the Restored Name King James Bible by default and, at note 24, describe "the French bible by Edouard Dhorme, the one that Rael had with him during his encounter".

**ANALYSIS.** This is an edition-level statement, by editors, in 1998 and 2005. It supports the scope proposal for woh-claim-0066 (Dhorme as the Old Testament text behind the readings) and shows that the question of the New Testament quotations remains separate: the Pléiade Dhorme is an Old Testament. **OPEN:** whether a first printing carries the same acknowledgement.

### 4.3 The 1997 message exists in a held primary copy

The site cites the message of 13 December 1997 through the 2005 English. The French text is in the held 1998 volume, pp. 207–210, in the voice of the Elohim. Statements it prints:

- "Notre préférence pour Jérusalem était purement sentimentale"
- "Les véritables Juifs de la Terre ne sont plus le peuple d'Israël, mais tous ceux qui nous reconnaissent comme leurs créateurs"
- "c'est désormais à toutes les nations de la Terre qu'il faudra demander l'autorisation et l'extraterritorialité"
- the one-kilometre radius "pourra être composé d'eau aussi bien que de terre ferme"
- Israel keeps priority for "une période de réflexion très limitée"; otherwise "le peuple de David perdra notre protection et sera disséminé"
- "Le bouddhisme dépouillé des lourdeurs mystiques du passé donne le raëlisme"

**ANALYSIS.** Book 2's condition (QUOTE[ETTMTTP-2:125]: sinon un autre pays accueillera le Guide des guides et édifiera notre ambassade sur son territoire ENDQUOTE) is here acted on, 22 years later, in a text outside the three books. Core has no source note for it. It bears on the embassy and chosen-people records and on the Buddha entry written this month.

## 5. Book 3: French 2001 against English 2005

Method: digits compared paragraph by paragraph, then paragraphs whose length ratio is unusual. The witness letters at the end of chapter 4 are known to be misaligned in the library and are excluded.

| Ref | French 2001 | English 2005 | Kind |
|---|---|---|---|
| LWTE-1:2 | "le 7 octobre 30 (1975)" | "October 7th, 1975 (31)" | Year count differs. Book 2's rule (1946 = year 1) gives 30 for 1975. |
| LWTE-4:191 | "en 1977 je pris connaissance du message" | "in 1978" | A witness's date differs. |
| LWTE-1:4, 1:17, 1:20, 1:26, 1:30, 2:79, 3:26 | page references to the French volumes | page references to the 2005 volume | Repagination. LWTE-2:80 drops its page reference. |
| LWTE-1:1 | chapter introduction | adds "in the years immediately following the publication of his first two books in the mid-1970s" | Editorial addition. |
| LWTE-3:53 | "(Soumission à l'autorité, S. Milgram, Paris, 1974.)" | empty; moved to editor's note 25 | Citation relocated. |
| LWTE-2:208–209 | one paragraph, then Hiroshima | sentence on the 666th generation moved into the next paragraph | Paragraph break only; figures identical (666, 20, 13,320, 1945). |
| LWTE-1:28 | "Evolution ou Création" | "Evolution or Creation" | Title translated; same bibliography entry. |

**TEXT.** The 2005 editor's notes record further deliberate changes: Bible passages taken from six different English versions chosen to fit the French wording (notes 1, 8, 11, 12, 17, 20, 21); "Yahushua" replaced by "Jesus" (16); "fish" replaced by "pisces" in Zephaniah 1:10 (19); a Bible quotation "modified from the original quotation" so that it reads "soul" as in Dhorme (24); and, at note 2, that the French original has "science" where English Bibles have "good and evil".

The two editions date the movement's renaming differently in their own editorial notes: 15 May 1976 (French footnote, section 3) and "In 1975" (English note 23).

**ANALYSIS.** I found no change of doctrine or figure between the 2001 French and the 2005 English of book 3 in the paragraphs compared. The differences are bookkeeping, with two exceptions that touch dates (year 30 or 31; 1977 or 1978). The English Bible quotations are a patchwork selected to match readings first made on Dhorme's French, so the "selective quotation" findings in `hebrew-audit.md` must be made on the French, as they were.

## 6. Do the lead findings survive in the 2005 English of books 1 and 2?

Checked by locating each passage in the 2005 PDF. All of the following are present with the same figures or sense:

- creation "day" as the period the sun rises under the same sign at the vernal equinox, "about 2,000 years" (TBWTT-2:10)
- 22,000 years since the decision (TBWTT-5:4); landing 25,000 years ago (ETTMTTP-2:43)
- the correction "that you wrongly transcribed" (ETTMTTP-2:23)
- dispersal "all over the continent" (TBWTT-2:76); "the single continent" (TBWTT-3:279)
- the "repulsion beam" at the sea crossing (TBWTT-3:15–16)
- two-child law (TBWTT-7:13); "temporary rule" (ETTMTTP-3:96)
- "the State of Israel will be destroyed once more" (ETTMTTP-2:125)
- he "would return only when all that he had asked of me was accomplished" (TBWTT-7:72)
- 1946 as year one, 1976 as year 31 (ETTMTTP-3:172)
- parasang passage and figures (TBWTT-5:52)

Not checked in the 2005 English: the remaining lead findings, and any passage-by-passage collation of books 1 and 2.

## 7. Limits

- No first printing was seen. Nothing here says what 1974, 1975 or 1979 printed.
- `pdftotext` output was read as text; no page image was inspected. Printed page numbers are taken from the running page numbers in the extraction.
- The French–English comparison of book 3 is mechanical (digits, lengths). A changed word that keeps length and digits would not be found.
- Counts in section 2 depend on the run length chosen (six and eight words).

## 8. Proposals (for the founder; none acted on)

1. **Source notes.** Add edition statements to the three canon source notes: French = 1998 (La Fondation Raëlienne) and 2001 (Nova Distribution); English book 3 = 2005 edition. Correct the `data-sources` sidecar year (2005 → 1998) for the combined French volume.
2. **New source note:** "Message du 13 décembre 52 (1997)", French text, 1998 volume pp. 207–210, with the access level `direct`; decide whether it joins the library.
3. **woh-claim-0071 evidence map / `science-dated.md`:** change *Évolution ou Création* from probable to identified, citing the two bibliographies.
4. **woh-claim-0066:** cite the 1998 acknowledgement and 2005 editor's note 24 as edition-level support, labelled as editors' statements.
5. **Holdings.** Register the three PDFs in `data-sources/holdings/` so locators in core can name the copy. Want-list: any 1974, 1975 or 1979 printing.
6. **Library housekeeping.** Record in the book metadata that the English of book 3 is the 2005 edition; rule on its licence status.
