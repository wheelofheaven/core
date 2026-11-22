# Finding: woh-exp-0002

- Date: 2026-11-22
- Source and edition inspected:
  - `data-library/the-book-which-tells-the-truth/chapter-1.json` … `chapter-7.json` (project digitization, French base text in `paragraphs[].text`; 759 paragraphs; `_meta.json` revision 1, updated 2026-04-26). `i18n.en` used as a reading aid only and not quoted.
  - `data-library/exodus-woh/chapter-N.json` and `source-he-N.json` for N = 3, 13, 14, 16, 17, 19 (Hebrew: "Tanach with Ta'amei Hamikra", fetched by the project from the Sefaria v3 API on 2026-06-03 per the file header; for every verse used, `source-he-N.json` `he` and `chapter-N.json` `text` are identical). Chapter 20 files exist but were not needed (see Answer).
  - Lexicon: Brown-Driver-Briggs as reproduced on BibleHub (`https://biblehub.com/hebrew/<Strong's no.>.htm`, section "Brown-Driver-Briggs"), fetched 2026-11-22. HALOT not reached.
- Access achieved: `project_digitization` (book, full text of all seven chapters); `project_digitization` (Hebrew); BDB via public reproduction (full entry text, with OCR faults noted below).
- Search performed:
  - All 759 paragraphs of chapters 1-7 searched for `Exode`/`exode`/`Exod`/`Ex.`; 17 parenthesised Exodus references found, all in chapter 3, TBWTT-3:8 to TBWTT-3:41. No hit in chapters 1, 2, 4, 5, 6, 7.
  - Counter-search for unreferenced Exodus matter across all chapters: `Moïse`, `Sinaï`, `Horeb`, `manne`, `buisson`, `nuée`, `colonne de nuée`, `bâton`, `rocher`, `cor`, `Pharaon`, `Égypt/Egypt`, `mer Rouge`, `Décalogue`, `commandement`, `sabbat`, `tueras`, `adultère`, `convoit`, `voleras`, `faux témoi`, `Honore`, `pierres de taille`, `maison de servitude`, `en vain`, `autel`, `idole`, `XX`. No further Exodus quotation found.
  - TBWTT-3:1 to TBWTT-3:46 read in full and in order (quotation, same paragraph, preceding and following paragraphs).
  - Hebrew verses read: Ex 3:2-3; 13:21-22; 14:19-21, 30; 16:13-15, 31; 17:5-6; 19:16, 18-19, 21-24.

## Answer

**Quotations in scope: 10** (Ex 3: 1; Ex 13: 1; Ex 14: 3; Ex 16: 1; Ex 17: 1; Ex 19: 3; **Ex 20: 0**). The book contains no quotation of Exodus 20; its only pointer to the commandments is the general sentence at TBWTT-3:24, which places the rules "au chapitre XIX".

The other seven Exodus references in the book (XXIV-2, XXIV-10, XXIV-17, XXV 2-7, XXXIII-9, XXXIII-11, XXXIII-20, plus the unreferenced tent quotation at TBWTT-3:37) are outside the stated chapters and were not analysed.

**Hinge words: 4, in 4 quotations. Quotations with no hinge word: 6.**

| # | refId | Verse | French hinge word | Commentary re-describes it as | Hebrew at that place | Class |
|---|---|---|---|---|---|---|
| 1 | TBWTT-3:8 → 3:9 | Ex 3:2 | « flamme de feu … embrasé par le feu, mais … pas dévoré » | white light of a craft that lights the trees without burning them (light) | לַבַּת־אֵשׁ … בֹּעֵר בָּאֵשׁ … אֵינֶנּוּ אֻכָּל | `carried` |
| 2 | TBWTT-3:13 → 3:14 | Ex 14:19(-20) | « (colonne de) nuée » | emitted smoke forming a curtain (material) | עַמּוּד הֶעָנָן / הֶעָנָן | `carried` |
| 3 | TBWTT-3:20 → 3:22 | Ex 16:14 | « mince croûte » | synthetic chemical food sprayed on the ground (material, procedure) | דַּק מְחֻסְפָּס | `carried` |
| 4 | TBWTT-3:23 (same paragraph) | Ex 17:6 | « de faire jaillir de l'eau » | locating underground water with a detector, then digging (device, procedure) | וְיָצְאוּ מִמֶּנּוּ מַיִם | `carried` (with reservation, see below) |

