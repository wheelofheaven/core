# Finding: woh-exp-0008

- Date: 2026-11-22
- Source and edition inspected: project digitizations in `data-library`, French base text (`text` field) only:
  - *Les extra-terrestres m'ont emmené sur leur planète* (1975), code ETTMTTP, `extraterrestrials-took-me-to-their-planet/chapter-1.json` (77 paragraphs), `chapter-2.json` (132), `chapter-3.json` (266).
  - *Accueillir les extra-terrestres* (1979), code LWTE, `lets-welcome-the-extraterrestrials/chapter-1.json` (201), `chapter-2.json` (235), `chapter-3.json` (88), `chapter-4.json` (312).
  - The LWTE file carries an editorial footnote dated after 1998 (LWTE-3:26), so the digitized text follows a later reprint, not the 1979 printing. No printed edition was compared.
- Access achieved: `project_digitization` (complete text of all seven chapter files).
- Search performed:
  - Case-insensitive substring search of the `text` field of every paragraph in all seven files for the twenty protocol terms. Hit counts (substring, whole book):
    - ETTMTTP: création 12, créé 29, créer 20, créateurs 57, laboratoire 0, vie 139, espèce 3, animaux 6, plantes 4, homme 141, humanité 26, évolution 2, évolué 9, hasard 6, singe 0, Darwin 0, sélection 3, mutation 0, apparition 3, spontané 0.
    - LWTE: création 38, créé 50, créer 18, créateurs 70, laboratoire 21, vie 186, espèce 18, animaux 13, plantes 1, homme 295, humanité 73, évolution 29, évolué 5, hasard 11, singe 3, Darwin 2, sélection 8, mutation 9, apparition 4, spontané 1.
  - Added terms: créa, laborat-, animal, végét-, apparu, génétique, ADN, synth-, ancêtre, fabriqu-, façonn-, image, naturel, descend-, origine, race, vivant, primitif, premiers hommes, nos pères, Genèse, adapt-, transform-, engendr-, déluge, arche.
  - Reading: every paragraph containing any term other than the bare high-frequency words (vie, homme, humanité, naturel, descend-, origine, race) was read in full (127 paragraphs in ETTMTTP, 210 in LWTE), with neighbours where the passage ran on (e.g. ETTMTTP-2:30-36, 3:217-224; LWTE-1:144-154, 2:1-31, 4:1-60).
  - Limit: paragraphs whose only hits were the bare high-frequency words (115 in ETTMTTP, 180 in LWTE) were not read in full. They were screened sentence by sentence with the added terms above, and each sentence that matched was read. A passage on origins that uses none of those terms would have been missed.
  - The `i18n.en` rendering was not used for any quotation.

## Answer

Counting unit: one paragraph (refId), one class. A paragraph is listed when it contains a statement about how terrestrial organisms or humans came to exist or changed; paragraphs that only use the epithet "nos créateurs" without such a statement are not listed.

| Class | ETTMTTP (1975) | LWTE (1979) |
|---|---|---|
| `designed` | 25 | 39 |
| `undirected` | 0 | 0 |
| `rejected_view` | 0 | 18 |
| `ambiguous` | 1 | 4 |

- Both books attribute terrestrial life and humans to creation by the Elohim, repeatedly and in general terms ("toute vie", "toutes les formes de vie que nous connaissons, y compris l'homme", "Chaque être vivant présent sur terre actuellement").
- No passage in either book attributes the origin of any terrestrial organism, or its transformation into another kind, to a process without their intervention.
- The 1975 book does not discuss evolution, chance origin, apes, Darwin or mutation at all (zero hits for singe, Darwin, mutation, laboratoire, spontané). The 1979 book reports the evolutionary account several times, each time to reject it.
- The five `ambiguous` paragraphs are quoted in full below. One (LWTE-1:107) says in Raël's voice that present humans are "le fruit d'une longue sélection naturelle". Three (LWTE-4:11, 4:13, 4:16, in Marcel Terrusse's essay) affirm that mutations alter size, shape and colour inside a species while denying they produce a new organism. One (ETTMTTP-2:123) derives the people of Israel from unions of "fils d'Elohim" and "filles des hommes"; it is ambiguous only as to class fit (neither laboratory creation nor a process without them).

