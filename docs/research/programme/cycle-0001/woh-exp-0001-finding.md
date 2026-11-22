# Finding: woh-exp-0001

- Date: 2026-11-22
- Source and edition inspected: *Le Livre qui dit la vérité* (The Book Which Tells the Truth, 1974), project digitization, French base text (`text` field), files `data-library/the-book-which-tells-the-truth/chapter-1.json` … `chapter-7.json` (paragraph counts 64 / 92 / 305 / 118 / 68 / 29 / 83; paragraphs with speaker `Yahweh`: 28 / 86 / 294 / 112 / 59 / 26 / 38). The `i18n.en` rendering was not quoted and in practice not needed.
- Access achieved: `project_digitization` for the source. For the checks: Brown-Driver-Briggs (BDB) as reproduced on BibleHub (`biblehub.com/hebrew/<Strong no.>.htm`, section "Brown-Driver-Briggs", downloaded and read directly) and, for one entry BibleHub does not carry, the "BDB Dictionary" entry served by Sefaria (`sefaria.org/api/words/קדש`, reached only through a fetch tool that relays short quotations; Sefaria refused direct download). HALOT: not reached. Hebrew verse text: project file `genesis-woh/chapter-7.json` (Gen 7:17-18); BibleHub interlinear pages `biblehub.com/text/...` (Westminster Leningrad text as shown there) for Josh 10:13, Ezek 42:14, Ps 8:6, Ps 19:5, Josh 6:5; Sefaria v3 API (version "מקרא על פי המסורה") for the first half of Ezek 42:14. Greek of Matt 5:3: project file `matthew-woh/chapter-5.json` and BibleHub `text/matthew/5-3.htm`.
- Search performed:
  - Chapters 2 and 3 read in full in French (all 397 paragraphs, every speaker).
  - Chapters 1, 4, 5, 6, 7: sentence-level regex search of the French text, case-insensitive, for the protocol terms `hébreu`, `hébraï`, `signifi`, `veut dire / veulent dire / voulait dire / voulaient dire`, `traduit`, `traduction`, `traduire`, `original`, `originel`, `littéral`, `\bmots?\b`, `\bnoms?\b`, plus my additions `c’est-à-dire`, `en réalité`, `il est dit`, `il est écrit`, `écrit`, `Bible`, `appel`, `déform`, `copiste`, `recopi`, `dicté`, `Évangile`, `Testament`. Only `speaker == "Yahweh"` kept. Hits read in context (TBWTT-4:1-8, 4:22-28, 4:47-49, 4:76-79, 5:20-26, 5:65-67, 6:7, 6:10-14, 7:7-8, 7:32-36).
  - Chapters 1, 4, 5, 6, 7 were **not** read in full; a statement there that uses none of the terms above would have been missed.
  - Left out as instructed: the explanation of "Élohim" (TBWTT-2:5, 3:251, 5:21, 7:33) and the "dragons" sentence (TBWTT-2:22).

## Answer

The scope contains two kinds of material, and I have kept them apart because the protocol's lexicon test fits only the first.

**List A — explicit statements about what a word or name means, about the wording of the text, or about the original text** (10 statements in 9 paragraphs):

| # | refId | Subject | Class |
|---|---|---|---|
| A1 | TBWTT-2:10 | "jour" (Gen 1:5) = a period of about 2,000 years | `unsupported` |
| A2 | TBWTT-2:41 | Gen 3:21 is "une phrase à peu près intacte du document originel" | `not_checkable` |
| A3a | TBWTT-2:60 | Gen 7:17 says the ark "s’éleva au-dessus de la Terre" | `supported` |
| A3b | TBWTT-2:60 | "… et non pas sur les eaux" | `unsupported` |
| A4 | TBWTT-3:71 (with 3:69-70) | Josh 10:13: "il est dit plus loin qu’elle [la guerre] dura «presque un jour entier»" | `unsupported` |
| A5 | TBWTT-3:192 | Ezek 42:14: they should have written "sains", not "saints" | `unsupported` |
| A6 | TBWTT-3:240 | Ps 8:6: "égal aux Elohim" was what had been dictated | `not_checkable` |
| A7 | TBWTT-4:24 | Matt 5:3: the "sens originel" was "les pauvres, s’ils ont de l’esprit seront heureux" | `unsupported` (against the Greek; not a Hebrew text) |
| A8 | TBWTT-5:66 | "RAËL" means literally "lumière de Dieu" … "messager" | `not_checkable` |
| A9 | TBWTT-5:67 | "Ramuel" means "le fils de celui qui apporte la lumière" | `not_checkable` |

