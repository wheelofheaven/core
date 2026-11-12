---
title: "Canon close reading: biblical quotations against the original languages"
status: draft
version: 0.1.0
last_reviewed: 2026-11-12
---

# hebrew-audit — the canon's scripture quotations against the Hebrew, Aramaic and Greek

## Exact question

For each biblical passage the canon quotes and then reads technologically or historically, does the reading rest on (a) what the Hebrew/Aramaic/Greek text itself says, (b) a feature of the French translation the canon quotes, or (c) neither — an interpretation added to a neutral wording?

## Method

- **Inventory.** Every scripture citation in TBWTT, ETTMTTP and LWTE that the site's citation index resolves (`www.wheelofheaven.world/data/canon_citations/*.json`: 274 citations in 258 paragraphs), plus a manual sweep of the three French dumps for quotations, paraphrases and word-meaning statements with no parenthetical reference. Result: **321 register items** (TBWTT 2: 43 · TBWTT 3:3–141: 65 · TBWTT 3:144–304: 78 · TBWTT 4–7 + ETTMTTP: 75 · LWTE: 60).
- **Original-language text.** The standalone `data-library` clone is stale (Hebrew/Greek for ~110 chapters only). The audit used the fuller copy at `www.wheelofheaven.world/data/library/<book>-woh/chapter-N.json`, which holds every chapter the canon cites (the "canon-cited" programme, signed off 2026-11-01); refIds are identical where both exist. Isaiah refIds have the form `ISA-<c>:<v>`; all others `<BOOK>-WOH-<c>:<v>`. Nothing in any repo was modified.
- **Comparison.** For each item: the canon's French (verbatim), the load-bearing words in the original (exact substrings of the library `text`), what each `(...)` or silent truncation removed, and a classification. The work was split into five slices read in full; the merged register is machine-checked: every French string is a substring of the stated canon paragraph and every Hebrew/Aramaic/Greek string a substring of the stated library verse (`agent-hebrew-audit/check_frag.py`: 321 items, 0 failures).
- **Classification.** `hebrew-supported` = the load-bearing wording is in the original (also used for Aramaic/Greek); the identification — craft, ray, suit, base — is usually still the canon's. `translation-dependent` = the hook exists only in the French the canon prints. `interpretive-addition` = wording neutral in both. `contradicted-by-original` = the original, usually in the words the quotation cut or the next verse, says something incompatible with the hook. `no-reading` = quoted for moral or prophetic use. `direction` records whether the original is more or less favourable to the reading than the French quoted.
- **What was not done.** Dhorme's Pléiade text was not available beyond the Genesis 1–3 extract core already holds, so "translation-dependent" means *dependent on the French the canon prints*; whether that French is Dhorme's or an alteration is open in every case (see Limitations). Lexical glosses are the auditors' own reading of the library text and notes; statements about scholarship or other French Bibles are flagged per item in the JSON as `[outside knowledge — unverified, needs source]`.

## Headline numbers

| Classification | n |
|---|---|
| hebrew-supported | 138 |
| interpretive-addition | 116 |
| translation-dependent | 30 |
| contradicted-by-original | 20 |
| no-reading | 13 |
| not-checkable | 4 |

Direction: neutral 179 · original less favourable 92 · original more favourable 50.
Ellipsis or silent truncation present in 203 items; it changes the sense in **83**. References: ok 294 · partial 25 · wrong 2. An existing library verse note already makes the item's main observation in 165 of 321.

Answer to the question in one paragraph (analysis): the French the canon prints is, for the most part, a literal rendering, so the translation is rarely the lever — 30 of 321 readings hang on a French word. In 138 the textual hook is really in the original and in 116 the wording is neutral and the reading is supplied. The lever that matters most is **selection**: 83 quotations are cut in a way that changes the sense, and most of the 20 contradicted cases are contradicted by the words under a `(...)` or by the adjacent verse, not by a mistranslation.

## Findings (ranked)

### 1. The ellipsis, not the translation, is the main lever (new)

TBWTT prints `(...)` 193 times; ETTMTTP never; LWTE once. In 83 register items the cut changes the sense. The strongest cases are those where the removed words are the text's own mechanism or identification, and the canon's reading occupies exactly that slot.

**A-030** — TBWTT-2:59 (Genèse, VII-17) → Gen 7:17 (first and last words only) · `contradicted-by-original` · original-less-favourable

QUOTE[TBWTT-2:59]: (...) l’arche (...) s’éleva au-dessus de la terre ENDQUOTE
QUOTE[TBWTT-2:60]: Vous pouvez constater qu’il est bien dit qu’elle s’éleva audessus de la Terre et non pas sur les eaux ENDQUOTE

- «s’éleva au-dessus de la terre» ↔ `וַתָּ֖רָם מֵעַ֥ל הָאָֽרֶץ` (GEN-WOH-7:17) — 'and it rose up from upon / above the earth'
- «(...)» ↔ `וַיִּרְבּ֣וּ הַמַּ֗יִם וַיִּשְׂאוּ֙ אֶת־הַתֵּבָ֔ה` (GEN-WOH-7:17) — 'and the waters increased and LIFTED the tēbâ' — the words under the canon's second (...); verb 3rd PLURAL with 'waters' as subject
- «non pas sur les eaux» ↔ `וַתֵּ֥לֶךְ הַתֵּבָ֖ה עַל־פְּנֵ֥י הַמָּֽיִם` (GEN-WOH-7:18) — 'and the tēbâ went upon the face of the waters' (next verse, not quoted)
- Cut: (1) 'The deluge was forty days on the earth; the waters increased and lifted' before 'l’arche'; (2) nothing substantive after it — the quotation is 'l’arche … s’éleva au-dessus de la terre' with 'les eaux … soulevèrent' removed from in front. **(changes sense)**

The quoted words are really there (wattārom mēʿal hāʾāreṣ), so the phrase is not a translation artefact. But the canon's explicit textual argument — that the verse says the ark rose above the earth 'and not on the waters' — is contradicted by the same verse in Hebrew ('the waters increased and lifted the ark', the clause replaced by '(...)') and by the next verse ('the ark went on the face of the waters'). This is the one place in the Genesis sequence where the canon makes a claim about what the wording says and the full wording says the opposite.

**B-006** — TBWTT-3:16 (Exode, XIV-21) → Exod 14:21b · `contradicted-by-original` · original-less-favourable

QUOTE[TBWTT-3:16]: «(...) il mit ainsi la mer à sec et les eaux se fendirent» ENDQUOTE
QUOTE[TBWTT-3:15]: Ensuite la traversée de l'eau est obtenue grâce à un rayon répulseur qui permet de dégager un passage. ENDQUOTE

- «il mit ainsi la mer à sec» ↔ `וַיָּ֥שֶׂם אֶת־הַיָּ֖ם לֶחָרָבָ֑ה` (EXO-WOH-14:21) — and he made the sea into dry land
- «les eaux se fendirent» ↔ `וַיִּבָּקְע֖וּ הַמָּֽיִם׃` (EXO-WOH-14:21) — and the waters were split (Niphal)
- (not quoted by the canon) `וַיּ֣וֹלֶךְ יְהוָ֣ה ׀ אֶת־הַ֠יָּם בְּר֨וּחַ קָדִ֤ים עַזָּה֙ כָּל־הַלַּ֔יְלָה` (EXO-WOH-14:21) — and YHWH made the sea go by a strong east wind all the night
- (not quoted by the canon) `וַיֵּ֨ט מֹשֶׁ֣ה אֶת־יָדוֹ֮ עַל־הַיָּם֒` (EXO-WOH-14:21) — and Moses stretched out his hand over the sea
- Cut: The '(...)' removes 14:21a: Moses stretching out his hand, and 'YHWH drove the sea back by a strong east wind all night'. **(changes sense)**

The splitting and drying are in the Hebrew as quoted, but the instrument is named in the half-verse the canon elides: a strong east wind working all night. A 'repulsor ray' is therefore not an addition to neutral wording; it replaces a stated cause that the quotation has removed. The same holds for the French: Dhorme-type French also has the wind, so this is a selection effect, not a translation effect. v 22 ('the waters were a wall for them on their right and on their left') is the detail most compatible with a held-open passage and is not quoted.

**C-043** — TBWTT-3:216 none → Dan 10:13 (unreferenced) · `contradicted-by-original` · original-less-favourable

QUOTE[TBWTT-3:216]: «Michaël (...) est venu (...) là, auprès des rois de Perse». ENDQUOTE
QUOTE[TBWTT-3:214]: les créateurs, pour le punir de son manque de foi, ont placé des hommes à eux, des «anges», parmi ces peuples, afin de leur faire accomplir des progrès techniques ENDQUOTE
QUOTE[TBWTT-3:215]: L’ange Michaël était le chef de la délégation chargée d’aider les Perses ENDQUOTE

- «Michaël (...) est venu» ↔ `מִֽיכָאֵ֗ל אַחַ֛ד הַשָּׂרִ֥ים הָרִאשֹׁנִ֖ים בָּ֣א לְעָזְרֵ֑נִי` (DAN-WOH-10:13) — Michael, one of the chief princes, came to help me
- «là, auprès des rois de Perse» ↔ `וַאֲנִי֙ נוֹתַ֣רְתִּי שָׁ֔ם אֵ֖צֶל מַלְכֵ֥י פָרָֽס׃` (DAN-WOH-10:13) — and I was left there beside the kings of Persia
- «chargée d’aider les Perses» ↔ `וְשַׂ֣ר ׀ מַלְכ֣וּת פָּרַ֗ס עֹמֵ֤ד לְנֶגְדִּי֙` (DAN-WOH-10:13) — and the prince of the kingdom of Persia was standing against me
- «L’ange Michaël» ↔ `מִיכָאֵ֥ל שַׂרְכֶֽם׃` (DAN-WOH-10:21) — Michael your prince
- Cut: Two "(...)" inside one verse: "one of the chief princes"; "to help me; and I remained". Also the verse opening "the prince of the kingdom of Persia withstood me twenty-one days". **(changes sense)**

This is the clearest case in the slice of an ellipsis producing the reading. In Hebrew, Persia has its own śar who opposes the speaker; Michael, "one of the chief princes", comes to help the speaker against him; and it is the speaker who is then "left there beside the kings of Persia". Michael is explicitly Israel's prince (10:21 "your prince"; 12:1). The canon's spliced sentence puts Michael beside the kings of Persia and its commentary makes him the helper of the Persians — the opposite alignment. The Hebrew does support a general idea the canon uses (nations each have a non-human śar), but with Michael on Israel's side. No reference is printed for this quotation.

**B-024** — TBWTT-3:49 (Nombres, XVIII-13) → Num 18:13a · `contradicted-by-original` · original-less-favourable

QUOTE[TBWTT-3:49]: «Les primeurs de tout ce qui sera en leur pays et qu'ils apporteront à Iahvé» ENDQUOTE
QUOTE[TBWTT-3:48]: les créateurs préféraient les fruits et légumes frais ENDQUOTE

- «Les primeurs de tout ce qui sera en leur pays» ↔ `בִּכּוּרֵ֞י כָּל־אֲשֶׁ֧ר בְּאַרְצָ֛ם` (NUM-WOH-18:13) — the first-ripe produce of all that is in their land
- «qu'ils apporteront à Iahvé» ↔ `אֲשֶׁר־יָבִ֥יאוּ לַיהוָ֖ה` (NUM-WOH-18:13) — which they bring to YHWH
- (not quoted by the canon) `לְךָ֣ יִהְיֶ֑ה` (NUM-WOH-18:13) — shall be yours (2 m.sg. — Aaron)
- (not quoted by the canon) `כָּל־טָה֥וֹר בְּבֵיתְךָ֖ יֹאכֲלֶֽנּוּ׃` (NUM-WOH-18:13) — every clean person in your house shall eat it
- Cut: Silent truncation (no '(...)'): the quotation ends before the predicate 'shall be yours; everyone who is clean in your house shall eat of it'. **(changes sense)**

The quoted words are accurate but form only the subject of the Hebrew sentence. Its predicate assigns the first-fruits to Aaron ('ləḵā yihyeh') and has his household eat them. The verse therefore says the opposite of what it is cited for: the fresh produce 'brought to YHWH' is consumed by the human priesthood. The effect comes from the truncation, not from the French.

**E-016** — LWTE-2:122 (Apocalypse, I, 17 à 19.) → Rev 1:17-19 · `hebrew-supported` · neutral

QUOTE[LWTE-2:122]: Ecris donc ce que tu as vu, ce qui est et ce qui va être après, (…) ENDQUOTE
QUOTE[LWTE-2:123]: Nous lui avons dit que nous étions le «premier et le dernier», c'est-àdire les premiers sur la Terre, et les derniers si les hommes s'auto-détruisent ENDQUOTE
QUOTE[LWTE-2:123]: celui qui leur parlait avait connu la mort et qu'il avait été recréé, grâce au processus expliqué dans le premier message et qui nous permet de vivre éternellement à travers plusieurs corps ENDQUOTE

- «je suis le premier et le dernier» ↔ `ἐγώ εἰμι ὁ πρῶτος καὶ ὁ ἔσχατος` (REV-WOH-1:17) — I am the first and the last
- «J'ai été mort et voici, je suis vivant dans les âges des âges» ↔ `ἐγενόμην νεκρὸς καὶ ἰδοὺ ζῶν εἰμι εἰς τοὺς αἰῶνας τῶν αἰώνων` (REV-WOH-1:18) — I became dead and behold I am living unto the ages of the ages
- «ce qui va être après, (…)» ↔ `οἱ ἑπτὰ ἀστέρες ἄγγελοι τῶν ἑπτὰ ἐκκλησιῶν εἰσιν, καὶ αἱ λυχνίαι αἱ ἑπτὰ ἑπτὰ ἐκκλησίαι εἰσίν` (REV-WOH-1:20) — the seven stars are the angels/messengers of the seven assemblies, and the seven lampstands are seven assemblies
- Cut: Rev 1:20 (the mystery of the seven stars and lampstands explained as the angels of the seven churches and the seven churches); then all of chapters 2-3 (the seven letters) before the next quotation at 4:1 **(changes sense)**

'Was dead and am alive for ever' is literally what the Greek says, so the re-creation reading has a real hook; 'first and last' is singular in Greek and pluralised only in the commentary. The ellipsis is the important feature: v.19 is quoted in full, so the printed (…) covers what follows — 1:20, the vision's own explanation of the seven stars and seven lampstands as the 'angels' (angeloi) of seven assemblies and the assemblies themselves. That in-text key is incompatible with stars = indicator lights and lampstands = craft, and it is the verse left out. (An ἄγγελοι/'messengers' reading of 1:20 would have been available to the canon and is not used.)

**D-057** — TBWTT-5:28 (Isaïe, XLIII, 10, 12-13) → Isa 43:10, 12-13 · `translation-dependent` · original-less-favourable

QUOTE[TBWTT-5:28]: «Vous êtes mes témoins ! oracle de Iahvé, et vous êtes mon serviteur que j’ai élu, afin que vous sachiez, que vous croyiez en moi et que vous compreniez que je suis le même (...). Quant à vous, vous êtes mes témoins, oracle de Iahvé, et moi je suis Dieu : aujourd’hui aussi je suis le même». ENDQUOTE
QUOTE[TBWTT-5:29]: «Vous êtes mes témoins», c’est explicite non ? Et je peux vous redire en ce jour : «aujourd’hui je suis le même» grâce au témoignage que vous avez en main avec la Bible. ENDQUOTE

- «aujourd’hui aussi je suis le même» ↔ `גַּם־מִיּוֹם֙ אֲנִ֣י ה֔וּא` (ISA-43:13) — also from (the) day, I (am) he
- «que je suis le même» ↔ `כִּֽי־אֲנִ֣י ה֔וּא` (ISA-43:10) — that I (am) he
- «(...)» ↔ `לְפָנַי֙ לֹא־נ֣וֹצַר אֵ֔ל וְאַחֲרַ֖י לֹ֥א יִהְיֶֽה` (ISA-43:10) — before me no god (ʾēl) was formed, and after me there shall be none
- «(...)» ↔ `אָנֹכִ֥י אָנֹכִ֖י יְהוָ֑ה וְאֵ֥ין מִבַּלְעָדַ֖י מוֹשִֽׁיעַ` (ISA-43:11) — I, I am YHWH, and apart from me there is no saviour
- «et moi je suis Dieu» ↔ `וַֽאֲנִי־אֵֽל` (ISA-43:12) — and I am El/God (singular)
- Cut: 43:10b ('before me no god was formed, nor shall there be after me'), 43:11 ('I, I am YHWH, and besides me there is no saviour') and 43:12a. **(changes sense)**

Two findings. (1) The phrase the canon re-utters 'on this day' depends on the French « aujourd'hui »; the Hebrew מִיּוֹם is 'from (the) day', temporally ambiguous (since/henceforth), and is not the word for 'today'. (2) The ellipsis removes 43:10b–11, where the speaker says no god was formed before him and none will be after, and that there is no saviour but him — wording that sits badly with a plural-creators reading and with a speaker who is one of a council; the retained « moi je suis Dieu » translates singular ʾēl. The 'witnesses' hook itself (ʾattem ʿēḏay) is sound.

Three further patterns of the same kind, each recurring:

- **Ezekiel's journeys lose "in visions of Elohim" every time** (C-024 Ezek 8:3; C-028 Ezek 11:24; C-031 Ezek 40:2; C-029 Ezek 37:1 loses "by the rûaḥ of YHWH").

**C-024** — TBWTT-3:175 (Ezéchiel, VIII-3) → Ezek 8:3 (middle) · `hebrew-supported` · original-less-favourable

QUOTE[TBWTT-3:175]: «(...) l’esprit me souleva entre ciel et terre et m’amena à ENDQUOTE
QUOTE[TBWTT-3:174]: Plus loin, le «prophète» est encore emmené dans un engin volant ENDQUOTE

- «l’esprit me souleva entre ciel et terre» ↔ `וַתִּשָּׂ֣א אֹתִ֣י ר֣וּחַ ׀ בֵּֽין־הָאָ֣רֶץ וּבֵ֣ין הַשָּׁמַ֡יִם` (EZK-WOH-8:3) — and (a) rûaḥ lifted me between the earth and the skies
- «m’amena à» ↔ `וַתָּבֵא֩ אֹתִ֨י יְרוּשָׁלְַ֜מָה בְּמַרְא֣וֹת אֱלֹהִ֗ים` (EZK-WOH-8:3) — and brought me to Jerusalem in visions of Elohim
- Cut: Before: "He stretched out the form of a hand and took me by a lock of my head" (וַיִּקָּחֵנִי בְּצִיצִת רֹאשִׁי). After: "in visions of Elohim, to the entrance of the gate ...". **(changes sense)**

- **The serpent's animal class is cut twice** (A-015 Gen 3:1 at TBWTT-2:34; A-017 Gen 3:14 at TBWTT-2:38), and the Hebrew serpent is one individual addressed in the second person singular.
- **Self-interpretations are skipped**: Ezek 37:11 "these bones are the whole house of Israel" (C-030, D-071); Rev 1:20 (E-016 above); Matt 13:18–23, the Gospel's own decoding of the sower (D-017); Zech 5:3, the flying scroll explained as a curse (C-051); Ezek 2:10b, the scroll's content "laments, mourning and woe" (C-021).

### 2. Where the original is MORE favourable to the reading than the French the canon quotes


**B-041** — TBWTT-3:93 (I Samuel, XVII-26) → 1 Sam 17:26b · `hebrew-supported` · original-more-favourable

