# Finding: woh-exp-0006

- Date: 2026-11-22
- Source and edition inspected: *Les Extra-Terrestres M'ont Emmené sur Leur Planète* (1975), project digitization, French base text (`text` field), files `data-library/extraterrestrials-took-me-to-their-planet/chapter-1.json`, `chapter-2.json`, `chapter-3.json` (`_meta.json`: revision 1, updated 2026-05-17, 475 paragraphs). The `i18n.en` rendering was used only as a reading aid and is not quoted.
- Access achieved: `project_digitization` (complete for all three chapters). Lexicon: Brown-Driver-Briggs as reproduced on BibleHub (`biblehub.com/hebrew/NNNN.htm`), fetched 2026-11-22. Hebrew: project library `ezekiel-woh/chapter-37.json` and `genesis-woh/chapter-6.json` (`text` field); for Isaiah 43 and Joel 3, which the project library does not hold in Hebrew, the Masoretic text from Sefaria (API v3, version "Miqra according to the Masorah"). HALOT was not reached.
- Search performed:
  - Speaker census: chapter 1 has 77 paragraphs, all `Narrator` (no `Yahweh` paragraph); chapter 2 has 86 `Yahweh` and 46 `Narrator`; chapter 3 has 258 `Yahweh` and 8 `Narrator`.
  - Every one of the 344 paragraphs with `speaker == "Yahweh"` (ETTMTTP-2:11 to 2:129 and ETTMTTP-3:5 to 3:263, as labelled) was read in full in French.
  - Cross-check: regex search of the French `text` of all 475 paragraphs for the protocol terms `hébreu`, `hébraïque`, `signifie`, `veut dire`, `voulait dire`, `traduit`, `traduction`, `original`, `littéralement`, `Bible`, `Kabbale`, `nom` (word-bounded), plus `veulent dire`, `étymolog`, `sens `, `appel`, `désign`, `mot `, `Messie`, `Satan`, `Jésus`, `Christ`, `Israël`, `Jéhovah`, `Yahvé`, `Iahvé`, `Juif/juif`, `apocalypse`, `prophète`, `évangile`, `Lucifer`, `diable`, `Éden/Eden`, `Adam`, `Ève`, `Moïse`, `Genèse`, `écrit`, `Raël`, `Dieu/dieu`, `âme`, `religion`, `Torah/Thora`, `Talmud`, `Coran`, `Bouddha`, `Mahomet`, `grec`, `latin`.
  - Hits of the protocol terms in `Yahweh` paragraphs: `signifie` 2:24, 2:35; `veut dire` 2:25, 2:35, 3:245; `littéralement` 3:178; `nom` 2:50, 2:64. Zero hits in `Yahweh` paragraphs for `hébreu`, `hébraïque`, `voulait dire`, `traduit`, `traduction`, `original`, `Bible`, `Kabbale`. (`hébreu` occurs once, Narrator, 2:47; `original` once, Narrator, 1:64.)

## Answer

In this book the paragraphs labelled `Yahweh` contain **no statement about the meaning of a Hebrew word, name or title** (leaving aside "Élohim", which is in any case not explained in these paragraphs), and **no statement that refers to "the original", "the Hebrew" or a translation** of the biblical text. The words `hébreu`, `hébraïque`, `traduit`, `traduction`, `original`, `Bible`, `Kabbale` do not occur in any `Yahweh` paragraph.

What the scope does contain are four statements of the weaker kind "this is what a (Hebrew-Bible) text says": one quotation with reference, one named allusion, one attributed loose quotation, one quotation of an unnamed writing.

| # | refId | Statement | Class |
|---|---|---|---|
| 1 | ETTMTTP-2:71–72 | Quotation of Ezekiel (the bones) | `supported` (wording); the printed chapter number does not match |
| 2 | ETTMTTP-2:104 (repeated 2:123) | Genesis speaks of "fils d'Elohim" and "filles des hommes" | `supported` |
| 3 | ETTMTTP-2:124 | Isaiah wrote "au Nord donne et au Midi ne retiens pas …" | `supported` (first clause verbatim; second clause adapted) |
| 4 | ETTMTTP-3:256 | "Il y aura des signes dans le ciel", cela est écrit depuis longtemps | `not_checkable` (source text not named) |