### Passages classed `designed`

Scope tag: H = humans, N = non-human life, B = both.

ETTMTTP (speaker field as given in the file):

| refId | Speaker | Scope | French sentence |
|---|---|---|---|
| 2:34 | Yahweh | B | "seules les formes peuvent changer selon la volonté de ceux qui atteignent un niveau scientifique leur permettant de réaliser cela." (said "en ce qui concerne l'origine de la vie sur terre") |
| 2:51 | Yahweh | B | "comme sur terre, nous avons créé ici toute vie" |
| 2:53 | Yahweh | H | "fabriqués selon le même principe que nous avons utilisé pour créer les hommes de la Terre, d'une manière cent pour cent scientifique" |
| 2:59 | Yahweh | H | "la nudité, l'image de ce que nous avons fait !" |
| 2:104 | Yahweh | H | "Leur faute originelle fut de s'être unis à leur création scientifique" |
| 2:121 | Yahweh | H | "celui qui ramènera à leurs créateurs ceux qu'ils ont créés" |
| 3:11 | Yahweh | H | "les Elohim nous ont créés à leur image, donc capables de nous reproduire par nous-mêmes" |
| 3:23 | Yahweh | H | "refaire ce que leurs créateurs ont fait : créer ailleurs d'autres humanités, scientifiquement." |
| 3:30 | Yahweh | B | "Nos créateurs nous ont donné des sens [...] tout ce qui nous entoure et que nos créateurs ont placé là pour que nous en jouissions." |
| 3:35 | Yahweh | H | "ceux qu'ils ont créés avoir honte de l'aspect qui leur a été donné." |
| 3:36 | Yahweh | B | "comme on doit aimer chaque partie de la création des Elohim" |
| 3:37 | Yahweh | H | "Chacun de nos organes a été créé par nos pères les Elohim" |
| 3:74 | Yahweh | H | "cette partie de l'infini qui a été organisée par nos créateurs selon un plan bien précis" |
| 3:102 | Yahweh | N | "En respectant la nature, tu respectes ceux qui l'ont créée, nos pères les Elohim." |
| 3:109 | Yahweh | H | "nos créateurs qui nous ont créés à leur image." |
| 3:127 | Yahweh | H | "tous les êtres humains parce qu'ils sont faits à votre image" |
| 3:159 | Yahweh | H | "Toutes les races qui peuplent la Terre ont été créées par les Elohim" |
| 3:166 | Yahweh | H | "les Elohim, tes créateurs, t'ont créé scientifiquement." |
| 3:177 | Yahweh | B | "tout ce que tu ne comprends pas et que tes scientifiques ne peuvent expliquer est dû aux Elohim, car l'horloger connaît tous les rouages de la montre qu'il a fabriquée." |
| 3:185 | Yahweh | H | "aucune des caractéristiques physiques des hommes ne leur a été donnée pour rien." |
| 3:218 | Yahweh | H | "Vous n'étiez que matière, poussière, et les Elohim ont fait de vous des êtres vivants capables de dominer la matière, à leur image" |
| 3:219 | Yahweh | H | "Les Elohim ont créé les premiers hommes sans savoir qu'ils faisaient ce qui avait déjà été fait pour eu" |
| 3:225 | Yahweh | B | "ceux qui sont maintenant capables de comprendre comment la vie peut être créée" |
| 3:242 | Yahweh | H | "quelle a été leur oeuvre quand ils ont créé les hommes" |
| 3:243 | Yahweh | H | "faire fonctionner les organes que leur ont donné leurs créateurs" |

LWTE (speaker field is "Narrator" throughout; actual voice noted):

