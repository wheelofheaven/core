# Finding: woh-exp-0010

- Date: 2026-11-22
- Source and edition inspected:
  - Genesis: project edition `data-library/genesis-woh/chapter-1.json`, `chapter-5.json`, `chapter-9.json` (GEN-WOH, translation version 1.1.0; its declared source text is "Tanach with Ta'amei Hamikra (Westminster Leningrad)", accessed via sefaria.org). Fields read: `text` (Hebrew), `i18n.en`, `notes.official`.
  - Lexicon: Brown-Driver-Briggs, entry צֶלֶם (and the Biblical Aramaic entry צְלֵם printed with it), as reproduced by BibleHub at `https://biblehub.com/bdb/6754.htm` and `https://biblehub.com/hebrew/6754.htm` (Strong's no. 6754). HALOT was not reached.
  - Concordance: BibleHub Englishman's Hebrew Concordance, `https://biblehub.com/hebrew/strongs_6754.htm` (Hebrew, 6754) and `https://biblehub.com/hebrew/6755.htm` (Aramaic, 6755).
  - Masoretic text for all verses outside Genesis (and a cross-check of the Genesis verses): Sefaria API, `https://www.sefaria.org/api/v3/texts/<Ref>?version=hebrew`, version title returned: "Miqra according to the Masorah".
- Access achieved: `full_text` (Genesis edition: `project_digitization`; BDB: full entry text as reproduced on a public site, not the printed page; MT: full text of every listed verse).
- Search performed:
  1. Read GEN-WOH-1:26, 1:27, 5:1, 5:2, 5:3, 9:6 in the project files.
  2. Downloaded the two BibleHub pages for 6754 and extracted the BDB entry text from the raw HTML (not from a summary). Downloaded `bdb/6755.htm`: it carries no BDB text of its own; the Aramaic BDB entry is printed at the end of the 6754 entry.
  3. Took the occurrence list from the BDB entry and checked it against the Englishman's Concordance list (17 Hebrew hits; 17 Aramaic hits). The two lists agree on the verses.
  4. Fetched each listed verse from Sefaria: Numbers 33:52; 1 Samuel 6:5, 6:11; 2 Kings 11:18; 2 Chronicles 23:17; Psalms 39:7, 73:20; Ezekiel 7:20, 16:17, 23:14; Amos 5:26; Genesis 1:26, 1:27, 5:3, 9:6; Daniel 2:31-35; Daniel 3:1-19.
  5. In the Daniel ranges, counted every word whose consonants contain צלם / צלמ (17 found, matching the concordance verse by verse).
  6. Not done: no independent whole-Bible consonantal search for צלם outside the verses the lexicon and concordance list. The occurrence list therefore rests on BDB plus the Englishman's Concordance, as the brief specifies.

## Answer

**Genesis (project edition).** The noun rendered "image" is צֶלֶם (tselem); the noun rendered "likeness" is דְּמוּת (demut).

| Verse | "image" noun | "likeness" noun | Order |
|---|---|---|---|
| 1:26 | בְּצַלְמֵנוּ (tselem) | כִּדְמוּתֵנוּ (demut) | tselem with בְּ first, demut with כְּ second |
| 1:27 | בְּצַלְמוֹ, בְּצֶלֶם אֱלֹהִים (tselem, twice) | none | tselem only |
| 5:1 | none | בִּדְמוּת אֱלֹהִים (demut) | demut only |
| 5:2 | none | none | neither noun |
| 5:3 | כְּצַלְמוֹ (tselem) | בִּדְמוּתוֹ (demut) | demut with בְּ first, tselem with כְּ second |
| 9:6 | בְּצֶלֶם אֱלֹהִים (tselem) | none | tselem only |

**Is the same noun used at Genesis 5:3?** Yes. Genesis 5:3 has כְּצַלְמוֹ, the same noun צֶלֶם as 1:26-27, and BDB lists 5:3 under the same sense as 1:26-27 and 9:6. Relative to 1:26, the order of the two nouns and the prepositions attached to them are swapped (1:26 בְּ + tselem, כְּ + demut; 5:3 בְּ + demut, כְּ + tselem).

**Hebrew occurrences outside Genesis** (BDB entry צֶלֶם; 12 occurrences in 11 verses):

| # | Verse | Form | Class | BDB's own gloss for the verse |
|---|---|---|---|---|
| 1 | Numbers 33:52 | צַלְמֵי מַסֵּכֹתָם | `concrete_object` | "their molten images" |
| 2 | 1 Samuel 6:5 (first) | צַלְמֵי טְחֹרֵיכֶם (ketiv עפליכם) | `concrete_object` | "images of tumours and mice (of gold)" |
| 3 | 1 Samuel 6:5 (second) | וְצַלְמֵי עַכְבְּרֵיכֶם | `concrete_object` | same |
| 4 | 1 Samuel 6:11 | צַלְמֵי טְחֹרֵיהֶם | `concrete_object` | same |
| 5 | 2 Kings 11:18 | צְלָמָיו | `concrete_object` | "especially of heathen gods ... (both with verb שִׁבְּרוּ)" |
| 6 | 2 Chronicles 23:17 | צְלָמָיו | `concrete_object` | same |
| 7 | Ezekiel 7:20 | וְצַלְמֵי תוֹעֲבֹתָם | `concrete_object` | listed under "especially of heathen gods" |
| 8 | Ezekiel 16:17 | צַלְמֵי זָכָר | `concrete_object` | "(i.e. in male form, according to figurative of harlotry for idolatry)" |
| 9 | Ezekiel 23:14 | צַלְמֵי כַשְׂדִּים (ketiv כשדיים) | `concrete_object` | "of painted pictures of men" |
| 10 | Amos 5:26 | צַלְמֵיכֶם | `concrete_object` (text marked dubious by BDB; see below) | "especially of heathen gods Amos 5:26 (text dubious; strike out We as gloss ...)" |
| 11 | Psalm 39:7 (English 39:6) | בְּצֶלֶם | `non_concrete` | "as (ב essentiae) a (mere) semblance man walks about" |
| 12 | Psalm 73:20 | צַלְמָם | `non_concrete` | "thou wilt despise their semblance" |

**Totals, Hebrew outside Genesis:** `concrete_object` 10 occurrences (9 verses); `non_concrete` 2 occurrences (2 verses); `unclear` 0. If Amos 5:26 is set aside because BDB calls its text dubious, the count is 9 / 2 / 0 with one withheld.

**Genesis occurrences** (not classified; outside the classification scope of the protocol): 5 occurrences in 4 verses (1:26; 1:27 twice; 5:3; 9:6). BDB puts all five in a sense of their own, separate from both groups above: "2 image, likeness, of resemblance".

**Aramaic occurrences (Daniel), listed separately** (BDB entry צְלֵם, "17"; 17 occurrences in 15 verses): Daniel 2:31 (twice), 2:32, 2:34, 2:35; 3:1, 3:2, 3:3 (twice), 3:5, 3:7, 3:10, 3:12, 3:14, 3:15, 3:18, 3:19.
- `concrete_object`: 16 (the statue of the dream, 2:31-35, five occurrences; the gold statue set up by Nebuchadnezzar, 3:1-18, eleven occurrences). BDB gloss: "image".
- `non_concrete`: 1 (Daniel 3:19, צְלֵם אַנְפּוֹהִי, "the image of his face"; BDB: "i.e. his expression").
- `unclear`: 0.

## Quotations

### Genesis, project edition (genesis-woh)

- GEN-WOH-1:26 — `וַיֹּ֣אמֶר אֱלֹהִ֔ים נַֽעֲשֶׂ֥ה אָדָ֛ם בְּצַלְמֵ֖נוּ כִּדְמוּתֵ֑נוּ ...` — i18n.en: "And the Elohim said, "Let us make humankind in our image, according to our likeness; ..."
- GEN-WOH-1:27 — `וַיִּבְרָ֨א אֱלֹהִ֤ים ׀ אֶת־הָֽאָדָם֙ בְּצַלְמ֔וֹ בְּצֶ֥לֶם אֱלֹהִ֖ים בָּרָ֣א אֹת֑וֹ זָכָ֥ר וּנְקֵבָ֖ה בָּרָ֥א אֹתָֽם׃` — i18n.en: "And the Elohim shaped humankind in their image; in the image of the Elohim they shaped him; male and female they shaped them."
- GEN-WOH-5:1 — `זֶ֣ה סֵ֔פֶר תּוֹלְדֹ֖ת אָדָ֑ם בְּי֗וֹם בְּרֹ֤א אֱלֹהִים֙ אָדָ֔ם בִּדְמ֥וּת אֱלֹהִ֖ים עָשָׂ֥ה אֹתֽוֹ׃` — i18n.en: "This is the record of the begettings of Adam. On the day the Elohim shaped Adam, in the likeness of Elohim they made him."
- GEN-WOH-5:2 — `זָכָ֥ר וּנְקֵבָ֖ה בְּרָאָ֑ם וַיְבָ֣רֶךְ אֹתָ֗ם וַיִּקְרָ֤א אֶת־שְׁמָם֙ אָדָ֔ם בְּי֖וֹם הִבָּֽרְאָֽם׃` — i18n.en: "Male and female they shaped them. They blessed them, and they called their name Adam on the day they were shaped."
- GEN-WOH-5:3 — `וַֽיְחִ֣י אָדָ֗ם שְׁלֹשִׁ֤ים וּמְאַת֙ שָׁנָ֔ה וַיּ֥וֹלֶד בִּדְמוּת֖וֹ כְּצַלְמ֑וֹ וַיִּקְרָ֥א אֶת־שְׁמ֖וֹ שֵֽׁת׃` — i18n.en: "Adam lived one hundred and thirty years, and fathered a son in his own likeness, after his own image, and called his name Shet."
- GEN-WOH-9:6 — `שֹׁפֵךְ֙ דַּ֣ם הָֽאָדָ֔ם בָּֽאָדָ֖ם דָּמ֣וֹ יִשָּׁפֵ֑ךְ כִּ֚י בְּצֶ֣לֶם אֱלֹהִ֔ים עָשָׂ֖ה אֶת־הָאָדָֽם׃` — i18n.en: "One who sheds the blood of the human — by the human his blood shall be shed; for in the image of the Elohim, they made the human."

The Sefaria "Miqra according to the Masorah" text of Genesis 1:26, 1:27, 5:3 and 9:6 has the same words at the relevant points (differences seen are orthographic only, e.g. וּבְכׇל for וּבְכָל, וַיְחִי for וַֽיְחִי).

### Brown-Driver-Briggs, entry צֶלֶם (BibleHub reproduction, biblehub.com/bdb/6754.htm), in full as displayed

> צֶ֫לֶם noun masculine Ezekiel 16:17 image (something cut out, compare מֶּסֶל; Nö 'Schnitzbild'); — ׳צ absolute Psalm 39:7, construct Genesis 1:27 +; suffix צַלְמוֺ Genesis 1:27; Genesis 5:3, צַלְמֵנוּ Genesis 1:26, צַלְמָם Psalm 73:20; plural construct צַלְמֵי 1 Samuel 6:5 (twice in verse) +, suffix צְלָמָיו 2 Kings 11:18; 2Chronicles 23:17, צַלְמֵיכֶם Amos 5:26; —
> 1 images of tumours and mice (of gold) 1 Samuel 6:5 (twice in verse); 1 Samuel 6:11; especially of heathen gods Amos 5:26 (text dubious; strike out We as gloss, compare GASm Dr), 2 Kings 11:18 2Chronicles 23:17 (both with verb שִׁבְּרוּ), Ezekiel 7:20, so זָכָר ׳צ Ezekiel 16:17 (i.e. in male form, according to figurative of harlotry for idolatry); צַלְמֵי מַסֵכֹתָם Numbers 33:52 their molten images; of painted pictures of men Ezekiel 23:14.
> 2 image, likeness, of resemblance, ׳בְּצ (בָּרָא) עָשָׂה, of God's making man in his own image, Genesis 1:26 ("" כִּדְמוּתֵנוּ), Genesis 1:27; Genesis 1:27; Genesis 9:6, ׳כְּצ Genesis 5:3 ("" בִּדְמוּתוֺ; all P).
> 3 figurative = mere, empty, image, semblance, ׳בְּצ Psalm 39:7 as (ב essentiae) a (mere) semblance man walks about; צַלְמָם תִּבְזֶה Psalm 73:20 thou wilt despise their semblance.

### Brown-Driver-Briggs, Biblical Aramaic entry צְלֵם (same page)

> צְלֵם 17 noun masculine Daniel 2:31 image (see Biblical Hebrew צלם); — absolute ׳צ Daniel 2:31; Daniel 3:1; construct ׳צ Daniel 3:19, צֶ֫לֶם Daniel 3:5 +; emphatic צַלְמָא Daniel 2:31 +; — image Daniel 2:31 (twice in verse); Daniel 2:32,34,35; Daniel 3:1 10t. 3; אַנֶמּוֺהִי ׳צ Daniel 3:19 i.e. his expression.

### Masoretic text, Sefaria ("Miqra according to the Masorah"), Hebrew occurrences outside Genesis

- Numbers 33:52 — `וְה֨וֹרַשְׁתֶּ֜ם אֶת־כׇּל־יֹשְׁבֵ֤י הָאָ֙רֶץ֙ מִפְּנֵיכֶ֔ם וְאִ֨בַּדְתֶּ֔ם אֵ֖ת כׇּל־מַשְׂכִּיֹּתָ֑ם וְאֵ֨ת כׇּל־צַלְמֵ֤י מַסֵּֽכֹתָם֙ תְּאַבֵּ֔דוּ וְאֵ֥ת כׇּל־בָּמוֹתָ֖ם תַּשְׁמִֽידוּ׃`
- 1 Samuel 6:5 — `וַעֲשִׂיתֶם֩ צַלְמֵ֨י (עפליכם) [טְחֹרֵיכֶ֜ם] וְצַלְמֵ֣י עַכְבְּרֵיכֶ֗ם הַמַּשְׁחִיתִם֙ אֶת־הָאָ֔רֶץ וּנְתַתֶּ֛ם לֵאלֹהֵ֥י יִשְׂרָאֵ֖ל כָּב֑וֹד ...`
- 1 Samuel 6:11 — `וַיָּשִׂ֛מוּ אֶת־אֲר֥וֹן יְהֹוָ֖ה אֶל־הָעֲגָלָ֑ה וְאֵ֣ת הָאַרְגַּ֗ז וְאֵת֙ עַכְבְּרֵ֣י הַזָּהָ֔ב וְאֵ֖ת צַלְמֵ֥י טְחֹרֵיהֶֽם׃`
- 2 Kings 11:18 — `וַיָּבֹ֣אוּ כׇל־עַם֩ הָאָ֨רֶץ בֵּית־הַבַּ֜עַל וַֽיִּתְּצֻ֗הוּ אֶת־מִזְבְּחֹתָ֤ו וְאֶת־צְלָמָיו֙ שִׁבְּר֣וּ הֵיטֵ֔ב ...`
- 2 Chronicles 23:17 — `וַיָּבֹ֨אוּ כׇל־הָעָ֤ם בֵּית־הַבַּ֙עַל֙ וַֽיִּתְּצֻ֔הוּ וְאֶת־מִזְבְּחֹתָ֥יו וְאֶת־צְלָמָ֖יו שִׁבֵּ֑רוּ ...`
- Psalm 39:7 — `אַךְ־בְּצֶ֤לֶם ׀ יִֽתְהַלֶּךְ־אִ֗ישׁ אַךְ־הֶ֥בֶל יֶהֱמָי֑וּן יִ֝צְבֹּ֗ר וְֽלֹא־יֵדַ֥ע מִֽי־אֹסְפָֽם׃`
- Psalm 73:20 — `כַּחֲל֥וֹם מֵהָקִ֑יץ אֲ֝דֹנָ֗י בָּעִ֤יר ׀ צַלְמָ֬ם תִּבְזֶֽה׃`
- Ezekiel 7:20 — `וּצְבִ֤י עֶדְיוֹ֙ לְגָא֣וֹן שָׂמָ֔הוּ וְצַלְמֵ֧י תוֹעֲבֹתָ֛ם שִׁקּוּצֵיהֶ֖ם עָ֣שׂוּ ב֑וֹ עַל־כֵּ֛ן נְתַתִּ֥יו לָהֶ֖ם לְנִדָּֽה׃`
- Ezekiel 16:17 — `וַתִּקְחִ֞י כְּלֵ֣י תִפְאַרְתֵּ֗ךְ מִזְּהָבִ֤י וּמִכַּסְפִּי֙ אֲשֶׁ֣ר נָתַ֣תִּי לָ֔ךְ וַתַּעֲשִׂי־לָ֖ךְ צַלְמֵ֣י זָכָ֑ר וַתִּזְנִי־בָֽם׃`
- Ezekiel 23:14 — `וַתּ֖וֹסֶף אֶל־תַּזְנוּתֶ֑יהָ וַתֵּ֗רֶא אַנְשֵׁי֙ מְחֻקֶּ֣ה עַל־הַקִּ֔יר צַלְמֵ֣י (כשדיים) [כַשְׂדִּ֔ים] חֲקֻקִ֖ים בַּשָּׁשַֽׁר׃`
- Amos 5:26 — `וּנְשָׂאתֶ֗ם אֵ֚ת סִכּ֣וּת מַלְכְּכֶ֔ם וְאֵ֖ת כִּיּ֣וּן צַלְמֵיכֶ֑ם כּוֹכַב֙ אֱלֹ֣הֵיכֶ֔ם אֲשֶׁ֥ר עֲשִׂיתֶ֖ם לָכֶֽם׃`

### Masoretic text, Sefaria, Aramaic (Daniel), sample clauses and forms

- Daniel 2:31 — `... וַאֲל֨וּ צְלֵ֥ם חַד֙ שַׂגִּ֔יא צַלְמָ֨א דִכֵּ֥ן רַ֛ב וְזִיוֵ֥הּ יַתִּ֖יר קָאֵ֣ם לְקׇבְלָ֑ךְ וְרֵוֵ֖הּ דְּחִֽיל׃`
- Daniel 3:1 — `נְבוּכַדְנֶצַּ֣ר מַלְכָּ֗א עֲבַד֙ צְלֵ֣ם דִּֽי־דְהַ֔ב רוּמֵהּ֙ אַמִּ֣ין שִׁתִּ֔ין פְּתָיֵ֖הּ אַמִּ֣ין שִׁ֑ת ...`
- Daniel 3:19 — `בֵּאדַ֨יִן נְבוּכַדְנֶצַּ֜ר הִתְמְלִ֣י חֱמָ֗א וּצְלֵ֤ם אַנְפּ֙וֹהִי֙ (אשתנו) [אֶשְׁתַּנִּ֔י] עַל־שַׁדְרַ֥ךְ מֵישַׁ֖ךְ וַעֲבֵ֣ד נְג֑וֹ ...`
- Forms found, verse by verse: 2:31 צְלֵם, צַלְמָא; 2:32 צַלְמָא; 2:34 לְצַלְמָא; 2:35 לְצַלְמָא; 3:1 צְלֵם; 3:2 צַלְמָא; 3:3 צַלְמָא, צַלְמָא; 3:5 לְצֶלֶם; 3:7 לְצֶלֶם; 3:10 לְצֶלֶם; 3:12 וּלְצֶלֶם; 3:14 וּלְצֶלֶם; 3:15 לְצַלְמָא; 3:18 וּלְצֶלֶם; 3:19 וּצְלֵם. Every occurrence was read with three words of context on each side: 2:32 `ה֣וּא צַלְמָ֗א רֵאשֵׁהּ֙ דִּֽי־דְהַ֣ב טָ֔ב`; 2:34 `וּמְחָ֤ת לְצַלְמָא֙ עַל־רַגְל֔וֹהִי`; 2:35 `וְאַבְנָ֣א ׀ דִּֽי־מְחָ֣ת לְצַלְמָ֗א`; 3:2 and 3:3 `לַחֲנֻכַּ֣ת צַלְמָ֔א דִּ֥י הֲקֵ֖ים נְבוּכַדְנֶצַּ֥ר`; 3:3 `לׇקֳבֵ֣ל צַלְמָ֔א דִּ֥י הֲקֵ֖ים`; 3:5, 3:7, 3:10, 3:12, 3:14, 3:18 `לְצֶ֣לֶם דַּהֲבָ֔א` ("the image of gold"); 3:15 `לְצַלְמָ֣א דִֽי־עַבְדֵת֒`. The statue of 2:31-35 is one seen in a dream; it is classed `concrete_object` because what is described is a statue of metal and clay.

## Absent or ambiguous

- **Amos 5:26.** BDB flags the verse: "text dubious; strike out We as gloss, compare GASm Dr" (that is, Wellhausen deletes the word as a gloss). In the Masoretic text as it stands the word is followed by "the star of your god which you made for yourselves" and is the object of "you carried"; it is classified `concrete_object` on that wording and on BDB's placement of it under "of heathen gods", but the verse is textually disputed and the syntax of סִכּוּת / כִּיּוּן is contested.
- **Psalm 39:7 and 73:20.** BDB's sense 3 is labelled "figurative = mere, empty, image, semblance". They are classed `non_concrete` on that gloss. BDB still treats them as the same noun, used figuratively, not as a separate word. Whether these two belong to the same root as the "cut out" noun or to a different one (a "shadow/darkness" root) is a matter on which lexica differ; that was not checked in HALOT, which was not reached. Strong's (same BibleHub page) gives a different derivation from BDB; see adjacent observations.
- **Psalm verse numbering.** BDB and the Hebrew text number the verse Psalm 39:7; the Englishman's Concordance lists it as Psalm 39:6 (English numbering). Same verse.
- **Ezekiel 23:14.** The figures are "engraved on the wall ... engraved in vermilion" (מְחֻקֶּה עַל־הַקִּיר ... חֲקֻקִים בַּשָּׁשַׁר). BDB: "painted pictures of men". Classed `concrete_object` (picture) under the protocol's definition; these are wall depictions, not free-standing statues.
- **1 Samuel 6:5.** Ketiv/qere at the first occurrence (עפליכם / טְחֹרֵיכֶם); it affects the word for the tumours, not the noun tselem.
- **Daniel 3:19.** The BibleHub reproduction of BDB prints the Aramaic phrase as "אַנֶמּוֺהִי ׳צ", which does not match the Masoretic אַנְפּוֹהִי and appears to be a transcription fault in the online reproduction. The gloss "i.e. his expression" is legible.
- **BDB access.** The entry was read in BibleHub's reproduction, not in a page image of the printed lexicon; abbreviations (Nö, We, GASm, Dr, P) are as displayed and were not expanded from the lexicon's own key.
- **Genesis 5:1.** Contains only דְּמוּת; the noun tselem does not occur in 5:1 or 5:2.
- **Scope not searched.** No consonantal search of the whole Hebrew Bible was run; the list is the lexicon's and the concordance's. No Hebrew occurrence of the noun is listed by either outside the 17 given.

## Adjacent observations

- **BDB's three-way division.** BDB does not file the Genesis verses under the concrete sense (1) nor under the figurative sense (3); it gives them a sense of their own, "2 image, likeness, of resemblance", and marks all five as "P". Its head gloss for the noun as a whole is "image (something cut out, compare מֶּסֶל; Nö 'Schnitzbild')".
- **Strong's on the same page differs from BDB on derivation.** BibleHub's Strong's text for 6754 reads: "From an unused root meaning to shade; a phantom, i.e. (figuratively) illusion, resemblance; hence, a representative figure, especially an idol -- image, vain shew." The NAS Exhaustive Concordance block on the same page gives "NASB Translation form (1), image (5), images (6), likenesses (3), phantom (1)."
- **Prepositions and order at 5:3 versus 1:26.** 1:26 בְּצַלְמֵנוּ כִּדְמוּתֵנוּ; 5:3 בִּדְמוּתוֹ כְּצַלְמוֹ. Same two nouns, reversed order, prepositions exchanged. BDB notes the parallelism in both places ("" כִּדְמוּתֵנוּ; "" בִּדְמוּתוֺ).
- **The project edition's own notes, compared with what was found** (reported as observations about the files read, not as judgments):
  - The official note at GEN-WOH-9:6 says: "This is the third invocation of *tselem Elohim* in Genesis (1:26–27, 5:1, now 9:6)". Genesis 5:1 in the same edition has בִּדְמוּת אֱלֹהִים, not tselem; the edition's own note at GEN-WOH-5:1 says "Only *demut* (likeness) is invoked; *tselem* (image) is held back until the next verse below". (In fact tselem returns at 5:3, two verses on, not the next verse.)
  - The official note at GEN-WOH-1:27 lists "Num 33:52 ..., 1 Sam 6:5 ..., Ezek 7:20, 16:17" as where tselem "elsewhere denotes physical statues/representations". It does not mention Psalm 39:7 or Psalm 73:20, which BDB glosses "(mere) semblance", nor Daniel 3:19.
  - The official note at GEN-WOH-1:26 says "the same word names the images at 2 Kgs 11:18, Amos 5:26, Dan 3:1". Daniel 3:1 is Biblical Aramaic צְלֵם, which BDB enters separately with a cross-reference ("see Biblical Hebrew צלם"); Amos 5:26 is the verse BDB marks "text dubious".
  - The same note says "the Brown-Driver-Briggs gloss is 'something cut out'". In BDB as reproduced, "something cut out" stands in parentheses after the head gloss "image", as an etymological explanation with a comparison to מֶּסֶל and Nöldeke's "Schnitzbild".
- **Subjects of the concrete occurrences.** By what is depicted: tumours and mice in gold (1 Sam 6:5 twice, 6:11); cult images of Baal's house (2 Kgs 11:18; 2 Chr 23:17); cast images of the land's inhabitants (Num 33:52); images made from ornaments or gold and silver (Ezek 7:20; 16:17, "male images"); wall pictures of Chaldeans (Ezek 23:14); Amos 5:26 (disputed).
- **Aramaic forms.** In Daniel 3:5-18 the construct form before "gold" is pointed צֶלֶם, identical to the Hebrew absolute; BDB records this ("construct ׳צ Daniel 3:19, צֶ֫לֶם Daniel 3:5 +").
