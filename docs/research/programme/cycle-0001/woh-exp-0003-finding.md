# Finding: woh-exp-0003

- Date: 2026-11-22
- Source and edition inspected:
  - *The Book Which Tells the Truth*, project digitization, French base text (`text` field), files `data-library/the-book-which-tells-the-truth/chapter-1.json` … `chapter-7.json` (759 paragraphs; refIds `TBWTT-N:n`). The `i18n.en` field was used only as a reading aid and is not quoted.
  - Hebrew: Isaiah 6 from the project book `data-library/isaiah-woh/` (`chapter-6.json`, `source-he-6.json`; its source note says "Tanach with Ta'amei Hamikra", fetched from sefaria.org). No `-woh` book exists for Joshua, 1–2 Kings, Zechariah or Psalms; `isaiah-woh` has no chapters 13–14 and `job-woh` has no chapter 37. For those, the Masoretic text was read from Sefaria (`https://www.sefaria.org/api/v3/texts/<ref>?version=hebrew`, version title returned: "Miqra according to the Masorah"), fetched 2026-11-22.
  - Lexicon: Brown-Driver-Briggs as reproduced on Sefaria (`https://www.sefaria.org/api/words/<headword>`, lexicon "BDB Dictionary", entry ids `BDBnnnnn` given below). For four headwords the Sefaria lookup returned no BDB entry and the BDB section of BibleHub was used instead (`https://biblehub.com/hebrew/<Strong>.htm`): שַׁחַק (7834), רְאִי (7209), תְּקוּפָה (8622), שָׁמַיִם (8064). HALOT was not reached.
- Access achieved: `project_digitization` (book); `full_text` (Hebrew verses and BDB entries, public reproductions)
- Search performed:
  1. All seven chapters dumped to one text file (refId, speaker, French text). Every parenthetical reference of the form `(Book, chapter-verse)` was extracted by regular expression and listed (about 230 references).
  2. Chapters 1–2 and TBWTT-3:1–41 contain only Genesis and Exodus references (also checked by grep for the names Nombres, Deutéronome, Josué, Juges, Samuel, Rois, Isaïe, Jérémie, Daniel, Psaume, Job, Lévitique, Zacharie, Amos, Proverbes: no hits before TBWTT-3:43).
  3. TBWTT-3:42 to 3:157 (Leviticus to the start of the Ezekiel section) and TBWTT-3:206 to 3:262 (Daniel to Job) were read in full, paragraph by paragraph, including quotations whose reference is given in running text and not in parentheses (Lév. XXI 17-18, Nombres XI 7-8, Josué III 15-16, I Rois XVII-6, II Rois I-12, the Michaël quotation in Daniel).
  4. Reading stopped being exhaustive after TBWTT-3:262, because eight qualifying quotations (and six reserve candidates) had been found before that point. TBWTT-3:263 to the end of chapter 7 was covered only by the reference list of step 1, not by a reading of the commentary.

## Answer

### Two reading decisions the protocol left open

The list of eight depends on two decisions. Both are stated here so the count can be redone the other way; the data for the alternative are in "Adjacent observations".

- **Commentary placed before the quotation.** The protocol says "the same or the following paragraph". In this book the comment often introduces the quotation from the paragraph before (for example TBWTT-3:129 before the quotation in 3:130–131). I counted an introducing paragraph as commentary when it is plainly about the quoted passage. Three of the eight (nos. 2, 4 and, for its position, 1) depend on this or on a small gap; they are marked.
- **Sky or flight not named with a listed word.** I required the commentary itself (not the quoted verse) to speak of the sky or of flight. Joshua X-11 ("bombardement", no sky word in the commentary) was left out as borderline; Isaiah VI 1-2 ("six petits réacteurs … directionnels") was kept as speaking of a flight device, and is marked.

### The eight qualifying quotations, in book order

