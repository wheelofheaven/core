# Finding: woh-exp-0007

- Date: 2026-11-22
- Source and edition inspected: project digitizations in `data-library/`, French base text (`paragraphs[].text`):
  - `extraterrestrials-took-me-to-their-planet/chapter-1.json` .. `chapter-3.json` (code ETTMTTP; *Les Extra-Terrestres m'ont emmené sur leur planète*, `_meta.json` publicationYear 1975; 77 + 132 + 266 paragraphs).
  - `lets-welcome-the-extraterrestrials/chapter-1.json` .. `chapter-4.json` (code LWTE; *Accueillir les Extra-Terrestres*, `_meta.json` publicationYear 1979; 201 + 235 + 88 + 312 paragraphs).
  - The LWTE digitization carries editorial footnotes dated after 1979 ("Depuis 1998 les deux premiers livres de Raël sont regroupés en un volume …", e.g. LWTE-1:21, LWTE-2:60, LWTE-2:83) and a contact list with e-mail addresses (LWTE-4:220–312), so the scanned exemplar is a later reprint, not a 1979 printing. No printed edition was compared.
- Access achieved: `project_digitization` (full French text of all seven chapter files).
- Search performed:
  - All 7 files, field `text` only. `i18n.en` was not quoted and was not used to decide any classification.
  - Protocol terms, case-insensitive, as regex: `lohim | créateur | extra-?terrestre | planète | \bmondes?\b | \bcorps\b | \bchair\b | hommes comme | biologique | \besprits?\b | \bâmes?\b | immatéri | surnaturel | dieu | origine | viennent | \bvenus\b`. Every sentence containing a hit was extracted with its refId and read (ETTMTTP: 197 paragraphs with hits; LWTE: 290). Hit counts by substring: ETTMTTP Elohim 79, créateur 64, planète 30, monde 39, corps 34, chair 6, hommes comme 1, biologique 6, esprit 50, âme 20, immatéri 1, surnaturel 1, dieu 13, origine 5, viennent 5, venus 7, extra-terrestre 1 (printed "extra- terrestre"); LWTE Elohim 135, créateur 76, extra-terrestre/extraterrestre 32, planète 87, monde 38, corps 20, chair 5, hommes comme 5, biologique 8, esprit 29, âme 19, immatéri 2, surnaturel 4, dieu 70, origine 26, viennent 18, venus 23.
  - Supplementary pass (not in the protocol, added to catch physical description and origin wording the listed terms miss): `taille, cheveux, peau, barbe, semblable(s) à, ressembl, à leur/notre/son image, cieux, venu(s) du ciel, galaxie, système solaire, année(s)-lumière, immortel, humanoïde, palpable, matériel, sang, race, ancêtres, pères, descendants, mourir, mortel`.
  - Candidate paragraphs were then read in full with their neighbours: ETTMTTP-2:9–25, 2:29–33, 2:44–55, 2:73–74, 2:98, 2:104, 2:123, 3:11, 3:179, 3:193, 3:214–219, 3:225, 3:258; LWTE-1:2–18, 1:26–27, 1:57–59, 1:63–69, 1:89–93, 1:106, 1:147, 1:195, 2:5–11, 2:18–28, 2:58–59, 2:79–105, 2:118, 2:123, 2:128, 2:147, 2:199–202, 3:5–11, 3:19–23, 4:25, 4:80–96, 4:142, 4:149–159, 4:183–198, 4:205. Paragraphs with no hit were not read in full (this includes most of ETTMTTP chapter 1 and the LWTE-4:220–312 address list).
  - Limit: classification was done at sentence/paragraph level from the hit extraction, not by a cover-to-cover continuous reading.

## Answer

**Physical nature.** In both books every passage that characterises the Elohim does so as bodily, organic, human-like beings: they have faces, skin and hair, age and die, have a stated lifespan, can be sterilised, father children with human women, need a suitable atmosphere, and are called "des hommes comme eux faits de chair et de sang" / "des hommes comme lui" / "bien palpables". I found **no** passage in either book that, in the book's own voice, presents the Elohim as spirits, non-physical or supernatural (`immaterial_or_supernatural`: 0 and 0). Supernatural or divine status appears only as a view the books reject or as a pretence the Elohim are said to have staged.

**Origin.** In both books the Elohim come from another planet ("notre planète", "la planète de nos créateurs, les Elohim", "leur planète d'origine", "leur planète originelle"). I found **no** passage giving an Earth origin or any non-planetary origin (`origin_other`: 0 and 0). Both books add that the Elohim were themselves created; LWTE specifies "en laboratoire, par des êtres venus sur leur planète d'un autre monde".

**Disagreement.** No passage contradicts another on whether the Elohim are physical or on whether they come from another planet. There are differences of wording and of detail, three of which LWTE itself raises as questions:

1. *Which planet.* ETTMTTP-3:193 names two planets ("la planète de nos créateurs, les Elohim, et la planète des éternels"); ETTMTTP-2:50 calls the residence of the eternals "une résidence se trouvant sur notre planète" and then "une planète tout entière"; ETTMTTP-3:214 and 3:216 use "la planète des éternels" and "la planète des Elohim" for the same destination; LWTE-2:22 has "conseil des Eternels gouvernant la planète des Elohim".
2. *Could a human live there.* LWTE-1:2 and 1:4 quote the first book ("L'atmosphère est très différente de la vôtre"; "il mourrait car l'atmosphère ne lui convient pas") against the 1975 visit, under the heading "Contradictions apparentes entre le premier et le deuxième message". The answer (LWTE-1:5–12) is "psychologie" and says the refusal was given "pour couper court à toute nouvelle demande"; it does not mention the atmosphere again.
3. *Distance.* LWTE-1:26 sets "un peu moins d'une année-lumière" (first book) against the nearest star at four light-years; LWTE-1:27 answers that the Elohim do not want the location known and offers a members' hypothesis.
4. *Same as men or visibly different.* LWTE says "des hommes comme eux" (2:22), "des hommes comme lui" (2:200), "hommes comme nous" (4:192, a testimony); ETTMTTP-2:46 distinguishes by sight "des hommes semblables à ceux qui vivent sur Terre et non pas des Elohim", and LWTE-2:118 describes "un petit être" with white skin and hair.
5. *Mortal or eternal.* ETTMTTP-2:53: "Ils vieillissent et meurent comme nous … sept-cents ans environ"; LWTE-1:65: "ils sont éternels"; LWTE-2:123 supplies the mechanism "vivre éternellement à travers plusieurs corps".
6. *"Tout-puissant".* LWTE-1:195 (Raël's answer) calls the Elohim "bien palpables et tout-puissants dans ce secteur de l'infini"; LWTE-4:87 (testimony of Victor Le Gendre) says "pas de dieu ou d'être surnaturel, immatériel, tout-puissant, mais bien Elohim".

### Counts per book

Unit: one refId (paragraph). A paragraph may carry more than one class. "ambiguous" is used in two senses, kept apart below: (a) *origin wording only* — the passage says "du ciel", "dans les cieux", "des étoiles", "extra-terrestre" or "venus sur la Terre" without naming a planet in that paragraph (non-terrestrial is clear, "planet" is not stated there); (b) *nature wording* — the passage grants the Elohim an attribute usually divine (eternal, all-powerful, "dieu" in a qualified sense) while still treating them as created, palpable beings. A reader who prefers to fold (a) into `origin_other_planet` can do so from the lists.

| Class | ETTMTTP (1975) | LWTE (1979) |
|---|---|---|
| `biological_physical` | 16 | 22 |
| `immaterial_or_supernatural` | 0 | 0 |
| `origin_other_planet` | 5 | 17 |
| `origin_other` | 0 | 0 |
| `ambiguous` (a) origin wording only | 5 | 20 |
| `ambiguous` (b) nature wording | 0 | 3 |
| `rejected_view` (about the Elohim) | 3 | 9 |
| `rejected_view` (god / soul / supernatural in general) | 5 | many; not exhaustively counted (see LWTE-1:41–44, 1:61–70, 2:3) |

## Quotations

Speaker is the value of the file's `speaker` field. In LWTE that field is "Narrator" for every paragraph; the voice inside the text is given in brackets where it matters.

### ETTMTTP — `biological_physical` (16)

- ETTMTTP-2:10, Narrator: "Je remarquai tout de suite une seule différence : il n'avait plus le scaphandre qui faisait, la première fois, comme un halo autour de son visage."
- ETTMTTP-2:11, Yahweh: "Vous pouvez remarquer qu'aujourd'hui je n'ai pas de protection autour du visage et que mon véhicule vous est apparu d'un seul coup et n'était pas équipé de lumières clignotantes."
- ETTMTTP-2:15, Narrator: "Enfin une dernière porte s'ouvrit et je retrouvai mon guide ; il était accompagné de deux êtres semblables à lui mais dont les traits étaient différents tout en étant aussi accueillants."
- ETTMTTP-2:32, Yahweh: "Un de nos globules rouges ou, mieux, un des atomes formant notre corps ne pourrait pas non plus imaginer qu'il forme avec ses semblables un être vivant." (The "nous" may be generic.)
- ETTMTTP-2:46, Narrator: "En arrivant dans une clairière, je découvris avec stupéfaction un groupe d'hommes semblables à moi, je veux dire des hommes semblables à ceux qui vivent sur Terre et non pas des Elohim."
- ETTMTTP-2:47, Narrator: "Il devait y avoir une quarantaine de convives semblables aux hommes de la Terre en plus de mes trois guides."
- ETTMTTP-2:53, Yahweh (of the "robots biologiques"): "Ils vieillissent et meurent comme nous, mais la machine qui les fabrique peut en produire largement plus qu'il ne nous en faut." and "Leur durée de vie est similaire à la nôtre, c'est-à-dire, grâce à une petite intervention chirurgicale, de sept-cents ans environ."
- ETTMTTP-2:55, Yahweh: "Comme les Elohim membres du conseil des éternels, les terriens éternels n'ont pas le droit d'avoir d'enfants et acceptent de subir une petite intervention qui les rend stériles, mais cette stérilité pourrait facilement être annulée."
- ETTMTTP-2:104, Yahweh: "Il y a une révélation importante que vous pouvez faire dès maintenant : les Juifs sont nos descendants directs sur la Terre." … "Ils sont les descendants des fils d'Elohim et des filles des hommes dont il est question dans la Genèse. Leur faute originelle fut de s'être unis à leur création scientifique ; c'est pour cela qu'ils ont souffert si longtemps."
- ETTMTTP-2:123, Yahweh: "Nous souhaitons avoir notre ambassade parmi nos descendants, puisque le peuple d'Israël est composé des descendants des enfants qui naquirent des unions entre les fils d'Elohim et les filles des hommes."
- ETTMTTP-3:11, Yahweh: "Une naissance doit être une fête car les Elohim nous ont créés à leur image, donc capables de nous reproduire par nous-mêmes, et en créant un être vivant nous conservons l'espèce que nous sommes et nous respectons l'oeuvre de nos créateurs."
- ETTMTTP-3:109, Yahweh: "L'homme n'a pas besoin de s'améliorer car il est parfait, car il est fait à l'image de ses créateurs."
- ETTMTTP-3:127, Yahweh: "Elohim, j'aime comme mes frères tous les êtres humains parce qu'ils sont faits à votre image,"
- ETTMTTP-3:166, Yahweh: "En étant scientifique tu plais à tes créateurs car tu agis comme eux et tu leur montres que tu es conscient d'être fait à leur image et soucieux d'exploiter toutes les possibilités qui sont les tiennes."
- ETTMTTP-3:218, Yahweh: "Vous n'étiez que matière, poussière, et les Elohim ont fait de vous des êtres vivants capables de dominer la matière, à leur image, et vous redeviendrez matière, poussière, et ils vous feront revivre, comme ils vous ont créés, scientifiquement."
- ETTMTTP-3:219, Yahweh: "Les Elohim ont créé les premiers hommes sans savoir qu'ils faisaient ce qui avait déjà été fait pour eu; ils croyaient ne faire qu'une expérience scientifique sans grand intérêt, et c'est pour cela qu'ils détruisirent une première fois presque toute l'humanité, mais lorsqu'ils comprirent qu'ils avaient été créés comme nous, ils se mirent à nous aimer comme leurs propres enfants et jurèrent de ne plus jamais essayer de nous supprimer, nous laissant surmonter par nous-mêmes notre propre violence." ("eu" sic in the file.)

(3:11, 3:109, 3:127, 3:166 and 3:218 are "à leur image" likeness statements; they are classed here because the likeness is tied to body, reproduction or matter in the passage or its neighbours. Remove them and the count is 11.)

### ETTMTTP — `origin_other_planet` (5)

- ETTMTTP-2:25, Yahweh: "Ceci est, en quelque sorte, une sélection naturelle, à l'échelon cosmique, des espèces capables d'échapper à leur planète." … "Voilà pourquoi nous ne craignons jamais les êtres qui viennent d'ailleurs pour nous contacter." (Indirect: the Elohim place themselves among planet-bound species that have left their system.)
- ETTMTTP-2:29, Yahweh: "Cela est d'ailleurs entretenu par les visiteurs venus d'autres planètes, qui n'ont que ce moyen qui soit pour visiter tranquillement des mondes qui n'ont pas encore dominé leur agressivité." … "Nous continuons d'ailleurs sur terre à faire des "apparitions" afin de voir si cela prend toujours et quelles sont les réactions des pouvoirs publics, des gouvernements et de la presse."
- ETTMTTP-2:50, Yahweh: "«Dans mon premier message je vous avais parlé d'une résidence se trouvant sur notre planète où des hommes de la Terre étaient maintenus en vie grâce au secret scientifique de l'éternité à partir d'une cellule, et parmi lesquels se trouvaient Jésus, Moïse, Elie, etc. Cette résidence est en fait très grande puisqu'il s'agit d'une planète tout entière où vivent également les membres du conseil des éternels."
- ETTMTTP-3:193, Yahweh: "… et par rapport aux étoiles qui sont autant de soleils ayant autour d'eux des planètes sur lesquelles vivent une infinité d'autres êtres, parmi lesquelles se trouve la planète de nos créateurs, les Elohim, et la planète des éternels, où tu seras un jour admis pour l'éternité ;"
- ETTMTTP-3:216, Yahweh: "Et ceux qui auront droit à la réincarntion scientifique sur la planète des Elohim vivront éternellement dans un monde où la nourriture leur sera amenée sans qu'ils aient à faire le moindre effort, …" ("réincarntion" sic.)

### ETTMTTP — `ambiguous` (a) origin wording only (5), quoted in full sentence

- ETTMTTP-1:63, Narrator: "Voilà donc en gros quels furent les événements qui précédèrent l'extraordinaire journée du 13 décembre 1973 où, dans le cratère d'un volcan d'Auvergne, le Puy-de-Lassolas, je rencontrai pour la première fois l'extra- terrestre, ou plus exactement l'Eloha (au pluriel Elohim) que je devais revoir six jours de suite au même endroit et qui, à chaque fois pendant une heure environ, me dicta Le Livre qui dit la Vérité et ses fantastiques révélations1." (The only occurrence of "extra-terrestre" in the body text of this book.)
- ETTMTTP-3:120, Yahweh: "Elohim, vous êtes là quelque part près de ces étoiles,"
- ETTMTTP-3:179, Yahweh: "Ils préfèrent croire ce que les hommes primitifs et bornés ont recopié tremblants de crainte en écoutant ceux qu'ils prenaient pour des dieux parce qu'ils venaient du ciel, plutôt que le message transmis à des êtres qui ne s'agenouillent plus bêtement devant tout ce qui vient du ciel et qui essaient de comprendre l'univers, à qui on peut s'adresser comme à des adultes." (Also `rejected_view`.)
- ETTMTTP-3:246, Yahweh: "Vous qui êtes de ces quarante-neuf mille cinq cents, et qui ressentez le besoin de rayonner et de faire quelque chose pour vos semblables, vous qui voulez rester fidèles à vos créateurs et à Jésus quand il vous disait de vous aimer les uns les autres et de respecter les Créateurs : "le père qui est dans les cieux", vous qui ressentez que ce message est véridique, venez avec nous et devenez des guides, c'est-à-dire des hommes qui se consacrent aux Elohim, dans la tradition de Moïse, d'Elie et de Jésus, et à la propagation de leurs messages, tout en menant une vie normale, c'est-à-dire en vous épanouissant pleinement, en jouissant de tous les sens que vos créateurs vous ont donnés."
- ETTMTTP-3:258, Yahweh: "Tu suivras le Guide des guides car il est l'ambassadeur des Elohim, nos créateurs, nos pères qui sont dans les cieux."

### ETTMTTP — `rejected_view`

About the Elohim (3):
- ETTMTTP-2:29, Yahweh: "Si vous arrivez prochainement à ce stade de visiteurs évolués de mondes primitifs, vous serez vous-mêmes forcés d'utiliser ce système, d'ailleurs très amusant, qui consiste à se faire passer pour des dieux à leurs yeux. Ceci est d'ailleurs extrêmement facile, car pour les primitifs, dès que l'on vient du ciel on ne peut être que divin..."
- ETTMTTP-3:179 (quoted above).
- ETTMTTP-3:225, Yahweh: "Aussi longtemps que l'homme n'était pas capable de comprendre scientifiquement l'oeuvre des Elohim, il était normal que l'homme croie en un dieu impalpable, mais maintenant que, par la science, l'homme comprend la matière, l'infiniment grand et l'infiniment petit, il n'a plus le droit de continuer à croire au dieu auquel croyaient ses ancêtres primitifs."

General (5): ETTMTTP-2:30 "il n'y a pas de dieu et évidemment pas d'âme"; 2:31 "un "bon dieu" immatériel"; 2:33 "Aucun argument cherchant à appuyer l'existence d'un quelconque dieu, ou d'une âme, ne tient debout …"; 2:80 "l'inexistence de l'âme … ou d'une entité purement spirituelle propre à chaque corps"; 2:103 "ils se mettent à croire au "surnaturel", à la magie et autres choses on ne peut plus stupides, comme la croyance à un corps éthérique".

### LWTE — `biological_physical` (22)

- LWTE-1:4 [questioner, quoting the first book]: "«Si l'homme venait sur notre planète, il y verrait les créateurs sans scaphandres, mais il mourrait car l'atmosphère ne lui convient pas. »"
- LWTE-1:14 [Raël]: "Lorsqu'ils ont décidé de poursuivre leurs expériences de création de la vie en laboratoire, ils ont recherché dans l'univers une planète possédant une atmosphère leur permettant d'y travailler."
- LWTE-1:17 [questioner, quoting ETTMTTP]: "«les Juifs sont nos descendants directs sur la Terre. C'est pour cela qu'un destin particulier leur est réservé. Ils sont les descendants des fils d'Elohim et des filles des hommes dont il est question dans la Genèse »"
- LWTE-1:18 [Raël]: "C'est peut-être justement parce que ce peuple était le plus réussi que les fils d'Elohim se laissèrent tenter par leurs filles et en eurent des enfants dont descend effectivement le peuple juif."
- LWTE-1:64 [Raël]: "… et eux, les Elohim, qui nous avaient créés à leur image."
- LWTE-1:65 [Raël]: "… puisque les Elohim sont un peu l'instrument de l'infini dans leur création d'êtres intelligents leur ressemblant." (Full sentence under `ambiguous` (b).)
- LWTE-1:106 [Raël]: "… nous sommes leurs enfants et nous nous devons de leur montrer que nous sommes fiers d'avoir eu le privilège qu'ils nous créent à leur image, c'est-à-dire capables de prendre conscience de l'infini et de créer un jour à notre tour des êtres faits à notre image."
- LWTE-1:195 [Raël]: "… des créateurs, les Elohim, qui sont eux bien palpables …" (Full sentence under `ambiguous` (b).)
- LWTE-2:6 [Raël]: "Lorsque les Elohim ont créé les premiers êtres vivants entièrement synthétiques dans les laboratoires de leur planète d'origine, une partie de la population de leur monde a protesté contre ces manipulations génétiques qu'elle pensait dangereuses pour leur civilisation."
- LWTE-2:18 [Raël]: "Mais l'on sait également que le gouvernement de la planète des Elohim permit aux scientifiques de venir sur Terre poursuivre leurs expériences à la condition qu'ils ne créent pas d'êtres à leur image."
- LWTE-2:20 [Raël]: "L'on comprend donc parfaitement que Satan n'est que l'un des Elohim, dirigeant en quelque sorte un parti politique de leur planète, parti opposé à la création d'êtres artificiels par d'autres Elohim qui, eux, pensent qu'ils peuvent créer, à leur image, des êtres positifs et non violents."
- LWTE-2:22 [Raël]: "… il décide, devant les extraordinaires aptitudes de leur création, de passer outre les directives du gouvernement de leur planète et de révéler à ces êtres qu'ils ne sont pas des «dieux» mais des hommes comme eux faits de chair et de sang et venus du ciel dans des engins volants fabriqués avec des matériaux bien palpables." and "Lucifer, le «porteur de lumière», apporte donc la lumière aux hommes en leur révélant que leurs créateurs ne sont pas des dieux mais des hommes comme eux, …"
- LWTE-2:25 [Raël]: "Ces derniers se livrent à de tendres ébats en compagnie des filles des hommes, …" ("ces derniers" = "les fils des Elohim bannis, du groupe de Lucifer".)
- LWTE-2:28 [Raël]: "C'est alors que les Elohim s'aperçoivent qu'ils ont été eux-mêmes créés de la même manière qu'ils ont créé les hommes, en laboratoire, par des êtres venus sur leur planète d'un autre monde."
- LWTE-2:85 [Yahvé, reported by Raël]: "Cette femme nous l'avons enlevée à bord d'un de nos engins et elle fut inséminée tout comme nous l'avions fait pour la mère de Jésus."
- LWTE-2:87 [Yahvé, reported]: "Ton véritable père est également le père de Jésus, qui est donc ton frère, et ce père tu l'as en face de toi maintenant."
- LWTE-2:118 [Yahvé's message, on Apocalypse I]: "Il voit sept engins volants faits d'un métal doré, «sept lampes d'or», au milieu desquelles se tient un petit être, «une sorte de fils d'homme », revêtu d'une combinaison qui le moule tout entier, même les pieds, et qui porte une grosse ceinture. Sa peau et ses cheveux sont blancs, …" and "L'être qui apparut à Jean était bien l'un d'entre nous."
- LWTE-2:123 [Yahvé's message]: "Nous lui avons expliqué que celui qui leur parlait avait connu la mort et qu'il avait été recréé, grâce au processus expliqué dans le premier message et qui nous permet de vivre éternellement à travers plusieurs corps."
- LWTE-2:200 [Yahvé's message]: "Là, nous avons clairement dit à Jean qu'il n'y avait pas de dieu, et que nous étions des hommes comme lui, …"
- LWTE-4:154 [testimony; section "La consécration de mon sacerdoce", LWTE-4:148 ff.]: "… je comprenais déjà le Père de Jésus comme étant matériellement semblable à lui, à nous …"
- LWTE-4:192 [testimony; section headed "Etre actif pour essayer de ne pas devenir radioactif", LWTE-4:177 ff.]: "Ce message émane d'hommes comme nous qui, bien qu'étant d'une autre planète, ont eu une évolution comparable à la nôtre, seulement ils ont réussi à se libérer de cette progression-destruction que nous poursuivions depuis longtemps."
- LWTE-4:197 [testimony; section "Du Marxisme au Raëlisme", signed at LWTE-4:203 Jean-Bernard Ndjoga-Awirondjogo]: "Savoir que l'homme n'est pas le fruit d'un hasard, mais la création en science et sagesse de Quelqu'un qui l'a fait à Son Image et à Sa Ressemblance !"

### LWTE — `origin_other_planet` (17)

- LWTE-1:2 [questioner, quoting the first book]: "… lorsque vous lui demandez s'il vous serait possible d'aller sur sa planète : “Non, vous ne pourriez pas y vivre. L'atmosphère est très différente de la vôtre et vous n'êtes pas assez entraîné pour supporter le voyage.”"
- LWTE-1:4 (quoted above: "notre planète").
- LWTE-1:26 [questioner]: "En page 114 du premier message il est écrit que la planète des Elohim est située à un peu moins d'une année-lumière, …"
- LWTE-1:27 [Raël]: "Les Elohim ne veulent absolument pas que nous sachions où se situe leur planète (et étant donné l'acharnement destructeur des hommes on les comprend, même si le niveau des connaissances sur Terre est encore très primitif ...)."
- LWTE-1:84 [Raël]: "… le chapitre du premier message qui expliquait quelle était l'organisation politique de la planète des Elohim, …"
- LWTE-1:93 [Raël]: "Les Elohim ont été créés par d'autres êtres venus d'une autre planète, qui eux-mêmes avaient été créés par d'autres êtres venus d'une autre planète et ainsi de suite à l'infini."
- LWTE-2:6 (quoted above: "leur planète d'origine", "la planète des Elohim").
- LWTE-2:10 [Raël]: "… la première planète choisie par les scientifiques pour aller y poursuivre leurs expériences de création de la vie en laboratoire était trop proche de leur monde, et que si les êtres créés étaient par malheur plus intelligents que leurs créateurs et s'avéraient être violents, cela serait dangereux pour la population de leur planète."
- LWTE-2:18 (quoted above: "le gouvernement de la planète des Elohim").
- LWTE-2:20 (quoted above: "un parti politique de leur planète").
- LWTE-2:22 [Raël]: "… tout cela parce que le gouvernement de leur planète originelle, présidé par Yahvé, leur interdit formellement de leur dire la vérité en les obligeant à jouer la comédie du surnaturel en permanence." and "… Yahvé, le président du conseil des Eternels gouvernant la planète des Elohim."
- LWTE-2:26 [Raël]: "… en permettant à l'équipe de Lucifer de revenir sur la planète des Elohim en les amnistiant de leur condamnation à l'exil."
- LWTE-2:28 (quoted above: "par des êtres venus sur leur planète d'un autre monde"; also "le vaisseau automatique en provenance du monde des créateurs des Elohim").
- LWTE-2:128 [Yahvé's message]: "Ce personnage, c'était moi Yahvé et j'étais entouré de vingt-quatre autres éternels représentant le conseil des Eternels gouvernant notre Planète."
- LWTE-3:20 [Raël]: "L'on peut donc lire en clair: « dont je serais le père et le personnage assurant la liaison entre la planète des créateurs et celle des hommes»."
- LWTE-3:23 [Raël]: "… une assemblée dont je serais le père et le personnage assurant la liaison entre la planète des créateurs et celle des hommes, …"
- LWTE-4:192 (quoted above: "bien qu'étant d'une autre planète").

### LWTE — `ambiguous` (a) origin wording only (20), quoted in full sentence

- LWTE-1:10 [Raël]: "Jusqu'à notre époque, nos créateurs n'apparaissaient qu'en cherchant à impressionner au maximum leurs créatures incapables de comprendre qui étaient ces êtres venus du ciel."
- LWTE-1:14 [Raël]: "Ils sont alors venus sur notre planète et ils y ont créé toutes les formes de vie que nous connaissons, y compris l'homme."
- LWTE-1:89 [questioner]: "Les Elohim nous ont créés, et d'autres extra-terrestres les ont créés eux."
- LWTE-1:147 [Raël]: "Les Elohim sont venus sur la terre alors qu'il n'y avait pas de vie."
- LWTE-1:200 [Raël]: "Les autres sont tous des messagers de nos pères qui sont dans les cieux et doivent vivre pour évangéliser, c'est-à-dire pour apporter aux autres la bonne nouvelle."
- LWTE-2:79 [Raël]: "Lors de ma première rencontre avec cet extra-terrestre que je ne savais pas encore être Yahvé, le président du conseil des Eternels, je lui demandais pourquoi m'avoir choisi moi pour être leur messager."
- LWTE-2:92 [Raël]: "Moi, Raël, je vous montre également la route à suivre, en vous transmettant les informations que m'a données mon père qui est «dans les cieux», et l'important c'est de reconnaître les Elohim comme étant nos pères et de leur préparer sur Terre l'ambassade qu'ils réclament, et non de prêter attention au messager."
- LWTE-3:6 [Raël]: "Elohim a été injustement traduit par «dieu», alors qu'il signifiait «ceux qui sont venus du ciel» en hébreu, et Apocalypse a été traduit par «fin du monde » alors qu'il signifie «révélation», tout cela nous le savons maintenant parfaitement."
- LWTE-3:10 [Raël]: "Donc «messie » signifie «choisi par dieu», et comme nous savons que le mot «dieu » n'est qu'une mauvaise traduction de Elohim signifiant «ceux qui sont venus du ciel», l'on peut donc dire que «messie» signifie en définitive «choisi par ceux qui sont venus du ciel»."
- LWTE-3:11 [Raël]: "«Il m’a dit que j'étais celui qui avait été choisi par ceux qui sont venus du ciel pour la révélation. »"
- LWTE-3:77 [Raël]: "Du fond de ma prison, je connaîtrais le bonheur de celui qui a accompli ce pour quoi il existait et qui s'aperçoit que tout continue de marcher même sans lui, espérant alors que mon père qui est dans les cieux se rendra compte que je ne suis plus très utile sur terre et me permettra de rejoindre mes frères les prophètes sur la planète des Éternels."
- LWTE-4:25 [Marcel Terrusse]: "La vie sur terre n'est pas le fruit du hasard et de la nécessité, mais le résultat d'une intervention extérieure, de l'intervention des Elohim, nos créateurs."
- LWTE-4:83 [Victor Le Gendre]: "Quand j'ai pris connaissance des messages que les extra-terrestres (Elohim) ont transmis à Claude Vorilhon «Raël», j'effectuais un voyage en Europe comme touriste."
- LWTE-4:87 [Le Gendre]: "… Dans la Bible originelle, écrite en hébreu, on parle des Elohim, signifiant littéralement «ceux qui sont venus du ciel», mot injustement traduit dans les bibles courantes par le mot Dieu; donc pas de dieu ou d'être surnaturel, immatériel, tout-puissant, mais bien Elohim présents constamment dans la Bible et qui, entre autres, ont créé la vie en laboratoire, y compris notre humanité, à partir de produits chimiques inertes associés à l'A.D.N." (Also `rejected_view`. The sentence opens "J'énumère, sans trop de commentaires, les points forts, question de brosser une synthèse de mes impressions qui mériteraient d'être plus longuement décrites : –".)
- LWTE-4:88 [Le Gendre]: "– Présence constante des Elohim ou extra-terrestres à différentes époques pour différentes civilisations: nous sommes loin de cette conception bornée disant ceci, qu' «il ne faut pas mêler la Bible avec les extra-terrestres »; …" (first item of a longer enumeration in the same paragraph).
- LWTE-4:96 [Terrusse]: "Oui, je suis raëlien, un disciple de la religion de l'infini du temps et de l'espace, un enfant de la Terre qui a retrouvé la trace de nos pères des étoiles, et qui essaie de faire prendre conscience au reste de l'humanité de cette histoire fabuleuse qu'est la nôtre."
- LWTE-4:127 [Terrusse]: "Il suffit d'ouvrir les yeux pour comprendre que cette histoire fabuleuse qu'a été la venue des Elohim sur la Terre, et la création scientifique de la vie dans des laboratoires, nous-mêmes sommes très près de la renouveler."
- LWTE-4:159 [testimony, section from LWTE-4:148]: "Là, ce soir-là, je vis et je sentis que mes années d'études n'avaient pas été inutiles ; je compris beaucoup de choses, entre autres, que j'avais, au fond, toujours été profondément «athée», mais aussi profondément religieux, c'est-à-dire attentif à la matière, amoureux de l'homme, en communication ou en contact constant par la prière, que je démystifiais de jour en jour, avec ce groupe d'extra-terrestres, nos créateurs, les Elohim."
- LWTE-4:198 [Ndjoga-Awirondjogo]: "Et dire qu'un jour l'homme de la Terre s'égalera à ses Créateurs extraterrestres !"
- LWTE-4:201 [same section]: "Il n'est pour nous guides, qui avons voulu l'épauler, que de continuer à l'aider à diffuser plus avant les messages de nos Pères célestes!"

Other paragraphs where "extra-terrestre(s)/extraterrestre(s)" occurs without a statement about the Elohim's nature or origin beyond the label, not counted: LWTE-1:7, 1:15 (hypothetical future visitors), 2:65 and 2:69 (the invasion story proposed to Raël), 4:142, 4:189, 4:191, 4:209, 4:210, 4:211, 4:212, 4:218; and in book titles inside editorial notes: LWTE-1:21, 1:201, 2:60, 2:83, 3:26.

### LWTE — `ambiguous` (b) nature wording (3), quoted in full

- LWTE-1:65 [Raël]: "Peu à peu on a attribué aux Elohim les propriétés de l'infini, ce qui est en partie vrai puisqu'ils sont éternels, et à l'infini le pouvoir de se manifester en nous envoyant des messagers célestes, nos créateurs, ce qui est également en partie vrai puisque les Elohim sont un peu l'instrument de l'infini dans leur création d'êtres intelligents leur ressemblant."
- LWTE-1:67 [Raël]: "Ceux pour qui «dieu » c'est nos créateurs, les Elohim, n'ont pas tort non plus, dans la mesure où ils n'en font pas des êtres qu'il faut vénérer à genoux ou à plat ventre, mais nos grands frères de l'infini, qu'il faut aimer comme nous souhaiterons être aimés de ceux que nous créerons un jour."
- LWTE-1:195 [Raël]: "Un concept qui mélange à la fois l'infini, effectivement impalpable dans sa totalité puisque infini dans l'espace, et éternel, mais n'ayant aucune conscience de lui-même et donc aucun pouvoir sur les hommes dans leur totalité ni individuellement, et des créateurs, les Elohim, qui sont eux bien palpables et tout-puissants dans ce secteur de l'infini, mais qui nous aiment et nous laissent évoluer librement dans notre progression scientifique et spirituelle." (Preceding sentence: "Les faux prophètes actuels, les faux révélateurs donc, ce sont tout d'abord ceux qui essaient de ramener les hommes vers des croyances primitives en un dieu immatériel, impalpable, mais tout-puissant et surveillant les hommes un par un afin de leur réserver un châtiment ou une récompense.")

None of the three says the Elohim are immaterial; each is listed because it concedes a divine-sounding attribute ("éternels", "«dieu» … n'ont pas tort non plus", "tout-puissants dans ce secteur de l'infini") in the book's own voice.

### LWTE — `rejected_view` about the Elohim (9)

- LWTE-1:63 [Raël]: "… de ceux qui cachent derrière le mot «dieu » un être à barbe blanche assis sur un nuage et qui aurait créé les hommes à son image."
- LWTE-1:76 [Raël, of future opponents]: "Ils prétexteront que les Elohim sont des usurpateurs, ou qu'ils sont envoyés par «le diable », …"
- LWTE-1:195 (preceding sentence quoted above: "un dieu immatériel, impalpable, mais tout-puissant").
- LWTE-2:18 [Raël]: "… exigeant qu'on les oblige à craindre leurs créateurs en demandant à ceux-ci de se faire passer pour des êtres surnaturels, divins en quelque sorte."
- LWTE-2:22 (quoted above: "ils ne sont pas des «dieux»"; "la comédie du surnaturel").
- LWTE-2:200 (quoted above).
- LWTE-2:202 [Yahvé's message]: "Nous lui avons clairement expliqué que lorsque le temps sera venu, les hommes comprendront qu'il n'y a pas de dieu, et comprendront que nous sommes leurs créateurs."
- LWTE-3:28 [Raël]: "Le culte n'est pas grave en soi, s'il émane de personnes qui ne divinisent pas nos créateurs, …"
- LWTE-4:87 (quoted above: "donc pas de dieu ou d'être surnaturel, immatériel, tout-puissant").

## Absent or ambiguous

- No `immaterial_or_supernatural` passage and no `origin_other` passage was found in either book within the searched scope.
- ETTMTTP gives no physical description of how an Eloha differs from an Earth human, although 2:46 and 2:47 say the difference is visible. Height, skin and hair appear only in LWTE-2:118, and there as Yahvé's gloss on the figure of Apocalypse I, not as a description of the Elohim in general.
- Neither book names a star, constellation or direction for the home planet. The only figure is the first book's "un peu moins d'une année-lumière", reported second-hand in LWTE-1:26; the first book itself was outside this brief and was not opened.
- "Planète des Elohim" and "planète des éternels" are not used consistently (see Answer, point 1). On the texts read it cannot be decided whether "notre planète" in ETTMTTP-2:50 or LWTE-2:128/2:147 means the home planet or the planet of the eternals; ETTMTTP-2:51 implies the latter is a made habitat: "comme sur terre, nous avons créé ici toute vie … ce qui nous permettra de quitter cette planète pour créer un autre "paradis" ailleurs".
- The origin of the Elohim as a species is given as creation by earlier beings (ETTMTTP-3:219; LWTE-1:93; LWTE-2:28), regressing "à l'infini" (LWTE-1:93). ETTMTTP-3:219 does not say where or by whom; LWTE-2:28 says in a laboratory, on their planet, by beings from another world. Whether "leur planète d'origine" (LWTE-2:6) is therefore the place the species was made or merely where it lived when it began its own experiments is not stated.
- LWTE-4:192 ("ont eu une évolution comparable à la nôtre") is a member's testimony, not Raël's or Yahvé's voice; "évolution" there reads as historical development, but the word is not glossed.
- The `speaker` field should be used with care: in ETTMTTP chapter 3 ("Les Clés") it is "Yahweh" throughout, although the text speaks of "les Elohim nos créateurs" in a human first person plural; in LWTE it is "Narrator" throughout, including Yahvé's dictated message (LWTE-2:94 ff.), Satan's speech (LWTE-2:59) and the members' testimonies in chapter 4.
- Typographic state of the digitization: line-break hyphens survive ("extra- terrestre", "extra- ordinaires"), footnote digits are fused to words ("révélations1", "MADECH1"), and editorial notes are spliced into running text (LWTE-2:60, 2:83). Searches for hyphenated terms must allow an optional space.

## Adjacent observations

- LWTE opens with a section titled "Contradictions apparentes entre le premier et le deuxième message" (LWTE-1:2–12) and continues with further question-and-answer items on apparent discrepancies (LWTE-1:17–18 on the descent of the Jewish people; LWTE-1:26–27 on distance). The book thus records and answers perceived disagreements itself.
- Interbreeding and paternity are stated in both books (ETTMTTP-2:104, 2:123; LWTE-1:18, 2:25), and LWTE-2:85–88 has Yahvé state that he is the biological father of both Jesus and Raël by insemination.
- ETTMTTP-2:54 separates "hommes" from "Elohim" as two groups ("obéir aux hommes et aux Elohim"; "un peu plus de neuf mille Terriens et Elohim"), while LWTE-2:22 and 2:200 call the Elohim "hommes".
- Acts that could read as supernatural are attributed to technique: ETTMTTP-2:98 "nous verrons par vos yeux, nous entendrons par vos oreilles et nous parlerons par votre bouche. Nous pourrons même guérir par vos mains - comme nous guérissons déjà à Lourdes …"; ETTMTTP-2:103 "leur don de médiumnité (qui n'est qu'un don de télépathie)"; LWTE-1:57 "ce que peuvent faire nos créateurs paraîtrait également miraculeux à nos scientifiques les plus évolués"; LWTE-1:59 "ils sont capables de modifier les trajectoires des planètes de certains systèmes solaires, et même de déplacer des systèmes solaires entiers".
- LWTE-2:7, 2:20 and 2:21 make Satan and Lucifer members of the same people ("l'un des Elohim"), with political parties and a government on their planet.
- LWTE-1:14: "Les Elohim expliquent bien qu'ils n'ont pas fabriqué notre planète."