**Totals, List A:** `supported` 1, `unsupported` 5, `contested` 0, `not_checkable` 4 (total 10). Without A7, the one New Testament/Greek item: `supported` 1, `unsupported` 4, `contested` 0, `not_checkable` 4.

**List B — decoding glosses**: a biblical word, usually in guillemets, is said to be "en réalité" or "c’est-à-dire" some other thing. These are identifications of a referent, not claims about Hebrew; I list the ones nearest to a statement of word meaning and give the BDB line, but a lexicon can only say that the gloss is or is not one of its senses. They are **not** in the totals above.

| # | refId | Gloss | BDB headword | Class (lexical sense only) |
|---|---|---|---|---|
| B1 | TBWTT-2:5 | "créé" = "découvert en réalité" | בָּרָא | `unsupported` |
| B2 | TBWTT-2:39 | "serpent" = a group of creators | נָחָשׁ | `unsupported` |
| B3 | TBWTT-3:33, 3:193 | "gloire" = flying craft | כָּבוֹד | `unsupported` |
| B4 | TBWTT-3:63 | "trompette" = "un instrument très compliqué" | שׁוֹפָר / יוֹבֵל | `unsupported` |
| B5 | TBWTT-3:74 | "canne" = "tuyau flexible" | מִשְׁעֶנֶת | `unsupported` |
| B6 | TBWTT-3:189 | "chérubins" ~ "enfants" | כְּרוּב | `unsupported` |
| B7 | TBWTT-3:214 | "anges" = "des hommes à eux" | מַלְאָךְ | `supported` (sense 1 "messenger, one sent") |
| B8 | TBWTT-3:254 | "Satan" = "l’opposition" | שָׂטָן | `supported` |
| B9 | TBWTT-3:267, 3:277, 3:279 | "sagesse" = "la science" | חָכְמָה (Proverbs only) | `not_checkable` as stated; see below |

**Totals, List B:** `supported` 2, `unsupported` 6, `contested` 0, `not_checkable` 1 (total 9). Further glosses of the same kind that I did not check individually are listed under "Absent or ambiguous".

No statement in either list was classed `contested`: I consulted one lexicon and no commentaries, so division of opinion could not be established from what I opened.

## Quotations

### List A

**A1 — TBWTT-2:10** (commenting on Gen 1:5, quoted at TBWTT-2:9)
> Le «jour» correspond à la période pendant laquelle votre soleil se lève sous le même signe le jour de l’équinoxe de printemps, soit deux mille ans terrestres environ.

BDB יוֹם (BibleHub, Strong 3117): "noun masculine Genesis 1:5 day"; sense "2 Day as division of time … d. day as defined by evening and morning Genesis 1:5 ,8,13,19,23,31 (all P; …)". The entry also has "6 יוֺם = time ; a. vividly in General sense … time of harvest" and, for the plural, "b. of long time" and "c. plural in specific sense, apparently = year". No sense of a fixed period of about two thousand years, and Gen 1:5 is filed under 2d. → `unsupported`.

**A2 — TBWTT-2:41** (commenting on Gen 3:21, quoted at TBWTT-2:40)
> La Bible a conservé ici une phrase à peu près intacte du document originel.

The "document originel" is not available to compare. → `not_checkable`.

**A3 — TBWTT-2:60** (commenting on Gen 7:17, quoted at TBWTT-2:59 as «(...) l’arche (...) s’éleva au-dessus de la terre»)
> Vous pouvez constater qu’il est bien dit qu’elle s’éleva audessus de la Terre et non pas sur les eaux.

Hebrew, `genesis-woh/chapter-7.json`:
- GEN-WOH-7:17 "וַֽיְהִ֧י הַמַּבּ֛וּל אַרְבָּעִ֥ים י֖וֹם עַל־הָאָ֑רֶץ וַיִּרְבּ֣וּ הַמַּ֗יִם וַיִּשְׂאוּ֙ אֶת־הַתֵּבָ֔ה וַתָּ֖רָם מֵעַ֥ל הָאָֽרֶץ׃"
- GEN-WOH-7:18 "וַיִּגְבְּר֥וּ הַמַּ֛יִם וַיִּרְבּ֥וּ מְאֹ֖ד עַל־הָאָ֑רֶץ וַתֵּ֥לֶךְ הַתֵּבָ֖ה עַל־פְּנֵ֥י הַמָּֽיִם׃"