| # | Quotation (refId) | Commentary (refId) | Hinge word(s) | Hebrew at that place | Class |
|---|---|---|---|---|---|
| 1 | I Rois VIII 12-13 (TBWTT-3:104) | TBWTT-3:107 (after two further quotation paragraphs, 3:105–106) | « nuage » (« réside dans un nuage ») | עֲרָפֶל (1 Kgs 8:12) | `carried` |
| 2 | I Rois XVIII-38 (TBWTT-3:116) | TBWTT-3:115 (preceding paragraph) | no hinge word | — | — |
| 3 | I Rois XIX 11-12 (TBWTT-3:120) | TBWTT-3:121 | no hinge word | — | — |
| 4 | II Rois II-1 (TBWTT-3:130–131) | TBWTT-3:129 (preceding paragraph) | no hinge word | — | — |
| 5 | II Rois II-11 (TBWTT-3:132) | TBWTT-3:133 | « chevaux de feu » | סוּסֵי אֵשׁ | `carried` |
|   |   |   | « char de feu » | רֶכֶב־אֵשׁ | `carried` (see note on number) |
| 6 | Isaïe VI 1-2 (TBWTT-3:144) | TBWTT-3:145 (borderline qualification) | « six ailes » | שֵׁשׁ כְּנָפַיִם | `carried` |
| 7 | Isaïe XIII 4-5 (TBWTT-3:146) | TBWTT-3:147 | « Ils viennent d'un pays lointain, des confins du ciel » | בָּאִים מֵאֶרֶץ מֶרְחָק מִקְצֵה הַשָּׁמָיִם | `carried` |
| 8 | Isaïe XIV-13 (TBWTT-3:148) | TBWTT-3:149 | no hinge word | — | — |

### Totals

- Qualifying quotations taken: 8 (more than eight exist; see reserve list).
- Hinge words: 5, in 4 quotations.
  - `carried`: 5
  - `shifted`: 0
  - `absent`: 0
  - `not_checkable`: 0
- Quotations with no hinge word: 4 (nos. 2, 3, 4, 8).

In every one of the five cases the French word of the quoted verse (nuage, chevaux, char, ailes, confins du ciel) is an ordinary BDB sense of the Hebrew word at that place. In each case the technical object named by the commentary (engin en orbite, tuyères, fusée, réacteurs) is the commentary's own gloss on that French word; it is not a word of the quoted French verse and was therefore not what the protocol's classes test.

### Skipped quotations

No New Testament or non-Hebrew-original quotation stands before the eighth qualifying quotation, so none had to be skipped to reach it. Later in chapter 3 the book quotes Tobit (TBWTT-3:264) and the Wisdom of Solomon (TBWTT-3:266, 3:268, 3:270); chapter 4 and part of chapter 5 quote Matthew, Mark, Luke and Acts. These fall outside the first eight and were not examined.

## Quotations

### 1. I Rois VIII 12-13

- TBWTT-3:104: « Iahvé a dit qu'il réside dans un nuage. J'ai donc bâti vraiment une Maison pour ta demeure ». (I Rois, VIII, 12-13)
- TBWTT-3:105: « La gloire de Iahvé avait rempli la maison de Iahvé ». (I Rois, VIII-11) « La nuée remplit la maison de Iahvé ». (I Rois, VIII-10)
- TBWTT-3:106: « J'y résiderai au milieu des fils d'Israël ». (I Rois, VI-13)
- Commentary, TBWTT-3:107: "Qu'il réside dans un nuage, c'est-à-dire dans un engin en orbite autour de la Terre, au-dessus des nuages... mais allez donc faire comprendre cela à des primitifs."
- Hebrew, 1 Kgs 8:12 (Sefaria, Miqra according to the Masorah): אָז אָמַר שְׁלֹמֹה יְהֹוָה אָמַר לִשְׁכֹּן בָּעֲרָפֶל׃
- BDB, עֲרָפֶל (Sefaria BDB07664): "n.m. cloud, heavy cloud … ע׳ in which God dwells Ex 20:18 …, 1 K 8:12 = 2 Ch 6:1; + עָנָן Dt 4:11 (also חֹשֶׁךְ) …"
- Class: `carried`.
- The same block quotes « La nuée » for 1 Kgs 8:10; Hebrew there is הֶעָנָן. BDB, עָנָן (BDB07470): "cloud-mass, cloud … especially of theophanic cloud … in temple 1 K 8:10, 11". The commentary takes up only the wording of 3:104.

### 2. I Rois XVIII-38