| refId | Voice | Scope | French sentence |
|---|---|---|---|
| 1:10 | Raël | H | "leurs créatures incapables de comprendre qui étaient ces êtres venus du ciel" |
| 1:13 | questioner | B | "Les Elohim disent avoir créé la vie sur Terre il y a vingtcinq mille ans." |
| 1:14 | Raël | B | "ils y ont créé toutes les formes de vie que nous connaissons, y compris l'homme." |
| 1:15 | Raël | B | "la vie qui se trouve actuellement Terre n'est pas la première qui y fut créée et n'est pas la dernière qui y sera créée." |
| 1:18 | Raël | H | "le peuple qui avait été créé dans le laboratoire situé à cet endroit de notre planète." |
| 1:64 | Raël | H | "eux, les Elohim, qui nous avaient créés à leur image." |
| 1:65 | Raël | H | "leur création d'êtres intelligents leur ressemblant." |
| 1:106 | Raël | H | "le privilège qu'ils nous créent à leur image" |
| 1:147 | Raël | B | "Les Elohim sont venus sur la terre alors qu'il n'y avait pas de vie." |
| 1:148 | Raël | B | "Ils ont pris cette matière, ils l'ont «pétrie» comme dit la Bible, et ils l'ont «modelée » pour en faire des êtres vivants." |
| 1:149 | Raël | B | "Chaque être vivant présent sur terre actuellement a été créé par les Elohim à partir d'une «brique » de base" |
| 1:152 | Raël | H | "Ceux qui ont fait le plan de ces maisons [...] Ce type de maison supérieur c'est l'homme" |
| 1:153 | Raël | B | "le vivant a été créé capable de se situer dans son environnement" |
| 1:171 | Raël | H | "Il a été programmé pour cela, il obéit ainsi à son code génétique" |
| 2:18 | Raël | H | "aux premiers hommes terrestres qu'ils avaient fabriqués" |
| 2:19 | Raël | H | "ces créatures fabriquées en laboratoire." |
| 2:20 | Raël | H | "la création d'êtres artificiels par d'autres Elohim" |
| 2:21 | Raël | B | "Lucifer est l'un des Elohim qui a créé la vie sur Terre et les hommes donc." |
| 2:22 | Raël | H | "étudiant les réactions des premiers hommes synthétisés" |
| 2:25 | Raël | H | "que les êtres qui ont été créés soient totalement détruits" |
| 2:26 | Raël | B | "détruire totalement la vie qui a été créée sur la Terre" |
| 2:27 | Raël | B | "quelques hommes et certaines espèces animales dont l'on conserve le code génétique afin de les recréer après le cataclysme." |
| 2:28 | Raël | B | "de la même manière qu'ils ont créé les hommes, en laboratoire [...] réimplanter sur Terre les formes de vie qui ont été préservées dans «l'arche »." |
| 2:59 | "Satan", reported | H | "des êtres qui sont le fruit d'une expérience ratée." |
| 2:202 | "Yahvé" message | H | "comprendront que nous sommes leurs créateurs." |
| 2:208 | "Yahvé" message | H | "depuis la création en laboratoire du premier homme par les Elohim." |
| 2:210 | "Yahvé" message | H | "depuis le commencement, depuis la création" |
| 2:233 | "Yahvé" message | H | "A ces hommes que nous avons créés" |
| 3:28 | Raël | H | "l'extraordinaire acte d'amour qu'ils ont accompli en nous donnant la vie" |
| 3:29 | Raël | H | "ceux à qui nous devons d'exister" |
| 3:30 | Raël | H | "ceux qui les avaient créés capables de comprendre" |
| 4:25 | M. Terrusse | B | "La vie sur terre n'est pas le fruit du hasard et de la nécessité, mais le résultat d'une intervention extérieure, de l'intervention des Elohim, nos créateurs." |
| 4:34 | M. Terrusse | B | "ainsi que l'ensemble de leur création" |
| 4:35 | M. Terrusse | N | "couvert de forêts habitées par tous les animaux de la création" |
| 4:54 | M. Terrusse | N | "Toutes les espèces vivantes ne furent pas recréées après le déluge" |
| 4:87 | V. Le Gendre | B | "ont créé la vie en laboratoire, y compris notre humanité, à partir de produits chimiques inertes associés à l'A.D.N." |
| 4:93 | V. Le Gendre | H | "quand ils ont créé les hommes" |
| 4:127 | M. Terrusse | B | "la venue des Elohim sur la Terre, et la création scientifique de la vie dans des laboratoires" |
| 4:197 | J.-B. Ndjoga-Awirondjogo | H | "l'homme n'est pas le fruit d'un hasard, mais la création en science et sagesse de Quelqu'un qui l'a fait à Son Image et à Sa Ressemblance !" |

