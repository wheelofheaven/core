# Finding: woh-exp-0011

- Date: 2026-11-22
- Source and edition inspected: *The Book Which Tells the Truth* (1974), project digitization, French base text (`text` field), `data-library/the-book-which-tells-the-truth/chapter-2.json` (92 paragraphs, TBWTT-2:1 to 2:92) and `chapter-3.json` (305 paragraphs, TBWTT-3:1 to 3:305). Hebrew: `data-library/genesis-woh/chapter-N.json` and `data-library/job-woh/chapter-1.json`, field `text`; for books with no `-woh` chapter, the Unicode/XML Leningrad Codex (UXLC 2.6) served by tanach.us (`Server.txt`). Lexica: Brown-Driver-Briggs (BDB) and Strong's Exhaustive Concordance as reproduced on biblehub.com `/hebrew/<Strong number>.htm`; commentaries as reproduced on biblehub.com `/commentaries/<book>/<c>-<v>.htm`. French dictionary: Trésor de la langue française informatisé (TLFi) at cnrtl.fr `/definition/<mot>`.
- Access achieved: `project_digitization` for the book (both chapters read in full, French `text` only) and for the Genesis and Job Hebrew; `full_text` for the UXLC verses, the BDB/Strong's entries and the TLFi entries actually quoted. Not reached: Sefaria (HTTP 403 to the API); the BDB entry for עַל / מֵעַל (the Bible Hub page for Strong 5921 carries no BDB text; studylight.org returned 403).
- Search performed: every paragraph of both chapters printed in order (refId, speaker, `kind`, `text`) and read; the `i18n` renderings were not used; the `notes` field was not read (a fragment of the note on TBWTT-2:2 was displayed by a first dump and was not used). Every string in « » that reproduces a Bible verse was listed. For each `sense_dependent` case and for the borderlines named below, the Hebrew verse was opened and the lexicon entry downloaded and searched by verse reference and by keyword. The Hebrew of the other quotations (the `image_step` and `no_explanation` ones) was not compared word for word. Verse references are the book's own (French numbering); they were checked against the Hebrew only where a Hebrew verse is quoted below.

## Answer

Counting rule used: one quotation = one « » citation of a verse or verse-range (continuation paragraphs joined; two separately referenced verses in one paragraph count as two; phrases re-quoted inside the commentary are not counted again).

**Totals.** Quotations listed: 168 (chapter 2: 39; chapter 3: 129). Already recorded and left out of the classification: 2 (TBWTT-2:29/2:30, Genesis 2:16-17; TBWTT-3:191/3:192, Ezekiel 42:14). Classified: 166.

- `sense_dependent`: 13
- `image_step`: 150
- `no_explanation`: 3

Within `sense_dependent` (13):

- `shared`: 8 (TBWTT-2:26, 2:59, 2:67, 3:49, 3:93, 3:146, 3:241, 3:276)
- `french_only`: 2 (TBWTT-2:42, 2:62)
- `disputed`: 1 (TBWTT-2:9)
- `not_checkable`: 0
- not assignable to one of the four classes as the protocol defines them: 2 (TBWTT-2:4 and 3:250, both on the word « Elohim »; see below). Step 6 could not be carried out as written for these two: the commentary asserts a sense of the *Hebrew* word (« ceux qui sont venus du ciel ») that is not a sense in the BDB or Strong's entries, and it is not a sense or property of a French word either, so neither `shared` nor `french_only` describes it. The property "plural" that TBWTT-2:5 also uses is a property of the Hebrew word (BDB: "noun masculine plural").

So, in the protocol's vocabulary: of the 13 places where the commentary leans on a particular sense or property of a word in the quoted French, the Hebrew word has that sense in 8, the sense belongs to the French only in 2, lexica and commentaries divide in 1, and in 2 the sense claimed for the Hebrew word is not found in the lexica consulted. Nine of the thirteen (every `shared` case except TBWTT-2:67, and both « Elohim » cases) rest on decisions between (a) and (b) that are stated under "Borderline decisions".

### The thirteen `sense_dependent` cases

