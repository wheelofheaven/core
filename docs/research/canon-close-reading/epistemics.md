---
title: "Canon close reading: the canon on its own evidence"
status: draft
version: 0.1.0
last_reviewed: 2026-11-12
---

# epistemics — the canon's account of its own status as knowledge

Research note for wheelofheaven/core. Draft for founder review; nothing here is a decision.

## Exact question

What does the canon say about its own status as knowledge — how it expects to be believed, tested, proven or doubted — and which of its statements are, on its own terms, checkable?

## Method

- All three books were read in full in the French dumps (`TBWTT.fr.txt`, `ETTMTTP.fr.txt`, `LWTE.fr.txt`), one reader pass per book, each producing five registers: R1 self-description and transmission, R2 proof and belief, R3 forward-looking statements, R4 checkable-in-principle statements, R5 declared unknowns and refusals. The three per-book registers (717 items) are reproduced in full below and are the data behind `epistemics.json`.
- The per-book passes were run as three parallel reader passes; the synthesis in this note was then written from the registers, with the lead paragraphs re-read in the French (TBWTT-1:44, 6:26, 7:72; ETTMTTP-2:23; LWTE-1:12, 1:87, 2:66 and others).
- Layers are kept apart. In the synthesis, "TEXT" marks what the books say, "ANALYSIS" marks my counts, patterns and tensions, "OPEN" marks what would discriminate. In the registers, bullets are text-layer paraphrase; anything after `ANALYSIS:`, `[analysis]` or in a closing "patterns" section is analysis.
- Every quotation is verbatim French on a `QUOTE[REF]: … ENDQUOTE` line and was run through `verify_quotes.py`.
- Outside facts are marked `[outside knowledge — unverified]`. None was checked against a source in this study.
- Voice: the dump's speaker tags are unreliable at the margins (see finding 9). Voices in this note are assigned by reading, not by tag. "Yahweh" is used for the principal speaker as a convenience; in TBWTT's dialogue he gives no personal name, and names himself only at ETTMTTP-2:50.
- Word counts are regex counts over the French dumps (stems `preuve|prouv`, `croi|croy|cru|foi`, `vérifi`, `compren|compris`, `dout|sceptiq`) and are approximate.

## Findings (ranked; new relative to core unless stated)

### 1. Proof is promised on day one, refused on day six, and by 1979 is what the tempter offers

TEXT. On the first morning the speaker tells Raël to wait until he knows everything so as to bring unbelievers incontestable proofs:

QUOTE[TBWTT-1:44]: Attendez de tout savoir avant de leur parler afin de vous défendre correctement contre ceux qui ne vous croiront pas et de pouvoir leur apporter des preuves incontestables. ENDQUOTE

On the sixth morning the same speaker rules out any help usable as proof, and makes being believed without material proof the criterion of worthiness:

QUOTE[TBWTT-6:26]: Nous ne vous aiderons jamais ouvertement ni de quelque façon qui puisse servir de preuve aux sceptiques, le scepticisme allant souvent de pair avec l’agressivité. ENDQUOTE

QUOTE[TBWTT-6:26]: Cela est important pour nous, que l’on vous croie sans preuve matérielle nous prouve plus que tout autre chose que l’on est intelligent et donc digne de recevoir de nous l’héritage scientifique. ENDQUOTE

In the third book the offer of proofs is put in the mouth of the opposing Eloha ("Satan") during the test, and the mission is described from his side as one given without proofs:

QUOTE[LWTE-2:65]: Nous vous donnerons des preuves de notre existence et plus personne ne doutera de vos dires. ENDQUOTE

QUOTE[LWTE-2:66]: sans vous donner de preuves pour convaincre vos frères, ni aucune aide financière ENDQUOTE

ANALYSIS. The book never says what the "preuves incontestables" of 1:44 are. The only thing in TBWTT that the text itself calls proof is scripture (finding 2), so the two statements are reconcilable if 1:44 means the exegesis; the text does not make that identification. The reasons given for refusing demonstration are five, across the books, and are not ranked: scepticism goes with aggression (TBWTT-6:26); prodigies would revive supernatural religion (TBWTT-7:71, LWTE-1:57); crowd panic (TBWTT-4:72, 5:56); safety and non-location (TBWTT-5:56-57); and a public arrival would not convince committed believers anyway (LWTE-1:76-78).

OPEN. Whether the 1973/1974 first printing has the same wording at 1:44 and 6:26 (uncollated; see `woh-claim-0070`).

### 2. In the canon's own vocabulary "preuve" means scripture, and proof runs from humans to creators

TEXT. The Bible is designated the proof, by design, in advance:

QUOTE[TBWTT-3:267]: Les écrits bibliques seront la preuve de tout cela. ENDQUOTE

QUOTE[TBWTT-4:2]: afin qu’ils servent de preuve quand l’ère de la science expliquerait tout aux hommes ENDQUOTE

Also TBWTT-2:55, 3:125, 5:48. The parties asked to prove something are humans: humanity must prove its intelligence (TBWTT-4:51-55), its love (5:64), pass "another test of intelligence" (7:13); Raël has proved himself trustworthy (ETTMTTP-2:11); disarmament will prove worthiness:

QUOTE[LWTE-2:205]: les hommes nous prouveront qu'ils sont dignes de recevoir notre héritage étant non violents. ENDQUOTE

ANALYSIS. Across the three books `preuve/prouv-` occurs about 86 times (26 / 16 / 44). In the register, its uses fall into: scripture as proof; humans proving themselves to the Elohim; private demonstrations to Raël reported to the reader (ETTMTTP-2:80, the replica as proof that there is no soul); asserted Elohim results (ETTMTTP-2:30 « cela nous avons pu le prouver »; LWTE-1:44); adherents' happiness (ETTMTTP-3:3); and what the tempter offers. I found no use in which the reader is handed something materially inspectable other than the biblical text. Null result recorded: no instrument reading, sample, photograph, recording or third-party document is offered in any of the three books; the narrator notes the missing camera himself (TBWTT-1:5, 1:42-43).

### 3. The canon declares its own first book fallible in transmission, and revises it — in book 2 by erratum, in book 3 by reclassifying statements as staging or put-off

TEXT. Book 2 corrects book 1 and attributes the error to the scribe:

QUOTE[ETTMTTP-2:23]: Pour commencer, il faut rectifier un passage du message que vous avez mal retranscrit concernant une intervention éventuelle de notre part pour détruire l'humanité. Il faut bien préciser que nous n'interviendrons pas. ENDQUOTE

Raël separately says the book-1 notes were taken too fast and that he misnamed the site:

QUOTE[ETTMTTP-1:64]: Je mis tout d'abord au propre les notes que j'avais prises le mieux possible, mais beaucoup trop vite pendant que mon interlocuteur parlait. ENDQUOTE

Book 2 also re-dates a book-1 figure (7× light speed "était vrai il y a vingt-cinq mille ans", ETTMTTP-2:43), re-scales the "résidence" to a planet (2:50), and states that the 1973 helmet and lights were approach techniques:

QUOTE[ETTMTTP-2:11]: Tout cela n'était destiné qu'à vous tranquilliser en vous apparaissant sous des aspects correspondants à l'image qu'on se fait généralement d'un voyageur de l'espace. ENDQUOTE

Book 3 opens with a questioner listing "contradictions" between books 1 and 2 (LWTE-1:2-4) and answers that a book-1 statement was said to cut the matter short:

QUOTE[LWTE-1:12]: ils m'ont répondu pour couper court à toute nouvelle demande que cela m'était impossible, comme l'on dit à un enfant que s'il boit de l'alcool il ne grandira plus. ENDQUOTE

and that the reporter's own wording was pitched to the audience:

QUOTE[LWTE-1:57]: J'ai utilisé pour rapporter ce que j'avais vu des mots que les hommes actuels peuvent comprendre, en me mettant psychologiquement à la portée du plus grand nombre ENDQUOTE

ANALYSIS. (a) On the canon's own account, then, the dictated books contain at least four classes of non-literal or defeasible statement: mis-transcription (2:23), figures true of another epoch (2:43), staging (2:11; LWTE-1:5-8), and deliberate put-off (LWTE-1:12). The text gives no rule for telling which other statements belong to these classes. (b) The erratum names "un passage"; the dump's TBWTT still carries the intervention threat in three places (5:65 « ce sera un nouveau «Sodome et Gomorrhe» », 6:25, 7:6). Either the erratum covers all three or two stand; the text does not say. (c) The erratum is itself followed in the same paragraph by a rescue promise (« seuls les gens qui vous suivent seront sauvés »), and book 3 promises active delay of the cataclysm (LWTE-2:159) after reporting Yahweh's « nous ne devions pas intervenir » (LWTE-2:76). Non-intervention is asserted for humanity as a whole and suspended for individuals and followers (ETTMTTP-3:220).

OPEN. Collation of TBWTT-5:65, 6:25, 7:6 across the 1974 printing and later editions would show whether the "mal retranscrit" passage was ever amended in the text itself.

### 4. Three declared modes of transmission, with decreasing documentary control

TEXT. Book 1: live note-taking under dictation (TBWTT-1:63, 2:1), then notes ordered, classified and recopied at home (7:75), reproduced « le plus fidèlement possible » (7:80). Book 2, chapter 2: no notes; a technical means fixes it in memory; written at home in one go:

QUOTE[ETTMTTP-2:22]: Vous n'avez rien pour prendre des notes, mais n'ayez pas peur, tout ce que je vais vous dire restera gravé dans votre esprit, car ici nous avons un moyen technique pour que vous vous rappeliez de tout ce que vous allez entendre. ENDQUOTE

Book 2, chapter 3 ("Les clés"): writing of which he did not feel the author:

QUOTE[ETTMTTP-2:132]: J'écrivais mais je ne me sentais pas l'auteur de ce qui apparaissait sur le papier. ENDQUOTE

From October 1975 the Elohim are said to speak through him:

QUOTE[ETTMTTP-2:98]: À partir de maintenant nous verrons par vos yeux, nous entendrons par vos oreilles et nous parlerons par votre bouche. ENDQUOTE

Book 3: Yahweh's 1979 message is given « par la bouche de mon prophète Raël » (LWTE-2:95) with no date, place or mode of reception stated; the Satan/Lucifer back-story is introduced with « L'on sait que » (LWTE-2:6); chapter 1 is compiled interview answers (1:1); chapter 4 is by named followers.

ANALYSIS. The sequence runs from notes-under-dictation, to machine-assisted memory, to inspired writing, to unspecified. The canon's own fallibility admission (finding 3) attaches to the first and most documented mode. Editorial control is asserted throughout (publisher's changes refused, ETTMTTP-1:64; self-publication to keep control, 1:69; licence to comment, 2:129; exegesis delegated, TBWTT-4:117). This refines `woh-claim-0035`: its "six mornings, one October night" profile is right for the reported sessions, but two further bodies of text (ETTMTTP ch. 3; LWTE-2:95-235) have no reported session at all.

### 5. "Comprendre et non croire" is the programme; belief vocabulary is the practice; the word "vérifier" is absent from the first two books

TEXT. The programmatic formula is in book 3:

QUOTE[LWTE-2:85]: le dernier prophète, et le premier qui s'adresserait aux hommes en leur demandant de comprendre et non de croire. ENDQUOTE

and book 2 ranks science first:

QUOTE[ETTMTTP-3:166]: La science doit être ta religion, car les Elohim, tes créateurs, t'ont créé scientifiquement. ENDQUOTE

The same books define adherents by belief (TBWTT-6:23 « ceux qui croiront en vous, donc en nous »; ETTMTTP-3:260 « croient aux messages transmis par Raël »), reward faith:

QUOTE[LWTE-3:31]: L'on peut donc ne plus croire sans comprendre tout en faisant confiance aux Elohim, en ayant foi en eux, car ceux qui ont l'intelligence d'avoir foi en eux seront de toute façon récompensés. ENDQUOTE

forbid believers to judge:

QUOTE[ETTMTTP-3:241]: Vous qui croyez, ne portez pas de jugements sur les actions ou les paroles des Elohim. Le créé n'a pas le droit de juger son créateur. Respectez notre prophète et ne portez pas de jugement sur ses actions et sur ses paroles ENDQUOTE

and state a gap rule:

QUOTE[ETTMTTP-3:177]: N'oublie jamais que tout ce que tu ne comprends pas et que tes scientifiques ne peuvent expliquer est dû aux Elohim, car l'horloger connaît tous les rouages de la montre qu'il a fabriquée. ENDQUOTE

ANALYSIS. Counts (approximate): belief/faith stems about 158 (38 / 62 / 58); `compren-/compris` about 152 (43 / 43 / 66); `vérifi-` 0 / 0 / 3, and of the three, one is a dictionary check (LWTE-1:10) and one is a follower's statement that he verified the messages point by point, without method or result (LWTE-4:210). The operative verb for the reader is "understand" (and "recognise"), not "test". What the reader is invited to do is a synthesis of three public things — reread the prophets, learn current biology, look at the sky (ETTMTTP-3:256-257) — plus a few specific textual checks (find a Kabbalah, TBWTT-5:51; chemists could reconstitute manna, TBWTT-3:46; any dictionary, LWTE-1:10). Counter-examples to "the canon discourages inquiry" are real and are recorded: TBWTT-4:71 praises those who seek the why of things; ETTMTTP-3:8 prescribes permanent questioning of social habit; LWTE-3:59 places a limit on the source itself (an Eloha who asked you to kill « serait Satan »); belief at the approach of death earns nothing, acts do (ETTMTTP-3:25-26). Counter-examples in the other direction: non-recognition by those with « tous les éléments en main » is punishable (ETTMTTP-2:82); smiling readers « auraient crucifié Jésus » (3:222); the conscious person need not test — « On sait, on ressent » (LWTE-1:187).

### 6. The one observable the reader is told to watch (sightings) is undercut inside the canon

TEXT. Book 1 designates rising UFO frequency as the Elohim's only help and as the sign:

QUOTE[TBWTT-6:28]: Notre seule aide se bornera à apparaître dès à présent de plus en plus fréquemment afin de sensibiliser les gens au problème ENDQUOTE

QUOTE[TBWTT-7:83]: Si vous doutez encore, lisez les journaux et regardez le ciel ; vous verrez que les apparitions d’engins mystérieux seront de plus en plus nombreuses ENDQUOTE

Book 2 repeats it (3:256) but also says apparitions are staged to observe reactions:

QUOTE[ETTMTTP-2:29]: Nous continuons d'ailleurs sur terre à faire des "apparitions" afin de voir si cela prend toujours et quelles sont les réactions des pouvoirs publics, des gouvernements et de la presse. Nous nous amusons souvent beaucoup... ENDQUOTE