### Passages classed `rejected_view` (LWTE only)

| refId | Voice | French sentence |
|---|---|---|
| 1:135 | Raël | "L'école leur enseignera que l'homme descend du singe, qu'importe, il faut respecter l'enseignement de l'école car c'est une tradition" |
| 1:196 | Raël | "tous ceux, scientifiques ou non, qui attribuent l'origine de la vie sur terre et donc de l'homme à une succession de hasards ayant opéré tout au long de ce qu'ils appellent l'évolution. [...] tous ceux qui croient que nous descendons du singe par la suite d'une lente évolution due au hasard croient que la merveilleuse horloge que nous sommes s'est faite toute seule, par hasard." |
| 3:38 | Raël | "ces scientifiques qui disent que nous descendons du singe, mais font baptiser leurs enfants" |
| 4:2 | M. Terrusse | "La plupart des gens ont appris l'évolution à l'école. [...] «[...] Nous avons répété, machinalement, que la vie évolue, que les êtres se transforment les uns dans les autres. »" (quoting Jean Rostand) |
| 4:4 | M. Terrusse | "Lorsque des savants, des professeurs et des ecclésiastiques bien en vue affirment que l'évolution est un fait" |
| 4:6 | M. Terrusse | "«Est-il bien sûr qu'ainsi que le veulent les néo-darwiniens, le problème de l'évolution soit dès maintenant résolu ?»" (Rostand) |
| 4:7 | M. Terrusse | "« Les mutations que nous connaissons et qu'on veut rendre responsables de l'édification du monde vivant sont, en général, des privations organiques des déficiences [...]" (Rostand) |
| 4:8 | M. Terrusse | "«Non, décidément, je ne puis me résoudre à penser que ces " lapsus " de l'hérédité ont pu, même avec le concours de la sélection naturelle [...] bâtir tout le monde vivant" (Rostand) |
| 4:12 | M. Terrusse | "toute modification aléatoire provoquera inévitablement une désorganisation." |
| 4:14 | M. Terrusse | "Un accident n'apporte jamais des améliorations, mais des dégâts." |
| 4:15 | M. Terrusse | "Et le facteur temps ne change rien, ce qui était impossible hier l'est encore aujourd'hui." |
| 4:17 | M. Terrusse | "Est-il possible que ces atomes initialement disséminés aient pu spontanément se regrouper et s'assembler?" |
| 4:18 | M. Terrusse | "Non, car la matière inanimée ne cherche pas à s'améliorer" |
| 4:21 | M. Terrusse | "Il n'y a jamais un gain d'ordre sans l'intervention d'une force extérieure." |
| 4:22 | M. Terrusse | "La théorie évolutionniste est en contradiction avec la loi de l'entropie." |
| 4:23 | M. Terrusse | "l'on continue à ne pas appliquer les méthodes vraiment scientifiques pour bâtir les théories de l'évolution." |
| 4:88 | V. Le Gendre | "L'évolution par hasard, selon une succession de hasards, c'est un mythe ; au contraire, l'évolution réside d'abord dans l'esprit des créateurs" |
| 4:184 | M. Beluet | "La théorie de l'évolution selon laquelle l'homme serait le résultat d'une succession de mutations à partir de l'inorganique pour en arriver à l'organique me semblait pleine de failles" |

## Quotations

No passage was classed `undirected`. The five `ambiguous` paragraphs in full:

**ETTMTTP-2:123** (speaker: Yahweh)

> Nous souhaitons avoir notre ambassade parmi nos descendants, puisque le peuple d'Israël est composé des descendants des enfants qui naquirent des unions entre les fils d'Elohim et les filles des hommes.

Why ambiguous: the origin of a human population is given as interbreeding between Elohim and created humans. It is neither laboratory creation nor a process without them. The same statement appears at ETTMTTP-2:104 and LWTE-1:17-18, where it stands beside an explicit creation statement and was classed `designed`.

**LWTE-1:107** (speaker field: Narrator; Raël answering a question)