- Commentary, TBWTT-3:115: "Évidemment, au moment convenu à l'avance entre Elie et les créateurs, le bûcher qui leur était destiné s'alluma, même inondé, grâce à un puissant rayon se rapprochant du laser et émis d'un vaisseau caché dans les nuages."
- TBWTT-3:116: « Et le feu de Iahvé tomba, il dévora l'holocauste et le bois, les pierres et la poussière, puis il lampa l'eau qui était dans la rigole ». (I Rois, XVIII-38)
- No word of the verse is taken up; the comment comes before the quotation and describes the event. Recorded as "no hinge word".
- Hebrew, 1 Kgs 18:38: וַתִּפֹּל אֵשׁ־יְהֹוָה וַתֹּאכַל אֶת־הָעֹלָה וְאֶת־הָעֵצִים וְאֶת־הָאֲבָנִים וְאֶת־הֶעָפָר וְאֶת־הַמַּיִם אֲשֶׁר־בַּתְּעָלָה לִחֵכָה׃

### 3. I Rois XIX 11-12

- TBWTT-3:120: « Et voici que Iahvé passe. Un vent très fort secoue les montagnes et brise les rochers par devant Iahvé ; mais Iahvé n'est pas dans le vent. Et après le vent, un tremblement de terre (...) Et après le tremblement de terre, un feu ; mais Iahvé n'est pas dans le feu. Et après le feu, le son d'une brise légère ». (I Rois, XIX, 11-12)
- Commentary, TBWTT-3:121: "Vous avez là, la description exacte de l'atterrissage d'un engin comparable à vos fusées actuelles."
- General explanation; no word of the verse is taken up. "No hinge word".

### 4. II Rois II-1

- Commentary, TBWTT-3:129: "Dans II Rois, II Elie est l'invité des créateurs dans un vaisseau spatial qui décolle et l'emmène."
- TBWTT-3:130–131: « Quand Iahvé fit monter Elie aux cieux dans un tourbillon (...) ». (II Rois, II-1)
- General introduction; no word of the verse is taken up. "No hinge word".
- Hebrew, 2 Kgs 2:1: וַיְהִי בְּהַעֲלוֹת יְהֹוָה אֶת־אֵלִיָּהוּ בַּסְעָרָה הַשָּׁמָיִם …

### 5. II Rois II-11

- TBWTT-3:132: « (...) voici qu'un char de feu et des chevaux de feu s'interposèrent entre eux deux (entre Elie et Elisée) : Elie monta aux cieux dans le tourbillon ». (II Rois, II-11)
- Commentary, TBWTT-3:133: "C'est le décollage d'un engin volant et le feu des tuyères fait que le narrateur parle de chevaux de feu. Si aujourd'hui vous prenez des primitifs d'Amérique du Sud ou d'Afrique noire et que vous les faites assister au décollage d'une fusée, ils parlent de char de feu et de chevaux de feu en revenant dans leurs tribus, […]"
- Hebrew, 2 Kgs 2:11: … וְהִנֵּה רֶכֶב־אֵשׁ וְסוּסֵי אֵשׁ וַיַּפְרִדוּ בֵּין שְׁנֵיהֶם וַיַּעַל אֵלִיָּהוּ בַּסְעָרָה הַשָּׁמָיִם׃
- Hinge « chevaux de feu »: BDB, סוּס² (BDB06689): "n.m. Ex 15:1 horse … סוּסֵי אֵשׁ 2 K 2:11 (Elijah), cf. 6:17". BDB, אֵשׁ (BDB00883): "fire … 2. of supernatural fire, attending theophany". Class: `carried`.
- Hinge « char de feu »: BDB, רֶכֶב (BDB09336): "chariotry, chariot, mill-stone; appar. also riders … 1. coll. chariotry, chariots … רֶכֶב אֵשׁ 2 K 2:11 chariotry of fire (at Elijah's translation)". Class: `carried`. Note: "chariot" is among the entry's head senses, but BDB files this verse under the collective sense ("chariotry of fire"), where the French has the singular « un char ».
- Not counted as hinge words because the commentary does not take up the words themselves: « monta aux cieux » (וַיַּעַל … הַשָּׁמָיִם; BDB עָלָה, BDB07293, "go up, ascend, climb … c. acc. of place whither … (הַ)שָּׁמַיִם … 2 K 2:11") and « tourbillon » (סְעָרָה; BDB06830, "tempest, storm-wind … storm-wind of Elijah's translation 2 K 2:1, 11").

### 6. Isaïe VI 1-2