ANALYSIS. "More and more numerous" is unbounded in rate and time and is a statement about reports. It is the canon's only reader-facing empirical sign, and it is the one `woh-claim-0057` declines to enlist; the canon's own text gives a further internal reason for that posture (2:29). Sanctions are likewise built to leave no trace (ETTMTTP-3:221 « sans que rien ne paraisse être dû à quelques chose venu d'en haut »).

### 7. Forward-looking statements: no calendar deadline in any book; four near-unconditional exceptions

TEXT and classification (full list in the registers, R3 of each book; 143 items). A grep for future years, "2035", "fin du siècle", "avant l'an" returns nothing; all dates in the canon are past or calendrical rules. The return is conditional and stacked (TBWTT-6:20, 6:25, 7:20-21: enough followers, intense enough wish, warlike temperaments « réduits à une totale impuissance dans le monde entier », the residence built to specification at 6:21-22) and the text allows it to fall after Raël's death:

QUOTE[TBWTT-6:27]: si nous devons attendre vos descendants pour venir ENDQUOTE

The exceptions, judged on wording only:

| REF | Wording | Class | What the wording commits to |
|---|---|---|---|
| LWTE-1:87 | « ce qui est sûr c'est que l'ambassade sera construite bientôt » | undated, unconditional | construction "soon", said 1979, in Raël's voice; no bound, so wording alone does not settle it; 47 years elapsed |
| LWTE-3:79 | « vous aurez la chance de le vivre … Cette génération, c'est vous ! » | generation-bound, disjunctive | the 1979 addressees live to see the "triumph of truth" in one of two forms; lapses, on its wording, only with that generation; the text reckons a generation at 20 years at LWTE-2:208 |
| TBWTT-6:16 | « on ne parlera plus le français à Paris bientôt, ni l’anglais à Londres, ni l’Allemand à Francfort » | undated, unconditional | national languages gone from their capitals "soon", said 1973; 53 years elapsed |
| TBWTT-7:83 | « Nous allons très vite être assez nombreux pour entreprendre le choix du terrain » | undated, unconditional | rapid growth sufficient to choose a site |
| ETTMTTP-3:237 | « il y a de fortes chances pour qu'il ait lieu … et dans pas longtemps » | undated, probabilistic | a high chance, as of 1975, of a near cataclysm |
| LWTE-2:96, 2:231 | one chance in a hundred of not self-destructing | probabilistic, no horizon | nothing datable |
| LWTE-1:36 | « Le raëlisme sera la religion dominante dans le monde du troisième millénaire. » | dated, unconditional | window open to 3000 |
| LWTE-1:152; TBWTT-2:2 | man « sera bientôt capable de créer synthétiquement de nouveaux codes génétiques » | undated, unconditional | a technological forecast [outside knowledge — unverified: synthetic-genome work bears on it] |
| ETTMTTP-2:125 | on refusal, embassy in a country « proche du tien », and « l'Etat d'Israël sera détruit une nouvelle fois » | undated, conditional | a geographic commitment and a threat, no deadline for the refusal |
| TBWTT-7:72 | he « ne reviendrait que quand ce qu’il m’avait demandé serait accompli » | conditional | see below |

QUOTE[LWTE-1:87]: ce qui est sûr c'est que l'ambassade sera construite bientôt ENDQUOTE

QUOTE[TBWTT-7:72]: après m’avoir dit qu’il ne reviendrait que quand ce qu’il m’avait demandé serait accompli ENDQUOTE

ANALYSIS. (a) Only one item is settled by the canon's own wording: TBWTT-7:72 against the reported return of 1975 (ETTMTTP-2:9 ff.). Either "what he had asked" was accomplished by October 1975 — the book published and a movement founded, but not the residence of 6:21-22 — or the statement was not kept; ETTMTTP-2:11 calls the two years « une mise à l'épreuve » and does not address 7:72. (b) Similarly TBWTT-6:26 « jamais ouvertement » stands beside a three-witness sighting read as « signe évident de l'accord des Elohim » (ETTMTTP-2:5) and healing through his hands (2:98). (c) The disjunction at LWTE-2:231 / 3:79 (golden age, or destruction with the faithful saved) is exhaustive: no outcome contradicts it. (d) Yahweh's 1979 message limits foreknowledge in principle:

QUOTE[LWTE-2:97]: Il est impossible de prédire l'avenir, car il est impossible de voyager dans le temps, mais il est possible de prédire l'avenir d'une entité biologique ENDQUOTE

so on the canon's own terms its forward statements are developmental forecasts about a species, not predictions of events. (e) Probabilities differ by voice: nine in ten (Raël in the 1975 scene, LWTE-2:68), ninety-nine in a hundred (Yahweh, 2:231), with Raël « persuadé » of the one-in-a-hundred outcome (1:72).

Bearing on `woh-claim-0015`: "conditional rather than predicted" holds for the Elohim's arrival in all three books. It does not hold for the embassy's construction in Raël's voice (LWTE-1:87) nor for the generation clause (LWTE-3:79). Also a null result that cuts against a common summary: ETTMTTP nowhere says the arrival waits on the embassy; that conditional is stated in TBWTT (5:66, 6:20-25, 7:20) and LWTE (1:23, 1:27, 3:82).

### 8. Evidence standards are applied asymmetrically, most visibly in book 3

TEXT. Radiometric dating is rejected in principle:

QUOTE[LWTE-1:28]: l'erreur de ces méthodes de datation est de partir du principe que le comportement atomique actuel a toujours été le même ENDQUOTE

and used two paragraphs later against the wooden-ark reading (Ararat wood 700 years old, LWTE-1:46), while a future contrary find is discounted in advance:

QUOTE[LWTE-1:47]: cela ne prouverait pas pour autant que l'arche de Noé était un bateau de bois. L'on trouvera certainement près du mont Ararat des morceaux de bateaux de bois datant de l'époque du véritable déluge ENDQUOTE

Concordant near-death testimony proves only shared brain chemistry (LWTE-1:54); concordant creation myths are « une vérité première » (LWTE-4:183, a follower's voice). Bones older than 25,000 years are assigned to earlier destroyed creations (LWTE-1:13-15). Contemporary science is cited as catching up when it agrees (TBWTT-2:14 continental fit; 7:62 rat memory transfer; 3:111 electrodes) and as priestcraft when it does not:

QUOTE[LWTE-1:196]: Comme l'a dit Einstein, il n'y a pas d'horloge sans horloger. ENDQUOTE

(LWTE-1:196 classes those who attribute life to chance evolution among the false prophets; scientists are « grands prêtres en blouse blanche ».)

ANALYSIS. This is the awkward finding for `woh-claim-0036` and for the epistemic principles: the canon itself, in Raël's and Terrusse's voices, uses anti-evolution arguments of the improbability and entropy type (TBWTT-5:62-63; LWTE-1:196; LWTE-4:10-25, « La théorie évolutionniste est en contradiction avec la loi de l'entropie ») and cites a creationist title (*Evolution ou Création*, LWTE-1:28) as doing the work « très sérieusement ». Record 0036's first wall (no endorsement of the ID movement's arguments) is a Wheel position that departs from arguments the canon makes; the record does not currently say so. The 1:28 dating passage is already carried in `woh-claim-0071` and ADR 0014.

### 9. The dumps are not clean witnesses of the 1974/1975/1979 texts, and voice tags mislead

TEXT. TBWTT-3:305 is a third-person caption inside the dictated chapter (« Symbole que Raël a vu représenté sur la soucoupe volante en 1973. »), tagged Yahweh. ETTMTTP chapter 3 is tagged Yahweh throughout but speaks of « nos créateurs les Elohim » and says "me" of Raël (3:174); Yahweh's October 1975 speech names « le Mouvement Raëlien » and « une religion athée » (2:105) while the frame still says MADECH (2:1-3, 2:114); the book closes on a Geneva « Religion Raëlienne » address (3:265) and refers to « la première partie de ce livre » (3:84). LWTE carries post-1998 footnotes (1:21, 1:201, 2:60, 2:83, 3:26), two of which split running sentences, and an address list with e-mail addresses (4:220-312). ETTMTTP-2:132 breaks off at « Les Elohim commençaient à… ».

ANALYSIS. Any claim about what the canon "originally" committed to (finding 7 especially) is a claim about these digitizations until the first printings are collated. This extends `woh-claim-0070`'s uncollated-first-printings trigger from TBWTT to all three books, and it means LWTE's "Narrator" tag hides at least twelve voices (editor, questioner, Raël, reported Satan, reported Yahweh, first-person Yahweh, and six chapter-4 authors).

### 10. The checkable layer: what is exposed, and who says it

TEXT and ANALYSIS (full list: R4 of each register, 182 items). Grouped by voice:

- **Yahweh, book 1 — a tight numeric cluster.** Parasang defined as one light-second; planet at 30 million parasangs ≈ 9×10¹² km, « un peu moins d’une année lumière »; rockets would need « près de 26 000 ans »; travel under two months at seven times light speed; planet 70.8 billion km from its sun (TBWTT-5:51-53). The arithmetic is self-consistent. What bears on it: the historical definition of the parasang; a stellar census within one light-year [outside knowledge — unverified: nearest known star is beyond four light-years; the parasang is usually described as a road measure of a few kilometres]. Book 3 withdraws the precision: location data only at the embassy, « En attendant, l'on ne peut que se poser des questions » (LWTE-1:27).
- **Yahweh, books 1 and 3 — chronology.** A Genesis day ≈ 2,000 years (TBWTT-2:10); work decided 22,000 years ago (5:4); the speaker is 25,000 years old and directed the creation (7:56); all terrestrial life, dinosaurs included (2:22), therefore falls inside about 25,000 years; first humans about 13,000 years ago by 666 × 20 (LWTE-2:208); flood about 5,000 years ago (LWTE-1:47, Raël). What bears on it: radiometric and stratigraphic dating — which book 3 disallows (finding 8). Creation order differs between TBWTT-2:16-25 and 5:62.
- **Yahweh — biology and physics.** Any cell rebuilds the whole being with memories and personality (TBWTT-3:184; ETTMTTP-2:80); hair and beard are antennas (TBWTT-3:85; ETTMTTP-3:185); a body loses « quelques grammes » at death as energy (ETTMTTP-2:30); the frontal bone « contient le code génétique le plus pur et le plus fidèle » (LWTE-2:158); each human race corresponds to one creator team (TBWTT-2:25); Jews are direct descendants (ETTMTTP-2:104); rat memory transfer « viennent de découvrir » (TBWTT-7:62). Each has an obvious bearing observation, listed in the registers.
- **Philology.** "Elohim" = « ceux qui sont venus du ciel » (TBWTT-2:5); *sains/saints* (TBWTT-3:192, a confusion that exists only in French); Matt 5:3 (4:24); the Kabbalah figures 236,000 and 30 million parasangs (5:51); Ezekiel's dry bones cited as chapter « XXVII » (ETTMTTP-2:72); Buddhist writings on a Western Buddha (3:228); « pas d'horloge sans horloger » attributed to Einstein (LWTE-1:196).
- **Raël's life.** ETTMTTP chapter 1 gives named third parties and datable events (Lucien Morisse, Marcel Jullian, Chancel's *Grand Échiquier*, Bouvard, Salle Pleyel, *Le Point*, *La Montagne*; birth 30 Sept 1946 at Vichy; the 31 July 1975 three-witness sighting; the persisting arm mark, 2:6). This is the most independently checkable layer in the canon and none of it bears on the encounters themselves.
- **Followers' commentary (LWTE ch. 4).** The most testable geology and physics in the canon is Terrusse's, not Elohim speech: dinosaurs as antediluvian species not re-created (4:54-55); continents blasted apart at the flood, now at a decaying « vitesse résiduelle » (4:40-41; Raël gives « plusieurs centaines de kilomètres chaque année » at 1:31); stars « beaucoup plus près » than measured (4:121); Hertz dated to « les années 1920 » (4:73); the Mahabharata as comprising the Vedas and the Ramayana (4:104); Nehring's study attributed to the « Hudson Institut » (4:26).

Null results: no physical constant other than the speed of light; no mechanism of the creation of life beyond "from chemicals"; no named star; no third-party witness to either contact (TBWTT-7:36-37 says an automatic system would warn of anyone approaching); one elapsed-time oddity (arrives « vers minuit », ETTMTTP-2:9; watch reads « minuit » on return, 2:131, after a reported day on the planet).

### 11. The speakers are not presented as omniscient

TEXT. They did not know they were themselves fulfilling a "written" mission (TBWTT-5:58); never found their own creators (7:25); are unsure humanity can stabilise in abundance (5:59); disagree among themselves about humanity (5:64; LWTE-2:25-26); treated the first creation as « une expérience scientifique sans grand intérêt » (ETTMTTP-3:219); can prove of the great being only that it is alive:

QUOTE[LWTE-1:44]: La seule chose qu'ont pu prouver les Elohim, c'est que c'est quelque chose de vivant. ENDQUOTE

and cannot predict the future (LWTE-2:97). Refusals: planet location (TBWTT-1:49, 5:57; LWTE-1:27), scientific knowledge for now (TBWTT-5:65), living witnesses for now (7:68-71), any proof (6:26), the reasons for the three-year embargo on the Satan test and the paternity (LWTE-2:1, 2:90 — no reason given).

## How the canon frames its own standard of evidence (analysis)

1. **It invites one kind of verification and declines another.** Invited: textual and synthetic checking by the reader — compare the account with scripture, with current science, with sighting reports, and judge whether it coheres ("fais donc la synthèse", ETTMTTP-3:257). Declined: material demonstration, by policy and "ever" (TBWTT-6:26), with reasons. The standard is coherence and explanatory satisfaction (« tout s’éclaire et tout paraît simple », TBWTT-7:79), not experiment.
2. **Belief without material proof is not a concession; it is the test.** TBWTT-6:26 makes it the criterion of intelligence and of worthiness for the scientific heritage. The embassy functions the same way: the conditions are things humans must do first.
3. **"Understand, not believe" replaces the object and manner of belief, not belief.** What is to stop is belief in an immaterial God and belief without understanding (LWTE-1:10, 1:12, 3:30-31; ETTMTTP-3:225). What remains is belief in the messenger and senders, redefined as trust (« foi, c'est-à-dire confiance », LWTE-1:70) and rewarded.
4. **Disbelief and counter-evidence are explained in advance.** Majorities are imbecile (TBWTT-6:20); experts save face (7:77); opponents die out (LWTE-1:80, 4:143); the unready should not be argued with (ETTMTTP-3:210, 3:261; LWTE-1:129); older bones, slow drift and Ararat finds are pre-assigned (finding 8).
5. **The tension is real and is not resolved in the text**: science is to be one's religion and scientists are high priests; the reader should question everything in society and should not judge the Elohim or the prophet; nothing is mystical and the text's own authenticating sign is that only the scientifically evolved can understand it (ETTMTTP-2:121).

## How the three books differ (analysis)

| | TBWTT (1974) | ETTMTTP (1975) | LWTE (1979) |
|---|---|---|---|
| Transmission claimed | dictation with notes, recopied | memory "engraved"; then not-the-author writing | interview answers; message "par la bouche de"; followers' essays |
| Proof | scripture is the proof; material proof refused "ever" | proof = private demonstration to Raël; demand for a miracle classed as mockery | proofs are the tempter's offer; public landing said to be insufficient |
| Belief | "croiront en vous, donc en nous"; belief without proof = intelligence | adherents = those who "croient aux messages"; do not judge; gap rule | "comprendre et non croire" stated; faith kept as trust and rewarded |
| Self-correction | none (but internal variances inside the six days) | erratum to book 1; staging admitted | contradictions listed and explained as psychology and put-off |
| Forward statements | all undated; conditions for return; "bientôt" items | none dated; Israel/embassy conditionals; cataclysm "fortes chances" | none dated; "bientôt" embassy; generation clause; 1-in-100; no prediction possible in principle |
| Science | catching up, cited as agreeing | "doit être ta religion"; trust only uncorrupted scientists | dating void; evolutionists false prophets; ch. 4 argues physics and geology |
| Checkable content | numeric cluster, chronology, biology | biography; a few numbers | followers' geology/physics; 666 arithmetic |

## Full register

The three per-book registers follow verbatim after the closing sections of this note (717 items: TBWTT 236, ETTMTTP 238, LWTE 243). Item ids are per book (`[R2.31]` in the LWTE register is not the same item as `[R2.31]` in TBWTT); `epistemics.json` gives each a unique id.

## Tensions and null results (summary)

Tensions inside the text:
- preuves incontestables (TBWTT-1:44) / sans preuve matérielle (6:26) / proofs as temptation (LWTE-2:65);
- nous n'interviendrons pas (ETTMTTP-2:23; LWTE-2:76) / followers rescued (2:23; 3:238-240) / cataclysm delayed (LWTE-2:159) / Israel punished, embassy country protected (ETTMTTP-2:125) / book-1 threats still in the text (TBWTT-5:65, 6:25, 7:6);
- comprendre et non croire (LWTE-2:85) / foi rewarded (3:31) / do not judge (ETTMTTP-3:241) / « On sait, on ressent » (LWTE-1:187);
- la science doit être ta religion (ETTMTTP-3:166) / dating void, evolutionists false prophets (LWTE-1:28, 1:196);
- sightings as sign (TBWTT-6:28, 7:83; ETTMTTP-3:256) / apparitions staged for amusement (ETTMTTP-2:29);
- cannot visit the planet (TBWTT-1:61) / can (7:68) / did (ETTMTTP ch. 2) / the first answer was a put-off (LWTE-1:12);
- he would return only when the task was accomplished (TBWTT-7:72) / returned in 1975;
- impossible to predict the future (LWTE-2:97) / "nous savons avec précision" what happens to such a humanity (2:98);
- infinite universe has no centre (ETTMTTP-2:33) / galaxies turn around the centre of the universe (3:194);
- no life before the Elohim came (LWTE-1:147) / an infinity of earlier creations (1:15); 25,000 / 13,000 / 5,000-year figures.

Null results:
- no future calendar date or deadline in any of the three books;
- no inspectable material evidence, recording, photograph or third-party document offered; no third-party witness to either contact;
- `vérifi-` absent from TBWTT and ETTMTTP;
- no statement in ETTMTTP that the arrival waits on the embassy;
- no reception circumstances for the 1979 message of Yahweh; no reason for the three-year embargo;
- no rule in the text for telling literal from staged or simplified statements;
- no statement that any passage of the dictated books is Raël's own addition, apart from *La géniocratie* (LWTE-1:84), « J'y ajouterai » (1:27), section titles and the adapted vocabulary (1:57);
- no passage found in which the reader is told to test the account experimentally, other than the manna remark (TBWTT-3:46).

## Relation to existing core records

- **`docs/foundations/epistemic-principles.md`.** The source–world distinction and evidence proportionality are Wheel's standards, not the canon's. The canon's own standard is coherence with scripture and present science plus trust in the reporter, with material proof refused as policy. Nothing in the principles needs changing; but a reader could take "the canon as interpretive centre" to include the canon's epistemics, and the findings show these diverge (findings 2, 5, 8). The "independence of evidence" principle applies to the canon's own "proof by scripture": the Bible as read by the speaker is not independent of the speaker's reading.
- **`woh-claim-0020` (contact reports as provenance)** and **`woh-claim-0070` (canonical contact report).** Consistent. New for both: the canon itself grades its first book's transmission as fallible (ETTMTTP-1:64, 2:23) and later reclassifies statements in it (LWTE-1:12, 1:57). 0070 already notes TBWTT-1:53 is qualified at 1:61; it should know that 1:61 is in turn declared a put-off at LWTE-1:12 — the qualifier 0070 cites is one the canon later withdraws. The uncollated-first-printing trigger extends to ETTMTTP and LWTE (finding 9).
- **`woh-claim-0035` (serial dictation).** Supported and sharpened: "later books retrospectively framing earlier ones" is stronger than framing — it includes erratum and reclassification. "Dictation" covers only TBWTT and ETTMTTP ch. 2 by the canon's own description; ETTMTTP ch. 3 and LWTE-2:95-235 are other modes.
- **`woh-claim-0015` (Great Return conditional).** Holds for the arrival. Two sentences in Raël's voice are not conditional (LWTE-1:87 embassy "bientôt"; LWTE-3:79 generation clause), and the record's "dated prophecy fails on a date" contrast should know of them. TBWTT-6:27 (coming may fall after Raël's death) supports the record's reading. The condition list in the record ("must want the return, unified and wise, Embassy on extraterritorial ground, guarantee safety") matches TBWTT-5:56, 6:19-25, 7:20; "warlike temperaments reduced to total impotence in the whole world" (6:25) is the strongest condition and is not in the record's summary.
- **`woh-claim-0031` (threshold choice).** Supported (ETTMTTP-2:23 two-branch fork; LWTE-2:231). New: the canon assigns odds (1 in 100; 9 in 10) and declares event-prediction impossible (LWTE-2:97), which supports the record's exclusion of outcome predictions from the canon's own mouth; and the fork is exhaustive, which is a point for the millenarian-genre alternative.
- **`woh-claim-0036` (design signature, natural designers).** The record's first wall departs from the canon's own argumentation (finding 8). The canon's "appearance of design" arguments are at TBWTT-5:62-63 (ornament), ETTMTTP-3:177 (gap rule, watchmaker), LWTE-1:196, LWTE-4:10-25. The naturalness of the designers is supported throughout (TBWTT-4:70 « Il n’y a pas de miracle, il n’y a que des décalages de civilisations. »).
- **`woh-claim-0057` (UAP reception posture).** The canon designates sightings as its sign (TBWTT-6:28, 7:83) and also undercuts them (ETTMTTP-2:29). The record's "none of it evidence" is a Wheel posture stricter than TBWTT and consistent with ETTMTTP-2:29.
- **`woh-claim-0066` (quotation layer).** Collation leads: Ezekiel « XXVII » (ETTMTTP-2:72); Qur'an wording with « créateur » (2:106-111); Revelation quotations (LWTE-2:108-227).
- **`woh-claim-0071` / ADR 0014.** LWTE-1:28, 1:31, 4:26-41 already carried there; this study adds only the asymmetry at 1:46-47.
- **`woh-claim-0021`** already touches the parasang; the self-consistency of the 5:52-53 arithmetic and LWTE-1:27's withdrawal of precision may be new to it (not checked in detail).

## Candidate claims or revisions for founder review (proposals, not decisions)

1. **New `source_report` record: "the canon's stated policy on proof".** Proposition: the canon reports that the Elohim will give no help usable as proof, gives reasons, designates scripture as the proof, and makes belief without material proof the test (TBWTT-1:44, 3:267, 4:2, 6:26, 7:71; LWTE-1:57, 2:65-66). Label `direct`; contextual. Forbidden use: citing the policy as an explanation of why no evidence exists (that would turn a source report into an auxiliary hypothesis).
2. **New `source_report` record: "the canon's self-revisions".** The erratum (ETTMTTP-2:23), the hasty notes (1:64), the re-dated figure (2:43), the staging (2:11; LWTE-1:5-8), the put-off (LWTE-1:12), the adapted vocabulary (1:57). Consequence to state: canon statements are not uniformly literal on the canon's own account, and the text supplies no rule for sorting them.
3. **Revision note to `woh-claim-0035`.** Add the three (four) transmission modes and that two text-bodies have no reported session.
4. **Revision note to `woh-claim-0015`.** Record LWTE-1:87 and LWTE-3:79 as non-conditional sentences in Raël's voice; add TBWTT-6:27; add 6:25 to the condition list; note that ETTMTTP does not state the embassy conditional.
5. **Revision note to `woh-claim-0070`.** The 1:61 qualifier is itself withdrawn at LWTE-1:12; extend the collation trigger to books 2 and 3.
6. **Revision note to `woh-claim-0036`.** State that the canon itself argues from improbability, entropy and the watchmaker, and that Wheel's first wall is a departure from those arguments, not from the canon's premise.
7. **A forward-statement register as a dataset or evidence appendix** (the 143 R3 items, classified), so that corpus prose cannot drift into date-setting or into "the canon never commits to anything".
8. **Research question, not a claim:** first-printing collation of the passages on which findings 1, 3 and 7 rest (TBWTT-1:44, 5:65, 6:16, 6:25-28, 7:6, 7:72, 7:83; ETTMTTP-2:23, 2:105, 3:84, 3:265; LWTE-1:87, 3:79).
9. **Editorial question for the founder:** `.claude/rules` and ADR 0014 direct that canon premises be stated directly. Findings 3 and 8 raise a case the rule does not cover — canon statements that the canon itself later reclassifies (1:61), or canon arguments (dating void; anti-evolution) that Wheel's own records decline. A ruling on how prose should carry these would prevent ad hoc handling.

## Limitations

- The reading was done on the project's French digitizations, which carry later editorial layers (finding 9). First printings were not seen.
- The per-book registers were produced in three parallel passes and consolidated here; I re-read the paragraphs behind the lead findings but did not re-read all 717 items against the French. Paraphrases in the registers may carry reader error; quotations are machine-verified against the dumps.
- "Exhaustive" means every paragraph was read with the five registers in mind; borderline items (routine "environ", every scripture citation used as support) were sampled, not all listed.
- Outside-knowledge flags (parasang, nearest star, memory-transfer experiments, Hertz, Mahabharata, Einstein attribution, Israel 1948, synthetic genomes, Ezekiel 37, Afar rifting) are unverified and need sources before any use.
- Word counts are regex-based and approximate; they include quoted scripture.
- No ruling is made on whether any forward statement was fulfilled, except where the canon's own later text bears on an earlier one (TBWTT-7:72; 6:26; 1:61).
- The classification of reasons, modes and "classes of non-literal statement" is mine, not the text's.

---

# Appendix — full registers by book

# TBWTT — epistemics registers (Le Livre qui dit la vérité, 1974)

Basis: full read of `texts/TBWTT.fr.txt` (all 7 chapters, every paragraph). French is the source of record; paraphrases are mine.
Voices: Y = the visitor (tagged [Yahweh]); R = Raël in dialogue; N = Raël as narrator.
Layer (a) = bullets (what the text says). Layer (b)/(c) = the closing section and any text after "ANALYSIS:" inside a bullet.
Tags: dated|undated · cond|uncond · `[outside knowledge — unverified]` marks anything not from the text.

## R1 — Self-description, transmission, accuracy, limits

- [R1.1] TBWTT-1:44 | Y | Commission: tell men the truth; wait until you know everything; write down all I say and publish it as a book | transmission, commission
QUOTE[TBWTT-1:44]: Vous écrirez tout ce que je vous dirai et ferez publier le livre regroupant ces écrits. ENDQUOTE
- [R1.2] TBWTT-1:46 | Y | Why this reporter: country open to new ideas; intelligent and open; free-thinker but not anti-religious; Jewish father/Catholic mother; his trade makes him more credible; not a scientist so he will explain simply; not a literary man so no complicated sentences | transmission, declared simplification
QUOTE[TBWTT-1:46]: N’étant pas un scientifique, vous ne compliquerez pas la chose et l’expliquerez simplement. ENDQUOTE
- [R1.3] TBWTT-1:63 | Y | Come back tomorrow with the Bible and something to take notes; bring nothing metallic; tell no one or meetings stop | transmission, secrecy condition
QUOTE[TBWTT-1:63]: Revenez demain avec la Bible, à la même heure, et amenez de quoi prendre des notes. ENDQUOTE
- [R1.4] TBWTT-2:1 | N | Arrived with notebook, pen and Bible; had told no one; invited to take notes | transmission = live note-taking
QUOTE[TBWTT-2:1]: Il m’invita à prendre des notes et commença à parler. ENDQUOTE
- [R1.5] TBWTT-2:91 | Y | End of day 2: assimilate and write what I said | transmission
QUOTE[TBWTT-2:91]: Ce que je viens de dire, assimilez-le et écrivez-le. ENDQUOTE
- [R1.6] TBWTT-7:8 | Y | "I had you note the passage" (women in the Bible) | transmission, notes directed by speaker
- [R1.7] TBWTT-7:75 | N | At home he put the notes in order, classified and recopied them | transmission: a redaction stage by Raël is stated
QUOTE[TBWTT-7:75]: en mettant de l’ordre dans les notes que j’avais prises, en les classant et en les recopiant ENDQUOTE
- [R1.8] TBWTT-7:80 | N | The book was written "trying to reproduce as faithfully as possible" what was said | accuracy claim, hedged (effort, not verbatim guarantee)
QUOTE[TBWTT-7:80]: ce livre que j’ai écrit en essayant de reproduire le plus fidèlement possible tout ce qui m’a été dit ENDQUOTE
- [R1.9] TBWTT-7:81 | N | "All I have said is only the deep truth" | accuracy claim, absolute
- [R1.10] TBWTT-7:76 | N | To sceptics: I do not drink, I sleep well; one cannot dream six days running nor invent all this | self-authentication by exclusion of dream/invention
QUOTE[TBWTT-7:76]: on ne peut pas rêver six jours de suite ni inventer tout cela. ENDQUOTE
- [R1.11] TBWTT-7:16 | R | Six consecutive days of meetings | transmission frame
- [R1.12] TBWTT-1:4, 1:33 | N/R | Narrator already "firmly believed" in flying saucers and in telepathy before the encounter | reporter's prior beliefs, self-declared
QUOTE[TBWTT-1:4]: J’y croyais fermement depuis longtemps mais je n’espérais pas en voir une moi-même un jour. ENDQUOTE
- [R1.13] TBWTT-1:5, 1:42-43 | N/Y | Narrator regrets having no camera; the visitor names that regret as wanting "preuve à l'appui" | absence of record acknowledged
- [R1.14] TBWTT-2:2 | Y | The Bible keeps "traces of the truth", somewhat deformed by copyists who could not conceive the technology and attributed it to the supernatural | status of the Bible as degraded record
QUOTE[TBWTT-2:2]: vous pourrez retrouver les traces de la vérité qui ont bien sûr été un peu déformées par les copistes ENDQUOTE
- [R1.15] TBWTT-2:3 | Y | Only the parts "I am going to translate for you" matter; the rest is "poetic chatter"; thanks to the copy-without-change law the deep sense survived | selection principle declared by speaker; text is selective by design
QUOTE[TBWTT-2:3]: Seules les parties de la Bible que je vais vous traduire sont importantes. Les autres, qui ne sont que des bavardages poétiques, je ne vous en parlerai pas. ENDQUOTE
- [R1.16] TBWTT-2:41 | Y | One Genesis sentence (3:21) is "nearly intact from the original document" | implies an original document behind Genesis
QUOTE[TBWTT-2:41]: La Bible a conservé ici une phrase à peu près intacte du document originel. ENDQUOTE
- [R1.17] TBWTT-2:58 | Y | The ark with a couple of each species "is an image"; in reality one living cell of each species sufficed | explicit image/reality marker inside the account itself
QUOTE[TBWTT-2:58]: Ceci est une image. En réalité, et vos connaissances scientifiques vous permettront bientôt de le comprendre, il suffit d’avoir une cellule vivante de chaque espèce, mâle et femelle, pour reconstituer ensuite l’être tout entier. ENDQUOTE
- [R1.18] TBWTT-3:169 | Y | Ezekiel "eating" the scroll "is an image", like eating from the tree of knowledge: intellectual food | image marker
- [R1.19] TBWTT-3:69-71 | Y | Joshua's sun standing still is "one of the most deformed passages": it only means a one-day lightning war | corrective reading that removes, not adds, a prodigy
- [R1.20] TBWTT-3:147 | Y | "The whole truth is described here. One had to read between the lines." | hermeneutic rule
- [R1.21] TBWTT-3:164 | Y | Ezekiel's description is "not too badly" done "knowing it is a primitive speaking" | accuracy of ancient witness graded
- [R1.22] TBWTT-3:192 | Y | "They should have written" sains (healthy) not saints (holy) | correction of scripture by a French homophone (see R4.31)
- [R1.23] TBWTT-3:240 | Y | Copyists "did not dare write" *equal to* the Elohim "as it had been dictated" (Ps 8:6) | asserts an original dictation altered by copyists; no witness offered
QUOTE[TBWTT-3:240]: Ils n’ont pas osé écrire, ceux qui ont recopié, égal aux Elohim comme cela avait été dicté. ENDQUOTE
- [R1.24] TBWTT-3:265 | Y | All this is easy to see in the writings; one must still try to understand | hermeneutic rule
- [R1.25] TBWTT-3:223, 3:227, 3:275 | Y | Daniel's sealed words could only be understood once science was sufficient, "i.e. now"; men long had the truth but could not "read" | the present level of science is the stated key to legibility
QUOTE[TBWTT-3:275]: Depuis longtemps les hommes ont la vérité entre les mains mais ils ne pouvaient pas la comprendre avant de «savoir lire», d’être suffisamment évolués scientifiquement. ENDQUOTE
- [R1.26] TBWTT-4:24 | Y | Matt 5:3 "unjustly translated"; original sense: the poor, if they have spirit, will be happy | translation correction asserted without source
- [R1.27] TBWTT-4:110 | Y | "Vision"/"dream" language in scripture marks real events; compare people who really see the craft being told they hallucinated | rule for reading visions as reports
- [R1.28] TBWTT-4:116-117 | Y | We will not go on reading the rest; you will translate it yourself for questioners in the light of my explanations | delegation of exegesis to Raël
QUOTE[TBWTT-4:117]: Vous saurez vous-même les traduire, pour ceux qui vous poseront des questions, à la lumière des explications que je vous ai données jusque-là ENDQUOTE
- [R1.29] TBWTT-5:19 | Y | The truth "has been revealed to you for some days" | self-description as revelation
- [R1.30] TBWTT-5:21 | Y | The Church mistranslated: replaced "Elohim" (plural of Eloha) with singular "Dieu" in "usual Bibles" | translation claim (see R4.3)
- [R1.31] TBWTT-5:51 | Y | The Kabbalah is among the richest testimonies "but it would not have been easy for you to procure one"; if one day you find a copy you can check | speaker explains why a source was not put before the reporter; invites later checking
QUOTE[TBWTT-5:51]: Si un jour vous pouvez en trouver un exemplaire, vous pourrez y constater un très grand nombre d’allusions à nous. ENDQUOTE
- [R1.32] TBWTT-5:54 | Y | Kabbalah is "the book closest to the truth"; nearly all religious books allude to us "more or less clearly/obscurely" (Andes, Himalaya, Greece, Buddhism, Islam, Mormons) | ranking of other sources
- [R1.33] TBWTT-5:56 | Y | "You now know the truth. It must be written and made known" | closure of the doctrinal part
- [R1.34] TBWTT-5:62 | Y | "I open a parenthesis here" to dissipate "the doubt of evolution" | structural self-marking
- [R1.35] TBWTT-5:65 | Y | Declared scope of the message: not the scientific baggage (not yet), but the political and humanitarian baggage | the text states what class of content it withholds
QUOTE[TBWTT-5:65]: Si nous ne pensons pas encore que nous pouvons vous donner notre bagage scientifique, nous pensons que nous pouvons vous donner sans danger notre bagage politique et humanitaire. ENDQUOTE
- [R1.36] TBWTT-5:66 | Y | Name RAËL glossed four ways: "lumière de Dieu", "lumière des Elohim", "celui qui apporte la lumière des Elohim"/"Ambassadeur des Elohim", or simply "messager" | graded glosses ("littéralement", "plus précise", "plus exactement", "plus simplement")
- [R1.37] TBWTT-6:20 | Y | We stay in telepathic contact to restore confidence and give further information "if we find it necessary" | open channel for later supplements, at speaker's discretion
- [R1.38] TBWTT-7:72 | N | He said he would return only when what he asked was accomplished | closure condition (see R3.42)
- [R1.39] TBWTT-3:31, 3:33, 2:27 | Y | Exegesis is anchored to what the reporter is seeing: same bluish alloy as "the floor of the craft we are in"; the fire colour "as you noticed at departure"; "you can see the resemblance is striking" | reporter's own sight used as corroboration of biblical readings
- [R1.40] TBWTT-4:70, 4:72 | Y | No miracles, only gaps between civilisations; "even your most eminent scientists could not even glimpse" how we would do ours | limit of present understanding declared
QUOTE[TBWTT-4:70]: Il n’y a pas de miracle, il n’y a que des décalages de civilisations. ENDQUOTE
- [R1.41] TBWTT-3:305 | tagged Y, voice editorial | Caption on the emblem speaks of "Raël" in the third person and of "notre planète"; calls the symbol "certainly the oldest" on Earth | ANALYSIS: not dialogue; a later editorial/caption layer inside the dictated text (speaker tag in the dump is wrong); emblem gloss here (infinity in space/time) differs in wording from 3:288
QUOTE[TBWTT-3:305]: Symbole que Raël a vu représenté sur la soucoupe volante en 1973. ENDQUOTE
- [R1.42] passim (2:10, 5:52, 5:53, 7:15, 7:46, 1:4, 1:6) | Y/N | Quantities are routinely hedged with "environ", "à peu près", "presque", "près de" | approximation is the stated register for numbers
- [R1.43] TBWTT-1:55 vs 5:53 | Y | Travel time: "the time to think of it" (day 1) vs "less than two months" (day 5) | internal variance between a quip and a figure
- [R1.44] TBWTT-1:61 vs 7:67-68 | Y | Could a man visit the planet? Day 1: "Non" (could not live there, not trained). Day 6: "Oui", with a suit, and Earth-air residence exists | internal reversal
- [R1.45] TBWTT-1:49, 1:51 vs 5:52-53 | Y | "I will tell you nothing" of the planet; yet "when I tell you the distance" (1:51) and distance + star details given at 5:52-53 | staged disclosure; refusal partly lifted within the same book
- [R1.46] chapter/section heads (e.g. 2:46, 3:262, 5:61) | N | Section titles are narrator-layer (e.g. "Les hommes ne pouvaient pas comprendre", "L'évolution : un mythe") | editorial framing by Raël, not speech

## R2 — Proof, belief, doubt, science vs religion, refused proofs, conditions, asks

- [R2.1] TBWTT-1:42-44 | Y | The missing camera would have been "proof in support"; instead: tell them, and "according to their reactions we will see whether we can show ourselves freely and officially"; wait to know all so as to defend yourself against unbelievers and "bring them incontestable proofs" | promise of proofs + reaction-conditional showing
QUOTE[TBWTT-1:44]: Suivant leurs réactions, nous verrons si nous pouvons nous montrer à eux librement et officiellement. Attendez de tout savoir avant de leur parler afin de vous défendre correctement contre ceux qui ne vous croiront pas et de pouvoir leur apporter des preuves incontestables. ENDQUOTE
- [R2.2] TBWTT-6:26 | Y | We will never help you openly nor in any way that could serve as proof to sceptics; scepticism often goes with aggressiveness; the intelligent will believe because nothing here is mystical; being believed without material proof is what proves intelligence and worthiness | refusal of proof, with reason; belief-without-proof as the test
QUOTE[TBWTT-6:26]: Nous ne vous aiderons jamais ouvertement ni de quelque façon qui puisse servir de preuve aux sceptiques, le scepticisme allant souvent de pair avec l’agressivité. ENDQUOTE
QUOTE[TBWTT-6:26]: Cela est important pour nous, que l’on vous croie sans preuve matérielle nous prouve plus que tout autre chose que l’on est intelligent et donc digne de recevoir de nous l’héritage scientifique. ENDQUOTE
- [R2.3] TBWTT-1:44 vs 6:26 | Y | "preuves incontestables" promised on day 1; "sans preuve matérielle" required on day 6 | ANALYSIS: reconcilable only if the "incontestable proofs" are the biblical readings (see R2.4-R2.9); the text does not say so explicitly
- [R2.4] TBWTT-2:55 | Y | Gen 6:4 is "the proof" that creators could mate with human women | scripture verse used as proof
QUOTE[TBWTT-2:55]: Vous avez là, la preuve que les créateurs pouvaient s’accoupler avec les filles des hommes ENDQUOTE
- [R2.5] TBWTT-3:94, 3:125 | Y | 1 Sam 17:26 "shows well the reality" of a palpable God; 2 Kings 1:12 is "again the proof" of protection | scripture as proof
- [R2.6] TBWTT-3:267 | Y | When the time comes the "wisdom"/science will be known; "the biblical writings will be the proof of all this" | scripture designated as the proof
QUOTE[TBWTT-3:267]: Les écrits bibliques seront la preuve de tout cela. ENDQUOTE
- [R2.7] TBWTT-4:2 | Y | Christ's function: spread the biblical writings worldwide "so that they serve as proof" when the age of science explains everything | proof-by-prior-text designed in advance
QUOTE[TBWTT-4:2]: afin qu’ils servent de preuve quand l’ère de la science expliquerait tout aux hommes ENDQUOTE
- [R2.8] TBWTT-4:90-93 | Y | Jesus must die and scripture spread so that when the creators return they are not taken for usurpers or invaders; the writings exist to keep the trace and secure recognition | purpose of scripture = recognition evidence
- [R2.9] TBWTT-5:25-29, 5:48 | Y | "You are my witnesses": the Bible preserved by the Jewish people is the testimony; the Church's finished mission was propagating "what must serve as proof today" | witness/proof vocabulary
QUOTE[TBWTT-5:48]: à savoir la propagation de ce qui doit servir de preuve aujourd’hui ENDQUOTE
- [R2.10] TBWTT-3:268-270 | Y | It was simple to see the truth: recognise the creators by observing the created thing (Wisdom 13:5, 13:1) | inference from creation to creators endorsed
- [R2.11] TBWTT-5:62-63 | Y | "You could realise for yourself" that accidental evolution is very unlikely to yield such variety (bird colours, courtship, spiral horns); "what natural need?" | appeal to the reader's own judgement; improbability/argument from ornament
QUOTE[TBWTT-5:63]: Vous pouviez vous rendre compte par vous même qu’une évolution accidentelle a bien peu de chances de se produire pour arriver à une si grande variété de formes de vie ENDQUOTE
- [R2.12] TBWTT-5:62 | Y | Purpose of the evolution passage: to "dissipate from your mind the doubt of evolution"; scientists "are not completely wrong" | doubt named as something to be removed; partial concession to science
- [R2.13] TBWTT-3:113 | Y | Past policy: appear as little as possible, to see whether man reaches the scientific era alone, while reinforcing prophets' authority with "miracles" (science incomprehensible then) | miracles as past credentialing method
- [R2.14] TBWTT-4:21, 3:263 | Y | Jesus did "miracles" so most people would rally; the robot Raphael left "after having proved to them who he was" | proof by demonstration was given in the past
- [R2.15] TBWTT-7:68-71 | Y | Moses, Elijah, Jesus are alive and could be sent "in due time to support what you say"; not now, because in an incredulous world Christ would be put in an asylum, and scientific prodigies to prove him would relaunch God-religion and the supernatural | living witnesses withheld; second stated reason for refusing proof
QUOTE[TBWTT-7:71]: Si nous intervenions en réalisant des prodiges scientifiques pour montrer qu’il est vraiment le «Christ», cela relancerait la religion basée sur Dieu et revaloriserait le surnaturel ou le mystique, ce que nous ne voulons pas non plus ENDQUOTE
- [R2.16] TBWTT-4:72 | Y | A third reason: demonstrations would panic the crowds | refusal reason (panic)
- [R2.17] TBWTT-5:56 | Y | A fourth: safety — human war craft have chased ours; showing ourselves risks injury/death and "a murderous panic" | refusal reason (safety)
- [R2.18] TBWTT-5:57 | Y | Radio contact refused so the planet cannot be located | refusal reason (location)
- [R2.19] TBWTT-6:28 | Y | "Our only help" = appearing more and more frequently from now on, to sensitise opinion and make people want to read the truth you transmit | UFO sightings designated as the sole supporting sign
QUOTE[TBWTT-6:28]: Notre seule aide se bornera à apparaître dès à présent de plus en plus fréquemment afin de sensibiliser les gens au problème ENDQUOTE
- [R2.20] TBWTT-4:102-104 | Y | Before returning, creators appear at shorter and shorter intervals "as is happening now"; when UFOs appear "en pagaille comme maintenant" the times have come | sightings as sign of the times
- [R2.21] TBWTT-7:77-78, 7:83 | N | To unbelievers: "look at the sky"; if you still doubt, "read the newspapers and look at the sky" | reader directed to an external observable as confirmation
QUOTE[TBWTT-7:83]: Si vous doutez encore, lisez les journaux et regardez le ciel ; vous verrez que les apparitions d’engins mystérieux seront de plus en plus nombreuses ENDQUOTE
- [R2.22] TBWTT-3:284, 3:287 | Y | We want to show ourselves officially only if man is grateful; "if we were sure you would not turn against us" | condition: gratitude/love
- [R2.23] TBWTT-5:56 | Y | Conditions for sharing knowledge: men must show they want to meet us, deserve it, that it is safe, that they "really sketch out union"; hunger and war still exist | conditions list (1)
- [R2.24] TBWTT-6:19-20 | Y | We will wait to see men truly want us, love and respect us as fathers, craft not threatened; "what we want is to see whether there are enough wise people on Earth"; "if a large enough number follow you, we will return openly" — where? in the place you will have prepared | conditions list (2); the test is a headcount of followers
QUOTE[TBWTT-6:20]: Ce que nous voulons c’est voir s’il y a suffisamment de sages sur la Terre. Si un assez grand nombre vous suivent, nous reviendrons au grand jour. ENDQUOTE
- [R2.25] TBWTT-6:21-22 | Y | Residence specification: mild-climate country; 7 rooms each with bathroom; conference room ≥21; pool; dining room 21; park walled; residence ≥1000 m from wall; ≤1 storey; N and S gates; roof terrace for a 12 m craft; no military/radar surveillance of airspace; try to obtain neutral-territory status "au titre de notre ambassade"; sealed metal door; asepsis airlock | concrete, auditable conditions (also R3)
- [R2.26] TBWTT-6:23 | Y | Funding from "those who will believe in you, therefore in us, and who will therefore be wise and intelligent"; they will be rewarded when we come; keep a file of contributors | belief equated with intelligence; reward for believers
QUOTE[TBWTT-6:23]: ceux qui croiront en vous, donc en nous, et qui seront donc sages et intelligents ENDQUOTE
- [R2.27] TBWTT-6:24-25 | Y | Yearly gathering on a mountain near the residence; make them think of us and wish intensely for our coming, "without religious mysticism, as responsible men" | prescribed practice; anti-mystical framing of a collective wishing rite
- [R2.28] TBWTT-6:20 | Y | "The wise will listen. Many will take you for a madman"; recall what I said of "imbecile majorities" | disbelief pre-explained
QUOTE[TBWTT-6:20]: Beaucoup vous prendront pour un fou ou un illuminé mais je vous ai expliqué plus haut ce qu’il faut penser des majorités imbéciles. ENDQUOTE
- [R2.29] TBWTT-6:4, 7:77 | Y/N | Copernicus condemned by an incapable majority; scientists and military will give face-saving "chatter" because the truth did not come from their closed circle | expert rejection pre-explained (see R4.44)
- [R2.30] TBWTT-4:50-53 | Y | "Let him who can, understand": seekers will understand, others won't; peoples that fail to prove their intelligence will be destroyed | understanding as selection
- [R2.31] TBWTT-4:71 | Y | The most evolved among you will "seek the why of things instead of stupidly lying flat with offerings" | inquiry commended over worship
- [R2.32] TBWTT-4:72 | Y | "There is no immaterial God; there are men who created other men in their image" | science-replaces-religion thesis
- [R2.33] TBWTT-5:3-4 | Y | End of the Church's world; people of scientific countries "no longer believe in anything", cannot believe in the bearded God, "no longer know what to believe" | diagnosis of belief vacuum
- [R2.34] TBWTT-5:4 | Y | "Certain men already wrote it but were not believed" | unnamed precursors
- [R2.35] TBWTT-5:37 | Y | The Church erred in making man pray "without seeking to understand" | understanding over rote
- [R2.36] TBWTT-7:24-25 | Y | "Our only religion is human genius. We believe only in that" | belief vocabulary applied to the speakers
- [R2.37] TBWTT-7:23 | Y | Other planets' "religious writings prove to us" that their creators had science equal to ours | the speakers themselves reason from religious texts to creators
- [R2.38] TBWTT-3:219 | Y | At the "last judgement" those who "believed in the creators, followed their commandments" are welcomed | belief rewarded
- [R2.39] TBWTT-3:214 | Y | Jews were dominated by Persians and Greeks as punishment for "lack of faith" | faith vocabulary, punitive
- [R2.40] TBWTT-2:89, 3:249-254, 4:20 | Y | Creators test humans' feelings (Abraham; Job; Jesus tested by "the sceptic Satan") | loyalty tests; scepticism personified as Satan
QUOTE[TBWTT-4:20]: le sceptique «Satan», soutenu par les opposants au gouvernement de notre lointaine planète ENDQUOTE
- [R2.41] TBWTT-4:55, 5:64, 7:13 | Y | Humanity must "prove its intelligence"; "you will prove to us that you love us"; birth control is "another test of intelligence" | proof flows from humans to creators, not the reverse
- [R2.42] TBWTT-7:79 | N | "Official scientists" fail to give a sufficiently precise explanation of our origins and aims; with these revelations "everything becomes clear and seems simple" | explanatory satisfaction offered as warrant
- [R2.43] TBWTT-7:80 | N | He would be "deeply disappointed" if readers thought it imagination or mere amusement | anticipated reception
- [R2.44] TBWTT-7:81, 7:83 | N | Asks of the reader: understand it as truth, wish for their coming, write to me, join the Mouvement Raélien, help build the residence, contribute "passively or actively according to your means" | what the reader is asked to do
- [R2.45] TBWTT-7:82 | N | Believers in God/Christ "were right to believe" in the foundation of the writings but wrong to support the Church; continuing to fund it means you "want to remain primitives" | belief partly validated, institution rejected
- [R2.46] TBWTT-1:32-40 | Y | Telepathy made Raël come to the crater and buy a Bible days earlier | reporter's own impulses offered as evidence of prior influence (self-report only)
- [R2.47] TBWTT-1:22-24 | Y | Visitor recites Raël's name, trade, marital status, children: "we have been observing you for a long time" | in-story credential
- [R2.48] TBWTT-4:40, 3:227 | Y | Space travel and television have made the texts readable and "miracles comprehensible"; nothing astonishes people any more | plausibility from the present state of technology
- [R2.49] TBWTT-5:9, 5:48 | Y | The Church could survive if it understood its error and served the truth (Pope on the road, Vatican sells its riches) | conditional offer to the Church
- [R2.50] TBWTT-6:26 | Y | "The future of man is in his hands and the truth is in yours" | responsibility assigned

## R3 — Forward-looking statements

Null result first: TBWTT contains **no future calendar date**. All dates are past (1945, 1946, 13 Dec 1973, "1973" in the 3:305 caption). Every forward statement is undated ("bientôt", "un jour", "très vite", "en temps voulu") or conditional.

- [R3.1] TBWTT-2:2 | Y | Earth will "soon" have the technical level at which their ancestors began making living cells in test tubes | undated(bientôt) · uncond · commits to: lab-made primitive life in Earth's near future
- [R3.2] TBWTT-2:58 | Y | Your science will "soon" let you understand rebuilding a whole being from one cell | undated · uncond · commits to: near-term understanding of whole-organism reconstitution from a cell
- [R3.3] TBWTT-3:186 | Y | Resurrecting a being from bone debris: "you will do it one day" | undated · uncond
QUOTE[TBWTT-3:186]: Tout cela est très facile à réaliser et vous le ferez un jour. ENDQUOTE
- [R3.4] TBWTT-3:219-221 | Y | A "last judgement" will let great men live again; the bad will live in eternal regret; geniuses most rewarded | undated · uncond
- [R3.5] TBWTT-3:267 | Y | The science behind creation "will be known to man in due time" | undated · uncond
- [R3.6] TBWTT-3:277, 3:279, 4:27, 4:77 | Y | Men will do as the creators did: "you will create other men"; on Earth too scientists will end up reigning | undated · uncond
QUOTE[TBWTT-3:279]: Nous sommes vos créateurs et vous créerez d’autres hommes. ENDQUOTE
- [R3.7] TBWTT-3:283 | Y | Extinct species "can live again when you know how to recreate them" | undated · cond(on capability)
- [R3.8] TBWTT-4:53, 4:88 | Y | Peoples/worlds that do not prove their intelligence "will be destroyed"; the world that has not progressed will be dominated and annihilated by the other | undated · cond · threat
- [R3.9] TBWTT-4:55 | Y | The planet with greatest scientific progress receives the heritage at the "last judgement", if not aggressive; "men of Earth are not very far from that time" | undated(near) · cond
QUOTE[TBWTT-4:55]: Et les hommes de la Terre ne sont pas très loin de ce temps. ENDQUOTE
- [R3.10] TBWTT-4:57 | Y | Creators will bring their knowledge "when they have shown themselves worthy" | undated · cond
- [R3.11] TBWTT-4:93 | Y | "when the creators come back to Earth" — a return is presupposed | undated · presupposed
- [R3.12] TBWTT-4:102 | Y | Before returning the creators "will make" appearances closer and closer together | undated · uncond · commits to rising frequency of appearances
- [R3.13] TBWTT-6:28 | Y | From now on we will appear more and more frequently; gradually opinion will be sensitised and appearances will trigger a desire for contact rather than stupid adoration | undated(dès à présent) · uncond · commits to: increasing sightings after Dec 1973
- [R3.14] TBWTT-7:77 | N | "You will see more and more apparitions that neither your scientists nor your military can explain otherwise than by chatter" | undated · uncond · same commitment in Raël's voice
- [R3.15] TBWTT-7:83 | N | Mysterious-craft sightings "will be more and more numerous" | undated · uncond
- [R3.16] TBWTT-5:3 | Y | The Church made too many errors; "that was foreseen and they will collapse, no longer serving any purpose" | undated · uncond
QUOTE[TBWTT-5:3]: Cela était prévu et ils s’écrouleront, ne servant plus à rien. ENDQUOTE
- [R3.17] TBWTT-5:9 | Y | The revelation will restore hope to the morose and will hasten the fall of the Church "unless it understands its error" | undated · cond(unless)
- [R3.18] TBWTT-5:21 | Y | "You will not manage to destroy the Church completely, but it will die out by itself"; extinction already begun | undated · uncond
- [R3.19] TBWTT-5:7 | Y | The "noisy clamour" = the noise this revelation "will make" | undated · uncond · commits to: the revelation will be loud/widely noticed
- [R3.20] TBWTT-5:16 | Y | "Everyone will then understand" | undated · uncond
- [R3.21] TBWTT-5:19 | Y | "You are the one who is going to spread the truth throughout the world" | undated · uncond
- [R3.22] TBWTT-5:56 | Y | If men want our knowledge (saving them 25,000 years) they must show desire/merit/safety | undated · cond
- [R3.23] TBWTT-5:59 | Y | "We will perhaps disappear one day but you will have taken over" | undated · hedged
- [R3.24] TBWTT-5:65 | Y | The political/humanitarian baggage "will allow you to be happier" and progress faster; otherwise, if aggressiveness persists and war-promoters stay in or take power, "we will prevent them from becoming a danger to us and it will be a new Sodom and Gomorrah" | undated · cond · threat
QUOTE[TBWTT-5:65]: nous les empêcherons de devenir un danger pour nous et ce sera un nouveau «Sodome et Gomorrhe» ENDQUOTE
- [R3.25] TBWTT-5:66 | Y | "We will land officially only in your embassy" | undated · cond(exclusive venue) · commits to: no official landing anywhere else
QUOTE[TBWTT-5:66]: nous ne débarquerons officiellement que dans votre ambassade ENDQUOTE
- [R3.26] TBWTT-5:66 | Y | You will progressively replace your name by RAËL | undated · instruction/prediction
- [R3.27] TBWTT-6:16 | Y | "Auvergnat is no longer spoken in Clermont-Ferrand; soon French will no longer be spoken in Paris, nor English in London, nor German in Frankfurt" | undated(bientôt) · uncond · commits to: disappearance of national languages from their capitals "soon" (in support of a single world language)
QUOTE[TBWTT-6:16]: on ne parle plus l’auvergnat à Clermont-Ferrand, on ne parlera plus le français à Paris bientôt, ni l’anglais à Londres, ni l’Allemand à Francfort. ENDQUOTE
- [R3.28] TBWTT-6:14 | Y | If genius is admitted to power it will understand the usefulness of these reforms | undated · cond
- [R3.29] TBWTT-6:20 | Y | "The wise will listen to you. Many will take you for a madman" | undated · uncond (reception forecast)
- [R3.30] TBWTT-6:20 | Y | If a large enough number follow you, we return openly, at the place you prepare | undated · cond; threshold number unspecified
- [R3.31] TBWTT-6:23 | Y | Contributors "will be rewarded when we come" | undated · cond(on coming)
- [R3.32] TBWTT-6:25 | Y | When they are numerous enough and want it intensely enough, "we will come openly and give the men of Earth our scientific heritage"; "if warlike temperaments are reduced to total impotence in the whole world, this will happen" | undated · cond (three stacked conditions: numbers, intensity, world-wide disarmament of warlike temperaments)
QUOTE[TBWTT-6:25]: Si les tempéraments guerriers sont réduits à une totale impuissance dans le monde entier, cela se produira. ENDQUOTE
- [R3.33] TBWTT-6:25 | Y | "We will wait"; if man stays aggressive and progresses dangerously for other worlds, "we will annihilate this civilisation" and its scientific stores — new Sodom and Gomorrah — until humanity is morally worthy | undated · cond · threat
- [R3.34] TBWTT-6:26 | Y | "We will never help you openly"; "the intelligent will believe you" | undated · uncond ("jamais") · commits to: no overt assistance, ever
- [R3.35] TBWTT-6:27 | Y | You will not be forgotten if you triumph in your lifetime, "and even after, if we must wait for your descendants to come": we can revive you and others, provided remains are kept in tombs | undated · cond · NB: the text itself provides for the coming falling after Raël's death
QUOTE[TBWTT-6:27]: si nous devons attendre vos descendants pour venir ENDQUOTE
- [R3.36] TBWTT-7:6 | Y | Men may destroy themselves; if not and they threaten us, we need only detonate their stockpiles (by rays, or telepathically making one great power "the aggressor") | undated · cond · threat
- [R3.37] TBWTT-7:13 | Y | Overpopulation "will arise very rapidly on Earth"; if each couple has two children, population stops growing; we will observe how you manage | undated(très rapidement) · uncond forecast + cond remedy
- [R3.38] TBWTT-7:20-21 | Y | If men do exactly as wished: we come officially to the residence, ask you to summon official representatives of the most important countries to obtain total union; "if that goes well" we share science progressively; "according to the use made" we see whether to give all | undated · cond, three-stage (coming → union meeting → graduated transfer)
- [R3.39] TBWTT-7:27 | Y | If our world is annihilated, the same automatic process will give you our heritage | undated · cond
- [R3.40] TBWTT-7:58 | Y | Man "will perhaps be superior to us"; can progress faster "if nothing opposes it" | undated · hedged
- [R3.41] TBWTT-7:68 | Y | Moses, Elijah, Jesus and others "we can bring back to Earth in due time to support what you say" | undated(en temps voulu) · capability/intent, not a firm promise
- [R3.42] TBWTT-7:72 | N (reporting Y) | He "would return only when what he had asked was accomplished" | undated · cond · commits to: no further visit before the tasks are accomplished [a later book reports a further contact in 1975 — outside this book; for the parent to weigh against this wording]
QUOTE[TBWTT-7:72]: après m’avoir dit qu’il ne reviendrait que quand ce qu’il m’avait demandé serait accompli ENDQUOTE
- [R3.43] TBWTT-7:79 | N | "It will soon be given to us" to create life on other worlds | undated(bientôt) · uncond
- [R3.44] TBWTT-7:81 | N | When we are numerous enough worldwide awaiting them with respect and love, "they will come" and share their knowledge | undated · cond
- [R3.45] TBWTT-7:83 | N | "We are very quickly going to be numerous enough to undertake the choice of the land" for the residence | undated(très vite) · uncond · commits to: rapid growth sufficient to choose a site
QUOTE[TBWTT-7:83]: Nous allons très vite être assez nombreux pour entreprendre le choix du terrain où s’élèvera la résidence. ENDQUOTE
- [R3.46] TBWTT-1:44 | Y | "According to their reactions we will see" whether to show ourselves | undated · cond
- [R3.47] TBWTT-1:51, 5:53 | Y | You cannot reach us with current knowledge; "we have nothing to fear for the moment" | present-limit statement
- [R3.48] "already fulfilled / happening now" claims: 3:225 (Israel regained its land), 3:223 & 3:227 (Daniel now understandable), 4:101 (antivenom, surgery: "ce qui se passe maintenant"), 4:104 (UFOs en pagaille), 4:113 (Israel = sign), 5:4 (Aquarius since 1946; "les temps sont venus"), 5:32-34 (medicine conquering infant mortality) | Y | The present (1973) is read as fulfilment of scripture | retrospective fulfilment claims, not predictions

## R4 — Checkable-in-principle statements (nature, history, places, datable life events)

### Raël's life and the encounter
- [R4.1] TBWTT-1:1 | N | Founded a motor-sport review "three years ago"; raced; about ten cups | bears: press registration records, race results
- [R4.2] TBWTT-1:2-3 | N | Morning of 13 December 1973, volcanoes above Clermont-Ferrand; walked to the centre of the crater of the "Puy-de-Lassolas"; air cool, sky rather grey with mist | bears: place exists and is a scoria cone with accessible crater; weather archive for that date [outside knowledge — unverified]
- [R4.3] TBWTT-1:3 | N | Lava flowed there "some thousands of years ago" | bears: dating of the Chaîne des Puys eruptions [outside knowledge — unverified]
- [R4.4] TBWTT-1:4-6, 1:41, 1:64, 2:92 | N | Craft ~7 m diameter, ~2.5 m high, silent, red flashing light below, white flash above, hovered 2 m; occupant ~1.20 m, long black hair, small beard, greenish-white skin, green one-piece suit; rose to ~400 m; turned red, white, blue-violet and vanished | bears: none independent — single witness, no camera (1:5), no third party (7:36-37: an automatic system would warn of anyone approaching)
- [R4.5] TBWTT-1:22, 5:67 | Y | Claude Vorilhon, editor of a small motor-sport review, married, father of two; son named Ramuel | bears: civil records
- [R4.6] TBWTT-1:46-47 | Y | Jewish father, Catholic mother; born 1946 | bears: civil/family records
- [R4.7] TBWTT-1:37 | R | Bought a Bible only "a few days" before | bears: none stated (the Bible used transliterates "Iahvé"/"Elohim" throughout the quotations — an edition is identifiable from the quoted wording)
- [R4.8] TBWTT-7:16 | R/N | Six consecutive mornings of meetings (13–18 Dec 1973 by implication) | bears: whereabouts on those mornings
- [R4.9] TBWTT-1:47 | Y | First atomic explosion took place in 1945 | bears: historical record

### Language, texts, translation
- [R4.10] TBWTT-2:5, 3:251, 5:21, 7:33 | Y | "Elohim" means in Hebrew "those who came from the sky", "literally 'come from the sky'"; is plural; is the plural of "Eloha" | bears: Hebrew lexicography/morphology
QUOTE[TBWTT-2:5]: Elohim, injustement traduit dans certaines Bibles par Dieu, veut dire en Hébreu «ceux qui sont venus du ciel» et est bel et bien au pluriel. ENDQUOTE
- [R4.11] TBWTT-4:24 | Y | Matt 5:3 originally meant "the poor, if they have spirit, will be happy" | bears: Greek text of Matt 5:3
- [R4.12] TBWTT-5:44 | Y | "Mamon: wealth in Aramaic" | bears: Aramaic lexicon
- [R4.13] TBWTT-5:66-67 | Y | "RAËL" literally "light of God"; "Ramuel" = "son of the one who brings the light" | bears: Hebrew lexicon/onomastics
- [R4.14] TBWTT-7:35 | Y | The Elohim official language "closely resembles ancient Hebrew" | bears: nothing available; in principle, any specimen of the language
- [R4.15] TBWTT-3:192 | Y | Scribes "should have written" *sains* not *saints* | ANALYSIS: the confusion exists only in French; bears: Hebrew of Ezek 42:14
- [R4.16] TBWTT-3:171 | Y | A scroll written on both sides was surprising "at a time when one wrote on only one side of parchments" | bears: history of ancient writing practice
- [R4.17] TBWTT-3:235 | Y | 20 cubits = 9 m; 10 cubits = 4.50 m (cubit = 0.45 m) | bears: metrology
- [R4.18] TBWTT-5:51 | Y | The Kabbalah, in/on the Song of Songs (V), gives the "height of the creator" as 236,000 parasangs and the "height of his heels" as 30 million parasangs | bears: locating these figures in a Kabbalistic text (the text names no title) [outside knowledge — unverified: figures of this kind are associated with the Shi'ur Qomah literature]
QUOTE[TBWTT-5:51]: Il y est dit que la «hauteur du créateur» est de 236 000» parasanges» et que la «hauteur de ses talons» est de 30 millions de «parasanges». ENDQUOTE
- [R4.19] TBWTT-5:52 | Y | The parasang, "like the parsec", is a unit equal to the distance light travels in one second, ~300,000 km | bears: historical metrology [outside knowledge — unverified: the parasang is ordinarily described as an ancient Persian road measure of a few kilometres]
QUOTE[TBWTT-5:52]: Le parasange qui, comme le parsec, est une unité de mesure, équivaut à la distance que parcourt la lumière en une seconde soit environ 300 000 kilomètres. ENDQUOTE
- [R4.20] TBWTT-6:11-13 | Y | 49-year leases are "already prescribed in the Bible" (Lev 25) | bears: text of Leviticus 25
- [R4.21] TBWTT-2:60, 2:62 | Y | Gen 7:17 says the ark rose "above the earth", not on the waters; three storeys = three-stage rocket | bears: Hebrew of Gen 7:17
- [R4.22] TBWTT-3:71 | Y | The text itself says the battle lasted "almost a whole day" | bears: Josh 10:13

### Cosmology, physics, astronomy
- [R4.23] TBWTT-5:52 | Y | Their planet is 30 million parasangs away = ~9 thousand billion km = "a little less than one light-year" | ANALYSIS: arithmetic is internally consistent (3×10^7 × 3×10^5 km = 9×10^12 km; 1 ly ≈ 9.46×10^12 km). bears: stellar census within 1 ly of the Sun [outside knowledge — unverified: nearest known star is over 4 ly away]
QUOTE[TBWTT-5:52]: Notre planète est à 30 millions de parasanges soit neuf mille milliards de kilomètres environ ou un peu moins d’une année lumière. ENDQUOTE
- [R4.24] TBWTT-5:52 | Y | Present rockets go only 40,000 km/h and would need "nearly 26,000 years" | ANALYSIS: consistent (9×10^12 / 4×10^4 h ≈ 25,700 yr); the figure coincides with the "25,000 years" of scientific lead (5:56, 7:21) and of the speaker's age (7:56)
- [R4.25] TBWTT-5:53 | Y | They travel in "less than two months" on rays "seven times faster than light"; craft leave the optical window; observers see them turn bright white, then blue, then vanish; a craft exceeding light speed "disappears" | ANALYSIS: consistent with 5:52 (0.95 ly ÷ 7 ≈ 50 days). bears: physics of superluminal propagation; sighting reports
QUOTE[TBWTT-5:53]: nous permettant de nous déplacer à la vitesse de rayons qui sont sept fois plus rapides que la lumière ENDQUOTE
- [R4.26] TBWTT-5:53 | Y | Their planet is 236,000 parasangs = 70.8 billion km from its sun, "a big star" | ANALYSIS: arithmetic consistent (236,000 × 300,000 = 7.08×10^10 km ≈ 470 AU). bears: a large star within ~1 ly; habitability at that orbital distance
QUOTE[TBWTT-5:53]: La planète des créateurs est éloignée de son soleil de 236 000 parasanges, soit 70 milliards huit cent millions de kilomètres ENDQUOTE
- [R4.27] TBWTT-5:57 | Y | Their transmitters use waves "seven times faster than radio waves", undetectable by our technique; they are testing waves 1.5× faster again | bears: detection of superluminal signalling
- [R4.28] TBWTT-5:57-59 | Y | Planets and stars are atoms of a gigantic being; intelligent beings live on particles in the infinitely small ("we were able to discover"); infinite in both directions | bears: particle physics at ever smaller scales; stated as their discovery, no method given
QUOTE[TBWTT-5:57]: Nous avons en effet pu découvrir que dans l’infiniment petit, des êtres vivants intelligents vivent sur des particules qui sont pour eux des planètes et des soleils ENDQUOTE
- [R4.29] TBWTT-2:10, 5:4, 5:7 | Y | A Genesis "day" = the period the sun rises in one sign at the spring equinox, "about two thousand Earth years"; Earth entered Aquarius in 1946; work on Earth decided 22,000 years ago | bears: precession rate; constellation boundaries; date of equinox point entering Aquarius [outside knowledge — unverified: one-twelfth of the precession cycle is ~2,150 yr; astronomical boundary dates differ from 1946]
QUOTE[TBWTT-2:10]: Le «jour» correspond à la période pendant laquelle votre soleil se lève sous le même signe le jour de l’équinoxe de printemps, soit deux mille ans terrestres environ. ENDQUOTE
- [R4.30] TBWTT-7:17, 7:19 | Y | An "intergalactic vessel" with nine aboard stays constantly near Earth | bears: space surveillance
- [R4.31] TBWTT-7:4 | Y | Invisible helmet of repulsor rays passing waves but not air molecules | bears: none available

### Geology, Earth history
- [R4.32] TBWTT-2:7, 2:12 | Y | Earth was then entirely covered with water and thick mists | bears: geological record at the implied date (<25,000 yr)
- [R4.33] TBWTT-2:14 | Y | The sea floor was shallow and about equal everywhere; strong explosions piled matter into one place, forming a single original continent; "your scientists have just realised" the drifted continents fit into one | bears: marine geology; age of continental crust; plate-tectonic chronology. NB the text cites contemporary science as agreeing
QUOTE[TBWTT-2:14]: À l’origine, il n’y avait qu’un continent sur la Terre et vos savants viennent d’ailleurs de s’apercevoir que tous les continents qui ont dérivé s’emboîtent parfaitement pour n’en former qu’un seul. ENDQUOTE
- [R4.34] TBWTT-2:28 | Y | Israel was then not far from Greece and Turkey on the single continent | bears: palaeogeography
- [R4.35] TBWTT-2:58, 2:60-64 | Y | Flood = nuclear missiles from the home planet; a huge tidal wave submerged the continent and destroyed all life; life preserved "some thousands of km" above Earth; fallout waited out; radioactivity removed "scientifically" | bears: global isotopic/fallout horizon; continuity of biological and archaeological records
- [R4.36] TBWTT-2:83-87 | Y | Sodom and Gomorrah destroyed by an atomic bomb; "as you now know", atomic burns kill making victims resemble a statue of salt | bears: site geology/radiology; medical description of blast casualties
- [R4.37] TBWTT-3:271, 3:292-294, 5:54 | Y | Creators had seven bases; on high mountains "where traces of high civilisations are now found (Himalaya, Peru, etc.)", later under the seas; also Andes, Himalaya, Greece | bears: archaeology of named regions; attribution is the text's
- [R4.38] TBWTT-4:49 | Y | A wholly vegetal planet "still exists"; two other relatively near planets bear human-like beings by the same creators | bears: exoplanet biosignature surveys (in principle)

### Biology, origins, medicine
- [R4.39] TBWTT-2:16, 2:20-25 | Y | Creation order day by day: plants from chemicals → plankton, small then large fish, algae → birds → dinosaurs ("dragons") → land herbivores → carnivores → humans | bears: fossil succession and dates
- [R4.40] TBWTT-5:62 | Y | Order restated: unicellular first; then fish, batrachians, mammals, birds, primates, man — "an improved model of ape" | ANALYSIS: differs from ch. 2 (birds before land animals there; mammals before birds here). bears: fossil succession
QUOTE[TBWTT-5:62]: En réalité le premier organisme vivant créé sur la Terre a bien été monocellulaire et a ensuite donné des êtres plus compliqués. Mais pas par hasard ! ENDQUOTE
- [R4.41] TBWTT-5:4, 7:56, 2:10 | Y | Timescale: work decided 22,000 years ago; the speaker is 25,000 years old and "himself directed the creation of life on Earth" | ANALYSIS: all terrestrial life, dinosaurs included (2:22), falls inside ~25,000 years on the text's own figures. bears: radiometric dating of fossils and rocks
QUOTE[TBWTT-7:56]: Le plus âgé, le président du conseil des Éternels a vingtcinq mille ans et vous l’avez devant vous. ENDQUOTE
- [R4.42] TBWTT-2:25, 2:62, 2:68 | Y | Each human race corresponds to one team of creators; each race was put back in its place of creation after the flood | bears: human population genetics
QUOTE[TBWTT-2:25]: Le nombre d’équipes de créateurs est facile à trouver; chaque race humaine correspond à une équipe de créateurs. ENDQUOTE
- [R4.43] TBWTT-5:64 | Y | Prehistoric skulls are those of successive human prototypes, supplanted by more evolved ones; successive hominian races dominated/annihilated each other | bears: palaeoanthropology, hominin dates
- [R4.44] TBWTT-2:43, 7:58 | Y | Human faculties are "slightly superior" to the creators'; the memory part of the human brain is larger | bears: nothing available on the comparison
- [R4.45] TBWTT-2:55, 3:84, 4:3 | Y | Creators and humans are interfertile; offspring inherit telepathic faculties | bears: none available
- [R4.46] TBWTT-2:43, 2:49, 2:53, 7:13, 7:30, 7:46 | Y | A "small surgical intervention" gives ~10× lifespan (750–1,200 years); not hereditary; patriarchs' ages are literal | bears: biology of ageing
- [R4.47] TBWTT-2:58, 3:184, 7:30 | Y | Any cell/particle of a body holds the information to rebuild the whole being; a machine supplies living matter; the re-created body has "all its scientific knowledge and its personality" as at sampling | bears: cloning biology (genome vs. memory) [outside knowledge — unverified: clones are not known to carry the donor's memories]
- [R4.48] TBWTT-3:184 | Y | "A spermatozoon possesses all the information to create a living being, down to hair or eye colour" | bears: genetics [outside knowledge — unverified: a sperm carries half the genome]
- [R4.49] TBWTT-7:61-62 | Y | "Your scientists have just discovered" that injecting memory liquid from a trained rat's brain makes an untrained rat know what the other knew; their children learn by such injections | bears: replication record of memory-transfer experiments [outside knowledge — unverified: such experiments were reported c. 1960s–70s and are generally regarded as not replicated]
QUOTE[TBWTT-7:62]: Vos savants viennent de découvrir que l’on peut en injectant dans le cerveau d’un rat le liquide de la mémoire d’un rat éduqué, faire en sorte que le rat qui n’a rien appris, sache ce que l’autre savait. ENDQUOTE
- [R4.50] TBWTT-3:85-86, 3:95 | Y | The brain is a transmitter; hair and beard are its antennas; telepathy with the creators works only when they are near Earth; "you have surely noticed" many scientists, prophets and sages are long-haired/bearded | bears: controlled tests of telepathy vs hair length
QUOTE[TBWTT-3:85]: Les antennes, ce sont les cheveux et la barbe. ENDQUOTE
- [R4.51] TBWTT-5:63 | Y | No natural need explains spiral horns, blue or red feathers, exotic fish: they are the work of "artists" | bears: sexual-selection and functional studies of ornaments
- [R4.52] TBWTT-3:63, 3:75 | Y | Amplified ultrasound can bring down "any concrete wall"; certain sounds pushed to the extreme can drive any man mad | bears: acoustics, physiology
- [R4.53] TBWTT-3:22, 3:46 | Y | Manna was a synthetic chemical food; Num 11:7-8 is a "very exact description" that "your chemists could reconstitute" | bears: an attempted reconstitution (the text proposes the test)
- [R4.54] TBWTT-3:111 | Y | Remote guidance of animals by electrode, "as you are beginning to discover" | bears: 1960s–70s neurostimulation literature
- [R4.55] TBWTT-3:138, 4:64 | Y | Astronauts' vitamin pills: one pill feeds a man; communion hosts derive their shape from such pills | bears: space-food history; liturgical history
- [R4.56] TBWTT-7:13 | Y | Humans live 75 years on average; two children per couple stabilises population | bears: demography

### History, society
- [R4.57] TBWTT-3:225, 5:4, 5:25, 5:31 | Y | The state of Israel was created "some tens of years ago"; Aquarius "is here since 1946, the epoch when the people of Israel regains its country" | bears: date of the state's creation [outside knowledge — unverified: 1948]
- [R4.58] TBWTT-6:4, 7:77 | Y/N | "Copernicus was condemned by a majority of incapable people" | bears: historical record of Copernicus's reception [outside knowledge — unverified: the condemnation usually cited is of Galileo; Copernicus's book was censured after his death]
- [R4.59] TBWTT-1:46 | Y | France is the country where democracy was born | bears: political history
- [R4.60] TBWTT-2:43, 3:142, 3:214 | Y | The people of Israel was the most intelligent creation ("the number of geniuses this race has produced"); its civilisation was in "constant regression" after dispersion; Persian and Greek high periods are due to "angels" placed among them | bears: history; the first is a value claim framed as observation
- [R4.61] TBWTT-6:16 | Y | Auvergnat is no longer spoken in Clermont-Ferrand | bears: sociolinguistic surveys (1973)
- [R4.62] TBWTT-5:56 | Y | Human military craft have several times tried to chase their craft | bears: military records of intercept attempts
- [R4.63] TBWTT-3:288, 3:305 | Y/editorial | Emblem on craft and suit: Star of David with a swastika at centre; "also the emblem of the Jewish people"; caption: "certainly the oldest symbol" on the planet | bears: iconographic history
- [R4.64] TBWTT-5:3-4, 5:21 | Y | "As you have noticed, the Christian Church is dying"; its extinction "has already begun" | bears: religious demography (which measure, which region is unspecified)

### Their world (uncheckable now; internally checkable)
- [R4.65] TBWTT-7:15, 7:19, 7:45-47 | Y | ~7 billion inhabitants; seven provinces; 700 eternals + 210 trainees (~70/yr, 10 per province); ~40 million children; ~1 million inactive; oldest know descendants to the 50th generation; cities of ~500,000 in ~1 km cubes | ANALYSIS (mine): 70 trainees/yr × 3 lives ≈ 210 is self-consistent; with a constant 7 billion and lives of 750–1,200 years, steady state implies roughly 6–9 million births a year, i.e. well over 100 million under-20s, against the stated 40 million — a tension unless the hedge "environ" or unstated assumptions absorb it
- [R4.66] TBWTT-7:56 | Y | 25,000 years old, 25 bodies | ANALYSIS: consistent with ~1,000-year bodies (7:30)
- [R4.67] TBWTT-2:5, 1:61, 3:42 vs 1:53 | Y | Planet "fairly similar to Earth" (1:53); atmosphere "very different" (1:61), "not quite identical" (2:5); a human would die there (3:42) | internal gradation of the same fact

## R5 — Declared unknowns, uncertainties, refusals

- [R5.1] TBWTT-1:49 | Y | Refusal: "a distant planet of which I will tell you nothing", lest unwise Earthmen disturb our tranquillity | refusal, reason given
QUOTE[TBWTT-1:49]: D’une lointaine planète dont je ne vous dirai rien de peur que, si les hommes de la Terre n’étaient pas sages, ils ne troublent notre tranquillité. ENDQUOTE
- [R5.2] TBWTT-1:52-53 | Y | "What is your name?" is answered "We are men like you" — no name given (collective name only at 7:33; no personal name anywhere in this book) | question deflected
- [R5.3] TBWTT-1:58-59 | Y | "Are you many?" — "More numerous than you" (figure only at 7:15) | deferred answer
- [R5.4] TBWTT-2:3, 4:116 | Y | Will not discuss the rest of the Bible / will not continue through the remaining New Testament | declared omission
- [R5.5] TBWTT-5:57 | Y | Will not answer radio searchers, so that the planet cannot be located; also transmission time and unknown waves | refusal
- [R5.6] TBWTT-5:65 | Y | Scientific knowledge withheld for now | refusal
- [R5.7] TBWTT-6:26 | Y | No open help, nothing usable as proof by sceptics, ever | refusal
- [R5.8] TBWTT-7:69-71 | Y | Will not bring Moses/Elijah/Jesus now | refusal
- [R5.9] TBWTT-4:72 | Y | How their "miracles" work is beyond even glimpsing; none will be explained | declared incomprehensibility
- [R5.10] TBWTT-5:58 | Y | "We did not know, in creating you, that we were accomplishing a secondary mission 'written' in us" | past ignorance admitted
QUOTE[TBWTT-5:58]: Nous ne savions pas, en vous créant, que nous accomplissions une mission secondaire, «écrite» en nous ENDQUOTE
- [R5.11] TBWTT-5:58, 7:25 | Y | Their own creators: never seen again; world not found; "their world certainly disintegrated" / "they must have disappeared" — inference, not observation | unknown, inferred
QUOTE[TBWTT-7:25]: nos créateurs à nous, que nous n’avons jamais revus et dont nous n’avons pu retrouver le monde. Ils ont dû disparaître. ENDQUOTE
- [R5.12] TBWTT-7:23 | Y | No civilisation as evolved as theirs found; creator-civilisations of nearby created worlds "impossible to find"; "perhaps we will find some farther"; this "makes us fear the worst" though nothing abnormal is seen in their system | unknown + fear
- [R5.13] TBWTT-5:59 | Y | "We will perhaps disappear one day"; humanity "certainly" develops elsewhere (surmise); "we are not sure that man can ever stabilise in abundance" | uncertainty
QUOTE[TBWTT-5:59]: Mais nous ne sommes pas sûrs que l’homme puisse jamais se stabiliser dans l’abondance. ENDQUOTE
- [R5.14] TBWTT-5:57 | Y | The great being is "surely" itself a parasite of other atoms; their research aims "to understand and enter into relation with" it — not yet achieved | ongoing research, unknown
- [R5.15] TBWTT-5:60 | Y | "The important thing is apparently" to create enough worlds… | hedge on purpose itself
- [R5.16] TBWTT-5:65 | Y | "It is moreover possible that" each creation brings a slight improvement | possibility only
- [R5.17] TBWTT-5:64, 3:284 | Y | Not sure humans will not turn against them; a minority ("Satan") thinks man a danger; "the majority of us think" otherwise | internal disagreement among the speakers disclosed
- [R5.18] TBWTT-7:6 | Y | "Perhaps they will destroy themselves"; "you do not know what you are exposing yourselves to" by nuclear tests (unspecified) | uncertainty; unspecified warning
- [R5.19] TBWTT-7:58 | Y | "I could not store much more" knowledge; man "will perhaps be superior" | own limit admitted
- [R5.20] TBWTT-3:164 | Y | In Ezekiel's time "we had not yet found the means" to see through metal walls | past limit of their science admitted
- [R5.21] TBWTT-7:13 | Y | "We are not eternal" (bodies), correcting Raël's "in a way immortal" | precision/correction
- [R5.22] TBWTT-6:20, 6:25 | Y | The threshold ("a large enough number", "numerous enough", "intensely enough") is never quantified | unspecified criterion
- [R5.23] TBWTT-1:31, 1:39 | R | Raël: "I don't know" why he came / why he bought a Bible | reporter's unknowns, then explained by telepathy
- [R5.24] TBWTT-7:39 | Y | Reactor fuels: "many other simple and safe materials", unnamed | unspecified
- [R5.25] null | — | No method, chemistry or mechanism of the creation of life is given anywhere beyond "from nothing other than chemicals" (2:16); no physical constant other than light speed (5:52) and rocket speed is stated | null result

## Patterns, tensions, counter-examples, null results (analysis)

1. Two-track standard of evidence. Track A ("preuve" = text): scripture is repeatedly called *the proof* (2:55, 3:125, 3:267, 4:2, 5:48) and Raël is promised "preuves incontestables" (1:44). Track B (no material proof): 6:26 refuses anything that could serve as proof and makes proofless belief the criterion of intelligence. The book never states that the "incontestable proofs" of 1:44 are the exegeses, but nothing else in it could be.
2. Proof runs upward. The only parties asked to *prove* anything are humans (4:51-55, 5:64, 7:13). The creators' past proofs (miracles, 3:113, 3:263, 4:21) are described as a discontinued policy.
3. Four distinct reasons for refusing demonstration: sceptic-aggression (6:26), revival of supernatural religion (7:71), crowd panic (4:72, 5:56), safety/location (5:56-57). They are not ranked.
4. One designated observable: rising UFO frequency (4:102, 6:28, 7:77, 7:83). It is the only confirmation the reader is told to look for, and it is unbounded in time and rate.
5. Verification is invited at the textual level (check the Bible verses; find a Kabbalah, 5:51; chemists could remake manna, 3:46; "you could realise for yourself", 5:63) and discouraged at the material level (6:26). Counter-example to "discourages inquiry": 4:71 praises those who "seek the why of things".
6. Belief vocabulary is not avoided: followers "croiront en vous, donc en nous" (6:23); the rewarded "auront cru dans les créateurs" (3:219); Jews punished for "manque de foi" (3:214) — alongside "no mysticism" (6:25) and "our only religion is human genius" (7:25).
7. No future date. Every forward statement is "bientôt / un jour / très vite / en temps voulu" or conditional; 6:27 explicitly allows the coming to fall after Raël's death. The nearest thing to a time-bound unconditional claim is 6:16 (French/English/German "soon" no longer spoken in their capitals) and 7:83 ("very quickly numerous enough" to choose the land).
8. The conditions for the coming are stacked and partly unquantified: followers "numerous enough", wish "intense enough", warlike temperaments "reduced to total impotence in the whole world" (6:25), plus a built residence with specified features (6:21-22) and an attempted neutral status. Only the building specification is auditable.
9. Self-declared limits of accuracy: "le plus fidèlement possible" (7:80); notes reordered and recopied (7:75); explicit "ceci est une image" inside the account (2:58, 3:169); simplification is designed in via the choice of a non-scientist (1:46); numbers are "environ".
10. Internal variances inside the six days: visit impossible (1:61) → possible (7:68); "nothing about the planet" (1:49) → distance and star (5:52-53); "time to think of it" (1:55) → under two months (5:53); creation order ch. 2 vs 5:62; "similar planet" vs "very different atmosphere".
11. Appeals to contemporary science as already agreeing: continental fit (2:14), ecology (2:20), animal electrodes (3:111), rat memory transfer (7:62), IQ tests (6:5), CPR and transplants (3:134, 4:36). Science is treated as catching up with, and thereby vouching for, the account.
12. Hard-number cluster is tightly self-consistent arithmetically (5:52-53: distance, rocket time, 7c travel time, 70.8 billion km) while resting on a unit definition (parasang = one light-second) that is itself a checkable claim. The demographic cluster (7:45-46) is less consistent.
13. The speakers are not presented as omniscient: they did not know their own role (5:58), have not found their creators (7:25), fear extinction (7:23), disagree among themselves about humanity (5:64), and are unsure about abundance (5:59).
14. Editorial layer: 3:305 is a third-person caption inside the dictated chapter; section titles are narrator-layer. The dump's speaker tags (e.g. 1:27 tagged Narrator though it is Raël's reply; 3:305 tagged Yahweh) are not reliable at the margins.
15. Null results: no physical constant beyond c; no mechanism of abiogenesis/engineering; no named star; no personal name for the speaker in this book (the tag "Yahweh" is the project's, not this book's dialogue); no third-party witness; no instruction to test the account experimentally other than the manna remark.

---

# ETTMTTP — epistemics registers (book 2, 1975)

Source of record: `texts/ETTMTTP.fr.txt`, read in full (ch. 1 = 77 paras, ch. 2 = 132, ch. 3 = 266). Paraphrases are what the text says; `[analysis]` marks my own inference; `[outside knowledge — unverified]` marks anything not in the dump.

Voice note (applies to every item): the dump tags ch. 1 `[Narrator]` (= Raël, first person), ch. 2 `[Narrator]`/`[Yahweh]`, ch. 3 almost wholly `[Yahweh]`. Two tagging problems: (a) ETTMTTP-2:74, 2:76, 2:77 are tagged `[Yahweh]` but are Raël's narration/reply; (b) ch. 3 "Les Clés" is NOT plain Elohim speech — it is introduced at 2:132 as text Raël wrote after finishing the narration while "not feeling the author", and it speaks of "nos créateurs les Elohim" in the third person and says "me"/"moi" of Raël (3:174–175, 3:208), switching to an Elohim "nous" only in places (3:241). I give the voice per item as: Raël / Yahweh (ch. 2 reported speech) / Keys (ch. 3 inspired-writing voice).

## Register 1 — self-description, transmission, accuracy, limits

- [R1.1] ETTMTTP-1:1 | Raël | Ch. 1 is retrospective: memories "mises bout à bout" showed him his life "avait véritablement été guidée" toward 13 Dec 1973 | retrospective-reconstruction
QUOTE[ETTMTTP-1:1]: Je fus surpris moi-même en fouillant dans mes souvenirs, alors que je pensais que rien d'extraordinaire ne s'était produit au début de ma vie, de constater que des scènes ressurgissaient ENDQUOTE
- [R1.2] ETTMTTP-1:2 | Raël | Autobiography was nearly written when the second encounter occurred; he then "résumé au maximum" the memoir to give room to the second message | editing, compression by author
QUOTE[ETTMTTP-1:2]: J'ai alors résumé au maximum le texte de mes souvenirs afin de donner la plus grande place au deuxième message ENDQUOTE
- [R1.3] ETTMTTP-1:3 | Raël | Writes "à l'heure où je mets ces lignes au propre"; the truth is "trop grande pour moi" | fair-copy stage, self-limit
- [R1.4] ETTMTTP-1:5 | Raël | After ~40 lectures, some points of the message "ont besoin d'être éclaircis", which he will try to do in this book | author as clarifier of the message
QUOTE[ETTMTTP-1:5]: je suppose que certains points du message ont besoin d'être éclaircis ce que je vais essayer de faire dans cet ouvrage ENDQUOTE
- [R1.5] ETTMTTP-1:6 | Raël | Childhood events had no significance to him "jusqu'à ce que j'en fasse la synthèse"; done only "très peu de temps" ago; prefers to tell all himself rather than let "mauvaises langues" | retrospective meaning-making, pre-emptive account
- [R1.6] ETTMTTP-1:47 | Raël | Infers "sans doute" that those guiding him did not want him too famous | hedged inference of guidance
- [R1.7] ETTMTTP-1:63 | Raël | First book was dictated: six consecutive days, about one hour each; he had wrongly named the site Puy-de-la-Vache, correct name Puy-de-Lassolas | dictation; self-correction of a place-name
QUOTE[ETTMTTP-1:63]: me dicta Le Livre qui dit la Vérité et ses fantastiques révélations1. J'avais d'ailleurs appelé à tort ce lieu le Puy-de-la-Vache, qui est le nom du volcan situé juste à côté du Puy-de-Lassolas. ENDQUOTE
- [R1.8] ETTMTTP-1:64 | Raël | Notes of book 1 were taken "le mieux possible, mais beaucoup trop vite"; he then made a fair copy ("mis au propre"); that became the "manuscrit original" | note-taking limits; two-stage text (notes → fair copy)
QUOTE[ETTMTTP-1:64]: Je mis tout d'abord au propre les notes que j'avais prises le mieux possible, mais beaucoup trop vite pendant que mon interlocuteur parlait. ENDQUOTE
- [R1.9] ETTMTTP-1:64 | Raël | Publisher (Marcel Jullian) wanted the life story first and "quelques petites choses à changer"; refused outright | refusal of editorial change
QUOTE[ETTMTTP-1:64]: il y aurait peut-être "quelques petites choses à changer". De tout cela il n'était absolument pas question. ENDQUOTE
- [R1.10] ETTMTTP-1:65 | Raël | Wanted "le message et uniquement le message" published, his person not being as important | message over messenger (but ch. 1 of this book then supplies the life)
- [R1.11] ETTMTTP-1:66–68 | Raël | Original manuscript left the author's hands for weeks (a "lecteur" took it away); recovered via Courrèges; he still wonders whether it was really mislaid or publication was being blocked | custody gap of the original MS; declared uncertainty
- [R1.12] ETTMTTP-1:69 | Raël | Self-publication chosen to keep "un contrôle permanent de l'utilisation de ces écrits" | editorial control retained by reporter
- [R1.13] ETTMTTP-1:75 | Raël | At lectures answers "venaient toutes seules"; felt "aidé d'en haut, comme cela m'avait été promis"; heard himself say things he could not find alone | claimed assisted speech
- [R1.14] ETTMTTP-2:7, 2:9 | Raël | Chose 6 Aug "sans trop savoir pourquoi, mais en fait les Elohim m'avaient guidé"; follows intuitions since told he could be guided telepathically | guidance inferred after the fact
- [R1.15] ETTMTTP-2:11 | Yahweh | The helmet/halo and flashing lights of 1973 were staged "techniques d'approche" matching the popular image of a space traveller; the two years were "une mise à l'épreuve" | admitted staging of the first encounter's appearance
QUOTE[ETTMTTP-2:11]: Tout cela n'était destiné qu'à vous tranquilliser en vous apparaissant sous des aspects correspondants à l'image qu'on se fait généralement d'un voyageur de l'espace. ENDQUOTE
- [R1.16] ETTMTTP-2:22 | Yahweh | Second message "complétera" the one "dicté en décembre 1973"; no notes this time — a technical means engraves everything in his mind | transmission mode changes: memory, not notes
QUOTE[ETTMTTP-2:22]: Vous n'avez rien pour prendre des notes, mais n'ayez pas peur, tout ce que je vais vous dire restera gravé dans votre esprit, car ici nous avons un moyen technique pour que vous vous rappeliez de tout ce que vous allez entendre. ENDQUOTE
- [R1.17] ETTMTTP-2:23 | Yahweh | A passage of the first message was "mal retranscrit" by Raël (possible Elohim intervention to destroy humanity) and must be rectified: "nous n'interviendrons pas" | explicit erratum to book 1; transcription error attributed to the reporter
QUOTE[ETTMTTP-2:23]: Pour commencer, il faut rectifier un passage du message que vous avez mal retranscrit concernant une intervention éventuelle de notre part pour détruire l'humanité. Il faut bien préciser que nous n'interviendrons pas. ENDQUOTE
- [R1.18] ETTMTTP-2:43 | Yahweh | Book 1's "seven times faster than light", as Raël "noted" it, "était vrai il y a vingt-cinq mille ans"; they now travel much faster | retro-qualification of a book-1 figure (not called an error)
QUOTE[ETTMTTP-2:43]: Dans le premier message vous avez noté que nous nous déplacions sept fois plus vite que la lumière, ceci était vrai il y a vingt-cinq mille ans lorsque nous avons débarqué sur la terre. ENDQUOTE
- [R1.19] ETTMTTP-2:50 | Yahweh | The "résidence" of the first message "est en fait" a whole planet; speaker now names himself Iahvé, president of the council of the eternals | staged disclosure / re-scaling of an earlier statement
QUOTE[ETTMTTP-2:50]: Cette résidence est en fait très grande puisqu'il s'agit d'une planète tout entière où vivent également les membres du conseil des éternels. Mon nom est Iahvé et je suis le président du conseil des éternels. ENDQUOTE
- [R1.20] ETTMTTP-2:59 | Yahweh | "bien d'autres choses que vous ne pourrez comprendre en une fois" make the world a paradise | limit of recipient's comprehension; content withheld
- [R1.21] ETTMTTP-2:73–74 | Yahweh, Raël | Yahweh predicts Raël's own future description will be "très proche de celle d'Ezéchiel"; Raël confirms what he saw "correspondait parfaitement" | the report's conformity to scripture announced in advance inside the report
QUOTE[ETTMTTP-2:73]: La description que vous allez faire est certainement très proche de celle d'Ezéchiel, mis à part le bruit que nous avons pu supprimer ENDQUOTE
- [R1.22] ETTMTTP-2:96–98 | Yahweh | A machine awakens dormant faculties; "À partir de maintenant" the Elohim see, hear and speak through Raël | post-1975 utterances of Raël given Elohim authority
QUOTE[ETTMTTP-2:98]: À partir de maintenant nous verrons par vos yeux, nous entendrons par vos oreilles et nous parlerons par votre bouche. ENDQUOTE
- [R1.23] ETTMTTP-2:100 | Yahweh | Select guides severely "pour que notre message ne soit jamais déformé ou trahi" | deformation risk acknowledged
- [R1.24] ETTMTTP-2:104 | Yahweh | "une révélation importante que vous pouvez faire dès maintenant" (Jews as direct descendants) | release permission ⇒ disclosure is staged
- [R1.25] ETTMTTP-2:129 | Yahweh | "Vous serez capable de commenter tout cela par vous-même une fois sur Terre" | licence for the reporter's own commentary
QUOTE[ETTMTTP-2:129]: Voilà, j'ai terminé. Vous serez capable de commenter tout cela par vous- même une fois sur Terre. ENDQUOTE
- [R1.26] ETTMTTP-2:131 | Raël | Back home he wrote "tout ce qui m'avait été dit" at once, "d'un trait sans aucune hésitation"; words "restés comme gravés" | written from memory immediately; claims verbatim recall
QUOTE[ETTMTTP-2:131]: Tout était parfaitement clair dans mon esprit et je fus surpris de m'apercevoir que j'écrivais tout cela d'un trait sans aucune hésitation pour retrouver les phrases que j'avais entendues. ENDQUOTE
- [R1.27] ETTMTTP-2:132 | Raël | After the narration, something "se déclenchait": he wrote while "le découvrant comme un lecteur", not feeling the author; sentence breaks off "Les Elohim commençaient à…" | third transmission mode: inspired/automatic writing; origin of ch. 3; lacuna or deliberate ellipsis in the dump
QUOTE[ETTMTTP-2:132]: J'écrivais mais je ne me sentais pas l'auteur de ce qui apparaissait sur le papier. ENDQUOTE
- [R1.28] ETTMTTP-3:1 | Keys | "Ces écrits sont des clés" for opening minds closed by millennia of obscurantism | self-characterisation: keys, not proofs
- [R1.29] ETTMTTP-3:5–9, 3:11, 3:19 etc. | Keys | Speaks of "les Elohim nos pères, nos créateurs" in third person, i.e. from the human side | voice is human "we", not Yahweh
- [R1.30] ETTMTTP-3:71, 3:84, 3:101, 3:160 | Keys | Refers back to "le Livre" and to "la première partie de ce livre" for geniocracy, urbanism, world government | books 1+2 treated as one book in two parts (edition signal)
QUOTE[ETTMTTP-3:84]: Comme cela est dit dans la première partie de ce livre ENDQUOTE
- [R1.31] ETTMTTP-3:174–175 | Keys (= Raël "me") | "De nombreux médiums sont venus me voir"; "J'attends avec impatience" | first person is Raël inside the "Yahweh"-tagged chapter
QUOTE[ETTMTTP-3:174]: De nombreux médiums sont venus me voir en me demandant ce qu'ils devaient faire ENDQUOTE
- [R1.32] ETTMTTP-3:179 | Keys | Ancient writings = messages "recopié tremblants de crainte" by "hommes primitifs et bornés"; the present message is given to beings addressed "comme à des adultes" | relative-reliability claim: this text over older scripture
- [R1.33] ETTMTTP-3:180 | Keys | Not the messenger but the sender and the message count | messenger discounted
- [R1.34] ETTMTTP-3:206–208 | Keys (= Raël "m'") | "Que ce livre guide…" those who believe "en ce qui m'a été révélé et en ce qui a été révélé avant moi" | book as guide; revelation vocabulary
- [R1.35] ETTMTTP-3:241 | Keys → Elohim "nous" | Voice shifts: "Respectez notre prophète… nous entendons par ses oreilles" | voice instability inside ch. 3
- [R1.36] ETTMTTP-3:242 | Keys | The messages given by the Elohim "sont dans la vérité"; the systems built on them are in error | truth-claim for all Elohim messages incl. older ones
- [R1.37] ETTMTTP-3:256 | Keys | "tout ceci n'est pas un conte" | genre disclaimer
- [R1.38] ETTMTTP-3:257 | Keys | Raël "n'a pas écrit ce qu'ont écrit Moïse, Ezéchiel…" and "n'est pas biologiste" — offered as ground for taking the synthesis seriously | argument from the reporter's non-authorship / non-expertise
QUOTE[ETTMTTP-3:257]: Raël existe, il est bien vivant, et il n'a pas écrit ce qu'ont écrit Moïse, Ezéchiel, Elie, Jésus, Mahomet, Bouddha et tous les autres, et il n'est pas biologiste ENDQUOTE
- [R1.39] ETTMTTP-3:259–260 | Keys | Counsels "de tes créateurs, transmis par la bouche de Raël"; "ce livre est le dernier, celui que tes propres prophètes t'annonçaient" | finality claim
- [R1.40] ETTMTTP-2:121 | Yahweh | Raël is "le premier prophète à ne pouvoir être compris que par les êtres évolués scientifiquement"; incomprehensible to primitives — "C'est là un signe" | intelligibility-to-science as the text's own authenticating sign
QUOTE[ETTMTTP-2:121]: Tous ceux qui ont les yeux ouverts verront que vous êtes le premier prophète à ne pouvoir être compris que par les êtres évolués scientifiquement. ENDQUOTE
- [R1.41] ETTMTTP-2:12, 2:14, 2:16, 2:44, 2:47, 2:67 | Raël | Narration is full of estimates ("devait avoir", "peut-être une centaine de kilomètres à l'heure, peut-être plus", "quelques secondes peut-être", language "qui ressemblait à de l'hébreux" not understood) | eyewitness approximations flagged as such
- [R1.42] ETTMTTP-2:105 vs 2:1–3, 2:114 | Yahweh / Raël | Yahweh (Oct 1975) says "le mouvement que vous avez créé, le Mouvement Raëlien" while Raël's frame (2:1–3) and Yahweh at 2:114 still say MADECH; closing address is "Religion Raëlienne… Genève" (3:265) | [analysis] later-edition wording inside reported 1975 speech; needs collation with the 1975 printing
QUOTE[ETTMTTP-2:105]: Car le mouvement que vous avez créé, le Mouvement Raëlien, doit être la religion des religions. J'insiste, c'est bel et bien une religion, mais une religion athée comme vous l'aviez déjà compris. ENDQUOTE
- [R1.43] ETTMTTP-1:76–77 | Raël | Press distorts (Le Point; La Montagne refuses coverage); good journalists report "exactement ce qu'ils ont vu ou ce qu'ils ont lu" | standard of accurate reporting stated by the author

## Register 2 — proof, belief, doubt, science vs religion, what convinces, refused proofs, embassy conditions, asks of the reader

- [R2.1] ETTMTTP-1:3 | Raël | 700 people "ont compris que LE LIVRE disait bien LA VÉRITÉ"; compares with the few who followed Jesus after two years | adherence counted as understanding
- [R2.2] ETTMTTP-1:4 | Raël | Followers are not "gogos": some hold degrees/doctorates; but he admires as much those without diplomas who "ont ressenti cela" | two warrants: credentials and feeling
QUOTE[ETTMTTP-1:4]: sans avoir par leurs études acquis des connaissances leur permettant de savoir que l'on peut créer scientifiquement de la matière vivante et des hommes comme nous, ils ont ressenti cela ENDQUOTE
- [R2.3] ETTMTTP-1:7 | Raël | Conception dated 25 Dec 1945; "Pour ceux qui croient au hasard, ma vie commence donc par un hasard" | coincidence offered as sign; chance dismissed rhetorically
- [R2.4] ETTMTTP-1:10 | Raël | Grandmother told of a 1947 silent craft over Ambert only after reading his book, when she also joined MADECH | post-hoc corroborating testimony from a family member
- [R2.5] ETTMTTP-1:13 | Raël | "Je sais maintenant exactement" whom père Dissard addressed and what the grandmother's craft was; counting to nine "comme un code" | certainty by retrospective reading
- [R2.6] ETTMTTP-1:67 | Raël | Chancel grasped it was fantastic "qu'on me croit ou qu'on ne me croit pas"; thousands of letters: "si quelques-uns riaient, beaucoup prenaient la chose très au sérieux" | reception as indicator
- [R2.7] ETTMTTP-1:72–75 | Raël | Mockers ("railleurs") made ridiculous by the smallness of their questions; full halls ⇒ "plus aucun doute quant à la réussite de ma mission" | success of mission inferred from audience size
- [R2.8] ETTMTTP-1:77 | Raël | Le Point turned a MADECH walk at the site into "un rendez-vous manqué avec les Elohim" — he denies any failed appointment | denial of a (reported) failed prediction/appointment
QUOTE[ETTMTTP-1:77]: il avait tout simplement transformé une promenade des membres du MADECH1 sur les lieux de la rencontre en un rendez-vous manqué avec les Elohim ENDQUOTE
- [R2.9] ETTMTTP-2:5 | Raël | 31 July 1975: craft seen with Marie-Paule and François at ~500 m; "très heureux que d'autres personnes soient avec moi"; read as "signe évident de l'accord des Elohim" | only multi-witness event in the book; value of co-witnesses acknowledged
QUOTE[ETTMTTP-2:5]: J'étais très heureux que d'autres personnes soient avec moi pour assister à ce spectacle ENDQUOTE
- [R2.10] ETTMTTP-2:6 | Raël | Next morning a circular red mark on the arm (3 cm, three inner circles → two concentric → white spot "que j'ai toujours"); "bien des gens me dirent" it was theirs; "Certains scientifiques ouverts" hypothesised a laser sample | physical trace offered; attribution by others; unnamed scientists; hypothesis only
QUOTE[ETTMTTP-2:6]: Certains scientifiques ouverts à qui j'ai montré cette marque ont émis l'hypothèse qu'il pouvait s'agir d'un prélèvement effectué grâce à un laser perfectionné. ENDQUOTE
- [R2.11] ETTMTTP-2:7 | Raël | 6 Aug meeting = 30th anniversary of Hiroshima and feast of the Transfiguration: "Hasard diront les imbéciles." | sceptical reading pre-labelled as stupid
- [R2.12] ETTMTTP-2:11 | Yahweh | "vous nous avez prouvé que nous pouvions vous faire confiance" | proof flows from Raël to the Elohim, not the reverse
- [R2.13] ETTMTTP-2:25 | Yahweh | "Des milliers de contacts ont confirmé cette règle absolue": beings able to leave their planetary system are always peaceful | inductive-evidence idiom ("confirmed by thousands of contacts")
- [R2.14] ETTMTTP-2:28 | Yahweh | Millions are still primitives "incapables de voir quelque chose dans le ciel sans y voir une manifestation 'divine'" | religion as misperception
- [R2.15] ETTMTTP-2:29 | Yahweh | Deist religions are "entretenu" by visitors from other planets who pass themselves off as gods; the Elohim still stage "apparitions" on Earth to see "si cela prend toujours" and how governments/press react: "Nous nous amusons souvent beaucoup" | admitted ongoing deception of observers; sightings are not offered as honest evidence
QUOTE[ETTMTTP-2:29]: Nous continuons d'ailleurs sur terre à faire des "apparitions" afin de voir si cela prend toujours et quelles sont les réactions des pouvoirs publics, des gouvernements et de la presse. Nous nous amusons souvent beaucoup... ENDQUOTE
- [R2.16] ETTMTTP-2:30 | Yahweh | No god, "évidemment pas d'âme"; intelligent life in the infinitely small: "cela nous avons pu le prouver" | proof asserted, not shown
QUOTE[ETTMTTP-2:30]: Vous savez également que nous avons découvert que sur l'infiniment petit il y a de la vie intelligente organisée, très certainement aussi évoluée que nous et comparable à ce que nous sommes nous-mêmes ; cela nous avons pu le prouver. ENDQUOTE
- [R2.17] ETTMTTP-2:33 | Yahweh | "Aucun argument" for a god or soul "ne tient debout" once infinity is glimpsed; no paradise anywhere since an infinite universe has no centre | deductive argument from infinity
- [R2.18] ETTMTTP-2:34 | Yahweh | Anticipated objection ("vous ne pouvez pas dire ce qu'il y avait au commencement") is a "question stupide" | objection named and dismissed
QUOTE[ETTMTTP-2:34]: question stupide qui prouve que la personne qui pose cette question n'a pas pris conscience de l'infini qui existe dans le temps comme dans l'espace ENDQUOTE
- [R2.19] ETTMTTP-2:36 | Yahweh | Belief in gods explained by the finite brain's need to bound the universe; those who ask whether there is life elsewhere are "cerveaux bornés" (frogs-in-pond simile from Raël's lecture, which "nous a beaucoup plu") | psychological account of belief; Elohim monitor Raël's lectures
- [R2.20] ETTMTTP-2:40 | Yahweh | "Il n'est pas prouvé que ceux qui sont 'morts pour la France' aient eu raison" | burden-of-proof idiom used against patriotism
- [R2.21] ETTMTTP-2:70–74 | Yahweh, Raël | A biological robot is made before Raël's eyes; matched to Ezekiel's dry-bones passage | demonstration given to the reporter only
- [R2.22] ETTMTTP-2:77–80 | Raël, Yahweh | Replica of his mother from a photo, replica of himself from a forehead cell; "encore une preuve, s'il en était besoin, de l'inexistence de l'âme" | "proof" = private demonstration; reader must take it on report
QUOTE[ETTMTTP-2:80]: Ceci est encore une preuve, s'il en était besoin, de l'inexistence de l'âme, à laquelle croient certains primitifs, ou d'une entité purement spirituelle propre à chaque corps ENDQUOTE
- [R2.23] ETTMTTP-2:82 | Yahweh | Those who, "bien qu'ayant tous les éléments en main pour comprendre d'où ils venaient, n'ont pas su reconnaître la vérité", are listed with the violent among those recreated for punishment | non-recognition made culpable
QUOTE[ETTMTTP-2:82]: ceux qui, bien qu'ayant tous les éléments en main pour comprendre d'où ils venaient, n'ont pas su reconnaître la vérité, seront recréés pour subir le châtiment qu'ils méritent ENDQUOTE
- [R2.24] ETTMTTP-2:98 | Yahweh | Elohim "pourrons même guérir par vos mains — comme nous guérissons déjà à Lourdes" — only certain sick people judged deserving for spreading the messages | healings: selective, merit-gated, hence not a public test
- [R2.25] ETTMTTP-2:99, 2:112 | Yahweh | Readers who follow and help Raël will be received in paradise; those who believed Jesus and Muhammad live eternally, their critics "seront recréés pour leur châtiment" | reward for belief/help, sanction for criticism
QUOTE[ETTMTTP-2:112]: ainsi que Mahomet et tous ceux qui les ont suivis et qui les ont crus, tandis que ceux qui les ont critiqués seront recréés pour leur châtiment ENDQUOTE
- [R2.26] ETTMTTP-2:103 | Yahweh | Mediums' gift is telepathy; belief in the "surnaturel", magic, etheric body is "on ne peut plus stupides"; they really contact people recreated on the planet | naturalising re-description; supernatural belief rejected
- [R2.27] ETTMTTP-2:105 | Yahweh | "Les gens qui croient en vous et donc en nous doivent vous aider"; an atheist religion; today's risk is only "l'ironie des imbéciles"; "il est plus aisé que jamais de suivre son intuition" | belief in messenger = belief in senders; intuition as guide
- [R2.28] ETTMTTP-2:106–111 | Yahweh | Quotes Qur'an 21:1–5 ("Qu'il nous apporte un miracle…") and Matthew 27 ("Qu'il descende… de la croix") as examples of sarcasm prophets suffered | the demand for a miracle/sign is classed as mockery — the nearest thing in this book to a refusal of proof
QUOTE[ETTMTTP-2:109]: C'est un poète. Qu'il nous apporte un miracle comme ceux qui ont été envoyés dans les temps passés ENDQUOTE
- [R2.29] ETTMTTP-2:121–122 | Yahweh | Raël is "celui dont les anciens prophètes… ont annoncé la venue dans toutes les religions"; "relisez vos écrits et ouvrez les yeux" | proof by fulfilment of scripture; reader sent to texts
- [R2.30] ETTMTTP-2:104, 2:122–128 | Yahweh | Embassy condition: Israel "doit donner un territoire situé près de Jérusalem" to the Guide of guides for "la résidence, l'ambassade des Elohim"; Israel must recognise Raël | embassy = test of recognition for Israel, not (here) a condition stated for the Elohim's arrival
QUOTE[ETTMTTP-2:122]: L'Etat d'Israël doit donner un territoire situé près de Jérusalem au Guide des guides afin qu'il y fasse édifier la résidence, l'ambassade des Elohim. ENDQUOTE
- [R2.31] ETTMTTP-2:114, 2:120, 3:69, 3:263 | Yahweh / Keys | Pending the embassy: a monastery of guides; the Guide of guides will be its guardian and may live there; frontal-bone fragments to be kept there; believers must fund it "pour accueillir les Elohim" | embassy functions: residence, relic depository, reception
- [R2.32] ETTMTTP-3:2 | Keys | Society fears what is behind the door; Gandhi: "Ce n'est pas parce que nul ne voit la vérité qu'elle devient une erreur"; ignore the sarcasm of those who saw nothing | consensus is not a criterion; mockery to be ignored
- [R2.33] ETTMTTP-3:3 | Keys | Guides are "des témoins vivants du bonheur" and "la preuve" that the fearful are wrong | proof = lived testimony of adherents
- [R2.34] ETTMTTP-3:8, 3:18 | Keys | Question "en permanence" all society's habits and traditions; teach the child to keep distance from what society and schools inculcate | critical stance prescribed — toward society
- [R2.35] ETTMTTP-3:10, 3:20 | Keys | Impose no religion on a child; teach the religions "sans parti pris", then the outline of this message; let the child choose | non-imposition; informed choice
- [R2.36] ETTMTTP-3:15 | Keys | Creators treat us as individuals, hence "n'interviennent pas pour nous aider directement" | rationale for non-intervention
- [R2.37] ETTMTTP-3:25–26 | Keys | Believing at the approach of death "en un dieu quelconque, ou aux Elohim" does not earn eternity; one is judged on acts | belief alone insufficient (counter-example to belief-salvation passages)
QUOTE[ETTMTTP-3:25]: il ne faut pas croire qu'il suffit de se mettre, lorsque la mort est proche, à croire en un dieu quelconque, ou aux Elohim, pour avoir droit à l'éternité ENDQUOTE
- [R2.38] ETTMTTP-3:69 | Keys | From the day one learns of the message the automatic cell-sampling at death is "déconnecté"; only those who then "appliqueront exactement ce qu'il demande" are recreated | knowledge of the message raises the stakes: reading is not neutral
QUOTE[ETTMTTP-3:69]: car seuls ceux qui, ayant pris connaissance du message, appliqueront exactement ce qu'il demande, seront ainsi recréés ENDQUOTE
- [R2.39] ETTMTTP-3:91, 3:117–118, 3:125, 3:207–208, 3:240, 3:260, 3:266 | Keys | Adherents are defined throughout as those "qui croient aux Elohim", "croient aux messages"; prayer text: "je crois en lui et dans les messages"; "sûrs que la réincarnation scientifique est une réalité" | belief vocabulary is the standard self-designation
QUOTE[ETTMTTP-3:260]: d'autres personnes qui comme toi sont raëliens, c'est-à-dire croient aux messages transmis par Raël ENDQUOTE
- [R2.40] ETTMTTP-3:165–168 | Keys | "La science est la chose la plus importante"; keep up with all discoveries; "La science doit être ta religion"; trust scientists not manipulated by financial interests "et seulement à ceux-là" | science-as-religion; conditional trust in scientists
QUOTE[ETTMTTP-3:166]: La science doit être ta religion, car les Elohim, tes créateurs, t'ont créé scientifiquement. ENDQUOTE
- [R2.41] ETTMTTP-3:177 | Keys | Whatever you do not understand and your scientists cannot explain "est dû aux Elohim" (watchmaker image) | explicit gap-attribution rule
QUOTE[ETTMTTP-3:177]: N'oublie jamais que tout ce que tu ne comprends pas et que tes scientifiques ne peuvent expliquer est dû aux Elohim, car l'horloger connaît tous les rouages de la montre qu'il a fabriquée. ENDQUOTE
- [R2.42] ETTMTTP-3:178–179 | Keys | Apocalypse (= "l'âge de la révélation") has arrived "comme cela était prévu"; false prophets = horoscope-makers and scriptural literalists who refuse science; many fanatic sects | sign-reading from the present; literalism rejected
- [R2.43] ETTMTTP-3:181–183 | Keys | Truth is not in the Himalaya or Peru: "la vérité est en toi"; the East has nothing to teach the West | inward criterion of truth
- [R2.44] ETTMTTP-3:116–117, 3:185–190 | Keys | Daily telepathic attempt; group "tentative"; do not cut hair/beard for quality; "ne t'impatiente pas si tu n'obtiens pas de résultat tout de suite" (atrophied organ) | practice whose null result is explained in advance
- [R2.45] ETTMTTP-3:201 | Keys | Lie under the stars, be ready to do exactly what they ask "même si tu ne comprenais pas très bien pourquoi"; "Tu verras peut-être un signal si tu es suffisamment prêt" | personal sign possible, conditional on readiness; obedience without understanding
QUOTE[ETTMTTP-3:201]: Tu verras peut-être un signal si tu es suffisamment prêt. ENDQUOTE
- [R2.46] ETTMTTP-3:202 | Keys | Perception is limited: gravity, radio/TV waves, magnetism are unseen yet real; pigeons find north | analogy argument for unperceived realities
- [R2.47] ETTMTTP-3:210 | Keys | Useless to speak of the message to "ceux qui ne sont pas éveillés" | audience restriction; unreceptive not to be argued with
- [R2.48] ETTMTTP-3:218 | Keys | "Comment ne pouvez-vous pas croire à tout cela alors que maintenant la science et les religions anciennes se recoupent parfaitement." | stated ground of belief: convergence of science and old religions
QUOTE[ETTMTTP-3:218]: Comment ne pouvez-vous pas croire à tout cela alors que maintenant la science et les religions anciennes se recoupent parfaitement. ENDQUOTE
- [R2.49] ETTMTTP-3:220 | Keys | Elohim act on individuals; "Malheur à ceux qui prétendent les avoir rencontrés… alors que ce n'est pas vrai" — their life will become hell | sanction on false contact claims (implicitly an argument for Raël's sincerity)
- [R2.50] ETTMTTP-3:221 | Keys | Opponents of the Guide will see their life become hell "sans que rien ne paraisse être dû à quelques chose venu d'en haut" | sanction declared undetectable as intervention
QUOTE[ETTMTTP-3:221]: ils sauront pourquoi, sans que rien ne paraisse être dû à quelques chose venu d'en haut ENDQUOTE
- [R2.51] ETTMTTP-3:222–223 | Keys | Readers who smile "auraient crucifié Jésus"; mockers send dissenters to psychiatric asylums | scepticism equated with persecution
QUOTE[ETTMTTP-3:222]: Vous qui souriez en lisant ces lignes, vous êtes de ceux qui auraient crucifié Jésus si vous aviez vécu à cette époque ENDQUOTE
- [R2.52] ETTMTTP-3:224 | Keys | Ask believers in eternal life why they weep at a death | consistency test put to other believers
- [R2.53] ETTMTTP-3:225 | Keys | Belief in an impalpable god was "normal" before science; now man "n'a plus le droit" to it; the Elohim "entendent être reconnus" by those able to understand how life can be created "et de faire le rapprochement avec les écrits anciens"; those get eternity | science licenses the shift; recognition demanded and rewarded
QUOTE[ETTMTTP-3:225]: Les Elohim, nos créateurs, entendent être reconnus par ceux qui sont maintenant capables de comprendre comment la vie peut être créée et de faire le rapprochement avec les écrits anciens. ENDQUOTE
- [R2.54] ETTMTTP-3:226–229 | Keys | Christian, Jew, Buddhist ("tes écrits indiquent que le nouveau Bouddha doit naître en Occident ; reconnais les signes prévus"), Muslim each told their own tradition points to Raël | appeal to each tradition's expectations
- [R2.55] ETTMTTP-3:234–236 | Keys | Noah was not believed; unbelievers at Sodom destroyed; "Vous pouvez encore ne rien en croire, mais quand le moment sera venu vous repenserez à ces lignes, mais il sera trop tard." | disbelief permitted but warned; vindication deferred to catastrophe
QUOTE[ETTMTTP-3:236]: Vous pouvez encore ne rien en croire, mais quand le moment sera venu vous repenserez à ces lignes, mais il sera trop tard. ENDQUOTE
- [R2.56] ETTMTTP-3:239 | Keys | Qur'an 56:15–23 cited: paradise "Seront la récompense de leur foi" | faith-reward vocabulary taken over via quotation
- [R2.57] ETTMTTP-3:241 | Keys/Elohim | "Vous qui croyez, ne portez pas de jugements sur les actions ou les paroles des Elohim. Le créé n'a pas le droit de juger son créateur"; nor on the prophet's acts and words | explicit prohibition of critical judgment by believers
QUOTE[ETTMTTP-3:241]: Vous qui croyez, ne portez pas de jugements sur les actions ou les paroles des Elohim. Le créé n'a pas le droit de juger son créateur. Respectez notre prophète et ne portez pas de jugement sur ses actions et sur ses paroles ENDQUOTE
- [R2.58] ETTMTTP-3:246 | Keys | Addresses those "qui ressentez que ce message est véridique" | felt truth as entry criterion
- [R2.59] ETTMTTP-3:256–257 | Keys | Verification programme given to the reader: reread the old prophets, learn the latest scientific (esp. biological) discoveries, look at the sky (UFOs "apparaissent chaque jour" = "signes dans le ciel"), then "Fais donc la synthèse" | invitation to check — by synthesis of three public sources
QUOTE[ETTMTTP-3:256]: Relis tous les écrits des anciens prophètes, prends connaissance des dernières découvertes scientifiques, notamment biologiques, et regarde le ciel. Les signes annoncés sont là ! ENDQUOTE
- [R2.60] ETTMTTP-3:261 | Keys | Make the message known "sans jamais chercher à convaincre"; if people are ready "ils s'ouvriront d'eux-mêmes" | no persuasion; self-selection of the ready
QUOTE[ETTMTTP-3:261]: fais en sorte qu'autour de toi, nul n'ignore ces fantastiques révélations, sans jamais chercher à convaincre ceux à qui tu en parles ENDQUOTE
- [R2.61] ETTMTTP-2:116, 3:70, 2:118, 3:71, 3:263 | Yahweh / Keys | Reader obligations: present oneself once to the Guide (cellular-plan transmission by manual contact), think of the Elohim daily, spread the message, give ≥1% of income yearly, host the regional guide, bequeath to the Guide, "prouver" one's love by aiding the embassy | what the reader is asked to do
- [R2.62] ETTMTTP-2:98, 2:113, 3:69 | Yahweh / Keys | All humans are permanently observed by "immenses ordinateurs" and scored | unobservable surveillance claim underpinning the sanctions
- [R2.63] NULL | — | This book contains no explanation of why there is no public landing, no offer of a physical proof for the public, and no statement that the Elohim will come when the embassy is built (only "pour accueillir les Elohim", 3:263; "préparer la venue de nos créateurs", 3:260) | null result

## Register 3 — forward-looking statements

Tags: D = dated, U = undated; C = conditional, X = unconditional. "Commits to" is judged on wording alone.

- [R3.1] ETTMTTP-1:4 | Raël | MADECH "est en route et rien ne pourra plus l'arrêter" | U, X | commits to: the movement continuing; (MADECH as an organisation is restructured within this same book, 2:1–3)
- [R3.2] ETTMTTP-1:77 | Raël | "un jour viendra où ceux qui ont cherché à cacher ou à déformer la vérité regretteront leurs erreurs" | U, X
- [R3.3] ETTMTTP-2:22 | Yahweh | Rest of the mission "sera peut-être plus difficile"; "vous serez récompensé de vos efforts quoi qu'il arrive" | U; hedged / X promise to Raël
- [R3.4] ETTMTTP-2:23 | Yahweh | "nous n'interviendrons pas"; humanity's future "ne dépend plus que d'elle-même" | U, X | commits to: no Elohim intervention to destroy humanity
- [R3.5] ETTMTTP-2:23 | Yahweh | If humanity masters its aggression → "l'âge d'or de la civilisation interplanétaire"; if violent → self-destruction "soit directement, soit indirectement" | U, C (two-branch fork; no branch predicted)
QUOTE[ETTMTTP-2:23]: Si elle sait maîtriser son agressivité vis-à-vis d'elle-même et de l'environnement dans lequel elle se trouve, elle atteindra l'âge d'or de la civilisation interplanétaire ENDQUOTE
- [R3.6] ETTMTTP-2:23 | Yahweh | "Plus vite vous mettrez en place la géniocratie, plus vite vous supprimerez les risques de cataclysme" | U, C
- [R3.7] ETTMTTP-2:23 | Yahweh | In a cataclysm destroying humanity, "seuls les gens qui vous suivent seront sauvés" and will repopulate the Earth, as in Noah's time | U, C | [analysis] sits beside "nous n'interviendrons pas" in the same paragraph: rescue is an intervention
QUOTE[ETTMTTP-2:23]: En cas de cataclysme détruisant l'humanité, seuls les gens qui vous suivent seront sauvés et devront repeupler la terre dévastée lorsque tout danger sera écarté, comme cela s'est déjà produit à l'époque de Noé. ENDQUOTE
- [R3.8] ETTMTTP-2:26 | Yahweh | France "devrait être le premier pays sans armée"; if it dropped conscription and put its army at Europe's service, neighbours would not invade but "très vite" imitate | U, C (counterfactual prescription)
- [R3.9] ETTMTTP-2:27 | Yahweh | After a military Europe, "une monnaie européenne unique"; then same process worldwide plus a single world language | U, prescriptive sequence, not a prediction | [outside knowledge — unverified, needs source]: a single European currency was later introduced; the text orders it AFTER military union, and as advice
- [R3.10] ETTMTTP-2:29 | Yahweh | "Si vous arrivez prochainement à ce stade de visiteurs évolués" you too will have to pose as gods | U, C
- [R3.11] ETTMTTP-2:37 | Yahweh | "Vous pourriez vivre très vite dans un véritable paradis terrestre si" technology served well-being; the one person supervising a car plant's computer "pourra même être supprimée" "dans l'avenir" | U; C / X (full automation of car manufacture)
- [R3.12] ETTMTTP-2:51 | Yahweh | Raël has his place reserved "Quelle que soit la suite de votre mission"; the Elohim will leave their planet for another when they detect its solar system ageing | U, X
- [R3.13] ETTMTTP-2:82, 2:99, 2:112, 3:217 | Yahweh / Keys | The wicked, critics of the prophets, and those who make others suffer "seront recréés… quand le temps sera venu" to be judged and punished | U, X; timing explicitly unspecified
- [R3.14] ETTMTTP-2:83, 2:129 | Yahweh | Raël will be brought back to finish his mission "avant de revenir définitivement avec nous" | U, X
- [R3.15] ETTMTTP-2:98 | Yahweh | "À partir de maintenant" Elohim see/hear/speak through Raël and "pourrons même guérir par vos mains" selected deserving sick | D (from Oct 1975), X as capacity; healings selective
- [R3.16] ETTMTTP-2:99, 3:230, 3:257 | Yahweh / Keys | Followers/helpers of Raël "y serez accueillis"; "tu auras sans aucun doute droit"; pioneer "aur[a] ta place, quoi qu'il arrive" | U, C on following (3:257 words it unconditionally "quoi qu'il arrive")
- [R3.17] ETTMTTP-2:104 | Yahweh | For the Jews "le temps du pardon est arrivé"; they "pourront maintenant vivre tranquilles dans leur pays retrouvé à moins qu'ils ne commettent une nouvelle faute en ne vous reconnaissant pas" | U, C | commits to: tranquillity for Jews in Israel unless Raël is not recognised as envoy
QUOTE[ETTMTTP-2:104]: ils pourront maintenant vivre tranquilles dans leur pays retrouvé à moins qu'ils ne commettent une nouvelle faute en ne vous reconnaissant pas comme notre envoyé ENDQUOTE
- [R3.18] ETTMTTP-2:104 | Yahweh | Wish: embassy in Israel on land "que le gouvernement vous donnera"; "S'ils refusent, vous pourrez la construire ailleurs et Israël subira un nouveau châtiment" | U, C
- [R3.19] ETTMTTP-2:105 | Yahweh | "vous aurez de quoi faire vivre votre famille"; helpers and troublemakers alike "nous ne les oublierons pas" | U, X
- [R3.20] ETTMTTP-2:121 | Yahweh | Raël is "le dernier des prophètes avant le Jugement", who brings back the flock "avant que l'eau ne soit versée" | U, X | commits to: no later prophet before a Judgment; a Judgment
- [R3.21] ETTMTTP-2:124 | Yahweh | Israel "pourr[a] y vivre en paix si tu écoutes le dernier des prophètes… et que tu l'aides" | U, C
- [R3.22] ETTMTTP-2:125 | Yahweh | "C'est là ta dernière chance, sinon un autre pays accueillera le Guide des guides et édifiera notre ambassade… et ce pays sera proche du tien, et il sera protégé et le bonheur y régnera, et l'Etat d'Israël sera détruit une nouvelle fois" | U, C | commits (on refusal) to: embassy in a country NEAR Israel; that country protected and happy; State of Israel destroyed. No deadline for the refusal.
QUOTE[ETTMTTP-2:125]: C'est là ta dernière chance, sinon un autre pays accueillera le Guide des guides et édifiera notre ambassade sur son territoire, et ce pays sera proche du tien, et il sera protégé et le bonheur y régnera, et l'Etat d'Israël sera détruit une nouvelle fois. ENDQUOTE
- [R3.23] ETTMTTP-2:126 | Yahweh | Diaspora Jews: wait to see whether the government accepts; if refused do not return — "tu seras de ceux qui seront sauvés de la destruction", descendants regain the land "quand les temps seront venus" | U, C
- [R3.24] ETTMTTP-2:127–128 | Yahweh | If the embassy rises elsewhere "tu seras à nouveau dispersé"; "tu n'auras plus droit à la terre" | U, C
- [R3.25] ETTMTTP-2:120 | Yahweh | Successor Guide is designated by the previous one; the Guide "sera le gardien de l'ambassade terrestre" and may live there | U, X (presupposes the embassy)
- [R3.26] ETTMTTP-3:23 | Keys | Men to become "un jour capables de refaire ce que leurs créateurs ont fait : créer ailleurs d'autres humanités, scientifiquement" | U, purpose clause
- [R3.27] ETTMTTP-3:26 | Keys | One who regrets only at death "ne sera pas pardonné" | U, X (unobservable)
- [R3.28] ETTMTTP-3:77, 3:89–90, 3:151, 3:153, 3:157 | Keys | Science will find the "moyen médical" to suppress violence; one day "on saura guérir et surtout prévenir la maladie du crime" and executions will scandalise | U, X | commits to: a medical cure/prevention for criminal violence
- [R3.29] ETTMTTP-3:84 | Keys | "Déjà des savants sont en train de mettre au point des techniques permettant de mesurer l'intelligence à l'état brut" | present-tense (1975) claim with forward implication
- [R3.30] ETTMTTP-3:88, 3:149 | Keys | "même les juges humains seront jugés un jour par nos créateurs" | U, X
- [R3.31] ETTMTTP-3:96, 3:98–99 | Keys | Robots will do all tasks and money will be abolished; men, "s'ils s'organisent, n'en ont pas pour longtemps"; "Si tous les hommes s'y mettaient vraiment, il n'y en aurait que pour quelques années"; "Vous pouvez, en quelques années, faire un monde complètement différent. Vous êtes arrivés à l'âge d'or." | U ("quelques années"), C on universal effort | commits to: feasibility within a few years IF all worked at it — condition unmet, so not auditable
QUOTE[ETTMTTP-3:99]: Si tous les hommes s'y mettaient vraiment, il n'y en aurait que pour quelques années pour que l'homme soit dégagé de l'obligation de travailler. ENDQUOTE
- [R3.32] ETTMTTP-3:140 | Keys | Audio-visual media "peuvent remplacer avantageusement la littérature"; literature is "provisoirement utile" | U
- [R3.33] ETTMTTP-3:172 | Keys | Date writings from 1946 = year 1 "après Raël"; "1976 sera donc l'an 31" | D, calendrical rule (not a prediction)
- [R3.34] ETTMTTP-3:193 | Keys | Meditation script: "la planète des éternels, où tu seras un jour admis pour l'éternité" | U, worded unconditionally (contrast R3.16, R2.37)
- [R3.35] ETTMTTP-3:203–205 | Keys | Children so educated will be "l'homme nouveau, dont les facultés seront infiniment supérieures" | U, C on education
- [R3.36] ETTMTTP-3:220–221 | Keys | False contact-claimants and opponents of the Guide: "leur vie deviendra un enfer" (illness, family, professional, sentimental troubles) "en attendant la punition éternelle" | U, X — and explicitly without visible sign of origin (R2.50)
- [R3.37] ETTMTTP-3:233 | Keys | "D'un jour à l'autre l'homme peut s'autodétruire. Seuls seront sauvés de la destruction ceux qui suivent le dernier des prophètes." | U; possibility + C promise
- [R3.38] ETTMTTP-3:236 | Keys | Man "va peut-être détruire lui-même toute vie sur la Terre"; only those who recognise the Elohim saved | U, hedged ("peut-être")
- [R3.39] ETTMTTP-3:237 | Keys | "lorsque le cataclysme aura lieu, car il y a de fortes chances pour qu'il ait lieu étant donné la façon d'agir des hommes actuellement, et dans pas longtemps" | U but near-term ("dans pas longtemps"), probabilistic ("fortes chances") | commits to: a high likelihood, as of 1975, of a soon cataclysm — the book's strongest prediction; wording alone does not fix a window, so not settled by text
QUOTE[ETTMTTP-3:237]: Et lorsque le cataclysme aura lieu, car il y a de fortes chances pour qu'il ait lieu étant donné la façon d'agir des hommes actuellement, et dans pas longtemps, il y aura deux sortes d'hommes ENDQUOTE
- [R3.40] ETTMTTP-3:238 | Keys | Non-recognisers "subiront… la fournaise finale"; the others "seront préservés et seront amenés avec le Guide des guides sur la planète des éternels" | U, C on cataclysm | commits to: physical evacuation of followers with the Guide
- [R3.41] ETTMTTP-3:240 | Keys | When the Guide summons you, drop everything: "c'est peut-être parce qu'il a reçu une information concernant la fin"; those near him "serez sauvés et amenés avec lui" | U, C; implies the Guide will be forewarned
QUOTE[ETTMTTP-3:240]: quand le Guide des guides vous convoque quelque part, laissez tomber toutes vos préoccupations, c'est peut-être parce qu'il a reçu une information concernant la fin ENDQUOTE
- [R3.42] ETTMTTP-3:242, 3:245, 3:254 | Keys | "L'Église est en train de disparaître"; it "n'a plus aucune raison d'être" | U, X trend claim
- [R3.43] ETTMTTP-3:252–253 | Keys | The pope, unless he has all Vatican goods sold for the poor, "ne sera pas admis parmi les justes"; repentant clergy pardoned | U, C (unobservable)
- [R3.44] ETTMTTP-3:260, 3:263 | Keys | "Viens avec nous préparer la venue de nos créateurs"; build "une ambassade pour accueillir les Elohim" | U; a coming is presupposed, neither dated nor explicitly conditioned in this book
- [R3.45] ETTMTTP-3:69 | Keys | Those who know the message "seront recréés d'après les cellules qu'ils auront laissées dans notre ambassade", only if the bone is sent | U, C (presupposes the embassy exists to hold them)
- [R3.46] ETTMTTP-3:201 | Keys | "Tu verras peut-être un signal si tu es suffisamment prêt" | U, C, hedged
- [R3.47] NULL | — | No calendar-dated prediction anywhere in ETTMTTP (no year, no "before the end of the century"); the only dates are past events, the era rule (3:172) and recurring meeting days (3:266) | null result

## Register 4 — checkable-in-principle statements (nature, history, places, datable life events)

Bearing observation in brackets. Nothing here is asserted as verified.

### 4a Raël's life (ch. 1–2 frame)
- [R4.1] ETTMTTP-1:7 | Raël | Born 30 Sept 1946 c. 02:00 in a clinic at Vichy; father unknown, "paraît-il, un réfugié juif" (hearsay marker); raised at Ambert, "capitale mondiale du chapelet" | [civil registry; the paternal claim is flagged by the text itself as hearsay]
- [R4.2] ETTMTTP-1:7 | Raël | Conceived 25 Dec 1945 | [not observable; 25 Dec → 30 Sept = 279 days, arithmetic only; the date appears to be derived, not recorded — analysis]
- [R4.3] ETTMTTP-1:10 | Raël | Grandmother saw a fast silent craft over Ambert in 1947, told nobody until she read the book | [single late testimony; uncheckable]
- [R4.4] ETTMTTP-1:11–13 | Raël | "le père Dissard" of Ambert, long hair/beard/cape, lived opposite the collège municipal; identified in "un livre… parlant de l'Auvergne mystérieuse" read summer 1974 as the last "pape" of the druids, since deceased; laid a hand on the boy's head at age seven | [existence of the man and of the book; the book's wording; local records] — the druidic identification is second-hand from an unnamed book
- [R4.5] ETTMTTP-1:19–21 | Raël | At nine: boarding at "pensionnat Notre-Dame-de-France, au Puy-en-Velay", run by Catholic brothers; six months of daily communion though unbaptised; first prize in a poetry contest | [school rolls; baptismal absence]
- [R4.6] ETTMTTP-1:23–31 | Raël | Collège municipal d'Ambert; boarding at Cunlhat (~30 km from Ambert), ran away ~10 km; day-pupil with the brothers at Ambert; at 14 a collège at Le Mont-Dore | [school records; road distance Ambert–Cunlhat]
- [R4.7] ETTMTTP-1:33–39 | Raël | At 15 hitch-hiked to Paris with 2,000 old francs; ~3 years of street/cabaret singing; Jean-Pierre Darras arranged free T.N.P. classes ("cours Dullin") for three months; radio contests; driving licence at 18 | [named person and institutions]
- [R4.8] ETTMTTP-1:38 | Raël | Stage name Claude Celler, after Tony Sailer | [record labels, press]
- [R4.9] ETTMTTP-1:40–46 | Raël | Three-year contract with the label directed by Lucien Morisse, director of "Europe N° 1"; second record with "Le miel et la cannelle", "très souvent à la radio"; selected for "la Rose d'or de la chanson française à Antibes" and withdrawn by Morisse a week before | [discography, radio archives, festival lists]
- [R4.10] ETTMTTP-1:49–53 | Raël | A year as sales agent at Bordeaux (15 départements); crash at ~100 km/h into a wall where "plus de dix personnes s'étaient déjà tuées"; >3 months immobilised; age 22 | [hospital/police records; site unspecified]
- [R4.11] ETTMTTP-1:55–58 | Raël | Answered an ad in "L'Équipe"; two unpaid months at Dijon for a man just out of prison who had swindled 150–300 F from "plus de cinq cents jeunes gens" | [court/press records, Dijon; year not given in the text]
- [R4.12] ETTMTTP-1:57 | Raël | Met Marie-Paule (a nurse, 1:69) in June, married three months later; she was expecting a daughter | [civil registry]
- [R4.13] ETTMTTP-1:59–61 | Raël | Founded a publishing house and motor-sport magazine at Clermont-Ferrand, "très vite un des premiers dans sa spécialité"; tested cars at the circuit of Mas-du-Clos (Creuse); "nombreuses victoires"; three years | [dépôt légal, race results]
- [R4.14] ETTMTTP-1:62–63 | Raël | 13 Dec 1973, crater of the Puy-de-Lassolas (previously misnamed Puy-de-la-Vache); six consecutive days, ~1 h each | [place exists/adjacent volcano — outside knowledge, unverified; the encounters themselves are report only]
- [R4.15] ETTMTTP-1:64–68 | Raël | MS sent to the house run by Marcel Jullian; appearance on Jacques Chancel's "Le Grand Échiquier"; "milliers de lettres"; "Le célèbre couturier Courrèges" retrieved the MS | [TV archives; named third parties could confirm or deny]
- [R4.16] ETTMTTP-1:70 | Raël | Book off the press "à l'automne 1974" | [dépôt légal date]
- [R4.17] ETTMTTP-1:72–75 | Raël | Philippe Bouvard's "Samedi-Soir" "au mois de juin" (assistant dressed as a Martian), then a second broadcast; Salle Pleyel: 150-seat room booked, "plus de trois mille personnes" came; second lecture in the 2,000-seat hall, "plus de deux mille"; three-line notice in France-Soir | [TV archives; Pleyel bookings; press] — chronology problem: "juin" precedes "automne 1974" publication yet the lectures run "depuis le mois de septembre" (1:76) [analysis]
- [R4.18] ETTMTTP-1:3, 1:5, 1:76 | Raël | 700 members; ~40 lectures since September; regional offices in all big French cities | [association records]
- [R4.19] ETTMTTP-1:76–77 | Raël | Le Point published a "diffamatoire" article and did not rectify properly; La Montagne refused even a paid ad | [press archives; registered letters]
- [R4.20] ETTMTTP-2:1–4 | Raël | June 1975: resigned MADECH presidency; loi-1901 association; successor "Christian", a physicist; "François" lent a farm in Périgord | [association filings]
- [R4.21] ETTMTTP-2:5 | Raël | 31 July 1975, evening, Périgord: huge silent craft, jerky motion, ~500 m, three witnesses (Raël, Marie-Paule, François) | [independent statements of the two named co-witnesses]
- [R4.22] ETTMTTP-2:6 | Raël | Arm mark: red circle ~3 cm diameter, 5 mm thick, three inner circles; after ~15 days two concentric circles; after ~15 more a white spot "que j'ai toujours" | [dermatological examination/photographs of the persisting spot; the scientists are unnamed]
- [R4.23] ETTMTTP-2:7 | Raël | Meeting 6 Aug 1975 in the crater; = 30th anniversary of Hiroshima and feast of the Transfiguration | [calendar; both coincidences are true of 6 August — outside knowledge, unverified, needs source]
- [R4.24] ETTMTTP-2:9 | Raël | 7 Oct 1975, left ~23:00, reached "le Roc Plat" (between two streams, forested) "vers minuit"; cloudless sky, shooting stars | [weather records for the Périgord that night; site identification]
- [R4.25] ETTMTTP-2:131 | Raël | After a meal, a night, a morning and "plusieurs heures" more on the planet, he is set down at Roc-Plat and "je regardai ma montre : il était minuit" | [internal: arrival "vers minuit" and return at "minuit" — either zero elapsed Earth time or exactly 24 h; the text does not say which, and names no one who noted his absence — analysis]
QUOTE[ETTMTTP-2:131]: je regardai ma montre : il était minuit ENDQUOTE

### 4b Physical / cosmological / biological statements (Yahweh, ch. 2; Keys, ch. 3)
- [R4.26] ETTMTTP-2:43 | Yahweh | Base "relativement près de la terre"; 25,000 years ago they travelled at 7× light speed and the trip took "près de deux mois"; now "quelques instants" | [arithmetic: 7 c × ~2 months ≈ 1.2 light-years — analysis; nearest known star is farther than that — outside knowledge, unverified, needs source]. Also asserts superluminal travel.
QUOTE[ETTMTTP-2:43]: Il ne nous faut que quelques instants pour effectuer le trajet que nous mettions près de deux mois à parcourir à cette époque, et nous continuons de progresser. ENDQUOTE
- [R4.27] ETTMTTP-2:12, 2:44 | Raël | Transit Earth→base: a few seconds of intense cold; base→planet: ~10 minutes of cold | [report only]
- [R4.28] ETTMTTP-2:43 | Yahweh | Elohim landed on Earth 25,000 years ago | [palaeontological/genetic record of life and humans far older — outside knowledge, unverified, needs source]
- [R4.29] ETTMTTP-2:25 | Yahweh | Universal rule: any species able to leave its planetary system is peaceful; others self-destruct | [would be refuted by one hostile interstellar species; untestable at present]
- [R4.30] ETTMTTP-2:30 | Yahweh | "On a pu constater qu'un être perd quelques grammes au moment de sa mort"; this is the departing energy, since "l'énergie est, comme la matière, pesante" | [precision weighing of the dying; a few grams of mass-equivalent energy would be enormous — outside physics, unverified, needs source]
QUOTE[ETTMTTP-2:30]: On a pu constater qu'un être perd quelques grammes au moment de sa mort ; en fait il ne s'agit que de l'énergie dont dispose tout être vivant, qui s'élimine à ce moment-là. ENDQUOTE
- [R4.31] ETTMTTP-2:30, 2:80 | Yahweh | A single cell "contient le plan physique et intellectuel" of the being; from a cell a "réplique totale… avec ses souvenirs, sa personnalité, son caractère"; from a photo only the physique | [whether acquired memories are recoverable from a somatic cell: testable in principle by cloning — outside knowledge on cloning outcomes unverified]
QUOTE[ETTMTTP-2:80]: nous pouvons réaliser une réplique totale de l'individu à qui nous avons prélevé cette cellule, avec ses souvenirs, sa personnalité, son caractère, etc. ENDQUOTE
- [R4.32] ETTMTTP-2:30–32, 3:194–195 | Yahweh / Keys | Intelligent organised life exists within the infinitely small; stars and planets are atoms of a gigantic being; time runs inversely to mass/"niveau de la forme de vie" (a millennium here = one step of the giant); Earth and all planets are alive | [sub-atomic structure; no known observation — largely unfalsifiable as stated; "inversement proportionnel à la masse" is a quantitative-sounding law with no units]
QUOTE[ETTMTTP-2:32]: Le temps est en effet inversement proportionnel à la masse ou plutôt au niveau de la forme de vie. ENDQUOTE
- [R4.33] ETTMTTP-2:33 vs 3:194 | Yahweh / Keys | 2:33: "l'univers étant infini, il ne peut avoir de centre"; 3:194: galaxies "tournent elles-mêmes autour du centre de l'univers", and "notre univers" is itself a particle | [internal inconsistency on a centre, unless "notre univers" (bounded) ≠ "l'univers" (infinite) — analysis; observation: large-scale galaxy kinematics]
QUOTE[ETTMTTP-3:194]: par rapport à ces galaxies qui tournent elles-mêmes autour du centre de l'univers ENDQUOTE
- [R4.34] ETTMTTP-2:34 | Yahweh | Matter has neither beginning nor end ("rien ne se perd, rien ne se crée, tout se transforme") | [cosmological evidence on the universe's past]
- [R4.35] ETTMTTP-2:35, 2:24 | Yahweh | The swastika-in-hexagram emblem is found in ancient writings "comme le Bardo Thödol"; swastika means the cycle | [inspect manuscripts/editions of the Bardo Thödol]
- [R4.36] ETTMTTP-2:37 | Yahweh | In "vos usines les plus modernes" (1975) one person watching a computer suffices to build a car where hundreds were needed | [industrial history; checkable and specific]
- [R4.37] ETTMTTP-2:28–29 | Yahweh | Only ~30 years since the most advanced countries ceased to be quite primitive; the more primitive a people, the more deist religion flourishes | [sociology of religion vs development]
- [R4.38] ETTMTTP-2:50, 2:53–54 | Yahweh | 8,400 Earth people + 700 Elohim on the planet of the eternals; ~10 robots each ⇒ ~90,000; lifespan ~700 years after "une petite intervention chirurgicale" | [uncheckable; internally consistent: 9,100 × 10 ≈ 90,000]
- [R4.39] ETTMTTP-2:58 | Yahweh | The planet has no winter; all live in an equator-like zone; weather controlled, rain at night | [uncheckable]
- [R4.40] ETTMTTP-2:62, 2:64 | Yahweh | Jesus recreated from a cell kept before the crucifixion; Moses, Elijah, Buddha, Muhammad present; Muhammad wrote "Allah" because "il n'osait pas me nommer par respect" | [the last is a claim about the origin of a word, bearing on Arabic philology — outside knowledge, unverified]
- [R4.41] ETTMTTP-2:72 | Yahweh | Quotes "Ezéchiel, XXVII, 3, 7-8, 10" (dry bones) | [collate: the dry-bones vision is usually numbered chapter 37 — outside knowledge, unverified, needs source; wording to collate with Dhorme]
- [R4.42] ETTMTTP-2:106–111, 3:232, 3:239 | Yahweh / Keys | Qur'an 21:1–5; Matthew 27:42–43; Qur'an 54:1; Qur'an 56:15–23, in French | [collation with a named French Qur'an/Bible translation; "créateur" for the usual "Seigneur" at 21:1–2 looks like an adapted wording — analysis, needs collation]
- [R4.43] ETTMTTP-2:98 | Yahweh | The Elohim already heal "à Lourdes et dans bien d'autres endroits" | [Lourdes medical-bureau records bear on whether cures occur, not on agency]
- [R4.44] ETTMTTP-2:104, 2:123 | Yahweh | "les Juifs sont nos descendants directs": descendants of the unions of sons of Elohim and daughters of men | [population genetics: a non-terrestrial paternal contribution confined to one lineage would in principle be detectable]
QUOTE[ETTMTTP-2:104]: les Juifs sont nos descendants directs sur la Terre ENDQUOTE
- [R4.45] ETTMTTP-2:128 | Yahweh | Had Israel recognised Jesus, all Christians would be Jews; Rome was given the role instead | [counterfactual; not checkable]
- [R4.46] ETTMTTP-3:47 | Keys | The parents' conscious state at conception shapes the first cell, "le plan de l'individu" | [developmental genetics]
- [R4.47] ETTMTTP-3:51 | Keys | Abortion by competent persons leaves no physical "et surtout morales" sequelae | [clinical outcome studies]
- [R4.48] ETTMTTP-3:69 | Keys | The bone to keep: frontal bone "à 33 mm au-dessus du milieu de l'axe reliant tes deux pupilles", ≥1 cm² | [a precise anatomical specification; its claimed function is not checkable]
- [R4.49] ETTMTTP-3:91 | Keys | French conscientious objectors do not go to prison but serve unarmed/civil service of double duration | [French law in force in 1975]
- [R4.50] ETTMTTP-3:105–106 | Keys | Plants "souffrent de la même façon que toi" | [plant physiology]
- [R4.51] ETTMTTP-3:173, 3:185, 3:202 | Keys | Telepathy is a real sixth sense with an "organe télépathique"; uncut hair and beard improve it; humans can awaken organs for unseen waves as pigeons find north | [controlled telepathy trials incl. hair-length comparison; anatomy]
QUOTE[ETTMTTP-3:185]: Si tu veux obtenir des communications télépathiques de grande qualité, ne coupe pas tes cheveux ni ta barbe. ENDQUOTE
- [R4.52] ETTMTTP-3:182–183 | Keys | "L'Occident ne connaît pas les problèmes du tiers monde"; "Tous les peuples de la Terre ont eu les mêmes chances au départ" | [economic history]
- [R4.53] ETTMTTP-3:228 | Keys | Buddhist writings "indiquent que le nouveau Bouddha doit naître en Occident" | [Buddhist textual sources; none is named]
- [R4.54] ETTMTTP-3:231 | Keys | Energies sufficient to reach the Moon suffice to destroy all life on Earth | [arsenal yields vs biosphere; loosely true/false depending on "toute vie"]
- [R4.55] ETTMTTP-3:245 | Keys | "Il y a cinquante ans, il y avait cinquante mille séminaristes, maintenant il n'y en a plus que cinq cents" (country unspecified) | [Church statistics c. 1925 and 1975]
QUOTE[ETTMTTP-3:245]: Il y a cinquante ans, il y avait cinquante mille séminaristes, maintenant il n'y en a plus que cinq cents ENDQUOTE
- [R4.56] ETTMTTP-3:256 | Keys | UFOs "apparaissent chaque jour" | [sighting-report statistics; reports ≠ objects]
- [R4.57] ETTMTTP-3:84 | Keys | Scientists (1975) are developing techniques to measure "l'intelligence à l'état brut" | [psychometrics history]
- [R4.58] ETTMTTP-3:265–266 | Raël | Address "Religion Raëlienne, Siège International, C.P. 225, 1211 Genève 8"; four annual gatherings (first Sunday of April, 6 Aug, 7 Oct, 13 Dec) | [edition marker: a Geneva "Religion Raëlienne" address in a book narrated from 1975 Périgord — needs collation with the 1975 printing]
- [R4.59] ETTMTTP-2:16, 2:14, 2:67–68 | Raël | Base rooms: ~15 m diameter × ~10 m high; hall ~100 m across under a transparent dome with black starry sky; belts carrying at ~20 m altitude, ~100 km/h, no wind felt | [report only; "no wind felt" is a physical oddity noted by the narrator himself]

## Register 5 — declared unknowns, hedges, refusals

- [R5.1] ETTMTTP-1:7 | Raël | Father "inconnu (pas si inconnu que ça…)", Jewish refugee "paraît-il" | hearsay flagged
- [R5.2] ETTMTTP-1:13 | Raël | "Je n'avais jamais pu expliquer cette habitude subite" (counting to nine) | unexplained, then read as code
- [R5.3] ETTMTTP-1:48 | Raël | Morisse "ne pouvait m'en dire plus sur le moment"; "je comprendrais pourquoi plus tard" — no explanation is ever given in the text | third-party refusal; reason left open
- [R5.4] ETTMTTP-1:68 | Raël | "Je me demande toujours s'il était réellement égaré ou si on cherchait à en empêcher la publication" | declared uncertainty
QUOTE[ETTMTTP-1:68]: Je me demande toujours s'il était réellement égaré ou si on cherchait à en empêcher la publication. ENDQUOTE
- [R5.5] ETTMTTP-2:6 | Raël | Did not at first connect the mark with the sighting; its cause is others' opinion and a hypothesis | cause not asserted on his own authority
- [R5.6] ETTMTTP-2:12, 2:47 | Raël | Words "dans un langage incompréhensible"; the eternals' speech not understood | not understood
- [R5.7] ETTMTTP-2:23 | Yahweh | Humanity's future "ne dépend plus que d'elle-même" | [analysis] the outcome is disclaimed, not foretold
- [R5.8] ETTMTTP-2:30–31, 3:194–195 | Yahweh / Keys | The being of which stars are atoms "contemple certainement d'autres étoiles"; "Il est aussi fort possible que…"; "située, peut-être, dans le bras d'un être"; cells "peut-être, ne sont pas conscientes" | hedged speculation about adjacent levels
- [R5.9] ETTMTTP-2:33 | Yahweh | No communication is possible between levels (mass/time gap) | in-principle limit on knowledge of other levels — yet life below was "proved" (R2.16)
- [R5.10] ETTMTTP-2:34 | Yahweh | What was "au commencement": refused as a "question stupide" — there is no beginning | question dissolved rather than answered
- [R5.11] ETTMTTP-2:36 | Yahweh | "très difficile à un cerveau humain 'fini' de prendre conscience de l'infini" | cognitive limit
- [R5.12] ETTMTTP-2:43 | Yahweh | Location given only as "une base située relativement près de la terre"; the planet's position is never given | location withheld
- [R5.13] ETTMTTP-2:51 | Yahweh | "nous commençons à comprendre parfaitement la vie de l'infiniment grand" | Elohim knowledge incomplete, progressing
- [R5.14] ETTMTTP-2:59 | Yahweh | "bien d'autres choses que vous ne pourrez comprendre en une fois" | withheld for comprehension
- [R5.15] ETTMTTP-2:82, 2:99, 2:126 | Yahweh | Judgment/recreation of the wicked "lorsque le temps sera venu" / "quand les temps seront venus" | timing not stated
- [R5.16] ETTMTTP-2:104 | Yahweh | Only one revelation is released "dès maintenant" | implies others not yet released
- [R5.17] ETTMTTP-2:132 | Raël | "Les Elohim commençaient à…" — the sentence is not completed in the dump | lacuna/ellipsis at the hinge between report and Keys
- [R5.18] ETTMTTP-3:77 | Keys | Whether suicide is good is left for when science can abolish suffering | question deferred
- [R5.19] ETTMTTP-3:68, 3:73 | Keys | The dead "accède peut-être au paradis"; "S'il a été bon…" | individual outcomes unknown to survivors
- [R5.20] ETTMTTP-3:161, 3:163 | Keys | Esperanto and federalism recommended only "si personne ne propose mieux" / "n'a mieux à proposer" | non-final, defeasible recommendations
- [R5.21] ETTMTTP-3:173 | Keys | "Les possibilités du cerveau humain sont loin d'être toutes connues" | open unknown
- [R5.22] ETTMTTP-3:219 | Keys | The Elohim created men "sans savoir qu'ils faisaient ce qui avait déjà été fait pour eu[x]", thinking it an experiment "sans grand intérêt", and for that destroyed almost all humanity once | past ignorance and error of the Elohim admitted
QUOTE[ETTMTTP-3:219]: ils croyaient ne faire qu'une expérience scientifique sans grand intérêt, et c'est pour cela qu'ils détruisirent une première fois presque toute l'humanité ENDQUOTE
- [R5.23] ETTMTTP-3:236–237, 3:240 | Keys | Cataclysm: "va peut-être", "fortes chances", "c'est peut-être parce qu'il a reçu une information" | probability, not certainty
- [R5.24] ETTMTTP-3:201 | Keys | Believer may be asked things without understanding why | reasons may be withheld from the believer
- [R5.25] ETTMTTP-3:266 | Raël | Gathering place "te sera indiqué" on writing | practical withholding
- [R5.26] NULL | — | Nowhere does Yahweh say "I cannot/will not tell you X" in so many words in this book; refusals are indirect (R5.10, R5.12, R5.14, R5.16) | null result

## Patterns, tensions, counter-examples, null results (terse)

1. Three transmission modes are declared in one book: dictation with hasty notes (book 1, 1:63–64), machine-assisted memory with no notes (2:22, 2:131), and "not-the-author" writing (2:132 → ch. 3). The text itself grades the first as fallible ("beaucoup trop vite", "mal retranscrit", wrong place-name).
2. Book 2 revises book 1 three times: an erratum blamed on the scribe (2:23), a figure made obsolete (2:43), a "residence" re-scaled to a planet (2:50) — plus the admission that the 1973 visual appearance was staged (2:11).
3. Ch. 3's voice is Raël's "we humans" under claimed inspiration, with Elohim "nous" intruding (3:241); the dump's blanket `[Yahweh]` tag hides this. 2:98 ("nous parlerons par votre bouche") is the warrant that makes the distinction doctrinally moot but textually real.
4. Invitation to verify exists and is specific (3:256–257: scriptures + current biology + the sky → "fais la synthèse"; 2:122 "relisez vos écrits"), and science is ranked first (3:165–166).
5. Discouragement of verification also exists and is specific: believers must not judge Elohim or prophet (3:241); smilers = crucifiers (3:222); sceptics are "imbéciles" (2:7, 2:105); a miracle-demand is mockery (2:109–111); obey without understanding (3:201); gap rule (3:177).
6. "Proof" (preuve/prouver) is used for: private demonstrations to Raël (2:80), asserted Elohim results (2:30), adherents' happiness (3:3), Raël's reliability to the Elohim (2:11) — never for evidence the reader can inspect.
7. Belief vocabulary is pervasive and positive for adherents ("croient aux Elohim/aux messages", ~12 occurrences in ch. 3) alongside "tu n'as plus le droit de continuer à croire" in God (3:225) and "La science doit être ta religion" (3:166); 2:105 calls it "une religion athée". Counter-example to belief-salvation: 3:25–26 (acts, not late belief).
8. Sightings cut both ways inside the book: signs for Raël (2:5, 3:256) but also admitted staged "apparitions" for amusement (2:29) — the canon here undermines UFO reports as honest evidence.
9. Sanctions are built to be unobservable (3:221 "sans que rien ne paraisse…"; computers 2:98; judgment "quand le temps sera venu").
10. Non-intervention (2:23, 3:15, 3:219) vs rescue of followers (2:23, 3:238–240), protection of the embassy country and punishment of Israel (2:125), action on individuals (3:220): reconciled only by the "humanity as a whole / individuals" distinction at 3:220.
11. Forward statements: zero calendar dates; all major ones conditional (Israel/embassy; aggression fork) or probabilistic ("fortes chances… dans pas longtemps", 3:237). Unconditional ones are either unobservable (judgment) or trends (Church disappearing).
12. Embassy: in this book it is a demand on Israel and a relic/residence site; "another country near yours" (2:125) is a concrete geographic commitment on refusal. No statement that arrival waits on it (null).
13. Most checkable material is ch. 1 biography (named people, broadcasts, venues) and a handful of numbers (2:30 grams, 2:43 speed/time, 3:245 seminarians, 2:37 car plant, 2:72 citation).
14. Edition signals needing collation with the 1975 printing: "Mouvement Raëlien"/"religion" in Yahweh's 1975 speech (2:105), "première partie de ce livre" (3:84), Geneva address (3:265), "MADECH1"/"svastika1" footnote digits.
15. Internal oddities: universe-centre (2:33 vs 3:194); midnight→midnight (2:9/2:131); June TV before autumn-1974 publication vs lectures "depuis septembre" (1:70–76).

---

# LWTE (Accueillir les extra-terrestres, 1979) — epistemics register

Read: all of `texts/LWTE.fr.txt` (chapters 1–4, every paragraph; 4:220–312 is an address list). French is the source; quotes verbatim.
Format: `- [R<register>.<n>] REF | voice | what the text says | tags`. Layer (a) only, except the closing section.

Voices (the dump tags everything `[Narrator]`):
- **Editor** — framing notes (1:1, 2:1–2) and the footnotes about the 1998/1999/2000 combined editions (1:21, 1:201, 2:60, 2:83, 3:26).
- **Questioner** — journalists' questions in ch.1.
- **Raël** — ch.1 answers; ch.2:3–93 (exposition + first-person narrative); ch.3.
- **"Satan" (reported by Raël)** — 2:59–67, 2:71, 2:73, 2:77. **Yahweh (reported by Raël)** — 2:76, 2:85–88.
- **Yahweh (first-person message "par la bouche de mon prophète Raël")** — 2:95–235.
- **Terrusse** (chemical engineer, guide) 4:1–79, 4:95–147 · **Le Gendre** (ex-priest) 4:80–94 · **Giroux** (ex-priest) 4:148–176 · **Beluet** 4:177–193 · **Ndjoga-Awirondjogo** 4:194–203 · **Deydier** (psychologist) 4:204–219.

---

## Register 1 — Self-description, transmission, accuracy, limits

- [R1.1] LWTE-1:1 | Editor | Ch.1 is a compilation of journalists' most frequent radio/TV questions and "des réponses qu'il a pu donner" | genre: oral Q&A, compiled; not dictation
- [R1.2] LWTE-1:2–4 | Questioner | Lists "contradictions" between message 1 and 2: told he could not go to the planet / then taken there; craft appeared gradually with flashing lights / then instantaneously; halo-scaphandre / then none; Ex 33:20 gloss ("il mourrait car l'atmosphère ne lui convient pas") | internal-consistency challenge raised inside the canon
- [R1.3] LWTE-1:5–7 | Raël | The contradictions reduce to one word, psychology: lights, gradual approach and suit were chosen to resemble known aircraft/cosmonauts so as not to frighten him | staging; appearance adapted to witness
QUOTE[LWTE-1:5]: L'explication de ces apparentes contradictions est très simple et peut se résumer en un mot: psychologie. ENDQUOTE
QUOTE[LWTE-1:7]: ne pas affoler le contacté tout en lui laissant voir des techniques que les terriens sont incapables d'utiliser afin qu'il comprenne tout de même que ce qu'il découvre est extraterrestre. ENDQUOTE
- [R1.4] LWTE-1:8 | Raël | Second time the Elohim used their technology "sans camouflage" before a prepared witness | implies first encounter was camouflaged
QUOTE[LWTE-1:8]: les Elohim utilisant sans camouflage leur technologie, devant un témoin qu'ils savaient suffisamment préparé psychiquement ENDQUOTE
- [R1.5] LWTE-1:11 | Raël | Elohim decided to test him before giving the whole message; disclosure was progressive | staged disclosure, stated by the reporter
QUOTE[LWTE-1:11]: les Elohim avaient décidé de me mettre à l'épreuve avant de me donner la totalité du message, ils y sont donc allés très progressivement. ENDQUOTE
- [R1.6] LWTE-1:12 | Raël | The first-message statement that he could not travel to their planet was said "to cut short" further requests, as one tells a child alcohol stops growth; the Exodus verse they added was addressed to primitives | **a statement in message 1 is retroactively classified as a deliberate put-off, not a fact**
QUOTE[LWTE-1:12]: ils m'ont répondu pour couper court à toute nouvelle demande que cela m'était impossible, comme l'on dit à un enfant que s'il boit de l'alcool il ne grandira plus. ENDQUOTE
- [R1.7] LWTE-1:10 | Raël | The Bible was dictated by the Elohim to the first men "justement dans le but d'être reconnus maintenant" | scripture as planned recognition device
- [R1.8] LWTE-1:17–18 | Questioner / Raël | Israel "elected in a contest" (msg 1 p.34) vs Jews "direct descendants" (msg 2 p.84): Raël harmonises with a conjecture marked "C'est peut-être justement parce que…" | harmonisation by reporter's own conjecture
- [R1.9] LWTE-1:27 | Raël | The "a little less than one light-year" figure (msg 1 p.114): Elohim do not want their location known; exact data only at the embassy; meanwhile only questions; movement scientists' curved-light hypothesis "est possible"; "J'y ajouterai…" | figure effectively withdrawn as precise; reporter adds own physics
QUOTE[LWTE-1:27]: Tout cela sera révélé exactement lorsqu'ils viendront officiellement dans l'ambassade que nous devons édifier pour les accueillir. En attendant, l'on ne peut que se poser des questions. ENDQUOTE
- [R1.10] LWTE-1:40 | Raël | "Only those who follow you will be saved" applies only to those who have read the messages | restrictive re-reading of an earlier passage
- [R1.11] LWTE-1:57 | Raël | He reported what he saw in words present-day people can understand, pitching it psychologically to the majority; Elohim capacities are in fact "inimaginable" | **report adapted/simplified by the reporter**
QUOTE[LWTE-1:57]: J'ai utilisé pour rapporter ce que j'avais vu des mots que les hommes actuels peuvent comprendre, en me mettant psychologiquement à la portée du plus grand nombre ENDQUOTE
- [R1.12] LWTE-1:58 | Raël | Restates: lights and scaphandre were used "afin de ne pas trop me désorienter au début" | staging
- [R1.13] LWTE-1:72 | Raël | The "keys" in message 2 describe the techniques "sommairement" | declared summary level
- [R1.14] LWTE-1:84 | Raël | *La géniocratie* was written by him as a manifesto at Raëlians' request, developing a chapter of message 1 | authored, not dictated
- [R1.15] LWTE-1:105 | Raël | "Comme le disent les messages": everything judged on four levels | self-citation as authority
- [R1.16] LWTE-1:2, 1:4, 1:17, 1:20, 1:26, 1:30, 1:197, 2:79, 2:80, 3:26 | Questioner / Raël | Page citations to the first editions (msg 1 pp. 21, 22, 28, 34, 51, 111, 114; msg 2 pp. 84, 87, 90, 113) | checkable against first printings
- [R1.17] LWTE-1:21, 1:201, 2:60, 2:83, 3:26 | Editor | Footnotes: since 1998 the first two books are combined (1998, 1999, 2000 titles), with new page numbers (234, 263, 240, 237) | **post-1998 editorial layer inside the 1979 text**; 2:60 and 2:83 footnotes interrupt running sentences
- [R1.18] LWTE-2:1–2 | Editor | Ch.2 contains revelations Raël "n'avait pas le droit d'annoncer" until three years after the second-message voyage; now year 34 (1979) | embargo; no reason given
QUOTE[LWTE-2:1]: des révélations que Raël n'avait pas le droit d'annoncer avant que trois années se soient écoulées après le voyage au cours duquel le deuxième message lui fut remis. ENDQUOTE
- [R1.19] LWTE-2:6, 2:17, 2:18 | Raël | New back-story (opposition led by Satan; escaped monsters; ban; first planet destroyed; two failures; life on two other planets) introduced with "L'on sait que" | **no source or occasion of disclosure stated for this material**
- [R1.20] LWTE-2:18 | Raël | Refers to message 1 for the creators' decision to ignore the ban; government ordered them to pose as supernatural | canon cross-reference
- [R1.21] LWTE-2:58–78 | Raël | Previously unreported episode in the relay vessel (1975): another Eloha offers wealth, books he would dictate, eternal life; revealed afterwards as Satan's test; then departure for the planet "comme cela est relaté dans le livre contenant le deuxième message" | retroactive insertion into the 1975 narrative
- [R1.22] LWTE-2:61 | "Satan" (rep.) | Raël's role would be to publish "les livres que je vous dicterais" | dictation named as the mode for books
- [R1.23] LWTE-2:79–80 | Raël | "Nous vous suivions depuis votre naissance et même avant" (msg 1 p.21) puzzled him for two years; answered only on the planet, at the end of the address on p.90 of msg 2 | later book frames earlier one
- [R1.24] LWTE-2:85–88 | Yahweh (rep.) | Raël's mother was taken aboard, inseminated, memory erased; legal father (Jewish, chosen so the child would not be strongly conditioned by one religion) believed himself the father; Yahweh is his and Jesus's father; shift from *vous* to *tu* | new self-description of the messenger
QUOTE[LWTE-2:85]: elle fut inséminée tout comme nous l'avions fait pour la mère de Jésus. Puis elle fut libérée après que nous eûmes totalement effacé de sa mémoire toute trace de ce qui venait de se passer. ENDQUOTE
- [R1.25] LWTE-2:90 | Raël | Asked not to reveal the kinship for three years; hence no earlier allusion | withheld on instruction
QUOTE[LWTE-2:90]: Ensuite il me demanda de ne pas révéler ce lien de parenté aux hommes avant que trois années soient écoulées. C'est pourquoi je n'y fis pas allusion jusqu'alors. ENDQUOTE
- [R1.26] LWTE-2:91–93 | Raël | The kinship "n'a que très peu d'importance"; message matters, not messenger | deflection from messenger
QUOTE[LWTE-2:93]: Ne regardez pas mon doigt, mais la direction qu'il indique! ENDQUOTE
- [R1.27] LWTE-2:95, 2:232 | Yahweh | The 1979 message is spoken "par la bouche de mon prophète Raël" | **mode, date and place of reception not stated anywhere**
QUOTE[LWTE-2:95]: Moi Yahvé, par la bouche de mon prophète Raël, je m'adresse aux hommes de la Terre. ENDQUOTE
- [R1.28] LWTE-2:104 | Yahweh | "Nous avons dicté à nos messagers anciens ces textes" to be recognised when men could understand | ancient scripture = dictation
- [R1.29] LWTE-2:105–106 | Yahweh | Revelation was dictated to John and shown on a viewing device; the text was "très surchargé et assez déformé" by copyists | dictated text declared corrupted in transmission
QUOTE[LWTE-2:106]: Le texte de l'Apocalypse de Jean a lui aussi été malheureusement très surchargé et assez déformé par des copistes qui ne pouvaient être que déistes, étant primitifs. ENDQUOTE
- [R1.30] LWTE-2:118 | Yahweh | The two-edged sword is treated as a copyists' addition to make the apparition menacing | selective excision of an inconvenient detail
- [R1.31] LWTE-2:129 | Yahweh | John was shown "ce qui allait arriver normalement" and "ce qui risquait de lui arriver" | two modalities: normal course vs risk
- [R1.32] LWTE-2:198 | Yahweh | The strange description results from a primitive writing down detailed explanations, then ten others recopying it in his absence | model of transmission loss
QUOTE[LWTE-2:198]: surtout si vous demandez à une dizaine de ses congénères de recopier ce qu'il a écrit hors de sa présence. ENDQUOTE
- [R1.33] LWTE-2:199–200 | Yahweh | John was told plainly there is no god but asked not to write it ("Scelle…") | withheld by instruction; men need a "béquille"
QUOTE[LWTE-2:200]: nous lui avons demandé de ne pas écrire ce qui lui était expliqué ENDQUOTE
- [R1.34] LWTE-2:210 | Yahweh | 666: no need to interpret, only to read what was written | literalism claim
QUOTE[LWTE-2:210]: Il n'y avait encore une fois pas besoin d'interpréter pour comprendre. Il suffisait de lire ce qui était écrit. ENDQUOTE
- [R1.35] LWTE-2:230 | Yahweh | John, Moses, Jesus, all prophets were primitives relative to the Elohim before initiation; so are today's most advanced scientists | limits of every recipient
- [R1.36] LWTE-3:1–24 | Raël | A "mystical" sentence is re-translated word by word through etymology into a "rationally comprehensible" one; both "meant exactly the same" | method: etymology as demystification
- [R1.37] LWTE-3:5 | Raël | Etymology = "science du vrai"; people gathered around *Le Livre qui dit la vérité* are "avant tout des étymologistes" | self-description of method
- [R1.38] LWTE-3:6 | Raël | Elohim "signifiait «ceux qui sont venus du ciel» en hébreu" and Apocalypse = révélation: "tout cela nous le savons maintenant parfaitement" | canonical gloss asserted as known
- [R1.39] LWTE-3:25–28 | Raël | The movement is a religion ("ce qui relie"), atheist, with a cult (Sunday 11 a.m. telepathic contact, daily thought, annual 6 August gathering) | self-classification
- [R1.40] LWTE-3:27 | Raël | The Raëlian "croit dans le sens profond des Ecritures" (Genesis especially, Qur'an, others) as stripped of mysticism by the messages; human laws grafted on are ignored | canon as hermeneutic filter over scripture
- [R1.41] LWTE-3:59 | Raël | If Raël, or even an Eloha, asked a Raëlian to kill, he must refuse: that Eloha "serait Satan" | **limit placed on the authority of the source itself**
QUOTE[LWTE-3:59]: si un Eloha lui-même vous demandait de tuer un homme vous ne devriez pas le faire, car il serait Satan ENDQUOTE
- [R1.42] LWTE-3:82 | Raël | The messages are contained in "les deux livres"; this third book presupposes them | LWTE positions itself as supplement
- [R1.43] LWTE-4:83, 4:181, 4:191, 4:212 | Le Gendre / Beluet / Deydier | Messages "transmis"/"confié"/"donnés" to Claude Vorilhon «Raël» by the Elohim, Dec 1973 and 1975 | followers' description of transmission
- [R1.44] LWTE-4:88 | Le Gendre | The title of message 1 is "annoncé" in Ezek 2:9–10, Rev 5:1, Dan 10:21, 12:4 | scriptural self-validation
- [R1.45] LWTE-4:99–100 | Terrusse | For a technically trained reader some passages "ne paraissent pas très «orthodoxes »"; sifted critically (Montaigne) the messages are "un monument extrêmement solide" | admitted non-conformity with science teaching
QUOTE[LWTE-4:99]: certains passages des messages ne paraissent pas très «orthodoxes », peu conformes à l'enseignement traditionnel. ENDQUOTE
- [R1.46] LWTE-4:111 | Terrusse | Apparent contradiction between facts cited in the messages and accepted knowledge; resolved by declaring accepted science fragile | conflict acknowledged, resolved against science
QUOTE[LWTE-4:111]: ce que nous considérons comme des acquis scientifiques reposent sur des hypothèses fragiles et contestables ENDQUOTE
- [R1.47] LWTE-4:142 | Terrusse | Do not give the messenger more importance than the message | echoes 2:91–93
- [R1.48] LWTE-4:173 | Giroux | The messages "annoncent la religion des religions, la religion de l'infini" | self-description by follower
- [R1.49] LWTE-4:220–312 | Editor | Address list with e-mail addresses | later (post-1990s) layer; not 1979 text

## Register 2 — Proof, belief, doubt, science vs religion, refused proofs, conditions, asks

- [R2.1] LWTE-1:10 | Raël | Until our era creators appeared so as to impress; their main concern was that men believe in them even without understanding; now they appear "en cherchant à être compris" | belief→understanding shift
QUOTE[LWTE-1:10]: Leur principal souci était de faire en sorte que les hommes croient en eux, même s'ils n'y comprenaient rien. ENDQUOTE
- [R2.2] LWTE-1:10 | Raël | Apocalypse = revelation, "comme vous pouvez le vérifier dans n'importe quel dictionnaire" | explicit invitation to verify (lexical)
QUOTE[LWTE-1:10]: comme vous pouvez le vérifier dans n'importe quel dictionnaire ENDQUOTE
- [R2.3] LWTE-1:12 | Raël | Primitives "devaient croire sans surtout chercher à comprendre" | belief without understanding = past regime
QUOTE[LWTE-1:12]: Ces primitifs qui devaient croire sans surtout chercher à comprendre. ENDQUOTE
- [R2.4] LWTE-1:13–15 | Questioner / Raël | Bones older than 25,000 years do not refute the account: there may have been earlier creations destroyed; future beings would wrongly "donner pour preuve" our bones | counter-evidence pre-empted by auxiliary hypothesis
- [R2.5] LWTE-1:27–28, 1:31–32 | Raël | "Rien n'est constant": extrapolating from a short observation to millennia is one of scientists' greatest errors; radiometric methods (C-14, K-Ar, U-Pb-Th) rest on false bases | **physical dating discounted as evidence**
QUOTE[LWTE-1:28]: l'erreur de ces méthodes de datation est de partir du principe que le comportement atomique actuel a toujours été le même ENDQUOTE
- [R2.6] LWTE-1:28 | Raël | Refers scientists to the book *Evolution ou Création* (bibliography) which develops this "très sérieusement" | external authority cited (creationist title; no author given in text)
- [R2.7] LWTE-1:44 | Raël | Whether the "great being" is a man, dog or earthworm is unknown; the only thing the Elohim could prove is that it is alive | explicit statement of what Elohim have *proved*
QUOTE[LWTE-1:44]: La seule chose qu'ont pu prouver les Elohim, c'est que c'est quelque chose de vivant. ENDQUOTE
- [R2.8] LWTE-1:45–46 | Raël | Ararat wood was analysed and found only 700 years old; even tripling for dating error gives 2,000 | **dating accepted as evidence when it disfavours the rival reading**
QUOTE[LWTE-1:46]: Même si l'on admet que les systèmes de datation font d'énormes erreurs et que l'on multiplie la datation par trois ENDQUOTE
- [R2.9] LWTE-1:47 | Raël | Even a 5,000-year-old wooden boat would not prove the ark was wooden: ordinary boats were swept up by tidal waves | rival evidence declared non-probative in advance
QUOTE[LWTE-1:47]: cela ne prouverait pas pour autant que l'arche de Noé était un bateau de bois. L'on trouvera certainement près du mont Ararat des morceaux de bateaux de bois datant de l'époque du véritable déluge ENDQUOTE
- [R2.10] LWTE-1:48 | Raël | Textual-logic argument: had it been rain, all sailors would have survived; "il est bien écrit" only Noah's vessel survived | scripture's wording used as premise
- [R2.11] LWTE-1:49–54 | Questioner / Raël | Concordant near-death testimonies do not prove a soul; concordance proves identical brain chemistry; ten people sharing a dream of a fire-breathing bull is not proof of such bulls | **concordant testimony ≠ proof of referent**
QUOTE[LWTE-1:54]: Le fait que tous les ex-comateux décrivent à peu près la même chose prouve bien qu'il s'agit de réactions chimiques identiques ENDQUOTE
- [R2.12] LWTE-1:57 | Raël | The Elohim could show feats that would seem miraculous to our best scientists; "Ils n'en feront rien, normalement", so as not to recreate incomprehension → belief → primitive religion; they want us to understand matter by ourselves | **refused proof, with reason**
QUOTE[LWTE-1:57]: Ils n'en feront rien, normalement, car ils ne veulent pas nous replacer dans un contexte d'incompréhension débouchant fatalement sur une revalorisation des croyances engendrant des religions primitives ENDQUOTE
- [R2.13] LWTE-1:70 | Raël | No god, but creators "en qui nous avons foi, c'est-à-dire confiance" | faith redefined as trust
QUOTE[LWTE-1:70]: en qui nous avons foi, c'est-à-dire confiance ENDQUOTE
- [R2.14] LWTE-1:73 | Raël | That beings 25,000 years ahead hold the religion of the infinite "est la preuve" it is the absolute religion | proof by the Elohim's authority
QUOTE[LWTE-1:73]: est la preuve qu'elle est la religion absolue et éternelle ENDQUOTE
- [R2.15] LWTE-1:76–78 | Raël | Even an open arrival with the prophets would not convince all: fanatics would call the Elohim usurpers or devil-sent; the Vatican would not hand over its fortune to a Jesus presented in the flesh | **a public landing is said not to be sufficient proof for believers**
- [R2.16] LWTE-1:77 | Raël | Montreal Jewish leader: would keep applying the Bible even if Moses said otherwise; the Elohim "doivent être plus forts que les croyances qu'ils ont engendrées" | belief as obstacle to recognition
QUOTE[LWTE-1:77]: Ils doivent être plus forts que les croyances qu'ils ont engendrées. ENDQUOTE
- [R2.17] LWTE-1:80 | Raël | One does not change the minds of people in place; they die and are replaced; "Le temps travaille pour nous" (cf. Planck at 4:143) | persuasion by generational turnover
- [R2.18] LWTE-1:119–120 | Raël | "Il a été démontré scientifiquement" (pleasure centre; electrode experiments; aroused artists more creative) | appeal to experimental science
- [R2.19] LWTE-1:129 | Raël | Never try to convince; find the common point so the other feels he found the new path alone | persuasion technique, not demonstration
QUOTE[LWTE-1:129]: Il ne faut jamais chercher à convaincre les autres, car un individu qui s'aperçoit qu'on essaie de le convaincre a tendance à renforcer sa position. ENDQUOTE
- [R2.20] LWTE-1:131 | Raël | Typology of truth-seekers; Raëlians are those who "l'ont vraiment trouvée et qui le montrent" | truth-possession claim
- [R2.21] LWTE-1:134–135 | Raël | Tradition-keepers accept both school ("l'homme descend du singe") and priest without asking why they differ | critique of compartmentalised belief
- [R2.22] LWTE-1:182–183 | Raël | Machines show man has "rien en lui de mystérieux"; man can "sans le moindre doute" regard himself as a mechanism | certainty claim from technology analogy
- [R2.23] LWTE-1:187 | Raël | The conscious "total man" need not do something to know its result | **knowledge without test**
QUOTE[LWTE-1:187]: on n’a pas besoin de faire quelque chose pour en connaître le résultat. On sait, on ressent. ENDQUOTE
- [R2.24] LWTE-1:195 | Raël | False prophets (1): those returning men to belief in an immaterial god; prophet = "celui qui révèle" | deism = false revelation
- [R2.25] LWTE-1:196 | Raël | False prophets (2): all who attribute life to chance evolution; watchmaker argument attributed to Einstein; shake watch parts "un milliard de fois"; scientists as "grands prêtres en blouse blanche"; masses "volontairement mal informées" | **mainstream biology cast as false prophecy**
QUOTE[LWTE-1:196]: Comme l'a dit Einstein, il n'y a pas d'horloge sans horloger. ENDQUOTE
- [R2.26] LWTE-2:25–26 | Raël | Satan "accumule les preuves" of human aggression and brings them to the council | evidence-gathering attributed to the opposing Eloha
- [R2.27] LWTE-2:29 | Raël | Religions were to preserve the trace until men had evolved scientifically enough "pour comprendre rationnellement" | understanding conditioned on science
QUOTE[LWTE-2:29]: quand les temps seront venus, et que les hommes auront suffisamment évolué scientifiquement pour comprendre rationnellement. ENDQUOTE
- [R2.28] LWTE-2:30–31 | Raël | Prophets are tested by Satan (diabolos = calumniator) before being entrusted with messages | credential = loyalty test, not public proof
- [R2.29] LWTE-2:35–42 | Raël | Jesus refuses to prove sonship by miracle; he "n'a pas été mis sur Terre pour mettre inutilement à l'épreuve ses créateurs" | testing the creators discouraged (scriptural model)
- [R2.30] LWTE-2:65 | "Satan" (rep.) | Offer: say ETs plan an invasion; "we will give you proofs of our existence and no one will doubt you" | **proofs are what the tempter offers**
QUOTE[LWTE-2:65]: Nous vous donnerons des preuves de notre existence et plus personne ne doutera de vos dires. ENDQUOTE
- [R2.31] LWTE-2:66 | "Satan" (rep.) | Yahweh's mission is described as given "sans vous donner de preuves pour convaincre vos frères, ni aucune aide financière" | **canon states its messenger was given no proofs**
QUOTE[LWTE-2:66]: sans vous donner de preuves pour convaincre vos frères, ni aucune aide financière ENDQUOTE
- [R2.32] LWTE-2:70 | Raël | Prefers the mission accomplished by collective effort of those who want to welcome the Elohim: "la plus belle preuve d'amour" | absence of proof/aid reframed as value
- [R2.33] LWTE-2:76 | Yahweh (rep.) | Satan will be convinced only when men are united and have abolished money and arms | proof demanded *of* humanity
QUOTE[LWTE-2:76]: ne sera convaincu que lorsque les hommes seront unis, qu'ils auront supprimé l'argent et les armes ENDQUOTE
- [R2.34] LWTE-2:85 | Yahweh (rep.) | Raël is "le dernier prophète" and the first to ask men to understand and not to believe | programmatic formula
QUOTE[LWTE-2:85]: le dernier prophète, et le premier qui s'adresserait aux hommes en leur demandant de comprendre et non de croire. ENDQUOTE
- [R2.35] LWTE-2:97–103 | Yahweh | Epistemology of prophecy: no time travel, so no prediction of individuals' future; but a species' development is predictable like a foetus's; all the predictions rest on biology of species | prophecy naturalised as developmental forecast
- [R2.36] LWTE-2:104, 2:200–202 | Yahweh | Appear openly only when it would not create new deist religions; men need a "béquille" until technological level suffices; then they will understand there is no god | timing of disclosure tied to science
- [R2.37] LWTE-2:205 | Yahweh | If humanity achieves total disarmament, men "nous prouveront" they are worthy of the heritage | proof demanded of humanity
QUOTE[LWTE-2:205]: les hommes nous prouveront qu'ils sont dignes de recevoir notre héritage étant non violents. ENDQUOTE
- [R2.38] LWTE-2:208–210 | Yahweh | 666 = number of human generations since creation (20 years × 666 = 13,320) ending with the 1945 generation | numerical "fit" offered as self-evident
- [R2.39] LWTE-3:30 | Raël | Men used to venerate; now they must understand those who created them | understanding over veneration
- [R2.40] LWTE-3:31 | Raël | foi < fides "engagement, lien": one can stop believing-without-understanding while trusting the Elohim; those intelligent enough to have faith "seront de toute façon récompensés" | **faith retained as trust, with reward**
QUOTE[LWTE-3:31]: L'on peut donc ne plus croire sans comprendre tout en faisant confiance aux Elohim, en ayant foi en eux, car ceux qui ont l'intelligence d'avoir foi en eux seront de toute façon récompensés. ENDQUOTE
- [R2.41] LWTE-3:32 | Raël | A Raëlian "sait" the Elohim will not forget him in the final cataclysm | knowledge-claim about an unobserved promise
- [R2.42] LWTE-3:33–38 | Raël | Jesus would have been dismissed by "scientifiques officiels" as abusing public credulity; official religion and press tolerate only old religions; scientists are "grands prêtres d’Etat en blouse blanche" who baptise their children | scepticism toward new prophets likened to Jesus's rejection
- [R2.43] LWTE-3:41–53 | Raël | Milgram experiment reported at length with percentages; conclusion: refuse authority | experimental psychology used as evidence
- [R2.44] LWTE-3:56, 3:58, 3:65, 3:68 | Raël | Refuse every hierarchy that removes personal responsibility; each is fully responsible | anti-obedience norm
- [R2.45] LWTE-3:75–76 | Raël | The powerful first smiled at the "jeune chevelu" speaking of saucers; now use "justice" against him as against Jesus | opposition read as confirmation pattern
- [R2.46] LWTE-3:82–83 | Raël | Reader asked to: read the two books, join, help build the residence, write to Raël, have the cellular plan transmitted — "premier acte prouvant votre reconnaissance" | asks of the reader; "proof" = act of recognition
QUOTE[LWTE-3:83]: premier acte prouvant votre reconnaissance des Elohim comme étant nos créateurs ENDQUOTE
- [R2.47] LWTE-3:85 | Raël | Do not fear "que cela ne soit qu'une illusion": "C'est faux!"; live the exaltation to the end; hundreds discovered the messages "en une nuit, d'une traite" | doubt addressed by exhortation
- [R2.48] LWTE-3:86, 4:97 | Raël (quoting guide Pierre) / Terrusse | One does not become Raëlian; one discovers one already was | recognition model of assent
- [R2.49] LWTE-1:23 | Raël | Embassy: not palace or cathedral but a simple house with modern comfort and diplomatic immunity | condition (residence)
QUOTE[LWTE-1:23]: une simple maison disposant du confort auquel tout homme a droit de nos jours, et de l'immunité diplomatique à laquelle le plus petit Etat terrestre a droit dans ses ambassades. ENDQUOTE
- [R2.50] LWTE-1:34, 1:36 | Raël | Cellular-plan transmission and frontal-bone bequest are "reconnaissance" in life and death; intent recorded by the computer suffices even if the body is destroyed | ritual as recognition; unfalsifiable recording
- [R2.51] LWTE-1:40 | Raël | Those ignorant of the messages but acting well are saved; those who know them have "aucune excuse" | knowledge of the text raises obligation
- [R2.52] LWTE-1:85, 1:87, 2:92 | Raël | Mission: spread the messages and build the embassy — "la priorité des priorités" | ask
- [R2.53] LWTE-4:2–8 | Terrusse | Evolution taught by indoctrination; Rostand quoted doubting neo-Darwinism | appeal to dissenting scientist
- [R2.54] LWTE-4:10–22 | Terrusse | Mutations always harmful (Muller); no new organism from Drosophila; inanimate matter cannot self-assemble; time only decomposes; evolution contradicts entropy | scientific-style argument for design
QUOTE[LWTE-4:22]: La théorie évolutionniste est en contradiction avec la loi de l'entropie. ENDQUOTE
- [R2.55] LWTE-4:23–25 | Terrusse | Evolutionists do not apply "méthodes vraiment scientifiques"; conclusion: life results from intervention of the Elohim | inference from anti-evolution to Elohim (no intermediate step)
- [R2.56] LWTE-4:33 | Terrusse | On the oil-ring "enigma": Raëlians hold the key | canon as explanatory key
QUOTE[LWTE-4:33]: Nous, Raëliens, avons la clef de cette énigme. ENDQUOTE
- [R2.57] LWTE-4:57 | Terrusse | "Apprenons à ouvrir les yeux, nous avons tout autour de nous pour comprendre" | evidence said to be everywhere
- [R2.58] LWTE-4:74 | Terrusse | Baptism/transmission "s'explique scientifiquement" | scientific legitimation of rite (see R5.13)
QUOTE[LWTE-4:74]: Le principe du baptême et de la transmission du plan cellulaire nous est aujourd'hui compréhensible, et cette cérémonie s'explique scientifiquement. ENDQUOTE
- [R2.59] LWTE-4:90 | Le Gendre | "La rencontre parfaite de la science et de la religion" in the age of Apocalypse | convergence claim
- [R2.60] LWTE-4:91 | Le Gendre | Church required man to "croire sans comprendre" | critique of faith
- [R2.61] LWTE-4:92 | Le Gendre | Signs of the times fulfilled: creation of life, prostheses, telecommunications, antidotes, surgery ("imposition des mains"), infant mortality, State of Israel, UFOs as "signes dans le ciel", false prophets | fulfilment list as evidence
- [R2.62] LWTE-4:102, 4:109–110 | Terrusse | "J'ai eu confirmation" in myths (Greek, Mahabharata, Gilgamesh, Kujiki, Popol Vuh, Chronicle of Akakor, Enoch, Kabbalah, Bible) and physical traces (Nazca, Baalbek, "très certainement" Tiahuanaco, Easter Island) | comparative material as confirmation
- [R2.63] LWTE-4:127 | Terrusse | "Je trouve partout autour de moi des confirmations des messages" | confirmation everywhere
QUOTE[LWTE-4:127]: Je trouve partout autour de moi des confirmations des messages. ENDQUOTE
- [R2.64] LWTE-4:143 | Terrusse | Planck: new scientific truth wins by opponents dying out | generational model of acceptance
- [R2.65] LWTE-4:144 | Terrusse | Beliefs and religions are "béquilles"; religions imposed "croire"; today our history is comprehensible | belief→understanding
- [R2.66] LWTE-4:159–161 | Giroux | Conviction in ninety minutes at a lecture ("j'en étais maintenant sûr, convaincu"); friends rejected it with "raisonnements confus, mystiques" as people rejected Jesus | conversion testimony; dissent pathologised
- [R2.67] LWTE-4:183–184 | Beluet | All religions and mythologies speak of creation by gods from the sky → "une vérité première"; evolution "pleine de failles", questioned by "d'éminents spécialistes" | concordance of traditions as evidence (contrast R2.11)
- [R2.68] LWTE-4:188 | Beluet | Knowledge is provisional; every theory is an attempt to interpret undeniable facts | fallibilism stated by a follower
- [R2.69] LWTE-4:210–211 | Deydier | He "verified one by one" the main elements, entertained many hypotheses; refuses the credo; does not believe in ETs but understands | **strongest "verify, don't believe" statement in LWTE — no method or result given**
QUOTE[LWTE-4:210]: j'ai été conduit à vérifier un par un les éléments principaux des messages des extra-terrestres ENDQUOTE
QUOTE[LWTE-4:211]: Je ne crois pas aux extra-terrestres, je comprends réellement leur rôle ENDQUOTE
- [R2.70] LWTE-4:135 | Terrusse | Being Raëlian is not a closed group "persuadé de détenir une vérité" (contrast R2.20) | internal counter-statement

## Register 3 — Forward-looking statements

Tags: dated|undated · conditional|unconditional · commitment as worded.

- [R3.1] LWTE-1:15 | Raël | Present life is not the last that will be created on Earth | undated · unconditional · further creations will occur
- [R3.2] LWTE-1:22 | Raël | The movement has not and "n'aura jamais" a paid clergy, three-quarters of a capital's buildings, or a princely palace | undated · unconditional · standing promise about the movement (paid clergy clause is checkable)
- [R3.3] LWTE-1:23, 3:82 | Raël | The Elohim "viendront" make official contact in the embassy/residence, with Moses, Jesus, Buddha, Muhammad and others | undated · conditional on the embassy being built
- [R3.4] LWTE-1:24 | Raël | If surplus money: research centre near the embassy (lab creation of life, biological robots abolishing work and money) and a school for geniuses | undated · conditional · movement plan
- [R3.5] LWTE-1:27 | Raël | The planet's location etc. "sera révélé exactement" at the official arrival | undated · conditional on arrival
- [R3.6] LWTE-1:36 | Raël | When there are millions of Raëlians governments will have to respect last wishes; Raëlism will be the dominant religion of the third millennium | **dated (third millennium) · unconditional · window open until 3000**
QUOTE[LWTE-1:36]: Le raëlisme sera la religion dominante dans le monde du troisième millénaire. ENDQUOTE
- [R3.7] LWTE-1:38 | Raël | Those recreated are recreated young, each time, eternally | undated · conditional on merit · uncheckable
- [R3.8] LWTE-1:47 | Raël | Pieces of wooden boats from the true flood (~5,000 years) "will certainly" be found near Ararat | **undated · unconditional · archaeological prediction; pre-defused as non-probative for the rival view**
- [R3.9] LWTE-1:60 | Raël | Scientific re-creation/eternal life: our scientists "mettront pas mal de temps" | undated · unconditional · vague
- [R3.10] LWTE-1:72 | Raël | He is "persuadé" the good outcome (wisdom, diffusion, embassy, arrival) will happen though the chance is one in a hundred; then men's religion becomes the infinite | undated · personal conviction against stated odds
QUOTE[LWTE-1:72]: je suis persuadé que c'est ce qui arrivera, même s'il n'y a qu'une chance sur cent pour que les hommes choisissent la voie de la sagesse ENDQUOTE
- [R3.11] LWTE-1:76, 1:81 | Raël | On arrival most religions' faithful will rally to the movement; a fanatic core will oppose and then die out by itself | undated · conditional on arrival
- [R3.12] LWTE-1:82 | Raël | A problem arises only if the Elohim arrive before present primitive beliefs have disappeared | undated · admits arrival timing is open
QUOTE[LWTE-1:82]: Le problème se posera seulement si les Elohim arrivent sur terre avant que les croyances primitives actuelles aient elles aussi totalement disparu. ENDQUOTE
- [R3.13] LWTE-1:87 | Raël | "What is sure" is that the embassy will be built soon | **undated ("bientôt", said 1979) · unconditional · commits to construction soon; no bound stated, so wording alone does not settle fulfilment; 47 years have elapsed by 2026**
QUOTE[LWTE-1:87]: ce qui est sûr c'est que l'ambassade sera construite bientôt ENDQUOTE
- [R3.14] LWTE-1:87 | Raël | Geniocracy "peut-être" will become huge and help save humanity; "peut-être" men will be saved without it | undated · explicitly uncertain
- [R3.15] LWTE-1:107 | Raël | Humanity is "sur le point de pénétrer" the golden age | undated · imminence language
- [R3.16] LWTE-1:126, 1:137 | Raël | If individuals raise consciousness / when all enjoy their sensuality, world war becomes impossible | undated · conditional
- [R3.17] LWTE-1:152 | Raël | Man "sera bientôt capable" of synthetically creating new genetic codes from inanimate matter | **undated ("bientôt") · unconditional · technological prediction** [outside knowledge — unverified: synthetic-genome work since 2010 bears on this]
QUOTE[LWTE-1:152]: l'homme, qui sera bientôt capable de créer synthétiquement de nouveaux codes génétiques, de nouveaux plans, à partir de matière inanimée. ENDQUOTE
- [R3.18] LWTE-1:183 | Raël | No human capacity will ever be found that a computer cannot be given | undated · unconditional · universal negative
QUOTE[LWTE-1:183]: l'on ne peut pas et l'on ne pourra jamais trouver une capacité qu'aurait l'homme et dont l'on ne pourrait pas doter un ordinateur. ENDQUOTE
- [R3.19] LWTE-1:67, 1:106 | Raël | We will one day create beings in our image | undated · unconditional
- [R3.20] LWTE-1:198 | Raël | Judgement rule: majority of positive acts → eternal life; else nothing; negative majority may be recreated to be judged | undated · conditional · uncheckable
- [R3.21] LWTE-2:62–65 | "Satan" (rep.) | Promises (rescue aboard a craft, money via a Swiss foundation, eternal life, proofs) if Raël helps provoke a racial world war | conditional offer, refused; never triggered
- [R3.22] LWTE-2:68 | Raël | Yahweh told him those who struggled for peace would be saved from the final cataclysm and could repopulate Earth | undated · conditional on cataclysm
- [R3.23] LWTE-2:68 | Raël (1975 scene) | Nine chances in ten humanity self-destructs; worth trying even at one in a thousand | probability (reporter's)
QUOTE[LWTE-2:68]: Je ne suis pas du tout persuadé que l'humanité va s'autodétruire, même s'il y a neuf chances sur dix que cela se produise. ENDQUOTE
- [R3.24] LWTE-2:96, 2:231 | Yahweh | Only one chance in a hundred humanity does not self-destruct; 99 % the Apocalypse scenario | **undated · probabilistic · no time horizon given — cannot fail on any date**
QUOTE[LWTE-2:96]: Il n'y a malheureusement qu'une chance sur cent pour que votre humanité ne s'auto-détruise pas ENDQUOTE
QUOTE[LWTE-2:231]: C'est hélas ce qui attend les hommes avec quatre-vingt-dix-neuf pour cent de chance. ENDQUOTE
- [R3.25] LWTE-2:98 | Yahweh | "Nous savons avec précision" what happens to a humanity at our technological level without equal wisdom | certainty about a class outcome
QUOTE[LWTE-2:98]: nous savons avec précision ce qui se produit lorsqu'une humanité arrive à votre niveau technologique sans avoir atteint un niveau de sagesse équivalent. ENDQUOTE
- [R3.26] LWTE-2:102 | Yahweh | The Elohim could foresee the age of Apocalypse would come when men make the blind see with electronic prostheses, carry voice by satellite, and create synthetic beings in the laboratory | retrospective prediction; third marker stated as a feature of the present age
- [R3.27] LWTE-2:139 | Yahweh | Famine will cause many deaths "avant que les hommes ne la résolvent complètement sur la terre" | undated · implies complete resolution of famine
- [R3.28] LWTE-2:153–154 | Yahweh | From the final catastrophe, "si elle a lieu", those who follow the prophet and had the cellular plan transmitted will be saved, selected by the great computer | undated · conditional
- [R3.29] LWTE-2:158 | Yahweh | Those "sealed on the forehead" will total about 144,000, including those already recreated, the unknowing righteous, and those who recognised Raël | undated · numerical cap/target
QUOTE[LWTE-2:158]: Le total de ceux qui seront «scellés au front» sera d'à peu près cent quarante-quatre mille ENDQUOTE
- [R3.30] LWTE-2:159 | Yahweh | Until the total reaches ~144,000 "nous ferons en sorte que le cataclysme final soit retardé" | **undated · conditional · promise of active intervention to delay nuclear war**
QUOTE[LWTE-2:159]: Aussi longtemps que le total de ces hommes ne sera pas d'environ cent quarante-quatre mille, nous ferons en sorte que le cataclysme final soit retardé ENDQUOTE
- [R3.31] LWTE-2:160–219 | Yahweh | Seventh seal = world atomic war: a third of the earth burned, lava into oceans, waters poisoned, sky darkened, bombers, chain reaction making continents drift and rocks fall thousands of km away | undated · conditional scenario ("Voilà ce qui attend l'humanité si…", 2:229)
- [R3.32] LWTE-2:205 | Yahweh | If humanity passes the test and disarms totally, it proves itself worthy of the heritage | undated · conditional
- [R3.33] LWTE-2:228 | Yahweh | The saved will live on the planet of the Eternals until re-implanted on a habitable Earth | undated · conditional
- [R3.34] LWTE-2:231, 3:79 | Yahweh / Raël | Disjunction: either planetary consciousness and golden age, or "tout sautera" and the faithful are saved to rebuild | undated · exhaustive disjunction — no outcome falsifies
- [R3.35] LWTE-2:232, 2:123 | Yahweh | "Celui qui était le premier sur la terre et qui y sera le dernier"; "les derniers si les hommes s'auto-détruisent" | conditional
- [R3.36] LWTE-2:235 | Yahweh | "Notre héritage est prêt" — it suffices that the child not die at birth | undated · conditional transfer of knowledge
- [R3.37] LWTE-2:202 | Yahweh | When the time comes men will understand there is no god and that the Elohim are their creators | undated · unconditional
- [R3.38] LWTE-3:27 | Raël | The Raëlian awaits the return of Jesus, Moses, Buddha, Muhammad, Joseph Smith and all great prophets with the Elohim, "comme les Ecritures l'annoncent" | undated · expectation
- [R3.39] LWTE-3:31 | Raël | If a nuclear cataclysm occurs, those who tried to prevent it in the Elohim's name will be saved | undated · conditional
- [R3.40] LWTE-3:64 | Raël | "Irresponsables" will have to answer one day | undated
- [R3.41] LWTE-3:79 | Raël | The triumph of truth "n'est plus très loin, et vous aurez la chance de le vivre"; "Cette génération ne passera pas que tout ne soit révélé" applies to those living the age entered in 1945: "Cette génération, c'est vous !" | **generation-bound · addressees (Raëlians of 1979) will live to see it, in one of two forms (golden age on Earth / on the planet after destruction). The text elsewhere reckons a generation at twenty years (2:208). Window is closing but, on the wording, lapses only with the death of the 1979 addressees**
QUOTE[LWTE-3:79]: Même si le temps du triomphe de la vérité n'est pas encore là, il n'est plus très loin, et vous aurez la chance de le vivre. ENDQUOTE
QUOTE[LWTE-3:79]: Cette génération, c'est vous ! ENDQUOTE
- [R3.42] LWTE-3:83 | Raël | "Je répondrai personnellement à votre lettre" | personal promise to readers
- [R3.43] LWTE-4:73 | Terrusse | Where will we be in 50, 100, 1,000 years | rhetorical
- [R3.44] LWTE-4:127, 4:131 | Terrusse | We are "très près" of repeating laboratory creation of life; tissue regeneration, organ replacement, new animal species, "à terme" synthesis of humanoids in our image | undated · unconditional · technological
- [R3.45] LWTE-4:132 | Terrusse | RNA coding study will lead to using "substances mémorielles" transferable from one individual to another | undated · unconditional · testable [outside knowledge — unverified: 1960s–70s memory-transfer experiments were not replicated]
- [R3.46] LWTE-4:90 | Le Gendre | Nearly forty prophets will return with the creators; official coming to hand over the scientific heritage | undated
- [R3.47] LWTE-4:145 | Terrusse | Humanity is on the eve of its birth, perhaps its death; those who misread "apocalypse" may yet be right | undated · open
- [R3.48] LWTE-4:175 | Giroux | The time approaches when colleagues will speak to him of the messages: "J'en suis sûr" | personal

**Null result:** LWTE contains no calendar deadline for the embassy, the arrival, or the cataclysm. The only dated forward statement is "troisième millénaire" (R3.6); the only bounded one is the generation clause (R3.41).

## Register 4 — Checkable-in-principle statements

- [R4.1] LWTE-1:2 | Questioner | Second meeting 7 October "30 (1975)"; nearly 24 hours on the planet | Raël's whereabouts 7–8 Oct 1975; witnesses
- [R4.2] LWTE-1:3 | Questioner | First craft: red flashing light descending, white light on top; second: instantaneous at Roc Plat, vanished "comme s'il s'était désintégré" | no trace expected by the text's own account
- [R4.3] LWTE-1:9 | Raël | Nervous shock caused incipient stomach ulceration lasting several months after first contact | medical records 1973–74
- [R4.4] LWTE-1:13–15 | Questioner / Raël | Life on Earth created 25,000 years ago; older bones belong to earlier, destroyed creations; "une infinité" of creations and destructions | stratigraphic/genetic continuity across 25 ka; absence of sterile horizon [outside knowledge — unverified]
QUOTE[LWTE-1:15]: Car la vie qui se trouve actuellement Terre n'est pas la première qui y fut créée et n'est pas la dernière qui y sera créée. ENDQUOTE
- [R4.5] LWTE-1:147 | Raël | The Elohim came to Earth "alors qu'il n'y avait pas de vie" | conflicts with R4.4 unless prior life was wholly erased; same test
QUOTE[LWTE-1:147]: Les Elohim sont venus sur la terre alors qu'il n'y avait pas de vie. ENDQUOTE
- [R4.6] LWTE-1:26 | Questioner | Msg 1 p.114: Elohim planet a little under one light-year away; scientists: nearest star ~4 ly | parallax/proper-motion surveys for an object < 1 ly
- [R4.7] LWTE-1:27 | Raël | Light does not travel at the same speed in all "couches" of the universe; nothing is constant in space or time | spectroscopy of distant sources, pulsar timing [outside knowledge — unverified]
QUOTE[LWTE-1:27]: la lumière ne se déplace pas à la même vitesse dans toutes les couches de l'univers, car rien n'est constant ni dans l'espace ni dans le temps. ENDQUOTE
- [R4.8] LWTE-1:28 | Raël | C-14, K-Ar, U-Pb-Th dating are wrong because atomic behaviour was not always the same | concordance of independent decay systems, varves, tree rings, ice cores [outside knowledge — unverified]
- [R4.9] LWTE-1:30–31 | Questioner / Raël | Original continent created 25,000 years ago; continents at first separated by several hundred km per year, now a few cm | sea-floor age/magnetic stripes, sediment thickness, heat budget
QUOTE[LWTE-1:31]: Actuellement les continents s'écartent peut-être de quelques centimètres par an, au commencement, ils s'éloignaient de plusieurs centaines de kilomètres chaque année. ENDQUOTE
- [R4.10] LWTE-1:31 | Raël | A recent earthquake near the Arabian peninsula opened a fault separating two regions by more than a metre in one night | seismological record late 1970s [outside knowledge — unverified: possibly the 1978 Afar/Asal rifting episode]
- [R4.11] LWTE-1:34, 1:36, 2:154 | Raël / Yahweh | A huge computer records each person's genetic code from conception and all acts | not checkable as stated
- [R4.12] LWTE-1:46 | Raël | Wood from Ararat glacier "récemment analysés" and found 700 years old (≈ 1200 CE) | published radiocarbon results on the Ararat wood [outside knowledge — unverified]
- [R4.13] LWTE-1:47–48 | Raël | The real flood ~5,000 years ago: explosions, enormous tidal waves; a cataclysm that overturned the Earth's surface | global ~3000 BCE destruction horizon; continuity of Egyptian/Mesopotamian records [outside knowledge — unverified]
- [R4.14] LWTE-1:50–54 | Raël | All mental states are electrochemical; electrodes at the same spot in a thousand brains give the same sensations and visions | neurostimulation studies
- [R4.15] LWTE-1:59 | Raël | Elohim can alter planetary trajectories and move whole solar systems with waves unknown to us | not checkable
- [R4.16] LWTE-1:68; 2:21, 2:31; 3:5–25, 3:31, 3:78, 3:81 | Raël | Etymologies: âme < anima; Lucifer "porteur de lumière"; diable < diabolos "calomniateur"; étymologie < etumos + logos ("science"); ange < angelos; messie < Aramaic meschîhâ; seigneur < senior; évangile < euaggelion; église < ekklêsia; pape < pappas; pontife < pontifex (root of *pont*, extended to planet-to-planet link); prophète < prophêtês "celui qui révèle"; religion < religio "ce qui relie"; catholique < katholikos; athée < athéos; culte < cultus; foi < fides "engagement, lien"; alléluia "loué soit Yahvé"; amen; Elohim "ceux qui sont venus du ciel" in Hebrew; Apocalypse "révélation" | standard lexica; most are conventional, several are glosses [outside knowledge — unverified: *prophêtês* is usually "one who speaks forth/for"; *religio* derivation is disputed; the Elohim gloss is not the consensus derivation]
- [R4.17] LWTE-1:69; 2:8–16, 2:33–46, 2:49–56, 2:108–227; 3:35 | Raël / Yahweh | Bible quotations (Gen 9:4–5; Lev 17:11; Matt 4, 13, 27:20; Job 1–2; Rev 1–21) in a translation printing "Elohim"/"Yahvé" | collate against the Dhorme Pléiade (cf. woh-claim-0066)
- [R4.18] LWTE-1:77 | Raël | Recent lunch with a leader of Montreal's Jewish community | biographical
- [R4.19] LWTE-1:84 | Raël | Published *La géniocratie*; a party was formed and fielded a candidate a few months later | electoral records
- [R4.20] LWTE-1:119–120 | Raël | Pleasure centre shown by electrode experiments; an experiment showed sexually aroused artists more creative | literature check (second claim unsourced)
- [R4.21] LWTE-1:149 | Raël | All living things share one "alphabet" "dont chaque lettre serait un atome"; reproducing species merely reproduce the code of the first exemplar made by the Elohim | molecular biology (letters are nucleotides); fixity vs observed divergence
- [R4.22] LWTE-1:156, 1:169 | Raël | A wheeled computer navigating by TV cameras; a battery robot that plugs itself in to recharge | 1960s–70s robotics [outside knowledge — unverified]
- [R4.23] LWTE-1:176 | Raël | Ordinary men use on average ten per cent of the brain's possibilities | neuroscience [outside knowledge — unverified: regarded as a myth]
- [R4.24] LWTE-1:190 | Raël | Sexual differentiation in utero comes late; homosexuality is genetic; homosexual behaviour occurs in animals | biology literature
- [R4.25] LWTE-1:196 | Raël | "Pas d'horloge sans horloger" attributed to Einstein | attribution check [outside knowledge — unverified: commonly attributed to Voltaire]
- [R4.26] LWTE-2:1–2; 1:2; 4:219 | Editor / Questioner / Deydier | Era reckoning: 7 Oct 1975 = year 30; "an 34 (1979)"; 22 May 1979 = "an 33 après Raël" | internally consistent only if year changes on 6 August 1979 → ch.2 note written after that date
- [R4.27] LWTE-2:6–11, 2:17 | Raël | Elohim history: synthetic organisms, escaped monsters, ban; first planet's creation destroyed; two failures (star radiation; invasive vegetation); life also created on two other planets | not checkable
- [R4.28] LWTE-2:27–28 | Raël | Noah's craft orbited Earth with humans and stored genetic codes; an automatic vessel from the Elohim's own creators revealed they too were created | not checkable
- [R4.29] LWTE-2:79, 2:85–87 | Raël / Yahweh (rep.) | After Hiroshima (6 Aug 1945) a woman was selected, abducted, inseminated; an affluent Jewish man had been steered to meet her beforehand; he believed himself the father | civil records; timing vs Raël's birth date [outside knowledge — unverified: 30 Sept 1946]; paternity in principle genetic
- [R4.30] LWTE-2:158 | Yahweh | The frontal bone "contient le code génétique le plus pur et le plus fidèle" | genome comparison across tissues
QUOTE[LWTE-2:158]: l'os frontal qui contient le code génétique le plus pur et le plus fidèle. ENDQUOTE
- [R4.31] LWTE-2:208–209 | Yahweh | First humans created about 13,000 years ago; 666 generations of 20 years = 13,320; the 666th generation was born in 1945 | arithmetic holds; human remains and art older than 13 ka bear on it [outside knowledge — unverified]; relation to the 25,000-year figure (R4.4) not explained here
QUOTE[LWTE-2:208]: Les premiers hommes ayant été créés il y a environ treize mille ans, si l'on multiplie la durée d'une génération humaine estimée à vingt ans par six cent soixante-six on obtient un total de treize mille trois cent vingt ans. ENDQUOTE
- [R4.32] LWTE-2:147 | Yahweh | "Quelques milliers" of earthlings already recreated on the planet | not checkable
- [R4.33] LWTE-2:153, 2:213–216 | Yahweh | Nuclear chain reaction could make continents drift abruptly and sweep away mountains | geophysics/energy budget
- [R4.34] LWTE-3:41–46, 3:53, 3:61 | Raël | Milgram: 30 switches, 15–450 V; 60 % obedient in the US; over 70 % in European replications; 85 % in Germany; cites *Soumission à l'autorité*, Paris, 1974 | Milgram's publications and replications [outside knowledge — unverified]
QUOTE[LWTE-3:45]: le record absolu étant atteint en Allemagne, avec quatre-vingtcinq pour cent ENDQUOTE
- [R4.35] LWTE-3:75–76 | Raël | Anxious during the first two years; authorities now use "justice" against him; "je suis trois mille" | court records to 1979; membership figures
QUOTE[LWTE-3:76]: Je ne suis plus seul, je suis trois mille. ENDQUOTE
- [R4.36] LWTE-4:2, 4:6–8, 4:10 | Terrusse | Quotations from Jean Rostand (*L'évolution*, 1960) and H.-J. Muller (Nobel 1946) | source check of quotations
- [R4.37] LWTE-4:11–22 | Terrusse | No beneficial mutation; no new organism ever from mutation; self-assembly impossible; entropy forbids evolution | experimental evolution literature; open-system thermodynamics [outside knowledge — unverified]
- [R4.38] LWTE-4:26–30 | Terrusse | CIA commissioned the "Hudson Institut"; Prof. Nehring found an "anneau pétrolier" at end-Triassic continental configuration | locate the study [outside knowledge — unverified: project memory records the Nehring citation as traced to RAND, not Hudson]
QUOTE[LWTE-4:26]: La C.I.A., la centrale de renseignements U.S., a confié au Hudson Institut le soin de réaliser une étude ENDQUOTE
- [R4.39] LWTE-4:31–32 | Terrusse | Oil and coal require rapid burial; coal 2,000 m thick in northern France, 18,000 km² in the Appalachians; "aucune théorie actuelle" explains it | coal geology
- [R4.40] LWTE-4:34–41 | Terrusse | The flood destruction blasted the original continent; oil ring = ejecta rim; plates slid apart rapidly, slowing to today's cm/yr "vitesse résiduelle" that tends to decrease | age of oil source rocks; measurable plate deceleration (geodesy)
QUOTE[LWTE-4:41]: La vitesse d'écartement des continents que nous mesurons aujourd'hui est une «vitesse résiduelle », qui tend à décroître dans le temps. ENDQUOTE
- [R4.41] LWTE-4:42–46 | Terrusse | Andes, Rockies, Himalaya, Australian cordillera formed by post-flood plate motion; Antarctica drifted south keeping tropical vegetation under ice | orogeny dating; ice-core ages
- [R4.42] LWTE-4:47–48 | Terrusse | Sudden temperature change entombed "animaux et plantes de zone tropicale" in frozen mud; mammoths emerge from Siberian ice | mammoth carcass dates and ecology
- [R4.43] LWTE-4:54–55 | Terrusse | Dinosaurs and great reptiles were antediluvian species not re-created after the flood; hence their sudden simultaneous disappearance | **implies dinosaurs alive within the last ~25 ka until ~5 ka; fossil dating and absence of human–dinosaur co-occurrence bear on it**
QUOTE[LWTE-4:54]: ce fut le cas de tous les grands reptiles, dinosaures et autres sauriens épouvantables. ENDQUOTE
- [R4.44] LWTE-4:56 | Terrusse | All traces of Elohim presence found on Earth are post-diluvian | dating of cited sites (Nazca, Baalbek, etc.)
- [R4.45] LWTE-4:73 | Terrusse | Hertz discovered his waves only "dans les années 1920"; NMR known since 1946 | history of physics [outside knowledge — unverified: Hertz's experiments date to the 1880s]
QUOTE[LWTE-4:73]: Hertz n'a découvert les ondes qui portent son nom que dans les années 1920 ENDQUOTE
- [R4.46] LWTE-4:75–77 | Terrusse | Each person's chromosomal plan has an electromagnetic emission spectrum; a guide, hands wetted for electrical contact, relays it to a space relay | measurement of such emission; no detection claimed
- [R4.47] LWTE-4:83–85 | Le Gendre | European trip from 10 June 1976; bought msg 1 on 30 June and msg 2 on 2 July (Geneva, Clermont-Ferrand); Radio-Canada International interview broadcast in 1975–76 season | broadcast archives
- [R4.48] LWTE-4:104–107 | Terrusse | "Mahabarata … avec ses deux parties: les Védas et le Ramayana"; Kujiki; Popol Vuh; *Chronique d'Akakor* | bibliographic accuracy [outside knowledge — unverified: Vedas and Ramayana are not parts of the Mahabharata; the Akakor chronicle is a 1970s publication of disputed authenticity]
- [R4.49] LWTE-4:114–121 | Terrusse | Einstein's light-speed postulate is a "monumental error"; space is filled with a sub-quantum medium whose pressure causes attraction; wave speed depends on local energy density; all light-year distances are overestimated, stars are much nearer | parallax, radar/laser ranging, spacecraft telemetry
QUOTE[LWTE-4:121]: Les étoiles qui nous entourent sont beaucoup plus près que ce que nous croyons. ENDQUOTE
- [R4.50] LWTE-4:124–125 | Terrusse | Two quotations on time, unattributed | source not given
- [R4.51] LWTE-4:129 | Terrusse | Genes synthesised from nucleotides; DNA segments implanted in bacterial chromosomes | 1970s molecular biology [outside knowledge — unverified]
- [R4.52] LWTE-4:159 | Giroux | Lecture by Claude Vorilhon on 9 November 1976 at the auditorium Le Plateau, Montréal | event record
- [R4.53] LWTE-4:175 | Giroux | Removed from teaching religion as specialist after joining | employment record
- [R4.54] LWTE-4:191 | Beluet | Message entrusted in December 1973; second contact 1975 | consistent with woh-claim-0020
- [R4.55] LWTE-1:18 | Raël | The people of Israel were created in the laboratory located there; Jews descend from sons of Elohim and daughters of men | population genetics in principle; not operationalised
- [R4.56] LWTE-1:91–94 | Raël | Scientists who give the universe a size and an age measure only what is perceived; everything is eternal; seeking a beginning in time is "stupide" | cosmological observations (expansion, CMB) [outside knowledge — unverified]

## Register 5 — Declared unknowns and refusals

- [R5.1] LWTE-1:27 | Raël | Elohim absolutely do not want us to know where their planet is | refusal (by Elohim), reason: human destructiveness
QUOTE[LWTE-1:27]: Les Elohim ne veulent absolument pas que nous sachions où se situe leur planète ENDQUOTE
- [R5.2] LWTE-1:12 | Raël | The trip was first refused; the reason given then is now said not to have been the real one | refusal + admitted pretext
- [R5.3] LWTE-1:44 | Raël | "Rien ne dit" the great being is a man; perhaps a dog or an earthworm | declared unknown (even to Elohim)
- [R5.4] LWTE-1:57 | Raël | Elohim will "normalement" not demonstrate their capacities | refusal of demonstration ("normalement" leaves an exception open)
- [R5.5] LWTE-1:59 | Raël | They use "des ondes que nous ne connaissons pas encore" | mechanism undisclosed
- [R5.6] LWTE-1:18, 1:31, 1:87 | Raël | "Peut-être" markers: why sons of Elohim were tempted; present drift rate; geniocracy's future | reporter's own uncertainty
- [R5.7] LWTE-1:72, 2:68 | Raël | Not at all sure humanity will self-destruct; persuaded of the good outcome | subjective stance vs stated odds
- [R5.8] LWTE-2:1, 2:90 | Editor / Raël | Three-year embargo on the Satan episode and the paternity; no reason is given for the delay | withheld, unexplained
- [R5.9] LWTE-2:97, 2:99 | Yahweh | Impossible to predict the future or individuals' futures; impossible to travel in time | **declared limit on Elohim foreknowledge**
QUOTE[LWTE-2:97]: Il est impossible de prédire l'avenir, car il est impossible de voyager dans le temps, mais il est possible de prédire l'avenir d'une entité biologique ENDQUOTE
- [R5.10] LWTE-2:199–200 | Yahweh | John was told to seal and not write the no-god explanation | withheld from an earlier recipient
- [R5.11] LWTE-2:57 | Raël | Yahweh explained to Job only "sommairement" | partial disclosure as precedent
- [R5.12] LWTE-2:77 | "Satan" (rep.) | Does not think there are more than a dozen men like Raël | opinion, unquantified
- [R5.13] LWTE-4:71–72 | Terrusse | Present technology cannot detect the body's molecular emissions or isolate one molecule's signal; "Mais avec le temps..." | declared present unverifiability of the baptism mechanism
QUOTE[LWTE-4:71]: Notre technologie, aujourd'hui, ne nous permet pas d'appréhender de tels phénomènes sur un ensemble aussi complexe que le corps humain ENDQUOTE
- [R5.14] LWTE-4:27, 4:30, 4:32 | Terrusse | The oil ring is "une énigme" for Nehring and geologists; no current theory explains coal burial | unknown attributed to science, then filled by canon
- [R5.15] LWTE-4:109 | Terrusse | "Très certainement" Tiahuanaco, Easter Island | hedge
- [R5.16] LWTE-4:188 | Beluet | All knowledge is provisional | general fallibilism
- [R5.17] LWTE-3:77 | Raël | Hopes his father will judge him no longer useful on Earth and let him join the prophets | personal unknown
- [R5.18] (null) LWTE-2:94–235 | — | No statement of when, where or how the 1979 "Message de Yahvé" was received | absent
- [R5.19] (null) LWTE passim | — | No physical evidence, third-party witness, recording or document of either contact is offered or mentioned; the only "proofs" promised are those Satan offers (R2.30) | absent
- [R5.20] (null) LWTE passim | — | No statement that any part of the three books is Raël's own addition, apart from *La géniocratie* (R1.14), the "J'y ajouterai" physics (R1.9) and the adapted vocabulary (R1.11) | absent

---

## Patterns, tensions, counter-examples, null results (analysis — fork's reading, not the text's)

1. **LWTE is the canon's first self-revision.** It opens by listing contradictions between books 1 and 2 (R1.2) and resolves them by reclassifying earlier content as staging (R1.3–4, R1.12), a put-off told as to a child (R1.6), or audience-adapted wording (R1.11). On the text's own terms, statements in the dictated books are therefore not uniformly literal.
2. **"Comprendre et non croire" (R2.34) coexists with retained faith.** Faith is redefined as trust and attached to reward (R2.13, R2.40); assent is modelled as recognition (R2.48) and as knowing without testing (R2.23).
3. **Proof is asymmetric.** Demonstrations are refused by the Elohim (R2.12), described as not given to the messenger (R2.31), and offered only by the tempter (R2.30); meanwhile humanity must *prove* itself (R2.33, R2.37). A public arrival is even said to be insufficient for believers (R2.15).
4. **Evidence standards shift with direction.** Radiometric dating is void (R2.5) yet a 700-year date settles the Ararat wood (R2.8); concordant NDE testimony proves nothing about its referent (R2.11) yet concordant creation myths are a "vérité première" (R2.67).
5. **Counter-evidence is pre-empted** rather than awaited: older bones (R2.4), a future Ararat boat (R2.9), slow continental drift (R4.9).
6. **Forward statements are almost all undated, conditional or disjunctive** (R3.24, R3.34). Exceptions: "third millennium" (R3.6), "bientôt" for the embassy (R3.13) and synthetic genomes (R3.17), and the generation clause (R3.41).
7. **Non-intervention vs intervention:** Yahweh "understood we must not intervene" (2:76) but will delay the cataclysm until ~144,000 are sealed (R3.30).
8. **Probabilities are inconsistent across voices:** 9/10 (Raël, 1975 scene), 99/100 (Yahweh, 1979), 1/100 survival repeated by Raël (R3.10, R3.23–24).
9. **Chronology strain:** life "25,000 years" (R4.4), no life before arrival (R4.5) vs infinite prior creations (R4.4), first humans "13,000 years" (R4.31), flood "5,000 years" (R4.13), and ch.4's dinosaurs as antediluvian (R4.43).
10. **Ch.4 is the most checkable and the most exposed layer**, and it is followers' commentary, not Elohim speech: Terrusse's geology and physics (R4.38–49) include a dating slip on Hertz (R4.45) and a misdescribed Mahabharata (R4.48).
11. **Counter-examples to "discourages verification":** dictionary check invited (R2.2); Deydier's "vérifier un par un" (R2.69); Montaigne's sieve (R1.45); Beluet's fallibilism (R2.68); the anti-authority chapter even against an Eloha (R1.41, R2.44).
12. **Authority of science is used both ways:** "démontré scientifiquement" (R2.18, R2.43, R2.58) vs scientists as white-coated high priests and false prophets (R2.25, R2.42).
13. **Edition layer:** footnotes and address list post-date 1998 (R1.17, R1.49); two footnotes split running sentences (2:60, 2:83), so the dump is not a clean 1979 witness.
14. **Nulls:** no dated deadline; no reception circumstances for the 1979 Yahweh message; no physical proof offered; no reason for the three-year embargo (R5.8, R5.18–20).
15. **Relation to core:** R1.1–R1.6 and R1.18–25 extend woh-claim-0035 (staged disclosure, later books reframing earlier); R3.3/R3.13/R3.41 bear on woh-claim-0015's "conditional not predicted" wording (one unconditional "bientôt" and one generation-bound clause exist); R2.25 and R2.53–55 bear on woh-claim-0036's "two walls".