> Par rapport à la société humaine, notre vie est également très importante, car nous sommes l'aboutissement d'une longue lignée de survivants qui ont échappé aux épidémies, aux guerres, et qui ont fait de nous le fruit d'une longue sélection naturelle. Nous nous devons de contribuer à faire parvenir l'humanité à l'âge d'or qu'elle a grandement mérité et dans lequel elle est sur le point de pénétrer. Nous sommes les cellules de ce grand corps qu'est l'humanité, et au moment de la naissance de cette humanité, chaque cellule, chacun d'entre nous est très important et a son rôle à jouer.

Why ambiguous: in the book's own voice, present humans are called the product of natural selection (survival of epidemics and wars). No change of kind is asserted and no trait is named. This is the passage in either book that comes nearest to the `undirected` class.

**LWTE-4:11** (speaker field: Narrator; essay signed Marcel Terrusse, heading at LWTE-4:1)

> La plupart des mutations, aussi bien celles provoquées dans les laboratoires que celles qui apparaissent dans la population, produisent des détériorations de la viabilité, des maladies héréditaires et des monstruosités.

**LWTE-4:13** (same essay)

> Par des méthodes expérimentales on a produit des poules à cou nu et même sans plumes du tout, des insectes dont la couleur des yeux, les ailes, les membres postérieurs ou d'autres organes ont plus ou moins été modifiés. Mais à l'état libre aucun de ces mutants n'est avantagé.

**LWTE-4:16** (same essay)

> Les mutants restent toujours au sein de l'espèce primitive. Les innombrables mutations provoquées chez la Drosophile n'ont jamais produit autre chose que leurs ancêtres. Les mutations font varier la taille, la morphologie, la couleur des mouches, mais aucune mutation ou série de mutations n'a jamais fait apparaître un organisme vraiment nouveau.

Why ambiguous (4:11, 4:13, 4:16): they sit inside an argument against evolution, but they affirm in the essay's own voice that mutations occur "dans la population" and change size, form and colour within a species. They deny that this yields a new organism.

## Absent or ambiguous

- Neither book contains a statement, in its own voice, that any terrestrial species arose or became another species without the Elohim.
- ETTMTTP has no occurrence of laboratoire, singe, Darwin, mutation or spontané, and no discussion of evolution as an account of origins. Its "évolution/évolué" hits concern individuals, couples and civilisations (e.g. 2:11, 2:24, 2:28, 3:63). Its "hasard" hits (1:7, 1:17, 2:7, 3:46, 3:182) do not concern origins.
- ETTMTTP-2:34 raises "l'origine de la vie sur terre" only to answer an objection about what came "au commencement"; it does not restate how life was made beyond "seules les formes peuvent changer selon la volonté de ceux qui atteignent un niveau scientifique". Classed `designed` on that clause; the attribution is implicit.
- Which non-human organisms: the 1975 book speaks of "toute vie" and "la nature" without naming groups. The 1979 book names "végétaux ou animaux, hommes ou bêtes" (1:149), "certaines espèces animales" (2:27), "grands reptiles, dinosaures et autres sauriens" (4:54). Neither book describes a sequence or method of creating particular groups.
- Speaker metadata is unreliable for this question. Every LWTE paragraph is tagged "Narrator", though chapter 1 is question-and-answer, chapter 2 includes speech attributed to Satan (2:59-64) and a "Message de Yahvé" (2:94-233), and chapter 4 is six signed pieces by other authors (Terrusse 4:1-79 and 4:94-147; Le Gendre 4:80-93; Giroux 4:148-176; Beluet 4:177-193; Ndjoga-Awirondjogo 4:194-203; Deydier 4:204-218). In ETTMTTP chapter 3 nearly every paragraph is tagged "Yahweh", and ETTMTTP-2:74 and 2:77 are tagged "Yahweh" although they are first-person narration by Raël. Voices in the tables above are my reading of the text, not the file's field.
- The digitization has OCR faults in quoted passages ("pour eu" 3:219, "actuellement Terre" LWTE-1:15, "vingtcinq"). Quotations reproduce the file as it stands.
- The counts depend on the listing rule stated above. Bare "nos créateurs" epithets (57 substring hits for "créateurs" in ETTMTTP, 70 in LWTE) were not counted as passages.

## Adjacent observations

Change within created kinds:

- LWTE-1:149 (Raël): "Et lorsque ces espèces se reproduisent, elles ne font que «reproduire » le code génétique du premier exemplaire de leur espèce qui a été fabriqué par les Elohim." Same paragraph: "Pour des espèces différentes, l'ordre des lettres de cet alphabet serait différent, mais les lettres de l'alphabet seraient toujours les mêmes."
- LWTE-1:69 (Raël): "Ce code génétique, chaque être vivant le possède, et il diffère suivant les espèces et même selon les individus au sein d'une même espèce pour certains détails comme la couleur des yeux, des cheveux, le caractère, etc."
- LWTE-1:180 (Raël): "Le merle a toujours fait son nid de la même façon et le fera toujours ainsi. C'est dans son programme génétique et il ne peut pas le changer."
- LWTE-4:11, 4:13, 4:16 (Terrusse), quoted above: mutation varies individuals inside a species only.
- LWTE-1:107, quoted above: natural selection among human survivors.
- ETTMTTP-3:63 (tagged Yahweh): "Tout être vivant évolue et c'est bien ainsi." The context is the change of partners in a couple over a lifetime.

Selection language not about the origin of organisms:

- ETTMTTP-2:25 (Yahweh): "Ceci est, en quelque sorte, une sélection naturelle, à l'échelon cosmique, des espèces capables d'échapper à leur planète." It concerns which civilisations survive their own weapons.
- LWTE-1:65 (Raël): "Par rapport à l'infini, il est naturel qu'il y ait une sélection à tous les niveaux, aussi bien pour l'homme ou le chien dont la terre n'est qu'un atome du crâne ou de l'ongle".

Earlier and later creations, fossils, dates:

- LWTE-1:15 answers the objection from old bones by positing earlier creations: "Cela ne veut pas dire que dix ou vingt mille ans avant leur venue il n'y avait pas, sur Terre, une autre création qui fut détruite par une catastrophe naturelle ou artificielle." and "Il y a eu une infinité de créations sur notre planète et une infinité de destructions".
- LWTE-1:28 rejects radiometric dating and recommends a book titled *Evolution ou Création* ("voir bibliographie en fin d'ouvrage"); no bibliography is present in the digitized chapter files.
- Dates given: life created "il y a vingtcinq mille ans" (LWTE-1:13); "Les premiers hommes ayant été créés il y a environ treize mille ans" (LWTE-2:208).
- LWTE-4:54-55 (Terrusse): dinosaurs "ne furent pas réimplantées" after the flood; "Ceci explique la disparition brutale et simultanée de ces animaux antédiluviens..."
- LWTE-2:27-28: after the flood, animal species were recreated from preserved genetic code and reimplanted.

Creation elsewhere and by others:

- The Elohim were themselves created the same way: ETTMTTP-3:219; LWTE-1:93 ("Les Elohim ont été créés par d'autres êtres venus d'une autre planète [...] et ainsi de suite à l'infini"); LWTE-2:28.
- Life created by the Elohim on their home planet and on other planets: LWTE-2:6, 2:8, 2:10-11, 2:17 ("ont créé également la vie sur deux autres planètes"), 2:98; ETTMTTP-2:51, 2:58 ("créer des animaux toujours plus étonnants"), LWTE-2:81 (algae "que l'on avait créées et implantées artistiquement"). These concern non-terrestrial organisms and were not counted.
- Biological robots made by machine "selon le même principe" as humans: ETTMTTP-2:53-56, 2:69-77.
- Humans expected to do the same: ETTMTTP-1:4, 3:23, 3:100, 3:102; LWTE-1:24, 1:152, 2:102, 4:131 ("la création d'espèces animales nouvelles, et à terme sur la synthèse d'humanoïdes à notre image").

Other:

- LWTE-4:183 (Beluet) also sets aside divine creation: "La théorie d'une création divine ne me satisfaisait pas". It was not counted as `rejected_view` because it is not an undirected account.
- LWTE-4:88 pairs its rejection of chance evolution with the phrase "l'évolution réside d'abord dans l'esprit des créateurs", which uses "évolution" for something located in the creators' minds. The text does not explain it further.
- Raël's own conception is attributed to insemination of his mother aboard a craft (LWTE-2:85), likened to that of Jesus.