QUOTE[TBWTT-3:93]: «Qui (...) insulte les troupes du Dieu vivant ?» ENDQUOTE
QUOTE[TBWTT-3:94]: Ce qui montre bien la réalité de la présence à cette époque d'un «Dieu» tout à fait palpable... ENDQUOTE

- «les troupes» ↔ `מַעַרְכ֖וֹת` (1SA-WOH-17:26) — battle-lines, ranks
- «du Dieu vivant» ↔ `אֱלֹהִ֥ים חַיִּֽים׃` (1SA-WOH-17:26) — living Elohim — ḥayyîm is a masculine PLURAL adjective agreeing with ʾĕlōhîm
- Cut: The '(...)' removes 'is this uncircumcised Philistine, that he should'; the first half of the verse (David's question about the reward) is not quoted.

The reading rests on the adjective 'living', which is Hebrew (ḥayyîm). The original is more favourable to the canon's wider thesis than the French it quotes, on a point the canon does not notice: the adjective is plural (ʾĕlōhîm ḥayyîm), one of the minority of cases where Elohim is construed with a plural modifier, and the French singular 'Dieu vivant' erases it. (Core claim 0009 lists the parallel Deut 5:26 among the plural-adjective cases; this verse has the same phrase.) 'Palpable' is an inference from 'living'; the phrase is a fixed epithet.

**E-003** — LWTE-1:69 (Genèse, IX, 4 et 5.) → Gen 9:4-5 · `hebrew-supported` · original-more-favourable

QUOTE[LWTE-1:69]: Vous ne mangerez point la chair avec son âme, c'es-à-dire son sang. Pour ce qui est de votre sang je le réclamerai comme vos âmes: je le réclamerai de la main de tout animal je réclamerai l'âme de l'homme de la main de l'homme, de la main d’un chacun l'âme de son frère. ENDQUOTE
QUOTE[LWTE-1:69]: Même la Bible dit très clairement que chaque être vivant possède une «âme » et pas seulement les hommes ENDQUOTE
QUOTE[LWTE-1:69]: Donc il n'y a pas d'âme éthérée s'envolant gentiment du corps après la mort, mais il y a le code génétique qui est la personnalité de chacun. ENDQUOTE

- «la chair avec son âme, c'es-à-dire son sang» ↔ `בָּשָׂ֕ר בְּנַפְשׁ֥וֹ דָמ֖וֹ` (GEN-WOH-9:4) — flesh with/in its nep̄eš, its blood
- «comme vos âmes» ↔ `לְנַפְשֹֽׁתֵיכֶם֙` (GEN-WOH-9:5) — for/belonging to your lives
- «l'âme de l'homme» ↔ `אֶת־נֶ֥פֶשׁ הָֽאָדָֽם` (GEN-WOH-9:5) — the nep̄eš (life) of the human

The textual hook is real and is Hebrew, not French: the same noun nep̄eš is predicated of animal flesh (9:4) and of the human (9:5) and is tied to blood. The Hebrew is in fact more favourable than the French word the canon has to work with: 'âme' carries the Latin/Christian sense of an immaterial soul that Raël must then argue away, whereas nep̄eš in these verses simply is the creature's life, with no separable-soul connotation (library: 'the blood IS the nefesh, the carrier of the life-force'). What the Hebrew does not supply is the step from blood-life to 'code génétique' and to re-creation; that identification is an interpretive addition. The existing library note sits at Lev 17:11 and records only that 'soul' and 'life' render the same word.

**C-064** — TBWTT-3:259 (Job, XXXVII-18) → Job 37:18 · `hebrew-supported` · original-more-favourable

QUOTE[TBWTT-3:259]: «(...) étendras-tu, avec lui, des nuages, solides comme un miroir de métal fondu ?». ENDQUOTE
QUOTE[TBWTT-3:260]: Est-ce que l’homme est capable de faire des «nuages solides», des engins volants métalliques en réalité ENDQUOTE

- «étendras-tu» ↔ `תַּרְקִ֣יעַ` (JOB-WOH-37:18) — will you beat out / hammer flat (hiphil of rqʿ)
- «des nuages» ↔ `לִשְׁחָקִ֑ים` (JOB-WOH-37:18) — the šәḥāqîm: clouds / the skies (poetic plural)
- «solides comme un miroir de métal fondu» ↔ `חֲ֝זָקִ֗ים כִּרְאִ֥י מוּצָֽק׃` (JOB-WOH-37:18) — strong/hard as a cast mirror
- «avec lui» ↔ `עִ֭מּוֹ` (JOB-WOH-37:18) — with him
- Cut: The opening "(...)" covers nothing of v.18 (the verse begins with the verb); it stands for the preceding context.

The metallic hook is stronger in Hebrew than in the French the canon quotes: the verb is rqʿ, "to hammer out (metal)", and the comparison is to a cast-metal mirror, hard (ḥăzāqîm). What the Hebrew leaves open is the object: šәḥāqîm is "clouds" (canon's French, library line) or "the skies" (canon's English), and with the latter the verse is the standard picture of a solid sky-vault spread by God, not of discrete objects. The plural indefinite "des nuages" (some clouds = craft) is a French reading of a Hebrew definite poetic plural (lišḥāqîm, with article).

**A-038** — TBWTT-2:79 (Genèse, XIX-1) → Gen 19:1a · `hebrew-supported` · original-more-favourable

QUOTE[TBWTT-2:79]: Les deux Anges arrivèrent le soir à Sodome ENDQUOTE
QUOTE[TBWTT-2:78]: Les créateurs envoyèrent deux espions pour voir ce qui se préparait ENDQUOTE

- «Les deux Anges» ↔ `שְׁנֵ֨י הַמַּלְאָכִ֤ים` (GEN-WOH-19:1) — 'the two messengers/envoys' — malʾāk = one sent on a mission
- «arrivèrent» ↔ `וַ֠יָּבֹאוּ` (GEN-WOH-19:1) — 'and they came' (3rd pl.)
- Cut: Rest of v.1 (Lot at the gate, rising, bowing).

The Hebrew malʾākîm means 'those sent' — agents on a mission — which is closer to the canon's 'envoyèrent deux espions' than the French 'Anges' it quotes. The same two are called simply 'the men' in the narrative (הָֽאֲנָשִׁים֙, GEN-WOH-19:10 and 19:16). 'Spies' specifically is the canon's inference (a fact-finding purpose).

**C-061** — TBWTT-3:250 (Job, I-6) → Job 1:6 · `hebrew-supported` · original-more-favourable

QUOTE[TBWTT-3:250]: «Il advint un jour que les fils d’Elohim vinrent se présenter devant Iahvé et Satan vint aussi parmi eux». ENDQUOTE
QUOTE[TBWTT-3:251]: Elohim, cela veut dire littéralement «venus du ciel» en Hébreu. Les fils d’Elohim, donc les créateurs qui surveillent les hommes, font régulièrement des rapports sur leur planète d’origine ENDQUOTE
QUOTE[TBWTT-3:251]: Mais l’un d’entre eux nommé Satan, fait partie de ceux qui ont toujours condamné la création d’autres êtres intelligents ENDQUOTE

- «les fils d’Elohim» ↔ `בְּנֵ֣י הָאֱלֹהִ֔ים` (JOB-WOH-1:6) — the sons of THE Elohim (with article)
- «Satan vint aussi parmi eux» ↔ `וַיָּב֥וֹא גַֽם־הַשָּׂטָ֖ן בְּתוֹכָֽם׃` (JOB-WOH-1:6) — and the adversary also came in their midst
- «se présenter devant Iahvé» ↔ `לְהִתְיַצֵּ֖ב עַל־יְהוָ֑ה` (JOB-WOH-1:6) — to station themselves before/over-against YHWH
- «les créateurs qui surveillent les hommes» ↔ `מִשּׁ֣וּט בָּאָ֔רֶץ וּמֵֽהִתְהַלֵּ֖ךְ בָּֽהּ׃` (JOB-WOH-1:7) — from roaming on the earth and walking about on it

The scene the canon describes — a plurality of beings of the Elohim class reporting to a presiding YHWH, with an opposition figure among them — is the plain narrative of the Hebrew. Two details of the original are more favourable than the French: the article in bәnê hāʾĕlōhîm (a definite body, "the Elohim") and the article in haśśāṭān (an office, "the adversary", which is the canon's own "l'opposition"); a third, the adversary's roving inspection of the earth (v.7), is unquoted. Less favourable: haśśāṭān is not a name ("nommé Satan"), and the gloss "venus du ciel" is not a lexical meaning of ʾĕlōhîm (core woh-claim-0009). YHWH here is one individual distinct from the sons of the Elohim; "the government" is the canon's reading.

**B-005** — TBWTT-3:13 (Exode, XIV-19) → Exod 14:19b–20 · `hebrew-supported` · original-more-favourable

QUOTE[TBWTT-3:13]: «La colonne de nuée se déplaça de devant eux et se tint derrière eux (...) la nuée était (pour les uns) ténèbres, et (pour les autres) elle éclairait la nuit» ENDQUOTE
QUOTE[TBWTT-3:14]: La fumée émise derrière le peuple d'Israël faisait un rideau qui ralentissait les poursuivants. ENDQUOTE

- «La colonne de nuée se déplaça de devant eux et se tint derrière eux» ↔ `וַיִּסַּ֞ע עַמּ֤וּד הֶֽעָנָן֙ מִפְּנֵיהֶ֔ם וַיַּֽעֲמֹ֖ד מֵאַחֲרֵיהֶֽם׃` (EXO-WOH-14:19) — and the pillar of cloud set out from before them and stood behind them
- (not quoted by the canon) `וַיִּסַּ֞ע מַלְאַ֣ךְ הָאֱלֹהִ֗ים` (EXO-WOH-14:19) — and the messenger of the Elohim set out
- «la nuée était (pour les uns) ténèbres, et (pour les autres) elle éclairait la nuit» ↔ `וַיְהִ֤י הֶֽעָנָן֙ וְהַחֹ֔שֶׁךְ וַיָּ֖אֶר אֶת־הַלָּ֑יְלָה` (EXO-WOH-14:20) — and there was the cloud and the darkness, and it lit up the night
- (not quoted by the canon) `וַיָּבֹ֞א בֵּ֣ין ׀ מַחֲנֵ֣ה מִצְרַ֗יִם וּבֵין֙ מַחֲנֵ֣ה יִשְׂרָאֵ֔ל` (EXO-WOH-14:20) — and it came between the camp of Egypt and the camp of Israel
- (not quoted by the canon) `וְלֹא־קָרַ֥ב זֶ֛ה אֶל־זֶ֖ה כָּל־הַלָּֽיְלָה׃` (EXO-WOH-14:20) — and the one did not come near the other all night
- Cut: (1) 14:19a 'the messenger of the Elohim who went before the camp of Israel moved and went behind them' is not quoted (silently). (2) The '(...)' removes 14:20a 'it came between the camp of Egypt and the camp of Israel'. (3) The quotation stops before 'and the one did not come near the other all night'. **(changes sense)**

The screen function is stated more explicitly in the uncited Hebrew than in the excerpt the canon prints: the column 'came between' the two camps and 'the one did not come near the other all night'. 14:19a also pairs the column with a named agent, malʾaḵ hāʾĕlōhîm (articular Elohim), who relocates with it. Against the reading: the noun is ʿānān 'cloud', not smoke, and nothing is 'emitted'; and the bracketed 'for some … for others' is a translator's supplement to a difficult clause, not Hebrew.

**B-017** — TBWTT-3:36 chapitre XXVI de l'Exode (prose reference, no quotation) → Exod 26 (tabernacle instructions); the governing statement is Exod 25:8–9 · `hebrew-supported` · original-more-favourable

QUOTE[TBWTT-3:36]: Ils avaient également décidé de s'installer plus confortablement et demandèrent aux hommes de leur confectionner une résidence suivant leurs plans. ENDQUOTE
QUOTE[TBWTT-3:36]: Dans cette résidence ils devaient rencontrer les représentants des hommes : c'est la tente du rendez-vous où les hommes apportaient nourriture et présents en gage de soumission. ENDQUOTE

- «une résidence» ↔ `הַמִּשְׁכָּ֔ן` (EXO-WOH-25:9) — the dwelling-place (from šāḵan 'dwell')
- (not quoted by the canon) `וְשָׁכַנְתִּ֖י בְּתוֹכָֽם׃` (EXO-WOH-25:8) — and I will dwell in their midst
- «suivant leurs plans» ↔ `תַּבְנִ֣ית הַמִּשְׁכָּ֔ן` (EXO-WOH-25:9) — the pattern/model of the dwelling

This is a case where the canon cites a chapter without quoting and the unquoted Hebrew is closer to its reading than any French it prints: the structure is called miškān 'dwelling', its purpose is 'that I may dwell (wəšāḵantî) in their midst', and it is to be made after a taḇnîṯ 'plan/model' shown to Moses. The speaker and the dweller are singular ('I'); the canon's plural 'ils' is its own. 'More comfortably' and 'in token of submission' are additions.

Shorter entries of the same direction (details in the register): Gen 3:5 «comme des dieux» is "like Elohim", the makers' own name (A-015); Gen 22:1, unquoted, says "the Elohim tested Abraham" (A-043); Gen 11:6 is a statement of fact where the canon's French is conditional (A-036); Josh 5:13 introduces the commander as "a man" (B-029); 1 Kgs 17:4 "I have commanded the ravens" (B-051); 2 Kgs 1:12 "fire of Elohim" (B-059); Ezek 3:13 gives the rumbling to "the wheels" (C-023); Zech 4:10 ties the seven eyes to the seven lamps of 4:2 (C-053); Isa 29:11, skipped, says the vision has become a sealed book (C-009); Isa 40:21 — the canon's object reading is the unemended MT (C-012, D-049); Matt 28:6 agentless passive "was raised" (D-035); Acts 17:28 *genos* "stock, race" (D-044); *diabolos* = the Septuagint's rendering of *haśśāṭān* (E-048); Rev 8:12 (E-028).

### 3. Where the original is LESS favourable: readings that hang on a French word


**A-029** — TBWTT-2:62 none → Gen 6:16c · `translation-dependent` · original-less-favourable

QUOTE[TBWTT-2:62]: tu la disposeras en étages, l’inférieur, le second et le troisième ENDQUOTE
QUOTE[TBWTT-2:62]: Et la fusée à trois étages ENDQUOTE

- «en étages, l’inférieur, le second et le troisième» ↔ `תַּחְתִּיִּ֛ם שְׁנִיִּ֥ם וּשְׁלִשִׁ֖ים תַּֽעֲשֶֽׂהָ` (GEN-WOH-6:16) — 'lower ones, second ones and third ones you shall make it' — three plural adjectives, NO noun
- Cut: Rest of 6:16: the ṣōhar (roof/opening), 'finish it to a cubit above', and 'the door of the tēbâ you shall set in its side'.

The 'three-stage rocket' rests on the French noun 'étages', which does double duty in French (storeys of a building; stages of a rocket). The Hebrew has only three substantivised plural adjectives — lower, second, third — with the thing they qualify left unstated; they are plural ('lower ones'), suggesting sets of compartments per level rather than three single units. A three-level structure is hebrew-supported; the rocket-stage sense is carried by the French word.

**B-046** — TBWTT-3:104 (I Rois, VIII, 12-13) → 1 Kgs 8:12b–13 (condensed) · `translation-dependent` · original-less-favourable

QUOTE[TBWTT-3:104]: «Iahvé a dit qu'il réside dans un nuage. J'ai donc bâti vraiment une Maison pour ta demeure» ENDQUOTE
QUOTE[TBWTT-3:103]: Le grand roi Salomon fit construire sur la Terre une résidence somptueuse pour accueillir les créateurs quand ils venaient en visite. ENDQUOTE
QUOTE[TBWTT-3:107]: Qu'il réside dans un nuage, c'est-à-dire dans un engin en orbite autour de la Terre, au-dessus des nuages... ENDQUOTE

- «qu'il réside dans un nuage» ↔ `לִשְׁכֹּ֖ן בָּעֲרָפֶֽל׃` (1KI-WOH-8:12) — to dwell in the ʿărāp̄el — thick darkness, dark storm-cloud
- «une Maison pour ta demeure» ↔ `בֵּ֥ית זְבֻ֖ל לָ֑ךְ מָכ֥וֹן לְשִׁבְתְּךָ֖ עוֹלָמִֽים׃` (1KI-WOH-8:13) — a house of zəḇul (exalted dwelling) for you, a fixed place for your sitting/dwelling for ever
- (not quoted by the canon) `הַשָּׁמַ֜יִם וּשְׁמֵ֤י הַשָּׁמַ֙יִם֙ לֹ֣א יְכַלְכְּל֔וּךָ אַ֕ף כִּֽי־הַבַּ֥יִת הַזֶּ֖ה` (1KI-WOH-8:27) — the heavens and the heavens of the heavens cannot contain you; how much less this house
- Cut: Not marked: 'Then Solomon said' is dropped and the two verses are run together; 'a place for you to dwell in for ever' is shortened to 'pour ta demeure'. **(changes sense)**

The 'residence' half of the reading is solidly Hebrew (liškōn, ləšiḇtəḵā, bêṯ). The 'cloud = orbiting craft above the clouds' half depends on French 'nuage': the Hebrew word is ʿărāp̄el, the dense darkness of the Sinai theophany, not the common noun for cloud, so the gloss 'au-dessus des nuages' plays on a word the original does not use. The Hebrew also says the house is for dwelling 'for ever', against 'visits', and in the same prayer (v 27, unquoted) Solomon says no house can contain the one addressed.

**C-056** — TBWTT-3:243 (Psaumes, XIX-5) → Ps 19:5c (Hebrew numbering; English 19:4c) · `translation-dependent` · original-less-favourable

QUOTE[TBWTT-3:243]: «Pour le soleil, il a dressé une tente sur la mer (...)». ENDQUOTE
QUOTE[TBWTT-3:245]: Nouvelle allusion à l’amas de terre qui fut créé quand l’océan recouvrait la Terre et forma le continent originel ENDQUOTE

- «une tente sur la mer» ↔ `לַ֝שֶּׁ֗מֶשׁ שָֽׂם־אֹ֥הֶל בָּהֶֽם׃` (PSA-WOH-19:5) — for the sun he has set a tent in them
- Cut: Unmarked before: v.5ab "Their line has gone out through all the earth, and their words to the end of the world". The "(...)" after covers v.6. **(changes sense)**

The single word the reading rests on — "mer" — is absent from the Masoretic text, which reads bāhem "in them"; the French follows an emendation. This is the purest translation-dependent case in the slice: the reading (a structure on the sea = the first continent) has no foothold in the Hebrew as transmitted. Even in the emended form the "tent" is the sun's.

**C-032** — TBWTT-3:191 (Ezéchiel, XLII-14) → Ezek 42:14 (part) · `translation-dependent` · original-less-favourable

QUOTE[TBWTT-3:191]: «Quand les prêtres sortiront, (...) ils laisseront là les vêtements avec lesquels ils officient, car (ces vêtements) sont saints». ENDQUOTE
QUOTE[TBWTT-3:190]: avaient des vêtements aseptiques pour faire leur service et ces vêtements devaient rester dans le «temple» pour ne pas risquer de ramener des germes dangereux pour les créateurs ENDQUOTE
QUOTE[TBWTT-3:192]: Ils auraient dû écrire «car ces vêtements sont sains» SAINS ENDQUOTE

- «car (ces vêtements) sont saints» ↔ `כִּֽי־קֹ֣דֶשׁ הֵ֑נָּה` (EZK-WOH-42:14) — for they are holiness / a holy thing
- «Quand les prêtres sortiront» ↔ `בְּבֹאָ֣ם הַכֹּהֲנִ֗ים` (EZK-WOH-42:14) — when the priests enter
- «ils laisseront là les vêtements» ↔ `וְשָׁ֞ם יַנִּ֧יחוּ בִגְדֵיהֶ֛ם אֲשֶׁר־יְשָׁרְת֥וּ בָהֶ֖ן` (EZK-WOH-42:14) — and there they shall lay down their garments in which they minister
- «pour ne pas risquer de ramener des germes» ↔ `וְלֹֽא־יְקַדְּשׁ֥וּ אֶת־הָעָ֖ם בְּבִגְדֵיהֶֽם׃` (EZK-WOH-44:19) — so that they do not sanctify the people by their garments
- Cut: "they shall not go out of the holy place into the outer court"; and after the quotation "they shall put on other garments and approach what belongs to the people".

The explicit argument ("they should have written sains") is a French homophone and cannot be stated in Hebrew; on that point the reading is wholly translation-dependent. Separately, the rule the canon describes is in the Hebrew and is stated more fully in the omitted clauses and in 44:19: service garments are confined to the inner area and changed before contact with the people, because qōḏeš is treated as transmissible by contact. In the Hebrew the transmission runs outward (the people must not be "sanctified"), not inward as the germ reading requires.

**E-031** — LWTE-2:187 (Apocalypse, IX, 7 à 10.) → Rev 9:7-10 · `translation-dependent` · original-less-favourable

QUOTE[LWTE-2:187]: Elles avaient des thorax comme des thorax de fer et le bruit de leurs ailes était comme bruit de chars et de chevaux qui courent à la guerre. ENDQUOTE
QUOTE[LWTE-2:190]: Ces «sauterelles » métalliques, recouvertes de métal pour un primitif, comme un cheval qui part pour la guerre, ont un cockpit à l'intérieur duquel l'on voit le visage d'un homme, «leurs faces pareilles à des faces d'hommes », et en volant très haut dans le ciel elles laissent une traînée blanche que Jean appelle des cheveux, leurs «dents» ce sont les missiles accrochés sous leurs ailes, le «thorax de fer» c'est le fuselage, le bruit, c'est celui des tuyères des réacteurs ENDQUOTE

- «des thorax comme des thorax de fer» ↔ `θώρακας ὡς θώρακας σιδηροῦς` (REV-WOH-9:9) — breastplates like iron breastplates
- «cuirasses de feu» ↔ `θώρακας πυρίνους` (REV-WOH-9:17) — breastplates of fire
- «le bruit de leurs ailes» ↔ `ἡ φωνὴ τῶν πτερύγων αὐτῶν` (REV-WOH-9:9) — the sound of their wings
- «leurs faces comme des faces d'hommes» ↔ `τὰ πρόσωπα αὐτῶν ὡς πρόσωπα ἀνθρώπων` (REV-WOH-9:7) — their faces like faces of humans
- «pareil à des chevaux prêts pour la guerre» ↔ `ὅμοια ἵπποις ἡτοιμασμένοις εἰς πόλεμον` (REV-WOH-9:7) — like horses made ready for war

The clearest case in the slice of a reading resting on a French word. 'Thorax de fer' → fuselage works only because the French version transliterates thōrax, which in French means the body-trunk; in this Greek it is armour — and the same French version renders the same word 'cuirasses' eight verses later. With 'iron breastplates' the locusts are armoured like the war-horses of 9:7, and the body/fuselage step disappears. Conversely the Greek does give winged, loud, armoured, human-faced flyers, and every feature is flagged as comparison (hōs/homoios, as the library note stresses), which is the canon's own premise (a primitive describing by likeness). The golden crowns (9:7) get no gloss. The library note records the thorax point.

**E-032** — LWTE-2:191 (Apocalypse, IX, 13.) → Rev 9:13 · `translation-dependent` · original-less-favourable

QUOTE[LWTE-2:191]: Le sixième ange a trompeté et j'ai entendu une voix sortir des quatre cornes de l'autel d'or qui est devant Dieu. ENDQUOTE
QUOTE[LWTE-2:193]: Jean décrit là les quatre haut-parleurs situés devant moi lorsque je lui faisais assister à tout cela. ENDQUOTE

- «une voix sortir des quatre cornes de l'autel d'or» ↔ `φωνὴν μίαν ἐκ τῶν κεράτων τοῦ θυσιαστηρίου τοῦ χρυσοῦ` (REV-WOH-9:13) — one voice out of the horns of the golden altar
- «qui est devant Dieu» ↔ `τοῦ ἐνώπιον τοῦ θεοῦ` (REV-WOH-9:13) — which is before God

The count 'four' in «quatre haut-parleurs» depends on a textual variant: the Greek text the library translates reads 'from the horns of the golden altar' with no numeral, while the French the canon quotes has 'des quatre cornes'. The qualitative hook — a single voice coming out of horns standing before the throne — survives in either text; the number does not. The library note mentions that the canon quotes 'the four horns' and that its own line follows the SBLGNT, without drawing the consequence for the reading.

Others in this class: «science» for *daʿaṯ* at Gen 2:17, 3:22, Jer 10:14 (A-013, A-020, C-069) — at TBWTT-2:42 the `(...)` falls exactly on the object "good and bad"; «objet» at Gen 8:21 (A-034); «trompette» for *šôp̄ār* / *qeren hayyôḇēl* at Jericho and Gideon, although the canon's own quotation contains «corne de bélier» (B-030, B-034); «dieux étrangers» at Gen 35:2, the same noun *ʾĕlōhê* (B-002); «génies» from *maśkîlîm* (C-045); «La Peste» for the rider Death (E-021); «sept lampes d'or» for lampstands and «revêtu jusqu'aux pieds» (E-015); «aujourd'hui» at Isa 43:13 (D-057 above); «du monde» at Matt 13:35 (D-025); «Satan» as a proper name in Job, where the Hebrew always has the article (E-011) — though the title's sense, "the adversary", is the role the canon assigns (finding 2, C-061).

### 4. Plural and singular with Elohim in the quoted verses (extends woh-claim-0009)

What the text says, verse by verse:

- **Plural forms that are really there**, all inside direct speech or belonging to subordinate beings: Gen 1:26 cohortative and suffixes; Gen 3:22 "as one of us"; Gen 11:7 "let us go down and confuse" (A-012, A-019/A-020, A-037); plural verbs for the *bənê hāʾĕlōhîm* (Gen 6:2, 6:4; A-024, A-026) and for the two envoys at Sodom (A-039); the Aramaic plural in Dan 3:25, `לְבַר־אֱלָהִֽין` (DAN-WOH-3:25), printed literally as «fils des dieux» (C-040); the plural adjective at 1 Sam 17:26 (B-041 above).
- **Every narrator's verb with Elohim, YHWH Elohim or YHWH as subject is singular** in the quoted verses (Gen 1:1, 1:4, 1:7, 2:19, 3:14, 3:21, 3:22, 8:1, 11:8, 22:1; and throughout Exodus–Kings: no verse in TBWTT 3:3–141 has a plural verb or pronoun with Elohim). Unquoted Gen 1:27 reverts to "his image". The canon's «Ils / les créateurs / nous» is in its commentary, not in the French it quotes, which reproduces the Hebrew number faithfully. Core 0009's four plural-agreement exceptions (Gen 20:13; 35:7; Deut 5:26; Josh 24:19) are none of them quoted by the canon.
- **Singulars read as "the creators"** include *ʿelyôn* (Isa 14:14), *yōṣərô* (Isa 45:9), `γενεσιουργός` and `τὸν ὄντα` (Wis 13), singular *theou* (Matt 4:4), and "first and last" (Rev 1:17).
- **The canon's own quotations print «Dieu» where the Hebrew has ʾĕlōhîm.** TBWTT-2:5 objects to that rendering:

QUOTE[TBWTT-2:5]: Elohim, injustement traduit dans certaines Bibles par Dieu, veut dire en Hébreu «ceux qui sont venus du ciel» et est bel et bien au pluriel ENDQUOTE

  yet in the Old Testament quotations that follow (my count over the guillemeted quotation spans):

| Canon paragraph | Canon's French | Original | Form |
|---|---|---|---|
| TBWTT-3:30 | «le Dieu d’Israël» | `אֱלֹהֵ֣י יִשְׂרָאֵ֑ל` (EXO-WOH-24:10) | construct plural ʾĕlōhê |
| TBWTT-3:81 | «(voué) à Dieu» | `נְזִ֧יר אֱלֹהִ֛ים` (JDG-WOH-13:5) | ʾĕlōhîm |
| TBWTT-3:93 | «du Dieu vivant» | `אֱלֹהִ֥ים חַיִּֽים` (1SA-WOH-17:26) | ʾĕlōhîm + PLURAL adjective ḥayyîm |
| TBWTT-3:99 | «l’Arche de Dieu» | `אֲר֤וֹן הָֽאֱלֹהִים֙` (2SA-WOH-6:6) | hāʾĕlōhîm with article |
| TBWTT-3:99 | «Dieu le frappa» | `וַיַּכֵּ֥הוּ שָׁ֛ם הָאֱלֹהִ֖ים` (2SA-WOH-6:7) | hāʾĕlōhîm with a SINGULAR verb |
| TBWTT-3:108 | «un homme de Dieu» | `אִ֣ישׁ אֱלֹהִ֗ים` (1KI-WOH-13:1) | ʾîš ʾĕlōhîm |
| TBWTT-3:115 | «un homme de Dieu» | `אִ֥ישׁ אֱלֹהִ֖ים` (1KI-WOH-17:24) | ʾîš ʾĕlōhîm |
| TBWTT-3:137 | «l’homme de Dieu» | `לְאִ֨ישׁ הָאֱלֹהִ֜ים` (2KI-WOH-4:42) | ʾîš hāʾĕlōhîm |
| TBWTT-3:148 | «étoiles de Dieu» | `לְכֽוֹכְבֵי־אֵ֖ל` (ISA-14:13) | ʾēl (singular noun, not ʾĕlōhîm) |
| TBWTT-3:194 | «la gloire du Dieu d’Israël» | `כְּבוֹד֙ אֱלֹהֵ֣י יִשְׂרָאֵ֔ל` (EZK-WOH-43:2) | construct ʾĕlōhê |
| TBWTT-3:196 | «Iahvé, Dieu d’Israël» | `יְהוָ֥ה אֱלֹהֵֽי־יִשְׂרָאֵ֖ל` (EZK-WOH-44:2) | construct ʾĕlōhê |
| TBWTT-3:210 | «Mon Dieu a envoyé son ange» | `אֱלָהִ֞י שְׁלַ֣ח מַלְאֲכֵ֗הּ` (DAN-WOH-6:23) | Aramaic ʾĕlāhî, singular noun + singular verb |
| TBWTT-5:28 | «moi je suis Dieu» | `וַֽאֲנִי־אֵֽל` (ISA-43:12) | ʾēl, singular |

  Ten of the thirteen render a form of ʾĕlōhîm (three render *ʾēl* or Aramaic *ʾĕlāh*). «Élohim» occurs 13 times inside quotation spans (e.g. Ps 8:6, `מֵאֱלֹהִ֑ים` (PSA-WOH-8:6), «de peu inférieur aux Elohim»). The quotation layer is therefore not uniform on the very word the canon's opening gloss turns on.

### 5. The canon's explicit statements about what the wording says

These are the few places where the canon argues from the letter of the text rather than re-identifying its referents; each can be checked directly.

| Canon statement | Verdict | Item |
|---|---|---|
| Gen 7:17 "il est bien dit … non pas sur les eaux" | contradicted by the elided clause and by 7:18 | A-030 |
| Josh 10:13 "presque un jour entier" said of the war | the adverbial measures the sun's delay | B-032 |
| Jericho/Gideon: the instrument "que la Bible nomme «trompette»" | Hebrew names a ram's horn | B-030, B-034 |
| Ezek 42:14 "ils auraient dû écrire sains" | a French homophone; cannot be stated for `קֹדֶשׁ` | C-032, C-078 |
| Matt 5:3 "sens originel" (if they have spirit, they will have the kingdom) | Greek has no conditional, no "have", no future | D-009 |
| Rev 1:16 sword = copyists' addition | library records no variant there | E-015 |
| Elohim "signifiait … en hébreu" / "littéralement" those who came from the sky (LWTE-3:6, 3:10, 4:87) | no lexical basis; already governed by 0009 | E-046 |
| Gen 3:21 "une phrase à peu près intacte du document originel" (TBWTT-2:41) | the canon prints bare «Elohim» for YHWH Elohim there, but «Iahvé Elohim» at 3:14 | A-018 |

### 6. References are almost always right; the numbering is Hebrew

Of 321 items only two references are wrong: ETTMTTP-2:72 prints «XXVII» for Ezekiel XXXVII (TBWTT-3:185 has it right; D-071), and the guillemeted Tent-of-Meeting sentence at TBWTT-3:37 is not locatable as a verse (B-018). Twenty-five are partial (a range cited for part of a verse; two verses conflated, e.g. «(Ezéchiel, I-9)» = 1:6a + 1:9b, C-018; references printed in the paragraph after the quotation). Verse numbering follows the Hebrew throughout where Hebrew and Vulgate/LXX differ (Ps 8:6; 19:5, 7; Jonah 2:1, 11; Mic 5:1–4; Dan 6:23) — consistent with a Hebrew-numbered French Bible (analysis). Quotations missing from the site's citation index: Gen 3:1–5 («III, I-5»), Gen 6:16c, Gen 1:2b, Matt 1:20 («I20»), Matt 13:3–4 (LWTE-2:8), Dan 10:13 (no reference printed), and the prose-referenced Josh 10:13, Judg 7, 1 Kgs 17:6, 2 Kgs 1:12.

### 7. The canon's French is not consistent with itself (extends woh-claim-0066's partial-mediation alternative)

- **Divine name.** «Iahvé» 61× in TBWTT and 10× in ETTMTTP; never in LWTE, which has «Yahvé» 47× — including for the same French sentence of Job 1:6 (TBWTT-3:250 vs LWTE-2:49; E-011).
- **Same verse, different wording.** Exod 33:20 «me voir» (TBWTT-3:41) vs «voir ma face» (LWTE-1:4); the Hebrew matches TBWTT (E-001). Ezek 1:6/9, 1:7, 1:18, 1:22–26 differ between first quotation and re-quotation; at 1:7 the re-quoted plural «brillaient» is closer to the Hebrew plural participle (C-013, C-076). TBWTT-5:29 re-quotes 5:28 dropping «aussi».
- **Same Hebrew or Greek word, different French.** *rāqîaʿ*: «firmament» (Gen 1, Dan 12:3) vs «plateforme» (Ezek 1); *rûaḥ*: «esprit» (Gen 1:2, 6:3) vs «vent» (Gen 8:1), and the readings follow the split (A-002, A-025, A-032); *nep̄eš*: «âme» (Gen 9, Lev 17) vs «vie» (Job 2:6); *daʿaṯ*: «science» vs «connaissance»; *thōrax*: «thorax» (Rev 9:9) vs «cuirasses» (Rev 9:17).
- **Inserted or altered words against the MT.** 1 Sam 3:10 adds «Iahvé» where the Hebrew has only "Speak" (B-040); 1 Sam 5:6 French «bubons», commentary «brûlures», Hebrew "swellings" (B-043); Mark 16:18 is prefaced by a bracket of the canon's own, «(Les temps seront venus quand les hommes)», replacing "those who believe … in my name" (D-038).
- **New Testament.** The NT and Revelation French is a different, very literal translation; the library notes do not identify it (candidate, unverified: the Pléiade NT). Dhorme's Pléiade is Old Testament only, so 0066's proposition cannot cover the NT layer as worded.

### 8. Key nouns

| Word | Canon's French | What the library text has | Bearing |
|---|---|---|---|
| *rāqîaʿ* | firmament / plateforme | beaten-out expanse; the verb *rqʿ* recurs at Job 37:18 | Hebrew more "solid/metallic" than «firmament»; object is the sky-vault |
| *rûaḥ* | esprit / vent | one word: wind, breath, spirit | split is French; Ezek journeys are "by the rûaḥ … in visions of Elohim" |
| *kāḇôḏ* | gloire | weight, splendour; fills the house from inside at 1 Kgs 8:10–11 | "gloire = craft" fits Ezek 10–11, 43; fits 1 Kgs 8 badly (B-047) |
| *ʿānān* / *ʿărāp̄el* | nuée, nuage | cloud / thick darkness | 1 Kgs 8:12 is *ʿărāp̄el* (B-046) |
| *malʾāḵ* / *angelos* | ange | one sent, envoy | original closer to the canon's "envoys" than «ange» (A-038) |
| *tannînîm* | (not quoted; «dragons» in prose) | see woh-claim-0073 | not redone |
| *nəp̄îlîm* | cut from Gen 6:4 | the clause is under the `(...)` | cut removes the alternative antecedent of "the heroes" (A-026) |
| *bənê hāʾĕlōhîm* | fils d'Élohim | with article, plural verbs (Gen 6:2; Job 1:6) | "sons of" ≠ the creators themselves; plurality real |
| *tēḇâ* | arche | box/chest; "three" levels are plural adjectives without a noun | «étages» carries the rocket sense (A-029) |
| *haśśāṭān* | Satan | always with the article in Job | title "the adversary": against the name, for the role |
| *nep̄eš* | âme | life, tied to blood, of animal and human | original more favourable (E-003) |
| *šôp̄ār* | trompette | ram's horn | French-dependent (B-030) |

## Full register

Columns: id · canon paragraph · stated reference → actual · library refIds · classification · direction · E = ellipsis present, **S** = ellipsis changes sense · N = an existing library note already makes the observation. Full analysis, load-bearing words and outside-knowledge flags for each item are in `hebrew-audit.json`.

| id | canon ¶ | stated → actual | refIds | class | dir | E | N | first sentence of analysis |
|---|---|---|---|---|---|---|---|---|
| A-001 | TBWTT-2:4 | (Genèse, I-1) → Gen 1:1 | GEN-WOH-1:1 | addition | = |  |  | The plural FORM of Elohim is in the Hebrew (hebrew-supported as far as it goes), but the predicate is singular (bārāʾ), so the verse itself gives no plural agreement; the French reproduces that faithfully. |
| A-002 | TBWTT-2:6 | none → Gen 1:2b | GEN-WOH-1:2 | addition | MORE | E |  | The hook is the hovering of something belonging to Elohim over the waters, and that is the Hebrew's own image (participle of continuous hovering; subject rûaḥ, grammatically feminine singular). |
| A-003 | TBWTT-2:7 | (Genèse, I-4) → Gen 1:4a | GEN-WOH-1:4 | addition | = | **S** |  | The evaluative formula ('saw that … good') is in the Hebrew and is read by the canon as a test result — a possible construal of the wording. |
| A-004 | TBWTT-2:9 | (Genèse, I-5) → Gen 1:5b | GEN-WOH-1:5 | addition | less | **S** |  | Neither Hebrew nor French carries a hook for a 2,000-year 'day'; the equation is supplied by the canon. |
| A-005 | TBWTT-2:11 | (Genèse, I-7) → Gen 1:7 (middle clause) | GEN-WOH-1:7 | addition | less | **S** |  | The two-waters structure is in the Hebrew, but the agent's action there is making a rāqîaʿ and dividing — not descending. |
| A-006 | TBWTT-2:13 | (Genèse, I-9) → Gen 1:9 | GEN-WOH-1:9 | addition | = |  |  | French and Hebrew say the same thing: waters are gathered into one place and dry ground becomes visible. |
| A-007 | TBWTT-2:15 | (Genèse, I, 11-12) → Gen 1:11 (wording of v.11; v.12 repeats it) | GEN-WOH-1:11, GEN-WOH-1:12 | supported | = | E | N | The reading's textual hook — plants that carry their own seed and reproduce by kind — is squarely in the Hebrew (and doubled in v.12, including the cut 'seed-seeding' participle, which would have reinforced it). |
| A-008 | TBWTT-2:17 | (Genèse, I-14) → Gen 1:14 | GEN-WOH-1:14 | supported | = |  |  | The calendrical function (luminaries as markers for times, days, years) is the Hebrew's own statement, so the time-measurement hook is real. |
| A-009 | TBWTT-2:19 | (Genèse, I-20.) → Gen 1:20 | GEN-WOH-1:20 | supported | = | E |  | The order waters-creatures then flyers and the swarming image are the Hebrew's own; the canon's elaborations (plankton, food chains, artists, contests) are supplied. |
| A-010 | TBWTT-2:22 | none → Gen 1:21 (narrated, not quoted) | GEN-WOH-1:21 | supported | = | E | N | Already covered by core woh-claim-0073. |
| A-011 | TBWTT-2:23 | (Genèse, I-24) → Gen 1:24 | GEN-WOH-1:24 | supported | = |  |  | The sequence sea – air – land and the land-animal classes are in the Hebrew. |
| A-012 | TBWTT-2:26 | (Genèse, I-26) → Gen 1:26 | GEN-WOH-1:26 | supported | = | E |  | This is the strongest plural hook in the Genesis sequence and it is fully in the Hebrew: cohortative plural plus two plural suffixes. |
| A-013 | TBWTT-2:29 | (Genèse, II, 16-17) → Gen 2:16b–17 | GEN-WOH-2:16, GEN-WOH-2:17 | transl-dep | less | E |  | The step from the tree to 'scientific books' passes through the French word 'science'. |
| A-014 | TBWTT-2:31 | (Genèse, II-19) → Gen 2:19 (middle clause) | GEN-WOH-2:19 | contradicted | = | **S** | N | The canon's gloss (the creators taught him the names) reverses the direction of naming in the verse it quotes: in Hebrew — and already in the French clause quoted ('pour voir comment il les appellerait') — the maker brin |
| A-015 | TBWTT-2:34 | (Genèse, III, I-5) → Gen 3:1–5 (composite) | GEN-WOH-3:1, GEN-WOH-3:3… | addition | MORE | **S** |  | Two findings pull in opposite directions. |
| A-016 | TBWTT-2:36 | (Genèse, III-7) → Gen 3:7a | GEN-WOH-3:7 | addition | = | E |  | The eye-opening/knowing vocabulary is in the Hebrew, but the text specifies what was known (their nakedness) and the canon replaces that object with another. |
| A-017 | TBWTT-2:38 | (Genèse, III-14) → Gen 3:14 | GEN-WOH-3:14 | addition | less | **S** |  | The exile reading rests on taking 'on your belly … dust' figuratively as being bound to the ground; that is supplied. |
| A-018 | TBWTT-2:40 | (Genèse, III-21) → Gen 3:21 | GEN-WOH-3:21 | supported | = |  |  | The reading stays close to the plain sense (the makers clothe the pair), so the hook is in the Hebrew. |
| A-019 | TBWTT-2:42 | (Genèse, III-22) → Gen 3:22 — the plural and the tree of life | GEN-WOH-3:22 | supported | = | E |  | Both hooks of the reading — a plural 'us' among whom the human now ranks, and a means of living ləʿōlām that must be kept from him — are in the Hebrew wording. |
| A-020 | TBWTT-2:42 | (Genèse, III-22) → Gen 3:22 — 'grâce à la science (...)' | GEN-WOH-3:22 | transl-dep | less | **S** |  | This is the clearest case in the Genesis sequence of a reading produced by the French plus an ellipsis. |
| A-021 | TBWTT-2:44 | (Genèse, III-24) → Gen 3:24 | GEN-WOH-3:24 | supported | MORE |  |  | The guard-post scenario (beings stationed, a flaming device, to guard an access route) is the Hebrew's own. |
| A-022 | TBWTT-2:47 | (Genèse, IV, 3-4) → Gen 4:3–4a | GEN-WOH-4:3, GEN-WOH-4:4 | addition | = | E |  | Bringing produce and animals to a superior is the Hebrew's plain content, and the cut noun minḥâ ('tribute') fits the canon's provisioning reading at least as well as the French. |
| A-023 | TBWTT-2:49 | (en Genèse, V, 1-11) → Gen 5:5, 5:8, 5:11 (figures) | GEN-WOH-5:5, GEN-WOH-5:8… | addition | = |  |  | The three figures agree exactly with the Masoretic numbers in the library text. |
| A-024 | TBWTT-2:50 | (Genèse, VI, 1-2) → Gen 6:1–2 | GEN-WOH-6:1, GEN-WOH-6:2 | supported | MORE |  |  | The union of beings from the Elohim side with human women is the Hebrew's explicit content, with unambiguous plural verbs. |
| A-025 | TBWTT-2:52 | (Genèse, VI-3) → Gen 6:3 (speech only) | GEN-WOH-6:3 | supported | MORE | E |  | A limit on human lifespan connected with the withdrawal of something of the speaker's from the human is what the Hebrew says. |
| A-026 | TBWTT-2:54 | (Genèse, VI-4) → Gen 6:4b | GEN-WOH-6:4 | supported | = | **S** |  | Interfertility and offspring are stated in the Hebrew ('they bore to them'), so the canon's 'preuve' has its hook in the original. |
| A-027 | TBWTT-2:56 | (Genèse, VI-5) → Gen 6:5 | GEN-WOH-6:5 | addition | = |  |  | The canon redefines 'evil' as scientific ambition; that is a declared re-reading, not a property of either text. |
| A-028 | TBWTT-2:58 | none → Gen 6:14–16 (the ark as a rocket; narrated) | GEN-WOH-6:14 | addition | less | **S** |  | The canon itself flags part of this as figurative ('Ceci est une image' — about the animal pairs). |
| A-030 | TBWTT-2:59 | (Genèse, VII-17) → Gen 7:17 (first and last words only) | GEN-WOH-7:17 | contradicted | less | **S** |  | The quoted words are really there (wattārom mēʿal hāʾāreṣ), so the phrase is not a translation artefact. |
| A-031 | TBWTT-2:61 | (Genèse, VII-24) → Gen 7:24 | GEN-WOH-7:24 | addition | = | E |  | The duration is in the Hebrew; the fallout explanation is supplied. |
| A-029 | TBWTT-2:62 | none → Gen 6:16c | GEN-WOH-6:16 | transl-dep | less | E |  | The 'three-stage rocket' rests on the French noun 'étages', which does double duty in French (storeys of a building; stages of a rocket). |
| A-032 | TBWTT-2:63 | (Genèse, VIII-1) → Gen 8:1 | GEN-WOH-8:1 | addition | MORE | E |  | A deliberate agent-caused passing of a rûaḥ over the earth that makes the waters go down is the Hebrew's content; decontamination is supplied. |
| A-033 | TBWTT-2:65 | (Genèse, VIII-20) → Gen 8:20 | GEN-WOH-8:20 | addition | = |  |  | An animal offering to YHWH followed (8:21) by a promise not to strike again is the Hebrew sequence, so the gratitude-and-pledge frame has a textual basis. |
| A-034 | TBWTT-2:67 | (Genèse, VIII-21) → Gen 8:21 (one clause) | GEN-WOH-8:21 | transl-dep | less | **S** |  | The canon's equation 'objet … est le mal' → 'le but de l’homme est le progrès scientifique' needs the French word 'objet' in the sense of 'aim'. |
| A-035 | TBWTT-2:69 | (Genèse, X-32) → Gen 10:32b | GEN-WOH-10:32 | contradicted | = | **S** |  | The verse the canon cites for the redistribution of pre-existing races says, in Hebrew and in the French once the antecedent of 'D’elles' is restored, that the nations branched off from the families of Noah's sons. |
| A-036 | TBWTT-2:73 | (Genèse, XI-6) → Gen 11:6b | GEN-WOH-11:6 | supported | MORE | E | N | The speaker's concern in the Hebrew is exactly unlimited capability ('nothing they plan to do will be out of their reach'), with no moral vocabulary — the existing library note makes the same observation. |
| A-037 | TBWTT-2:75 | (Genèse, XI, 7-8.) → Gen 11:7–8a | GEN-WOH-11:7, GEN-WOH-11:8 | supported | = | **S** |  | The plural descent ('let us go down … let us confuse') is in the Hebrew in two unambiguous first-person-plural cohortatives, and the scattering is explicit. |
| A-038 | TBWTT-2:79 | (Genèse, XIX-1) → Gen 19:1a | GEN-WOH-19:1 | supported | MORE | E |  | The Hebrew malʾākîm means 'those sent' — agents on a mission — which is closer to the canon's 'envoyèrent deux espions' than the French 'Anges' it quotes. |
| A-039 | TBWTT-2:81 | (Genèse, XIX-11) → Gen 19:11a | GEN-WOH-19:11 | addition | MORE | E |  | That the two envoys themselves strike a crowd with an instantaneous blinding is the Hebrew's statement (plural active verb). |
| A-040 | TBWTT-2:83 | (Genèse, XIX-14) → Gen 19:14 (speech only) | GEN-WOH-19:14 | addition | = | **S** |  | The warning of imminent destruction is in the Hebrew; the atomic nature is supplied. |
| A-041 | TBWTT-2:85 | (Genèse, XIX-17) → Gen 19:17 (part) | GEN-WOH-19:17 | addition | MORE | E |  | Urgent evacuation orders are the Hebrew's content; 'la bombe' is supplied. |
| A-042 | TBWTT-2:86 | (Genèse, XIX, 24-26) → Gen 19:24–26 | GEN-WOH-19:24, GEN-WOH-19:25… | supported | = | E |  | Fire and sulphur 'from YHWH, from the skies', destroying cities, a plain and its vegetation, with a straggler turned to salt: all of that is the Hebrew's wording, so the sky-delivered destruction is a real textual hook. |
| A-043 | TBWTT-2:90 | (Genèse, XXII-12) → Gen 22:12a | GEN-WOH-22:12 | supported | MORE | E |  | The canon's reading (a test to establish the patriarch's disposition) is the Hebrew's own framing: 22:1 says 'the Elohim tested Abraham' and 22:12 'now I know'. |
| B-001 | TBWTT-3:3 | (Genèse, XXVIII-12) → Gen 28:12 | GEN-WOH-28:12 | supported | less | **S** |  | The traffic of malʾăḵê ʾĕlōhîm between earth and sky is in the Hebrew exactly as in the French, so the textual hook is real. |
| B-002 | TBWTT-3:5 | (Genèse, XXXV-2) → Gen 35:2 | GEN-WOH-35:2, GEN-WOH-35:4 | transl-dep | less | E |  | The reading contrasts the true creators (Elohim) with stones and idols ('dieux étrangers'). |
| B-003 | TBWTT-3:8 | (Exode, III-2) → Exod 3:2 | EXO-WOH-3:2, EXO-WOH-3:4 | addition | less | E |  | Nothing in the Hebrew describes a descent, a landing or a vehicle: the only objects are a messenger, a flame of fire, and one particular bush (hassəneh, with article). |
| B-004 | TBWTT-3:11 | (Exode, XIII-21) → Exod 13:21 | EXO-WOH-13:21 | supported | MORE |  |  | The guiding function (lanḥōṯām) and the day/night column are in the Hebrew as quoted. |
| B-005 | TBWTT-3:13 | (Exode, XIV-19) → Exod 14:19b–20 | EXO-WOH-14:19, EXO-WOH-14:20 | supported | MORE | **S** |  | The screen function is stated more explicitly in the uncited Hebrew than in the excerpt the canon prints: the column 'came between' the two camps and 'the one did not come near the other all night'. |
| B-006 | TBWTT-3:16 | (Exode, XIV-21) → Exod 14:21b | EXO-WOH-14:21, EXO-WOH-14:22 | contradicted | less | **S** |  | The splitting and drying are in the Hebrew as quoted, but the instrument is named in the half-verse the canon elides: a strong east wind working all night. |
| B-007 | TBWTT-3:18 | (Exode, XIV-30) → Exod 14:30a | EXO-WOH-14:30 | no-reading | = | E |  | Plain narrative summary; nothing rests on a particular word. |
| B-008 | TBWTT-3:20 | (Exode, XVI-14) → Exod 16:14 | EXO-WOH-16:14, EXO-WOH-16:4… | addition | MORE | E |  | The verse quoted gives only location (ʿal-pənê hammiḏbār) and texture (daq məḥuspās); 'chemical', 'synthetic' and 'swelling' are additions. |
| B-009 | TBWTT-3:23 | (Exode, XVII-6) → Exod 17:6 | EXO-WOH-17:6, EXO-WOH-17:5 | addition | less |  |  | The Hebrew gives the staff a striking role (wəhikkîṯā) and gives the locating role to YHWH, who stands 'there on the rock' in front of Moses. |
| B-010 | TBWTT-3:25 | (Exode, XIX-16) → Exod 19:16 | EXO-WOH-19:16 | addition | = | E |  | The phenomena listed are those of the Hebrew; none of the nouns denotes a vehicle. |
| B-011 | TBWTT-3:26 | (Exode, XIX, 18-19) → Exod 19:18–19a | EXO-WOH-19:18, EXO-WOH-19:19 | supported | = | E |  | Each physical element the reading uses — a descent (yāraḏ) onto the mountain, in fire, with kiln-like smoke, ground tremor and a sound that keeps getting louder — is in the Hebrew exactly as in the French. |
| B-012 | TBWTT-3:28 | (Exode, XIX, 23-24) → Exod 19:23a + 19:24b | EXO-WOH-19:23, EXO-WOH-19:24… | addition | less | **S** |  | The crowd-surge image has a real Hebrew basis in ʾal-yehersû 'let them not break through'. |
| B-013 | TBWTT-3:29 | (Exode, XXIV-2) → Exod 24:2 | EXO-WOH-24:2, EXO-WOH-24:1 | supported | = |  | N | Graded access (Moses alone; 'they' at a distance; the people not at all) is what the Hebrew says. |
| B-014 | TBWTT-3:30 | (Exode, XXIV-10) → Exod 24:10 | EXO-WOH-24:10, EXO-WOH-24:11 | supported | = |  | N | A made surface (maʿăśēh), of tile-work (liḇnâ), blue and sky-clear, under the feet of a single visible figure: all of this is Hebrew, and the French renders it without loss. |
| B-015 | TBWTT-3:32 | (Exode, XXIV-17) → Exod 24:17 | EXO-WOH-24:17, EXO-WOH-24:16 | addition | = | E | N | That the kāḇôḏ is a localized, visible thing with an 'appearance' that 'settles' on a mountain (v 16) is Hebrew, and the Hebrew noun (root kbd, weight) is more concrete than French 'gloire' — on the noun the original is  |
| B-016 | TBWTT-3:35 | (Exode, XXV, 2-7) → Exod 25:2–7 (condensed) | EXO-WOH-25:2, EXO-WOH-25:3… | contradicted | less | **S** | N | The reading needs a compulsory levy of food and exportable wealth. |
| B-017 | TBWTT-3:36 | chapitre XXVI de l'Exode (prose reference, no quotation) → Exod 26 (tabernacle instructions); the governing statement i | EXO-WOH-25:8, EXO-WOH-25:9 | supported | MORE |  |  | This is a case where the canon cites a chapter without quoting and the unquoted Hebrew is closer to its reading than any French it prints: the structure is called miškān 'dwelling', its purpose is 'that I may dwell (wəšā |
| B-018 | TBWTT-3:37 | none → Not a verse as worded; nearest is Exod 33:8–9 (Moses enterin | EXO-WOH-33:7, EXO-WOH-33:8 | supported | = |  |  | ʾōhel môʿēḏ does mean a tent of (appointed) meeting, so the 'rendez-vous' sense the canon relies on is in the Hebrew. |
| B-019 | TBWTT-3:38 | (Exode, XXXIII-9) → Exod 33:9 | EXO-WOH-33:9 | supported | MORE |  | N | Descent and stationing of the column at the door are Hebrew. |
| B-020 | TBWTT-3:39 | (Exode, XXXIII-11) → Exod 33:11a | EXO-WOH-33:11 | supported | = | E | N | The wording the reading rests on (pānîm ʾel-pānîm; ʾîš ʾel-rēʿēhû) is Hebrew and is rendered exactly. |
| B-021 | TBWTT-3:41 | (Exode, XXXIII-20) → Exod 33:20 | EXO-WOH-33:20, EXO-WOH-24:11 | addition | = |  | N | The verse states a prohibition/impossibility and a lethal consequence; it names no cause. |
| B-022 | TBWTT-3:44 | (Lévitique) XXI, 17-18 (prose reference in TBWTT-3:43) → Lev 21:17–18 (condensed) |  | not-checkable | = |  |  | Leviticus 21 is not held in the library in Hebrew (leviticus-woh has only chapters 17 and 25), so the load-bearing phrase 'l'aliment de son Dieu' cannot be compared against library data. |
| B-023 | TBWTT-3:47 | (Nombres) XI, 7-8 (prose reference in TBWTT-3:46) → Num 11:7 + 11:8b | NUM-WOH-11:7, NUM-WOH-11:8 | addition | less | E | N | All three descriptors are comparisons (kə-) to things that are themselves uncertain (gaḏ, bəḏōlaḥ, ləšaḏ), so 'very exact description' overstates what the Hebrew offers; the uncertainty is smoothed by the French ('corian |
| B-024 | TBWTT-3:49 | (Nombres, XVIII-13) → Num 18:13a | NUM-WOH-18:13 | contradicted | less | **S** | N | The quoted words are accurate but form only the subject of the Hebrew sentence. |
| B-025 | TBWTT-3:51 | (Nombres, XXI-8) → Num 21:8 | NUM-WOH-21:8, NUM-WOH-21:9 | addition | = |  | N | The Hebrew says a bitten person who sees (v 8) or gazes at (v 9) the bronze figure lives; no instrument, substance or operator is mentioned. |
| B-026 | TBWTT-3:54 | (Nombres, XXXIII, 52-53) → Num 33:52 (part) + 33:53a | NUM-WOH-33:52, NUM-WOH-33:53 | supported | = | E | N | A historical, not technological, reading, and the Hebrew says what the canon says: a divine order to destroy cast images and take the land. |
| B-027 | TBWTT-3:56 | (Deutéronome, IV-37) → Deut 4:37a | DEU-WOH-4:37 | supported | = | E | N | The election statement is Hebrew (wayyiḇḥar). |
| B-028 | TBWTT-3:58 | Josué, III, 15-16 (prose reference in TBWTT-3:57) → Josh 3:15a + 3:16 (condensed) | JOS-WOH-3:15, JOS-WOH-3:16 | addition | less | **S** | N | The Hebrew describes a river dammed 'very far off' at a named upstream location, with the lower reach running dry — a different geometry from the sea crossing (wind; walls of water to right and left, Exod 14:21–22) to wh |
| B-029 | TBWTT-3:62 | (Josué, V-14) → Josh 5:14a | JOS-WOH-5:14, JOS-WOH-5:13 | supported | MORE | E | N | The reading — a military officer of YHWH's forces arriving in person — is the literal sense of śar-ṣəḇāʾ-YHWH ʿattâ ḇāʾṯî. |
| B-030 | TBWTT-3:64 | (Josué, VI-5) → Josh 6:5 (condensed) | JOS-WOH-6:5, JOS-WOH-6:20 | transl-dep | less | **S** | N | The reading turns on the name of the instrument: 'un instrument très compliqué que la Bible nomme «trompette»'. |
| B-031 | TBWTT-3:67 | (Josué, X-11) → Josh 10:11 (condensed) | JOS-WOH-10:11 | supported | = | E | N | 'Hurled great stones from the skies' is the literal Hebrew (hišlîḵ … min-haššāmayim), and the casualty comparison is as quoted, so the hook for 'bombardment' is textual. |
| B-032 | TBWTT-3:70 | Josué, (X-13) (prose reference in TBWTT-3:69) → Josh 10:13a (quotation) + 10:13b (the phrase 'presque un jou | JOS-WOH-10:13, JOS-WOH-10:12… | contradicted | less | **S** | N | The canon's argument is that the text 'says further on that it [the war] lasted almost a whole day'. |
| B-033 | TBWTT-3:73 | (Juges, VI-21.) → Judg 6:21 | JDG-WOH-6:21, JDG-WOH-6:20… | addition | less | E | N | The Hebrew has a staff-tip touching food laid on a rock, fire rising from the rock and 'eating' the food, and the messenger walking away. |
| B-034 | TBWTT-3:75 | Juges, VII (prose reference, paraphrase) → Judg 7:16–22 | JDG-WOH-7:16, JDG-WOH-7:20… | transl-dep | less | **S** | N | As at Jericho the technological reading is hung on the word 'trompettes', printed in scare-quotes; the Hebrew instrument is the šôp̄ār, a ram's horn. |
| B-035 | TBWTT-3:78 | (Juges, XIII-3) → Judg 13:3 | JDG-WOH-13:3, JDG-WOH-13:6… | addition | MORE | E |  | The quoted verse says only that a messenger appeared and announced a conception; 'union' is supplied by the canon. |
| B-036 | TBWTT-3:81 | (Juges, XIII, 4-5) → Judg 13:4a + 13:5a | JDG-WOH-13:4, JDG-WOH-13:5 | addition | = | E | N | The uncut hair and the wine ban are Hebrew; the reasons the canon gives (antennas; a healthy experimental subject) replace the reason the Hebrew gives in the same clause, kî nəzîr ʾĕlōhîm — because he is a nazirite, a co |
| B-037 | TBWTT-3:82 | (Juges, XIII-9) → Judg 13:9b | JDG-WOH-13:9, JDG-WOH-13:8… | supported | less | **S** | N | The clause the canon leans on — 'her husband was not with her' — is Hebrew, and bôʾ ʾel ('came to the woman') can carry a sexual sense. |
| B-038 | TBWTT-3:86 | none (allusion to Judg 16) → Judg 16:17–30 |  | not-checkable | = |  |  | Judges 16 is not held in Hebrew in the library, so the wording behind 'force', the cutting of the hair and the collapse of the building cannot be compared. |
| B-039 | TBWTT-3:88 | (I Samuel, III-9) → 1 Sam 3:9a | 1SA-WOH-3:9, 1SA-WOH-3:8 | addition | = | E | N | The Hebrew vocabulary is that of ordinary speech and hearing (qārāʾ 'call', dibber 'speak', šāmaʿ 'hear'). |
| B-040 | TBWTT-3:91 | (I Samuel, III-10) → 1 Sam 3:10 | 1SA-WOH-3:10 | addition | less | **S** |  | For a telepathic reading the Hebrew is less favourable than the excerpt: the elided words say that YHWH 'came and stationed himself' (wayyāḇōʾ … wayyiṯyaṣṣaḇ) and then called — a presence in the room, not a transmission. |
| B-041 | TBWTT-3:93 | (I Samuel, XVII-26) → 1 Sam 17:26b | 1SA-WOH-17:26 | supported | MORE | E |  | The reading rests on the adjective 'living', which is Hebrew (ḥayyîm). |
| B-042 | TBWTT-3:96 | I Samuel, V, 1-5 (prose reference, paraphrase) → 1 Sam 5:3–4 | 1SA-WOH-5:3, 1SA-WOH-5:4 | addition | less |  | N | The position of the statue is as the Hebrew gives it. |
| B-043 | TBWTT-3:97 | (I Samuel, V-6) → 1 Sam 5:6 (condensed) | 1SA-WOH-5:6 | addition | = | E | N | Hebrew, French and reading are three different things here: the Hebrew has 'swellings' (with a Ketiv/Qere alternation), the French 'bubons', the canon's commentary 'burns'. |
| B-044 | TBWTT-3:99 | (II Samuel, VI, 6-7) → 2 Sam 6:6b–7 | 2SA-WOH-6:6, 2SA-WOH-6:7 | supported | = |  | N | The physical sequence the reading uses is exactly the Hebrew's: the load shifts, a man grasps the chest, and he dies on the spot beside it (šām … šām). |
| B-045 | TBWTT-3:101 | (I Rois, I-50 ; I Rois, II-28...) → 1 Kgs 1:50; 2:28 | 1KI-WOH-1:50, 1KI-WOH-2:28 | addition | less |  | N | Both verses give the action a stated cause — fear of Solomon and flight — and the verb is 'hold on to', which suits a suppliant clinging and not an operator at controls. |
| B-046 | TBWTT-3:104 | (I Rois, VIII, 12-13) → 1 Kgs 8:12b–13 (condensed) | 1KI-WOH-8:12, 1KI-WOH-8:13… | transl-dep | less | **S** | N | The 'residence' half of the reading is solidly Hebrew (liškōn, ləšiḇtəḵā, bêṯ). |
| B-047 | TBWTT-3:105 | (I Rois, VIII-11) + (I Rois, VIII-10) → 1 Kgs 8:11b; 8:10b | 1KI-WOH-8:11, 1KI-WOH-8:10 | addition | less | **S** |  | The French is exact for both clauses. |
| B-048 | TBWTT-3:106 | (I Rois, VI-13) → 1 Kgs 6:13a | 1KI-WOH-6:13 | supported | = | E | N | šāḵan 'dwell' is the verb of the miškān (Exod 25:8) and supports 'résider' fully. |
| B-049 | TBWTT-3:108 | (I Rois, XIII, 1-5) → 1 Kgs 13:1–5 (heavily condensed) | 1KI-WOH-13:1, 1KI-WOH-13:3… | contradicted | less | **S** | N | The canon identifies the actor as 'un des créateurs'. |
| B-050 | TBWTT-3:110 | (I Rois, XIII, 9-10) → 1 Kgs 13:9b–10a | 1KI-WOH-13:9, 1KI-WOH-13:10 | addition | = | E | N | The prohibition and its execution are quoted accurately. |
| B-051 | TBWTT-3:112 | I Rois, XVII-6 (prose reference in TBWTT-3:111) → 1 Kgs 17:6a | 1KI-WOH-17:6, 1KI-WOH-17:4 | supported | MORE | E | N | Birds delivering food twice daily is the plain Hebrew. |
| B-052 | TBWTT-3:114 | (I Rois, XVII-23) → 1 Kgs 17:23b | 1KI-WOH-17:23, 1KI-WOH-17:17… | supported | MORE | E | N | The canon says 'mourant' (dying), not dead. |
| B-053 | TBWTT-3:115 | (Rois, XVII-24) → 1 Kgs 17:24a | 1KI-WOH-17:24, 1KI-WOH-18:36… | addition | less | E |  | The Carmel paraphrase has one Hebrew-supported peg — the fire falls at a set hour (baʿălôṯ hamminḥâ, 18:36) — and one detail the Hebrew works against: 'hidden in the clouds'. |
| B-054 | TBWTT-3:116 | (I Rois, XVIII-38) → 1 Kgs 18:38 | 1KI-WOH-18:38 | supported | = |  | N | The Hebrew describes a fire that falls from above (wattippōl) and consumes offering, wood, stones, soil and water. |
| B-055 | TBWTT-3:119 | (I Rois, XIX, 5-6) → 1 Kgs 19:5b–6a | 1KI-WOH-19:5, 1KI-WOH-19:6 | supported | = | E | N | A messenger who touches the sleeper and leaves bread and water is exactly what the Hebrew says; the reading adds only the identification of the messenger. |
| B-056 | TBWTT-3:120 | (I Rois, XIX, 11-12) → 1 Kgs 19:11b–12 | 1KI-WOH-19:11, 1KI-WOH-19:12 | supported | MORE | E | N | The sequence the reading uses — a passing presence preceded by rock-breaking wind, then shaking, then fire, then quiet — is Hebrew. |
| B-057 | TBWTT-3:122 | (I Rois, XXII-19) → 1 Kgs 22:19b | 1KI-WOH-22:19 | supported | = | E | N | A plurality of beings around a presiding, seated YHWH is the Hebrew's own picture, in military vocabulary (ṣəḇāʾ haššāmayim), and the French is literal. |
| B-058 | TBWTT-3:124 | (I Rois, XXII-22) → 1 Kgs 22:22a | 1KI-WOH-22:22, 1KI-WOH-22:21 | addition | = | E | N | The Hebrew has a volunteer from the council, called 'the rûaḥ', who undertakes to become a rûaḥ of falsehood in the mouths of all the king's prophets simultaneously. |
| B-059 | TBWTT-3:126 | II Rois, I-12 (prose reference in TBWTT-3:125) → 2 Kgs 1:12 | 2KI-WOH-1:12, 2KI-WOH-1:10 | supported | MORE |  | N | Fire descending from the sky on request, on Elijah's behalf, is the Hebrew as quoted. |
| B-060 | TBWTT-3:128 | (II Rois, I-15) → 2 Kgs 1:15a | 2KI-WOH-1:15 | no-reading | = | E | N | Quoted as narrative continuation; nothing depends on the wording. |
| B-061 | TBWTT-3:130 | (II Rois, II-1) → 2 Kgs 2:1a | 2KI-WOH-2:1 | supported | = | E | N | A bodily ascent to the sky, caused by another party, in a violent wind, is the Hebrew. |
| B-062 | TBWTT-3:132 | (II Rois, II-11) → 2 Kgs 2:11b | 2KI-WOH-2:11, 2KI-WOH-2:12 | supported | = | E | N | A fiery vehicle (reḵeḇ-ʾēš), fiery draught animals, and an ascent to the sky in a tempest are the Hebrew's own terms, rendered literally. |
| B-063 | TBWTT-3:134 | (II Rois, IV, 32-37) → 2 Kgs 4:32–37 (cited, not quoted) | 2KI-WOH-4:32, 2KI-WOH-4:33… | supported | = |  | N | This is the canon's best-supported medical reading in the slice: the Hebrew itself narrates mouth on mouth, the adult's body bent over the child's, the flesh warming, and a sevenfold sneeze before the eyes open. |
| B-064 | TBWTT-3:137 | (II Rois, IV, 42-44) → 2 Kgs 4:42–44 (condensed) | 2KI-WOH-4:42, 2KI-WOH-4:43… | contradicted | less | **S** |  | The numbers (twenty loaves, a hundred men, a surplus) are Hebrew and the canon's arithmetic follows from them. |
| B-065 | TBWTT-3:141 | (II Rois, XVII-23) → 2 Kgs 17:23b | 2KI-WOH-17:23 | supported | = | E | N | A historical reading and the Hebrew supports its core (exile as the consequence of the conduct listed in 2 Kgs 17:7–22). |
| C-001 | TBWTT-3:144 | (Isaïe, VI, 1-2) → Isa 6:1-2 | ISA-6:1, ISA-6:2 | addition | MORE | **S** |  | The hooks that are in the Hebrew are the number six, flight (yəʿôp̄ēp̄) and position above. |
| C-002 | TBWTT-3:146 | (Isaïe, XIII, 4-5) → Isa 13:4-5 | ISA-13:4, ISA-13:5 | supported | = |  | N | The load-bearing sentence is literally in the Hebrew and Dhorme's French adds nothing: a plural host "coming from a distant land, from the end of the skies", with YHWH and "implements of his wrath". |
| C-003 | TBWTT-3:148 | (Isaïe, XIV-13) → Isa 14:13 (part) | ISA-14:13 | supported | = | **S** | N | The hook "I will ascend to the skies" is literally Hebrew. |
| C-004 | TBWTT-3:150 | (Isaïe, XIV-14) → Isa 14:14 | ISA-14:14 | supported | less |  | N | The wish to be "like" (dmh) the Most High is the Hebrew text. |
| C-005 | TBWTT-3:152 | (Isaïe, XIV-17) → Isa 14:17a | ISA-14:17 | contradicted | less | **S** | N | As placed in the canon the sentence reads as what the destroying force did. |
| C-006 | TBWTT-3:154 | (Isaïe, XV, 8-9) → Isa 15:8-9a | ISA-15:8, ISA-15:9 | addition | less | **S** | N | Nothing in the Hebrew wording describes an explosion: the verses report a cry and a wailing spreading through named Moabite towns and water full of blood, inside an oracle headed "Moab" (15:1). |
| C-007 | TBWTT-3:156 | (Isaïe, XXVI-20) → Isa 26:20 | ISA-26:20 | supported | = |  |  | The textual hook — take shelter indoors, shut the doors, hide briefly until the wrath has passed — is exactly the Hebrew; "blockhaus" is the canon's modernisation of ḥăḏārîm "inner rooms". |
| C-013 | TBWTT-3:159 | (Ezéchiel, I, 4-14) → Ezek 1:4b-14 | EZK-WOH-1:4, EZK-WOH-1:5… | supported | = | **S** |  | Several hooks are original and Dhorme is close: a great cloud with self-renewing fire and a ḥašmal-gleam at its centre, four figures of human likeness, gleam "like burnished bronze", wings, hands under the wings, movemen |
| C-014 | TBWTT-3:160 | (Ezéchiel, I-15) → Ezek 1:15 | EZK-WOH-1:15 | supported | = |  |  | A separate disc-shaped object resting "on the earth" beside the figures is what the Hebrew says (ʾôp̄an "wheel", bāʾāreṣ). |
| C-015 | TBWTT-3:161 | (Ezéchiel, I, 16-21) → Ezek 1:16-21 | EZK-WOH-1:16, EZK-WOH-1:17… | supported | less | E |  | Wheel-shaped objects that rise from the ground with the figures (v.19, 21: וּבְהִנָּשֵׂא ... |
| C-016 | TBWTT-3:162 | (Ezéchiel, I, 22-26) → Ezek 1:22-26 | EZK-WOH-1:22, EZK-WOH-1:23… | supported | MORE | **S** |  | A solid surface above the figures, gleaming like ice, with a seat on it and a human-like figure on the seat, is the Hebrew text. |
| C-076 | TBWTT-3:163 | none → Ezek 1:7 (re-quotation, unreferenced) | EZK-WOH-1:7 | supported | MORE | **S** |  | The re-quotation differs from the canon's own first quotation of the verse (plural for singular) and in doing so comes closer to the Hebrew, whose participle is masculine plural and most naturally says that "they" gleame |
| C-077 | TBWTT-3:164 | none → Ezek 1:16-18 (re-quotation, unreferenced) | EZK-WOH-1:16, EZK-WOH-1:17… | supported | less | E |  | Eyes all round the rims is the Hebrew of 1:18. |
| C-017 | TBWTT-3:165 | (Ezéchiel, I-21) → Ezek 1:21b (= 1:20b) | EZK-WOH-1:21 | transl-dep | less | E |  | The step from "the spirit of the beings was in the wheels" to "other creators inside" is easier from the French plural "des êtres" than from the Hebrew, where a single rûaḥ of "the living creature" (the collective alread |
| C-018 | TBWTT-3:165 | (Ezéchiel, I-9) → Ezek 1:6a + 1:9b (conflated) | EZK-WOH-1:6, EZK-WOH-1:9 | transl-dep | less |  |  | The reference is partial: the first sentence is 1:6 and the second 1:9. |
| C-019 | TBWTT-3:166 | (Ezéchiel, I, 22 et 26) → Ezek 1:22, 26 | EZK-WOH-1:22, EZK-WOH-1:26 | supported | = | E |  | Same assessment as C-016. |
| C-020 | TBWTT-3:168 | (Ezéchiel, II, 1 et 8) → Ezek 2:1, 8 | EZK-WOH-2:1, EZK-WOH-2:8 | addition | = | E | N | That the eating is figurative is the text's own device (the thing eaten is a written scroll, 2:9-3:3), so the canon's "intellectual food" is a reading the Hebrew invites; the comparison with the tree of knowledge is adde |
| C-021 | TBWTT-3:170 | (Ezéchiel, II, 9-10) → Ezek 2:9-10a | EZK-WOH-2:9, EZK-WOH-2:10 | contradicted | less | **S** |  | The physical detail (opisthograph scroll) is original. |
| C-022 | TBWTT-3:171 | (Ezéchiel, III-3) → Ezek 3:3b | EZK-WOH-3:3 | addition | = | E | N | Sweetness on eating the scroll is the Hebrew text and the figurative sense of eating is internal to it. |
| C-023 | TBWTT-3:173 | (Ezéchiel, III, 14 et 12) → Ezek 3:14a + 3:12a | EZK-WOH-3:14, EZK-WOH-3:12… | supported | MORE | **S** | N | A lifting-and-carrying agent and a great rumbling noise behind the prophet are the Hebrew text. |
| C-024 | TBWTT-3:175 | (Ezéchiel, VIII-3) → Ezek 8:3 (middle) | EZK-WOH-8:3 | supported | less | **S** | N | Lifting "between earth and sky" and transport to Jerusalem are the Hebrew wording. |
| C-025 | TBWTT-3:178 | (Ezéchiel, X-8) → Ezek 10:8 | EZK-WOH-10:8, EZK-WOH-10:20 | supported | less |  |  | Human hands under the wings is the Hebrew text (also 1:8). |
| C-026 | TBWTT-3:179 | (Ezéchiel, X-19) → Ezek 10:19a | EZK-WOH-10:19 | supported | MORE | E |  | Take-off from the ground, witnessed, with the wheels rising alongside, is the Hebrew text; the French is literal. |
| C-027 | TBWTT-3:180 | (Ezéchiel, XI-1) → Ezek 11:1a | EZK-WOH-11:1 | addition | = | E | N | Lifting and carrying by rûaḥ is the Hebrew; the craft is the canon's identification. |
| C-028 | TBWTT-3:181 | (Ezéchiel, XI, 23-24) → Ezek 11:23-24a | EZK-WOH-11:23, EZK-WOH-11:24 | supported | less | **S** | N | The kāḇôḏ behaves in Hebrew as a located object: it "goes up" from over the city and "stands" on a mountain (the etymological sense "heaviness" is, if anything, more object-like than "gloire"). |
| C-029 | TBWTT-3:183 | (Ezéchiel, XXXVII-1) → Ezek 37:1 (middle) | EZK-WOH-37:1 | transl-dep | less | **S** |  | The wording "Iahvé me fit sortir" is not the Hebrew clause: the original has an unnamed subject who brings the prophet out "by/in the rûaḥ of YHWH" under "the hand of YHWH", the book's formula for visionary transport (cf |
| C-030 | TBWTT-3:185 | (Ezéchiel, XXXVII, 3, 7-8, 10) → Ezek 37:3a, 7b, 8a, 10b | EZK-WOH-37:3, EZK-WOH-37:7… | supported | less | **S** |  | The anatomical sequence the canon reads technically (bones, sinews, flesh, skin, standing alive) is the Hebrew text and Dhorme renders it literally. |
| C-031 | TBWTT-3:188 | (Ezéchiel, XL, 2-3) → Ezek 40:2-3a | EZK-WOH-40:2, EZK-WOH-40:3 | supported | less | **S** | N | A high mountain with city-like structures and a man of bronze-like appearance are the Hebrew text; the suit and the base are the canon's reading of a simile. |
| C-032 | TBWTT-3:191 | (Ezéchiel, XLII-14) → Ezek 42:14 (part) | EZK-WOH-42:14, EZK-WOH-44:19 | transl-dep | less | E | N | The explicit argument ("they should have written sains") is a French homophone and cannot be stated in Hebrew; on that point the reading is wholly translation-dependent. |
| C-078 | TBWTT-3:192 | none → Ezek 42:14 (altered re-quotation) | EZK-WOH-42:14 | transl-dep | less |  | N | A correction stated in French orthography ("Ils auraient dû écrire") about a text written in Hebrew; see C-032. |
| C-033 | TBWTT-3:194 | (Ezéchiel, XLIII-2) → Ezek 43:2 | EZK-WOH-43:2 | supported | = |  | N | The kāḇôḏ arrives from a compass direction, with a roar like great waters, and lights up the ground: all three properties are in the Hebrew, rendered literally. |
| C-034 | TBWTT-3:196 | (Ezéchiel, XLIV-2) → Ezek 44:2 | EZK-WOH-44:2 | addition | = | E | N | The Hebrew gives its own reason (the gate is closed because YHWH passed through it); "they did not want to be disturbed" is a motive supplied by the canon. |
| C-035 | TBWTT-3:198 | (Ezéchiel, XLIV-3) → Ezek 44:3a | EZK-WOH-44:3 | addition | = |  | N | The prince's exclusive access to the closed gate is in the Hebrew; that he comes "to confer" with the creators is added — the text has him eat there. |
| C-036 | TBWTT-3:200 | (Ezéchiel, XLIV-3) → Ezek 44:3b | EZK-WOH-44:3 | addition | = |  | N | An entrance hall through which the prince must both enter and leave is the Hebrew text. |
| C-037 | TBWTT-3:202 | (Ezéchiel, XLIV, 15-16) → Ezek 44:15b-16 | EZK-WOH-44:15, EZK-WOH-44:16 | supported | = | E | N | First-person singular speech about personal attendance (šrṯ) and "my table" is the Hebrew; the service reading has a real hook and the French is literal. |
| C-038 | TBWTT-3:203 | (Ezéchiel, XLIV, 17-18) → Ezek 44:17a, 18b | EZK-WOH-44:17, EZK-WOH-44:18 | supported | = | E | N | The sweat rule is explicit in Hebrew (bayyāzaʿ) and literally translated; the motive (smell disagreeable to the creators) is supplied — the Hebrew states the rule without a reason. |
| C-039 | TBWTT-3:205 | (Ezéchiel, XLIV, 30) → Ezek 44:30 | EZK-WOH-44:30 | addition | = | E | N | Delivery of first produce is the Hebrew, but both Hebrew and French name the priests as the recipients; that the food went on to the creators is the canon's inference (it reads the priests as their staff). |
| C-040 | TBWTT-3:208 | (Daniel, III-25) → Dan 3:25 (Aramaic; = 3:92 in Bibles that insert the Greek ad | DAN-WOH-3:25, DAN-WOH-3:28 | supported | = |  |  | The identity hook is in the Aramaic and Dhorme transmits it exactly: a fourth "man" whose look is that of a bar-ʾĕlāhîn, a member of the class of gods (plural), later called a sent malʾaḵ (3:28). |
| C-041 | TBWTT-3:210 | (Daniel, VI-23) → Dan 6:23a (Aramaic numbering; English 6:22) | DAN-WOH-6:23 | addition | = | E |  | A sent agent (malʾaḵ) and closed mouths are the Aramaic; the paralysing ray is supplied. |
| C-042 | TBWTT-3:212 | (Daniel, X, 5-6) → Dan 10:5a, 6 | DAN-WOH-10:5, DAN-WOH-10:6 | supported | less | **S** |  | A "man" (ʾîš) with a gem-like body, lightning-like face and limbs like burnished bronze is the Hebrew text, and the bronze phrase is verbatim the one used of Ezekiel's creatures — an intertext that is real in Hebrew but  |
| C-043 | TBWTT-3:216 | none → Dan 10:13 (unreferenced) | DAN-WOH-10:13, DAN-WOH-10:21… | contradicted | less | **S** |  | This is the clearest case in the slice of an ellipsis producing the reading. |
| C-044 | TBWTT-3:218 | (Daniel, XII-2) → Dan 12:2 | DAN-WOH-12:2 | supported | = |  |  | A selective awakening ("many of") of the dead from the ground to two lasting fates is the Hebrew, rendered literally. |
| C-045 | TBWTT-3:220 | (Daniel, XII-3) → Dan 12:3 | DAN-WOH-12:3 | transl-dep | less | E |  | The step maśkîlîm → "gens intelligents" → "génies" is carried by the French: the Hebrew participle denotes the wise who instruct (parallel to "those who turn many to righteousness"), a moral-didactic category rather than |
| C-046 | TBWTT-3:222 | (Daniel, XII-4) → Dan 12:4 | DAN-WOH-12:4 | supported | = |  |  | The reading's two pillars — sealing "until the time of the end" and an increase of knowledge then — are both explicit in the Hebrew; this is one of the strongest textual hooks in the slice and owes nothing to the French. |
| C-047 | TBWTT-3:224 | (Daniel, XII-7) → Dan 12:7 (one clause) | DAN-WOH-12:7 | supported | = | E |  | The clause is literally the Hebrew. |
| C-048 | TBWTT-3:226 | (Daniel, XII-9) → Dan 12:9 | DAN-WOH-12:9 | supported | = |  |  | Literal Hebrew; the identification of "the time of the end" with the present is the canon's. |
| C-049 | TBWTT-3:229 | (Jonas, II-1) → Jonah 2:1 (Hebrew numbering; English 1:17) | JNA-WOH-2:1 | addition | MORE |  | N | Nothing in the Hebrew nouns suggests a vessel (dāḡ "fish", mēʿîm "innards", blʿ "swallow"). |
| C-050 | TBWTT-3:231 | (Jonas, II-11) → Jonah 2:11 (Hebrew numbering; English 2:10) | JNA-WOH-2:11 | addition | less |  | N | Speech addressed to the fish (a hook for "a crew receiving instructions") is in the Hebrew. |
| C-051 | TBWTT-3:234 | (Zacharie, V, 1-2) → Zech 5:1-2 | ZEC-WOH-5:1, ZEC-WOH-5:2… | contradicted | less | **S** | N | A flying object with stated dimensions is the Hebrew (and the 2:1 ratio is real), but the noun is "scroll" — the same mәḡillāh the canon reads as an ordinary book in Ezek 2:9 — and the text explains it in the next verse  |
| C-052 | TBWTT-3:237 | (Zacharie, V-9) → Zech 5:9a | ZEC-WOH-5:9, ZEC-WOH-5:8 | supported | = | **S** | N | Two winged women in flight are the Hebrew, literally rendered. |
| C-054 | TBWTT-3:239 | (Psaumes, VIII-6) → Ps 8:6a (Hebrew numbering; English 8:5) | PSA-WOH-8:6 | supported | = | E | N | The comparison of the human with ʾĕlōhîm (not with angels) is the Hebrew wording and Dhorme keeps it; the plural article "aux" is the French's resolution of an anarthrous noun. |
| C-055 | TBWTT-3:241 | (Psaumes, XIX-7) → Ps 19:7a (Hebrew numbering; English 19:6) | PSA-WOH-19:7, PSA-WOH-19:6 | contradicted | less | **S** | N | In Hebrew the sentence describes the sun's daily course from one horizon to the other; the antecedent (v.5c "for the sun", v.6 "he is like a bridegroom") and the closing "nothing is hidden from his heat" are exactly what |
| C-056 | TBWTT-3:243 | (Psaumes, XIX-5) → Ps 19:5c (Hebrew numbering; English 19:4c) | PSA-WOH-19:5 | transl-dep | less | **S** | N | The single word the reading rests on — "mer" — is absent from the Masoretic text, which reads bāhem "in them"; the French follows an emendation. |
| C-057 | TBWTT-3:246 | (Psaumes, XXXIII, 13-14) → Ps 33:13-14 | PSA-WOH-33:13, PSA-WOH-33:14 | supported | = | E | N | Observation of all humans from the skies, from an established dwelling-place, is the Hebrew and is literally rendered. |
| C-061 | TBWTT-3:250 | (Job, I-6) → Job 1:6 | JOB-WOH-1:6, JOB-WOH-1:7 | supported | MORE |  |  | The scene the canon describes — a plurality of beings of the Elohim class reporting to a presiding YHWH, with an opposition figure among them — is the plain narrative of the Hebrew. |
| C-062 | TBWTT-3:252 | (Job, I, 9, 11-12) → Job 1:9, 11, 12a | JOB-WOH-1:9, JOB-WOH-1:11… | supported | = | E |  | Delegated authority with a stated limit ("only against him do not put out your hand") is the Hebrew text; the political vocabulary (government, opposition, full powers) is the canon's, assisted by Dhorme's "à ta discréti |
| C-063 | TBWTT-3:255 | (Job, II-6) → Job 2:6 | JOB-WOH-2:6 | supported | = | E |  | Literal Hebrew; the reading only restates it in political terms. |
| C-064 | TBWTT-3:259 | (Job, XXXVII-18) → Job 37:18 | JOB-WOH-37:18 | supported | MORE | E | N | The metallic hook is stronger in Hebrew than in the French the canon quotes: the verb is rqʿ, "to hammer out (metal)", and the comparison is to a cast-metal mirror, hard (ḥăzāqîm). |
| C-065 | TBWTT-3:264 | (Tobit, XII, 19-20) → Tobit 12:19-20 (Greek, short text GI) | TOB-WOH-12:19, TOB-WOH-12:20 | supported | = | **S** | N | Greek, not Hebrew. |
| C-066 | TBWTT-3:266 | (La sagesse de Salomon, VI-22) → Wisdom 6:22 | WIS-WOH-6:22 | addition | = |  | N | The promise to disclose the origin of wisdom and hide no mysteries is the Greek; equating sophia with the creators' science, and the speaker's promise (Solomon to his readers) with a future revelation, is the canon's. |
| C-067 | TBWTT-3:268 | (Sagesse de Salomon, XIII-5) → Wisdom 13:5 | WIS-WOH-13:5 | supported | = |  | N | Greek. |
| C-068 | TBWTT-3:270 | (Sagesse de Salomon, XIII-1) → Wisdom 13:1 (middle clause) | WIS-WOH-13:1 | supported | MORE | E | N | Greek. |
| C-008 | TBWTT-3:272 | (Isaïe, XXVII-1) → Isa 27:1 | ISA-27:1 | supported | = | E |  | The reading's lexical chain is original: nāḥāš (the Eden serpent word) and tannîn (the Gen 1:21 "dragons" word) both stand in the Hebrew verse, the creature is located "in the sea", and YHWH is its enemy. |
| C-009 | TBWTT-3:274 | (Isaïe, XXIX-12) → Isa 29:12 | ISA-29:12 | supported | MORE | **S** | N | The illiteracy image is the Hebrew text. |
| C-069 | TBWTT-3:276 | (Jérémie, X-14) → Jer 10:14a | JER-WOH-10:14 | transl-dep | less | **S** | N | The move from the verse to "Cette science qui a permis aux créateurs de créer" runs through the French word "science". |
| C-070 | TBWTT-3:278 | (Proverbes, VIII, 22-23, 27, 29-31) → Prov 8:22-23, 27a, 29a, 30a, 31 | PRO-WOH-8:22, PRO-WOH-8:23… | supported | = | E | N | That wisdom was present and active at the making of sky, sea-limit and earth is the Hebrew text. |
| C-071 | TBWTT-3:280 | (L’Ecclésiaste, III-15) → Eccl 3:15a | ECC-WOH-3:15 | supported | = | E | N | Recurrence ("what is to be has already been") is the Hebrew; applying it to successive creations of humanities is the canon's. |
| C-072 | TBWTT-3:282 | (L’Ecclésiaste, III-19) → Eccl 3:19b | ECC-WOH-3:19 | addition | = | **S** | N | The no-advantage statement is literal Hebrew. |
| C-010 | TBWTT-3:285 | (Isaïe, XLV, 9-10) → Isa 45:9-10a | ISA-45:9, ISA-45:10 | supported | = | E | N | The maker-as-potter and maker-as-father images are the Hebrew text (yṣr, ʾāḇ), so the hook for "love us as fathers" is original. |
| C-011 | TBWTT-3:286 | (Isaïe, XLVIII, 10-11) → Isa 48:10b-11a | ISA-48:10, ISA-48:11 | transl-dep | less | E | N | Both words the commentary builds on are French-side. |
| C-012 | TBWTT-3:289 | (Isaïe, XL-21) → Isa 40:21 | ISA-40:21 | supported | MORE |  | N | The canon's French takes "the foundations of the earth" as the direct object of "understood", which is what the Masoretic consonants say without supplement; the library's own line supplies "from". |
| C-073 | TBWTT-3:291 | (Amos, IV-13) → Amos 4:13 (one participial clause) | AMO-WOH-4:13 | addition | = | E | N | Treading on the earth's heights is the Hebrew; a single figure walks there, and no installation is mentioned. |
| C-053 | TBWTT-3:293 | (Zacharie, IV-10) → Zech 4:10b | ZEC-WOH-4:10, ZEC-WOH-4:2 | supported | MORE | E | N | The canon's link between the number seven, YHWH's means of observing the earth, and the lampstand is not its invention: in the Hebrew of this chapter the seven lamps of the golden menorah (4:2) are explained as "the eyes |
| C-058 | TBWTT-3:296 | (Psaumes, CXXXIX, 4-6) → Ps 139:4-6 (Hebrew numbering; Vulgate/LXX 138) | PSA-WOH-139:4, PSA-WOH-139:5… | supported | MORE |  | N | That the addressee knows the psalmist's words unspoken is in the Hebrew of v.4, though the "not yet ... |
| C-059 | TBWTT-3:299 | (Psaumes, CXLVII, 4-5) → Ps 147:4-5 (Hebrew numbering) | PSA-WOH-147:4, PSA-WOH-147:5 | addition | = |  | N | Counting and naming the stars is the Hebrew; travel between them is not mentioned in either language. |
| C-060 | TBWTT-3:301 | (Psaumes, CXLVII-15) → Ps 147:15 (Hebrew numbering) | PSA-WOH-147:15, PSA-WOH-147:18 | supported | = | **S** | N | A word that is "sent" to the earth and "runs very swiftly" is the Hebrew image, and šlḥ ("send, dispatch") is if anything closer to transmission than the French "adresse". |
| C-074 | TBWTT-3:303 | (Michée, V, 1-4) → Mic 5:1, 3, 4a (Hebrew numbering; English 5:2, 4, 5a) | MIC-WOH-5:1, MIC-WOH-5:2… | addition | = | E | N | A ruler from Bethlehem with ancient origins whose greatness reaches the ends of the earth is the Hebrew. |
| C-075 | TBWTT-3:304 | (Zacharie, IX, 9-10) → Zech 9:9-10 (excerpts) | ZEC-WOH-9:9, ZEC-WOH-9:10 | addition | = | E | N | Traditional messianic proof-text quoted in excerpts; no technological reading and no French-dependent hook. |
| D-001 | TBWTT-4:4 | (Mathieu, I-18) → Matt 1:18 | MAT-WOH-1:18 | addition | = | E |  | Greek and French agree that the pregnancy has a non-human source named pneuma hagion. |
| D-002 | TBWTT-4:6 | (Matthieu, I20) → Matt 1:20 | MAT-WOH-1:20 | addition | less | **S** |  | The Greek frames the appearance as a dream (κατ' ὄναρ); the canon's excerpt omits those words and paraphrases with « vient ». |
| D-003 | TBWTT-4:9 | (Matthieu, II-2) → Matt 2:2 | MAT-WOH-2:2 | addition | = | E | N | In 2:2 the Greek has only 'his star at its rising'; nothing in the wording of this verse marks the object as other than a star. |
| D-004 | TBWTT-4:10 | (Matthieu, II-9) → Matt 2:9 | MAT-WOH-2:9 | supported | = | E | N | The behaviour the canon relies on — a light that leads on the ground-track of travellers, then comes and halts over a specific spot — is fully in the Greek (προῆγεν … ἐλθὼν ἐστάθη ἐπάνω). |
| D-005 | TBWTT-4:14 | (Matthieu, II-13) → Matt 2:13 | MAT-WOH-2:13 | addition | = | E | N | Wording neutral in both languages: a messenger appears in a dream and gives a warning. |
| D-006 | TBWTT-4:16 | (Matthieu, II, 19-20) → Matt 2:19-20 | MAT-WOH-2:19, MAT-WOH-2:20 | addition | = | E | N | Neutral wording; same pattern as 2:13. |
| D-007 | TBWTT-4:19 | (Mathieu, III, 16-17 et IV-I) → Matt 3:16-17; 4:1 | MAT-WOH-3:16, MAT-WOH-3:17… | supported | MORE | **S** | N | The passive 'was led up … to be tested' is in the Greek, and two Greek words are closer to the canon's reading than the quoted French: ἀνήχθη is 'led up' (not merely 'taken'), and διάβολος/πειρασθῆναι are literally 'the  |
| D-008 | TBWTT-4:22 | (Matthieu IV-24) → Matt 4:24 | MAT-WOH-4:24 | supported | = | **S** | N | The medical register is in the Greek (κακῶς ἔχοντας 'being ill', νόσοις, ἐθεράπευσεν 'treated'), and the French follows it. |
| D-009 | TBWTT-4:23 | (Matthieu, V-3) → Matt 5:3 | MAT-WOH-5:3 | contradicted | less | E |  | This is one of the few places where the canon makes an explicit claim about the original wording. |
| D-010 | TBWTT-4:25 | none → Matt 6:9 (the 'Our Father' named) | MAT-WOH-6:9 | supported | = |  |  | Allusion without reference; introduces the 6:10 quotation. |
| D-011 | TBWTT-4:26 | (Matthieu, VI-10) → Matt 6:10 | MAT-WOH-6:10 | supported | = |  |  | The comparison 'as in heaven, so on earth' and βασιλεία as 'reign' are in the Greek; the French transmits both (with the clause order reversed). |
| D-012 | TBWTT-4:29 | (Matthieu, VII, 28-29) → Matt 7:28-29 | MAT-WOH-7:28, MAT-WOH-7:29 | addition | = |  |  | The Greek reports astonishment at teaching 'with authority, not like their scribes' — a contrast of teaching style and warrant. |
| D-013 | TBWTT-4:31 | (Matthieu, VIII, 2-3) → Matt 8:2-3 | MAT-WOH-8:2, MAT-WOH-8:3 | addition | = | E | N | The Greek has a touch, a word and an immediate passive result. |
| D-014 | TBWTT-4:33 | (Matthieu, IX, 5, 7) → Matt 9:5, 7 | MAT-WOH-9:5, MAT-WOH-9:7… | addition | = | **S** | N | No wording in 9:2–7 relates to a mechanism; the reading is added. |
| D-015 | TBWTT-4:34 | (Matthieu, IX-13) → Matt 9:13 | MAT-WOH-9:13, MAT-WOH-15:24… | contradicted | less | E |  | French and Greek agree on the saying. |
| D-016 | TBWTT-4:38 | (Matthieu, X-32) → Matt 10:32 | MAT-WOH-10:32 | supported | = |  | N | The locative phrase the canon leans on ('in the heavens', plural) is the Greek wording, and the French reproduces it. |
| D-017 | TBWTT-4:43 | (Matthieu, XIII-3) → Matt 13:3 | MAT-WOH-13:3, MAT-WOH-13:19 | addition | less | **S** | N | The Greek wording of 13:3 is neutral, and the French matches it. |
| D-018 | TBWTT-4:45 | (Matthieu, XIII-4) → Matt 13:4 | MAT-WOH-13:4, MAT-WOH-13:19 | addition | = | E |  | Wording neutral. |
| D-019 | TBWTT-4:46 | (Matthieu, XIII, 5-6) → Matt 13:5-6 | MAT-WOH-13:5, MAT-WOH-13:6 | addition | less | **S** |  | The sun's scorching is in the Greek, but as a secondary agent: the Greek twice gives the cause as lack of depth and root, and both clauses fall inside the canon's ellipses. |
| D-020 | TBWTT-4:47 | (Matthieu, XIII-7) → Matt 13:7 | MAT-WOH-13:7 | addition | = | E |  | Plants choking the crop is the Greek image; the planetary application and humidity are added. |
| D-021 | TBWTT-4:48 | (Matthieu, XIII, 8-9) → Matt 13:8-9 | MAT-WOH-13:8, MAT-WOH-13:9 | supported | = |  |  | The structural hooks — three failures followed by a success that comes in three grades — are in the Greek, and γῆ ('earth' as well as 'soil') permits the 'world' sense as readily as French « terre ». |
| D-022 | TBWTT-4:54 | (Matthieu, XIII-11) → Matt 13:11 | MAT-WOH-13:11 | addition | = | E |  | Wording identical in substance. |
| D-068 | TBWTT-4:55 | none → 'Last judgement' (Matthean judgement scenes, e.g. Matt 13:49 | MAT-WOH-13:49 | not-checkable | = |  |  | A church-tradition term in scare quotes, not a quotation; no verse to compare. |
| D-023 | TBWTT-4:56 | (Matthieu, XIII-32) → Matt 13:32 | MAT-WOH-13:32, MAT-WOH-13:31 | supported | MORE | **S** |  | For the detail the reading uses, the Greek is slightly more open than the French: κατασκηνοῦν is 'to encamp, settle' — a word for people taking up residence — where « nicher » can only be said of birds, and πετεινὰ τοῦ ο |
| D-024 | TBWTT-4:58 | (Matthieu, XIII-33) → Matt 13:33 | MAT-WOH-13:33 | supported | = | E |  | The numeral is real and the French keeps it. |
| D-025 | TBWTT-4:60 | (Matthieu, XIII-35) → Matt 13:35 | MAT-WOH-13:35 | transl-dep | less | E |  | The canon's comment turns on 'the world' (planets have a life-span). |
| D-026 | TBWTT-4:63 | (Matthieu, XIII-49) → Matt 13:49 | MAT-WOH-13:49, MAT-WOH-13:50 | supported | = | E |  | αἰών 'age' is the Greek word, and the French the canon quotes already renders it as age rather than 'world' — a point where the original supports the canon's age-vocabulary against the common French Bibles, though the Gr |
| D-027 | TBWTT-4:64 | none → Matt 14:15-21 (feeding of the five thousand) | MAT-WOH-14:19, MAT-WOH-14:20 | addition | less |  |  | Unreferenced allusion. |
| D-028 | TBWTT-4:67 | (Matthieu, XIV-25) → Matt 14:25 | MAT-WOH-14:25 | addition | = | E | N | The Greek reports the fact without mechanism; the ray is added. |
| D-029 | TBWTT-4:69 | (Matthieu, XIV, 30, 32) → Matt 14:30, 32 | MAT-WOH-14:30, MAT-WOH-14:32… | contradicted | less | **S** | N | The cessation of wind on boarding is in the Greek (and the aorist participle fits the canon's 'once he was in the boat' better than the French imperfect). |
| D-030 | TBWTT-4:74 | (Matthieu, XVII, 1-3, 5) → Matt 17:1-3, 5 | MAT-WOH-17:1, MAT-WOH-17:2… | supported | = | E | N | The luminous cloud that comes over the group and the voice from inside it are the Greek wording (νεφέλη φωτεινή, ἐκ τῆς νεφέλης), and ἐπεσκίασεν 'overshadowed' is slightly more spatial than « couvrit ». |
| D-031 | TBWTT-4:77 | (d’après Matthieu, XIX-30) → Matt 19:30 (wording nearer 20:16) | MAT-WOH-19:30 | addition | less | **S** | N | A reversal of rank is the Greek sense; the cyclical 'created become creators' is added, and the Greek's 'many' is less general than the canon's wording. |
| D-032 | TBWTT-4:87 | none (TBWTT-4:79: « Au chapitre XXV (v. 14 à 29) de l’Évangile selon Matthieu ») → Matt 25:14-29 (paraphrase 25:14-27; direct quotation 25:28-2 | MAT-WOH-25:14, MAT-WOH-25:15… | supported | = | E |  | The triad the canon builds on is in the Greek (three slaves, three allotments, a reckoning on the master's return). |
| D-033 | TBWTT-4:91 | (Matthieu, XXVI, 52-53) → Matt 26:52-53 | MAT-WOH-26:52, MAT-WOH-26:53 | supported | = | E | N | The military image — a father who can dispatch organised units of messengers on request — is in the Greek and survives intact in French. |
| D-034 | TBWTT-4:92 | (Matthieu, XXVI-54) → Matt 26:54 | MAT-WOH-26:54 | addition | = |  | N | In the Greek the 'writings' are prior scriptures whose predictions must be fulfilled; the canon reads the sentence as a statement about the future utility of the biblical and gospel record. |
| D-035 | TBWTT-4:95 | (Matthieu, XXVIII, 2-3) → Matt 28:2-3 | MAT-WOH-28:2, MAT-WOH-28:3… | supported | MORE | E |  | The descent from the sky, the shaking and the lightning-like figure are the Greek wording. |
| D-036 | TBWTT-4:97 | (Matthieu, XXVIII, 19-20) → Matt 28:19-20 | MAT-WOH-28:19, MAT-WOH-28:20 | addition | less | **S** |  | The universal mission (πάντα τὰ ἔθνη) is Greek. |
| D-037 | TBWTT-4:99 | (Marc, XVI-19) → Mark 16:19 | MRK-WOH-16:19 | supported | = | **S** | N | The agentless passive 'was taken up into the sky' is the Greek, and the French reproduces it; the canon supplies 'the creators' as agent. |
| D-038 | TBWTT-4:100 | (Marc, XVI-18) → Mark 16:18 | MRK-WOH-16:18, MRK-WOH-16:17 | contradicted | less | **S** | N | The reading as a date-marker depends on the bracketed lead-in, which is neither in the French Bible nor in the Greek. |
| D-039 | TBWTT-4:103 | (d’après Luc, XXI, 29-30) → Luke 21:29-30 | LUK-WOH-21:29, LUK-WOH-21:30 | addition | = | E |  | A sign-of-the-season analogy in both languages; what the 'buds' stand for is supplied by the canon. |
| D-040 | TBWTT-4:106 | (Actes des Apôtres, II, 1-4) → Acts 2:1-4 | ACT-WOH-2:1, ACT-WOH-2:2… | supported | = | E |  | Every observable the reading uses is in the Greek: a sudden noise from the sky filling the house, a fire-like something distributed onto each individual, immediate speech in other languages. |
| D-041 | TBWTT-4:109 | (Actes des apôtres, XII, 7-9) → Acts 12:7-9 | ACT-WOH-12:7, ACT-WOH-12:8… | supported | = |  |  | The canon's methodological point — the narrator distinguishes what the witness took for a vision from what was real — is exactly what the Greek says (ἀληθές … ἐδόκει δὲ ὅραμα βλέπειν), and the French renders it without l |
| D-042 | TBWTT-4:112 | (Actes des apôtres, XII-10) → Acts 12:10 | ACT-WOH-12:10 | supported | = | E |  | The self-opening iron gate is the Greek wording (αὐτομάτη). |
| D-043 | TBWTT-4:114 | (Actes des apôtres, XV-16) → Acts 15:16 (citing Amos 9:11) | ACT-WOH-15:16, ACT-WOH-15:17… | addition | less | **S** |  | The words 'I will return and rebuild the fallen tent of David' are in the Greek. |
| D-044 | TBWTT-4:116 | (Actes des apôtres, XVII-28) → Acts 17:28 | ACT-WOH-17:28 | supported | MORE | **S** |  | γένος is a kinship word — 'stock, race' — and the French « race » renders it literally where many versions weaken it to 'offspring'; the Greek gives the canon's literal-kinship reading a real lexical footing. |
| D-045 | TBWTT-5:6 | (Sophonie, I-10) → Zeph 1:10 | ZEP-WOH-1:10, ZEP-WOH-1:11 | supported | less | **S** | N | The lexical hook is real and not a French artefact: שַׁעַר הַדָּגִים is 'the gate of the fishes', plural, exactly as « Porte des Poissons ». |
| D-046 | TBWTT-5:11 | (Isaïe, XXIX, 20-21) → Isa 29:20-21 | ISA-29:20, ISA-29:21 | supported | MORE |  | N | Two things can be said in opposite directions. |
| D-047 | TBWTT-5:13 | (Isaïe, XXXII, 3, 5) → Isa 32:3, 5 | ISA-32:3, ISA-32:5 | addition | = | E | N | Prophetic application; no technological re-reading. |
| D-048 | TBWTT-5:15 | (Isaïe, XXXII, 6-8) → Isa 32:6-8 | ISA-32:6, ISA-32:7… | contradicted | less |  |  | Application to the Church is added. |
| D-049 | TBWTT-5:17 | (Isaïe, XL-21) → Isa 40:21 | ISA-40:21 | supported | MORE |  | N | The canon's French takes 'the foundation(s) of the earth' as the thing to be understood. |
| D-050 | TBWTT-5:18 | (Isaïe, XLII-1) → Isa 42:1 | ISA-42:1 | addition | = |  | N | Identification of the servant is supplied; the Hebrew leaves him unnamed (library note). |
| D-051 | TBWTT-5:20 | (Isaïe, XLII-3) → Isa 42:3 | ISA-42:3 | addition | less | E | N | Wording agrees. |
| D-052 | TBWTT-5:21 | none → (doctrinal statement on Elohim / Eloha, no verse) | ISA-43:12 | supported | = |  |  | Not a quotation; recorded because it states the canon's translation principle beside quotations that test it. |
| D-053 | TBWTT-5:23 | (Isaïe, XLIV-19) → Isa 44:19 | ISA-44:19 | addition | = |  | N | 'A block of wood' one bows to is the Hebrew; the cross is an application the canon supplies (the passage, vv. |
| D-054 | TBWTT-5:25 | (Isaïe, XLIII, 5-7) → Isa 43:5-7 | ISA-43:5, ISA-43:6… | supported | = | E | N | The gathering from four directions is the Hebrew, and the French is close. |
| D-055 | TBWTT-5:26 | (Isaïe, XLIII-10) → Isa 43:10 | ISA-43:10 | supported | = | E | N | The address to Israel as witnesses is the Hebrew. |
| D-056 | TBWTT-5:27 | (Isaïe, XLIII, 8-9) → Isa 43:8-9 | ISA-43:8, ISA-43:9 | no-reading | = |  | N | Quoted as part of the witness theme without a specific technological or historical reading. |
| D-057 | TBWTT-5:28 | (Isaïe, XLIII, 10, 12-13) → Isa 43:10, 12-13 | ISA-43:10, ISA-43:11… | transl-dep | less | **S** | N | Two findings. |
| D-058 | TBWTT-5:30 | (Isaïe, LIV-7) → Isa 54:7 | ISA-54:7 | supported | = |  | N | Abandonment followed by regathering is the Hebrew. |
| D-059 | TBWTT-5:33 | (Isaïe, LXV-20) → Isa 65:20 | ISA-65:20 | supported | = | E | N | The end of infant death and premature death is the Hebrew wording. |
| D-060 | TBWTT-5:35 | (Proverbes, X-13) → Prov 10:13 | PRO-WOH-10:13 | no-reading | = |  | N | Moral maxim, literal French. |
| D-061 | TBWTT-5:38 | (Matthieu, VI-7) → Matt 6:7 | MAT-WOH-6:7 | no-reading | = |  |  | Moral/polemical use; French matches the Greek. |
| D-062 | TBWTT-5:40 | (Matthieu, VI, 24 et 19) → Matt 6:24, 19 | MAT-WOH-6:24, MAT-WOH-6:19 | no-reading | = | E |  | Moral use; the French is a close, literal rendering of the Greek. |
| D-063 | TBWTT-5:41 | (Matthieu, X, 9-10) → Matt 10:9-10 | MAT-WOH-10:9, MAT-WOH-10:10 | transl-dep | less | **S** | N | The polemical point (clergy must own nothing) leans on « possédez »; the Greek verb is 'acquire', in a charge for a specific journey, and the verse ends — in the part cut — by affirming that the worker deserves his keep. |
| D-064 | TBWTT-5:43 | (Matthieu, XV-11) → Matt 15:11 | MAT-WOH-15:11 | no-reading | = |  | N | Moral/polemical use; French exact. |
| D-065 | TBWTT-5:46 | (Matthieu, XIX-23) → Matt 19:23 | MAT-WOH-19:23 | no-reading | = |  | N | Moral use; French close to the Greek. |
| D-066 | TBWTT-5:47 | (Matthieu, XXIII, 4-11) → Matt 23:4-11 | MAT-WOH-23:4, MAT-WOH-23:5… | no-reading | = | **S** | N | Polemical application, no technological reading. |
| D-070 | TBWTT-5:65 | none → Gen 19:24-25 (Sodom and Gomorrah) as a threat formula | GEN-WOH-19:24 | no-reading | = |  |  | Allusion by name; nothing to compare beyond the names. |
| D-067 | TBWTT-6:13 | (Lévitique, XXV, 8, 14-16, 23) → Lev 25:8, 14-16, 23 | LEV-WOH-25:8, LEV-WOH-25:14… | supported | less | **S** | N | No technological reading; a socio-legal precedent. |
| D-069 | TBWTT-7:13 | none → Gen 2:9; 3:22 ('tree of life'), re-used | GEN-WOH-3:22 | addition | = |  |  | Allusion; the Genesis slice (fork A) carries the full comparison. |
| D-074 | ETTMTTP-2:50 | none → Moses and Elijah alive (cf. Matt 17:3; 2 Kgs 2:11); no verse | MAT-WOH-17:3 | addition | = |  |  | Doctrinal statement resting on Matt 17:3 as read in TBWTT-4:75. |
| D-071 | ETTMTTP-2:72 | (Ezéchiel, XXVII, 3, 7-8, 10) → Ezek 37:3, 7-8, 10 | EZK-WOH-37:3, EZK-WOH-37:7… | supported | less | **S** |  | The sequence the canon matches to the re-creation machine — noise, then sinews, flesh, skin layered onto bones, then standing figures — is the Hebrew sequence, and the noise is doubly marked (qôl, raʿaš), so the hook is  |
| D-073 | ETTMTTP-2:104 | none → Gen 6:1-4 ('sons of Elohim and daughters of men'); no verse  | GEN-WOH-6:2, GEN-WOH-6:4 | addition | less |  |  | The phrase is quoted accurately. |
| D-072 | ETTMTTP-2:111 | (Matthieu, XXVII, 42-43) → Matt 27:42-43 | MAT-WOH-27:42, MAT-WOH-27:43 | no-reading | = | E | N | Illustrative quotation, no re-reading. |
| D-075 | ETTMTTP-3:116 | none → Matt 6:9-13 (the Lord's Prayer), named | MAT-WOH-6:9, MAT-WOH-6:10 | addition | = |  |  | Allusion. |
| E-001 | LWTE-1:4 | (Exode, XXXIII, 20) → Exod 33:20 | EXO-WOH-33:20 | addition | = |  |  | Nothing in the Hebrew (rāʾâ 'see', pānîm 'face', ḥāy 'live') refers to atmosphere, breathing or a suit; the wording is neutral and the atmospheric reading is supplied by TBWTT. |
| E-047 | LWTE-1:10 | none → ἀποκάλυψις (Rev 1:1) | REV-WOH-1:1 | supported | = |  |  | Correct: apokalypsis is 'uncovering, revelation' and the library renders it so. |
| E-055 | LWTE-1:17 | none ("dont il est question dans la Genèse") → Gen 6:2, 6:4 | GEN-WOH-6:2, GEN-WOH-6:4… | addition | = |  |  | Gen 6:2-4 supports the unions and offspring; it names neither Israel nor any people (the daughters are 'of hāʾādām', humankind), so the Jewish-descent claim is added — Raël hedges it himself («peut-être»). |
| E-002 | LWTE-1:20 | (Matthieu, VI, 24 & 19) → Matt 6:24, 6:19a | MAT-WOH-6:24, MAT-WOH-6:19 | no-reading | = | E |  | Quoted (by the questioner, from TBWTT) as an ethical maxim; the French is literal to the Greek. |
| E-056 | LWTE-1:64 | none → Gen 1:26-27 | GEN-WOH-1:26, GEN-WOH-1:27 | supported | = |  |  | 'Leur image' has a genuine Hebrew plural behind it in the speech of 1:26 ('our image, our likeness', with a plural verb) and a singular against it in the narration of 1:27 (singular verb wayyiḇrāʾ, singular suffix bəṣalm |
| E-003 | LWTE-1:69 | (Genèse, IX, 4 et 5.) → Gen 9:4-5 | GEN-WOH-9:4, GEN-WOH-9:5 | supported | MORE |  |  | The textual hook is real and is Hebrew, not French: the same noun nep̄eš is predicated of animal flesh (9:4) and of the human (9:5) and is tied to blood. |
| E-004 | LWTE-1:69 | (Lévitique, XVII, 11.) → Lev 17:11a | LEV-WOH-17:11 | supported | MORE | E | N | The clause quoted is a literal rendering and the hook (nep̄eš located in blood) is in the Hebrew. |
| E-005 | LWTE-2:8 | en Matthieu, XIII, 3 et 4 (inline, not in the citation index) → Matt 13:3b-4 | MAT-WOH-13:3, MAT-WOH-13:4… | addition | MORE | **S** | N | The planetary reading of sower/seed/path is supplied by the canon; the Greek is an agricultural scene of one sowing. |
| E-006 | LWTE-2:14 | (Matthieu, XIII, 5 à 9.) → Matt 13:5-9 | MAT-WOH-13:5, MAT-WOH-13:6… | addition | = |  | N | Each element the canon decodes is present in the Greek (sun, thorns, good soil, three yields), and the French is literal; the planetary referents are supplied. |
| E-049 | LWTE-2:21 | none → Latin lucifer; cf. Isa 14:12 הֵילֵל | ISA-14:12 | transl-dep | less |  |  | The Latin etymology (lux + ferre) is correct, but the name exists only in translation: it enters the tradition as the Vulgate's rendering of hêlēl in Isa 14:12, where the Hebrew is an epithet ('shining one, son of dawn') |
| E-057 | LWTE-2:24 | none ("est-il écrit poétiquement") → Gen 3:14 | GEN-WOH-3:14 | addition | less |  |  | The exile reading hangs on the paraphrase 'ramper sur la Terre'; the Hebrew curse is 'on your belly you shall go' and classes the nāḥāš among the animals ('cursed above all cattle and every beast of the field'), with a s |
| E-048 | LWTE-2:31 | none → διάβολος (Matt 4:1) | MAT-WOH-4:1 | supported | MORE |  | N | The etymology is right and the library glossary confirms it. |
| E-007 | LWTE-2:33 | (Matthieu, IV, 1.) → Matt 4:1 | MAT-WOH-4:1 | supported | MORE | **S** | N | Both lexical hooks are Greek: diabolos does mean 'slanderer', and peirazō does mean 'test' — the Greek goes further than the quoted verse, since 4:3 calls the figure ho peirazōn, 'the tester', a participle LWTE's quotati |
| E-008 | LWTE-2:36 | (Matthieu, IV, 3 et 4.) → Matt 4:3b-4 | MAT-WOH-4:3, MAT-WOH-4:4 | addition | MORE | E | N | The saying is quoted accurately; the reading 'fidelity to the Elohim' substitutes a plural referent for singular theou (the Greek, quoting Deut 8:3, offers no plural). |
| E-009 | LWTE-2:39 | (Matthieu, IV, 6 et 7.) → Matt 4:6-7 | MAT-WOH-4:6, MAT-WOH-4:7… | addition | = |  | N | French and Greek agree apart from the slip l'/t'. |
| E-010 | LWTE-2:44 | (Matthieu, IV, 8 à 11.) → Matt 4:8-11 | MAT-WOH-4:8, MAT-WOH-4:9… | supported | = |  | N | Two of the three lexical claims are borne out by the Greek: Satana is a name in the vocative, and angeloi are 'messengers'. |
| E-011 | LWTE-2:49 | (Job, I, 6 à 12.) → Job 1:6-12 | JOB-WOH-1:6, JOB-WOH-1:7… | transl-dep | less |  |  | Split verdict, both directions. |
| E-012 | LWTE-2:53 | (Le livre de Job, I, 20 à 22.) → Job 1:20-22 | JOB-WOH-1:20, JOB-WOH-1:21… | addition | = | E |  | Accurate quotation. |
| E-013 | LWTE-2:55 | (Livre de Job, II, 1 à 6.) → Job 2:1-6 | JOB-WOH-2:1, JOB-WOH-2:2… | supported | MORE |  |  | The Hebrew of 2:1 and 2:3 carries the two things the canon needs: the adversary formally presents himself before YHWH at a periodic assembly, and YHWH states that he was incited by him — a relationship of superior and li |
| E-060 | LWTE-2:92 | none → Matt 6:9 (allusion) | MAT-WOH-6:9 | addition | = |  |  | The words are in the Greek as in the French (ouranoi plural = 'cieux'); the biological-paternity application is the canon's, and the prayer's possessive is plural ('our'). |
| E-014 | LWTE-2:108 | (Apocalypse de Jean, I, 10.) → Rev 1:10 | REV-WOH-1:10 | addition | = |  |  | The French is a word-for-word calque and adds nothing the Greek lacks; the telepathy and loudspeaker readings are supplied. |
| E-015 | LWTE-2:113 | (Apocalypse de Jean, I, 12 à 16.) → Rev 1:12-16 | REV-WOH-1:12, REV-WOH-1:13… | transl-dep | less | E |  | Three of the reading's hooks lean on the French more than the Greek: 'lampes' (Greek: lampstands), 'revêtu jusqu'aux pieds' read as a body-suit enclosing the feet (Greek: a robe reaching to the feet), and 'bronze du Liba |
| E-016 | LWTE-2:122 | (Apocalypse, I, 17 à 19.) → Rev 1:17-19 | REV-WOH-1:17, REV-WOH-1:18… | supported | = | **S** |  | 'Was dead and am alive for ever' is literally what the Greek says, so the re-creation reading has a real hook; 'first and last' is singular in Greek and pluralised only in the commentary. |
| E-017 | LWTE-2:124 | (Apocalypse, IV, 1 et 2.) → Rev 4:1-2 | REV-WOH-4:1, REV-WOH-4:2… | supported | = | **S** |  | All the objects are in the Greek as in the French: an opened door in the sky, a command to come up, a seated figure on a throne, twenty-four seated presbyteroi ('elders' — the canon says 'éternels … conseil', and a counc |
| E-018 | LWTE-2:130 | (Apocalypse de Jean, VI, 2.) → Rev 6:2 | REV-WOH-6:2 | addition | = |  |  | A historical-allegorical reading with no technological content; the wording is neutral between the readings the library note lists (Christ, Antichrist, conquest in general, Parthian archers), and the canon's choice sits  |
| E-019 | LWTE-2:133 | (Apocalypse, VI, 4.) → Rev 6:4 | REV-WOH-6:4 | supported | = |  |  | War is what the Greek describes (peace taken from the earth, mutual slaughter, a great sword); 'of religion' is added. |
| E-020 | LWTE-2:137 | (Apocalypse, VI, 5 et 6.) → Rev 6:5b-6 | REV-WOH-6:5, REV-WOH-6:6 | supported | = | E |  | The famine reading is the plain sense of the balance and the prices and is the ordinary reading of the passage. |
| E-021 | LWTE-2:140 | (Apocalypse, VI, 8.) → Rev 6:8a | REV-WOH-6:8 | transl-dep | less | **S** |  | The reading 'epidemics' is read straight off the French name 'La Peste'. |
| E-022 | LWTE-2:143 | (Apocalypse, VI, 9 à 11.) → Rev 6:9-11 | REV-WOH-6:9, REV-WOH-6:10… | addition | = |  |  | French and Greek agree; the reading fits neither closely. |
| E-023 | LWTE-2:150 | (Apocalypse, VI, 12 à 15.) → Rev 6:12-15 | REV-WOH-6:12, REV-WOH-6:13… | addition | = | **S** |  | Every image the canon maps is in the Greek as in the French (shaking, darkened sun, blood-coloured moon, sky rolling back, flight to caves), and 'secousse' is if anything truer to seismos than 'tremblement de terre'. |
| E-024 | LWTE-2:156 | (Apocalypse, VII, 2 et 3.) → Rev 7:2-3 | REV-WOH-7:2, REV-WOH-7:3… | supported | = | **S** | N | The anatomical hook — a mark applied to the forehead that protects from the coming harm — is in the Greek exactly as in the French. |
| E-025 | LWTE-2:161 | (Apocalypse, VIII, 7.) → Rev 8:7b | REV-WOH-8:7 | addition | = |  | N | The French follows the Greek closely (and has the 'third of the earth' clause that the canon's English lost). |
| E-026 | LWTE-2:164 | (Apocalypse, VIII, 8 et 9.) → Rev 8:8-9 | REV-WOH-8:8, REV-WOH-8:9 | transl-dep | less |  | N | A weak dependence: 'lava that flows into the oceans' sits more easily on the French reflexive 's'est jetée' than on eblēthē, 'was thrown/hurled' — one burning mass cast in from outside, by the same verb used for the hail |
| E-027 | LWTE-2:168 | (Apocalypse, VIII, 10 et 11.) → Rev 8:10-11 | REV-WOH-8:10, REV-WOH-8:11 | addition | = |  | N | The image (one flaming object falling from the sky, water made deadly) is the same in Greek and French; 'missile' is supplied. |
| E-028 | LWTE-2:172 | (Apocalypse, VIII, 12.) → Rev 8:12 | REV-WOH-8:12 | supported | MORE |  | N | The canon's gloss — day and night seem shorter — matches the Greek construction (the day not shining for a third of itself) better than the French it quotes, whose 'a brillé un tiers en moins' reads more naturally as dim |
| E-029 | LWTE-2:175 | (Apocalypse, IX, 1 et 2.) → Rev 9:1-2 | REV-WOH-9:1, REV-WOH-9:2 | addition | = |  | N | Falling luminous object followed by a rising column of furnace-like smoke that darkens the sun: the sequence is in the Greek as in the French, and the missile/mushroom identification is supplied. |
| E-030 | LWTE-2:181 | (Apocalypse, IX, 3 à 6.) → Rev 9:3-6 | REV-WOH-9:3, REV-WOH-9:4… | addition | = |  | N | French and Greek agree, and both resist the reading at two points the canon quotes without comment: the locusts may not kill (the canon confines the torment to 'those who will not die of the explosion', conceding deaths  |
| E-031 | LWTE-2:187 | (Apocalypse, IX, 7 à 10.) → Rev 9:7-10 | REV-WOH-9:7, REV-WOH-9:8… | transl-dep | less |  | N | The clearest case in the slice of a reading resting on a French word. |
| E-032 | LWTE-2:191 | (Apocalypse, IX, 13.) → Rev 9:13 | REV-WOH-9:13 | transl-dep | less |  | N | The count 'four' in «quatre haut-parleurs» depends on a textual variant: the Greek text the library translates reads 'from the horns of the golden altar' with no numeral, while the French the canon quotes has 'des quatre |
| E-033 | LWTE-2:196 | (Apocalypse, IX, 17 à 19.) → Rev 9:17-19 | REV-WOH-9:17, REV-WOH-9:18… | addition | = | E | N | The French is literal; the reading is an identification by resemblance, reinforced by a modern-language pun on 'tête'. |
| E-034 | LWTE-2:199 | (Apocalypse, X, 4.) → Rev 10:4 | REV-WOH-10:4 | addition | = |  | N | The verse records only that something was said and suppressed; any statement of its content is outside what Greek or French can support or contradict. |
| E-035 | LWTE-2:201 | (Apocalypse, X, 7.) → Rev 10:7 | REV-WOH-10:7 | transl-dep | less | E | N | A mild dependence on the French: 'le mystère de Dieu … sera fini' can be heard as 'the God-mystery will be over', which is how the canon reads it (the idea of god ends). |
| E-036 | LWTE-2:203 | (Apocalypse, XII, 12.) → Rev 12:12b | REV-WOH-12:12, REV-WOH-12:9 | addition | less | **S** |  | The half-verse quoted supports 'limited time' and 'rage' and nothing more specific. |
| E-037 | LWTE-2:206 | (Apocalypse, XIII, 18.) → Rev 13:18 | REV-WOH-13:18 | addition | less | E | N | The French is faithful; the Greek adds two constraints that the French reader does not see. |
| E-038 | LWTE-2:211 | (Apocalypse, XVI, 18.) → Rev 16:18 | REV-WOH-16:18 | addition | = |  | N | Literal French; 'secousse' rather than 'tremblement de terre' leaves room for a non-geological cause, and so does seismos. |
| E-039 | LWTE-2:214 | (Apocalypse, XVI, 20.) → Rev 16:20 | REV-WOH-16:20 | addition | = |  | N | Literal French. |
| E-040 | LWTE-2:217 | (Apocalypse, XVI, 21.) → Rev 16:21a | REV-WOH-16:21 | transl-dep | less | E | N | Slight dependence: the Greek says hailstones weighing about a talent — heavy ice; the French 'comme des lingots' substitutes a solid cast object for a unit of weight, which eases the move to 'rocks'. |
| E-041 | LWTE-2:220 | (Apocalypse, XXI, 1.) → Rev 21:1 | REV-WOH-21:1 | supported | = | E | N | The verb that carries the reading — the first sky and earth 'went away' — is in the Greek (apēlthan) with the same literal motion sense as the French 's'en sont allés'; standard translations obscure it, the canon's Frenc |
| E-042 | LWTE-2:223 | (Apocalypse, XXI, 2.) → Rev 21:2 | REV-WOH-21:2 | addition | = |  | N | The French is exact. |
| E-043 | LWTE-2:225 | (Apocalypse, XXI, 3 et 4.) → Rev 21:3b-4 | REV-WOH-21:3, REV-WOH-21:4 | transl-dep | less |  | N | 'No more death' is a real hook for eternal life. |
| E-046 | LWTE-3:6 | none → lexical claim about אֱלֹהִים (cf. Gen 1:1) | GEN-WOH-1:1 | contradicted | less |  | N | As a statement about what the Hebrew word means, the gloss has no lexical basis: core woh-claim-0009 already rules that 'those who came from the sky' is a canonical rendering and 'not the consensus lexical derivation' (w |
| E-050 | LWTE-3:7 | none → ἄγγελος (e.g. Matt 4:11) | MAT-WOH-4:11 | supported | = |  | N | Correct, and confirmed by the library's glossary entries on angelos. |
| E-051 | LWTE-3:9 | none → מָשִׁיחַ (cf. Dan 9:25-26) | DAN-WOH-9:25, DAN-WOH-9:26 | addition | less |  |  | The core sense 'anointed' is right. |
| E-054 | LWTE-3:22 | none → προφήτης (e.g. Rev 10:7) | REV-WOH-10:7 | addition | = |  |  | Loose but not wrong in function; the Greek word is 'spokesman', not 'revealer'. |
| E-044 | LWTE-3:35 | (Matthieu, XXVII, 20.) → Matt 27:20 | MAT-WOH-27:20 | no-reading | = |  | N | Rhetorical analogy only; quotation literal. |
| E-052 | LWTE-3:78 | none → הַלְלוּ־יָהּ (e.g. Ps 147:1, 20) | PSA-WOH-147:1, PSA-WOH-147:20 | supported | = |  |  | Substantially right: verb 'praise' plus the divine name (short form Yah). |
| E-053 | LWTE-3:81 | none → ἀμήν (e.g. Rev 1:6-7) | REV-WOH-1:6, REV-WOH-1:7 | addition | = |  |  | A conventional paraphrase rather than an etymology: the Hebrew root is 'firm, reliable', and 'so be it' is the usage-gloss. |
| E-045 | LWTE-4:90 | (I, Thess., V, 1à 3) → 1 Thess 5:3 (two nouns only) | 1TH-WOH-5:1, 1TH-WOH-5:2… | addition | = |  | N | Only two words are taken from the passage. |
| E-058 | LWTE-4:91 | l'Ecclésiaste, -VII, 10 (inline, not in the citation index) → Eccl 7:10 |  | not-checkable | = |  |  | The library holds Ecclesiastes 3 only in Hebrew (ecclesiastes-woh); chapter 7 is not available, so the wording cannot be compared. |
| E-059 | LWTE-4:92 | none → Matt 13:35 | MAT-WOH-13:35 | addition | = |  |  | The phrase is quoted as a slogan. |

## Tensions and null results

- **Null result on mistranslation as the engine.** Only 30 of 321 readings are translation-dependent, and several of those are mild. The French is literal enough that most hooks survive into the original; what does not survive is usually the cut context.
- **Null result on plural narration.** No quoted verse has a narrator's plural verb with Elohim. The plural-agreement verses that exist in the Hebrew Bible (core 0009) are not the ones the canon quotes; the one plural adjective inside a quoted verse (1 Sam 17:26) is hidden by the canon's own French.
- **Counter-examples to "the cuts always favour the reading".** Several cuts remove material that would have helped: Exod 14:20 (the screen), Exod 25:8–9 (dwelling and plans), 1 Kgs 17:4, Josh 5:13, Isa 29:11, Ezek 1:28 and 10:19b, Ps 139:2, Wis 13:1c. The cutting is not uniformly tendentious; it is also simply abbreviating.
- **Both directions on one word.** *haśśāṭān*: the article is against «nommé Satan» and for «l'opposition». *šəḥāqîm* at Job 37:18: metal-beating verb for, "the skies" as object against. *bənê hāʾĕlōhîm*: plural and articular, but "sons of".
- **A reading the canon later withdraws.** LWTE-1:12 downgrades TBWTT's atmospheric reading of Exod 33:20 to a verse added "en exemple" (E-001).
- **hebrew-supported is not confirmation.** In most of the 138 the original supplies the hook (a noise, a column, a lifting, a number) and the canon supplies the referent. The label records where the wording is, not whether the reading is right.

## Relation to existing core records

- **woh-claim-0066 (quotation layer).** Extended, not redone. This audit supplies what the record names as missing only in part: it is a collation against the *original languages*, not against Dhorme. It adds evidence for the partial-mediation alternative: the Iahvé→Yahvé shift between TBWTT/ETTMTTP and LWTE, a distinct NT/Revelation translation, re-quotation drift, «Dieu» for ʾĕlōhîm in ten OT quotations, and canon-side insertions (1 Sam 3:10; Mark 16:18).
- **woh-claim-0073 (dragons passage).** Not redone. One generalisation bears on its "quotation gap" observation: skipping a fulfilment verse is the canon's normal practice throughout (ellipsis in 203 items), which strengthens the deflationary reading that the Gen 1:21 omission is pattern, and equally the record's own point that the pattern is uniform.
- **woh-claim-0009 (Elohim plural).** Finding 4 gives the verse-level inventory for the quoted corpus and adds 1 Sam 17:26 to the plural-adjective list (same phrase as Deut 5:26, which the record lists). LWTE-3:6, 3:10, 4:87 are the canon's strongest gloss-as-etymology statements.
- **translation-accuracy-first.** Consistent: the library lines do not encode the canon's readings; 165 of 321 observations here are already in library notes as reception notes.
- **Records whose public prose leans on a verse audited here** and should be checked against the register: ark-communication-device (2 Sam 6; Exod 25), tent-of-meeting-residence (Exod 25:8–9; 33:7–11; B-017, B-018), merkavah-craft-observation (Ezek 1, 10; C-013 to C-026), sodom-strike (Gen 19), babel-pardon-expedition (Gen 11), flood-as-reset (Gen 6–8; A-029, A-030), lucifer-satan-distinction (Job 1–2; Isa 14:12; E-011, E-049), serpent-vocabulary-referent (Gen 3; Isa 27:1), watchers-nephilim-unions (Gen 6:1–4; A-024, A-026).

## Candidate claims or revisions for founder review (proposals, not decisions)

1. **New record (empirical_observation, direct): "The canon's quotations are selective; in a counted minority the ellipsis changes the sense."** Proposition limited to the counts and the register; no inference about intent. Would discipline any public page that argues from a canon quotation as if it were the verse.
2. **Revision to woh-claim-0066.** Scope the proposition to the Old Testament; record the NT layer as unidentified; add the orthography shift and the «Dieu»/«Élohim» mixture as evidence under the partial-mediation alternative.
3. **Revision to woh-claim-0009's evidence map.** Add 1 Sam 17:26 to the plural-adjective list; add the statement that no narrator's plural verb occurs in the verses the canon quotes; add the «comme des dieux» / "like Elohim" observation at Gen 3:5.
4. **Rule proposal for public prose: explicit wording-claims carry their check.** Where the canon says "il est bien dit", "sens originel", "ils auraient dû écrire", the page states what the original has (finding 5 table). The Gen 7:17 and Dan 10:13 cases in particular should not be repeated on a public page without the full verse.
5. **Rule proposal: prefer the stronger unquoted verse.** Where the original is more favourable than the canon's excerpt (finding 2 and the short list after it), public pages may cite the fuller text — labelled as the corpus's observation, not the canon's.
6. **Library housekeeping (not core):** the note at EXO-WOH-19:16 attributes the canon's quotation to ETTMTTP (it is TBWTT-3:25); the GEN-WOH-1:27 English line reads "their image" against singular `בְּצַלְמ֔וֹ` (GEN-WOH-1:27); ten quotations are missing from the citation index (finding 6).

## Limitations

- **No Dhorme collation.** For every translation-dependent item it is unknown whether the French word is Dhorme's or the canon's alteration. The Genesis 1–3 extract core holds could settle Gen 2:17, 3:5, 3:21, 3:22 now; the rest needs the volumes.
- **Masoretic and one Greek text only.** The library prints the MT and (for the NT) an SBLGNT-type text. Where the canon's French follows a variant or emendation (Ps 19:5 "sea"; Isa 48:10; Rev 9:13 "four"; Matt 13:35 "of the world"), "translation-dependent" means dependent on that textual choice; the register says so per item.
- **Lexical judgement.** Glosses and parsings are the auditors' reading of the library text and its notes, not a reviewed philological opinion; items carry `outside_knowledge` flags where a statement goes beyond the library.
- **Slice method.** Five parallel readers classified their slices independently; borderline calls between `hebrew-supported` and `interpretive-addition` are not perfectly uniform across slices. Counts are indicative to within a few items; the per-item evidence is what is checked.
- **Two chapters absent** from the library (Lev 21; Judg 16) leave their allusions not-checkable.
- **Project digitization.** The French dumps are the project's digitization; a printing error in the dump would read here as a canon variant (the «III, I-5» and «I20» references look like such).