- TBWTT-3:144: « L'année de la mort du roi ozias, je vis Adonaï assis sur un trône élevé (...). Des séraphins se tenaient au-dessus de lui. Chacun avait six ailes, deux dont il couvrait sa face, deux dont il couvrait ses pieds et deux pour voler ». (Isaïe, VI, 1-2)
- Commentary, TBWTT-3:145: "C'est là, la description des créateurs revêtus d'un scaphandre autonome muni de six petits réacteurs : deux dans le dos, deux aux mains et deux aux pieds, directionnels ceux-ci."
- Hebrew, `isaiah-woh` ISA-6:2: שְׂרָפִים עֹמְדִים מִמַּעַל לוֹ שֵׁשׁ כְּנָפַיִם שֵׁשׁ כְּנָפַיִם לְאֶחָד בִּשְׁתַּיִם יְכַסֶּה פָנָיו וּבִשְׁתַּיִם יְכַסֶּה רַגְלָיו וּבִשְׁתַּיִם יְעוֹפֵף׃
- Hinge « six ailes » (taken up as "six petits réacteurs", with the two-two-two division repeated): BDB, כָּנָף (BDB04582): "wing, extremity … du. כְּנָפַיִם … (even of more than two, Is 6:2(×2) …) … 1. wing, a. of birds … c. of cherubim … d. of seraphim Is 6:2(×2)". Class: `carried`.
- « pour voler »: יְעוֹפֵף; BDB, עוּף (BDB07099), Pōʿl. "1. fly about, to and fro; Impf. 3 ms. יְעוֹפֵף of birds Gn 1:20 (P); seraphim Is 6:2". Not taken up as a word by the commentary.

### 7. Isaïe XIII 4-5

- TBWTT-3:146: « Sur les montagnes, un bruit de tumulte ! Quelque chose comme un peuple nombreux ! Le bruit du vacarme des royaumes ! Les nations rassemblées ! Iahvé des armées passe en revue l'armée du combat. Ils viennent d'un pays lointain, des confins du ciel, Iahvé et les instruments de son courroux, pour détruire tout le pays ». (Isaïe, XIII, 4-5)
- Commentary, TBWTT-3:147: "Toute la vérité est décrite ici. Il fallait lire entre les lignes et comprendre. « Ils viennent d'un pays lointain, des confins du ciel ». on ne pouvait être plus clair."
- Hebrew, Isa 13:5 (Sefaria): בָּאִים מֵאֶרֶץ מֶרְחָק מִקְצֵה הַשָּׁמָיִם יְהֹוָה וּכְלֵי זַעְמוֹ לְחַבֵּל כׇּל־הָאָרֶץ׃
- BDB, מֶרְחָק² (BDB09295): "distant place, distance … א׳ (ה)מֶרְחָק land of distance, distant land Is 13:5".
- BDB, קָצֶה (BDB08896): "end, extremity … מִק׳ הַשָּׁמַיִם Is 13:5 (‖ מֵאֶרֶץ מֶרְחָק), ψ 19:7".
- BDB, שָׁמַיִם (BibleHub 8064): "heavens, sky … 1. a. visible heavens, sky … וְעַד־קְצֵה הַשּׁ׳ מִקְּצֵה הַשּׁ׳ of limits of horizon Deuteronomy 4:32, compare Deuteronomy 30:4; Nehemiah 1:9; Psalm 19:7".
- Class: `carried`. The commentary repeats the phrase and calls it clear; it adds no gloss of its own to it.
- TBWTT-3:149 (two paragraphs on) returns to this verse: "L'armée des cieux est décrite ici à cette époque, au moment où elle vient, avec les instruments de son courroux, pour détruire tout le pays." For « instruments de son courroux » the Hebrew is כְלֵי זַעְמוֹ; BDB, כְּלִי (BDB04502): "article, utensil, vessel … fig. of God's weapons כְּלֵי־מָוֶת ψ 7:14 …; כ׳ זַעְמוֹ Is 13:5 Je 50:25". This phrase lies outside "the same or the following paragraph" and is repeated without explanation, so it was not counted.

### 8. Isaïe XIV-13

