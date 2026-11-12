---
title: "Canon close reading (November 2026)"
status: draft
version: 0.1.0
last_reviewed: 2026-11-12
---

# Canon close reading (November 2026)

A set of research notes produced by reading Raël's three books in the original
French, paragraph by paragraph, against eleven questions, in two waves. Everything here is a
**draft research record**. Nothing in this directory promotes, revises or
retires a claim; each note ends with proposals labelled as proposals for
founder review.

## What was read

- *Le Livre qui dit la vérité* (TBWTT), *Les Extra-terrestres m'ont emmené sur
  leur planète* (ETTMTTP), *Accueillir les extra-terrestres* (LWTE): the
  project digitization in `data-library`, 2,070 paragraphs, about 105,000
  French words. The French is the source of record; the project's English is
  a reading aid.
- Original-language biblical and ancient texts from the project library
  (`*-woh` books), for the two comparative notes.

**Textual basis and its limit.** The digitization reflects later editions (it
carries footnotes dated after 1998 and editorial captions). Every statement
about what the 1974, 1975 and 1979 printings said is provisional until collated
with first printings. No outside source was consulted in the first nine notes; remarks there that
rely on outside knowledge are marked as unverified. `science-dated.md` and
`checkpoints.md` do use outside sources: each records the URL opened and a
verbatim excerpt. Those excerpts came through a fetch tool and have not been
re-read on the page by a second reader; library catalogues (BnF, SUDOC) and
several publisher sites were unreachable, so parts of that record rest on
abstracts, encyclopaedia pages and secondary reports, as each note states.

## The notes

| Note | Question | Register |
| --- | --- | --- |
| [numerics.md](numerics.md) | What quantities does the canon state, and do they agree? | 213 quantities |
| [development.md](development.md) | What changes from book 1 to book 2 to book 3? | 78 terms, 25 revisions |
| [hebrew-audit.md](hebrew-audit.md) | Do the canon's biblical readings rest on the original wording, on the French it quotes, or on neither? | 321 quotations |
| [ancient-parallels.md](ancient-parallels.md) | Which primeval-history details are absent from Genesis but present in older texts? | 37 details |
| [epistemics.md](epistemics.md) | What does the canon say about proof, belief, and its own reliability? | 717 items |
| [science.md](science.md) | What scientific and technological statements does the canon make, and in whose voice? | 676 statements |
| [voices.md](voices.md) | Who speaks in each paragraph, and where do the library's speaker tags disagree with the text? | every paragraph |
| [society.md](society.md) | What do the books say about the Elohim's world and the programme prescribed for Earth? | 87 items |
| [sendy-crosscheck.md](sendy-crosscheck.md) | Which non-Genesis details are already in Sendy's books, per the existing inventory? | 37 details |
| [science-dated.md](science-dated.md) | What did published science say, and when, on the points where the canon leans on recent discoveries? (outside sources) | 30 comparisons |
| [checkpoints.md](checkpoints.md) | Which public facts in the narrative can be compared with the public record? (outside sources) | 60 checkpoints |
| [editions.md](editions.md) | Which editions does the project hold, and how do the French and the 2005 English differ? (held PDFs) | 3 copies collated |

Structured registers are in [`registers/`](registers/). Quotations in the notes
are written `QUOTE[REF]: … ENDQUOTE` so that they can be machine-checked:

```sh
python3 tools/dump_canon.py <data-library> /tmp/canon
python3 tools/verify_quotes.py /tmp/canon *.md
```

At the time of writing all 1,210 canon quotations in the eleven notes verify as verbatim.

## Method and its limits

Each note was drafted by an AI research agent under one written brief
(separate what the text says, the analysis, and the open questions; verbatim
quotation with locator; no invented citations; report null and
framework-inconvenient results). Several agents read slices in parallel and
merged; their notes say which parts were read in full and which by targeted
retrieval. The maintainer's assistant then re-read the passages behind the
lead findings listed below against the French and, for the comparative notes,
against the library's Hebrew. Register items that are not cited below have
been machine-checked for quotation accuracy only, not re-read.

## Lead findings re-checked against the text

These were confirmed by a second reading of the cited paragraphs. They are
observations about the source, not framework claims.

1. **The canon defines the creation "day" precessionally but gives no
   lattice.** TBWTT-2:10 defines the day as the period during which the sun
   rises under the same sign at the spring equinox, "soit deux mille ans
   terrestres environ". The words *précession* and *zodiaque*, the figures
   2,160 and 25,920, a count of twelve signs and any BCE date do not occur.
   Landing "il y a vingt-cinq mille ans" (ETTMTTP-2:43) minus six such days
   gives 13,000 years, the figure LWTE-2:208 states for the first humans; the
   canon does not state the sum.
2. **LWTE-2:208 prints the multiplication 666 × 20 = 13,320**, counted to
   1945. LWTE-1:47 places the "déluge réel" about five thousand years ago.
