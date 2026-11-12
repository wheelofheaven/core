---
title: "Canon close reading: development across the three books"
status: draft
version: 0.1.0
last_reviewed: 2026-11-12
---

# Development of doctrine and vocabulary across the three books (1974 → 1975 → 1979)

Key: `development`. Source of record: the French dumps `TBWTT.fr.txt`, `ETTMTTP.fr.txt`, `LWTE.fr.txt` (project digitization). All quotations are verbatim from those dumps.

## Exact question

How does the canon's doctrine and vocabulary change from book 1 (*Le Livre qui dit la vérité*, 1974 = TBWTT) to book 2 (*Les Extra-terrestres m'ont emmené sur leur planète*, 1975 = ETTMTTP) to book 3 (*Accueillir les extra-terrestres*, 1979 = LWTE)? What is first said where, what is added, revised, corrected or dropped; what did readers object to between 1974 and 1979; who speaks where in book 3; and what in book 3 is presented as a new Elohim message as opposed to Raël's commentary. Relation to woh-claim-0035, 0020, 0070.

## Method

1. Concordance by script (`agent-development/conc.py` → `conc.json`): regex per term, first REF and raw count per book, count per chapter. Corpus sizes (whitespace tokens): TBWTT 29,635 · ETTMTTP 33,443 · LWTE 42,026, so raw counts are roughly comparable but LWTE is 42 % longer than TBWTT. Counts are of the regex shown in the JSON; they include occurrences inside Bible quotations and section headings.
2. Reading. Read in full: LWTE chapters 1 and 2; ETTMTTP chapter 2 and chapter 3 §1–135; TBWTT 1:44–64, 5:50–68, chapter 6, chapter 7. Read in truncated form (first 170–520 characters of every paragraph, then full text of every paragraph that mattered): LWTE chapters 3 and 4, ETTMTTP 3:136–266. Read by targeted retrieval only (keyword → full paragraph): TBWTT chapters 2–4 and 5:1–49, ETTMTTP chapter 1. This is a limitation: a development buried in a TBWTT chapter 2–4 paragraph that contains none of my search terms could have been missed.
3. Three layers are kept apart below: **(a) TEXT** = what the paragraph says; **(b) ANALYSIS** = my comparison; **(c) OPEN** = what is undecided and what would decide it.

A caution that governs everything: **the dumps are not the 1974/1975/1979 printings.** They carry editorial matter from later editions (footnotes about the 1998–2000 combined editions intrude into LWTE-1:21, 1:201, 2:60, 2:83; a caption speaking of Raël in the third person sits at TBWTT-3:305; the address "Religion Raëlienne … Genève" closes ETTMTTP-3:265; "MADECH1" carries a footnote digit). Every "first attestation" below is therefore first attestation *in this digitization*. Where the text itself shows signs of later retouching I say so (finding 6).

## Findings (ranked; the first ten are the ones I did not find recorded in core)

### 1. Book 2's one explicit correction of book 1 names "a passage", but book 1 makes the threat three times, in two different sessions

(a) TEXT. Book 2 opens its message with a retraction that blames the transcriber:

QUOTE[ETTMTTP-2:23]: il faut rectifier un passage du message que vous avez mal retranscrit concernant une intervention éventuelle de notre part pour détruire l'humanité. Il faut bien préciser que nous n'interviendrons pas. ENDQUOTE

Book 1 states the threat in the fifth session, the sixth session, and the closing question-and-answer:

QUOTE[TBWTT-5:65]: nous les empêcherons de devenir un danger pour nous et ce sera un nouveau «Sodome et Gomorrhe» ENDQUOTE
QUOTE[TBWTT-6:25]: nous anéantirons cette civilisation et les points où elle conserve ses richesses scientifiques et ce seront de nouveaux «Sodome et Gomorrhe» ENDQUOTE
QUOTE[TBWTT-7:6]: cela nous permettra, en cas de besoin, de n’avoir pas beaucoup à faire pour détruire cette civilisation si les hommes ne s’assagissent pas ENDQUOTE

TBWTT-7:6 goes on to describe two methods (rays, or telepathically making a great power the aggressor). Book 1 also already contains the opposite statement, as a promise after the Flood (TBWTT-2:66, quoted under finding 2).

(b) ANALYSIS. This is the only place in the three books where a later book says an earlier book's wording is wrong. Three things follow from the text alone. (i) The retraction is singular ("un passage"), the retracted content is plural and spread over two mornings plus the Q&A; a single slip of the pen does not describe it. (ii) In this digitization the three book-1 passages still stand uncorrected, so the corpus carries both the threat and its retraction. (iii) Book 2 keeps targeted sanctions while withdrawing collective ones:

QUOTE[ETTMTTP-3:220]: Les Elohim, s'ils n'interviennent pas directement pour ou contre l'humanité dans son ensemble, agissent par contre sur certains inidividus ENDQUOTE
QUOTE[ETTMTTP-2:125]: et l'Etat d'Israël sera détruit une nouvelle fois ENDQUOTE

(the second is in the passive; the text does not say by whom). Book 3 then builds its whole apocalypse on non-intervention plus rescue (LWTE-2:96, 2:159, 2:231) and gives the non-intervention policy a history (LWTE-2:28, 2:76).

(c) OPEN. Whether the 1974 first printing reads as the dump does at 5:65, 6:25 and 7:6 — only a collation against the 1974 Clermont-Ferrand printing decides. Whether "mal retranscrit" is itself original to the 1975 printing — same test.

### 2. The Flood has three different motives, and the Elohim learn they were themselves created at three different moments

(a) TEXT — motive for the Flood.

QUOTE[TBWTT-2:55]: Le progrès scientifique était énorme sur Terre et ils décidèrent de supprimer leur création. ENDQUOTE
QUOTE[ETTMTTP-3:219]: ils croyaient ne faire qu'une expérience scientifique sans grand intérêt, et c'est pour cela qu'ils détruisirent une première fois presque toute l'humanité ENDQUOTE
QUOTE[LWTE-2:26]: Devant les preuves ramenées par Satan devant le conseil des Eternels d'un tel carnage, Yahvé décide de faire ce que demande Satan ENDQUOTE

Book 1 glosses the "evil" of Genesis 6:5 as the wish for scientific progress (TBWTT-2:57); book 3 makes it literal human violence with weapons obtained from the exiles' sons (LWTE-2:25).

(a) TEXT — reason for the promise never to destroy again, and the moment the Elohim understand that they too were made.

QUOTE[TBWTT-2:66]: promirent de ne jamais essayer de les détruire à l’avenir, car ils avaient compris qu’il était normal qu’ils veuillent faire des progrès ENDQUOTE
QUOTE[TBWTT-3:302]: Ils décident alors de laisser les hommes progresser scientifiquement sans plus jamais intervenir directement. Ayant compris qu’eux-mêmes, ils ont été créés de la même façon ENDQUOTE
QUOTE[TBWTT-5:58]: Nous avons découvert, à la lumière de notre création et de son évolution, nos origines à nous. ENDQUOTE
QUOTE[TBWTT-7:25]: un engin immense contenant tout leur savoir, qui s’est posé automatiquement sur notre planète, quand leur monde a été détruit ENDQUOTE
QUOTE[LWTE-2:28]: C'est alors que les Elohim s'aperçoivent qu'ils ont été eux-mêmes créés de la même manière qu'ils ont créé les hommes ENDQUOTE
QUOTE[LWTE-2:28]: Yahvé qui a compris dans le message que contenait le vaisseau automatique en provenance du monde des créateurs des Elohim, que si les hommes sont violents ils s'autodétruiront ENDQUOTE