- TBWTT-3:148: « C'est toi qui disais dans ton cœur: je monterai aux cieux, au-dessus des étoiles de Dieu ». (Isaïe, XIV-13)
- Commentary, TBWTT-3:149: "Allusion aux savants disparus qui avaient acquis suffisamment de connaissances scientifiques pour entreprendre d'aller sur la planète des créateurs et furent détruits à Sodome et Gomorrhe."
- The comment explains the sentence as a whole and takes up no word of it. "No hinge word".
- Hebrew, Isa 14:13 (Sefaria): וְאַתָּה אָמַרְתָּ בִלְבָבְךָ הַשָּׁמַיִם אֶעֱלֶה מִמַּעַל לְכוֹכְבֵי־אֵל אָרִים כִּסְאִי …

## Absent or ambiguous

- **Which eight.** The set is not fixed by the text alone; it turns on the two reading decisions above. Under the strictest reading (commentary only in the same or the next paragraph, and commentary must itself name sky or flight), nos. 2 and 4 drop out, no. 1 is doubtful (its comment is three paragraphs after the quotation, separated only by further quotations), and no. 6 is doubtful. The list would then be filled from the reserve candidates below.
- **What counts as "taking up" a word.** In nos. 2, 4 and 8 the commentary plainly corresponds to particular words of the verse (« le feu de Iahvé tomba »; « fit monter … aux cieux dans un tourbillon »; « je monterai aux cieux »), but it does not repeat or gloss those words; it restates the event. I recorded these as "no hinge word". If a reader counts such implicit correspondences as hinges, the Hebrew has a plain counterpart in each case (אֵשׁ־יְהוָה … וַתִּפֹּל; בְּהַעֲלוֹת … בַּסְעָרָה הַשָּׁמָיִם; הַשָּׁמַיִם אֶעֱלֶה), with BDB senses "fire", "go up, ascend", "tempest, storm-wind", "heavens, sky" (entries cited above).
- **No. 6, « six ailes ».** The commentary does not repeat the word « ailes »; it replaces "six ailes" by "six petits réacteurs" and keeps the count and the division in pairs. I counted this as taking the phrase up.
- **No. 5, « char ».** Carried on the head sense "chariot"; BDB's own placement of 2 Kgs 2:11 is the collective "chariotry of fire".
- **No. 1, « nuage ».** BDB gives "cloud, heavy cloud". The separate Strong's-based summary shown beside it on Sefaria ("BDB Augmented Strong", no. 6205) reads "cloud, heavy or dark cloud, darkness, gross darkness, thick darkness". Only BDB proper was used for the classification.
- **French Bible version.** The digitization does not name the French translation the book quotes from; I did not try to identify it, and the French of the quotations was not compared with any printed French Bible.
- **Lexicon.** All checks rest on BDB (1906) in two web reproductions. HALOT was not consulted. The BibleHub BDB text shows OCR damage in places (for example "חִרְקִיעַ" for תַּרְקִיעַ).
- **Not inspected.** The commentary of TBWTT-3:263 to the end of chapter 7 was not read for this question.

## Adjacent observations

### Reserve candidates (for a recount under a different reading)

In book order, with the same checks. None of these is in the eight above.