3. **Book 2 corrects book 1 and attributes the error to the transcription.**
   ETTMTTP-2:23: "il faut rectifier un passage du message que vous avez mal
   retranscrit concernant une intervention éventuelle de notre part pour
   détruire l'humanité … nous n'interviendrons pas". TBWTT-7:6 still describes
   the means of such an intervention.
4. **The Flood's motive and the moment the Elohim learn they were created
   differ by book.** Motive: human progress (TBWTT-2:57); an experiment "sans
   grand intérêt" (ETTMTTP-3:219); violence proven by Satan before the council
   (LWTE-2:26). Self-discovery: before the sending of the Messiah
   (TBWTT-3:302); after the Flood (ETTMTTP-3:219); during it (LWTE-2:28). The
   exiles are pardoned after Babel in TBWTT-2:78 and amnestied before the
   Flood in LWTE-2:26.
5. **The account of Raël's father changes.** "Étant de père juif"
   (TBWTT-1:46, Yahweh); "né de père inconnu … paraît-il, un réfugié juif"
   (ETTMTTP-1:7); "Celui que tu prenais pour ton père n'était pas ton père"
   (LWTE-2:85–87), with a three-year embargo stated at LWTE-2:90.
6. **Proof is promised, refused, then offered by the tempter.** "preuves
   incontestables" (TBWTT-1:44); "Nous ne vous aiderons jamais ouvertement ni
   de quelque façon qui puisse servir de preuve aux sceptiques"
   (TBWTT-6:26); proofs offered in the temptation scene (LWTE-2:65) and the
   mission described as given "sans vous donner de preuves" (LWTE-2:66).
7. **TBWTT-7:72 says the visitor "ne reviendrait que quand ce qu'il m'avait
   demandé serait accompli"**; book 2 reports a further encounter in 1975.
8. **After Babel the canon still has one continent** (TBWTT-2:76: the
   scientists are dispersed "sur tout le continent"). The dating argument of
   LWTE-1:28 cites a terrestrial book, *Evolution ou Création*.