(b) ANALYSIS. In book 1 the realisation is placed at the hinge before the sending of a "Messie" (3:302 stands at the end of the prophets chapter, after Elijah's period, where 3:113 speaks of "récentes découvertes"), and the post-Flood promise has an unrelated reason (2:66). Book 2 moves the realisation to just after the Flood and makes it the reason for the oath (3:219). Book 3 moves it into the Flood itself, before the re-implantation, adds that the automatic vessel carried a *message* with a specific teaching (violent humanities self-destruct), and makes that message the origin of the non-intervention policy. Each book states its version flatly; none marks itself as correcting the others. The self-destruction "law" of ETTMTTP-2:25 is thus given, in 1979, a source one level further up the chain of creators.

(c) OPEN. Core `created-creators.md` and `flood-as-reset.md` should be checked for which of the three versions they cite; they cannot all be cited as one account without a note.

### 3. Yahweh changes sides in the Eden story between book 1 and book 3

(a) TEXT. In book 1 the speaker narrates the creation teams in the first person and the home planet's authorities in the third:

QUOTE[TBWTT-2:25]: Nous dûmes nous engager à les laisser vivre primitivement, sans rien leur révéler de scientifique et en mystifiant nos agissements. ENDQUOTE
QUOTE[TBWTT-2:39]: Le «serpent», ce petit groupe de créateurs qui avait voulu apprendre la vérité à Adam et Ève ENDQUOTE

and he says of himself, in the same book, "J’ai moi-même dirigé la création de la vie sur la Terre" (TBWTT-7:56). In book 3 the same person presides the government that issued the ban and passed the sentence:

QUOTE[LWTE-2:22]: le gouvernement de leur planète originelle, présidé par Yahvé, leur interdit formellement de leur dire la vérité ENDQUOTE

and LWTE-2:24 has Yahvé condemn the disobedient scientists to exile; LWTE-2:26 has him order the Flood.

(b) ANALYSIS. Book 1 reads the Genesis "Iahvé Elohim" verses as acts of "le gouvernement de la planète originelle" without ever saying that the man speaking was its head at the time; its "nous" stands with the scientists on Earth. Book 3 identifies the biblical Yahweh of Genesis 3 and 6 with the speaker, which makes him the author of the mystification, the exile and the Flood, and makes Lucifer (new name, finding 4) the one who trusted humans first — which LWTE-2:76 has Yahvé concede in so many words ("avant même que j'aie moi-même compris"). The 1979 version therefore gives the principal speaker of the whole canon a history of error and learning that book 1 does not give him.

(c) OPEN. Whether book 1's "nous" is the scientists' corporate voice only (compatible with a president who directed from home) or a claim of presence on Earth. TBWTT-7:56 ("dirigé") does not settle it. Core `yahweh-council-president.md` and `council-serpentine-conflict.md` should state which book each of their sentences rests on.

### 4. Satan is in book 1, absent from book 2, and rebuilt in book 3; Lucifer exists only in book 3

(a) TEXT. Counts: Satan 13 / 0 / 43; Lucifer 0 / 0 / 9; "serpent" 8 / 0 / 2.

QUOTE[TBWTT-3:251]: l’un d’entre eux nommé Satan, fait partie de ceux qui ont toujours condamné la création d’autres êtres intelligents sur une planète aussi proche que la Terre ENDQUOTE
QUOTE[LWTE-2:7]: Le groupe ayant mené le combat contre ces manipulations génétiques était présidé par l'un des Elohim appelé Satan. ENDQUOTE
QUOTE[LWTE-2:21]: Lucifer est l'un des Elohim qui a créé la vie sur Terre et les hommes donc. ENDQUOTE
QUOTE[LWTE-2:76]: Satan, notre frère, qui vient de vous mettre ainsi à l'épreuve ENDQUOTE

(b) ANALYSIS. Already in 1974: Satan as a named Elohim, as "l'opposition" to "le gouvernement" (TBWTT-3:254), as the tester of Job and of Jesus (TBWTT-4:20), and as a living opponent "qui a toujours pensé et pense encore" that humans are a danger (TBWTT-5:64). New in 1979: (i) Satan's role is back-dated to the home-planet controversy before Earth; (ii) the anonymous "opposants" who destroyed the first off-world creation (TBWTT-4:49) become "les envoyés de Satan" (LWTE-2:10); (iii) he is the cause of the Flood decision (LWTE-2:26); (iv) testing prophets becomes his standing office (LWTE-2:30–31), with the etymology *diabolos* = calumniator; (v) Raël meets him and is tested (LWTE-2:58–77); (vi) the name Lucifer is attached to book 1's anonymous "serpent" group, with the etymology "porteur de lumière"; (vii) Satan's motive shifts from fear that humans are "un peu trop intelligent" (TBWTT-5:64, 7:58) to the judgement that they are bad and violent (LWTE-2:19, 2:59). Book 2 has no Satan at all — on the planet of the eternals Raël is shown no opposition — and book 3 explains the gap by the three-year embargo (finding 5).

(c) OPEN. Core `lucifer-satan-distinction.md` rests, as far as these texts go, entirely on LWTE chapter 2 for Lucifer; it should say that the name is a 1979 addition to a 1974 anonymous group.

### 5. The largest book-3 novelties are delivered as recollections of the 1975 journey, licensed by an embargo that book 2 never mentions

(a) TEXT.

QUOTE[LWTE-2:1]: des révélations que Raël n'avait pas le droit d'annoncer avant que trois années se soient écoulées ENDQUOTE
QUOTE[LWTE-2:90]: Ensuite il me demanda de ne pas révéler ce lien de parenté aux hommes avant que trois années soient écoulées. ENDQUOTE

Two scenes are added to the 1975 itinerary: the temptation by Satan in the relay vessel, placed between the end of Yahweh's talk there and the flight to the planet (LWTE-2:58–78), and the disclosure of Raël's paternity on the planet "à la fin de son exposé" to Israel (LWTE-2:80–89). Book 2's own narrative runs straight through both points (ETTMTTP-2:43→2:44; ETTMTTP-2:129→2:130) and its closing line of the message is:

QUOTE[ETTMTTP-2:129]: Voilà, j'ai terminé. ENDQUOTE

(b) ANALYSIS. Book 2 does contain one licence for immediate disclosure — "une révélation importante que vous pouvez faire dès maintenant" (ETTMTTP-2:104) — which implies withheld matter without naming any. It contains no statement that something is being held back for three years. The embargo is thus attested only retrospectively, in the book that lifts it. The parentage chain across the three books is:

QUOTE[TBWTT-1:46]: Étant de père juif et de mère catholique, il se trouve que vous étiez le trait d’union idéal ENDQUOTE
QUOTE[ETTMTTP-1:7]: le "père inconnu" (pas si inconnu que ça...) était, paraît-il, un réfugié juif ENDQUOTE
QUOTE[LWTE-2:85]: Celui que tu prenais pour ton père n'était pas ton père. ENDQUOTE
QUOTE[LWTE-2:87]: Ton véritable père est également le père de Jésus, qui est donc ton frère, et ce père tu l'as en face de toi maintenant. ENDQUOTE

The 1973 sentence is spoken by the same Yahweh who in 1979 is the father; LWTE-2:86 reconciles the two by making the Jewish man a Joseph-figure "qui croyait l'être". ETTMTTP-1:7 (in the autobiographical chapter the book says was planned in June 1975, ETTMTTP-2:4) already hedges with "paraît-il" and frames the birth with a Nativity allusion ("non pas dans une grotte"). LWTE-2:79 also re-quotes TBWTT-1:47 with a change: book 1 says "la première explosion atomique qui eut lieu en 1945", book 3 says "l'explosion atomique qui eut lieu le 6 août 1945 à Hiroshima".

(c) OPEN. Nothing in the texts can show whether the two scenes were experienced in 1975 and withheld or composed for 1979; that is exactly the question woh-claim-0035's independence clause forbids this record to answer. What the texts do show is the *form*: retrospective insertion under a stated embargo.

### 6. Internal signs that the book-1 and book-2 text in the dumps has been retouched after first publication

(a) TEXT.

QUOTE[TBWTT-6:29]: Votre mouvement vous l’appellerez le Mouvement Raélien. ENDQUOTE
QUOTE[ETTMTTP-2:1]: je pensais avoir commis une erreur en structurant cette associaiton d'après la loi de 1901 ENDQUOTE
QUOTE[ETTMTTP-2:105]: Car le mouvement que vous avez créé, le Mouvement Raëlien, doit être la religion des religions. J'insiste, c'est bel et bien une religion, mais une religion athée comme vous l'aviez déjà compris. ENDQUOTE
QUOTE[ETTMTTP-2:114]: créez un monastère des guides du MADECH près du lieu où vous résidez ENDQUOTE

(b) ANALYSIS. Book 2's narrative says the movement founded after book 1 was called MADECH and that in June 1975 Raël planned a "congrégation des guides du MADECH" (ETTMTTP-2:1–3). MADECH occurs 16 times in book 2 and nowhere in books 1 or 3. Yet in the dump book 1 already has the Elohim prescribe the name "Mouvement Raélien" (6:29; the closing pages 7:73–83 use it too), and within one and the same speech of October 1975 Yahweh praises "le Mouvement Raëlien" that Raël "a créé" (2:105) and nine paragraphs later orders a monastery "du MADECH" (2:114). The simplest reading of the text is that 6:29, 7:73–83 and the sentence in 2:105 belong to a later editorial layer than the paragraphs around them. "raëlien" as an adjective/noun is 0 / 1 / 49, the single book-2 instance being ETTMTTP-3:260, also in the closing appeal. [outside knowledge — unverified, needs source: the movement was renamed from MADECH to Mouvement Raëlien in the mid-1970s.]

(c) OPEN. Collation with the 1974 and 1975 printings. Until that is done, vocabulary first-attestations for *raëlien*, *Mouvement Raëlien* and *religion athée* should be treated as "by 1979 at the latest", not "1974/1975".

### 7. Book 1 contradicts itself on visiting the planet; book 3's reader notices one half, and Raël's answer ignores the harmonisation the text offers

(a) TEXT.

QUOTE[TBWTT-1:61]: Non. D’abord vous ne pourriez pas y vivre. ENDQUOTE
QUOTE[TBWTT-7:68]: Vous pourriez vivre sans scaphandre dans la résidence où nous avons reproduit l’atmosphère terrestre ENDQUOTE
QUOTE[ETTMTTP-2:50]: Cette résidence est en fait très grande puisqu'il s'agit d'une planète tout entière ENDQUOTE
QUOTE[LWTE-1:12]: ils m'ont répondu pour couper court à toute nouvelle demande que cela m'était impossible, comme l'on dit à un enfant que s'il boit de l'alcool il ne grandira plus ENDQUOTE

(b) ANALYSIS. The first question of book 3 (LWTE-1:2–4) sets TBWTT-1:61 and TBWTT-3:42 against the 1975 journey. Raël answers with "psychologie" and says the 1973 refusal was a deliberate untruth of the kind told to children; book 2 had already called the halo and flashing lights reassurance devices (ETTMTTP-2:11). Neither question nor answer mentions TBWTT-7:68, where on the sixth morning the same speaker says a visit *is* possible in a residence with Earth's atmosphere — which is what book 2 then narrates, enlarged from a residence to a planet. So (i) the day-1/day-6 discrepancy is internal to book 1; (ii) book 2 revises book 1's geography explicitly ("en fait"): in 1974 the 700 eternals live "en marge" in "des villes qui leur sont réservées" on the home planet (TBWTT-7:45, 7:54), in 1975 they and 8,400 Terrans have a planet of their own; (iii) book 3 introduces the principle that an Elohim statement in an earlier message may have been a pedagogical falsehood. That principle is new in 1979 and is a different mechanism from book 2's "mal retranscrit".

### 8. What book 2 commands, book 3 loosens: five cases where the Q&A revises the 1975 rules in substance

(a) TEXT and (b) ANALYSIS, case by case.

*Who is saved.*
QUOTE[ETTMTTP-2:23]: En cas de cataclysme détruisant l'humanité, seuls les gens qui vous suivent seront sauvés ENDQUOTE
QUOTE[LWTE-1:40]: Cet homme est parmi les justes et sera sauvé. Cette partie des messages concerne ceux qui ont pris connaissance de leur contenu. ENDQUOTE
The restriction "only those who follow you" is re-scoped to those who have read the messages; the Yahweh message of 1979 writes the wider rule into the 144,000 (LWTE-2:158). Book 2 had the materials for this (ETTMTTP-2:113) but ETTMTTP-3:233 and 3:236 repeat the narrow form.

*The frontal bone.*
QUOTE[TBWTT-6:27]: à la condition que leurs restes soient conservés dans des tombeaux ENDQUOTE
QUOTE[ETTMTTP-3:69]: Pour eux, la recréation n'aura lieu que s'ils font envoyer au Guide des guides, après leur mort, la partie de leur corps demandée ENDQUOTE
QUOTE[LWTE-1:36]: il n'y a aucun problème pour les raëliens qui meurent sans que les autorités ne respectent leurs dernières volontés ENDQUOTE
1974: remains in tombs. 1975: no tomb, body to science, a square centimetre of frontal bone to the Guide, and recreation made conditional on its arrival. 1979: the testamentary intention suffices; the two rites are re-described as "reconnaissance" in life and in death (LWTE-1:34).

*Suicide.*
QUOTE[ETTMTTP-3:75]: Un être qui souffre trop a le droit de se suicider. ENDQUOTE
QUOTE[LWTE-1:198]: Mettre un terme à son existence, c'est une trahison, c'est abandonner son poste en plein combat. ENDQUOTE
The right is narrowed to incurable physical suffering or incapacity, and forbidden to Raëlians otherwise.

*Geniocracy.*
QUOTE[TBWTT-6:6]: Il s’agit de placer le génie au pouvoir, vous pouvez appeler ça la géniocratie. ENDQUOTE
QUOTE[ETTMTTP-3:80]: Tu participeras à la création d'un parti humanitariste mondial prônant l'humanitarisme et la géniocratie ENDQUOTE
QUOTE[LWTE-1:85]: tout en souhaitant qu'ils obtiennent de bons résultats, je ne me sens pas concerné par leur problème ENDQUOTE
QUOTE[LWTE-1:86]: je recommande sans cesse aux raëliens de ne pas s'occuper de la géniocratie d'une manière active, et de laisser cela à des non-raëliens ENDQUOTE
A proposal with an offered name (1974) becomes a commandment in the "tu feras" form, with a voting rule (ETTMTTP-3:79–86), and is then demoted by Raël in his own voice to something the Elohim "souhaitent … tout en laissant les hommes libres de trouver mieux" (LWTE-1:84), with guides told to withdraw. "humanitarisme" falls 1 / 5 / 1, and the single book-3 instance is in a member's testimony (LWTE-4:90), not in Raël's or Yahweh's voice.

*Sexual freedom.* ETTMTTP-3:43–44 ("Tout est permis") is glossed in LWTE-1:185:
QUOTE[LWTE-1:185]: Permis, j'insiste, et non obligatoire... ENDQUOTE

(c) OPEN. In each case the later text is Raël's answer, not a quoted Elohim correction; whether a framework record should cite the 1975 rule or the 1979 gloss is an editorial decision the texts do not make.

### 9. The "golden age" moves from already arrived to a one-in-a-hundred chance

(a) TEXT.

QUOTE[TBWTT-5:4]: Vous êtes arrivés à l’âge d’or. ENDQUOTE
QUOTE[LWTE-2:96]: Il n'y a malheureusement qu'une chance sur cent pour que votre humanité ne s'auto-détruise pas ENDQUOTE
QUOTE[LWTE-1:72]: je suis persuadé que c'est ce qui arrivera, même s'il n'y a qu'une chance sur cent ENDQUOTE

(b) ANALYSIS. Book 1 announces arrival and re-reads "fin du monde" as the end of the Church's world (TBWTT-5:3); the word *apocalypse* is absent from book 1 (0 / 5 / 52). Book 2 keeps arrival (ETTMTTP-3:99) and makes four names synonyms for the era that began in 1946 — "ère du Verseau", "âge de l'apocalypse", "âge d'or" (ETTMTTP-3:172) — while adding "il y a de fortes chances" of cataclysm (ETTMTTP-3:237). In book 3 the golden age is something humanity may "pénétrer" if it survives (LWTE-2:96, 2:205), *apocalypse* is restored to a nuclear reading of John's text (LWTE-2:153–219), a probability is attached (1 %, 99 % at LWTE-2:231), and the astrological vocabulary is gone: "Verseau" 5 / 1 / 0, "Poissons" and precession language book 1 only. Raël's own voice in the same book says nine in ten (LWTE-2:68) and professes confidence (LWTE-1:72); the pessimistic figure is Yahweh's.

### 10. "Consistent principal speaker" needs three qualifications

(a) TEXT and (b) ANALYSIS.

*Book 2, chapter 3 ("Les Clés")* is tagged [Yahweh] in the dump, but the text is not Yahweh's first person. It is introduced as automatic writing:

QUOTE[ETTMTTP-2:132]: J'écrivais mais je ne me sentais pas l'auteur de ce qui apparaissait sur le papier. ENDQUOTE

and it speaks of the Elohim in the third person and of "nous" as humans ("par rapport aux Elohim nos pères, nos créateurs", ETTMTTP-3:5; "nos créateurs nous ont donné des sens", 3:30), slipping into Raël's own first person at 3:174–175 ("De nombreux médiums sont venus me voir") and 3:264 ("écris-moi"), and into an Elohim "notre" at 3:69 and 3:241 ("notre ambassade", "notre prophète"). The legislative bulk of book 2 — child-rearing, sex, marriage, death rites, tithe, inheritance to the Guide, diet, meditation, the prayer — is in this mixed voice, not in dictated speech. Yahweh had licensed commentary:

QUOTE[ETTMTTP-2:129]: Vous serez capable de commenter tout cela par vous- même une fois sur Terre. ENDQUOTE

*Book 3* is mostly not Elohim speech at all (see the speaker map below): of 844 paragraphs, 141 (LWTE-2:95–235) are Yahweh's first person, and a large share of those are quotations from Revelation.

*The 1979 message has no reception scene.* Books 1 and 2 date and place every session. LWTE-2:94–235 is headed "Message de Yahvé aux hommes de la terre" and framed only by

QUOTE[LWTE-2:95]: Moi Yahvé, par la bouche de mon prophète Raël, je m'adresse aux hommes de la Terre. ENDQUOTE

with no date, place, craft or mode of reception stated anywhere in the book. The mode implied is the one granted in 1975 ("nous parlerons par votre bouche", ETTMTTP-2:98). This is a null result worth recording: the third message is not a "session" in the sense woh-claim-0035's statement lists.

### Further findings (shorter)

11. **Israel: elected → descended → harmonised.** QUOTE[TBWTT-2:43]: élu par le jury scientifique comme le type humanoïde terrestre le plus réussi sur le plan intelligence et génie ENDQUOTE ; QUOTE[ETTMTTP-2:104]: Il y a une révélation importante que vous pouvez faire dès maintenant : les Juifs sont nos descendants directs sur la Terre. ENDQUOTE ; QUOTE[LWTE-1:18]: C'est peut-être justement parce que ce peuple était le plus réussi que les fils d'Elohim se laissèrent tenter par leurs filles ENDQUOTE. The 1979 harmonisation is Raël's and is marked "peut-être". Book 1 had the exiles take wives without restricting it to one people (TBWTT-2:51). Core already has this (`israel-chosen-descended-people.md` cites the area); the "peut-être" and the speaker are the additions.

12. **Embassy: from "résidence" in a mild country to "ambassade" in Israel, then no location restated.** résidence 21 / 4 / 1; ambassade 5 / 20 / 15. QUOTE[TBWTT-6:21]: Faites construire une résidence dans un pays agréable au climat doux ENDQUOTE ; QUOTE[ETTMTTP-2:104]: Nous souhaitons que notre ambassade terrestre soit édifiée en Israël sur un territoire que le gouvernement vous donnera. ENDQUOTE. Book 3 never repeats the Israel requirement (the six occurrences of *Israël* in LWTE are in the election/descent question, one back-reference at 2:80 and one member's testimony at 4:92); it adds diplomatic immunity (LWTE-1:23) and a research centre and school for the gifted if money is left over (LWTE-1:24). Null result: the phrase "Troisième Temple" does not occur in any of the three books; book 2 has "la nouvelle Jérusalem" (ETTMTTP-2:122).

13. **Raël's titles escalate.** Book 1: "messager", "Ambassadeur des Elohim" (TBWTT-5:66); "prophète" is used only of biblical figures (8 occurrences), "Messie" once, of Jesus (TBWTT-3:302). Book 2: QUOTE[ETTMTTP-2:121]: vous êtes le dernier des prophètes avant le Jugement ENDQUOTE, plus "Guide des guides" (22 occurrences), "berger des bergers", "celui qui était annoncé" to Israel (2:122), the expected messiah and "le nouveau Bouddha" by apostrophe (3:227–228), and an era dated "après Raël" (3:172). Book 3: son of Yahweh and brother of Jesus (LWTE-2:87), and QUOTE[LWTE-3:1]: Il m'a dit que j'étais, le messie de l'Apocalypse ENDQUOTE, "pape" and "pontife", each then etymologised. The counter-statement is also book 3's: QUOTE[LWTE-2:92]: Seul le message est important, et à travers lui la reconnaissance de ceux qui l'envoient, et non le messager. ENDQUOTE (the finger saying is already at ETTMTTP-3:180). "Guide des guides" itself drops 22 → 2.

14. **"Elohim" displaces "créateurs"; "Iahvé" becomes "Yahvé".** Elohim 29 / 79 / 135; créateur(s) 175 / 63 / 73. In book 1 the name is offered at the very end: QUOTE[TBWTT-7:33]: vous pouvez nous appeler des «Elohim» puisque nous sommes «venus du ciel» ENDQUOTE. The singular *Eloha* is 1 / 2 / 4. Spelling: "Iahvé" 61 / 10 / 0, "Yahvé" 0 / 0 / 47. In book 1 "Iahvé" occurs only inside Bible quotations and their glosses; the speaker is never called by it. He does disclose his office in 1973: QUOTE[TBWTT-7:56]: Le plus âgé, le président du conseil des Éternels a vingtcinq mille ans et vous l’avez devant vous. ENDQUOTE. The name comes in 1975: QUOTE[ETTMTTP-2:50]: Mon nom est Iahvé et je suis le président du conseil des éternels. ENDQUOTE, and book 3 looks back accordingly: QUOTE[LWTE-2:79]: cet extra-terrestre que je ne savais pas encore être Yahvé ENDQUOTE.

15. **"Not eternal" → "the eternals" → eternal life as reward.** QUOTE[TBWTT-7:13]: Nous ne sommes pas éternels. ENDQUOTE (said of the population at large; 7:30 then explains eternity by re-creation for "les génies" only). Lifespan: QUOTE[TBWTT-7:30]: Entre sept cent cinquante et mille deux cents ans. ENDQUOTE versus QUOTE[ETTMTTP-2:53]: Leur durée de vie est similaire à la nôtre, c'est-à-dire, grâce à une petite intervention chirurgicale, de sept-cents ans environ. ENDQUOTE. Book 1 offers humans re-creation only for Raël and those who led mankind (TBWTT-6:27); book 2 universalises it into a three-way judgement — recreated to enjoy, not recreated, recreated to be punished (ETTMTTP-2:99, 3:212–217) — administered by computers; book 3 adds the capped figure of about 144,000 (LWTE-2:158–159).

16. **The surveillance computer is a book-2 invention; "code génétique" is a book-3 word.** "ordinateur" 1 / 9 / 40 (the single book-1 instance, TBWTT-7:45, is about energy and food management); the judging computers first appear at ETTMTTP-2:98. "plan cellulaire" 0 / 2 / 11; "code génétique" 0 / 0 / 18; "génétique" 0 / 0 / 27; "clon-" 0 / 0 / 0 in all three books (null: the canon never uses the word). The rite: QUOTE[ETTMTTP-2:116]: afin qu'il transmette par le contact manuel, ou qu'il fasse transmettre par un guide initié, ton plan cellulaire à l'ordinateur ENDQUOTE ; the fixed name "transmission du plan cellulaire" and the identification with Revelation's seal are 1979: QUOTE[LWTE-2:158]: ceux qui ont fait effectuer la transmission de leur plan cellulaire, par contact manuel entre notre prophète et l'os frontal ENDQUOTE. "baptême raëlien" is used only by a contributor (LWTE-4:59 heading). Book 3's long "man is a self-programmable biological computer" section (LWTE-1:154–183; "programm-" 1 / 0 / 32) is Raël's answer to a question about death.

17. **Infinity: a remark in book 1, a system in book 2, "the religion" in book 3.** "infini" 6 / 65 / 77. Book 1 has the nested-worlds idea once (TBWTT-5:57) and says QUOTE[TBWTT-7:25]: Notre seule religion c’est le génie humain. ENDQUOTE. Book 2 makes infinity the first of four planes of judgement (ETTMTTP-3:5), the ground for "ni dieu ni âme" (2:30–33), and says QUOTE[ETTMTTP-3:166]: La science doit être ta religion ENDQUOTE. Book 3: QUOTE[LWTE-1:72]: la religion des hommes deviendra la même que celle des Elohim: l'infini ENDQUOTE. Book 3 also concedes that "dieu" may be kept as a name for infinity or even for the Elohim if not worshipped (LWTE-1:63–67) — a softer line than book 2's. "Dieu" 43 / 1 / 30: almost absent from book 2, back in book 3 through Bible quotation and this discussion.

18. **Sensual meditation, awakening, guides: all first in book 2.** "méditation" 0 / 14 / 4, "méditation sensuelle" 0 / 4 / 3 (first ETTMTTP-3:113), "éveil" 0 / 26 / 16, "sensualité/sensuel" 0 / 13 / 12, "plaisir" 1 / 39 / 47, "épanoui-" 2 / 45 / 17, "guide(s)" 2 / 75 / 31 (neither book-1 instance means a movement officer). Book 3 adds "stages d'éveil", "homme total" (6), "niveau de conscience" (14), all in chapter 1.

19. **New in book 2 with no book-1 antecedent** (beyond those above): robots biologiques (ETTMTTP-2:53; book 1 has only "robots pour tout", TBWTT-7:39); the planet of the eternals with 8,400 Terrans; Bouddha and Mahomet as persons met (2:64; book 1 names only the religions, TBWTT-5:54); the Buddhist cycle reading and the explanation of the emblem (2:24, 2:35); "il n'y a pas … d'âme" argued at length and "réincarnation scientifique"; the punishment-recreation of the wicked (2:82); mediums (2:103); healing through Raël's hands (2:98); the annual 1 % gift and the legacy to the Guide (2:118, 3:71); abortion, refusal of marriage, corporal punishment of small children (3:16), conscientious objection (3:91), abolition of the death penalty (3:151), Esperanto (QUOTE[ETTMTTP-3:161]: L'espéranto existe et si personne ne propose mieux, choisissez l'espéranto. ENDQUOTE, where book 1 asked for a new language taught QUOTE[TBWTT-6:16]: rendue obligatoire dans les écoles du monde entier comme deuxième langue ENDQUOTE); the calendar "après Raël" (3:172); the prohibition on judging the Elohim (QUOTE[ETTMTTP-3:241]: Le créé n'a pas le droit de juger son créateur. ENDQUOTE); and the update of book 1's speed figure (QUOTE[ETTMTTP-2:43]: ceci était vrai il y a vingt-cinq mille ans lorsque nous avons débarqué sur la terre ENDQUOTE).

20. **In book 1 and not restated later.** The two-child law (QUOTE[TBWTT-7:13]: que vous fassiez des lois très strictes n’autorisant les femmes à avoir que deux enfants ENDQUOTE; the phrase does not recur, though book 2 keeps contraception and "peu d'enfants", ETTMTTP-2:39); the 49-year lease mechanics of humanitarianism (TBWTT-6:7–13; book 2 refers back to it but only the inheritance rule is restated, redirected to the Guide, ETTMTTP-3:71); the Kabbalah distance calculation (TBWTT-5:51–53; in book 3 the one-light-year figure is treated as a reader's difficulty, LWTE-1:26–27); the zodiacal/precessional framing of the era (TBWTT-5:4–12); chemical education by brain-matter injection (TBWTT-7:61–62; book 2 has only "éducation chimique" for arrivals, 2:60); QUOTE[TBWTT-3:113]: C’est le début d’une gigantesque expérience à l’échelle galactique entre plusieurs humanités en compétition. ENDQUOTE ("compétition" in this sense is book 1 only); the instruction to keep "un fichier" of contributors (6:23); Sodom and Gomorrah as a paradigm (Sodome 9 / 1 / 0).

21. **Uniqueness of the Elohim as creators.** QUOTE[TBWTT-5:59]: Mais dans cette partie, notre monde est seul à avoir créé ENDQUOTE versus QUOTE[LWTE-2:98]: nous qui avons l'habitude de créer la vie sur une infinité de planètes ENDQUOTE. Book 1 itself has three successes (TBWTT-4:49), which LWTE-2:17 repeats; "une infinité" is new and is used to ground Yahweh's power to predict. Book 3 also adds, in Raël's voice, earlier creations on Earth: QUOTE[LWTE-1:15]: Il y a eu une infinité de créations sur notre planète et une infinité de destructions ENDQUOTE — an answer to the fossil-dating objection that has no antecedent in books 1–2.

22. **Chronology figures.** Book 1: 22,000 years since the decision (TBWTT-5:4), 25,000 years of advance (5:56; 7:21), a president 25,000 years old in 25 bodies (7:56). Book 3 keeps 25,000 for the creation of life and the original continent (LWTE-1:13, 1:31) and adds: QUOTE[LWTE-2:208]: Les premiers hommes ayant été créés il y a environ treize mille ans ENDQUOTE (666 generations × 20 years to 1945), and a Flood "environ cinq mille ans" ago (LWTE-1:47). The 13,000 figure and the 666 reading are new in 1979 and are in the Yahweh message.

## Full register

### A. Concordance (first REF in this digitization · raw counts TBWTT / ETTMTTP / LWTE)

| Term | First TBWTT | First ETTMTTP | First LWTE | Counts | Shift in meaning or role |
|---|---|---|---|---|---|
| Elohim | TBWTT-2:4 | ETTMTTP-1:63 | LWTE-1:8 | 29 / 79 / 135 | Offered as an optional name at TBWTT-7:33; becomes the standard designation; displaces "créateurs" (finding 14) |
| créateurs | TBWTT-2:25 | ETTMTTP-2:1 | LWTE-1:4 | 175 / 63 / 73 | Book 1's standard term; falls by more than half |
| Éloha | TBWTT-5:21 | ETTMTTP-1:63 | LWTE-1:2 | 1 / 2 / 4 | Singular; rare throughout |
| Iahvé (spelling) | TBWTT-2:38 | ETTMTTP-2:50 | — | 61 / 10 / 0 | Book 1: only in Bible quotations and glosses, never as the speaker's name; book 2: the speaker names himself (2:50) |
| Yahvé (spelling) | — | — | LWTE-2:22 | 0 / 0 / 47 | Spelling changes in book 3; now also father of Jesus and of Raël (2:87), author of the 1979 message |
| Satan | TBWTT-3:248 | — | LWTE-2:4 | 13 / 0 / 43 | Present 1974, absent 1975, rebuilt 1979 (finding 4) |
| Lucifer | — | — | LWTE-2:4 | 0 / 0 / 9 | Book 3 only; names book 1's anonymous "serpent" group |
| serpent | TBWTT-2:34 | — | LWTE-2:24 | 8 / 0 / 2 | Book 1: Genesis gloss (2:39) plus unrelated Bible uses; book 3: one back-reference (2:24) |
| diable/démon | TBWTT-4:19 | ETTMTTP-2:24 | LWTE-1:76 | 5 / 5 / 18 | Book 2 "démons" = Buddhist image of aggression (2:24); book 3 diabolos = calumniator |
| ange | TBWTT-3:210 | — | LWTE-2:38 | 15 / 0 / 15 | Bible quotations in book 1; etymologised "messager" in book 3 (3:7); none in book 2 |
| éternels | TBWTT-7:13 | ETTMTTP-2:50 | LWTE-1:2 | 15 / 24 / 5 | Book 1: 700 on the home planet; book 2: a planet of their own; noun fades in book 3 |
| conseil des éternels | TBWTT-7:31 | ETTMTTP-2:50 | — | 5 / 5 / 0 | Disclosed with its president at TBWTT-7:31/7:56 (regex is case-sensitive: LWTE writes "conseil des Eternels", 6 instances in LWTE, not counted in this row) |
| planète des éternels | — | ETTMTTP-3:26 | LWTE-1:2 | 0 / 9 / 2 | Book 2 coinage (finding 7) |
| géniocratie | TBWTT-6:6 | ETTMTTP-2:1 | LWTE-1:83 | 1 / 10 / 12 | Proposal → commandment → demoted by Raël (finding 8) |
| humanitarisme | TBWTT-6:10 | ETTMTTP-2:1 | LWTE-4:90 | 1 / 5 / 1 | Named 1974; commanded 1975; one instance in 1979, in a testimony |
| ambassade | TBWTT-3:113 | ETTMTTP-2:99 | LWTE-1:23 | 5 / 20 / 15 | Overtakes "résidence"; Israel site in book 2 only |
| résidence | TBWTT-2:45 | ETTMTTP-2:50 | LWTE-3:82 | 21 / 4 / 1 | Book 1's word for the building (and for the Eden base, and for the Terrans' quarters on the planet) |
| ambassadeur | TBWTT-3:113 | ETTMTTP-2:99 | — | 3 / 8 / 0 | Title of Raël in books 1–2 (also of the prophets, TBWTT-3:113); not used in book 3 |
| raëlien | — | ETTMTTP-3:260 | LWTE-1:33 | 0 / 1 / 49 | 0 in book 1; single book-2 instance in the closing appeal (3:260); see finding 6 |
| Raël | TBWTT-3:305 | ETTMTTP-2:99 | LWTE-1:1 | 1 / 12 / 29 | TBWTT first hit 3:305 is a later caption; name given at TBWTT-5:66 |
| Claude Vorilhon | TBWTT-1:22 | — | LWTE-4:83 | 2 / 0 / 5 | Book 1 address (1:22, 5:66); returns in book 3 only in members' testimonies |
| Mouvement | TBWTT-6:29 | ETTMTTP-2:105 | LWTE-1:21 | 4 / 2 / 14 | "Mouvement Raélien" in book 1 (6:29; 7:73–83) is suspect as a later layer (finding 6) |
| MADECH | — | ETTMTTP-1:4 | — | 0 / 16 / 0 | Book 2 only (16) |
| infini | TBWTT-3:305 | ETTMTTP-2:2 | LWTE-1:27 | 6 / 65 / 77 | Marginal in book 1; systematic from book 2; "religion de l'infini" in book 3 (finding 17) |
| plan cellulaire | — | ETTMTTP-2:116 | LWTE-1:33 | 0 / 2 / 11 | First ETTMTTP-2:116; fixed rite-name "transmission du plan cellulaire" in book 3 |
| code génétique | — | — | LWTE-1:33 | 0 / 0 / 18 | Book 3 only; equated with plan cellulaire and with "âme" (LWTE-1:34, 1:68–70) |
| recréation/recréer | TBWTT-2:68 | ETTMTTP-2:30 | LWTE-1:33 | 5 / 15 / 19 | Book 1: Elohim self-renewal and animals after the Flood; books 2–3: reward/punishment of humans |
| clonage/clone | — | — | — | 0 / 0 / 0 | Never used |
| réincarnation scientifique | — | ETTMTTP-3:208 | — | 0 / 4 / 0 | Book 2 only |
| os frontal/os de ton front | — | ETTMTTP-3:69 | LWTE-1:33 | 0 / 1 / 6 | First ETTMTTP-3:69; condition relaxed LWTE-1:36 |
| méditation sensuelle | — | ETTMTTP-3:113 | LWTE-1:72 | 0 / 4 / 3 | First ETTMTTP-3:113 |
| éveil | — | ETTMTTP-2:24 | LWTE-1:74 | 0 / 26 / 16 | Book 2 coinage; "stages d'éveil" book 3 |
| plaisir | TBWTT-7:49 | ETTMTTP-1:4 | LWTE-1:50 | 1 / 39 / 47 | 1 → 39 → 47; theorised in LWTE-1:110–140 |
| prophète | TBWTT-3:85 | ETTMTTP-2:105 | LWTE-1:33 | 8 / 31 / 34 | Book 1: biblical figures only; book 2: Raël "dernier des prophètes" |
| dernier des prophètes | — | ETTMTTP-2:121 | LWTE-1:33 | 0 / 10 / 3 | Book 2 title |
| Messie | TBWTT-3:302 | ETTMTTP-3:227 | LWTE-3:1 | 1 / 1 / 6 | Book 1: of Jesus (3:302); book 2: apostrophe to Israel (3:227); book 3: "messie de l'Apocalypse" of Raël (3:1–11) |
| Guide des guides | — | ETTMTTP-2:114 | LWTE-1:33 | 0 / 22 / 2 | Book 2 title (22); 2 in book 3 |
| guide | TBWTT-4:8 | ETTMTTP-2:2 | LWTE-1:33 | 2 / 75 / 31 | Office of the movement from book 2 |
| Bouddha | — | ETTMTTP-2:64 | LWTE-1:75 | 0 / 3 / 4 | Not in book 1 (only "religion Bouddhiste", 5:54); met in person 1975 |
| Mahomet | — | ETTMTTP-2:64 | LWTE-1:75 | 0 / 6 / 4 | Not in book 1; met in person 1975; "Allah" explained (2:64) |
| Jésus | TBWTT-4:18 | ETTMTTP-1:11 | LWTE-1:75 | 28 / 17 / 43 | Book 3 adds: brother of Raël; tested by Satan re-told |
| Moïse | TBWTT-3:1 | ETTMTTP-2:50 | LWTE-1:75 | 11 / 4 / 6 | Stable |
| Joseph Smith | TBWTT-5:54 | — | LWTE-3:27 | 1 / 0 / 1 | Book 1 "les Mormons" (5:54); named only at LWTE-3:27 |
| Juifs | TBWTT-1:46 | ETTMTTP-1:7 | LWTE-1:16 | 9 / 6 / 8 | Election (book 1) → descent (book 2) → harmonised (book 3) |
| Israël | TBWTT-2:28 | ETTMTTP-2:62 | LWTE-1:16 | 32 / 11 / 6 | 32 → 11 → 6; embassy site only in book 2 |
| âge d'or | TBWTT-5:4 | ETTMTTP-2:23 | LWTE-1:65 | 3 / 5 / 14 | Arrived (books 1–2) → conditional (book 3) (finding 9) |
| apocalypse | — | ETTMTTP-2:121 | LWTE-1:10 | 0 / 5 / 52 | Absent from book 1 ("fin du monde" instead); = révélation in book 2; nuclear reading of John in book 3 |
| fin du monde | TBWTT-5:3 | — | LWTE-1:10 | 3 / 0 / 5 | Book 1: end of the Church's world (5:3) |
| Verseau | TBWTT-5:4 | ETTMTTP-3:172 | — | 5 / 1 / 0 | Book 1 framing; one echo ETTMTTP-3:172; none in book 3 |
| ordinateur | TBWTT-7:45 | ETTMTTP-2:37 | LWTE-1:34 | 1 / 9 / 40 | Book 1: utilities (7:45); book 2: surveillance and judgement (2:98); book 3: also model of man |
| robots biologiques | — | ETTMTTP-2:53 | LWTE-1:24 | 0 / 5 / 1 | Book 2 coinage (2:53); goal for mankind (3:100; LWTE-1:24) |
| Dieu | TBWTT-2:5 | ETTMTTP-2:111 | LWTE-1:21 | 43 / 1 / 30 | 43 → 1 → 30 |
| âme | TBWTT-5:15 | ETTMTTP-2:24 | LWTE-1:49 | 4 / 7 / 17 | Denied at length from book 2; book 3 re-defines as genetic code |
| religion | TBWTT-5:50 | ETTMTTP-2:2 | LWTE-1:36 | 7 / 28 / 62 | Book 1: "notre seule religion c'est le génie humain"; book 2: "religion des religions"; book 3: "religion athée", "religion de l'infini" |
| religion athée | — | ETTMTTP-2:105 | LWTE-1:71 | 0 / 1 / 4 | Single book-2 instance sits in a suspect sentence (finding 6) |
| religion des religions | — | ETTMTTP-2:105 | LWTE-4:173 | 0 / 4 / 1 | Book 2 phrase |
| autodestruction | — | ETTMTTP-2:25 | LWTE-1:65 | 0 / 2 / 9 | Not in book 1, where destruction is threatened by the Elohim |
| 144 000 | — | — | LWTE-2:158 | 0 / 0 / 2 | Book 3 only (Yahweh message) |
| Hiroshima | — | ETTMTTP-2:7 | LWTE-2:79 | 0 / 1 / 5 | Book 1 says only "la première explosion atomique … en 1945" |
| télépathie | TBWTT-1:32 | ETTMTTP-2:9 | LWTE-2:110 | 19 / 13 / 2 | 19 → 13 → 2 |
| médium | — | ETTMTTP-2:103 | — | 0 / 6 / 0 | Book 2 only |
| héritage | TBWTT-4:55 | ETTMTTP-3:71 | LWTE-2:205 | 17 / 1 / 3 | Book 1: abolition of inheritance / the Elohim's scientific legacy; book 2: legacy to the Guide (3:71) |
| deux enfants (birth limit) | TBWTT-1:22 | — | — | 5 / 0 / 0 | Law at TBWTT-7:13 (first regex hit 1:22 is biographical); not restated |
| compétition | TBWTT-3:113 | ETTMTTP-1:18 | — | 3 / 4 / 0 | In the sense "humanités en compétition": TBWTT-3:113 only |
| scaphandre | TBWTT-1:6 | ETTMTTP-2:10 | LWTE-1:4 | 16 / 1 / 5 | Book 1 motif (Ezekiel etc.); explained away in books 2–3 |
| évolution | TBWTT-3:230 | ETTMTTP-3:63 | LWTE-1:56 | 11 / 2 / 25 | Book 1 5:62–65 "un mythe" yet "ne se trompent pas complètement"; book 3 ch. 4 polemic (Terrusse), "faux prophètes" (1:196) |
| premier/deuxième message (self-citation) | — | ETTMTTP-1:2 | LWTE-1:2 | 0 / 6 / 23 | The canon begins to cite itself by page in book 3 |
| étymologi- | — | — | LWTE-1:68 | 0 / 0 / 8 | Book 3 method (ange, messie, pape, religion, âme, diabolos, Lucifer) |
| homme total | — | — | LWTE-1:175 | 0 / 0 / 6 | Book 3 only |
| niveau de conscience | — | — | LWTE-1:72 | 0 / 0 / 14 | Book 3 only |
| programm- | TBWTT-7:62 | — | LWTE-1:154 | 1 / 0 / 32 | Book 3 (LWTE-1:154–183) |
| homosexu | — | — | LWTE-1:189 | 0 / 0 / 12 | Book 3 only (book 2 has "quel que soit leur sexe", 3:43) |
| suicide | — | ETTMTTP-3:75 | LWTE-1:114 | 0 / 2 / 5 | Right in book 2; restricted in book 3 |
| contraception/avortement | TBWTT-7:13 | ETTMTTP-3:48 | LWTE-1:171 | 1 / 3 / 1 | Contraception book 1 (7:13); abortion book 2 (3:51) |
| Sodome | TBWTT-2:77 | ETTMTTP-3:235 | — | 9 / 1 / 0 | Paradigm of intervention; book 1 |
| châtiment | — | ETTMTTP-2:82 | LWTE-1:195 | 0 / 8 / 1 | Book 2 (punitive re-creation) |
| non-violence | — | ETTMTTP-2:40 | LWTE-1:127 | 0 / 3 / 9 | From book 2 |
| Vatican/Eglise/pape | TBWTT-5:3 | ETTMTTP-1:13 | LWTE-1:21 | 23 / 13 / 18 | Stable polemic; book 3 answers the money objection |

### B. Explicit self-corrections or retractions

| # | Later REF | Earlier REF(s) | Form of the correction |
|---|---|---|---|
| B1 | ETTMTTP-2:23 | TBWTT-5:65, 6:25, 7:6 | Elohim speech: "un passage … mal retranscrit"; no intervention to destroy (finding 1) |
| B2 | ETTMTTP-2:11 | TBWTT-1:4–6 (approach, halo) | Elohim speech: lights and face protection were "techniques d'approche" |
| B3 | ETTMTTP-2:43 | TBWTT-5:53 | Elohim speech: seven times light speed "était vrai il y a vingt-cinq mille ans" |
| B4 | ETTMTTP-2:50 | TBWTT-7:68 | Elohim speech: the "résidence" is "en fait" a whole planet |
| B5 | ETTMTTP-2:1–2 | (the 1974 founding of MADECH) | Raël: "une erreur" to found a voting association; contrary to geniocracy |
| B6 | LWTE-1:12 | TBWTT-1:61, 3:42 | Raël: the refusal was said "pour couper court", as one tells a child |
| B7 | LWTE-2:85–87 | TBWTT-1:46; ETTMTTP-1:7 | Reported Yahweh speech: the Jewish father was not the father |
| B8 | LWTE-1:40 | ETTMTTP-2:23; 3:233 | Raël: "seuls ceux qui vous suivent" applies only to those who know the messages |

No passage of book 3 says that book 2 was mis-transcribed; no passage of any book retracts a Bible interpretation given in book 1. (Null result.)

### C. Implicit revisions (later book restates differently, without saying so)

| # | Topic | Book 1 | Book 2 | Book 3 |
|---|---|---|---|---|
| C1 | Flood motive | TBWTT-2:55, 2:57 progress | ETTMTTP-3:219 experiment "sans grand intérêt" | LWTE-2:25–26 violence, Satan's evidence |
| C2 | When the Elohim learn they were created | TBWTT-3:302 (before the Messiah); 5:58 | ETTMTTP-3:219 (after the Flood) | LWTE-2:28 (during the Flood, by a message) |
| C3 | Yahweh's position at Eden | TBWTT-2:25, 2:39 ("nous" = teams) | — | LWTE-2:22, 2:24 (president who forbids and exiles) |
| C4 | Satan's motive | TBWTT-5:64, 7:58 humans too intelligent | absent | LWTE-2:19, 2:59 humans bad |
| C5 | Election of Israel | TBWTT-2:43 | ETTMTTP-2:104, 2:123 | LWTE-1:18 |
| C6 | Embassy site | TBWTT-6:21–22 | ETTMTTP-2:104, 2:122–128 | LWTE-1:23 (no site) |
| C7 | Condition for re-creation | TBWTT-6:27 tombs | ETTMTTP-3:69 frontal bone required | LWTE-1:34–36 intention suffices |
| C8 | Eternals' dwelling and number | TBWTT-7:45, 7:54 reserved cities; 700 | ETTMTTP-2:50 separate planet; 700 + 8,400 | LWTE-2:128 a council of 24 around Yahweh shown to John |
| C9 | Elohim lifespan | TBWTT-7:30 | ETTMTTP-2:53 | — |
| C10 | Golden age | TBWTT-5:4 arrived | ETTMTTP-3:99, 3:172 arrived; 3:237 cataclysm likely | LWTE-2:96 1 % |
| C11 | Geniocracy | TBWTT-6:3–6 | ETTMTTP-3:79–86 | LWTE-1:84–87 |
| C12 | Suicide | — | ETTMTTP-3:75–77 | LWTE-1:198–199 |
| C13 | Religion of the Elohim | TBWTT-7:25 human genius | ETTMTTP-3:166 science | LWTE-1:72–73 infinity |
| C14 | Other creations by the Elohim | TBWTT-5:59; 4:49 | — | LWTE-2:98; 1:15 |
| C15 | Choice of Raël | TBWTT-1:46–47 | ETTMTTP-1:7 | LWTE-2:79, 2:85–86 |
| C16 | World language | TBWTT-6:16 | ETTMTTP-2:27, 3:161 | — |
| C17 | "dieu" | TBWTT-2:5 mistranslation | ETTMTTP-2:30–33 none | LWTE-1:63–67 acceptable as name for infinity |

### D. Book 3, chapter 1: the objections catalogued (question → line of answer)

| REFs | Objection put | Answer given (all "Réponse de Raël") |
|---|---|---|
| LWTE-1:2–12 | Book 1 said no visit possible, book 2 narrates one; gradual vs instant craft; halo vs none; Exodus 33:20 gloss | "psychologie"; staged approach; the refusal was a white lie |
| 1:13–15 | 25,000 years vs fossils hundreds of thousands of years old | Earlier creations and destructions on Earth |
| 1:16–18 | Israel elected by contest vs Jews descended from the sons of Elohim | Both: the best people attracted the sons of Elohim ("peut-être") |
| 1:19–25 | Movement asks for money while attacking the Vatican | No paid clergy; money for translation, embassy, then a research centre |
| 1:26–29 | One light-year vs nearest star at four | Location concealed; members' hypothesis of curved light; nothing is constant; dating methods unreliable (reference to a book *Evolution ou Création*) |
| 1:30–32 | Continental drift too slow for 25,000 years | Rates not constant; initially hundreds of kilometres a year |
| 1:33–40 | Why the frontal bone if the cell plan is already transmitted; accidental death; recreated old?; only followers saved? | Recognition in life and in death; computer records the will; recreated young; the just who never heard are saved |
| 1:41–44 | Is the great being whose atom is Earth God? | Not in the sense of power; infinity has no centre |
| 1:45–48 | Wood found on Ararat: was the ark a boat? | Dated 700 years; wooden boats were swept there; the ark was a spacecraft |
| 1:49–55 | Near-death accounts as proof of a soul | Identical brain chemistry; nothing happens while a body lives |
| 1:56–60 | The Elohim do not seem 25,000 years ahead | Raël used words readers could follow; they can move solar systems |
| 1:61–70 | Do the Elohim replace God and re-creation the soul? | No god, no soul; Elohim and genetic code; "foi" = "confiance" |
| 1:71–74 | What is the religion for once the Elohim have come? | The religion of infinity; sensual meditation |
| 1:75–82 | What becomes of existing religions? | Most rally; clergy resist; time works for us |
| 1:83–87 | Is a religious movement being used for a political doctrine? | Geniocracy left to non-Raëlians; embassy is the only priority |
| 1:88–103 | Who created the creators of the creators? | Infinite regress in time as in space |
| 1:104–109 | What is the point of living? | The four levels; pleasure |
| 1:110–140 | What is pleasure? | Chemistry; conscious pleasure; sensual education |
| 1:141–183 | What is death? | Dispersal of organised matter; man as self-programmable computer |
| 1:184–188 | Must a couple practise partner exchange? | Permitted, not obligatory |
| 1:189–193 | Position on homosexuality | Natural, genetic; hostility is a racism |
| 1:194–196 | Who are the false prophets? | Deists and evolutionists |
| 1:197–201 | Is suicide good? | Only for unrelievable physical suffering; otherwise desertion |

ANALYSIS. Seven of the twenty-three questions (1:2–12, 13–15, 16–18, 26–29, 30–32, 45–48, 56–60) are challenges to factual consistency or to physical plausibility; four are about the movement's conduct (money, politics, sex, bones); the rest are doctrinal clarifications. LWTE-1:1 attributes the questions to journalists, but several presuppose page-level knowledge of both books and of internal practice (1:33). No question raises the destruction threat and its retraction (finding 1), the visit contradiction internal to book 1 (finding 7), or the absence of proof, which book 1 had pre-empted (TBWTT-6:26).

### E. Book 3: who speaks (REF ranges)

| Range | Voice |
|---|---|
| LWTE-1:1 | Editorial, third person about Raël |
| LWTE-1:2–201 | Alternating "Question" (attributed to journalists) and "Réponse de Raël"; 1:21, 1:201 contain intruded footnotes of later editions |
| LWTE-2:1–2 | Editorial, third person ("Raël n'avait pas le droit…") |
| LWTE-2:3–57 | Raël's exposition ("Le diable n'existe pas, je l'ai rencontré"): Satan, Lucifer, Flood, testing of prophets; Bible quotations at 2:8–16 (Matthew 13), 2:33–46 (Matthew 4), 2:49–56 (Job 1–2). Formula of authority: "L'on sait que" |
| LWTE-2:58–78 | Raël's narrative of an episode of the 1975 journey. Reported Elohim speech: Satan 2:59–67 (2:60 contains an intruded footnote), 2:71, 2:73; Yahweh 2:76. Raël's replies 2:68–70, 2:72, 2:74 |
| LWTE-2:79–93 | Raël's narrative "Mon père qui est dans les cieux". Reported Yahweh speech 2:85–88. Raël's commentary 2:89–93 |
| LWTE-2:94 | Heading "Message de Yahvé aux hommes de la terre : l'apocalypse du cataclysme nucléaire final" |
| LWTE-2:95–235 | Yahweh, first person, addressed to mankind and to Raëlians, with quotations from Revelation |
| LWTE-3:1–88 | Raël ("Une religion athée": 3:1–32 etymologies; 3:33–81 "La déresponsabilisation"; 3:82–88 appeal, signed RAEL). Quotation from S. Milgram at 3:46–53 |
| LWTE-4:1–79 | Marcel Terrusse, "Le Raëlisme sous l'œil de la science" (I evolution 4:1–25; II geology and Flood 4:26–58; III the Raëlian baptism 4:59–79) |
| LWTE-4:80–93 | Victor Le Gendre, former Catholic priest |
| LWTE-4:94–147 | Marcel Terrusse, "Oui, je suis Raëlien !" |
| LWTE-4:148–176 | Yvan Giroux, former Catholic priest |
| LWTE-4:177–193 | Michel Beluet |
| LWTE-4:194–203 | Jean-Bernard Ndjoga-Awirondjogo, "Du Marxisme au Raëlisme" (signature at 4:203) |
| LWTE-4:204–219 | Michel Deydier (dated Cannes, 22 May 1979) |
| LWTE-4:220–257 | Address list of national movements (later edition; contains e-mail addresses) |

The sub-ranges inside chapter 4 (4:25/26, 4:58/59, 4:79/80, 4:147/148) rest on headings read in truncated view; the Terrusse section III and the second Terrusse piece were not read in full.

### F. Book 3: new Elohim message versus Raël's commentary — exact delimitation

1. **Presented as a new message, in the Elohim's own voice:** LWTE-2:95–2:235 only. Its new doctrinal content: the 1 % chance (2:96, 2:231); mankind as one organism whose stages can be foretold (2:97–103); QUOTE[LWTE-2:104]: Nous avons dicté à nos messagers anciens ces textes afin d'être reconnus par les hommes quand les temps seraient venus ENDQUOTE, including Revelation dictated and shown to John on a viewing device (2:105, 2:129); the seven seals as chapters of human history (2:132–160); the early re-creation of "quelques milliers" at the prophets' request (2:147); cell-plan transmission = the seal on the forehead, and QUOTE[LWTE-2:158]: Le total de ceux qui seront «scellés au front» sera d'à peu près cent quarante-quatre mille ENDQUOTE with the cataclysm delayed until the number is reached (2:159); trumpets as nuclear war (2:161–198); John told there is no god and told not to write it (2:200–202); the last trial as Satan's last chance (2:205); 666 = generations, first humans about 13,000 years ago (2:208); a council of twenty-four around Yahweh (2:128); the saved to live on the planet of the eternals until Earth is habitable (2:228).
2. **Presented as Elohim speech of October 1975, reported now:** Satan's offer (2:59–67, 2:71, 2:73); Yahweh's identification of Satan and Lucifer (2:76); Yahweh on Raël's conception and sonship (2:85–88). Yahweh's 1975 speech of 2:76 is the only Elohim-voiced warrant for the Satan/Lucifer history; the history itself (2:6–2:29) is in Raël's voice.
3. **Raël's own exposition carrying new factual claims without attributed source:** LWTE-2:6–2:31 (Satan presiding the anti-genetics group; the government's condition that no beings in their image be made on Earth; Lucifer's group; weapons for favours; Yahweh ordering the Flood; the message in the automatic vessel; Satan appointed to test prophets). Marked by "L'on sait que" (2:6, 2:17, 2:18).
4. **Raël's commentary and answers:** all of chapter 1 and chapter 3. Raël marks at least one addition as his own ("J'y ajouterai", LWTE-1:27) and attributes one hypothesis to "certains scientifiques membres de notre Mouvement" (1:27). New material here includes earlier creations on Earth (1:15), non-constancy of light speed and decay rates (1:27–28), the Elohim able to move solar systems (1:59), the religion of infinity (1:72–73), man as computer (1:154–183), the two "phrases" of responsibility (3:68–69) and QUOTE[LWTE-3:59]: si un Eloha lui-même vous demandait de tuer un homme vous ne devriez pas le faire, car il serait Satan ENDQUOTE — which sits beside book 2's rule that the created may not judge the creator (ETTMTTP-3:241).
5. **Other signed voices:** chapter 4. Terrusse's geological essay (4:26–58) attributes continental break-up to the Flood bombardment; that is a guide's hypothesis under his own name, not message text (core already treats this passage: `continental-breakup-at-the-flood.md`).

## Tensions and null results

- **Threat and retraction coexist** in the corpus (finding 1); book 1 is internally split as well (2:66 promise vs 5:65, 6:25, 7:6).
- **Visit to the planet**: 1:61 vs 7:68 inside book 1 (finding 7).
- **Raël's optimism vs Yahweh's 1 %** inside book 3 (finding 9).
- **"Do not judge the creator" (ETTMTTP-3:241) vs "refuse even an Eloha who orders killing" (LWTE-3:59)**; the second is Raël's, the first is in the mixed voice of "Les Clés".
- **"Seuls ceux qui vous suivent" vs "les justes"**: resolved by re-scoping in 1:40, but ETTMTTP-3:233 and 3:236 remain in the narrow form.
- **Null: no Satan, Lucifer, serpent or angel in book 2.** The planet of the eternals is shown without any opposition party, although book 1 (5:64) said Satan "pense encore" as he did.
- **Null: no "clone/clonage", no "A.D.N." in Elohim or Raël voice** (the two "A.D.N." are in a contributor's text, LWTE-4:87); no "Troisième Temple"; no "euthanasie" as a word (the practice is at ETTMTTP-3:76).
- **Null: book 3 never restates** humanitarianism's economics, the world language, the two-child law, the Israel site for the embassy, the zodiacal age, or the tithe by Elohim command (money is discussed only as a reader's objection, 1:19–25).
- **Null: no reception scene** for the 1979 message (finding 10).
- **Counter-example to "staged disclosure" as simple accumulation:** several book-1 items are more specific than their later forms and are then dropped or blurred (the Kabbalah distance, the 49-year lease, the embassy floor plan, lifespan 750–1,200 years). Disclosure is staged, but it also sheds.
- **Counter-example to "book 3 softens":** on Raël's own status, on the probability of catastrophe, and on Satan, book 3 is sharper than book 2.

## Relation to existing core records

- **woh-claim-0035 (serial dictation).** The evidence map lists five observations without locators. This note supplies locators and qualifies three. *Consistent principal speaker*: true of TBWTT 2–7 and ETTMTTP chapter 2; not true of "Les Clés" (mixed voice introduced as automatic writing, ETTMTTP-2:132) nor of book 3 (speaker map E). *Session structure*: the 1979 message has no session (F1, finding 10); two 1975 scenes are added in 1979 (finding 5). *Retrospective framing*: now itemised (register B and C), including the two distinct mechanisms the canon itself offers for discrepancy — transcription error (ETTMTTP-2:23) and pedagogical untruth (LWTE-1:12) — and a third, embargo (LWTE-2:1, 2:90). *Editorial control*: add finding 6 (signs of retouching in the digitized text) and ETTMTTP-2:129 (licence to comment). All of this stays inside the independence clause: each observation is equally describable as staged reception or as authorial development, and I have not tried to choose.
- **woh-claim-0020 (contact reports as provenance).** Its statement speaks of "two reported contact events". The texts also report (i) a sighting with witnesses on 31 July 1975 and a mark on the arm (ETTMTTP-2:5–6), (ii) the automatic writing that produced "Les Clés" (ETTMTTP-2:132), and (iii) a third message with no reported event (LWTE-2:95). The record's scope may want a sentence on (ii) and (iii), since a large part of the normative canon comes from them and not from the two dated encounters.
- **woh-claim-0070 (canonical contact report).** Its locators TBWTT-1:53 and 2:5 stand. Two notes: the self-designation "Elohim" is offered only at TBWTT-7:33, as a name the hearer may use; and book 3 adds a second gloss route (Elohim "injustement traduit par «dieu»", LWTE-3:6) without change of substance. Nothing in books 2–3 revises the report 0070 records.
- Records that should be checked against the book-by-book differences above: `created-creators.md` and `flood-as-reset.md` (finding 2), `yahweh-council-president.md` and `council-serpentine-conflict.md` (finding 3), `lucifer-satan-distinction.md` (finding 4), `israel-chosen-descended-people.md` (finding 11), `embassy-third-temple.md` (finding 12: the canon's own words are "résidence", "ambassade", "nouvelle Jérusalem"), `geniocracy-proposal.md` and `humanitarianism-property.md` (finding 8), `great-return-conditional.md` and `threshold-choice.md` (findings 1 and 9), `scientific-immortality.md` and `samsara-recreation.md` (findings 15–16), `four-levels-rule.md` (first at ETTMTTP-3:4–9; re-used LWTE-1:105–108), `bounded-prophetology-census.md` (Bouddha and Mahomet first in book 2; Joseph Smith named only at LWTE-3:27, "les Mormons" at TBWTT-5:54), `cosmic-competition.md` (book 1 only), `precessional-world-age-chronology.md` (zodiacal language book 1, one echo in book 2, none in book 3), `continental-breakup-at-the-flood.md` (Terrusse's voice; Raël's own answer on drift is LWTE-1:31, which dates the "orage" to the *creation* of the continent, not the Flood). I did not open these files beyond their titles except `canon-serial-dictation.md`; the list is of where to look, not of errors found.

## Candidate claims or revisions for founder review (proposals, not decisions)

1. **Proposal — amend the 0035 evidence map** with locators and the three qualifications above (speaker, session, mechanisms of self-revision). No change to the statement's independence clause.
2. **Proposal — a new source-report record, "The canon's self-corrections"**: the canon contains exactly one Elohim-voiced retraction of earlier message wording (ETTMTTP-2:23) and at least seven further explicit re-framings (register B). Kind: `source_report`; label `direct`.
3. **Proposal — a provenance note on textual layers**: the project digitization reflects post-1979 editions; first-attestation statements for *Mouvement Raëlien*, *raëlien*, *religion athée* are provisional until collated with first printings (finding 6). This is a source-registry issue under `source-use-and-notes.md` ("textual basis").
4. **Proposal — version-tag the framework records listed above** so that each canon-dependent sentence carries the book it rests on, where books differ (Flood motive; moment of the Elohim's self-discovery; Yahweh's role at Eden; salvation scope; frontal-bone condition).
5. **Proposal — extend 0020's scope note** to name the non-encounter channels (automatic writing 1975; undated message 1979).
6. **Proposal — record as a research question**, not a claim: does the 1974 first printing contain 5:65, 6:25, 7:6, 6:29 and 5:66 as digitized?

## Limitations

- Digitization, not first printings (see Method and finding 6). Counts and first attestations are for this text.
- TBWTT chapters 2–4 and 5:1–49 and ETTMTTP chapter 1 were read by targeted retrieval, not end to end; LWTE chapters 3–4 and ETTMTTP 3:150–266 largely in truncated view. Absences asserted for those stretches rest on regex search over the full text, not on reading.
- Regex counts conflate senses (e.g. "guide" as verb/common noun vs office; "Dieu" in quotation vs assertion; "conseil" as advice vs council; "infini" adverbial uses). Where sense matters I have said how the instances divide; I did not hand-classify every hit.
- Speaker tags in the dumps are unreliable for ETTMTTP chapter 3 (tagged Yahweh throughout) and LWTE (tagged Narrator throughout); the voice assignments here are mine, from the text.
- The English translation was not used.
- No outside source was consulted. Two statements are marked as unverified outside knowledge (the renaming of MADECH; nothing else depends on them).