- **Before no. 1 — Josué X-11** (TBWTT-3:67; borderline, excluded). Introduced at 3:66: "Un peu plus tard, c'est un véritable bombardement qui est effectué :"; quotation: « Iahvé lança des cieux contre eux de grandes pierres (...). Ceux qui moururent par les pierres de grêle furent plus nombreux que ceux que les fils d'Israël tuèrent par l'épée ». Comment at 3:68: "Un bombardement en règle qui tua plus de gens que les armes blanches du peuple d'Israël." The words « des cieux » are in the quoted verse; the commentary itself has no sky word. No word is taken up (no hinge word). Hebrew: … הִשְׁלִיךְ עֲלֵיהֶם אֲבָנִים גְּדֹלוֹת מִן־הַשָּׁמַיִם … בְּאַבְנֵי הַבָּרָד. BDB, בָּרָד (BDB01448): "hail … another great hailstorm Jos 10:11 (E), where אַבְנֵי הַבּ׳".
- **After no. 8 — Zacharie V 1-2** (TBWTT-3:234–235). Introduced at 3:233: "Dans Zacharie V, il y a encore la description d'un engin volant :"; quotation: « Je recommençai à lever les yeux et j'eus une vision : et voici un rouleau volant (...) d'une longueur de vingt coudées (9 mètres) et d'une largeur de dix coudées (4,50 mètres) ». The metric figures stand inside the quotation marks. Hebrew: מְגִלָּה עָפָה. BDB, מְגִלָּה (BDB01846): "n.f. roll (writing, book; late) … roll of writing, book … מ׳ alone … Zc 5:1, 2"; BDB, עוּף (BDB07099): "fly … roll (in vision) Zc 5:1, 2". If « rouleau volant » is counted as a hinge (the comment precedes and does not repeat the words), the French words are carried; BDB's sense is specifically a roll of writing.
- **Zacharie V-9** (TBWTT-3:237): « (...) et voici qu'apparurent deux femmes. Il y avait du vent dans leurs ailes, car elles avaient des ailes comme des ailes de cigogne ». Comment at 3:238: "Deux compagnes féminines des créateurs équipées de combinaisons de vol autonomes évoluent devant Zacharie." Hebrew: וְרוּחַ בְּכַנְפֵיהֶם וְלָהֵנָּה כְנָפַיִם כְּכַנְפֵי הַחֲסִידָה. BDB, כָּנָף (BDB04582): "1. wing … e. of women in Zec.'s vision Zc 5:9(×2)". If « ailes » is counted as a hinge: carried.
- **Psaumes XIX-7** (TBWTT-3:241): « (...) son point de départ est à un bout des cieux et son orbite à l'autre bout... ». Comment at 3:242: "Les créateurs sont venus d'une planète très éloignée de l'orbite terrestre." Hebrew, Ps 19:7: מִקְצֵה הַשָּׁמַיִם מוֹצָאוֹ וּתְקוּפָתוֹ עַל־קְצוֹתָם. BDB, מוֹצָא (BDB04101): "place or act of going forth, issue, export, source, spring … 1. a going forth: a. the act, of י׳ Ho 6:3; of the sun = rising ψ 19:7". BDB, תְּקוּפָה (BibleHub 8622): "coming round, circuit … singular suffix of finished circuit of sun Psalm 19:7 (opposed to מוֺצָאוֺ)". The possessive « son » has its antecedent outside the quoted fragment: in the Hebrew of verses 5–6 it is the sun (לַשֶּׁמֶשׁ … וְהוּא). « point de départ » corresponds to מוֹצָא; « orbite » corresponds to תְּקוּפָה "circuit", and the commentary reuses the word as "l'orbite terrestre". Whether « orbite » is `carried` or `shifted` is a judgement I leave open; it is outside the eight.
- **Psaumes XXXIII 13-14** (TBWTT-3:246): « Du haut des cieux Iahvé regarde, il voit tous les fils de l'homme, du lieu de son habitation il observe tous les habitants de la terre (...) ». Comment at 3:247: "Les créateurs surveillent de leurs engins volants les agissements de l'humanité comme ils l'ont toujours fait." Hebrew: מִשָּׁמַיִם הִבִּיט יְהֹוָה … מִמְּכוֹן־שִׁבְתּוֹ הִשְׁגִּיחַ. The Hebrew has "from [the] heavens" (מִן + שָׁמַיִם); there is no separate word for « haut ». BDB, מָכוֹן (BDB04414): "fixed or established place, foundation … of heavens מְכוֹן שִׁבְתְּךָ 1 K 8:39, 43, 49 …, cf. ψ 33:14". No word is explicitly taken up.
- **Job XXXVII-18** (TBWTT-3:259): « (...) étendras-tu, avec lui, des nuages, solides comme un miroir de métal fondu ? ». Comment at 3:260: "Est-ce que l'homme est capable de faire des « nuages solides », des engins volants métalliques en réalité." This is the clearest explicit hinge in the whole stretch (the commentary re-quotes « nuages solides » and glosses it). Hebrew: תַּרְקִיעַ עִמּוֹ לִשְׁחָקִים חֲזָקִים כִּרְאִי מוּצָק׃ BDB, שַׁחַק (BibleHub 7834): "dust, cloud (as fine, thin) … 1 fine dust … 2 (thin) cloud, usually plural (often ‖ שָׁמַיִם) … = heavens, sky Job 37:18 (with תַּרְקִיעַ)". BDB, חָזָק (BDB02982): "strong, stout, mighty … e. firm, hard, of face … of sky Jb 37:18 (pred.)". BDB, רְאִי (BibleHub 7209): "noun masculine mirror; — כִּרְאִי מוּצָק Job 37:18 (simile)". BDB, יָצַק (BDB04112), Hoph. "2. Pt. = cast, molten … ראי Jb 37:18". BDB, רָקַע (BDB09551): "Hiph. … Jb 37:18 canst thou make with (= like) him a spreading for clouds (spread out clouds; cf. רָקִיעַ)?". So "cloud" is an ordinary sense of שַׁחַק, while BDB assigns this particular verse to "= heavens, sky" under שַׁחַק and to "clouds" under רָקַע; « solides » corresponds to חֲזָקִים "firm, hard"; « miroir de métal fondu » corresponds to רְאִי מוּצָק "cast/molten mirror", where the Hebrew has no separate word for « métal ».