9. **The canon states the Babel pardon motive outright** (TBWTT-2:72: "afin
   d'obtenir leur pardon"), which the 0017 evidence map grades as inferred,
   and gives a non-labor motive for creating man (TBWTT-2:25).
10. **Ellipses carry several readings.** Exodus 14:21 is quoted from "il mit
    ainsi la mer à sec" (TBWTT-3:16) for the "rayon répulseur" of 3:15; the
    Hebrew clause before it is "by a strong east wind all night"
    (EXO-WOH-14:21). Daniel 10:13 is quoted as "Michaël (...) est venu (...)
    là, auprès des rois de Perse" (TBWTT-3:216) for a delegation helping the
    Persians (3:215); in DAN-WOH-10:13 the prince of Persia opposes the
    speaker and Michael comes to help the speaker. Genesis 7:17 is quoted for
    the ark rising "non pas sur les eaux" (TBWTT-2:60); the same verse has the
    waters lift the ark and 7:18 has it go "on the face of the waters".
11. **The original is sometimes more favourable than the French printed.**
    "Dieu vivant" (TBWTT-3:93, 1 Samuel 17:26) is אֱלֹהִים חַיִּים with a plural
    adjective (1SA-WOH-17:26). The "three stages" of TBWTT-2:62 have no noun
    in GEN-WOH-6:16 (three plural adjectives).

12. **"Les Clés" speaks as a created human.** ETTMTTP chapter 3 is framed by
    2:132 ("je me mis à écrire en observant tout ce que j'écrivais et en le
    découvrant comme un lecteur"), speaks of "Elohim nos pères, nos
    créateurs" (3:5), has Raël as "je" (3:174) and the Elohim as "nous" in
    3:241. The library tags the chapter as Yahweh's speech.
13. **TBWTT narrates four "Le lendemain" frames** (2:1, 3:2, 5:2, 6:1), so five
    sessions are narrated, while the text says "six jours de suite" (7:16,
    7:76). No frame stands at the joins of chapters 3/4 and 6/7.
14. **A post-mortem regime with punitive re-creation is stated** (ETTMTTP-2:99;
    the class includes those who "n'ont pas su reconnaître la vérité", 2:82).
    Humanitarianism is called "une règle provisoire" (ETTMTTP-3:96); the
    estate beyond the family home is to be willed "au Guide des guides"
    (ETTMTTP-3:71). The conditional destruction of the State of Israel stands
    at ETTMTTP-2:125. LWTE-3:59 forbids killing even at an Eloha's request;
    LWTE-3:70 allows execution as a last resort against a military threat to
    humanity.
15. **Sendy inventory.** *Ces dieux* names the Epic of Gilgamesh for the ark's
    cargo ("les semences de vie", `check-ces-dieux.json#I033`); *Les cahiers*
    records leaders "qui vivent dans les cieux" deciding the destruction
    (`check-cahiers.json`, sendy_only, line 1472); Sendy's Satan is the
    pro-human discloser (`check-cahiers.json#I021`).
16. **The digitized TBWTT already reads "Puy-de-Lassolas"** (TBWTT-1:3) and
    carries the heading "Mouvement Raélien" (7:73).

## Findings reported by the notes and not yet re-checked

Counts and patterns that rest on the agents' registers: the classification
totals of the Hebrew audit (138 supported, 116 interpretive addition, 30
translation-dependent, 20 contradicted); the 21-of-37 distribution of
non-Genesis details; term frequencies by book (for example *Satan* 13 / 0 /
43, *Lucifer* 0 / 0 / 9); the home-planet demographic arithmetic; the
Enochic cluster of LWTE-2:25–27; the Qur'anic cluster; the claim that the
New Testament quotations follow a translation other than Dhorme's. Treat
these as leads until each has been re-read. From the second wave: the voice
shares by book (Yahweh's speech 67 % of TBWTT, 22 % of ETTMTTP, 8 % of LWTE);
the data-fix list for speaker tags; the 14-of-21 Sendy coverage count; zero
occurrences of *paradisme*, *troisième temple* and *eugén-*; and every
outside-source comparison in `science-dated.md` and `checkpoints.md` (memory
transfer 1965–72 and its later abandonment; the nearest-star and parasang
comparisons; the Ararat radiocarbon ages; INA dates
for the 1974 television appearances; station weather for 13 December 1973
and 7 October 1975).

## Third wave: the held editions (2026-11-12)

[editions.md](editions.md) reads the three PDFs in `data-sources` and I re-read
each point below against them.

- The French in the library is the 1998 combined volume (books 1 and 2) and
  the 2001 Nova edition (book 3). No first printing is held.
- The library's English for book 3 is the 2005 edition's translation
  (630 of 631 paragraphs). Its licence status needs a ruling.
- *Évolution ou Création* (LWTE-1:28) is now identified: both editions print
  the bibliography entry (Flori misprinted "Fiori"; Éditions S.D.T.,
  Dammarie-les-Lys).
- Both editions name Dhorme's translation as the Bible used; the 2005 editor
  calls it "the one that Rael had with him during his encounter".
- The 1998 volume prints the French text of the message of 13 December 1997
  (pp. 207–210), which core has no source note for.
- Book 3, French 2001 against English 2005: no change of doctrine or figure
  found; two date differences (year 30 or 31 for October 1975; a witness's
  1977 or 1978).
- The lead findings checked in the 2005 English of books 1 and 2 are all
  present there (list in the note).

## Housekeeping found on the way (other repositories)

- `data-library`: ETTMTTP chapter 3 ("Les Clés") is tagged as Yahweh's speech
  but speaks of "nos créateurs"; LWTE is tagged Narrator throughout though it
  contains several voices; the `eridu-genesis` slug holds a different tablet
  (the Eridu Genesis is `flood-story-woh`); a library note at EXO-WOH-19:16
  attributes a TBWTT-3:25 quotation to ETTMTTP.
- The standalone `data-library` clone lags the copy vendored in the website
  repository.

## Proposals

Each note carries its own list. None has been acted on. The ones that touch
accepted records most directly:

- 0021: grade the parasang conversions as canon-explicit (TBWTT-5:52–53).
- 0003 / 0059 / 0050: add the canon's own figures and label the 2,160-year
  lattice and "11,375 BCE" as project refinements at a declared offset.
- 0017: regrade the pardon motive as canon-explicit (TBWTT-2:72).
- 0034: record that the canon states no labor motive for creating man.
- 0035: qualify "consistent principal speaker" with the voice and
  self-revision findings.
- 0066: scope the Dhorme finding to the Old Testament.
- 0009: add 1 Samuel 17:26 to the evidence map.
- 0071: add TBWTT-2:76, LWTE-1:31 and LWTE-2:216.
- New descriptive records (candidates): the canon's numerical chronology; the
  canon's self-corrections; the canon's proof policy; selective quotation.
- Research question: collate the passages named in `development.md` with the
  1974 first printing.
- 0029 / 0032 / 0033 / 0049: bring the scope notes into line with the wording
  recorded in `society.md` (punitive re-creation; council recruitment versus
  the electorate prescribed for Earth; which planet book 2 describes;
  inheritance and the provisional status of humanitarianism).
- 0035 / 0020: the session count and the four modes of transmission
  (`voices.md`).
- 0072: six resemblance rows and two difference rows from
  `sendy-crosscheck.md`; twelve look-ups to run when the Sendy texts are in
  hand.
- 0021: record the historical parasang beside the canon's gloss, once the
  source is opened.
- `data-library`: the speaker-tag fix list in `voices.md` (maintainers'
  decision; "Les Clés" needs a ruling).
