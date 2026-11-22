# Finding: woh-exp-0004

- Date: 2026-11-22
- Source and edition inspected:
  - *Le Livre qui dit la vérité* (The Book Which Tells the Truth), project digitization, French base text (`text` field): `data-library/the-book-which-tells-the-truth/chapter-1.json` … `chapter-7.json` (`_meta.json`: `primaryLang` fr, `publicationYear` 1973, revision 1, 759 paragraphs). All quotations below are from `chapter-2.json` unless marked.
  - Hebrew: `data-library/genesis-woh/chapter-1.json` and `chapter-2.json` (`text` field), compared with `source-he-1.json` / `source-he-2.json` beside them: chapter 1 is string-identical in all 31 verses; chapter 2 is identical in consonants and words in all 25 verses and differs only at the byte level (apparently the encoding order of points and accents; the verses quoted below display identically). Header of both source-he files: (Masoretic text, "Tanach with Ta'amei Hamikra", tanach.us, fetched from sefaria.org 2026-05-18).
  - Lexicon: Brown-Driver-Briggs as reproduced on BibleHub (`https://biblehub.com/hebrew/<Strong's no.>.htm`, "Brown-Driver-Briggs" section), fetched 2026-11-22. Sefaria's `/api/words/` returned a bot challenge page or a Jastrow entry only, so it was not used. HALOT not reached.
