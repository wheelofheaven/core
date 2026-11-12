---
title: "Canon close reading: non-Genesis details against the Sendy inventory"
status: draft
version: 0.1.0
last_reviewed: 2026-11-12
---

# sendy-crosscheck — the canon's extra-Genesis primeval details against the existing Sendy inventory

Research note for wheelofheaven/core. Draft for founder review. Nothing here is a decision.

## Exact question

Of the canon's primeval-history details that are absent from Genesis but paralleled in older texts (the 37 details D01–D37 of `ancient-parallels.md`), which are already present in Jean Sendy's books of 1963–1970, according to the project's existing passage-level inventory?

## Method

1. Inputs read in full: `ancient-parallels.md` / `.json`; `core/docs/research/sendy-inventory/` (`tbwtt-inventory.json`, the five `check-*.json` and `.md`, `combined-best.json`, `BRIEF.md`); the 0072 record, evidence map, grounding report and editorial review; the five Sendy source notes and the *Les temps messianiques* note.
2. Each detail was mapped to the inventory items that cover the same TBWTT paragraphs and biblical verse. For each mapped item the five per-book records (status, locator, quote, note) were read. The `sendy_only` lists (25–29 readings per book) and every note in all 1,130 records were also searched for Mesopotamian and Enochic names and for weapons, survival, pardon, council.
3. **The Sendy texts were not available.** `core/unversioned/sendy/` is not on disk. Everything below is what the inventory *records*. A Sendy quotation here is the inventory's `quote_fr`, copied exactly, and cited as `SQ[file#item]`. A script (`agent-sendy-crosscheck/verify_sq.py`) confirms each is a substring of that record.
4. Verdict codes per detail:
   - **IN** — the same or a closely similar reading is recorded, with a quote, in at least one book.
   - **PARTIAL** — a related reading is recorded, with a material difference of agent, mechanism or direction.
   - **NOT** — an inventory item probed the point and records it absent or contrary in all five books.
   - **UNDECIDED** — no inventory item probes the point.
5. Layers: (a) what the inventory records; (b) analysis; (c) open questions and the work order.

### What the inventory can and cannot settle

- It was built from **TBWTT only** (226 items). Details that exist only in LWTE or ETTMTTP (D06 in part, D18, D19, D24, D28, D31, D32) have no item. Where a verdict is given for them it rests on a neighbouring item's quote or note.
- "Absent" was coded against the *Message's reading of a verse*. It does not mean the motif is absent from the book. The 0072 evidence map says so: "thematic parallels without the same verse were coded absent/mentioned and noted".
- Each book was coded by a separate agent; `sendy_only` was capped at about 25 readings; quotes are under about 40 words. A passage that neither matched a TBWTT search term nor made the top 25 is invisible.
- The witnesses are later digital editions. The *Ces dieux* file is a **1979 J'ai Lu reissue**; no first printing of any of the five has been collated (source notes). "In Sendy before 1974" therefore means "in the inspected witness of a work first published before 1974".
- *Les dieux nous sont nés* (1966) was never inspected. *Les temps messianiques* (1975) was read for one passage only and is not inventoried; it matters for LWTE (1979).

## Findings (ranked)

Counts over the 37 details: IN 10 · PARTIAL 11 · NOT 9 · UNDECIDED 7.
Over the 21 that `ancient-parallels` classes "shared with an older text, absent from Genesis": IN 7 (D09, D14, D15, D22, D26, D33, D35) · PARTIAL 7 (D04, D05, D10, D11, D16, D20, D37) · NOT 2 (D12, D34) · UNDECIDED 5 (D18, D19, D23, D28, D29).

### 1. Sendy cites the Epic of Gilgamesh by name for the ark's cargo (D26)

(a) The inventory records, for *Ces dieux* ch. 31:

SQ[check-ces-dieux.json#I033]: Noé n’a pas fait entrer dans son tebah un couple d’éléphants, deux puces et un raton laveur mâle et femelle ; il y a entassé ce que l’Épopée de Gilgamesh appelle « les semences de vie » ENDSQ (ch. 31 / PL33 / line 1137)

and for *L'ère du Verseau* ch. 19:

SQ[check-ere-du-verseau.json#I033]: Il en fallait de l’imagination, aux auteurs de la Tradition, pour inventer un vaisseau clos, chargé de matériel génétique ENDSQ (ch. 19 (PL36) / lines 1374, 1380–1382; ch. 20 / line 1391)

The canon:

QUOTE[TBWTT-2:58]: il suffit d’avoir une cellule vivante de chaque espèce, mâle et femelle, pour reconstituer ensuite l’être tout entier ENDQUOTE

(b) Analysis. `ancient-parallels` finding 10 found the formulation closest to the canon's in Gilgamesh XI 27 ("the seed of all living things"). The inventory shows that exact formula reaching a French reader through Sendy, attributed to Gilgamesh, attached to Noah, and used to deny that animals were loaded. For D26 the explanation E1 (French-language availability) now has a recorded carrier. This is the only place in the inventory where a Mesopotamian text is quoted for a primeval detail.

### 2. The two "resistant" items stay open — the inventory has no record for either (D29, D18)

(a) D29 (deciders discover later that life survived, TBWTT-2:74). The inventory's summary of I040 includes "realized life had not been destroyed", but none of the five check notes on I040 addresses it. D18 (weapons through the women, LWTE-2:25–27) has no item at all.

(b) Analysis. For D29 the inventory gives structural indications against in three books and leaves one open (*Les cahiers*). For D18 it gives only neighbours. Section "The two resistant items" has everything. Neither can be called absent from Sendy.

### 3. The makers fed by human produce is in Sendy — on Genesis 4, in three books (D09)

(a) Recorded:

SQ[check-cahiers.json#I027]: ils manifestent leur reconnaissance en assurant le vivre et le couvert aux Elohim ENDSQ (Cahier 2, ch. V / PL5 / line 1423)

SQ[check-ces-dieux.json#I027]: ils interdirent l’entrée d’Éden à tout bipède indigène, sauf pour leur apporter les viandes d’élevage (Abel) et les graminées, fruits et légumes (Caïn) ENDSQ (ch. 30 / PL32 / line 1102)

SQ[check-ere-du-verseau.json#I027]: les Élohim tellement adaptés à la vie terrestre qu’Abel et Caïn leur apportent le produit de l’élevage et de l’agriculture pratiqués hors d’Eden ENDSQ (ch. 17 (PL33) / line 1206)

The canon:

QUOTE[TBWTT-2:48]: poussèrent les hommes à leur amener de la nourriture ENDQUOTE

(b) Analysis. This answers one of the three questions `ancient-parallels` left open ("Do Sendy's books contain D29, D18 or D09?"): D09 yes, for the Cain-and-Abel half. The second half — Noah's post-Flood pledge "pour leur subsistance" (TBWTT-2:64) — is recorded absent: every I036 note says "no tithe" or has nothing. The 0072 evidence map does not list provisioning among its features.

### 4. The Flood's decision and aftermath in *Les cahiers* (1963) are closer to the canon than the summaries say, and the decisive passage was not transcribed (D21, D22, D23)

(a) Recorded for *Les cahiers*:

SQ[check-cahiers.json#sendy_only-S12]: NOS DIRIGEANTS (qui vivent dans les cieux) ont décidé de détruire toutes les installations théosites de la Terre ENDSQ (Cahier 2, ch. V / PL5 / line 1472)

SQ[check-cahiers.json#sendy_only-S13]: le fond des mers protège des radiations nucléaires et il savait que la seule chance de survie de Noé était de construire par conséquent un sous-marin ENDSQ (Cahier 2, ch. VI / PL5 / line 1510)

SQ[check-cahiers.json#I034]: toute pollution radioactive ayant disparu, la terre pût être enfin tenue pour « sèche » ENDSQ (Cahier 2, ch. VI / PL5 / line 1481)

The S12 reading says the Flood is "linked to a Mahabharata-style 'War of the Gods' between colonist factions".

(b) Analysis. Three elements of the canon's Flood are therefore recorded in the 1963 book: a decision by leaders who live in the heavens (D21), nuclear means with a wait for fallout to clear (D22), and factions among the visitors. The inventory does not say who "il" is — the one who knows the submarine is Noah's only chance. If "il" is a colonist acting against the leadership's decision, *Les cahiers* has D23 (the dissident warner). If "il" is the deciding authority, it has the Genesis structure. This is the single look-up with the most leverage (work order L01).

*Ces dieux* is decided the other way by its own quote: the destroyers help.

SQ[check-ces-dieux.json#I038]: Ils l’aident à construire son tebah et à y entasser matériel, documentation et semences de vie ENDSQ (ch. 34 / PL36 / line 1199)

That quote also gives D24 (helpers build the vessel; LWTE-2:27 "qu'ils aident à construire un vaisseau spatial").

### 5. Babel: intervention and destroyed equipment are in Sendy; the pardon motive is not (D33, D35, D34, D36)

(a) Recorded:

SQ[check-cahiers.json#I040]: les hommes se mettent à édifier la tour de lancement d’un astronef prématuré, dite Tour de Babel ENDSQ (Cahier 2, ch. VII / PL5 / line 1597)

SQ[check-cahiers.json#I041]: leur Tour s’effondre, entraînant dans sa chute la destruction de tout l’appareillage ENDSQ (Cahier 2, ch. VII / PL5 / line 1607)

SQ[check-la-lune.json#I041]: ils préfèrent compromettre le succès de la civilisation projetée ENDSQ (Part I ch.4 (Tour de Babel) / line 1037)

Against: for Babel *Ces dieux* says SQ[check-ces-dieux.json#I041]: aucun Céleste n’avait besoin de se déranger ENDSQ (ch. 35 / PL37 / line 1243).

The canon:

QUOTE[TBWTT-2:76]: ils détruisirent les appareillages scientifiques ENDQUOTE

(b) Analysis. `ancient-parallels` finding 9 traced ascent and demolition to Jubilees and the Sibyl. Both are in Sendy by 1963/1968, with the word "appareillage". The pardon motive (D34), the pardoned return (D36) and help from an exiled group are recorded absent in every book that treats Babel; the stated destinations are a "premature" spacecraft or the Moon. `ancient-parallels` found no ancient attestation of the pardon either. So the pardon is absent from both the older texts and the inventoried precursor.

On languages: `ancient-parallels` noted that the canon has the builders scattered to lands where language "était différent", agreeing with Genesis 10 against Genesis 11. *L'ère* draws attention to the same verse:

SQ[check-ere-du-verseau.json#I039]: Noé a une nombreuse progéniture, qui part « essaimer les nations », chacune selon sa langue, précise le chapitre X de la Genèse. ENDSQ (ch. 20 (PL38) / line 1415)

and reads the "one language" of Genesis 11 as an imposed initiatic language (note on I041). Similar, not the same.

### 6. The Eden cluster is the best-covered part: discloser, confinement and forbidden books are all recorded (D13, D14, D15) — with Satan on the opposite side from the canon's (D11, D37)

(a) Recorded:

SQ[check-cahiers.json#I021]: De son vrai nom ce Théosite anticonformiste s’appelait, comme chacun sait, M. Satan. ENDSQ (Cahier 2, ch. III / PL5 / line 1116)

SQ[check-ere-du-verseau.json#I021]: Lucifer veut porter la lumière aux hommes tout de suite. Satan veut que les hommes sachent tout, tout de suite. ENDSQ (ch. 18 (PL34) / lines 1305–1306, 1353)

SQ[check-ere-du-verseau.json#I023]: à partir d’eux-mêmes amputés de Lucifer-Satan laissé sur Terre ENDSQ (ch. 17 (PL33) / line 1212)

SQ[check-ces-dieux.json#I023]: Un humain, mutant initialement destiné à devenir Céleste, maudit et désormais condamné à rester cloué au sol ENDSQ (ch. 29 / PL31 / line 1053)

SQ[check-ces-dieux.json#I019]: le Seigneur des Célestes leur a bien dit qu’ils mourraient s’ils entraient dans ce laboratoire, s’ils « mangeaient » les livres et gravures qui s’y trouvent ENDSQ (ch. 29 / PL31 / line 1047)

SQ[check-la-lune.json#I136]: Satan, « l’ange déchu », est présenté comme « ﬁls des Elohim » dans le Livre de Job ENDSQ (Part III ch.troisième (Gen 3) / line 4907)

SQ[check-ces-dieux.json#I136]: D’un commun accord, le Seigneur et Satan choisissent un sujet d’expérience, Job ENDSQ (ch. 30 / PL32 / line 1113)

SQ[check-la-lune.json#sendy_only-S20]: l’usage de dénommer « Iahvé » leur roi héréditaire, ou leur président élu, est concevable chez les Elohim ENDSQ (Part I ch.9 (Iahvé/Carnot) / line 2085)

The canon:

QUOTE[TBWTT-3:251]: l’un d’entre eux nommé Satan, fait partie de ceux qui ont toujours condamné la création d’autres êtres intelligents ENDQUOTE
QUOTE[LWTE-2:22]: désobéissant aux ordres de Yahvé, le président du conseil des Eternels ENDQUOTE

(b) Analysis. Sendy supplies: a member of the visiting company as the "serpent", philanthropic motive, the discloser left on Earth while the others leave, Satan among the sons of the Elohim through Job, Job as an agreed experiment, and "président élu" as a possible sense of Iahvé. In every Sendy book that names him, **Satan is the pro-human discloser and is the same figure as Lucifer**. In the canon Satan heads the party hostile to man (TBWTT-3:251) and, in LWTE, Lucifer's group is the opposite party. All five I136 notes record "no opposition faction on a home planet". The canon's arrangement is not a transcription of Sendy's; it uses the same names and the same proof-text (Job 1) with the roles redistributed. `ancient-parallels` assigned D11 and D19 to common Second Temple and Qur'anic lore (E2); the inventory adds that the Job-based membership of Satan among the Elohim was in a 1968 French book.

### 7. Where an item probed the point and found the canon's detail missing or reversed (9 details)

(a) D01 home-world ban (I004: absent ×4; *Ces dieux* has scientists leaving a civilisation that "ne trouve plus à s'employer"). D03 one continent raised by explosions (I010: "no explosions, no single continent" ×4). D06 failed creations and two other seeded planets (I171: absent ×5). D08 a motive for making man (no making: natives pre-exist). D12 the makers teach the names — reversed:

SQ[check-ces-dieux.json#I020]: utilisant, à mesure, le procédé usuel des colonisateurs cherchant à apprendre la langue des indigènes ENDSQ (ch. 18 / PL20 / line 653)

D27 a couple of each race aboard (I035, I038). D30 the covenant as a promise not to destroy (I037: a bow or archive on the Moon, or a handover of documents, in all five). D34 and D36 the pardon.

(b) Analysis. Seven of these nine are details that `ancient-parallels` also found without any ancient counterpart or contradicted by the older texts (D01, D03, D06, D08, D27, D34, D36). On the present record these are in neither the older texts nor the inventoried Sendy. That is an observation about two corpora, not a finding of originality: the 1960s control corpus does not exist (0072, outstanding research 4).

### 8. Enoch, Atrahasis, Utnapishtim, Berossus: no record at all

(a) A search of every inventory file, the 0072 documents and the six source notes for Hénoch/Enoch (as a book), Veilleurs, Atrahasis, Outa-Napishtim/Utnapishtim, Ziusudra, Xisuthros, Bérose, Oannès, Enlil and Anunna returns nothing. The only "Enoch" records are the Genesis figure: Cain's city ("Hénoc-City", *Cahiers* sendy_only S11, reading field) and Enoch as "adoptive son" (*La lune* I028, note field). See section "Mesopotamian material".

(b) Analysis. This is a null result about the inventory, not about Sendy. The inventory's search terms came from TBWTT, which never names these texts.

## Full register — the 37 details

Statuses are per book in the order **Cah** (*Les cahiers de cours de Moïse*, 1963) · **Lune** (*La lune, clé de la Bible*, 1968) · **Dieux** (*Ces dieux qui firent le ciel et la terre*, 1969) · **Nous** (*Nous autres, gens du Moyen Âge*, 1969) · **Ère** (*L'ère du Verseau*, 1970): S same, s similar, m mentioned, a absent, – no item. The full per-book record (locator, quote, note) for every mapped item is in `sendy-crosscheck.json`.

| ID | Detail (short) | AP class | Items | Cah · Lune · Dieux · Nous · Ère | Verdict | What is recorded |
|---|---|---|---|---|---|---|
| D01 | Home world forbids the experiments | unique | I004 | a·a·s·a·a | NOT | No ban. *Dieux*: scientists leave on good terms. |
| D02 | Earth found; water-covered; light tested | unique | I005, I006, I007 | I006: S·S·S·S·s; I007: s·s·s·a·s | PARTIAL | Orbital survey of a cloud-wrapped Earth: same. Light = dispersing clouds, not a ray test. |
| D03 | One continent raised by explosions; later break-up | unique | I010 | m·s·s·a·s | NOT | Verse treated; no explosions, no single continent. *Cah* note mentions the America/Eurafrica fit, for Atlantis. Break-up (LWTE ch. 4): no item. |
| D04 | Teams, comparison, contests | shared | I011, I013, I016 | I016: s·a·a·m·a | PARTIAL | *Cah*: each species carries the "marque de fabrique" of the biologist who made its ancestor. No contests, artists or regional teams. *Dieux*: one team. |
| D05 | Monsters; superseded prototypes | shared | I014, I215 | I014: s·a·s·a·a; I215: s·m·s·m·m | PARTIAL | *Cah*: flawed species, prototype language. *Dieux*: laboratory trial and error, "diplodocus raté" as an image. Not attributed to rival teams. |
| D06 | Failed earlier creations; two other planets | unique | I171 | a·a·a·a·a | NOT | Matthew 13 not read this way anywhere. LWTE-2:11 not covered. |
| D07 | Man made in laboratories, in the image | genesis | I017, I018 | I017: s·s·s·s·S | PARTIAL | Literal image: yes. Manufacture: contradicted in all five (natives improved, not made). |
| D08 | Motive: makers want a being like themselves | contradicts older | I017, I018 | – | NOT | No making, so no motive. Natives are civilised, sampled, used as guards and servants. |
| D09 | Humans supply food to the makers | shared | I027, I036, I064 | I027: s·m·s·a·s; I036: s·a·m·a·m | IN | Gen 4 provisioning: three books. Noah's pledge: "no tithe". |
| D10 | Home world objects; man must be kept ignorant | shared | I004, I019, I025, I136 | I019: S·m·S·s·s | PARTIAL | Knowledge withheld, fear of parity: yes. Objection from a home world: no. |
| D11 | Satan one of the Elohim, hostile to man, licensed tester | shared | I136, I021, I162 | I136: a·s·s·a·a | PARTIAL | Member, and Job as experiment: yes. Hostile to man: no — Sendy's Satan is the discloser. |
| D12 | Makers teach the names | shared | I020 | a·s·s·a·s | NOT | Reversed: the Elohim learn the natives' words. |
| D13 | Prohibition = scientific books | genesis | I019 | S·m·S·s·s | IN | *Cah* lecture hall of science; *Dieux* "livres et gravures", on pain of death. |
| D14 | Serpent = dissident maker(s), benevolent | shared | I021, I022 | S·s·s·s·S | IN | One individual, not a group. *Dieux*: a mutant native instead. |
| D15 | Disclosers confined to Earth; others leave | shared | I023 | s·a·s·m·s | IN | *Ère*: "laissé sur Terre". *Dieux*: "cloué au sol" (a human). *Cah*: demoted to teacher. No home government. |
| D16 | Longevity technique for chiefs; not hereditary | shared | I025, I028, I030, I222 | I028: s·m·m·a·a | PARTIAL | *Cah*: tree of life = genetics lab; ages are real ages of hybrid kings, hereditary and declining. |
| D17 | Sons of Elohim = the makers; exceptional children | genesis | I029, I031 | I029: S·S·s·m·s | IN | Not exiles. Offspring are kings, "demi-dieux". |
| D18 | Weapons through the women; bloodshed as the case | shared | none | – | UNDECIDED | See "resistant items". |
| D19 | Accuser before the Council; president decides | shared | none (I136 near) | – | UNDECIDED | Components only (finding 6, finding 4). |
| D20 | Flood motive: progress (TBWTT) / violence (LWTE) | shared | I031, I032 | I032: m·m·s·a·a | PARTIAL | Progress motive: not found. Violence: *Dieux* "guerres furieuses"; *Lune* quotes Gen 6:5. |
| D21 | Decision on the distant home planet | weak | I033 | – | PARTIAL | *Cah*: leaders "qui vivent dans les cieux". Others: the departing visitors. |
| D22 | Explosions, sudden cataclysm, fallout | shared | I033, I034, I036 | I033: s·s·s·m·s | IN | *Cah*: thermonuclear scale, radioactive contamination. No missiles from afar, no tidal wave over one continent. |
| D23 | Survivor warned by dissidents against the deciders | shared | I033, I036, I038 | – | UNDECIDED | *Dieux*: destroyers help. *Cah*: open (finding 4). |
| D24 | Exiles help build the vessel | weak | I038 | I038: s·a·s·a·a | IN | *Dieux* ch. 34 (helpers are the departing Celestials). |
| D25 | Orbiting rocket; "above the earth, not on the waters" | unique, contradicted | I033, I034, I035 | I034: s·a·a·a·s; I035: a·a·a·a·m | PARTIAL | Closed vessel likened to an Apollo capsule; "DANS", not "SUR". No orbit recorded. *Cah*: submarine. |
| D26 | Cells of each species; re-creation | shared | I033, I038 | I038: s·a·s·a·a | IN | "semences de vie" (citing Gilgamesh), "matériel génétique". |
| D27 | A couple of each race aboard | unique, contradicted | I035, I038 | – | NOT | Not recorded anywhere. |
| D28 | Noah mocked | shared | none | – | UNDECIDED | ETTMTTP only. *Ère* quotes Matt 24:37 (I194) without mockery. |
| D29 | Deciders learn later that life survived | shared | I040 (summary only) | – | UNDECIDED | See "resistant items". |
| D30 | Promise never again; the reason | genesis | I037 | s·s·m·m·s | NOT | Covenant = lunar bow/archive or documents, never a promise. |
| D31 | The Elohim were themselves created | unique | none | – | UNDECIDED | Neighbours: "Le Commencement fit les Élohim"; a galactic chain of civilisations. |
| D32 | Species not restored; geology rewritten | unique | none | – | UNDECIDED | LWTE ch. 4 (Terrusse). Neighbours only. |
| D33 | Tower = vehicle to the makers' world | shared | I040 | S·S·s·a·s | IN | Launch tower. Destination the Moon; no exiled helpers. |
| D34 | Purpose: the exiles' pardon | shared | I040, I042 | – | NOT | No pardon motive in any Babel treatment. |
| D35 | Home world intervenes, scatters, destroys equipment | shared | I041, I039 | I041: s·s·s·a·m | IN | *Cah*, *Lune*: intervention, equipment lost. *Dieux*: no intervention. No scattering of the learned. |
| D36 | Exiles pardoned, return, plead | contradicts older | I042 | m·a·s·a·a | NOT | "no pardoned exiles" (*Dieux* note); nothing elsewhere. |
| D37 | Three roles: accuser, president, saving faction | shared | I136, I021 | – | PARTIAL | President title: *Lune*. Satan = Lucifer = one pro-human figure. |

Neighbour quotes referred to in the table:

SQ[check-cahiers.json#I016]: chacune de celles-ci porte en effet la marque de fabrique du biologiste théosite qui « créa » son lointain ancêtre ENDSQ (Cahier 2, ch. IV / PL5 / line 1296)
SQ[check-cahiers.json#I014]: l’existence d’espèces qui ont survécu malgré des erreurs flagrantes dans la conception de leur anatomie ENDSQ (Cahier 2, ch. VII / PL5 / line 1616)
SQ[check-ces-dieux.json#I014]: démesurés comme la bactérie et l’hippopotame successeur du diplodocus raté ENDSQ (ch. 2 / PL4 / line 124)
SQ[check-ces-dieux.json#I004]: Ces cosmonautes quittent une civilisation qui, ayant réalisé le dernier des rêves fous qui passionnent les scientifiques dignes de ce nom, ne trouve plus à s’employer ENDSQ (ch. 15 / PL17 / line 553)
SQ[check-nous-autres.json#I025]: le primitif, jusque-là serviteur soumis, ivre d’orgueil de se savoir semblable aux « dieux », risquait évidemment à tout moment de jouer avec les manettes de n’importe quoi, de faire tout sauter ENDSQ (ch. "Notre âge ingrat" (PL2) / line 161)
SQ[check-cahiers.json#I028]: Ces Géants vivront 85o ans, en moyenne. ENDSQ (Cahier 2, ch. V / PL5 / line 1455)
SQ[check-ces-dieux.json#I032]: les thèses du « serpent » triomphaient : là où les Célestes avaient projeté d’instaurer un placide bonheur bovin s’instaurait un système de guerres furieuses ENDSQ (ch. 30 / PL32 / line 1124)
SQ[check-cahiers.json#I033]: les plus récentes bombes thermonucléaires sont de l’enfantillage à côté de ce que les Théosites surent déclencher, lorsqu’ils se résolurent à abandonner notre planète ENDSQ (Cahier 2, ch. VI / PL5 / line 1482)
SQ[check-ere-du-verseau.json#I034]: il précise que Noé ne les passa pas SUR un bateau, qu’il les passa DANS une construction close ENDSQ (ch. 19 (PL36) / line 1380)
SQ[check-ere-du-verseau.json#sendy_only-S03]: sont peut-être mieux traduits par « Le Commencement fit les Élohim » ENDSQ (ch. 16 (PL31) / line 1061)
SQ[check-ces-dieux.json#sendy_only-S22]: partie du centre de la Galaxie, d’un système planétaire de la constellation de l’Archer ENDSQ (ch. 14 / PL16 / line 508)
SQ[check-ces-dieux.json#sendy_only-S29]: le mythe de l’Atlantide, mythe tenace et parfaitement compatible avec la description de l’Éden, dont la destruction évoque un super-Hiroshima ENDSQ (ch. 31 / PL33 / line 1141)

## Answer 1 — sufficient channel, recorded absent, undecided

Restricted to the 21 details that `ancient-parallels` classes as shared with an older text and absent from Genesis.

**Recorded in Sendy before 1974 (Sendy is a sufficient channel for the detail as a reading of the verse) — 7.**
D09 (first half), D14, D15, D22, D26, D33, D35. Earliest recorded witness: *Les cahiers* (1963) for D09, D14, D22, D33, D35; *Ces dieux* (1969) for D15 and D26. Each differs from the canon in agent or scale as the table states.

**Recorded in part, with a stated difference — 7.**
D04, D05, D10, D11, D16, D20, D37. Sendy could supply the materials; the canon's specific form is not recorded.

**An item probed it; recorded absent or reversed in all five — 2.**
D12 (direction of the naming lesson reversed), D34 (pardon motive at Babel).

**The inventory cannot decide — 5.**
D18, D19, D23, D28, D29.

Set against the `ancient-parallels` ranking of sixteen:

| Rank | Detail | Sendy, per the inventory | Effect on the competing explanations |
|---|---|---|---|
| 1 | D23 dissident warns | UNDECIDED (*Dieux* no; *Cah* open) | The discriminator `ancient-parallels` asked for is not in the inventory. |
| 2 | D29 later discovery of survival | UNDECIDED | Unchanged. |
| 3 | D18 arming through the women | UNDECIDED | Unchanged. |
| 4 | D09 makers fed | IN (Gen 4 half) | E1 has a recorded carrier for the first half; the Noah half has none. |
| 5 | D20 knowledge motive | PARTIAL (violence only, *Dieux*) | TBWTT's motive not in Sendy; E3 unaffected. |
| 6 | D19 accusation | UNDECIDED (components) | Job-based Satan among the Elohim is in Sendy; the Flood accusation is not recorded. |
| 7 | D15 confined to Earth | IN | As 0072 already holds. |
| 8 | D14 benevolent discloser | IN | As 0072 already holds; individual vs group. |
| 9 | D10, D11, D12, D28 | PARTIAL, PARTIAL, NOT, UNDECIDED | Sendy does not carry the Qur'anic cluster as a cluster; D12 is reversed. |
| 10 | D33, D35 Babel | IN, IN | Both have a recorded French carrier from 1963. |
| 11 | D04, D05 contest, failed makes | PARTIAL, PARTIAL | As 0072 v0.2.0 holds (laboratory trial and error). |
| 12 | D16 conferred longevity | PARTIAL | Mechanism opposite. |
| 13 | D26 seed | IN, with Gilgamesh named | New: the Gilgamesh formula itself is in the carrier. |
| 14 | D22 sudden fiery cataclysm | IN | Nuclear Flood with fallout, 1963. |
| 15 | D37 three roles | PARTIAL | President title only. |
| 16 | D34 pardon | NOT | Absent from both the older texts and Sendy. |

## Answer 2 — the two resistant items: everything the inventory holds

### D29 — the deciders discover afterwards that life survived

QUOTE[TBWTT-2:74]: Ils observaient toujours la terre et s’étaient aperçus que la vie n’avait pas été détruite ENDQUOTE

(a) What is recorded.

- `tbwtt-inventory.json` I040 (TBWTT 2:72–74, Gen 11:1–6) carries the detail in its `message_reading`: "the home planet was afraid, and realized life had not been destroyed". Its `distinctive_detail` and search terms are about the rocket. No check note on I040 in any of the five books mentions survival or its discovery.
- *Ces dieux*: the departing Celestials equip Noah themselves (I038 quote above) and stay in contact:
  SQ[check-ces-dieux.json#I036]: La communication entre les Élohim et Noé n’a rien de plus « miraculeux » que les contacts radio et télé entre Cap Kennedy et Apollo ENDSQ (ch. 32 / PL34 / line 1156)
  At Babel nobody comes (I041 quote above). The 0072 evidence map adds that ch. 35 "explicitly says the original visitors are dead".
- *L'ère*: SQ[check-ere-du-verseau.json#I036]: Lorsque Noé et ses fils sortirent de leur « arche », ils constatèrent qu’il n’y avait personne. ENDSQ (ch. 20 (PL38) / line 1390). The Elohim are gone.
- *La lune*: SQ[check-la-lune.json#sendy_only-S23]: Noé [cf. Gen. V] est un bâtard des Elohim ENDSQ (Part I ch.4 (Tour de Babel) / line 736), "entrusted with their 'things and teachings'" (reading field); the Flood SQ[check-la-lune.json#I033]: le Déluge n’a détruit que leurs bases, la Terre reste peuplée de communautés paléolithiques ENDSQ (line 756). Yet at Babel the Elohim act (I041 quote above; note: "Elohim sabotage the project").
- *Les cahiers*: decision by leaders in the heavens; an unidentified "il" behind Noah's submarine; at Babel "colonists stop a premature space attempt" (I040 note) and "discord sown among the scientists" (I041 note).
- *Nous autres*: Flood and Babel not treated (I033 lexical mention only; I040 absent).

(b) Analysis. In *Ces dieux*, *L'ère* and *La lune* the Flood does not aim at mankind and Noah's survival is arranged by the visitors; there is nothing for them to discover. On that structure D29 cannot occur, and the notes agree. This is an inference from the recorded notes, not a recorded "absent". *Les cahiers* is different: it has a deciding leadership in the heavens, factions, and a later intervention at Babel. Whether the leadership is shown learning that Noah survived is not recorded. *La lune* has an intervention at Babel by visitors who had left, and how they learn of the tower is not recorded.

(c) What the inventory cannot settle: whether any Sendy book retells Gilgamesh XI beyond the "semences de vie" phrase (Enlil's anger at finding a survivor is in the same tablet as the seed formula Sendy quotes).

### D18 — weapons reach men through the unions with women

QUOTE[LWTE-2:25]: avec les armes qui leur sont données par les fils des Elohim bannis, du groupe de Lucifer ENDQUOTE
QUOTE[LWTE-2:25]: qui parviennent à se faire remettre par eux des armes en échange de leurs charmes ENDQUOTE
QUOTE[LWTE-2:26]: Devant les preuves ramenées par Satan devant le conseil des Eternels d'un tel carnage, Yahvé décide de faire ce que demande Satan ENDQUOTE
QUOTE[LWTE-2:27]: Noé qu'ils aident à construire un vaisseau spatial ENDQUOTE

(a) What is recorded.

- No inventory item covers LWTE-2:25–27. The inventory's unions items are I029 (Gen 6:1–2) and I031 (Gen 6:4). None of the ten notes on them mentions weapons, hunting, gifts or exchange.
- Unions, as recorded:
  SQ[check-cahiers.json#I029]: « les fils des Elohim virent que les filles des hommes étaient belles et en prirent pour femmes » (GEN. VI, 2) ENDSQ (Cahier 2, ch. V / PL5 / line 1453)
  SQ[check-la-lune.json#I029]: des bâtards nés des amours entre ﬁls d’Elohim et ﬁlles d’hommes ENDSQ (Part I ch.3 (Cosmonautes) / line 576)
  SQ[check-ere-du-verseau.json#I029]: en « fécondant les filles des hommes » qui leur auraient donné des bâtards capables de faire fonctionner les installations terrestres ENDSQ (ch. 19 (PL36) / lines 1371, 1375–1377; front matter PL46 / line 30)
  SQ[check-cahiers.json#I031]: Rois, Géants nés des Elohim et des « filles des hommes » ENDSQ (Cahier 2, ch. V / PL5 / line 1455)
- Weapons, as recorded — only the makers' own:
  SQ[check-la-lune.json#I026]: la « ﬂamme tournoyante de l’épée des chérubins » qui, à la ﬁn du chapitre III, interdiront l’accès à « l’arbre de vie » implique des usines d’armements ENDSQ (Part III ch.premier-suite / line 4619)
- Fighting before the Flood: *Ces dieux* "guerres furieuses" (I032 quote above), among the "Gérants" per the note; *Les cahiers*, a "War of the Gods" between colonist factions (sendy_only S12 reading; note on I031: "Flood follows a 'War of the Gods'").
- The remaining elements of LWTE-2:25–27: an accuser with evidence before a council — not recorded; the helpers building the vessel — recorded for *Ces dieux* (I038); amnesty offered before the Flood — not recorded (I042).

(b) Analysis. The inventory holds three of the ingredients separately (unions; arms in the visitors' hands; war before the Flood) and no passage that joins them. It was not designed to find one. D18 is in the 1979 book; Sendy's 1975 *Les temps messianiques* and anything else printed between 1974 and 1979 lie outside the inventory altogether.

## Answer 3 — Mesopotamian and related material in Sendy, per the inventory and source notes

| Text or name | Record | Where | Use |
|---|---|---|---|
| Epic of Gilgamesh | SQ[check-ces-dieux.json#I033]: ce que l’Épopée de Gilgamesh appelle « les semences de vie » ENDSQ | *Dieux* ch. 31 / PL33 / line 1137 | Noah's cargo. The only detail-level use. |
| Epic of Gilgamesh | SQ[check-ces-dieux.json#I214]: Maha Bharata sanscrit, Épopée de Gilgamesh assyrienne, Popol Vuh amérindien, pour ne rien dire des textes chinois, tibétains et autres ENDSQ | *Dieux* ch. 25 / PL27 / line 953 | Listed among witnesses of one common myth. |
| Gilgamesh | note on I214: "Mahabharata, Gilgamesh, Genesis, Avesta, Chinese myths, Popol Vuh all record the same visitors"; quote: SQ[check-cahiers.json#I214]: ne seraient pas TOUS à l’origine des reportages sur le même événement, l’arrivée des Théosites sur Terre ENDSQ | *Cah* Cahier 2, ch. III / PL5 / line 1213 | Same list, 1963. The name is in the note, not in the transcribed quote. |
| Sumerian | SQ[check-cahiers.json#sendy_only-S04]: en langue sumérienne ti signifie à la fois côte et donner la vie ENDSQ | *Cah* Cahier 2, ch. IV / PL5 / line 1339 | Eve's rib. |
| Sargon legend | SQ[check-cahiers.json#sendy_only-S24]: l’histoire de l’enfant appelé à devenir Moïse est la répétition exacte de la légende de Sargon ENDSQ | *Cah* Cahier 1, ch. IX / PL4 / line 656 | Moses' birth. |
| Babylonian imagery | SQ[check-ere-du-verseau.json#I108]: Ézéchiel a trouvé des concordances entre la Tradition hébraïque et les illustrations babyloniennes. ENDSQ | *Ère* ch. 10 (PL21) / line 682 | Ezekiel 1 explained from it. |
| Mesopotamia (place) | SQ[check-ces-dieux.json#I039]: Quand les fils et petits-fils de Noé se dispersent, dans le bassin méditerranéen et en Mésopotamie ENDSQ | *Dieux* ch. 34 / PL36 / line 1210 | Post-Flood dispersal. |
| Santillana | SQ[check-ere-du-verseau.json#I041]: ils ont réussi à imposer ce « seul langage » que Santillana appelle « le langage initiatique international » des temps archaïques ENDSQ | *Ère* ch. 20 (PL38) / lines 1416, 1424, 1427 | The "one language" of Genesis 11. |
| Mahabharata | S12 reading; note on I150 ("SWASTI") | *Cah* | "War of the Gods" before the Flood. |
| Prometheus | SQ[check-nous-autres.json#sendy_only-S21]: Prométhée a volé le « feu » des dieux ENDSQ; *Dieux* sendy_only S15 reading links the Nefilim "to Lucifer and Prometheus" | *Nous* ch. "Le Moyen Age" (PL5) / line 351; *Dieux* ch. 30 | Theft of the gods' fire. |
| Enoch (Genesis figure) | reading/note fields only: "Hénoc-City"; "Enoch adoptive son" | *Cah* S11; *Lune* I028 | Genealogy. Not the Book of Enoch. |
| Apocrypha (word) | SQ[check-nous-autres.json#sendy_only-S23]: « Apocalypse » ne veut pas du tout dire « vision d’horreur », mais « Révélation » ENDSQ (reading: "apocryphal means hidden, not false") | *Nous* ch. "Les inventeurs" (PL3) / line 203 | Etymology only. |
| Book of Enoch, Watchers, Jubilees, Atrahasis, Utnapishtim/Ziusudra/Xisuthros, Berossus, Oannes, Enlil, Anunnaki | **no record** in any inventory file, the 0072 documents or the source notes | — | Null result about the inventory. |

Analysis. On the record, Sendy's use of Mesopotamian literature is slight and of one kind: Gilgamesh as a named witness to the common myth, and once as the source of the "seeds of life". No narrative from Atrahasis or Tablet XI (council, oath, Ea's warning, Enlil's discovery, the hungry gods) is recorded, and nothing Enochic. `ancient-parallels` found that TBWTT and ETTMTTP never name Gilgamesh or Enoch and that LWTE names both once, in Terrusse's essay (LWTE-4:105, 4:108). Sendy named Gilgamesh in 1963 and 1969.

## Answer 4 — work order for when the Sendy texts are back in hand

Line numbers are those of the inventory's text extractions (`/private/tmp/sendy-study/*.txt` at the time; they will need re-deriving from the EPUB/PDF if the extractions are gone). Ordered by leverage.

| # | Book | Where | Question | Closes |
|---|---|---|---|---|
| L01 | *Les cahiers* (1963) | Cahier 2, ch. V–VII (PL5), lines c. 1455–1610; anchors 1472 ("NOS DIRIGEANTS…"), 1510 ("il savait…"), 1597–1607 (Babel) | Who is "il"? Who speaks "NOS DIRIGEANTS" and to whom? Is the warning to Noah given against the leadership's decision? After the Flood, do the Théosites learn that Noah or the documents survived, and is that why they act at Babel? | D23, D29, D21 |
| L02 | all five; first *Cahiers* (lines 1453–1475), *Dieux* (ch. 24–25, 30) | the Gen 6:1–4 passages | Full-text search: arme(s), épée, glaive, arsenal, chasse, "en échange", charmes, near "filles des hommes". Any transfer of weapons or technique to or through the women? | D18 |
| L03 | *Dieux* (ch. 30, PL32, lines 1095–1124); *Cahiers* (line 1472) | "guerres furieuses"; the War of the Gods | Who fights, with whose weapons? Is the fighting a reason for the Flood or its setting? | D18, D20 |
| L04 | *Cahiers* (1472); *Lune* (lines 2085, 4907); *Dieux* (line 1113) | leadership and council passages | Any deliberation before the Flood — accusation, evidence, a president deciding? | D19, D37 |
| L05 | *Lune* (Part I ch. 4, lines 733–1040); *Ère* (ch. 20, lines 1390–1427) | Babel chapters | *Lune*: how do the departed Elohim learn of the tower; any surprise at human survival or progress? *Ère*: confirm nobody intervenes. | D29 |
| L06 | *Ère* (ch. 16, line 1061; ch. 17); *Dieux* (ch. 14, line 508; ch. 39, lines 1385–1386) | "Le Commencement fit les Élohim"; galactic chain | Were the Elohim themselves made or seeded by predecessors? Any message, probe or automatic vessel from them? | D31 |
| L07 | *Dieux* (ch. 30, lines 1111–1113); *Lune* (4907); *Ère* (ch. 17–18) | Satan, Lucifer, Job | Is Satan ever hostile to mankind? Are Satan and Lucifer ever two persons or parties? | D11, D19, D37 |
| L08 | all five, full-text | Gilgamesh, Outa-Napishtim, Sumer, Chaldée, Bérose, Oannès, Hénoch (book), Veilleurs, Jubilés, apocryphes | Every occurrence with context and the edition Sendy cites. Read the whole passage round *Dieux* line 1137: does he retell Tablet XI (Ea's warning, Enlil's anger)? | D23, D29, D26, D18 |
| L09 | all five, full-text | moqu-, railler, risée, incrédul- near Noé | Is Noah mocked or disbelieved? | D28 |
| L10 | *Ère* (ch. 19, lines 1374–1382); *Dieux* (ch. 31, lines 1136–1141) | tebah passages | Does the closed vessel ever leave the ground? Is Gen 7:17 cited? | D25 |
| L11 | *Cahiers* (line 1176); *Dieux* (ch. 2; line 1141) | continental fit; Atlantis; diplodocus | Any link between the Flood and a break-up of continents or the end of the great reptiles? | D03, D32 |
| L12 | *Cahiers* (lines 1079–1084) | earlier Golden Age destroyed by megatons | Is it ever a failed creation, or on another planet? | D06 |

Outside the five books, and needed before anything is said about LWTE (1979): the same searches L02, L04, L06, L08 in *Les temps messianiques* (1975, held but read for one passage) and in *Les dieux nous sont nés* (1966, never inspected). A first-printing collation of *Ces dieux* is needed before its passages (D15, D24, D26) are dated to 1969 rather than to the 1979 reissue.

## Answer 5 — how this refines woh-claim-0072

The record's open position stands. Nothing here argues dependence or independence.

**Resemblance — additions the evidence map does not yet list.**
- Humans provisioning the physical Elohim on Genesis 4 (I027; *Cahiers*, *Ces dieux*, *L'ère*) against TBWTT-2:48.
- The Flood decided by leaders "qui vivent dans les cieux" (*Cahiers* sendy_only S12) against TBWTT-2:58 "de leur lointaine planète". The 0.2.0 row "Deliberate technological Flood … factional structure differs" could cite this and note that *Les cahiers* has factions.
- Radioactive contamination and the wait for it to clear (*Cahiers* I034, I036) against TBWTT-2:60.
- Loss of the Babel "appareillage" (*Cahiers* I041) against TBWTT-2:76 "appareillages".
- The visitors help build the vessel (*Ces dieux* I038) against LWTE-2:27 — a first data point for outstanding research 5 (extension to the later Messages).
- Gilgamesh named as the source of "semences de vie" (*Ces dieux* I033). The existing row "Noah and biological preservation" mentions seeds of life without the attribution.

**Difference — sharpened.**
- Satan. In Sendy, Satan = Lucifer = the pro-human discloser. In the canon Satan heads the party hostile to man and Lucifer's group is the other party. Same names, same Job proof-text, opposite assignment.
- No pardon anywhere in the inventoried Sendy: not as Babel's purpose, not as the exiles' fate.
- Direction of the naming lesson (already in the map) and absence of any motive for making man.
- No orbit; the capsule analogy stays an analogy (the map's caution is confirmed by the notes).
- Where the survivor's warner is recorded (*Ces dieux*), it is the destroying party itself.

**Dependence — what moves and what does not.**
- For the Genesis chapter the inventory already reported 44 of 44 items precedented. This cross-check shows the same holds, in substance, for 14 of the 21 older-text parallels that `ancient-parallels` isolated (7 IN, 7 PARTIAL). For those, an ancient Near Eastern text is not needed to explain the canon's wording: a French book of 1963–1970 carries the reading. That statement is about sufficiency of a channel. It says nothing about which channel was used, and nothing about whether the events occurred.
- Two parallels are recorded as *not* carried (D12, D34) and five cannot be decided (D18, D19, D23, D28, D29). The two that `ancient-parallels` called resistant are both among the undecided. They remain the places where a test has purchase.
- One caution for `ancient-parallels` explanation E1: it described 0072 as having verified three shared items. On the inventory the count of primeval items with a recorded Sendy carrier is larger, and one of them (D26) carries a Mesopotamian formula by name.
- The 0072 revision trigger "a broader reading materially changes the differences reported here" is not met by this note: it adds rows, it does not change the adjudication.

## Tensions and null results

- **Null:** no inventory record of the Book of Enoch, the Watchers, Jubilees, Atrahasis, Utnapishtim, Berossus or Oannes (finding 8).
- **Null:** no record of a dissident warner, of a later discovery of survival, of weapons passed to humans, of an accusation before a council, of Noah mocked, of a pardon.
- **Tension inside Sendy, per the inventory:** the serpent is a dissident colonist (1963), a mutant native (1969), a fallen Angel (1969, the other book) and a Théosite again (1970). Babel is stopped by the colonists (1963), sabotaged by the Elohim (1968), left alone (1969). Any statement "Sendy has X" must name the book. The 0072 record already warns of this.
- **Tension with the inventory's own summary:** `check-cahiers.md` summarises the Flood as "nuclear Flood with radioactive fallout, but the ark is a submarine". The item-level records add the leaders in the heavens and the factions, which the summary and the 0072 map ("factional structure differs") do not bring out.
- **Counter-example to "Sendy as sufficient channel":** seven details that have no ancient counterpart are also recorded absent from Sendy (D01, D03, D06, D08, D27, D34, D36), and the TBWTT Flood motive (progress) is recorded not found. The canon's primeval narrative is not exhausted by the older texts plus the inventoried Sendy.
- **Coding inconsistency to note:** `combined-best.json` reduces each item to its best status across books. For this question that hides the book and the date; the per-book files were used throughout.

## Relation to existing core records

- **woh-claim-0072** — see Answer 5. No change to proposition or adjudication is proposed.
- **woh-claim-0010 (flood-as-reset), 0012 (watchers), 0017 (Babel), 0008 (council), 0034 (labor anthropogony)** — `ancient-parallels` proposed revisions to each. This note adds one consideration to those proposals: where an evidence map reads a canon detail as converging with an older text, it should also record whether the inventoried Sendy carries the same detail (D09, D22, D26, D33, D35 do; D34 does not).
- **`ancient-parallels.md`** — its open question 1 is answered in part (D09 yes; D29 and D18 undecided). Its statement that "Sendy and all other modern precursors were not inspected" can now point here for the inventory-level answer.

## Candidate claims or revisions for founder review

Proposals only.

1. **0072 evidence map:** add the six resemblance rows and the Satan/Lucifer and pardon difference rows of Answer 5, each citing the inventory item. Grade them "agent-coded, not spot-checked" until the texts are re-read.
2. **0072 outstanding research:** add the work order (L01–L12) as item 7, with L01 and L08 first.
3. **Sendy inventory, second pass:** a supplementary inventory built from LWTE ch. 2 and ch. 4 and ETTMTTP (the details with no item: D18, D19, D24, D28, D31, D32), coded against the five books plus *Les temps messianiques* and *Les dieux nous sont nés*.
4. **Source note `sendy-cahiers-moise`:** add the "NOS DIRIGEANTS (qui vivent dans les cieux)" passage and the War of the Gods to "Reported content", flagged as inventory-derived.
5. **`ancient-parallels` explanation E1:** reword "the only part the project has verified is … three items" to refer to the inventory-level result here, keeping its [outside knowledge] flags on French availability of the ancient texts themselves.
6. **Not proposed:** any new claim. The result is a cross-reference between two existing studies.

## Limitations

- The Sendy texts were not read. Every Sendy statement is second-hand from agent-coded records, each quote under about 40 words, some with typographic artefacts kept as recorded ("85o ans", "ﬁls").
- The inventory's "absent" is relative to TBWTT's reading of a verse. Seven details have no item at all.
- The verdicts IN / PARTIAL / NOT are my grading of the recorded notes. The register gives the items so each can be re-graded.
- Structural inferences (D29 in three books, D08) are marked as inferences.
- Dates are of first publication; the witnesses are later digital editions, one a 1979 reissue. No first printing collated.
- The canon text is the 2005 collected French edition as dumped for this research; the 1974 first printing is uncollated (0072).
- Locators are line numbers in extractions that may no longer exist.
- Whether Raël read any of these books is outside this note and outside the inventory.

## Verification

- Canon quotations: `verify_quotes.py` on this file.
- Sendy quotations: `agent-sendy-crosscheck/verify_sq.py` on this file (each `SQ[…]` is a substring of the named inventory record's `quote_fr`).
- Register: `sendy-crosscheck.json`, built by `agent-sendy-crosscheck/build.py` directly from the inventory files.