| # | refId (quotation / commentary) | Verse | French word | Sense or property used | Hebrew word | Class |
|---|---|---|---|---|---|---|
| 1 | 2:4 / 2:5 | Gen 1:1 | Elohim | "ceux qui sont venus du ciel"; plural | אֱלֹהִים | unassigned (gloss not in lexica; plural form shared) |
| 2 | 2:9 / 2:10 | Gen 1:5 | jour | a long period (about two thousand years) | יוֹם | `disputed` |
| 3 | 2:26 / 2:27 | Gen 1:26 | image, ressemblance | visible, physical likeness | צֶלֶם, דְּמוּת | `shared` |
| 4 | 2:42 / 2:43 | Gen 3:22 | science | scientific knowledge (the sciences) | לָדַעַת (טוֹב וָרָע) | `french_only` |
| 5 | 2:59 / 2:60 | Gen 7:17 | s'éleva au-dessus de | rose above (as opposed to "sur les eaux") | וַתָּרָם מֵעַל | `shared` |
| 6 | 2:62 / 2:62 | Gen 6:16 | étages | stages of a rocket | (no noun) תַּחְתִּיִּם שְׁנִיִּם וּשְׁלִשִׁים | `french_only` |
| 7 | 2:67 / 2:68 | Gen 8:21 | objet | "but" (aim, purpose) | יֵצֶר | `shared` |
| 8 | 3:49 / 3:48 | Num 18:13 | primeurs | fresh fruit and vegetables | בִּכּוּרֵי | `shared` |
| 9 | 3:93 / 3:94 | 1 Sam 17:26 | vivant | actually alive, "palpable" | חַיִּים | `shared` |
| 10 | 3:146 / 3:147 | Isa 13:5 | confins du ciel; pays lointain | far end of the sky, taken literally | מִקְצֵה הַשָּׁמָיִם; מֵאֶרֶץ מֶרְחָק | `shared` |
| 11 | 3:241 / 3:242 | Ps 19:7 | orbite; point de départ | astronomical orbit; departure | וּתְקוּפָתוֹ; מוֹצָאוֹ | `shared` |
| 12 | 3:250 / 3:251 | Job 1:6 | Elohim | "littéralement «venus du ciel»" | הָאֱלֹהִים | unassigned (gloss not in lexica) |
| 13 | 3:276 / 3:277 | Jer 10:14 | science | the science by which the creators created | מִדַּעַת | `shared` |

### Borderline decisions between (a) and (b)

Rules applied, so the count can be redone:

- (a) was given where the commentary singles out a word of the quotation and its inference depends on which meaning that word has (a choice among senses, a technical or idiomatic French sense, or insistence on the literal sense against an available figurative one).
- (b) was given where the commentary replaces the thing named with another thing (X "en réalité" Y), including the standing replacement of Iahvé / Elohim / Anges by "les créateurs", and including a redefinition that gives a word a content no dictionary gives it.
- (c) was given only where no sentence within the window (two paragraphs before, three after) addresses the content of the quotation.

Counted (a), but arguably (b):