### Quotations considered and not qualifying (commentary has no sky or flight)

Lév. XXI 17-18 (3:44); Nombres XI 7-8 (3:47), XVIII-13 (3:49), XXI-8 (3:51), XXXIII 52-53 (3:54); Deut. IV-37 (3:56); Josué III 15-16 (3:58, "rayon répulseur"), V-14 (3:62), VI-5 (3:64, ultra-sons), X-13 (3:70); Juges VI-21 (3:73), XIII (3:78–83); I Samuel III (3:88–91), XVII-26 (3:93), V-6 (3:97); II Samuel VI 6-7 (3:99; the comment at 3:100 uses "appareil" of the ark, not of anything in the sky); I Rois I-50 / II-28 (3:101), XIII (3:108, 3:110), XVII-6 (3:112), XVII 23-24 (3:114–115), XIX 5-6 (3:119), XXII-19 (3:122; « armée des cieux » is in the verse, the adjacent commentary does not speak of the sky), XXII-22 (3:124); II Rois I-12 (3:126; « le feu descende des cieux » is in the verse, the adjacent commentary speaks only of "protection"), I-15 (3:128), IV 42-44 (3:137), XVII-23 (3:141); Isaïe XIV-14 (3:150–151), XIV-17 (3:152), XV 8-9 (3:154), XXVI-20 (3:156); Daniel III-25, VI-23, X 5-6, XII (3:208–226); Jonas II (3:229–232, "sous-marin"); Psaumes VIII-6 (3:239), XIX-5 (3:243–244); Job I–II (3:250–256).

### Other points

- At TBWTT-3:149 the commentary says "L'armée des cieux est décrite ici". The phrase « armée des cieux » does not occur in the French of Isaïe XIII 4-5 or XIV-13 as quoted (XIII-4 has « Iahvé des armées » and « l'armée du combat », Hebrew יְהֹוָה צְבָאוֹת … צְבָא מִלְחָמָה); it occurs in the book's quotation of I Rois XXII-19 (TBWTT-3:122).
- In no. 6 the verse assigns the pairs of wings to covering the face, covering the feet, and flying; the commentary assigns the pairs of "réacteurs" to the back, the hands and the feet.
- In no. 2 the commentary's "vaisseau caché dans les nuages" has no counterpart in the quoted verse: 1 Kgs 18:38, French or Hebrew, mentions no cloud.
- In no. 1 the commentary reads the singular « un nuage » and then contrasts it with the plural, "au-dessus des nuages".
- TBWTT-3:243–244 quotes Psaumes XIX-5 as « Pour le soleil, il a dressé une tente sur la mer (...) ». The Hebrew of Ps 19:5 fetched from Sefaria ends לַשֶּׁמֶשׁ שָׂם־אֹהֶל בָּהֶם ("in them"); no word for "sea" stands there. The commentary on this quotation (3:245) is not about the sky, so it lies outside the question; whether « sur la mer » comes from the French Bible used or from the book or its digitization was not checked.
- TBWTT-3:251 (commentary on Job I-6) states: "Elohim, cela veut dire littéralement « venus du ciel » en Hébreu." Job I-6 did not qualify (the claim is about the word's meaning, not about the passage describing movement in the sky) and the statement was not checked against a lexicon here.
- The digitized French shows OCR artefacts in the quotations (lower-case « ozias », « ouzza », "on" for "On"); quotations above reproduce the digitized text, with straight apostrophes substituted for the typographic ones.