**Totals: `carried` 4; `shifted` 0; `absent` 0; `not_checkable` 0. No hinge word: 6 quotations** (TBWTT-3:11 Ex 13:21; TBWTT-3:16/17 Ex 14:21; TBWTT-3:18 Ex 14:30; TBWTT-3:25 Ex 19:16; TBWTT-3:26 Ex 19:18-19; TBWTT-3:28 Ex 19:23-24).

How the protocol was read, since the totals depend on it:

1. **Classification compares the French verse word with the Hebrew word**, as step 6 words it, not the commentary's re-description with the Hebrew. In all four cases the French word of the quotation is an ordinary rendering of the Hebrew. In none of the four cases is the commentary's own re-description (light, smoke, synthetic food, detector/digging) a sense given in the BDB entry consulted. Both facts are recorded; the second is not what step 6 classifies.
2. **In no case does the commentary take up the hinge word verbatim and gloss it** (there is no sentence of the form "the word X means Y" in this scope, unlike « gloire » at TBWTT-3:33, which is outside scope). In cases 1-3 the uptake is by paraphrase of the thing the quotation names (flamme/feu → lumière; nuée → fumée; croûte → aliment … pulvérisé). Only case 4 repeats quoted words. On a strict reading requiring verbatim uptake plus explanation, the count is 1 hinge word (case 4) and 9 quotations with none.
3. **Three further quoted words are repeated or restated in the commentary without being re-described** and were not counted as hinge words: « buisson » (→ « les arbres », 3:9), « derrière eux » (→ « derrière le peuple d'Israël », 3:14), « à la surface du désert » (→ « à la surface du sol », 3:22). Checked anyway; all three would be `carried`. Counting them gives 7 hinge words, 7 `carried`.
4. **« bâton »** is the word the commentary at TBWTT-3:23 actually explains as a device, but it stands outside the guillemets and is not a word of the quoted French, so it is not counted. If counted: the cited verse 17:6 has no word for staff (it has only "you shall strike the rock"); the staff is named in 17:5 (מַטְּךָ). That would be `carried` if "that place" is the passage 17:5-6, `absent` if it is the cited verse alone.
5. **Commentary that precedes a quotation** was not counted (step 3 says "the same or the following paragraph"). It occurs four times; see Adjacent observations.

Reservation on case 4: the French is causative with Moses as agent and uses « jaillir »; the Hebrew verb is Qal "come out" with the water as subject, the causing act being "strike the rock", which the French fragment does not quote. BDB lists Ex 17:6 itself under the plain sense "go or come out". The commentary does not appear to rely on the difference, so `carried` was chosen; a stricter reader could enter `shifted`, giving 3 `carried`, 1 `shifted`.

## Quotations

### A. The ten quotations (French base text)

1. TBWTT-3:8 (Ex 3:2): « L'Ange de Iahvé lui apparut dans une flamme de feu, du milieu d'un buisson (...) le buisson était embrasé par le feu, mais il n'était pas dévoré !» (Exode, III-2)
2. TBWTT-3:11 (Ex 13:21): «or Iahvé marchait au-devant d'eux, le jour en colonne de nuée pour les guider sur la route, et la nuit en colonne de feu pour les éclairer en sorte qu'ils marchent jour et nuit». (Exode, XIII-21)
3. TBWTT-3:13 (Ex 14:19, running into 14:20): «La colonne de nuée se déplaça de devant eux et se tint derrière eux (...) la nuée était (pour les uns) ténèbres, et (pour les autres) elle éclairait la nuit». (Exode, XIV-19)
4. TBWTT-3:16 and 3:17 (Ex 14:21): «(...) il mit ainsi la mer à sec et les eaux se fendirent». / (Exode, XIV-21)».
5. TBWTT-3:18 (Ex 14:30): «En ce jour Iahvé sauva Israël (...)» (Exode, XIV-30)
6. TBWTT-3:20 and 3:21 (Ex 16:14): «(...) à la surface du désert il y eut une mince croûte (...)» / (Exode, XVI-14)
7. TBWTT-3:23 (Ex 17:6), quotation embedded in commentary: Quant au bâton de Moïse qui lui permit «de faire jaillir de l'eau» (Exode, XVII-6), ce n'était qu'un détecteur de nappes aquatiques souterraines semblable à ceux que vous utilisez actuellement pour trouver du pétrole par exemple. Une fois l'eau localisée, il suffit de creuser.
8. TBWTT-3:25 (Ex 19:16): «(...) il y eut des tonnerres, des éclairs et une lourde nuée sur la montagne, un son de cor très fort (...)» (Exode, XIX-16)
9. TBWTT-3:26 (Ex 19:18-19): «or le Mont Sinaï était tout fumant, parce que sur lui était descendu Iahvé dans le feu, et sa fumée montait comme la fumée d'une fournaise : toute la montagne tremblait fort. Le son du cor allait en se renforçant de plus en plus, (...)». (Exode, XIX, 18-19)
10. TBWTT-3:28 (Ex 19:23-24): «Le peuple ne pourra monter au Mont Sinaï (...) que les prêtres et le peuple ne se ruent pas pour monter vers Iahvé, de peur qu'il ne les abatte». (Exode, XIX, 23-24)

(The digitization uses the typographic apostrophe ’; it is given here as '.)

### B. Commentary sentences

- TBWTT-3:7 (before quotation 1): Dans l'Exode nous apparaissons à Moïse :
- TBWTT-3:9 (after quotation 1): Une fusée se posa devant lui et la description qu'il fait correspond à celle que ferait aujourd'hui un primitif du Brésil si nous nous y posions, dans cet engin dont la lumière blanche éclaire dans les arbres sans les faire brûler pour autant...
- TBWTT-3:10 (before quotation 2): L'Exode décrit, au début, tout ce que nous avons dû faire pour que le peuple d'Israël soit libéré. Lorsqu'ils partirent, nous les guidâmes jusqu'au pays que nous leur destinions.
- TBWTT-3:12 (after quotation 2, introducing quotation 3): Pour ralentir la marche des Egyptiens lancés à leur poursuite :
- TBWTT-3:14 (after quotation 3): La fumée émise derrière le peuple d'Israël faisait un rideau qui ralentissait les poursuivants.
- TBWTT-3:15 (before quotation 4): Ensuite la traversée de l'eau est obtenue grâce à un rayon répulseur qui permet de dégager un passage.
- TBWTT-3:19 (after quotation 5, introducing quotation 6): Puis à travers le désert la faim se fit sentir dans le peuple élu :
- TBWTT-3:22 (after quotation 6): La manne n'était qu'un aliment chimique de synthèse pulvérisé à la surface du sol et que la rosée du matin faisait gonfler.
- TBWTT-3:23: see quotation 7.
- TBWTT-3:24 (before quotations 8-9): Ensuite, au chapitre XIX de l'Exode, il est énoncé un certain nombre de règles. Le peuple d'Israël, étant donné son niveau primitif, avait besoin de lois sur le plan moral et surtout sur le plan hygiénique. Elles sont énoncées dans les commandements. Les créateurs vinrent dicter ces lois à Moïse sur le Mont Sinaï. Ils descendirent dans un engin volant :
- TBWTT-3:27 (after quotation 9, before quotation 10): Mais les créateurs eurent peur d'être envahis ou bousculés par les hommes, il fallait qu'ils soient respectés, vénérés même, afin de n'être pas en danger.

### C. Hebrew (exodus-woh, `source-he-N.json` = `chapter-N.json` text)

- EXO-WOH-3:2: וַ֠יֵּרָא מַלְאַ֨ךְ יְהֹוָ֥ה אֵלָ֛יו בְּלַבַּת־אֵ֖שׁ מִתּ֣וֹךְ הַסְּנֶ֑ה וַיַּ֗רְא וְהִנֵּ֤ה הַסְּנֶה֙ בֹּעֵ֣ר בָּאֵ֔שׁ וְהַסְּנֶ֖ה אֵינֶ֥נּוּ אֻכָּֽל׃
- EXO-WOH-13:21: וַֽיהוָ֡ה הֹלֵךְ֩ לִפְנֵיהֶ֨ם יוֹמָ֜ם בְּעַמּ֤וּד עָנָן֙ לַנְחֹתָ֣ם הַדֶּ֔רֶךְ וְלַ֛יְלָה בְּעַמּ֥וּד אֵ֖שׁ לְהָאִ֣יר לָהֶ֑ם לָלֶ֖כֶת יוֹמָ֥ם וָלָֽיְלָה׃
- EXO-WOH-14:19: וַיִּסַּ֞ע מַלְאַ֣ךְ הָאֱלֹהִ֗ים הַהֹלֵךְ֙ לִפְנֵי֙ מַחֲנֵ֣ה יִשְׂרָאֵ֔ל וַיֵּ֖לֶךְ מֵאַחֲרֵיהֶ֑ם וַיִּסַּ֞ע עַמּ֤וּד הֶֽעָנָן֙ מִפְּנֵיהֶ֔ם וַיַּֽעֲמֹ֖ד מֵאַחֲרֵיהֶֽם׃
- EXO-WOH-14:20: וַיָּבֹ֞א בֵּ֣ין ׀ מַחֲנֵ֣ה מִצְרַ֗יִם וּבֵין֙ מַחֲנֵ֣ה יִשְׂרָאֵ֔ל וַיְהִ֤י הֶֽעָנָן֙ וְהַחֹ֔שֶׁךְ וַיָּ֖אֶר אֶת־הַלָּ֑יְלָה וְלֹא־קָרַ֥ב זֶ֛ה אֶל־זֶ֖ה כָּל־הַלָּֽיְלָה׃
- EXO-WOH-14:21: וַיֵּ֨ט מֹשֶׁ֣ה אֶת־יָדוֹ֮ עַל־הַיָּם֒ וַיּ֣וֹלֶךְ יְהוָ֣ה ׀ אֶת־הַ֠יָּם בְּר֨וּחַ קָדִ֤ים עַזָּה֙ כָּל־הַלַּ֔יְלָה וַיָּ֥שֶׂם אֶת־הַיָּ֖ם לֶחָרָבָ֑ה וַיִּבָּקְע֖וּ הַמָּֽיִם׃
- EXO-WOH-14:30: וַיּ֨וֹשַׁע יְהוָ֜ה בַּיּ֥וֹם הַה֛וּא אֶת־יִשְׂרָאֵ֖ל מִיַּ֣ד מִצְרָ֑יִם וַיַּ֤רְא יִשְׂרָאֵל֙ אֶת־מִצְרַ֔יִם מֵ֖ת עַל־שְׂפַ֥ת הַיָּֽם׃
- EXO-WOH-16:13: וַיְהִ֣י בָעֶ֔רֶב וַתַּ֣עַל הַשְּׂלָ֔ו וַתְּכַ֖ס אֶת־הַֽמַּחֲנֶ֑ה וּבַבֹּ֗קֶר הָֽיְתָה֙ שִׁכְבַ֣ת הַטַּ֔ל סָבִ֖יב לַֽמַּחֲנֶֽה׃
- EXO-WOH-16:14: וַתַּ֖עַל שִׁכְבַ֣ת הַטָּ֑ל וְהִנֵּ֞ה עַל־פְּנֵ֤י הַמִּדְבָּר֙ דַּ֣ק מְחֻסְפָּ֔ס דַּ֥ק כַּכְּפֹ֖ר עַל־הָאָֽרֶץ׃
- EXO-WOH-17:5: וַיֹּ֨אמֶר יְהוָ֜ה אֶל־מֹשֶׁ֗ה עֲבֹר֙ לִפְנֵ֣י הָעָ֔ם וְקַ֥ח אִתְּךָ֖ מִזִּקְנֵ֣י יִשְׂרָאֵ֑ל וּמַטְּךָ֗ אֲשֶׁ֨ר הִכִּ֤יתָ בּוֹ֙ אֶת־הַיְאֹ֔ר קַ֥ח בְּיָדְךָ֖ וְהָלָֽכְתָּ׃
- EXO-WOH-17:6: הִנְנִ֣י עֹמֵד֩ לְפָנֶ֨יךָ שָּׁ֥ם ׀ עַֽל־הַצּוּר֮ בְּחֹרֵב֒ וְהִכִּ֣יתָ בַצּ֗וּר וְיָצְא֥וּ מִמֶּ֛נּוּ מַ֖יִם וְשָׁתָ֣ה הָעָ֑ם וַיַּ֤עַשׂ כֵּן֙ מֹשֶׁ֔ה לְעֵינֵ֖י זִקְנֵ֥י יִשְׂרָאֵֽל׃
- EXO-WOH-19:16: וַיְהִי֩ בַיּ֨וֹם הַשְּׁלִישִׁ֜י בִּֽהְיֹ֣ת הַבֹּ֗קֶר וַיְהִי֩ קֹלֹ֨ת וּבְרָקִ֜ים וְעָנָ֤ן כָּבֵד֙ עַל־הָהָ֔ר וְקֹ֥ל שֹׁפָ֖ר חָזָ֣ק מְאֹ֑ד וַיֶּחֱרַ֥ד כָּל־הָעָ֖ם אֲשֶׁ֥ר בַּֽמַּחֲנֶֽה׃
- EXO-WOH-19:18: וְהַ֤ר סִינַי֙ עָשַׁ֣ן כֻּלּ֔וֹ מִ֠פְּנֵי אֲשֶׁ֨ר יָרַ֥ד עָלָ֛יו יְהוָ֖ה בָּאֵ֑שׁ וַיַּ֤עַל עֲשָׁנוֹ֙ כְּעֶ֣שֶׁן הַכִּבְשָׁ֔ן וַיֶּחֱרַ֥ד כָּל־הָהָ֖ר מְאֹֽד׃
- EXO-WOH-19:19: וַיְהִי֙ ק֣וֹל הַשּׁוֹפָ֔ר הוֹלֵ֖ךְ וְחָזֵ֣ק מְאֹ֑ד מֹשֶׁ֣ה יְדַבֵּ֔ר וְהָאֱלֹהִ֖ים יַעֲנֶ֥נּוּ בְקֽוֹל׃
- EXO-WOH-19:23: וַיֹּ֤אמֶר מֹשֶׁה֙ אֶל־יְהוָ֔ה לֹא־יוּכַ֣ל הָעָ֔ם לַעֲלֹ֖ת אֶל־הַ֣ר סִינָ֑י כִּֽי־אַתָּ֞ה הַעֵדֹ֤תָה בָּ֙נוּ֙ לֵאמֹ֔ר הַגְבֵּ֥ל אֶת־הָהָ֖ר וְקִדַּשְׁתּֽוֹ׃
- EXO-WOH-19:24: וַיֹּ֨אמֶר אֵלָ֤יו יְהוָה֙ לֶךְ־רֵ֔ד וְעָלִ֥יתָ אַתָּ֖ה וְאַהֲרֹ֣ן עִמָּ֑ךְ וְהַכֹּהֲנִ֣ים וְהָעָ֗ם אַל־יֶֽהֶרְס֛וּ לַעֲלֹ֥ת אֶל־יְהוָ֖ה פֶּן־יִפְרָץ־בָּֽם׃

### D. Lexicon checks (BDB as reproduced on BibleHub; Strong's number gives the page)

Hinge words:

1. « flamme de feu … embrasé par le feu … pas dévoré » (Ex 3:2)
   - לַבַּת־אֵשׁ: BDB s.v. לֶהָבָה (page 3852; page 3827 לַבָּה carries no BDB text and BDB cross-refers "לַבַּת אֵשׁ Exodus 3:2 see לֶהָבָה above"): "1 flame … לַבַּת אֵשׁ Exodus 3:2. 2 point, head of spear".
   - בֹּעֵר: BDB s.v. I. [בָּעַר] (1197): "burn, consume … 2 be burning, burn … Exodus 3:2 (הסנה, with בָּאֵשׁ)".
   - אֻכָּל: BDB s.v. אָכַל (398), Pu'al: "be consumed with fire … so Participle אֻכָּל … Exodus 3:2".
   - The BDB text retrieved for these entries gives no sense "light" or "illuminate".
2. « nuée » / « colonne de nuée » (Ex 14:19-20)
   - עָנָן: BDB s.v. I. עָנָן (6051): "cloud-mass, cloud; — 1 cloud-mass: a. especially of theophanic cloud (58 t.) … usually עַמּוּד הֶעָנָן Exodus 13:21, 22 … compare Exodus 14:20 … as a barrier Lamentations 3:44 … 2 … Leviticus 16:13 (P) cloud of incense, so Ezekiel 8:11".
   - עַמּוּד: BDB s.v. עַמּוּד (5982): "pillar, column … 4 עַמּוּד עָשָׁן Judges 20:40 column of smoke: עַמּוּד (הֶ)עָנָן Exodus 13:21, 22 (J) + 6 t. … all of the theophanies at time of Exodus".
   - The entry for עָנָן gives no sense "smoke"; BDB sets "column of smoke" (with עָשָׁן, Judges 20:40) beside "column of cloud" under the same sense-number of עַמּוּד.
3. « mince croûte » (Ex 16:14)
   - דַּק: BDB s.v. דַּק (1851): "thin, small, fine … 2 small, fine, of the manna … Exodus 16:14".
   - מְחֻסְפָּס: BDB s.v. [חספס] (2636; BibleHub's reproduction prints the root with מּ for פ, an OCR fault): "verb only Passive participle (scaled off) scale-like … of the manna … Exodus 16:14 a fine, scale-like thing, fine as the hoar-frost".
   - The Hebrew has adjective + participle and no noun; the French noun « croûte » stands for the participle. BDB's gloss is "scale-like", not "crust".
4. « de faire jaillir de l'eau » (Ex 17:6)
   - וְיָצְאוּ: BDB s.v. יָצָא (3318), Qal: "go or come out … 1 … f. of inanimate things: river out of Eden Genesis 2:10 (J), water out of rock Exodus 17:6 (E), Numbers 20:11". The causative is listed separately under Hiph'il: "i. bring forth by miracle: Moses. water out of rock Numbers 20:8, 10", which is not the form in Ex 17:6.
   - No word for "dig" or "detect" stands in EXO-WOH-17:5-6; the action named is וְהִכִּיתָ בַצּוּר.

Words repeated but not counted as hinge words:

- « buisson » — סְנֶה: BDB (5572): "a thorny bush, perhaps black-berry bush … Exodus 3:2 (twice in verse)". (The Hebrew verse has the word three times; BibleHub's BDB text reads as quoted.)
- « derrière eux » — מֵאַחֲרֵיהֶם: BDB s.v. אַחַר (310), with מִן: "(β) denoting position … behind Exodus 14:19 (twice in verse)". « se déplaça » — וַיִּסַּע: BDB s.v. I. נָסַע (5265): "b. depart, with מִן … even of עַמּוּד הֶעָנָן Exodus 14:19".
- « à la surface du désert » — עַל־פְּנֵי הַמִּדְבָּר: BDB s.v. פָּנִים (6440), under עַל־פְּנֵי: "b. From the sense of surface, Genesis 1:2 … Exodus 16:14".
- « bâton » (commentary's word, outside the quotation) — מַטֶּה at 17:5: BDB (4294): "1 staff, rod, shaft. 2 branch. 3 tribe … of staff or rod, Moses as shepherd … Exodus 17:5 (all E)".

## Absent or ambiguous

- **Exodus 20: no quotation anywhere in chapters 1-7.** Nothing to compare.
- **No verbatim word-gloss in scope.** The commentary on these ten quotations never names a quoted word and defines it. Whether paraphrastic re-description counts as "explicitly takes up" is a matter of reading the protocol; counts under each reading are given in the Answer (1, 4 or 7 hinge words; `shifted` and `absent` are 0 under all of them unless « bâton » is admitted and tied to 17:6 alone, or case 4 is read as `shifted`).
- **The French Bible version quoted is not identified** in the digitization or its `_meta.json`. It was not established here; the French wording could therefore be checked against the Hebrew only, not against its own printed source.
- **Quotation 3** carries the reference XIV-19 but its second half corresponds to 14:20. The bracketed words « (pour les uns) » and « (pour les autres) » have no counterpart in EXO-WOH-14:20, which reads וַיְהִי הֶעָנָן וְהַחֹשֶׁךְ וַיָּאֶר אֶת־הַלָּיְלָה; the round brackets are in the French as digitized. Whether they are the French Bible's or the book's was not determined.
- **Quotation 7** is a fragment in indirect construction (« qui lui permit "de faire jaillir de l'eau" »), not a verse quotation; no clause of Ex 17:6 has that form.
- **Paragraphing.** Quotations 4 and 6 are split from their references across two paragraphs (3:16/3:17, 3:20/3:21); the reference paragraph was treated as part of the quotation, so 3:22 counts as "the following paragraph" for quotation 6. Paragraph 3:17 has a stray closing guillemet.
- **BibleHub's BDB** is an OCR reproduction with visible faults (פ printed as מּ in several headwords; some reference errors). Quotations above are as retrieved, with the Hebrew headwords normalised where the fault was plain. No printed BDB and no HALOT were consulted.

## Adjacent observations

- **Commentary placed before the quotation, with a verbal echo of it** (not counted under step 3):
  - TBWTT-3:10 « nous les guidâmes » before quotation 2 « pour les guider » — לַנְחֹתָם; BDB s.v. [נָחָה] (5148): "lead, guide … of pillar of cloud Exodus 13:21".
  - TBWTT-3:15 « un rayon répulseur qui permet de dégager un passage » before quotation 4. The quotation begins with « (...) »; the Hebrew verse has, immediately before the words quoted, וַיּוֹלֶךְ יְהוָה אֶת־הַיָּם בְּרוּחַ קָדִים עַזָּה כָּל־הַלַּיְלָה (project translation: "YHWH drove back the sea by a strong east wind all night"). That clause falls in the elided part.
  - TBWTT-3:24 « Ils descendirent dans un engin volant » before quotations 8-9; quotation 9 has « était descendu Iahvé dans le feu » — יָרַד; BDB (3381): "come or go down, descend".
  - TBWTT-3:27 « eurent peur d'être envahis ou bousculés » before quotation 10 « ne se ruent pas » — יֶהֶרְסוּ; BDB s.v. הָרַס (2040): "3 break through, intransitive … Exodus 19:21 … Exodus 19:24".
- **Commentary words absent from the quoted French but present in the Hebrew nearby:** « la rosée du matin » (3:22) — שִׁכְבַת הַטָּל in 16:13-14, in the part of 16:14 elided from the quotation; « la manne » (3:22) — מָן in 16:15 and 16:31. **Absent from the Hebrew read:** nothing in EXO-WOH-16:13-15 corresponds to « faisait gonfler »; a scan of the project translation of the whole chapter for swell/melt/dew/worm returned only 16:13, 14, 20, 21, 24 (dew, worms, melting), none of swelling.
- **Other French words in the quotations and their Hebrew:** « Ange » — מַלְאַךְ; « cor » — שֹׁפָר, BDB (7782): "horn, for blowing"; « de peur qu'il ne les abatte » — פֶּן־יִפְרָץ־בָּם (project translation: "lest he break out against them"; not checked in BDB).
- **Chapter attribution.** TBWTT-3:24 says the rules are set out « au chapitre XIX de l'Exode »; the three quotations that follow are all from chapter 19 and describe the descent on the mountain, not rules.
- The exodus-woh chapter files carry translator notes and `editorial_questions`; they were not used for any lexical statement here.
- TBWTT-3:46 to 3:48 return to the manna through Numbers XI, 7-8 (« la description très exacte de la manne que vos chimistes pourraient reconstituer »); and TBWTT-3:59 refers back to the sea crossing (« en utilisant le même rayon répulseur »). Both are outside the Exodus scope and were not analysed.