- Access achieved: `project_digitization` (French book and Hebrew text); lexicon as public reproduction (BDB on BibleHub).
- Search performed:
  - Read every paragraph of TBWTT chapter 2 (TBWTT-2:1 to 2:92) in French.
  - Regex over the French `text` of all seven chapters for: `Genèse|Genese|Gen.`, `poussière`, `glaise`, `argile`, `côte`, `narines`, `haleine`, `souffle de vie`, `à notre image`, `ressemblance`, `firmament`, `Adam`, `Eden|Éden`, `jardin`, `septième jour`, `luminaire`, `gazon`, `semence`, `selon leur espèce`, `foisonn`, `bestiaux`, `mâle et femelle`, `Croissez`, `multipliez`, `Fructifiez` (case-insensitive). Every hit outside TBWTT-2:4–2:33 was a later Genesis chapter, another biblical book, or a false positive, except TBWTT-5:62 (allusion, below).
  - Read genesis-woh 1:11, 1:12, 1:20, 1:21, 1:24, 1:25, 1:26, 1:27, 2:7, 2:16, 2:17, 2:19 (Hebrew, with `i18n.en` and notes as reading aids).
  - BDB entries fetched (Strong's number, headword as shown on the page): 6754 צֶלֶם, 1823 דְּמוּת, 1847 דַּעַת, 6086 עֵץ, 398 אָכַל, 7121 קָרָא, 6212 עֵשֶׂב, 1877 דֶּשֶׁא, 2233 זֶרַע, 4327 מִין, 8318 שֶׁרֶץ, 5775 עוֹף, 929 בְּהֵמָה, 7431 רֶמֶשׂ, 5315 נֶפֶשׁ, 6213 עָשָׂה.

## Answer

The book quotes Genesis 1:1–2:25 thirteen times, all in TBWTT-2:4 to 2:31. No quotation of that range was found in any other chapter (one unquoted allusion at TBWTT-5:62).

Applying the protocol's filter ("verse concerns the making of plants, animals or the human"):

**Core set — four quotations (Gen 1:11-12, 1:20, 1:24, 1:26).**

| # | refId | Verse | Hinge word(s) | Class |
|---|---|---|---|---|
| Q1 | TBWTT-2:15 | Gen 1:11-12 (plants) | no hinge word | — |
| Q2 | TBWTT-2:19 | Gen 1:20 (water animals, birds) | no hinge word | — |
| Q3 | TBWTT-2:23 | Gen 1:24 (land animals) | no hinge word | — |
| Q4 | TBWTT-2:26 | Gen 1:26 (the human) | « à notre image » (צֶלֶם) | `carried` |
| | | | « ressemblance » (דְּמוּת) | `carried` |

For Q1–Q3 the commentary (TBWTT-2:16, 2:20–2:22, 2:24) narrates what was done (chemical synthesis of plant cells, an ordered sequence of animals, ecological balance, contests, artists) without quoting, repeating in guillemets, or glossing any word of the quoted verse. The procedure and material it names ("cellules végétales", "produits chimiques") are not tied to a word of the quotation.

For Q4 the commentary (TBWTT-2:27) takes up two words of the verse and explains them as visible physical likeness between the speaker and the listener. This is the only explicit take-up in the core set. "Physical likeness" is not literally one of the protocol's listed categories (object, material, device, sound, light, movement, procedure); I counted it because the take-up is explicit and physical. If it is excluded, the core set has zero hinge words and four quotations with no hinge word.

**Borderline set — two quotations (Gen 2:16-17, 2:19).** These concern the human and the animals but not, in the quoted words, their making. Reported separately so they can be included or dropped.

| # | refId | Verse | Hinge word(s) | Class |
|---|---|---|---|---|
| Q5 | TBWTT-2:29 | Gen 2:16-17 (command about the trees) | « arbre » (עֵץ) → "livres" | `carried` (see note) |
| | | | « manger » (אָכַל) → "apprendre", "lire" | `carried` (see note) |
| | | | « science » (דַּעַת) → "livres scientifiques" | `shifted` |
| Q6 | TBWTT-2:31 | Gen 2:19 (animals brought to be named; Hebrew verse opens with their forming) | no hinge word | — |

Note on Q5 "arbre" and "manger": the Hebrew words mean what the French words mean (tree; eat). The commentary's substitutions (books; learning, reading) are not a lexicon sense of the Hebrew word and not a sense of the French word either. They are classed `carried` because the protocol's test is whether the Hebrew carries the sense of the French word; the substitution itself is not a lexical matter on either side.

**Totals**

| | carried | shifted | absent | not_checkable | quotations with no hinge word |
|---|---|---|---|---|---|
| Core set (4 quotations) | 2 | 0 | 0 | 0 | 3 |
| Borderline set (2 quotations) | 2 | 1 | 0 | 0 | 1 |
| Both (6 quotations) | 4 | 1 | 0 | 0 | 4 |

## Quotations

### Q1 — Gen 1:11-12

TBWTT-2:15 (Yahweh):
> «Que la terre produise du gazon, de l’herbe (...) des arbres (...) qui aient en eux leur semence... selon leur espèce». (Genèse, I, 11-12)

Commentary, TBWTT-2:16:
> Ils ont alors créé sur ce magnifique et gigantesque laboratoire des cellules végétales à partir de rien d’autre que des produits chimiques. Ce qui donna des plantes de toutes sortes. Tous leurs efforts ont porté sur la reproduction. Il fallait que les quelques brins d’herbes qu’ils faisaient naître puissent se reproduire. Ils se sont répandus sur cet immense continent en divers groupes de recherche scientifique et chacun, suivant son climat et son inspiration, créait des plantes différentes. […]

Hebrew, GEN-WOH-1:11:
> וַיֹּ֣אמֶר אֱלֹהִ֗ים תַּֽדְשֵׁ֤א הָאָ֙רֶץ֙ דֶּ֔שֶׁא עֵ֚שֶׂב מַזְרִ֣יעַ זֶ֔רַע עֵ֣ץ פְּרִ֞י עֹ֤שֶׂה פְּרִי֙ לְמִינ֔וֹ אֲשֶׁ֥ר זַרְעוֹ־ב֖וֹ עַל־הָאָ֑רֶץ וַֽיְהִי־כֵֽן׃

GEN-WOH-1:12:
> וַתּוֹצֵ֨א הָאָ֜רֶץ דֶּ֠שֶׁא עֵ֣שֶׂב מַזְרִ֤יעַ זֶ֙רַע֙ לְמִינֵ֔הוּ וְעֵ֧ץ עֹֽשֶׂה־פְּרִ֛י אֲשֶׁ֥ר זַרְעוֹ־ב֖וֹ לְמִינֵ֑הוּ וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃

Result: no hinge word. Near-echoes that fall short of an explicit take-up, with lexicon data for whoever wishes to count them:
- "herbe" recurs as "brins d’herbes" (not glossed). Hebrew עֵשֶׂב; BDB 6212: "herb, herbage". ("gazon" = דֶּשֶׁא; BDB 1877: "grass".)
- "semence" is answered by "reproduction … se reproduire" (the word is not repeated). Hebrew זֶרַע; BDB 2233: "sowing, seed, offspring".
- "selon leur espèce" is answered by "plantes de toutes sortes … plantes différentes" (not repeated). Hebrew לְמִינוֹ / לְמִינֵהוּ; BDB 4327 [מִין]: "kind, species, of plant Genesis 1:11,12".

### Q2 — Gen 1:20

TBWTT-2:19:
> «Que les eaux foisonnent d’une foison d’animaux vivants et que les volatiles volent au-dessus de la terre (...)». (Genèse, I-20.)

Commentary, TBWTT-2:20:
> Ils ont ensuite créé les premiers animaux aquatiques. Du plancton aux petits poissons puis ensuite de très gros poissons. Afin que tout ce petit monde soit équilibré et qu’il ne meure pas, ils ont créé des algues dont les petits poissons se nourrissent, des gros poissons pour manger les plus petits, etc. […]

TBWTT-2:22 (third paragraph after the quotation, outside the protocol's "same or following paragraph" window):
> Après les poissons, ils ont créé les oiseaux, […]

Hebrew, GEN-WOH-1:20:
> וַיֹּ֣אמֶר אֱלֹהִ֔ים יִשְׁרְצ֣וּ הַמַּ֔יִם שֶׁ֖רֶץ נֶ֣פֶשׁ חַיָּ֑ה וְעוֹף֙ יְעוֹפֵ֣ף עַל־הָאָ֔רֶץ עַל־פְּנֵ֖י רְקִ֥יעַ הַשָּׁמָֽיִם׃

Result: no hinge word. ("animaux" recurs as "animaux aquatiques", unglossed. BDB 8318 שֶׁרֶץ: "collective swarmers, swarming things … aquatic Genesis 1:20"; BDB 5775 עוֹף: "collective flying creatures, fowl, insects".)

### Q3 — Gen 1:24

TBWTT-2:23:
> «Que la terre fasse sortir des animaux vivants selon leur espèce : bestiaux, reptiles, bêtes sauvages, selon leur espèce !». (Genèse, I-24)

Commentary, TBWTT-2:24:
> Après les mers et les airs, ils ont créé des animaux terrestres sur une terre dont la végétation était alors devenue magnifique. Il y avait de la nourriture pour des herbivores. Ce sont les premiers animaux terrestres qui ont été faits. Ils ont ensuite créé des carnivores pour équilibrer le peuple des herbivores. Là aussi il fallait que les espèces s’équilibrent d’elles-mêmes. […]

Hebrew, GEN-WOH-1:24:
> וַיֹּ֣אמֶר אֱלֹהִ֗ים תּוֹצֵ֨א הָאָ֜רֶץ נֶ֤פֶשׁ חַיָּה֙ לְמִינָ֔הּ בְּהֵמָ֥ה וָרֶ֛מֶשׂ וְחַֽיְתוֹ־אֶ֖רֶץ לְמִינָ֑הּ וַֽיְהִי־כֵֽן׃

Result: no hinge word. ("espèce" recurs as "les espèces", unglossed. BDB 929 בְּהֵמָה: "beast, animal, cattle"; BDB 7431 רֶמֶשׂ: "collective creeping things, moving things". The commentary's "herbivores" / "carnivores" are not presented as glosses of "bestiaux" / "bêtes sauvages".)

### Q4 — Gen 1:26

TBWTT-2:26:
> «Faisons l’homme à notre image, à notre ressemblance ! Qu’il ait autorité sur les poissons de la mer et sur les oiseaux des cieux, sur les bestiaux, sur toutes les bêtes sauvages et sur tous les reptiles qui rampent sur la terre !». (Genèse, I-26)

Commentary sentence that takes the words up, TBWTT-2:27 (whole paragraph):
> A notre image! Vous pouvez constater que la ressemblance est frappante.

Hebrew, GEN-WOH-1:26:
> וַיֹּ֣אמֶר אֱלֹהִ֔ים נַֽעֲשֶׂ֥ה אָדָ֛ם בְּצַלְמֵ֖נוּ כִּדְמוּתֵ֑נוּ וְיִרְדּוּ֩ בִדְגַ֨ת הַיָּ֜ם וּבְע֣וֹף הַשָּׁמַ֗יִם וּבַבְּהֵמָה֙ וּבְכָל־הָאָ֔רֶץ וּבְכָל־הָרֶ֖מֶשׂ הָֽרֹמֵ֥שׂ עַל־הָאָֽרֶץ׃

Hinge 1 — French "(à notre) image"; Hebrew בְּצַלְמֵנוּ (צֶלֶם).
BDB 6754 צֶלֶם: "noun masculine … image (something cut out …)"; "1 images of tumours and mice (of gold) … especially of heathen gods … of painted pictures of men Ezekiel 23:14. 2 image, likeness, of resemblance, … of God's making man in his own image, Genesis 1:26 … 3 figurative = mere, empty, image, semblance".
Class: `carried`.

Hinge 2 — French "(à notre) ressemblance" (commentary: "la ressemblance est frappante"); Hebrew כִּדְמוּתֵנוּ (דְּמוּת).
BDB 1823 דְּמוּת: "noun feminine likeness, similitude (mostly late) … 1 likeness, similitude, of external appearance, chiefly in Ezek. … of son in likeness of father Genesis 5:3 (P); so also of man in likeness of God Genesis 1:26".
Class: `carried`.

### Q5 (borderline) — Gen 2:16-17

TBWTT-2:29:
> «De tout arbre du jardin tu pourras manger, mais de l’arbre de la science du bien et du mal tu n’en mangeras pas, car du jour où tu en mangerais, tu mourrais». (Genèse, II, 16-17)

Commentary sentence, TBWTT-2:30 (whole paragraph):
> Ce qui veut dire : tu peux apprendre tout ce que tu voudras, lire tous les livres que nous avons ici à ta disposition, mais ne touche pas aux livres scientifiques sinon tu mourrais.

Hebrew, GEN-WOH-2:16:
> וַיְצַו֙ יְהוָ֣ה אֱלֹהִ֔ים עַל־הָֽאָדָ֖ם לֵאמֹ֑ר מִכֹּ֥ל עֵֽץ־הַגָּ֖ן אָכֹ֥ל תֹּאכֵֽל׃

GEN-WOH-2:17:
> וּמֵעֵ֗ץ הַדַּ֙עַת֙ ט֣וֹב וָרָ֔ע לֹ֥א תֹאכַ֖ל מִמֶּ֑נּוּ כִּ֗י בְּי֛וֹם אֲכָלְךָ֥ מִמֶּ֖נּוּ מ֥וֹת תָּמֽוּת׃

Hinge 3 — French "arbre" (commentary: "tous les livres"); Hebrew עֵץ.
BDB 6086 עֵץ: "noun masculine … tree, trees, wood"; "1 a. a standing tree … b. collective trees, עֵץ־הַגָּן Genesis 2:16"; "2 … wood, as material". No sense "book" or "writing" appears in the portion of the entry read (first c. 2,500 characters of the BDB section).
Class: `carried` (Hebrew = tree, French = tree; see note in Answer).

Hinge 4 — French "manger" (commentary: "apprendre … lire"); Hebrew אָכֹל תֹּאכֵל / לֹא תֹאכַל (אָכַל).
BDB 398 אָכַל: "verb eat … 1 eat, human subject Genesis 3:11,18 + often". Only the opening of the entry was read; later figurative senses were not inspected.
Class: `carried` (Hebrew = eat, French = eat; see note in Answer).

Hinge 5 — French "science" in "l’arbre de la science du bien et du mal" (commentary: "livres scientifiques"); Hebrew הַדַּעַת (דַּעַת).
BDB 1847 דַּעַת: "noun feminine … knowledge (properly Infinitive, which appears clearly Genesis 2:9,17 …)"; "1. a. knowledge, perception … b. = skill (in work-manship) … c. of prophetic knowledge … d. especially knowledge with moral quality Genesis 2:9,17 (J; in both verbal force, הַדַּעַת טוֹב וָרַע the knowing good and evil). e. knowledge possessed by God …"; "2 especially in Wisdom Literature = discernment, understanding, wisdom".
Class: `shifted`. A Hebrew counterpart exists and means "knowledge / the knowing"; the commentary uses the French word in the narrower sense "scientific" ("livres scientifiques"; cf. TBWTT-2:28 "grands secrets scientifiques", in the paragraph before the quotation).

Not counted: "tu mourrais" is repeated verbatim in the commentary without explanation (Hebrew מוֹת תָּמוּת).

### Q6 (borderline) — Gen 2:19

TBWTT-2:31:
> «Il amena vers l’homme les animaux pour voir comment il les appellerait». (Genèse, II-19)

Commentary, TBWTT-2:32:
> Il fallait qu’il connaisse bien les plantes et les animaux qui l’entouraient, leur mode de vie et les moyens de se procurer grâce à eux de la nourriture. Les créateurs lui apprirent le nom et les pouvoirs de tout ce qui vivait autour de lui : la botanique et la zoologie car cela n’était pas dangereux pour eux.

Hebrew, GEN-WOH-2:19:
> וַיִּצֶר֩ יְהוָ֨ה אֱלֹהִ֜ים מִן־הָֽאֲדָמָ֗ה כָּל־חַיַּ֤ת הַשָּׂדֶה֙ וְאֵת֙ כָּל־ע֣וֹף הַשָּׁמַ֔יִם וַיָּבֵא֙ אֶל־הָ֣אָדָ֔ם לִרְא֖וֹת מַה־יִּקְרָא־ל֑וֹ וְכֹל֩ אֲשֶׁ֨ר יִקְרָא־ל֧וֹ הָֽאָדָ֛ם נֶ֥פֶשׁ חַיָּ֖ה ה֥וּא שְׁמֽוֹ׃

Result: no hinge word. No word of the quotation is repeated or glossed; "le nom" in the commentary is not a word of the French quotation (the quotation has "appellerait"; Hebrew יִקְרָא, BDB 7121 קָרָא "verb call, proclaim, read"; the Hebrew word for "name", שְׁמוֹ, stands in the part of the verse the book does not quote).

### Allusion without quotation marks — TBWTT-5:62 (chapter-5.json)

> […] et enfin l’homme qui n’est qu’un modèle de singe amélioré, auquel nous avons ajouté ce qui faisait que nous étions des hommes, nous l’avons fait à notre image comme cela est écrit dans la Genèse biblique.

Not in « », no verse reference; recorded, not tallied.

## Absent or ambiguous

- **Not quoted anywhere in the book** (per the searches above): Gen 1:21 (great sea creatures), 1:25, 1:27 (male and female), 1:28-31, 2:7 (forming of the human from dust, breath), 2:8-15, 2:18, 2:20-25 (including the rib). The searches for `poussière`, `glaise`, `argile`, `côte`, `narines`, `haleine`, `souffle de vie` returned no Genesis 1–2 passage.
- **Filter boundary.** Whether Gen 2:16-17 and 2:19 "concern the making of … the human / animals" is a judgement. I kept them apart as the borderline set. The quoted clause of 2:19 omits the forming of the animals with which the Hebrew verse opens.
- **Hinge-word boundary in Q4.** The commentary explains "image / ressemblance" as visible physical likeness, which is not literally in the protocol's list of explanation types. Counted, flagged.
- **Hinge-word boundary in Q1.** "herbe → brins d’herbes", "semence → reproduction", "espèce → plantes différentes" are echoes, not explicit take-ups. Counted as no hinge word; lexicon data given so they can be re-scored. On the BDB entries read, each of the three Hebrew words has the sense of the French word.
- **Preceding-paragraph commentary.** TBWTT-2:25 ("créer un homme comme nous artificiellement", "enfants d’éprouvette") stands before the Gen 1:26 quotation, not in the same or following paragraph, and takes up no word of it.
- **French Bible version.** The book does not name the French translation it quotes in this chapter, and I did not trace the wording to an edition. Whether the French words ("science", "gazon", "volatiles", "la Sèche", "Iahvé Elohim") belong to a particular published translation was not inspected.
- **"science" depends on translation.** The `shifted` result rests on the French rendering "science" for הַדַּעַת. In the French text read, the quotation itself has "science"; the commentary supplies "scientifiques".
- **Lexicon coverage.** BDB only, via BibleHub's reproduction (which contains OCR-type slips, e.g. "fruit #NAME? trees" in the עֵץ entry). HALOT not consulted. For אָכַל, קָרָא, עָשָׂה, נֶפֶשׁ and עֵץ only the opening portion of long entries was read.
- **Digitization.** The French `text` field shows minor typographic artefacts (e.g. TBWTT-2:27 "A notre image!" without accent; a quotation split across TBWTT-2:69/2:70). None affects the passages above.

## Adjacent observations

- **Other Genesis 1 quotations in the scope, outside the plants/animals/human filter** (listed, not classified, no lexical check made): TBWTT-2:4 (Gen 1:1), 2:6 (no reference given; wording of Gen 1:2), 2:7 (Gen 1:4), 2:9 (Gen 1:5), 2:11 (Gen 1:7), 2:13 (Gen 1:9), 2:17 (Gen 1:14). Several of these do carry explicit word-level glosses, more so than the plant and animal quotations:
  - TBWTT-2:5: "Elohim, injustement traduit dans certaines Bibles par Dieu, veut dire en Hébreu «ceux qui sont venus du ciel» et est bel et bien au pluriel." and "Ils ont «créé», découvert en réalité, la terre".
  - TBWTT-2:8: "La «lumière était bonne»."
  - TBWTT-2:10: "Le «jour» correspond à la période pendant laquelle votre soleil se lève sous le même signe le jour de l’équinoxe de printemps, soit deux mille ans terrestres environ."
  - TBWTT-2:12: "Entre les eaux d’en haut : les nuages, et les eaux d’en bas : l’océan recouvrant toute la Terre."
  - TBWTT-2:14: "grâce à d’assez fortes explosions qui ont fait un peu un travail de bulldozers, fait en sorte que de la matière soit enlevée du fond des mers et qu’elle s’amasse au même endroit".
- **"Dragons" without a quoted verse.** TBWTT-2:22 says: "Des dragons ou ce que vous avez baptisé des Dinosaures ou autres Brontosaures, etc." The book quotes Gen 1:20 and then 1:24; it does not quote 1:21. The Hebrew of GEN-WOH-1:21 has אֶת־הַתַּנִּינִם הַגְּדֹלִים. No BDB check of תַּנִּין was made (outside the quoted material).
- **Plural verb in Gen 1:26.** The French "Faisons … notre … notre" corresponds to Hebrew נַעֲשֶׂה … בְּצַלְמֵנוּ כִּדְמוּתֵנוּ (first-person plural forms; BDB 6754 cites "צַלְמֵנוּ Genesis 1:26", BDB 1823 "דְּמוּתֵנוּ Genesis 1:26"). The commentary's "A notre image!" keeps the possessive; it does not separately comment on the plural at this point (it does so for "Elohim" at TBWTT-2:5).
- **Verbs of producing.** French "Que la terre produise" (1:11) and "Que la terre fasse sortir" (1:24) stand for Hebrew תַּדְשֵׁא הָאָרֶץ and תּוֹצֵא הָאָרֶץ, in both of which the land is the grammatical subject. The commentary makes the visitors the subject ("Ils ont alors créé…", "ils ont créé des animaux terrestres") and takes up neither verb. BDB 1877 notes of דֶּשֶׁא: "accusative of cognate meaning with verb תַּדְשֵׁא Genesis 1:11 … (in both, produced by earth)".
- **Ellipses.** The Gen 1:11-12 quotation is heavily abridged with "(...)" and "..." and merges two verses; the omitted Hebrew material includes עֵץ פְּרִי עֹשֶׂה פְּרִי (fruit tree making fruit) and the closing formulas.
- **Stated selection principle.** TBWTT-2:3: "Seules les parties de la Bible que je vais vous traduire sont importantes. Les autres, qui ne sont que des bavardages poétiques, je ne vous en parlerai pas." The speaker describes the quotations as what he will "traduire".
- **Same word outside scope.** "science" recurs in the quotation of Gen 3:22 at TBWTT-2:42 ("grâce à la - science (...)"), outside the Gen 1:1–2:25 scope; not checked against the Hebrew.