- 2:26 (image / ressemblance): 2:27 only says « A notre image! Vous pouvez constater que la ressemblance est frappante. » Counted (a) because it takes the words as visible likeness.
- 2:59 (s'éleva au-dessus de la terre): counted (a) because 2:60 argues from the wording (« il est bien dit … »).
- 3:49 (primeurs): counted (a) because 3:48 ends « … préféraient les fruits et légumes frais. » and the verse is then given as the support.
- 3:93 (Dieu vivant): counted (a) because 3:94 infers a « «Dieu» tout à fait palpable ».
- 3:146 (confins du ciel): counted (a) because 3:147 re-quotes the words and adds « on ne pouvait être plus clair ».
- 3:241 (orbite): counted (a) because 3:242 answers with « l'orbite terrestre »; it also changes whose "point de départ" it is (see Quotations).
- 3:276 (science): counted (a) because 3:277 continues « Cette science qui a permis aux créateurs de créer … ».
- 2:4 and 3:250 (Elohim): counted (a) although the word is a transliteration, because the commentary states what the word "veut dire".

Counted (b), but arguably (a); with the class each would take if moved, where I checked it:

- 2:6 Gen 1:2 « planait » (2:7: reconnaissance flights, satellites). Hebrew מְרַחֶפֶת; BDB II. רָחַף: "Pi`el hover … hovering over face of waters, or perhaps (see Syriac) brooding (and fertilizing)". Would be `shared` (or `disputed` on hover / brood).
- 2:7 Gen 1:4 « bonne » (2:8: the sun sends no harmful rays; « La «lumière était bonne». »). Hebrew טוֹב; BDB II. טוֺב: "pleasant, agreeable, good". Not checked further.
- 2:56 Gen 6:5 « le mal » (2:57: « Le mal, c'est-à-dire le désir de devenir un peuple égal à ses créateurs »). Treated as a redefinition, hence (b). The same for « le mal » in 2:67.
- 3:37 « la tente du rendez-vous » (3:36: the place where they « devaient rencontrer les représentants des hommes »). Hebrew אֹהֶל מוֹעֵד (Exod 33:7, UXLC). BDB entry for מוֹעֵד downloaded but not quoted here; not classified.
- 3:73 Judg 6:21 « canne » (3:74: « un tuyau flexible, une «canne» »). Not checked.
- 3:104 1 Kgs 8:12 « nuage » (3:107: a craft in orbit « au-dessus des nuages »). Hebrew בָּעֲרָפֶל (UXLC). Not checked further.
- 3:162 Ezek 1:22 « plate-forme » (3:166: « le gros véhicule interplanétaire »). Hebrew רָקִיעַ (UXLC), the same word the book's Genesis quotation at 2:11 gives as « firmament ». Not classified.
- 3:168, 3:171 Ezek 2:8, 3:3 « mange », « mangeai » (3:169: « C'est une image … une «nourriture» intellectuelle »). Treated as an avowed figure, hence (b).
- 3:220 Dan 12:3 « Les gens intelligents » (3:221: « Les génies »). Hebrew וְהַמַּשְׂכִּלִים (UXLC). Not checked further.
- 3:222 Dan 12:4 « la connaissance s'accroîtra » (3:223: « un niveau de connaissances scientifiques suffisant »). Hebrew הַדָּעַת (UXLC); same word as case 13. Would be `shared` on the reasoning of case 13.
- 3:259 Job 37:18 « des nuages, solides comme un miroir de métal fondu » (3:260: « des «nuages solides», des engins volants métalliques »). Hebrew לִשְׁחָקִים חֲזָקִים כִּרְאִי מוּצָק (UXLC). BDB שַׁחַק: "2 (thin) cloud, usually plural … = heavens, sky Job 37:18 (with חִרְקִיעַ)". If moved to (a) on « nuages », BDB itself reads this verse as "sky", not clouds.
- 3:296 Ps 139:6 « Science trop mystérieuse pour moi » (3:297: telepathy). Hebrew דַעַת (UXLC); BDB דַּעַת 1e "knowledge possessed by God Job 10:7; Psalm 139:6".

(b) / (c) decisions: 3:18 (Exod 14:30), 3:128 (2 Kgs 1:15) and 3:289 (Isa 40:21) are (c). Quotations whose only "explanation" is a plain narrative link in the window (for example 2:69, 2:90, 3:5, 3:54, 3:56, 3:141) were put in (b) under the rule above; a stricter rule would move them to (c) without touching the (a) count.

### Recorded (b) and (c), by refId of the quotation

Chapter 2, `image_step` (31): 2:6 (Gen 1:2), 2:7 (1:4), 2:11 (1:7), 2:13 (1:9), 2:15 (1:11-12), 2:17 (1:14), 2:19 (1:20), 2:23 (1:24), 2:31 (2:19), 2:34 (3:1-5), 2:36 (3:7), 2:38 (3:14), 2:40 (3:21), 2:44 (3:24), 2:47 (4:3-4), 2:50 (6:1-2), 2:52 (6:3), 2:54 (6:4), 2:56 (6:5), 2:61 (7:24), 2:63 (8:1), 2:65 (8:20), 2:69-70 (10:32), 2:73 (11:6), 2:75 (11:7-8), 2:79 (19:1), 2:81-82 (19:11), 2:83 (19:14), 2:85 (19:17), 2:86 (19:24-26), 2:90 (22:12).

Chapter 3, `image_step` (119): 3:3 (Gen 28:12), 3:5-6 (Gen 35:2), 3:8 (Exod 3:2), 3:11 (13:21), 3:13 (14:19), 3:16-17 (14:21), 3:20-21 (16:14), 3:23 (17:6, phrase only), 3:25 (19:16), 3:26 (19:18-19), 3:28 (19:23-24), 3:29 (24:2), 3:30 (24:10), 3:32 (24:17), 3:35 (25:2-7), 3:37 (unreferenced, « la tente du rendez-vous »), 3:38 (33:9), 3:39 (33:11), 3:41 (33:20), 3:44 (Lev 21:17-18), 3:47 (Num 11:7-8), 3:51 (21:8), 3:54 (33:52-53), 3:56 (Deut 4:37), 3:58 (Josh 3:15-16), 3:62 (5:14), 3:64 (6:5), 3:67 (10:11), 3:70 (10:13), 3:73 (Judg 6:21), 3:78 (13:3), 3:79-81 (13:4-5), 3:82-83 (13:9), 3:88 (1 Sam 3:9), 3:90-91 (3:10), 3:97 (5:6), 3:99 (2 Sam 6:6-7), 3:101 (1 Kgs 1:50; 2:28), 3:104 (8:12-13), 3:105 (8:11), 3:105 (8:10), 3:106 (6:13), 3:108 (13:1-5), 3:110 (13:9-10), 3:112 (17:6), 3:114 (17:23), 3:115 (17:24), 3:116 (18:38), 3:119 (19:5-6), 3:120 (19:11-12), 3:122 (22:19), 3:124 (22:22), 3:126 (2 Kgs 1:12), 3:130-131 (2:1), 3:132 (2:11), 3:137 (4:42-44), 3:141 (17:23), 3:144 (Isa 6:1-2), 3:148 (14:13), 3:150-151 (14:14), 3:152 (14:17), 3:154 (15:8-9), 3:156 (26:20), 3:159 (Ezek 1:4-14), 3:160 (1:15), 3:161 (1:16-21), 3:162 (1:22-26), 3:168 (2:1, 8), 3:170 (2:9-10), 3:171 (3:3), 3:173 (3:14, 12), 3:175-176 (8:3), 3:178 (10:8), 3:179 (10:19), 3:180 (11:1), 3:181 (11:23-24), 3:183 (37:1), 3:185 (37:3, 7-8, 10), 3:188 (40:2-3), 3:194 (43:2), 3:196 (44:2), 3:198 (44:3), 3:200 (44:3), 3:202 (44:15-16), 3:203 (44:17-18), 3:205 (44:30), 3:208 (Dan 3:25, Aramaic), 3:210 (6:23, Aramaic), 3:212 (10:5-6), 3:216 (unreferenced; Daniel, by 3:211-3:215), 3:218 (12:2), 3:220 (12:3), 3:222 (12:4), 3:224 (12:7), 3:226 (12:9), 3:229 (Jonah 2:1), 3:231-232 (2:11), 3:234-235 (Zech 5:1-2), 3:237 (5:9), 3:239 (Ps 8:6), 3:243-244 (19:5), 3:246 (33:13-14), 3:252 (Job 1:9, 11-12), 3:255-256 (2:6), 3:259 (37:18), 3:272 (Isa 27:1), 3:274 (29:12), 3:278 (Prov 8:22-23, 27, 29-31), 3:280-281 (Eccl 3:15), 3:282 (3:19), 3:285 (Isa 45:9-10), 3:286 (48:10-11), 3:291 (Amos 4:13), 3:293 (Zech 4:10), 3:296 (Ps 139:4-6), 3:299 (147:4-5), 3:301 (147:15), 3:303 (Mic 5:1-4), 3:304 (Zech 9:9-10).

`no_explanation` (3): 3:18 (Exod 14:30), 3:128 (2 Kgs 1:15), 3:289 (Isa 40:21).

Listed, not classified (already recorded): 2:29 with 2:30 (Gen 2:16-17); 3:191 with 3:192 (Ezek 42:14).

Skipped under step 2 (no Hebrew or Aramaic original in the Hebrew Bible): 3:264 (Tobit 12:19-20), 3:266 (Sagesse 6:22), 3:268 (Sagesse 13:5), 3:270 (Sagesse 13:1). No New Testament quotation occurs in chapters 2 and 3.

## Quotations

French is from the `text` field. Hebrew from the source named in each case.

**Case 1. TBWTT-2:4 / 2:5, Genesis 1:1, « Elohim ».**
- 2:4: « Prenez d'abord la Genèse, au premier chapitre : «Au commencement Elohim créa les cieux et la terre». (Genèse, I-1) »
- 2:5: « Elohim, injustement traduit dans certaines Bibles par Dieu, veut dire en Hébreu «ceux qui sont venus du ciel» et est bel et bien au pluriel. Cela veut dire que les scientifiques issus de notre monde ont d'abord recherché la planète leur paraissant la plus apte à la réalisation de leurs projets. »
- French word: none to look up; « Elohim » is a transliteration, so no TLFi entry applies.
- Hebrew, GEN-WOH-1:1 (`text`): בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃
- BDB (Bible Hub, Strong 430): "אֱלֹהִים 2570 noun masculine plural … 1 plural in number. a. rulers, judges … b. divine ones, superhuman beings including God and angels … c. angels … d. gods … 2 Plural intensive. a. god or goddess … b. godlike one … c. works of God, or things specially belonging to him … d. God (see 3 & 4). 3 הָאֱלֹהִים the (TRUE) God".
- Strong's (same page): "Plural of 'elowahh; gods in the ordinary sense; but specifically used (in the plural thus, especially with the article) of the supreme God; occasionally applied by way of deference to magistrates; and sometimes as a superlative".
- Deciding observation: the BDB entry text was searched for "sky", "heaven" and "came from"; the only hit inside the BDB entry is "God of heaven" (אלהי השמים). No sense "those who came from the sky" is given. Plural form: given. Class: unassigned (see Answer).

**Case 2. TBWTT-2:9 / 2:10, Genesis 1:5, « jour ».**
- 2:9: « «Il y eut un soir, il y eut un matin : premier jour». (Genèse, I-5) »
- 2:10: « Ces études prirent pas mal de temps. Le «jour» correspond à la période pendant laquelle votre soleil se lève sous le même signe le jour de l'équinoxe de printemps, soit deux mille ans terrestres environ. »
- TLFi, JOUR: "II. — [Jour implique la notion de temps] … PHILOS., RELIG. [Jour en dehors du temps de l'homme] Jours de la création" (with the example "Croyons que les jours de la création … furent les jours de Dieu, les longs jours du monde"); "B. — Espace de temps qui s'écoule pendant une rotation complète de la terre sur elle-même, période de 24 heures"; "2. [Jour désigne une période de temps qui se prolonge, une époque]".
- Hebrew, GEN-WOH-1:5 (`text`): … וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם אֶחָֽד׃
- BDB (Strong 3117): "1 day, opposed to night … Genesis 1:5,14,16,18 (P)"; "d. day as defined by evening and morning Genesis 1:5,8,13,19,23,31 (all P …)"; and elsewhere in the entry "6 יוֺם = time; a. vividly in General sense".
- Strong's: "a day (as the warm hours), whether literal (from sunrise to sunset, or from one sunset to the next), or figurative (a space of time defined by an associated term)".
- Commentaries on the Bible Hub page for Genesis 1:5 divide. One (first on the page, under the heading "Ellicott's Commentary for English Readers"): "A creative day is not a period of twenty-four hours, but an œon, or period of indefinite duration". Others on the same page (attribution by position on the page not verified): "The days of this creation are natural days of twenty-four hours each."; "The Israelite writer, therefore, in speaking of the days of Creation, describes them as ordinary days with their succession of evening and morning."
- Class: `disputed`. BDB files this verse under the evening-and-morning day; the word has "time" as a sense elsewhere; commentaries divide on the creation days. No lexicon consulted gives a length of two thousand years or a link to the equinox.

**Case 3. TBWTT-2:26 / 2:27, Genesis 1:26, « image », « ressemblance ».**
- 2:26: « «Faisons l'homme à notre image, à notre ressemblance ! … ». (Genèse, I-26) »
- 2:27: « A notre image! Vous pouvez constater que la ressemblance est frappante. »
- TLFi, IMAGE: "— À l'image de. Sur le modèle de, à la ressemblance de, en conformité avec. Être (fait) à l'image de."
- Hebrew, GEN-WOH-1:26 (`text`): … נַֽעֲשֶׂ֥ה אָדָ֛ם בְּצַלְמֵ֖נוּ כִּדְמוּתֵ֑נוּ …
- BDB צֶלֶם (Strong 6754): "image (something cut out …) … 1 images of tumours and mice (of gold) … especially of heathen gods … of painted pictures of men … 2 image, likeness, of resemblance, … of God's making man in his own image, Genesis 1:26". BDB דְּמוּת (Strong 1823): "likeness, similitude … 1 likeness, similitude, of external appearance, chiefly in Ezek."
- Class: `shared`.

**Case 4. TBWTT-2:42 / 2:43, Genesis 3:22, « science ».**
- 2:42: « «Voici que l'homme est devenu comme l'un de nous, grâce à la - science (...). Maintenant il faut éviter qu'il étende sa main, prenne aussi de l'arbre de vie, en mange et vive à jamais». (Genèse, III-22) »
- 2:43: « La vie des hommes est très courte et il existe un moyen scientifique de la prolonger très longtemps. Un savant qui étudie toute sa vie commence à posséder suffisamment de connaissances pour faire des découvertes intéressantes quand il devient vieux, d'où la lenteur des progrès humains. Si les hommes pouvaient vivre dix fois plus longtemps, ils feraient un bond scientifique gigantesque. »
- TLFi, SCIENCE: "I. — Littér. ou vieilli, au sing. Somme de connaissances qu'un individu possède ou peut acquérir par l'étude, la réflexion ou l'expérience. A. — Connaissance approfondie des choses dans ce qu'elles sont." (the phrase "l'arbre de la science du bien et du mal" appears among the examples placed before section II on the page); "II. — Ensemble structuré de connaissances qui se rapportent à des faits obéissant à des lois objectives (ou considérés comme tels) et dont la mise au point exige systématisation et méthode."
- Hebrew, GEN-WOH-3:22 (`text`): … הֵ֤ן הָֽאָדָם֙ הָיָה֙ כְּאַחַ֣ד מִמֶּ֔נּוּ לָדַ֖עַת ט֣וֹב וָרָ֑ע …
- BDB יָדַע (Strong 3045): "Infinitive construct … דַּ֫עַת Genesis 3:22"; "1. a. know, learn to know, good and evil Genesis 3:22 (J)". BDB דַּעַת (Strong 1847): "d. especially knowledge with moral quality Genesis 2:9,17 (J; in both verbal force, הַדּ׳ טוֺב וָרַע the knowing good and evil)".
- Class: `french_only`. The Hebrew has a verb with its object ("to know good and evil"); the French noun « la science » stands alone because the object falls under « (...) », and the commentary takes it in TLFi sense II. Caveat for anyone redoing the count: TLFi sense I ("connaissance") is what the Hebrew has; a reader who takes the commentary to need no more than "knowledge" would mark this `shared`.

**Case 5. TBWTT-2:59 / 2:60, Genesis 7:17, « s'éleva au-dessus de la terre ».**
- 2:59: « «(...) l'arche (...) s'éleva au-dessus de la terre». (Genèse, VII-17) »
- 2:60: « Vous pouvez constater qu'il est bien dit qu'elle s'éleva audessus de la Terre et non pas sur les eaux. »
- TLFi, ÉLEVER: "— Emploi pronom. réfl. S'élever en l'air, dans les airs."
- Hebrew, GEN-WOH-7:17 (`text`): וַֽיְהִ֧י הַמַּבּ֛וּל אַרְבָּעִ֥ים י֖וֹם עַל־הָאָ֑רֶץ וַיִּרְבּ֣וּ הַמַּ֗יִם וַיִּשְׂאוּ֙ אֶת־הַתֵּבָ֔ה וַתָּ֖רָם מֵעַ֥ל הָאָֽרֶץ׃
- BDB רוּם (Strong 7311): "3 be lifted, rise, of ark, מֵעַל הארץ Genesis 7:17 (J), so of cherubim Ezekiel 10:16". Strong's עַל (5921): "above, over, upon, or against". BDB אֶרֶץ (Strong 776): "1. a. earth, whole earth (opposed to a part) … b. earth, opposed to heaven, sky".
- Class: `shared` for the sense of the words (rise; above/from upon; earth). The BDB entry for מֵעַל was not reached. See "Absent or ambiguous" for what the two « (...) » omit and for Genesis 7:18.

**Case 6. TBWTT-2:62, Genesis 6:16, « étages ».**
- 2:62: « Et la fusée à trois étages («tu la disposeras en étages, l'inférieur, le second et le troisième») se posa sur la Terre. »
- TLFi, ÉTAGE: "— ASTRONAUT. Chacun des éléments d'un engin composite. Fusée à trois étages."
- Hebrew, GEN-WOH-6:16 (`text`): … תַּחְתִּיִּ֛ם שְׁנִיִּ֥ם וּשְׁלִשִׁ֖ים תַּֽעֲשֶֽׂהָ׃
- BDB תַּחְתִּי (Strong 8482): "adjective and substantive lower, lowest (places) … Genesis 6:16 (P) תַּחְתִּיִּם = lower stories". BDB שֵׁנִי (Strong 8145): "Genesis 6:16 second stories (in ark)".
- Class: `french_only`. The Hebrew has three adjectives used as nouns and no word for « étages »; the lexicon sense is storeys of a structure; the rocket-stage sense is in the French dictionary only.

**Case 7. TBWTT-2:67 / 2:68, Genesis 8:21, « objet ».**
- 2:67: « «(...) l'objet du cœur de l'homme est le mal». (Genèse, VIII-21) »
- 2:68: « Le but de l'homme est le progrès scientifique. »
- TLFi, OBJET: "— Ce que l'on pose comme finalité de l'activité, de son moyen ou de son résultat. Synon. but, fin, objectif."
- Hebrew, GEN-WOH-8:21 (`text`): … כִּ֠י יֵ֣צֶר לֵ֧ב הָאָדָ֛ם רַ֖ע מִנְּעֻרָ֑יו …
- BDB יֵצֶר (Strong 3336): "form, framing, purpose … 4 of what is framed in the mind …, imagination, device, purpose: … יֵ׳ לב Genesis 8:21 (J)". Strong's: "a form; figuratively, conception (i.e. Purpose)".
- Class: `shared` for « objet » = « but ». The other half of 2:68 (« le mal » = « le progrès scientifique ») is a redefinition and was not classified.

**Case 8. TBWTT-3:49 / 3:48, Numbers 18:13, « primeurs ».**
- 3:48: « Mais cette manne n'était qu'une nourriture chimique à laquelle les créateurs préféraient les fruits et légumes frais. »
- 3:49: « «Les primeurs de tout ce qui sera en leur pays et qu'ils apporteront à Iahvé». (Nombres, XVIII-13) »
- TLFi, PRIMEUR: "C. — Gén. au plur. Fruit ou légume précoce arrivant à maturité avant ceux de son espèce, et en partic. fruit ou légume apparaissant sur le marché avant la saison normale".
- Hebrew, Num 18:13 (UXLC): בִּכּוּרֵ֞י כָּל־אֲשֶׁ֧ר בְּאַרְצָ֛ם אֲשֶׁר־יָבִ֥יאוּ לַיהוָ֖ה …
- BDB בִּכּוּרִים (Strong 1061): "noun masculine first-fruits … construct בִּכּוּרֵי … Numbers 18:13 (P) … — the first of grain and ftuit that ripened and was gathered and offered to God according to the ritual" [sic, "ftuit" on the page]. Strong's: "the first-fruits of the crop -- first fruit (-ripe (figuratively)), hasty fruit".
- Class: `shared` (first-ripened produce). The lexicon says grain and fruit; it does not say vegetables.

**Case 9. TBWTT-3:93 / 3:94, 1 Samuel 17:26, « vivant ».**
- 3:93: « «Qui (...) insulte les troupes du Dieu vivant ?» (I Samuel, XVII-26) »
- 3:94: « Ce qui montre bien la réalité de la présence à cette époque d'un «Dieu» tout à fait palpable... »
- TLFi, VIVANT: "II. — Adjectif A. — 1. [P. oppos. à mort, morte] Qui vit, qui est en vie; dont les fonctions de la vie se manifestent de manière perceptible."
- Hebrew, 1 Sam 17:26 (UXLC): … כִּ֣י חֵרֵ֔ף מַעַרְכ֖וֹת אֱלֹהִ֥ים חַיִּֽים׃
- BDB חַי (Strong 2416): "adjective alive, living … 1. a. of God, as the living one, the fountain of life … אלהים חיים Deuteronomy 5:23; 1 Samuel 17:26,36".
- Class: `shared` (alive, living). "Palpable" is the commentary's inference; it is not a sense in either dictionary.

**Case 10. TBWTT-3:146 / 3:147, Isaiah 13:5, « des confins du ciel ».**
- 3:146: « … Ils viennent d'un pays lointain, des confins du ciel, Iahvé et les instruments de son courroux, pour détruire tout le pays». (Isaïe, XIII, 4-5) »
- 3:147: « Toute la vérité est décrite ici. Il fallait lire entre les lignes et comprendre. «Ils viennent d'un pays lointain, des confins du ciel». on ne pouvait être plus clair. »
- TLFi, CONFINS: "Parties d'un territoire formant la limite extrême où commence un territoire immédiatement voisin. 1. … Parties extrêmes de." TLFi, CIEL: "I. — Domaine physique A. — ASTRON., COSMOGRAPHIE 1. Espace infini dans lequel évoluent les astres".
- Hebrew, Isa 13:5 (UXLC; chapter 13 is not in `isaiah-woh`): בָּאִ֛ים מֵאֶ֥רֶץ מֶרְחָ֖ק מִקְצֵ֣ה הַשָּׁמָ֑יִם יְהוָה֙ וּכְלֵ֣י זַעְמ֔וֹ לְחַבֵּ֖ל כָּל־הָאָֽרֶץ׃
- BDB קָצֶה (Strong 7097): "end, extremity … מִק׳ הַשָׁמַיִם Isaiah 13:5 ("" מֵאֶרֶץ מֶרְחָק)". BDB שָׁמַיִם (Strong 8064): "heavens, sky … 1. a. visible heavens, sky, where stars, etc., are".
- Class: `shared` (end of the heavens; far land).

**Case 11. TBWTT-3:241 / 3:242, Psalm 19:7, « orbite ».**
- 3:241: « «(...) son point de départ est à un bout des cieux et son orbite à l'autre bout...». (Psaumes, XIX-7) »
- 3:242: « Les créateurs sont venus d'une planète très éloignée de l'orbite terrestre. »
- TLFi, ORBITE: "II. A. — ASTRON. Courbe fermée qu'un corps céleste décrit dans l'espace sous l'action de l'attraction universelle et de forces d'inertie. … ellipticité de l'orbite terrestre."
- Hebrew, Ps 19:7 (UXLC): מִקְצֵ֤ה הַשָּׁמַ֨יִם ׀ מֽוֹצָא֗וֹ וּתְקוּפָת֥וֹ עַל־קְצוֹתָ֑ם וְאֵ֥ין נִ֝סְתָּ֗ר מֵֽחַמָּתוֹ׃
- BDB תְּקוּפָה (Strong 8622): "coming round, circuit … singular suffix of finished circuit of sun Psalm 19:7 (opposed to מוֺצָאוֺ …)". Strong's: "a revolution, i.e. (of the sun) course". BDB מוֹצָא (Strong 4161): "1 a going forth: a. the act … of the sun = rising Psalm 19:7".
- Class: `shared` for the word (the circuit of a heavenly body). What the lexica do not support is the change of owner: BDB reads both suffixes as the sun's (its rising, its circuit); Ps 19:5 (UXLC) has לַשֶּׁמֶשׁ. The commentary makes the departure the creators' and the orbit the Earth's.

**Case 12. TBWTT-3:250 / 3:251, Job 1:6, « Elohim ».**
- 3:250: « «Il advint un jour que les fils d'Elohim vinrent se présenter devant Iahvé et Satan vint aussi parmi eux». (Job, I-6) »
- 3:251: « Elohim, cela veut dire littéralement «venus du ciel» en Hébreu. Les fils d'Elohim, donc les créateurs qui surveillent les hommes, font régulièrement des rapports sur leur planète d'origine … »
- Hebrew, JOB-WOH-1:6 (`text`): וַיְהִ֣י הַיּ֔וֹם וַיָּבֹ֙אוּ֙ בְּנֵ֣י הָאֱלֹהִ֔ים לְהִתְיַצֵּ֖ב עַל־יְהוָ֑ה וַיָּב֥וֹא גַֽם־הַשָּׂטָ֖ן בְּתוֹכָֽם׃
- BDB (Strong 430): "c. angels … compare בני (ה)אלהים = (the) sons of God, or sons of gods = angels Job 1:6; Job 2:1; Job 38:7; Genesis 6:2,4".
- Class: unassigned, as case 1.

**Case 13. TBWTT-3:276 / 3:277, Jeremiah 10:14, « science ».**
- 3:276: « «Tout homme est abruti, faute de science (...)». (Jérémie, X-14) »
- 3:277: « Cette science qui a permis aux créateurs de créer et permettra aux hommes d'en faire autant : »
- TLFi, SCIENCE: as in case 4.
- Hebrew, Jer 10:14 (UXLC): נִבְעַ֤ר כָּל־אָדָם֙ מִדַּ֔עַת …
- BDB דַּעַת (Strong 1847): "knowledge … 1. a. knowledge, perception … b. = skill (in work-manship) Exodus 31:3; Exodus 35:31 … creative skill Isaiah 40:14 … 2 especially in Wisdom Literature = discernment, understanding, wisdom: a. … Jeremiah 10:14 = Jeremiah 51:17". Strong's: "knowledge -- cunning, (ig-)norantly, know(-ledge)".
- Class: `shared` at the level of the word (knowledge; skill in workmanship; creative skill). BDB files this verse under "discernment, understanding, wisdom", not under skill; and TLFi sense II (systematised science) is narrower than any BDB sense. A reader who holds the commentary to TLFi sense II would mark this `french_only`, as in case 4.

## Absent or ambiguous

- The digitization does not name the French Bible translation the book quotes from. I did not identify it.
- The Elohim gloss (cases 1 and 12) is presented by the book as the meaning of the Hebrew word. The lexica consulted (BDB, Strong's) do not contain it. I did not consult a lexicon that discusses the etymology of אלה at length, so "not found in BDB and Strong's as reproduced on Bible Hub" is the extent of the check.
- Genesis 7:17 (case 5): the first « (...) » in 2:59 stands where the Hebrew has וַיִּרְבּוּ הַמַּיִם וַיִּשְׂאוּ אֶת־הַתֵּבָה (the waters as subject of the verb that takes the ark as object). The next verse, GEN-WOH-7:18 (`text`), reads וַתֵּ֥לֶךְ הַתֵּבָ֖ה עַל־פְּנֵ֥י הַמָּֽיִם׃. The commentary's « et non pas sur les eaux » is a statement about what "is said"; these are the Hebrew words on either side of the quoted clause. Commentaries on the Bible Hub page for the verse read it as flotation ("raised up the ark till it floated").
- TBWTT-3:37 (« Il entrerait dans la tente du rendez-vous ») carries no reference and I did not locate the exact clause; only the phrase אֹהֶל מוֹעֵד was confirmed at Exod 33:7. TBWTT-3:216 carries no reference; I did not open the verse.
- The classification `disputed` for case 2 rests on commentaries reproduced on one aggregator page; apart from the first, their attribution was not verified.
- The Hebrew of the 150 `image_step` and 3 `no_explanation` quotations was not compared with the French, except for the borderlines named above. The list of French words with no Hebrew counterpart below is therefore not exhaustive.
- Daniel 3:25 and 6:23 are Aramaic; they were counted (the brief admits Aramaic originals) and not examined further.

## Adjacent observations

- **French words with no counterpart in the Hebrew verse, where the commentary uses them.**
  - TBWTT-3:243-244 / 3:245, Psalm 19:5: « «Pour le soleil, il a dressé une tente sur la mer (...)». » then « Nouvelle allusion à l'amas de terre qui fut créé quand l'océan recouvrait la Terre et forma le continent originel. » UXLC Ps 19:5 ends לַ֝שֶּׁ֗מֶשׁ שָֽׂם־אֹ֥הֶל בָּהֶֽם׃. The last word is בָּהֶם ("in them"); the verse as given in UXLC has no word for "sea". The commentary's link to the ocean depends on « sur la mer ». I searched the Bible Hub commentary page for Ps 19:4 for "sea" and found nothing; I did not find where the French reading comes from.
  - TBWTT-2:62, Genesis 6:16: « étages » (case 6); the Hebrew has no noun there.
  - TBWTT-2:42, Genesis 3:22: « grâce à la » has no separate Hebrew word (the Hebrew is ל + infinitive), and « (...) » stands where the Hebrew has טוֹב וָרָע (case 4).
- **Parenthetical words inside quotations.** The French marks some insertions itself with round brackets: « (pour les uns) … (pour les autres) » 3:13; « (précieuses) » and « etc. » 3:35; « (sur la note) » 3:64; « (voué) » 3:81; « (la main) » 3:99; « (entre Elie et Elisée) » 3:132; « (qui était) » 3:162; « (les ossements) » 3:185; « (il y avait) » 3:188; « (ces vêtements) » 3:191; « (9 mètres) » and « (4,50 mètres) » 3:234-235; « (et) » 2:63. I did not check each against the Hebrew.
- **A French sense used outside any quotation window.** TBWTT-3:189: « … de même qu'en raison de notre petite taille on nous prend pour des enfants, des chérubins... » TLFi, CHÉRUBIN: "Représentation sculptée, peinte... d'un chérubin, sous la forme d'une tête d'enfant"; "C. — P. anal. 1. P. compar., fam. [En parlant d'enfants]". BDB כְּרוּב (Strong 3742): "noun masculine cherub … 1 the living chariot of the theophanic God". The quotation in the window (3:188, Ezek 40:2-3) does not contain the word; the quotations that do (2:44, 3:178, 3:179) are outside the window, so this was not counted.
- **A phrase moved from one subject to another.** TBWTT-3:71 on Joshua 10:13: « … puisqu'il est dit plus loin qu'elle dura «presque un jour entier». » ("elle" is the war). UXLC Josh 10:13: … וַיַּעֲמֹ֤ד הַשֶּׁ֙מֶשׁ֙ בַּחֲצִ֣י הַשָּׁמַ֔יִם וְלֹא־אָ֥ץ לָב֖וֹא כְּי֥וֹם תָּמִֽים׃ BDB יוֹם: "כְּיוֺם תָּמִים Joshua 10:13 about a whole day". In the Hebrew the phrase is attached to the sun's not hastening to set.
- **Other lexicon notes on words the commentary passes over.** TBWTT-3:278 (Prov 8:30) « comme architecte »: BDB II. אָמוֹן (Strong 525): "artificer, architect, master-workman … (… > foster-son AE Ki AV) Proverbs 8:30", so the lexicon records a divided tradition; the commentary at 3:279 does not lean on the word. TBWTT-2:34 quotes « vous serez comme des dieux »; GEN-WOH-3:5 (`text`) has כֵּֽאלֹהִ֔ים, the same word the book elsewhere leaves as « Elohim ».
- **The same Hebrew word under two French words.** רָקִיעַ is « firmament » in the book's Genesis quotations (2:11, 2:17; GEN-WOH-1:7 `text` has לָרָקִיעַ) and « plate-forme » in its Ezekiel quotation (3:162; UXLC Ezek 1:22 רָקִ֔יעַ). The two commentaries (clouds and ocean at 2:12; the large vehicle at 3:166) differ accordingly.
- **Typography of the digitization.** 2:42 reads « grâce à la - science (...) » with a stray hyphen; 2:60 « audessus »; 2:75 and 3:164 open or close a quotation without the matching « or »; 3:17 has a doubled closing mark. 3:305 is an editorial caption about the symbol, not part of the 1974 text's dialogue.