Totals: `supported` 3; `unsupported` 0; `contested` 0; `not_checkable` 1. Statements of lexical meaning of a Hebrew word, name or title: 0.

Statements about words, symbols or texts of other languages or traditions (Greek New Testament, Arabic/Qur'an, Buddhist/Tibetan, symbols) are listed separately below and, per protocol, not classified.

## Quotations

### Listed and classified

**1. ETTMTTP-2:71–72 — `supported` (wording), locator mismatch**

- ETTMTTP-2:71: «Rappelez-vous dans l'Ancien Testament de cette description dans Ezéchiel :
- ETTMTTP-2:72: “Fils d'homme, ces ossements peuvent-ils revivre ?... il y eut un bruit et voilà que ce fut un branle-bas... il y avait sur (les ossements) des nerfs, de la chair croissait, et il étendit sur eux de la peau par-dessus... ils prirent vie et se dressèrent sur leurs pieds, armée très, très nombreuse”. (Ezéchiel, XXVII, 3, 7-8, 10)
- (ETTMTTP-2:73, same speaker: La description que vous allez faire est certainement très proche de celle d'Ezéchiel, mis à part le bruit que nous avons pu supprimer».)

Hebrew (project library `ezekiel-woh/chapter-37.json`, `text`; its `source-he-37.json` gives the source as "Tanach with Ta'amei Hamikra", fetched from Sefaria):

- EZK-WOH-37:3: בֶּן־אָדָ֕ם הֲתִחְיֶ֖ינָה הָעֲצָמ֣וֹת הָאֵ֑לֶּה
- EZK-WOH-37:7: וַֽיְהִי־ק֤וֹל כְּהִנָּֽבְאִי֙ וְהִנֵּה־רַ֔עַשׁ
- EZK-WOH-37:8: וְהִנֵּֽה־עֲלֵיהֶ֤ם גִּדִים֙ וּבָשָׂ֣ר עָלָ֔ה וַיִּקְרַ֧ם עֲלֵיהֶ֛ם ע֖וֹר מִלְמָ֑עְלָה
- EZK-WOH-37:10: וַיִּֽחְי֗וּ וַיַּֽעַמְדוּ֙ עַל־רַגְלֵיהֶ֔ם חַ֖יִל גָּד֥וֹל מְאֹד־מְאֹֽד

Lexicon lines (BDB via BibleHub):

- רַעַשׁ (Strong 7494): "noun masculine … quaking, shaking; — … 1 specifically earthquake … probably also Ezekiel 37:7 (… > rustling, rattling, Hi-Sm Toy)". French "branle-bas".
- גִּיד (Strong 1517): "noun masculine … sinew … plural גִּידִים Job 10:11; Ezekiel 37:6, גִּדִים Ezekiel 37:8". French "nerfs".
- חַיִל (Strong 2428): "noun masculine … strength, efficiency, wealth, army". French "armée".

Deciding point: verse by verse the French follows the Hebrew of Ezekiel 37:3, 7–8, 10 (bones living, a sound and a shaking, sinews/flesh/skin "from above", standing on their feet, "very, very" great force/army: מְאֹד־מְאֹֽד). The reference printed in the digitization is "XXVII"; the words are in chapter 37, not 27.

**2. ETTMTTP-2:104 (and 2:123) — `supported`**

- ETTMTTP-2:104: Ils sont les descendants des fils d'Elohim et des filles des hommes dont il est question dans la Genèse.
- ETTMTTP-2:123 (repeat, no reference to Genesis): … le peuple d'Israël est composé des descendants des enfants qui naquirent des unions entre les fils d'Elohim et les filles des hommes.

Hebrew (project library `genesis-woh/chapter-6.json`, `text`):

- GEN-WOH-6:2: וַיִּרְא֤וּ בְנֵי־הָֽאֱלֹהִים֙ אֶת־בְּנ֣וֹת הָֽאָדָ֔ם
- GEN-WOH-6:4: אֲשֶׁ֨ר יָבֹ֜אוּ בְּנֵ֤י הָֽאֱלֹהִים֙ אֶל־בְּנ֣וֹת הָֽאָדָ֔ם וְיָלְד֖וּ לָהֶ֑ם הֵ֧מָּה הַגִּבֹּרִ֛ים אֲשֶׁ֥ר מֵעוֹלָ֖ם אַנְשֵׁ֥י הַשֵּֽׁם

Deciding point: the statement about the text is only that Genesis speaks of "fils d'Elohim" and "filles des hommes"; the Hebrew has בְנֵי־הָאֱלֹהִים and בְּנוֹת הָאָדָם, and children born to them. Counted once (two occurrences). The classification covers that textual reference only; see "Absent or ambiguous" for the rest of the sentence.

**3. ETTMTTP-2:124 — `supported` (first clause verbatim, second clause adapted)**

- ETTMTTP-2:124: … et, comme prévu, nous avons dit au Nord donne et au Midi ne retiens pas, j'ai fait venir tes fils et tes filles des extrémités de la Terre, comme l'avait écrit Isaïe, et tu as pu retrouver ton pays …

Hebrew (Sefaria, "Miqra according to the Masorah"), Isaiah 43:6:

- אֹמַ֤ר לַצָּפוֹן֙ תֵּ֔נִי וּלְתֵימָ֖ן אַל־תִּכְלָ֑אִי הָבִ֤יאִי בָנַי֙ מֵרָח֔וֹק וּבְנוֹתַ֖י מִקְצֵ֥ה הָאָֽרֶץ׃

Lexicon lines (BDB via BibleHub):

- תֵּימָן (Strong 8486): "noun feminine Isaiah 43:6 south, south wind … of territory, the south Isaiah 43:6 (opposed to צָפוֺן)".
- כָּלָא (Strong 3607): "verb shut up, restrain, withhold … 2feminine singular תִּכְלָאִ֑י Isaiah 43:6".

Deciding point: "au Nord donne et au Midi ne retiens pas" corresponds word for word to לַצָּפוֹן תֵּנִי וּלְתֵימָן אַל־תִּכְלָאִי. The continuation is adapted: the Hebrew is an imperative with first-person possessives (הָבִיאִי בָנַי … וּבְנוֹתַי, "bring my sons … and my daughters"), with מֵרָחוֹק ("from afar") for the sons and מִקְצֵה הָאָרֶץ for the daughters; the French has a completed first-person act and second-person possessives ("j'ai fait venir tes fils et tes filles des extrémités de la Terre"). The source gives no chapter or verse; the identification with Isaiah 43:6 is mine, by matching the wording.

**4. ETTMTTP-3:256 — `not_checkable`**

- ETTMTTP-3:256: "Il y aura des signes dans le ciel", cela est écrit depuis longtemps...

No writing is named, so there is no single text to compare. Nearest wordings found:

- Joel 3:3 (Sefaria, "Miqra according to the Masorah"): וְנָֽתַתִּי֙ מֽוֹפְתִ֔ים בַּשָּׁמַ֖יִם וּבָאָ֑רֶץ (first person, "in the heavens and on the earth").
- Luke 21:11 (project library `luke-woh/chapter-21.json`, Greek): ἀπ’ οὐρανοῦ σημεῖα μεγάλα ἔσται; Luke 21:25: Καὶ ἔσονται σημεῖα ἐν ἡλίῳ καὶ σελήνῃ καὶ ἄστροις.

The preceding sentence of the same paragraph is "Relis tous les écrits des anciens prophètes", which does not decide between them.

### Separate list: other languages, traditions and symbols (not classified)

- ETTMTTP-3:178 (Greek-derived word): N'oublie pas que l'apocalypse, c'est-à-dire littéralement l'âge de la révélation, est arrivée comme cela était prévu. — For information only: Thayer's Greek Lexicon via BibleHub (Strong NT 602) begins "ἀποκάλυψις … an uncovering; 1. properly, a laying bare, making naked … 2. tropically … a disclosure of truth".
- ETTMTTP-2:121 (same word): C'est là un signe que reconnaîtront ceux qui ont les yeux ouverts, le signe de la révélation, de l'apocalypse.
- ETTMTTP-3:257 (same word): … le prophète de l'apocalypse, c'est-à-dire de l'époque où tout peut être compris.
- ETTMTTP-2:64 (Arabic name): Un peu plus loin vous pouvez voir Mahomet dans les écrits duquel je suis appelé Allah car il n'osait pas me nommer par respect.
- ETTMTTP-2:24 (symbol): C'est pour cela que dans notre emblème figure le svastika1 ou croix gammée que l'on retrouve dans de nombreux écrits anciens et qui signifie le cycle.
- ETTMTTP-2:35 (symbols): … l'étoile de David composée de deux triangles imbriqués l'un dans l'autre, ce qui veut dire "ce qui est en haut est comme ce qui est en bas". Avec le svastika1 ou croix gammée, qui signifie que tout est cyclique … Vous pouvez d'ailleurs retrouver ces deux symboles assemblés dans des écrits anciens comme le Bardo Thödol ou Livre des morts du Tibet et bien d'autres encore.
- ETTMTTP-2:24 (Buddhism): C'est ce qu'explique le bouddhisme, en disant qu'au moment de la mort "l'âme" du mourant doit être suffisamment vigilante pour échapper aux nombreux "démons" …
- ETTMTTP-2:105–109 (Qur'an, quoted with reference): Déjà, dans le Coran, Mahomet, qui est parmi nous, disait à propos des prophètes: “Le moment approche pour les hommes de rendre des comptes …” (Le Coran, sourate 21, versets 1 à 5).
- ETTMTTP-2:110–111 (New Testament, quoted with reference): “Qu'il descende (tout seul) de la croix maintenant... car il a dit : Je suis le fils de Dieu” (Matthieu, XXVII, 42-43)
- ETTMTTP-3:184 (Tibetan): "L'esprit et la matière sont éternellement la même chose" (Le Livre des Morts du Tibet).
- ETTMTTP-3:228 (Buddhist writings): Et toi, bouddhiste, tes écrits indiquent que le nouveau Bouddha doit naître en Occident …
- ETTMTTP-3:229 (Qur'an, paraphrase): Et toi, musulman, Mahomet t'as rappelé que les Juifs avaient fait une erreur en tuant les prophètes, et que les chrétiens avaient fait une erreur en adorant le prophète plus que celui qui envoie le prophète …
- ETTMTTP-3:232 (Qur'an): "L'heure s'approche quand la Lune se fend !" (Le Coran, sourate 54, verset 1).
- ETTMTTP-3:239 (Qur'an): "Sur des lits aux étoffes artistiquement arrangées, …" (Le Coran, sourate 56, versets 15 à 23).
- ETTMTTP-3:246 (New Testament phrase glossed): … à Jésus quand il vous disait de vous aimer les uns les autres et de respecter les Créateurs : "le père qui est dans les cieux" …
- ETTMTTP-3:250 (Gospels): On a lu et relu les évangiles qui disaient : "Tu ne te feras pas appeler mon père car vous n'avez qu'un seul père, celui qui est dans les cieux" …
- ETTMTTP-3:251 (unnamed "textes", Gospel register): On a lu et relu des textes qui disaient : "Tu prendras la route sans même emmener une paire de sandales de rechange" …

None of the New Testament, Qur'anic or Tibetan quotations was compared with its source; that is outside the protocol.

## Absent or ambiguous

- **No lexical statement.** Within the `Yahweh` paragraphs of this book there is no sentence of the form "word X means Y" for any Hebrew word, name or title, and no appeal to the Hebrew, to "the original" or to translation. The name is only stated, not glossed: ETTMTTP-2:50, "Mon nom est Iahvé et je suis le président du conseil des éternels."
- **"Élohim".** The word is used throughout (plural "Elohim"; the narrator, not the Yahweh speaker, uses the singular "Eloha" at 2:48), but no `Yahweh` paragraph in chapters 1–3 explains what the word means. Nothing was therefore set aside under the protocol's exclusion.
- **Item 1, chapter number.** The digitization prints "(Ezéchiel, XXVII, 3, 7-8, 10)". I did not inspect a printed 1975 edition or a page scan, so I cannot say whether "XXVII" is in the original printing or arose in digitization.
- **Item 1, translation dependence.** "nerfs" against גִּדִים (BDB "sinew") and "branle-bas" against רַעַשׁ (BDB "quaking, shaking … > rustling, rattling") depend on the French senses of those words; I did not consult a French dictionary or identify which published French Bible the quotation follows. "(les ossements)" in parentheses is an insertion marked as such in the source; "il étendit sur eux de la peau" has an explicit subject "il" where the Hebrew וַיִּקְרַם has none stated. BDB itself records a division on רַעַשׁ at Ezekiel 37:7 (earthquake versus rattling).
- **Item 2, extent.** Only the reference to what Genesis mentions was classified. The remainder of 2:104 and 2:123 — that the Jews, or the people of Israel, are the descendants of those unions — is not presented by the source as something Genesis says, and Genesis 6:4 as quoted above names the offspring only as הַגִּבֹּרִים … אַנְשֵׁי הַשֵּׁם. I did not classify it.
- **Item 3, form.** The words are not set in quotation marks in the source and are woven into first-person speech; whether this counts as "what the text says" or as an allusion is a judgement. I listed it because of "comme l'avait écrit Isaïe".
- **Item 4, scope.** Whether an unnamed "cela est écrit" belongs in the classified list or in the separate list depends on which writing is meant; it is listed as `not_checkable` for that reason. If it is moved to the separate list the totals become `supported` 3, others 0.
- **"apocalypse".** The three glosses (3:178, 2:121, 3:257) concern a Greek-derived word that is also a biblical book title. I placed them in the separate list because the protocol's lexicon is a Biblical Hebrew one; a reader who counts "biblical word" as including New Testament Greek would move them into the main list, where they would need a Greek lexicon and the question of whether "l'âge de" is part of the literal meaning (Thayer's entry as quoted gives "an uncovering", "a disclosure").
- **Speaker field.** The scope is defined by the `speaker` field, and the labelling is not uniform. In chapter 2, paragraphs 2:70, 2:74 and 2:77 are labelled `Yahweh` but consist of first-person narration by the narrator (e.g. 2:74, "Effectivement, ce que j'avais vu correspondait parfaitemet à la description d'Ezéchiel."). In chapter 3 ("Les Clés") 258 of 266 paragraphs are labelled `Yahweh`, yet the voice speaks of "les Elohim nos pères, nos créateurs" (3:5) and in places in the narrator's own first person (3:174, "De nombreux médiums sont venus me voir en me demandant ce qu'ils devaient faire"; 3:208, "Qui croient en ce qui m'a été révélé"). I followed the field as given; the attribution of chapter 3 statements (items 4, and the 3:xxx entries in the separate list) to the non-human speaker rests on that labelling.

## Adjacent observations

- Unattributed biblical echoes in `Yahweh`-labelled paragraphs, not presented as statements about a text and not classified:
  - ETTMTTP-3:24: "Tu es poussière et tu redeviendras poussière". Compare GEN-WOH-3:19 (project library): כִּֽי־עָפָ֣ר אַ֔תָּה וְאֶל־עָפָ֖ר תָּשֽׁוּב.
  - ETTMTTP-3:11: … les Elohim nous ont créés à leur image … (also 3:109, 3:127, 3:166). Compare GEN-WOH-1:26–27: בְּצַלְמֵ֖נוּ כִּדְמוּתֵ֑נוּ … בְּצֶ֥לֶם אֱלֹהִ֖ים.
  - ETTMTTP-3:235: Et quand les Elohim dirent aux habitants de Sodome et Gomorrhe de quitter la ville sans se retourner, certains ne croyaient pas à ce qui était annoncé et furent détruits. Compare GEN-WOH-19:17: אַל־תַּבִּ֣יט אַחֲרֶ֔יךָ (addressed in the singular, in the Lot narrative).
  - ETTMTTP-3:234: Autrefois Noé ne fut pas cru et les gens se moquaient de lui quand il se préparait pour la destruction. Not compared with any text.
  - ETTMTTP-3:176: Que ceux qui ont des oreilles entendent. ETTMTTP-3:179: Il est dit que quand les temps seront venus il y aura beaucoup de faux prophètes. ETTMTTP-3:13: "Aide-toi, le Ciel t'aidera". Not compared.
- Statements about the "original sense" of a practice rather than of a word: ETTMTTP-3:116, "Tu retrouveras ainsi le sens originel de la prière" (télépathic communication; repeated 3:207, 3:248).
- ETTMTTP-3:71 "Conformément à ce qui est écrit dans le Livre" and 3:80 "Le Livre qui dit la Vérité" refer to the author's earlier book, not to a biblical text.
- The only occurrence of `hébreu` in the book is the narrator's, ETTMTTP-2:47: "… tous parlaient une langue que je ne comprenais pas et qui ressemblait à de l'hébreux."
- The project's editorial `notes` on 2:24 and 2:35 exist in the data file; they were seen while checking the paragraph structure and were not used.
- Web sources were reached without difficulty; HALOT was not attempted beyond noting it is not on a public site I could open.