A3a: "וַתָּרָם מֵעַל הָאָרֶץ" reads as stated. → `supported`.
A3b: the same verse has "וַיִּרְבּוּ הַמַּיִם וַיִּשְׂאוּ אֶת־הַתֵּבָה" (the waters are the subject of "lifted the ark"), and 7:18 has "וַתֵּלֶךְ הַתֵּבָה עַל־פְּנֵי הַמָּיִם". The Hebrew does not read "not on the waters". → `unsupported`.

**A4 — TBWTT-3:69 to 3:71** (Josh 10:13)
> 3:69 Un des passages les plus déformés est celui où il est dit, toujours en Josué, (X-13) :
> 3:70 «Le soleil s’arrêta et la lune stationna, jusqu’à ce que la nation se fût vengée de ses ennemis».
> 3:71 Ce qui veut tout simplement dire que la guerre fut une guerre éclair qui ne dura qu’une journée puisqu’il est dit plus loin qu’elle dura «presque un jour entier». Cette guerre fut si courte par rapport à l’importance du terrain conquis que les hommes crurent que le soleil s’était arrêté...

Hebrew, Josh 10:13 (BibleHub interlinear): "… וַיַּעֲמֹ֤ד הַשֶּׁ֙מֶשׁ֙ בַּחֲצִ֣י הַשָּׁמַ֔יִם וְלֹא־אָ֥ץ לָב֖וֹא כְּי֥וֹם תָּמִֽים׃". The words "כְּיוֹם תָּמִים" are there, but their clause has the sun as subject ("וַיַּעֲמֹד הַשֶּׁמֶשׁ … וְלֹא־אָץ לָבוֹא"), not the war. BDB תָּמִים (Strong 8549): "3 complete, entire , of time: day Joshua 10:13"; BDB יוֹם files Josh 10:13 under "1 day , opposed to night". → `unsupported` (the phrase exists; the Hebrew does not say it of the war's duration). The assertion in 3:69 that the passage is among "les plus déformés" is itself `not_checkable` and is not counted separately.

**A5 — TBWTT-3:192** (commenting on Ezek 42:14, quoted at TBWTT-3:191 as «… car (ces vêtements) sont saints»)
> Ils auraient dû écrire «car ces vêtements sont sains» SAINS. Subtilité incompréhensible pour des primitifs déifiant tout ce qui leur était dit ou montré.

Hebrew, Ezek 42:14 (BibleHub interlinear; first half also confirmed from Sefaria): "… וְשָׁ֞ם יַנִּ֧יחוּ בִגְדֵיהֶ֛ם אֲשֶׁר־יְשָׁרְת֥וּ בָהֶ֖ן כִּֽי־קֹ֣דֶשׁ הֵ֑נָּה …". BDB קֹדֶשׁ (Sefaria "BDB Dictionary", relayed quotations): "apartness, sacredness (opp. חֹל Lv 10:10 + 4 times Ez);" and, in the sense for persons connected with sacred places, "garments of priesthood Ex 28:2, 4 + 7 times Ex, Lv 16:4, 32 Ez 42:14"; sense 6 "of things and persons ceremonially cleansed". The relay reported no sense "healthy/sound/hygienic" in the part of the page it read (the first 100,000 of 235,033 characters, which included the BDB noun entry). BDB קָדוֹשׁ (BibleHub, Strong 6918): "adjective sacred, holy". The saints/sains wordplay exists in French only. → `unsupported`.

**A6 — TBWTT-3:239 to 3:240** (Ps 8:6)
> 3:239 Dans les Psaumes VIII, il est dit en parlant de l’homme : «Tu l’as fait de peu inférieur aux Elohim». (Psaumes, VIII-6)
> 3:240 Les hommes sont presque aussi forts, intellectuellement, que leurs créateurs. Ils n’ont pas osé écrire, ceux qui ont recopié, égal aux Elohim comme cela avait été dicté.

Hebrew, Ps 8:6 (BibleHub interlinear, there numbered 8:5): "וַתְּחַסְּרֵ֣הוּ מְּ֭עַט מֵאֱלֹהִ֑ים וְכָב֖וֹד וְהָדָ֣ר תְּעַטְּרֵֽהוּ׃". BDB חָסֵר (Strong 2637): "Pi`el cause to lack , with accusative of person, … וַתְּחַסְּרֵהוּ מעט מֵאֱלהים Psalm 8:6 and thou didst make him lack little of God". The transmitted Hebrew agrees with the quotation in 3:239 ("de peu inférieur"); the claim that an earlier dictated text read "égal" cannot be tested against the text or a lexicon. → `not_checkable`.

**A7 — TBWTT-4:23 to 4:24** (Matt 5:3)
> 4:23 «Magnifiques les pauvres par l’esprit». (Matthieu, V-3)
> 4:24 Cette phrase fut injustement traduite par: bienheureux sont les pauvres d’esprit. Le sens originel était: «les pauvres, s’ils ont de l’esprit seront heureux». Rien à voir...

Not a Hebrew text; no Hebrew lexicon applies. Greek, MAT-WOH-5:3 (`matthew-woh/chapter-5.json`; identical on BibleHub): "Μακάριοι οἱ πτωχοὶ τῷ πνεύματι, ὅτι αὐτῶν ἐστιν ἡ βασιλεία τῶν οὐρανῶν." The Greek has no conditional clause; "τῷ πνεύματι" is a dative attached to "οἱ πτωχοὶ". No Greek lexicon was consulted. → `unsupported` against the Greek as it reads. If "sens originel" is taken to mean a spoken saying behind the Greek, the item would be `not_checkable`.

**A8 — TBWTT-5:66**
> Vous Claude Vorilhon, vous répandrez la vérité sous votre nom actuel que vous remplacerez progressivement par le nom que vous portez pour nous «RAËL». Ce qui veut dire littéralement «lumière de Dieu» et si l’on fait une traduction plus précise «lumière des Elohim» ou plus exactement «celui qui apporte la lumière des Elohim» ou «Ambassadeur des Elohim» car vous serez bel et bien notre ambassadeur sur la Terre et nous ne débarquerons officiellement que dans votre ambassade. RAËL peut être traduit plus simplement par «messager».

The sentence does not say which language the name is in (TBWTT-7:35, same speaker: "Notre langue officielle se rapproche beaucoup de l’hébreu ancien."). I did not find or look for a BDB headword for the name as a whole. Components checked: BDB אֵל (Strong 410) "god"; BDB אוֹר (Strong 216) "noun masculine … light"; BDB מַלְאָךְ (Strong 4397) "noun masculine messenger". I did not search BDB for an element *ra-* meaning "light". → `not_checkable`.

**A9 — TBWTT-5:67**
> C’est d’ailleurs par télépathie que nous vous avons fait appeler votre Fils Ramuel, ce qui veut dire «le fils de celui qui apporte la lumière», car il est bien le fils de notre messager, de notre ambassadeur.

Same position as A8; no lexicon entry sought for the name as a whole. → `not_checkable`.

### List B

- **B1 — TBWTT-2:5**: "Ils ont «créé», découvert en réalité, la terre et se sont rendus compte qu’elle réunissait tous les éléments nécessaires à la création d’une vie artificielle …" — BDB בָּרָא (Strong 1254): "verb shape, create"; Qal "shape, fashion, create , always of divine activity … 1 object heaven and earth Genesis 1:1"; Pi`el "1 cut down … 2 cut out". No sense "discover". → `unsupported`.
- **B2 — TBWTT-2:39**: "Le «serpent», ce petit groupe de créateurs qui avait voulu apprendre la vérité à Adam et Ève, était condamné par le gouvernement de la planète originelle à vivre sur Terre en exil …" — BDB נָחָשׁ (Strong 5175): "noun masculine Genesis 3:1 serpent"; "d. as crafty tempter Genesis 3:1 ,2,4,13,14". → `unsupported`.
- **B3 — TBWTT-3:33**: "Vous avez là la description de la «gloire», l’engin volant en réalité, des créateurs …"; **TBWTT-3:193**: "Au chapitre XLIII, le grand vaisseau appelé respectueusement «gloire de Dieu» approche :" — BDB כָּבוֹד (Strong 3519): "abundance, honour, glory"; "c. of God , glory , (1) in historic theophanies … P uses יהוה ׳ כ for theophanies of the Exodus … Exodus 24:16,17 … so Ezekiel … Ezekiel 43:2". The only vehicle word in the entry is in the list of things that have splendour ("chariots Isaiah 22:18"). → `unsupported`.
- **B4 — TBWTT-3:63**: "C’est ce qui fut fait grâce à un instrument très compliqué que la Bible nomme «trompette»." — Josh 6:5 Hebrew (BibleHub): "בִּמְשֹׁ֣ךְ בְּקֶ֣רֶן הַיּוֹבֵ֗ל … אֶת־ק֣וֹל הַשּׁוֹפָ֔ר". BDB שׁוֹפָר (Strong 7782): "horn, for blowing … in any case the ׳ שׁ is a curved horn, as of cow or ram"; BDB יוֹבֵל (Strong 3104): "ram, ram's horn, cornet". → `unsupported`.
- **B5 — TBWTT-3:74**: "… pour en extraire l’essentiel qui, au moyen d’un tuyau flexible, une «canne», parvient à les alimenter." — BDB מִשְׁעֶנֶת (BibleHub, under Strong 4938): "noun feminine staff ; — absolute Judges 6:21". → `unsupported`.
- **B6 — TBWTT-3:189**: "… de même qu’en raison de notre petite taille on nous prend pour des enfants, des chérubins..." — BDB כְּרוּב (Strong 3742): "noun masculine cherub … √ dubious"; senses "1 the living chariot of the theophanic God … 2 as the guards of the garden of Eden … 6 Ezekiel describes the cherubim: a. as four living creatures …". A search of the entry for child / boy / infant / young returned nothing. → `unsupported`.
- **B7 — TBWTT-3:214**: "… les créateurs, pour le punir de son manque de foi, ont placé des hommes à eux, des «anges», parmi ces peuples …" — BDB מַלְאָךְ (Strong 4397): "noun masculine messenger … 1 messenger , a. one sent with a message … b. a prophet … c. priest … 2 angel , as messenger of God". → `supported` in the limited sense that the first lexicon sense is a (human) messenger.
- **B8 — TBWTT-3:254**: "… le gouvernement triomphe devant l’opposition : «Satan»." (and 3:249: "Dans Job I, vous avez l’explication de ce qu’était Satan.") — BDB שָׂטָן (Strong 7854): "noun masculine … 1 adversary . 2 Satan … 2 superhuman adversary , ׳ הַשּׂ : a. of Job, one of בְּנֵי אֱלֹהִים Job 1:6". → `supported`.
- **B9 — TBWTT-3:267**: "Quand le temps en sera venu, la «sagesse», la science qui a permis à tout cela d’exister, sera connue de l’homme en temps voulu."; **3:277**: "Cette science qui a permis aux créateurs de créer et permettra aux hommes d’en faire autant :" (introducing Prov 8:22-31); **3:279**: "L’intelligence et la science, c’est grâce à ces deux vertus que les créateurs ont pu créer la «terre ferme» …" — The gloss at 3:267 attaches to a quotation from the Wisdom of Solomon, a book with no Hebrew text in the project library; no Hebrew lexicon applies there. For Proverbs 8, BDB חָכְמָה (Strong 2451): "noun feminine wisdom … 1 skill in war … in technical work … 5 wisdom , ethical and religious … b. the divine wisdom is personified : she was begotten before all things to be the architect and counsellor of God in the creation (Proverbs 8:22-31)". "Science" as such is not a BDB gloss; "skill … in technical work" is. → `not_checkable` as stated (mixed Greek/Hebrew basis; nearest lexicon sense is "skill").

## Absent or ambiguous

- No Yahweh paragraph in the scope, apart from the excluded "Élohim" passages, uses the words "hébreu"/"hébraïque" about a specific word. The only other occurrences are TBWTT-5:21 (Elohim/Eloha, excluded) and TBWTT-7:35 (the speaker's own language).
- The boundary of List A is a judgement. I counted a statement only where the speaker asserts something about meaning or wording beyond re-quoting a verse. Plain restatements of a quoted verse were not listed (for example TBWTT-3:147 "«Ils viennent d’un pays lointain, des confins du ciel». on ne pouvait être plus clair."; TBWTT-3:171 "Il était écrit recto-verso …"), nor were readings of whole sentences introduced by "veut dire" (TBWTT-2:30 on Gen 2:16-17; TBWTT-4:77 on Matt 19:30; TBWTT-4:25-27 on Matt 6:10, where "la vérité est dite littéralement").
- Decoding glosses of the List B type that I did not check against a lexicon: "arbre de la science" = scientific books (2:30); "le mal" = desire for scientific progress (2:57, 2:68); "arche" = "fusée" (2:58, 2:62); "Tour de Babel" = "immense fusée" (2:72); "Anges" = "deux espions" (2:78-79); "buisson" = "fusée" (3:9); manna = "aliment chimique de synthèse" (3:22); Moses' staff = water detector (3:23); "force" of Samson (3:86); "cornes de l’Autel" = levers of a transmitter (3:101); "nuage" = craft in orbit (3:107); seraphim's wings = "réacteurs" (3:145); "roue" = "soucoupe volante", "jante" = habitable part, "yeux" = "hublots", "ailes" (3:163-164); "manger" the scroll (3:169, 3:171); "homme à l’aspect d’airain" = man in a metal suit (3:189); "grand poisson" = "sous-marin" (3:230); "nuages solides" = metal flying craft (3:260); "oiseaux", "épines", "bonne terre" (4:49). These are in the scope and would enlarge List B if counted.
- A3 and A6 each contain two separable assertions. I split A3 (the sentence itself is built as "X et non pas Y") and did not split A6 (the first half merely repeats the quotation). A different convention changes the totals by one.
- A7 concerns a Greek text and A8-A9 concern names the speaker does not assign to a language; whether they belong under "Hebrew or biblical word, name or title" is open.
- BDB קֹדֶשׁ was read only through a relaying fetch tool that returned short quotations and a summary; I did not see the page myself. BibleHub's page for Strong 6944 carries no BDB section.
- Psalm verse numbers: BibleHub uses English numbering (Ps 8:5, 19:4) for the verses the book cites by Hebrew numbering (8:6, 19:5).
- HALOT was not consulted; no commentary was consulted.

## Adjacent observations

- General statements by the same speaker about the state of the biblical text, not tied to a word or verse: TBWTT-2:2 "… la Bible, où vous pourrez retrouver les traces de la vérité qui ont bien sûr été un peu déformées par les copistes …"; TBWTT-2:3 "Seules les parties de la Bible que je vais vous traduire sont importantes. … grâce à la loi qui disait qu’il fallait recopier la Bible sans rien en changer, même pas le plus petit signe, le sens profond est resté même si le texte s’est chargé de phrases mystiques et inutiles au fil des millénaires."; TBWTT-4:117 "Vous saurez vous-même les traduire …". The verb "traduire" is used here of the speaker's explanations.
- TBWTT-3:243-245 quotes Ps 19:5 as "«Pour le soleil, il a dressé une tente sur la mer (...)»" and comments "Nouvelle allusion à l’amas de terre qui fut créé quand l’océan recouvrait la Terre". The Hebrew as shown on BibleHub reads "לַ֝שֶּׁ֗מֶשׁ שָֽׂם־אֹ֥הֶל בָּהֶֽם׃" (last word "בָּהֶם", glossed there "in them"); the word for "sea" is not in that text. The speaker makes no claim about the wording, so this is not in List A, but the comment rests on the words "sur la mer". Which French Bible supplied the quotation is not stated in the chapter files.
- TBWTT-3:241-242 quotes Ps 19:7 with the word "orbite" and comments on "l’orbite terrestre"; I did not check the Hebrew of that verse.
- TBWTT-3:288 gives meanings for two symbols rather than words: "l’étoile de David qui veut dire : «Il en est en haut comme il en est en bas» et en son centre le «svastika» qui veut dire que tout est cyclique". TBWTT-3:305, tagged speaker `Yahweh`, reads as an editorial caption ("Symbole que Raël a vu représenté sur la soucoupe volante en 1973. …") and refers to Raël in the third person; the speaker tag there looks wrong.
- TBWTT-6:7 says "Vous naissez égaux, cela aussi est dans les écrits bibliques" and "Ce monde n’est pas à vous, cela aussi est écrit dans la Bible"; the only passage then quoted is Lev 25:8, 14-16, 23 (TBWTT-6:11-13), ending "car la terre est à moi, tandis que vous êtes des hôtes et des résidants chez moi". No verse is given for "Vous naissez égaux". I did not check the Hebrew of Lev 25.
- TBWTT-3:2 carries the sentence "Dans la Genèse, XXVIII, se trouve une autre description de notre présence." under speaker `Narrator`, although "notre présence" is the visitor's voice; it contains no lexical statement.
- The quotations throughout use the forms "Iahvé", "Elohim", "Adonaï", "Shaddaï" inside the French Bible text itself, so the retention of "Elohim" in quotations belongs to the Bible translation being read from, not only to the speaker's commentary.
- TBWTT-2:69/2:70, 3:5/3:6, 3:16/3:17 and similar pairs are single sentences split across two paragraphs in the digitization; refIds for quotations near them may be off by one against a print edition.
