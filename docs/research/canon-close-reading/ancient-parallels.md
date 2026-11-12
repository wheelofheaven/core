---
title: "Canon close reading: primeval-history details against older texts"
status: draft
version: 0.1.0
last_reviewed: 2026-11-12
---

# ancient-parallels — the canon's primeval history against Genesis and the older texts in the library

Research note for wheelofheaven/core. Draft for founder review. Nothing here is a decision.

## Exact question

Which specific narrative details in the canon's account of the creation, Eden, the exiled creators, the Flood, Babel and the unions with human women are **not in Genesis** but **do appear in other ancient texts held in the project library** — and which canon details have no ancient parallel there at all?

## Method

1. Read TBWTT, ETTMTTP and LWTE in French and extracted the primeval narrative as 37 discrete details (D01–D37). The narrative sits in TBWTT-2:2–78 (Yahweh's voice), is retold with changes in LWTE-2:6–29 (Raël's exposition) and LWTE-1:45–48 (Raël, Q&A), and is extended geologically in LWTE-4:40–56. ETTMTTP adds one detail (ETTMTTP-3:234).
2. Checked each detail against Genesis in `genesis-woh` (Hebrew and English).
3. Read in full: `atrahasis-woh`, `gilgamesh-woh` (Tablet XI, the only tablet held), `flood-story-woh`, `enki-and-ninmah-woh`, `adapa-woh`, `song-of-the-hoe-woh`, `eridu-genesis`, `enuma-elish`, 1 Enoch 6–16 in `book-of-enoch-woh`, Jubilees 3–10 in `jubilees-woh`. Read by targeted search: the rest of `book-of-enoch` (Charles), `book-of-jubilees` (Charles), `sumerian-king-list-woh`, `chaldean-account-of-genesis` (Smith 1876, for Berossus and the Babel fragments), `theogony-woh`, `baal-cycle-woh`, `quran`, `vendidad-woh`.
4. Every library citation is a refId from the library files. English is the library's `i18n.en` (or the English `text` of the public-domain editions). A script (`agent-ancient-parallels/check.py`) confirmed that every cited refId exists and that every English snippet occurs under the refIds given.
5. Layers are kept apart: **(a) what the texts say** is in the register; **(b) analysis** is marked "Analysis"; **(c) open questions** are in their own section.

Status codes in the matrix: **P** present, **p** partial, **A** absent, **C** contrary, **D** different content in the same slot, **-** episode not covered by the library holding.

Columns: **GEN** Genesis · **ATR** Atrahasis · **GIL** Gilgamesh XI · **SUM** Sumerian Flood Story, Enki and Ninmah, Song of the Hoe, Sumerian King List, Adapa · **BER** Berossus, the Sibyl and the Babel fragment as printed in Smith 1876 · **ENO** 1 Enoch · **JUB** Jubilees · **QUR** Quran · **OTH** Theogony, Vendidad 2, Enuma Elish.

## Findings (ranked)

Counts over the 37 details:

- Shared with an older text, absent from or reversed in Genesis: 21
- Already in Genesis (the canon's addition, if any, has no ancient counterpart): 4
- The canon contradicts the older texts: 2
- Canon only, and contradicted by every text that covers the point: 2
- Canon only (no counterpart found in the library): 6
- Too weak to discriminate: 2

### 1. The Flood's cast is Mesopotamian, and it is the reverse of Genesis, 1 Enoch, Jubilees and the Quran (D23, D29, D37)

(a) In the canon one party decides the destruction and another, against it, warns the survivor.

QUOTE[TBWTT-2:58]: Mais les exilés, prévenus de la chose, avaient demandé à Noé de construire une fusée ENDQUOTE

In Genesis the destroyer warns the survivor himself (GEN-WOH-6:13–14). So does the Most High in 1 Enoch (ENO-WOH-10:1–2), God in Jubilees (JUB-WOH-5:21) and in the Quran (QUR-11:37). In Atrahasis and Gilgamesh XI the warner is a god who is under the assembly's oath and breaks its intent: "Ea too swore with them" (ATRA-WOH-II:viii.3); "I did it, indeed, against your will! / I saw to it that life was preserved" (ATRA-WOH-III:vi.17–18); "Prince Ea was with them, bound by the (same) oath" (GILG-WOH-11:19).

The canon also has the deciders find out afterwards that life survived.

QUOTE[TBWTT-2:74]: Ils observaient toujours la terre et s’étaient aperçus que la vie n’avait pas été détruite ENDQUOTE

That is Enlil's discovery: "Where did life escape? / How did a man survive the catastrophe?" (ATRA-WOH-III:vi.9–10); "No man was to have survived the destruction!" (GILG-WOH-11:172). Genesis has the opposite (GEN-WOH-8:1).

(b) Analysis. The warning-by-a-dissident is partly forced by the canon's own premise: once the deciders are far away and a sympathetic group is on Earth, someone other than the destroyer has to warn. The later discovery of survival is not forced by that premise, and it is the more telling match. One structural difference remains: Ea is a sitting member of the assembly, while the canon's warners have already been expelled from it.

### 2. An Enochic cluster, concentrated in the 1979 book (D18, D19, D20, D15, D14)

(a) LWTE adds to the 1974 narrative that the exiles' sons armed mankind through the women, and that the resulting bloodshed was laid before the Council.

QUOTE[LWTE-2:25]: avec les armes qui leur sont données par les fils des Elohim bannis, du groupe de Lucifer ENDQUOTE
QUOTE[LWTE-2:26]: Devant les preuves ramenées par Satan devant le conseil des Eternels d'un tel carnage, Yahvé décide de faire ce que demande Satan ENDQUOTE

1 Enoch has each element: "Asael taught men to make swords and knives and shields and breastplates" (ENO-WOH-8:1); "they all began to reveal mysteries to their wives" (ENO-WOH-8:3); "this you made known to the women" (ENO-WOH-16:3); four heavenly beings "beheld much blood that was shed upon the earth" and bring the case to the Most High (ENO-WOH-9:1–11), who then rules (ENO-WOH-10:1). Genesis has only "the land was filled with violence" (GEN-WOH-6:11) and gives metal blades a human origin (GEN-WOH-4:22).

1 Enoch 69:6 (library refId 1ENO-69:4) gives one angel both acts the canon gives the Lucifer group: "he led astray Eve, and showed ... all the weapons of death to the children of men."

The 1974 Flood motive — knowledge, not violence — has one counterpart in the library: "their ruin is accomplished because they have learnt all the secrets of the angels" (1ENO-65:6).

(b) Analysis. The order of events in LWTE-2:25–27 is the order of 1 Enoch 6–10: unions, arming, bloodshed, report to the presiding figure, decree, Noah. The differences are just as definite. In Enoch the accusers are the loyal archangels, not a Satan. The warning to Noah comes from the Most High, not from the condemned group (finding 1). The offspring are man-eating giants (ENO-WOH-7:2–4), where the canon has "enfants exceptionnels" (TBWTT-2:55). The Watchers are sentenced *for* the unions; in the canon the group is already under sentence when the unions happen (D17).

(c) None of this is in TBWTT. The one place in the three books where the Book of Enoch and Gilgamesh are named is LWTE ch. 4, in a testimony by the guide Marcel Terrusse (attribution at LWTE-4:95), not in the Messages:

QUOTE[LWTE-4:105]: Le Gilgamesh, épopée suméro-babylonienne ENDQUOTE
QUOTE[LWTE-4:108]: le livre d'Enoch, la Kabbale, la Bible ENDQUOTE

A search of TBWTT and ETTMTTP for Hénoch/Enoch, Gilgamesh, Sumer and Babylon returns nothing (null result). TBWTT's own list of witnesses is at TBWTT-5:54: the Kabbalah, Greek mythology, and the Buddhist, Islamic and Mormon religions.

### 3. The vessel has no ancient parallel and every text contradicts it — including the verse the canon quotes (D25, D27)

(a) The canon's proof is a half-verse.

QUOTE[TBWTT-2:60]: il est bien dit qu’elle s’éleva audessus de la Terre et non pas sur les eaux ENDQUOTE

GEN-WOH-7:17 reads in full: "the waters increased and lifted up the ark, and it rose above the land" (וַיִּשְׂאוּ אֶת־הַתֵּבָה וַתָּרָם מֵעַל הָאָרֶץ). GEN-WOH-7:18 continues: "the ark went on the face of the waters" (וַתֵּלֶךְ הַתֵּבָה עַל־פְּנֵי הַמָּיִם). The canon's quotation at TBWTT-2:59 stops before the cause and skips the next verse.

Every other text that describes the vessel has a boat on water: pitch and a cut mooring-rope (ATRA-WOH-III:i.21, III:ii.33); punt-poles and a launch "until two-thirds of her had entered the water" (GILG-WOH-11:61, 11:76); "the great boat had been tossed by the destructive storms on the great waters" (FLS-WOH-D:5); "trust himself fearlessly to the deep" (CAG-3:17); "a wooden (building)" (1ENO-67:1, v. 2); a ship running "amid waves like mountains" (QUR-11:42, my gloss).

The passenger list is likewise the canon's alone: "un couple de chaque race humaine de la Terre" (TBWTT-2:62) against Noah's household in Genesis and family, kin and craftsmen in Gilgamesh (GILG-WOH-11:81–82).

(b) Analysis. This is the clearest case where the canon and the whole older record disagree on a concrete point. It cuts against simple borrowing (nothing to borrow) and equally against the reading of the older texts as unaltered memory of the canon's event (they would all have made the same change).

### 4. The canon contradicts the labor anthropogony at the creation, and agrees with it about feeding the makers (D08, D09)

(a) Why man is made:

QUOTE[TBWTT-2:25]: C’est alors que les plus habiles d’entre nous voulurent créer un homme comme nous artificiellement ENDQUOTE

Atrahasis, Enki and Ninmah and the Song of the Hoe say man was made to take over the gods' work: "let man bear the labor of the gods" (ATRA-WOH-I:195); "fashion a substitute for the gods (?), so that they may be released from their toil" (ENM-WOH-1:23); "took them up to provide rations for the gods" (SOTH-WOH-1:31). The canon has no such motive.

But after the Flood the canon has this:

QUOTE[TBWTT-2:64]: Noé s’engagea à verser une part de toutes les récoltes ou élevages aux créateurs pour leur subsistance ENDQUOTE

Genesis has only an aroma (GEN-WOH-8:21). Atrahasis and Gilgamesh have gods who go hungry without mankind and crowd the first sacrifice: "The Anunna, the great gods, / sat in thirst and hunger" (ATRA-WOH-III:iv.18–19); "The gods gathered like flies" (GILG-WOH-11:159).

(b) Analysis. Core claim 0034 reads the Mesopotamian labor anthropogonies and Genesis 2 as converging memory of a purposive creation. The canon itself does not state the labor purpose; it states a different one. What the canon shares with the Mesopotamian texts is the provisioning relationship, placed after the exile and after the Flood.

### 5. Pardon: explicit in the canon, absent from every Babel text, denied in every text that has a confined heavenly group (D34, D36)

(a) The pardon motive of the Babel expedition is stated outright:

QUOTE[TBWTT-2:72]: Ces derniers voulaient que les hommes aillent sur la planète des créateurs afin d’obtenir leur pardon ENDQUOTE

No Babel text in the library has it. Those that give a motive give defiance: "glorying in their own strength and size and despising the gods" (CAG-3:28); "evil purpose" (JUB-WOH-10:18). The nearest shape is in a different episode: before the Flood the condemned Watchers ask Enoch to carry "a memorial of petition for them, that they might find forgiveness" (ENO-WOH-13:4); he is borne up to heaven (ENO-WOH-14:3); the answer is "There shall be no peace for you" (ENO-WOH-16:4).

The canon then has the exiles pardoned:

QUOTE[TBWTT-2:78]: Les créateurs exilés furent pardonnés et eurent le droit de revenir sur leur planète d’origine ENDQUOTE

1 Enoch, Jubilees, the Quran and the Theogony all refuse release to their confined groups (ENO-WOH-12:5; JUB-WOH-5:6; QUR-15:37; THEO-732).

(b) Analysis. Two corrections for existing records follow. The 0017 evidence map grades the pardon motive "inferred ... the canon's account is read toward it rather than quoting it"; TBWTT-2:72 states it. And the two canon books date the amnesty differently: after Babel in TBWTT-2:78, offered before the Flood in LWTE-2:26.

### 6. The two canon books do not tell the same Flood (D20, D29, D30, D36)

(a) Four points differ between TBWTT (1974) and LWTE (1979).

- Motive. TBWTT: progress. QUOTE[TBWTT-2:55]: Le progrès scientifique était énorme sur Terre et ils décidèrent de supprimer leur création ENDQUOTE LWTE: violence. QUOTE[LWTE-2:25]: car il les juge dangereux en raison de leur violence ENDQUOTE
- Survival. TBWTT-2:74 has the home world discover it later. LWTE has the Elohim take part in the restoration: QUOTE[LWTE-2:28]: aident l'équipe de Lucifer à réimplanter sur Terre les formes de vie qui ont été préservées dans «l'arche » ENDQUOTE
- Why never again. TBWTT-2:66: they understood that progress is normal. LWTE-2:28: they found they had themselves been created.
- Amnesty. After Babel (TBWTT-2:78); before the Flood (LWTE-2:26).

(b) Analysis. On motive, the later book moves from the one position with a single ancient counterpart (1 Enoch 65:6) to the position of Genesis and 1 Enoch 9. Also unresolved inside TBWTT: the subject of "promirent" in TBWTT-2:66 is "Les créateurs", who "avaient compris" — which fits the deciders — yet eight paragraphs later the home world only then learns that life survived.

### 7. A Qur'anic cluster around the creation of man (D10, D11, D12, D15, D28)

(a) Five canon details absent from Genesis are explicit in the Quran (Arabic only in the library; glosses mine): the heavenly assembly objects to man before he is made, because he will shed blood (QUR-2:30); the maker teaches Adam the names (QUR-2:31), where Genesis has Adam do the naming (GEN-WOH-2:19) and the canon says "Les créateurs lui apprirent le nom" (TBWTT-2:32); the adversary is a member of the assembly who is given leave to work on mankind (QUR-15:36–39); the tempter is sent down to Earth with the humans (QUR-7:24); Noah is mocked (QUR-11:38; ETTMTTP-3:234).

Jubilees has two of them independently: angels teach Adam (JUB-WOH-3:15), and Mastema is licensed (JUB-WOH-10:8) and proposes the test of Abraham (JUB-17:10).

(b) Analysis. These are the stock of post-biblical retelling of Genesis, shared by Jewish, Christian and Islamic tradition. They need no Mesopotamian source and no special access.

### 8. Makers in competition and failed makes (D04, D05, D06)

(a) The canon's teams "organisaient des concours" (TBWTT-2:21) and some made monsters (TBWTT-2:22); earlier human "prototypes" were superseded (TBWTT-5:64). Enki and Ninmah is an explicit making-contest that yields defective humans (ENM-WOH-1:54–101). Berossus has "most hideous beings" that die and are replaced by "other men and animals, which should be capable of bearing the air" (CAG-3:13, 3:15); his first creatures die because they cannot "bear the prevalence of light", and LWTE-2:11 has an earlier creation burned by a star's "rayons nocifs".

(b) Analysis. Partial and typological. No library text has separate regional teams, races per team, or a jury.

### 9. Babel: ascent and demolition come from Jubilees and the Sibyl, not Genesis (D33, D35)

(a) "Let us ascend by it into heaven" (JUB-WOH-10:19); "that they might climb up into heaven" (CAG-3:34). The structure is destroyed: "the Lord sent forth a great wind against the tower, and overthrew it" (JUB-WOH-10:26); "the winds assisted the gods, and overthrew the work" (CAG-3:28). Genesis has a tower "with its top in the skies" and builders who simply stop (GEN-WOH-11:4, 11:8). The canon: "ils détruisirent les appareillages scientifiques" (TBWTT-2:76).

The canon's scattering sends the builders to lands "où aucun ne pouvait se faire comprendre car le langage y était différent" (TBWTT-2:76): languages already differ. That agrees with GEN-WOH-10:5 ("each by his tongue") and disagrees with GEN-WOH-11:7 and with every Babel parallel.

### 10. "Seed" (D26)

(a) "Bring aboard the seed of all living things into the boat" (GILG-WOH-11:27, zēr napšāti kalāma); "the seed of humankind" (FLS-WOH-E:10); taoxma, "seed", of men, cattle and plants in Vendidad 2 (VID-2:27–28; Avestan only, gloss mine); "to keep seed alive" (GEN-WOH-7:3). The canon: "une cellule vivante de chaque espèce, mâle et femelle" (TBWTT-2:58).

(b) Analysis. The word is in Genesis too, so this is not a clean extra-Genesis case. Gilgamesh XI 27 is the formulation closest to the canon's because the seed is itself the cargo. In all the ancient texts live animals are loaded as well; re-creation from the seed is the canon's alone.

## Matrix

| ID | Detail | GEN | ATR | GIL | SUM | BER | ENO | JUB | QUR | OTH | Class |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D01 | Home-world public opinion and government forbid the life experiments; the scientists leave for a distant planet | A | C | - | C | A | A | A | A | A | unique |
| D02 | Earth is found, not made; it is water-covered; the 'light' is tested for harmful rays | D | - | - | A | p | A | A | A | p | unique |
| D03 | One continent is raised from a shallow sea-bed by explosions; the continents later split (at the Flood, LWTE ch. 4) | p | A | A | A | A | A | A | A | A | unique |
| D04 | Several teams of makers work in parallel, meet, compare and hold contests | A | p | - | P | A | A | A | A | A | shared-not-genesis |
| D05 | Some teams make monsters; earlier human 'prototypes' are superseded | p | A | - | p | P | A | A | A | A | shared-not-genesis |
| D06 | Earlier creation attempts fail (destroyed on order; burned by a star's harmful rays; choked by vegetation); two other planets seeded | A | A | - | A | p | A | A | A | A | unique |
| D07 | Man is made artificially, in laboratories, in the makers' image | P | p | - | p | p | A | A | p | A | genesis-has-it |
| D08 | Why man is made: the ablest makers want to make a being like themselves (no labor motive) | D | C | - | C | A | A | A | A | A | canon-contradicts-older |
| D09 | Humans supply food to the makers: offerings prompted by the exiles; after the Flood Noah pledges a share of crops and herds 'for their subsistence' | p | P | P | P | p | A | A | A | p | shared-not-genesis |
| D10 | The home world objects to the making of man and fears he will surpass his makers; man must be kept ignorant | p | C | - | p | A | A | p | P | p | shared-not-genesis |
| D11 | Satan is one of the Elohim, head of the party that expects only evil from man; he is later licensed to test humans | A | p | p | A | A | p | P | P | A | shared-not-genesis |
| D12 | The makers teach the first man the names and properties of plants and animals | C | A | - | A | p | A | p | P | A | shared-not-genesis |
| D13 | The prohibition concerns scientific knowledge (books) | P | A | - | p | A | p | A | A | A | genesis-has-it |
| D14 | The 'serpent' is a small group of the makers themselves who, out of love for the humans, tell them the truth | D | p | p | p | A | p | D | p | p | shared-not-genesis |
| D15 | The disclosing group is sentenced by the home government to live on Earth; the other makers must leave | D | A | A | A | A | p | p | p | p | shared-not-genesis |
| D16 | Longevity is a technique ('tree of life'); the exiles obtain it for the chiefs of the first humans, hence the patriarchs' ages; it is not hereditary | C | A | p | p | p | p | D | D | A | shared-not-genesis |
| D17 | The 'sons of Elohim' who take human daughters are the exiled makers; the children are exceptional | P | A | - | A | A | P | P | A | p | genesis-has-it |
| D18 | The exiles' sons hand weapons to human women; men slaughter each other with them; this bloodshed is the case for destruction | A | A | - | A | A | P | p | A | A | shared-not-genesis |
| D19 | An accuser lays the evidence before the Council; the president decides | A | p | p | p | A | P | A | A | A | shared-not-genesis |
| D20 | Why the destruction: (TBWTT) human scientific progress, the wish to equal the makers; (LWTE) human violence | D | C | A | A | A | P | D | D | A | shared-not-genesis |
| D21 | The decision is taken on the distant home planet | p | p | C | A | A | p | A | A | A | weak |
| D22 | The means: explosions; a tidal wave over the single continent; a sudden cataclysm, not prolonged rain; fallout afterwards | D | p | p | p | A | p | D | D | A | shared-not-genesis |
| D23 | The survivor is warned by the dissident (exiled) makers, against the intent of those who decided — not by the destroyer | C | P | P | p | p | C | C | C | A | shared-not-genesis |
| D24 | The exiles help build the vessel | A | A | C | A | A | p | A | p | A | weak |
| D25 | The vessel is a rocket that orbits the Earth; life is kept some thousands of kilometres up; 'above the earth and not on the waters' | C | C | C | C | C | C | C | C | A | unique-and-contradicted |
| D26 | What is preserved is a living cell, male and female, of each species; the animals are re-created from them afterwards | p | p | P | p | p | p | A | p | p | shared-not-genesis |
| D27 | Aboard: Noah and one couple of each human race; each race is put back at its place of creation | C | C | C | A | C | C | A | C | A | unique-and-contradicted |
| D28 | Noah was not believed and was mocked | A | p | p | A | A | A | A | P | A | shared-not-genesis |
| D29 | Those who ordered the destruction learn only afterwards that life survived, and are alarmed | C | P | P | - | A | A | A | A | A | shared-not-genesis |
| D30 | The makers promise never again to destroy mankind; the reason | P | p | p | p | A | P | p | A | A | genesis-has-it |
| D31 | The Elohim are themselves created beings (message in an automatic vessel from their own makers) | A | A | A | A | A | A | A | A | p | unique |
| D32 | Not every species is re-established after the Flood (the great reptiles are left out); geology and coastlines are rewritten | C | A | p | A | p | p | A | A | A | unique |
| D33 | The tower is a vehicle for reaching the makers' world, built by the most advanced people with the exiles' help | p | - | - | - | P | A | P | A | A | shared-not-genesis |
| D34 | The purpose is to obtain the exiles' pardon by showing mankind grateful and peaceful | D | - | - | - | C | p | C | A | A | shared-not-genesis |
| D35 | The home world is alarmed, comes, removes the most learned and scatters them among peoples whose languages already differ, and destroys the equipment | p | - | - | - | P | A | P | A | A | shared-not-genesis |
| D36 | The exiles are then pardoned, return home and plead for mankind | A | p | p | A | A | C | C | C | C | canon-contradicts-older |
| D37 | Three roles: the one who presses for destruction (Satan), the president who decides (Yahweh), the faction that saves (Lucifer's group); Yahweh is also one of the makers | C | P | P | p | A | p | A | A | A | shared-not-genesis |

## Full register

### D01 — Home-world public opinion and government forbid the life experiments; the scientists leave for a distant planet

Episode: creation. Canon voice: Yahweh. Class: unique.

QUOTE[TBWTT-2:2]: l’opinion publique de notre planète et le gouvernement interdirent à ces savants de poursuivre leurs expériences ENDQUOTE

- **ATR C** [ATRA-WOH-I:220] the making of man is approved by the whole assembly: '"Yes!" they answered in their assembly' (an-nu i-pu-lu i-na pu-uḫ-ri-šu-nu)
- **SUM C** [ENM-WOH-1:23] the gods themselves ask for the substitute to be made
- Absent (read, nothing found): GEN, BER, ENO, JUB, QUR, OTH

### D02 — Earth is found, not made; it is water-covered; the 'light' is tested for harmful rays

Episode: creation. Canon voice: Yahweh. Class: unique.

QUOTE[TBWTT-2:5]: Ils ont «créé», découvert en réalité, la terre ENDQUOTE
QUOTE[TBWTT-2:8]: Il s’avéra que le soleil chauffait correctement la Terre sans lui envoyer de rayons nocifs ENDQUOTE

- **GEN D** [GEN-WOH-1:2] primeval waters are present ('the breath of the Elohim hovering over the face of the waters'); the Earth is not 'found'
- **BER p** [CAG-3:13, CAG-3:15] pre-existing 'darkness and an abyss of waters'; first creatures 'not being able to bear the prevalence of light, died'
- **OTH p** [EE-1:5] pre-existing mingled waters (King's text, fragmentary)
- Absent (read, nothing found): SUM, ENO, JUB, QUR

Analysis: Only the pre-existing water is shared, and Genesis has that too.

### D03 — One continent is raised from a shallow sea-bed by explosions; the continents later split (at the Flood, LWTE ch. 4)

Episode: creation. Canon voice: Yahweh (TBWTT); Marcel Terrusse, guide (LWTE-4:40, see LWTE-4:95). Class: unique.

QUOTE[TBWTT-2:14]: fait en sorte que de la matière soit enlevée du fond des mers et qu’elle s’amasse au même endroit, ce qui forma un continent ENDQUOTE
QUOTE[LWTE-4:40]: les plaques continentales se séparèrent brutalement ENDQUOTE

- **GEN p** [GEN-WOH-1:9] waters gathered 'to one place', dry ground appears; no explosions, no later break-up
- Absent (read, nothing found): ATR, GIL, SUM, BER, ENO, JUB, QUR, OTH

### D04 — Several teams of makers work in parallel, meet, compare and hold contests

Episode: creation. Canon voice: Yahweh. Class: shared-not-genesis.

QUOTE[TBWTT-2:16]: Ils se sont répandus sur cet immense continent en divers groupes de recherche scientifique ENDQUOTE
QUOTE[TBWTT-2:21]: organisaient des concours pour désigner l’équipe de savants ayant créé l’animal le plus beau ou le plus intéressant ENDQUOTE
QUOTE[TBWTT-2:25]: Chaque équipe se mit au travail, nous pûmes comparer bientôt nos créations ENDQUOTE

- **GEN A** [GEN-WOH-1:26] one grammatical subject; only the plural 'Let us make'
- **ATR p** [ATRA-WOH-I:255, ATRA-WOH-I:260, ATRA-WOH-I:267] 'The womb-goddesses were assembled'; 'she nipped off fourteen pieces of clay' (14 ki-iṣ-ri ik-ta-ri-iṣ); 'seven and seven they fashioned: seven male'
- **SUM P** [ENM-WOH-1:54, ENM-WOH-1:57, ENM-WOH-1:82] an explicit making-contest between two makers: 'As for the form of mankind — whether it turns out fair or ill is in (my) hands' / 'I will counter-balance it' / 'let me, in turn, fashion (one) for you'
- Absent (read, nothing found): BER, ENO, JUB, QUR, OTH

Analysis: Contest between makers is in Enki and Ninmah; plural birth-goddesses and a plural first batch are in Atrahasis. No text has geographically separate teams.

### D05 — Some teams make monsters; earlier human 'prototypes' are superseded

Episode: creation. Canon voice: Yahweh. Class: shared-not-genesis.

QUOTE[TBWTT-2:22]: d’autres équipes de savants créèrent des animaux épouvantables, des monstres ENDQUOTE
QUOTE[TBWTT-5:64]: les crânes des premiers prototypes d’homme qui furent supplantés par d’autres plus évolués ENDQUOTE

- **GEN p** [GEN-WOH-1:21] 'the great dragons' (ha-tanninim ha-gedolim) are among the creatures; no failed or superseded makes
- **SUM p** [ENM-WOH-1:59, ENM-WOH-1:88, ENM-WOH-1:101] defective humans made in the contest; Umul: 'not a living man, is not a [dead] man — he cannot sustain himself'
- **BER P** [CAG-3:13, CAG-3:15] 'most hideous beings ... creatures in which were combined the limbs of every species of animals'; they die and 'other men and animals' are formed
- Absent (read, nothing found): ATR, ENO, JUB, QUR, OTH

### D06 — Earlier creation attempts fail (destroyed on order; burned by a star's harmful rays; choked by vegetation); two other planets seeded

Episode: creation. Canon voice: Raël (LWTE ch. 2 exposition). Class: unique.

QUOTE[LWTE-2:11]: deux nouveaux échecs dus l'un à la trop grande proximité d'un astre dont les rayons nocifs brûlèrent leur création ENDQUOTE
QUOTE[LWTE-2:17]: les Elohim ont créé également la vie sur deux autres planètes à cette époque ENDQUOTE

- **BER p** [CAG-3:15] a first creation that dies of the light, then a second 'capable of bearing the air'
- Absent (read, nothing found): GEN, ATR, SUM, ENO, JUB, QUR, OTH

Analysis: Other planets: no parallel. The failed-first-creation shape has the Berossus partial only. The canon grounds the detail in Matthew 13, not in any primeval text.

### D07 — Man is made artificially, in laboratories, in the makers' image

Episode: creation. Canon voice: Yahweh; Raël. Class: genesis-has-it.

QUOTE[TBWTT-2:25]: voulurent créer un homme comme nous artificiellement ENDQUOTE
QUOTE[LWTE-2:6]: entièrement synthétiques dans les laboratoires de leur planète d'origine ENDQUOTE

- **GEN P** [GEN-WOH-1:26, GEN-WOH-2:7] image and likeness; formed 'dust from the ground' — the image motif is Genesis' own
- **ATR p** [ATRA-WOH-I:212, ATRA-WOH-I:213, ATRA-WOH-I:214, ATRA-WOH-I:215] substance not image: 'With the flesh of the god and (his) blood' ... 'so that god and man' / 'may be mixed together in the clay' (i-na ši-ir i-li ù da-mi ... i-lu-um-ma ù a-wi-lum)
- **SUM p** [ENM-WOH-1:28, ENM-WOH-1:133, SOTH-WOH-1:19] 'having drawn out from his own mind the form of his own being'; 'the human whose form is mine'; 'he placed the first of humankind in the brick-mould'
- **BER p** [CAG-3:15] divine blood mixed with earth: 'On this account it is that they are rational, and partake of divine knowledge'
- **QUR p** [QUR-15:28] a mortal from clay (my gloss of the Arabic)
- Absent (read, nothing found): ENO, JUB, OTH

Analysis: Laboratory, test-tube, chemicals: no ancient counterpart; every ancient text has clay/dust.

### D08 — Why man is made: the ablest makers want to make a being like themselves (no labor motive)

Episode: creation. Canon voice: Yahweh. Class: canon-contradicts-older.

QUOTE[TBWTT-2:25]: C’est alors que les plus habiles d’entre nous voulurent créer un homme comme nous artificiellement ENDQUOTE

- **GEN D** [GEN-WOH-1:26, GEN-WOH-2:15] to rule the animals; 'to work it and to guard it'
- **ATR C** [ATRA-WOH-I:195, ATRA-WOH-I:240] 'let man bear the labor of the gods' (a-wi-lum li-iš-ši du-ul-li i-li)
- **SUM C** [ENM-WOH-1:23, SOTH-WOH-1:31] 'fashion a substitute for the gods (?), so that they may be released from their toil'; 'took them up to provide rations for the gods'
- Absent (read, nothing found): BER, ENO, JUB, QUR, OTH

Analysis: The canon's creation motive is the opposite of the Mesopotamian labor anthropogony (core 0034).

### D09 — Humans supply food to the makers: offerings prompted by the exiles; after the Flood Noah pledges a share of crops and herds 'for their subsistence'

Episode: exile/flood. Canon voice: Yahweh. Class: shared-not-genesis.

QUOTE[TBWTT-2:48]: poussèrent les hommes à leur amener de la nourriture ENDQUOTE
QUOTE[TBWTT-2:64]: Noé s’engagea à verser une part de toutes les récoltes ou élevages aux créateurs pour leur subsistance ENDQUOTE

- **GEN p** [GEN-WOH-4:3, GEN-WOH-8:20, GEN-WOH-8:21] offerings exist; YHWH 'smelled the soothing aroma'; nothing about subsistence
- **ATR P** [ATRA-WOH-III:iv.18, ATRA-WOH-III:iv.19, ATRA-WOH-III:v.42] without mankind 'The Anunna, the great gods, sat in thirst and hunger' (uš-bu i-na ṣú-mi ù bu-bu-ti); 'like flies they gathered over the offering'
- **GIL P** [GILG-WOH-11:159] 'The gods gathered like flies around the (lord-of-the-)sacrifice' (ilānu kīma zumbī eli bēl niqê ip-taḫ-ru)
- **SUM P** [SOTH-WOH-1:31, ENM-WOH-1:8, FLS-WOH-D:11] people 'to provide rations for the gods' (diĝir-re-e-ne-ra šukur2-še3 mu-un-dab5-be2)
- **BER p** [CAG-3:18] altar and sacrifices
- **OTH p** [THEO-535] the Mekone division of the ox between gods and men
- Absent (read, nothing found): ENO, JUB, QUR

Analysis: The makers' material dependence on human produce is a Mesopotamian idea that Genesis has reduced to an aroma. In the canon it is a post-exile and post-Flood arrangement, not the purpose of creation (D08).

### D10 — The home world objects to the making of man and fears he will surpass his makers; man must be kept ignorant

Episode: creation. Canon voice: Yahweh; Raël. Class: shared-not-genesis.

QUOTE[TBWTT-2:25]: Ils craignaient que ces hommes soient un danger pour eux si leurs capacités ou leurs pouvoirs s’avéraient supérieurs à ceux de leurs créateurs ENDQUOTE
QUOTE[LWTE-2:18]: à la condition qu'ils ne créent pas d'êtres à leur image ENDQUOTE

- **GEN p** [GEN-WOH-3:22, GEN-WOH-11:6] divine alarm at human parity is in Genesis ('has become like one of us'; 'nothing will be withheld from them') but nobody objects to the creation itself
- **ATR C** [ATRA-WOH-I:220] unanimous approval
- **SUM p** [ADP-WOH-B:50] Anu: 'Why did Ea reveal (the things) of heaven and earth to a son of humankind?'
- **JUB p** [JUB-WOH-10:8] Mastema: 'great is the wickedness of the sons of men'
- **QUR P** [QUR-2:30, QUR-7:12, QUR-17:62] the angels object before the creation: a-tajʿalu fīhā man yufsidu fīhā wa-yasfiku d-dimāʾ (“will you place in it one who will work corruption in it and shed blood?” — my gloss); Iblīs refuses to bow
- **OTH p** [THEO-563] Zeus 'would not give the might of unwearying fire' to mortal men
- Absent (read, nothing found): BER, ENO

Analysis: An objection from within the heavenly assembly, made before or at the creation of man, on the ground that man will be violent: Quran 2:30. Not in Genesis, not in Mesopotamia.

### D11 — Satan is one of the Elohim, head of the party that expects only evil from man; he is later licensed to test humans

Episode: creation/exile. Canon voice: Yahweh; Raël. Class: shared-not-genesis.

QUOTE[TBWTT-3:251]: l’un d’entre eux nommé Satan, fait partie de ceux qui ont toujours condamné la création d’autres êtres intelligents ENDQUOTE
QUOTE[LWTE-2:19]: Satan pensait qu'il ne fallait rien attendre de bon de ces créatures fabriquées en laboratoire ENDQUOTE
QUOTE[LWTE-2:30]: l'on confie à Satan le soin de tester les prophètes ENDQUOTE

- **GEN A** no Satan in Genesis; the canon takes him from Job 1 (TBWTT-3:250)
- **ATR p** [ATRA-WOH-II:i.6] Enlil is the god hostile to mankind, but he is the ruler, not an opposition
- **GIL p** [GILG-WOH-11:166] Enlil
- **ENO p** [1ENO-65:6] 'the violence of the Satans' (plural class)
- **JUB P** [JUB-WOH-10:8, JUB-17:10, JUB-18:7] Mastema, 'chief of the spirits', negotiates before God for licence over mankind; proposes the test of Abraham ('bid him offer him as a burnt-offering ... and Thou wilt know if he is faithful'); 'was put to shame'
- **QUR P** [QUR-15:36, QUR-15:37, QUR-15:39, QUR-38:82] Iblīs asks for and is granted respite and announces he will mislead them all (my gloss)
- Absent (read, nothing found): SUM, BER, OTH

Analysis: The licensed adversary who doubts man and tests him is Second Temple and Qur'anic. Jubilees puts the Satan-figure behind the Abraham test; the canon's own Abraham paragraph (TBWTT-2:89) names only 'les créateurs'.

### D12 — The makers teach the first man the names and properties of plants and animals

Episode: eden. Canon voice: Yahweh. Class: shared-not-genesis.

QUOTE[TBWTT-2:32]: Les créateurs lui apprirent le nom et les pouvoirs de tout ce qui vivait autour de lui ENDQUOTE

- **GEN C** [GEN-WOH-2:19] the man does the naming: 'brought them to the human to see what he would call them'
- **BER p** [CAG-3:12] Oannes 'gave them an insight into letters and sciences ... made them distinguish the seeds of the earth'
- **JUB p** [JUB-WOH-3:15] 'we gave him work, and we taught him to do everything that was fitting to be done'
- **QUR P** [QUR-2:31] wa-ʿallama Ādama l-asmāʾa kullahā (“and He taught Adam the names, all of them” — my gloss)
- Absent (read, nothing found): ATR, SUM, ENO, OTH

Analysis: The canon quotes Genesis 2:19 and then states the reverse of it; the reversal matches Quran 2:31 and, more loosely, Jubilees 3:15.

### D13 — The prohibition concerns scientific knowledge (books)

Episode: eden. Canon voice: Yahweh. Class: genesis-has-it.

QUOTE[TBWTT-2:30]: ne touche pas aux livres scientifiques sinon tu mourrais ENDQUOTE

- **GEN P** [GEN-WOH-2:17] tree of knowing good and bad
- **SUM p** [ADP-WOH-A:10] 'Wisdom he gave him; eternal life he did not give him' (ne-me-qa id-din-šu napišta dāriti ul id-din-šu)
- **ENO p** [1ENO-32:4] 'the tree of wisdom' (v. 6, inside library refId 1ENO-32:4)
- Absent (read, nothing found): ATR, BER, JUB, QUR, OTH

Analysis: Books: no ancient counterpart in the library (core 0072 records the Sendy parallel).

### D14 — The 'serpent' is a small group of the makers themselves who, out of love for the humans, tell them the truth

Episode: eden. Canon voice: Yahweh; Raël. Class: shared-not-genesis.

QUOTE[TBWTT-2:35]: quelques-uns qui aimaient profondément leurs petits hommes ENDQUOTE
QUOTE[TBWTT-2:39]: Le «serpent», ce petit groupe de créateurs qui avait voulu apprendre la vérité à Adam et Ève ENDQUOTE
QUOTE[LWTE-2:22]: révéler à ces êtres qu'ils ne sont pas des «dieux» mais des hommes comme eux ENDQUOTE

- **GEN D** [GEN-WOH-3:1, GEN-WOH-3:5, GEN-WOH-3:22] the serpent is 'shrewder than any wild animal of the field'; its statement is confirmed by 3:22
- **ATR p** [ATRA-WOH-II:vii.1, ATRA-WOH-II:vii.2, ATRA-WOH-III:vi.17] a member of the assembly sides with mankind against it: 'he kept thwarting the work of Enlil'; 'I did it, indeed, against your will!'
- **GIL p** [GILG-WOH-11:189] 'the secret of the gods he heard'
- **SUM p** [ADP-WOH-B:50] a god reveals 'heaven and earth' to a human and the high god objects
- **ENO p** [1ENO-69:4, ENO-WOH-9:6, 1ENO-64:1] the tempter of Eve is one of the angels: Gâdreêl — 'he led astray Eve' (v. 6, inside library refId 1ENO-69:4); Asael 'revealed the mysteries of the age that are in heaven' — valued as sin
- **JUB D** [JUB-WOH-3:17] serpent, as Genesis
- **QUR p** [QUR-7:20, QUR-18:50] the tempter is Iblīs/the Shayṭān, a member of the heavenly assembly, not an animal — valued as enemy
- **OTH p** [THEO-565, THEO-566, THEO-614] 'kindly Prometheus' steals fire for men, deceiving Zeus (κλέψας ἀκαμάτοιο πυρὸς τηλέσκοπον αὐγήν)
- Absent (read, nothing found): BER

Analysis: Two separable features. (a) The tempter belongs to the heavenly company: 1 Enoch 69, Quran — negative valence. (b) A member of the divine company benefits mankind against the ruling decision: Ea, Prometheus — positive valence. The canon has (a)'s identity with (b)'s valence. No library text has both.

### D15 — The disclosing group is sentenced by the home government to live on Earth; the other makers must leave

Episode: eden/exile. Canon voice: Yahweh; Raël. Class: shared-not-genesis.

QUOTE[TBWTT-2:39]: était condamné par le gouvernement de la planète originelle à vivre sur Terre en exil tandis que les autres créateurs devaient stopper leurs expériences et quitter la Terre ENDQUOTE
QUOTE[LWTE-2:24]: Yahvé condamne les scientifiques qui ont désobéi à ses ordres à vivre en exil sur la Terre ENDQUOTE

- **GEN D** [GEN-WOH-3:14] 'on your belly you shall go' — an animal's curse
- **ENO p** [ENO-WOH-10:12, ENO-WOH-12:4, ENO-WOH-15:8] Watchers 'who have abandoned the high heaven' are bound 'in the valleys of the earth' (εἰς τὰς νάπας τῆς γῆς); the offence is the unions, not a disclosure in Eden
- **JUB p** [JUB-WOH-5:6] 'he removed them from all their stations; and he commanded us to bind them in the depths of the earth'
- **QUR p** [QUR-7:24, QUR-2:36] ihbiṭū ... wa-lakum fī l-arḍi mustaqarrun (“go down ... on the earth you shall have a dwelling for a time” — my gloss), plural address after the tempter's act
- **OTH p** [THEO-521, THEO-717, THEO-732] Prometheus bound; Titans 'beneath the wide-wayed earth ... no way out'
- Absent (read, nothing found): ATR, GIL, SUM, BER

Analysis: Confinement to the Earth of a heavenly group is Enochic; in Enoch it is imprisonment under the earth with no return, in the canon residence on it with later pardon (D39).

### D16 — Longevity is a technique ('tree of life'); the exiles obtain it for the chiefs of the first humans, hence the patriarchs' ages; it is not hereditary

Episode: eden. Canon voice: Yahweh. Class: shared-not-genesis.

QUOTE[TBWTT-2:49]: Ils obtinrent ainsi qu’on fasse bénéficier les chefs de ces premiers hommes de «l’arbre de vie» ENDQUOTE
QUOTE[TBWTT-2:53]: La longévité n’est pas héréditaire ENDQUOTE

- **GEN C** [GEN-WOH-3:22, GEN-WOH-3:24, GEN-WOH-5:5, GEN-WOH-6:3] the tree of life is barred to man; the long lives are stated without cause; the 120-year limit is present
- **GIL p** [GILG-WOH-11:196, GILG-WOH-11:285] godlike life is conferred on one man by decision of the gods; a plant is named 'The Old Man is Made Young!'
- **SUM p** [SKL-4, SKL-38, FLS-WOH-E:7, ADP-WOH-B:51] the huge spans belong to rulers: 'he ruled for 28800 years' (mu 28800 i3-ak); 'Life like (that of) a god they gave him'; Anu orders 'the food of life' for Adapa
- **BER p** [CAG-3:19] Xisuthrus 'translated to live with the gods'
- **ENO p** [ENO-WOH-10:9, ENO-WOH-10:10] the sons of the Watchers hope for long life: 'length of days shall not be theirs'
- **JUB D** [JUB-WOH-4:30] Adam dies within the thousand-year 'day'
- **QUR D** [QUR-20:120] the tempter offers “the tree of immortality” (shajarat al-khuld — my gloss)
- Absent (read, nothing found): ATR, OTH

Analysis: Longevity as something the gods can confer on selected men, and antediluvian longevity attached to rulers, are Mesopotamian. Genesis says the opposite about the tree.

### D17 — The 'sons of Elohim' who take human daughters are the exiled makers; the children are exceptional

Episode: unions. Canon voice: Yahweh. Class: genesis-has-it.

QUOTE[TBWTT-2:51]: Les créateurs en exil prirent aux hommes leurs filles les plus belles et en firent leurs femmes ENDQUOTE
QUOTE[TBWTT-2:55]: en avoir des enfants exceptionnels ENDQUOTE

- **GEN P** [GEN-WOH-6:2, GEN-WOH-6:4] unions and 'the mighty ones who were from of old, men of name'; who the sons of the Elohim are is not said
- **ENO P** [ENO-WOH-6:2, ENO-WOH-6:6, ENO-WOH-7:2, ENO-WOH-7:4] a named, numbered group of Watchers, 'in all two hundred'; the offspring are giants who 'devoured mankind'
- **JUB P** [JUB-WOH-4:10, JUB-WOH-5:1, JUB-WOH-7:22] the Watchers first 'descended upon the earth ... that they might instruct the sons of men'; the offspring destroy one another
- **OTH p** [THEO-967, THEO-968] goddesses with mortal men 'bore children like to the gods'
- Absent (read, nothing found): ATR, SUM, BER, QUR

Analysis: Genesis has the unions. What the canon adds — the fathers are a specific group already under sentence on Earth — is the Enochic identification with the order reversed: in Enoch the union is the offence and the sentence follows; in the canon the sentence comes first. The canon values the children positively, Enoch and Jubilees negatively.

### D18 — The exiles' sons hand weapons to human women; men slaughter each other with them; this bloodshed is the case for destruction

Episode: unions. Canon voice: Raël (LWTE ch. 2); absent from TBWTT (1974). Class: shared-not-genesis.

QUOTE[LWTE-2:25]: avec les armes qui leur sont données par les fils des Elohim bannis, du groupe de Lucifer ENDQUOTE
QUOTE[LWTE-2:25]: qui parviennent à se faire remettre par eux des armes en échange de leurs charmes ENDQUOTE

- **GEN A** [GEN-WOH-6:11, GEN-WOH-4:22] 'the land was filled with violence' with no source named; metal cutting-tools come from a human, Tuval-Cain
- **ENO P** [ENO-WOH-8:1, 1ENO-69:4, 1ENO-88:1, ENO-WOH-8:3, ENO-WOH-16:3, ENO-WOH-9:1] 'Asael taught men to make swords and knives and shields and breastplates' (ואסאל אלף לאנשא למעבד סיפין וסכינין); Gâdreêl showed 'all the weapons of death to the children of men' (v. 6, inside refId 1ENO-69:4); a sword is handed to the giants (v. 2, inside 1ENO-88:1); knowledge passes through the wives ('this you made known to the women'); 'much blood that was shed upon the earth'
- **JUB p** [JUB-WOH-7:22] 'they would destroy one another'
- Absent (read, nothing found): ATR, SUM, BER, QUR, OTH

Analysis: The closest single match in the register, and it is in the 1979 book only. 1 Enoch 69:6 gives one figure both roles the canon gives the Lucifer group: leading Eve astray and arming mankind.

### D19 — An accuser lays the evidence before the Council; the president decides

Episode: flood. Canon voice: Raël (LWTE ch. 2). Class: shared-not-genesis.

QUOTE[LWTE-2:26]: Devant les preuves ramenées par Satan devant le conseil des Eternels d'un tel carnage, Yahvé décide de faire ce que demande Satan ENDQUOTE

- **GEN A** [GEN-WOH-6:5] YHWH sees for himself
- **ATR p** [ATRA-WOH-II:vi.1, ATRA-WOH-II:vii.5, ATRA-WOH-II:viii.2] Enlil 'convened his assembly'; 'Anu and Enlil made all the gods swear'
- **GIL p** [GILG-WOH-11:14, GILG-WOH-11:15] 'the great gods' hearts were moved to bring on a flood. Their father Anu bound them by oath'
- **SUM p** [FLS-WOH-C:24] 'the word of the [assembly cannot be revoked]' (restored)
- **ENO P** [ENO-WOH-9:1, ENO-WOH-9:3, ENO-WOH-9:9, ENO-WOH-10:1] four heavenly beings bring the case — bloodshed, the unions, the revealed mysteries — before the Most High, who then rules
- Absent (read, nothing found): BER, JUB, QUR, OTH

Analysis: Assembly decision: Mesopotamian (already in core 0010). Accusation-then-ruling before a presiding figure: 1 Enoch 9–10, where the accusers are the loyal archangels, not a Satan.

### D20 — Why the destruction: (TBWTT) human scientific progress, the wish to equal the makers; (LWTE) human violence

Episode: flood. Canon voice: Yahweh (TBWTT); Raël (LWTE). Class: shared-not-genesis.

QUOTE[TBWTT-2:55]: Le progrès scientifique était énorme sur Terre et ils décidèrent de supprimer leur création ENDQUOTE
QUOTE[TBWTT-2:57]: Le mal, c’est-à-dire le désir de devenir un peuple égal à ses créateurs, un peuple scientifique et indépendant ENDQUOTE
QUOTE[LWTE-2:25]: car il les juge dangereux en raison de leur violence ENDQUOTE

- **GEN D** [GEN-WOH-6:5, GEN-WOH-6:11, GEN-WOH-6:13] wickedness and violence — agrees with the LWTE motive, not the TBWTT one
- **ATR C** [ATRA-WOH-II:i.6, ATRA-WOH-II:vii.5] noise of a multiplied humankind: 'The noise of humankind has grown burdensome to me' (ik-ta-ab-ta ri-gi-im a-wi-lu-ti)
- **GIL A** [GILG-WOH-11:14] no reason given
- **SUM A** [FLS-WOH-C:23] not preserved
- **BER A** [CAG-3:17] no reason given
- **ENO P** [1ENO-65:6, ENO-WOH-10:7, ENO-WOH-9:9] knowledge motive: 'their ruin is accomplished because they have learnt all the secrets of the angels'; violence motive also present
- **JUB D** [JUB-WOH-5:4] corruption of all flesh
- **QUR D** [QUR-11:37] wrongdoing, unbelief
- Absent (read, nothing found): OTH

Analysis: The TBWTT motive (illicit knowledge) has one ancient counterpart in the library, 1 Enoch 65:6. The two canon books give different motives; the later one is the Genesis/Enoch violence motive.

### D21 — The decision is taken on the distant home planet

Episode: flood. Canon voice: Yahweh. Class: weak.

QUOTE[TBWTT-2:58]: Ils décidèrent donc, de leur lointaine planète, de détruire toute vie sur la Terre en envoyant des missiles nucléaires ENDQUOTE

- **GEN p** [GEN-WOH-6:7] a decision by the deity; no place
- **ATR p** [ATRA-WOH-I:13, ATRA-WOH-II:vi.1] 'Anu went up to the heavens'; the assembly
- **GIL C** [GILG-WOH-11:13, GILG-WOH-11:112] the gods who decide dwell in Shuruppak ('the gods (dwelt) within it', ilānu qerbu-šu) and flee 'up to the heaven of Anu' when it comes
- **ENO p** [ENO-WOH-10:1] the Most High, from heaven
- Absent (read, nothing found): SUM, BER, JUB, QUR, OTH

Analysis: Not a discriminating detail: every text puts the decision with the higher gods.

### D22 — The means: explosions; a tidal wave over the single continent; a sudden cataclysm, not prolonged rain; fallout afterwards

Episode: flood. Canon voice: Yahweh; Raël (LWTE-1 Q&A). Class: shared-not-genesis.

QUOTE[TBWTT-2:58]: Le continent fut immergé par un immense raz-de-marée qui détruisit toute vie à sa surface ENDQUOTE
QUOTE[LWTE-1:48]: le déluge n'était pas le résultat d'une pluie continuelle comme on se le représente généralement ENDQUOTE

- **GEN D** [GEN-WOH-7:11, GEN-WOH-7:17] forty days of rain and 'all the fountains of the great deep burst open'
- **ATR p** [ATRA-WOH-III:iii.7, ATRA-WOH-III:iii.9, ATRA-WOH-III:v.34] 'He shattered the land like a pot'; 'like a battle'; seven days
- **GIL p** [GILG-WOH-11:101, GILG-WOH-11:102, GILG-WOH-11:105, GILG-WOH-11:108] 'The Anunnaki raised up their torches; with their bright radiance they set the land ablaze' (ina nam-ri-ri-šu-nu uḫam-ma-ṭu mātu); 'The land was shattered like a pot'; 'Like a battle it came over the people'
- **SUM p** [FLS-WOH-D:1, FLS-WOH-D:3] storms 'stood together as one'; seven days and nights
- **ENO p** [1ENO-65:1] 'the earth that it had sunk down'; 'shaken' (vv. 1, 3)
- **JUB D** [JUB-WOH-5:25] rain, deeps
- **QUR D** [QUR-54:11, QUR-54:12] sky-water and springs
- Absent (read, nothing found): BER, OTH

Analysis: A short, violent, fire-accompanied, battle-like event is the Mesopotamian picture; missiles and fallout have no counterpart. The canon nevertheless keeps Genesis' 150 days (TBWTT-2:61), which the seven-day texts contradict.

### D23 — The survivor is warned by the dissident (exiled) makers, against the intent of those who decided — not by the destroyer

Episode: flood. Canon voice: Yahweh; Raël. Class: shared-not-genesis.

QUOTE[TBWTT-2:58]: Mais les exilés, prévenus de la chose, avaient demandé à Noé de construire une fusée ENDQUOTE
QUOTE[LWTE-2:27]: Mais ces derniers apprennent que toute leur fantastique création va être détruite. Ils ne peuvent admettre cela ENDQUOTE

- **GEN C** [GEN-WOH-6:13, GEN-WOH-6:14, GEN-WOH-7:1] the destroyer himself warns and instructs: 'I am about to destroy them ... Make for yourself an ark'
- **ATR P** [ATRA-WOH-II:viii.3, ATRA-WOH-III:i.13, ATRA-WOH-III:vi.17, ATRA-WOH-III:vi.18, ATRA-WOH-III:ii.15] Ea is under the oath and still warns: 'Dismantle the house, build a boat!' (ú-qú-ur bi-ta bi-ni e-le-ep-pa); 'I did it, indeed, against your will! I saw to it that life was preserved' (aš-šum na-ap-ša-tim uš-te-ṣi); 'Enki and Enlil have grown angry with each other'
- **GIL P** [GILG-WOH-11:19, GILG-WOH-11:24, GILG-WOH-11:175, GILG-WOH-11:188] 'Prince Ea was with them, bound by the (same) oath'; 'Who but Ea could (have) devise(d) this matter?'; 'I did not (myself) reveal the secret of the great gods'
- **SUM p** [FLS-WOH-C:8, FLS-WOH-C:20, FLS-WOH-C:24] 'Enki took counsel in his own heart'; the side-wall speech (speaker lost in the break)
- **BER p** [CAG-3:17] 'The deity Cronos appeared to him in a vision, and warned him' — one god, no dissent stated
- **ENO C** [ENO-WOH-10:1, ENO-WOH-10:2, 1ENO-67:1, 1ENO-89:1] the Most High sends the warning; the Watchers are the ones condemned
- **JUB C** [JUB-WOH-5:21] 'he commanded Noah to make for himself an ark'
- **QUR C** [QUR-11:37] God commands the ship
- Absent (read, nothing found): OTH

Analysis: The strongest item. The canon's structure (decision by one party, warning by another against it) is the Atrahasis/Gilgamesh structure and is the reverse of Genesis, 1 Enoch, Jubilees and the Quran. In the Mesopotamian texts the warner is a full member of the deciding assembly; in the canon he is a group already expelled from it.

### D24 — The exiles help build the vessel

Episode: flood. Canon voice: Raël (LWTE); TBWTT-2:58 has only 'avaient demandé à Noé de construire'. Class: weak.

QUOTE[LWTE-2:27]: Noé qu'ils aident à construire un vaisseau spatial ENDQUOTE

- **GEN A** [GEN-WOH-6:14] Noah builds
- **ATR A** [ATRA-WOH-III:ii.10] the man builds
- **GIL C** [GILG-WOH-11:49, GILG-WOH-11:50] human craftsmen
- **ENO p** [1ENO-67:1] 'the angels are making a wooden (building)' (v. 2, inside refId 1ENO-67:1) — loyal angels, on God's order
- **QUR p** [QUR-11:37] built “under our eyes and our inspiration” (bi-aʿyuninā wa-waḥyinā — my gloss)
- Absent (read, nothing found): SUM, BER, JUB, OTH

### D25 — The vessel is a rocket that orbits the Earth; life is kept some thousands of kilometres up; 'above the earth and not on the waters'

Episode: flood. Canon voice: Yahweh; Raël. Class: unique-and-contradicted.

QUOTE[TBWTT-2:58]: une fusée qui devait tourner autour de la Terre durant le cataclysme ENDQUOTE
QUOTE[TBWTT-2:58]: la vie était préservée à quelques milliers de kilomètres au-dessus de la Terre ENDQUOTE
QUOTE[TBWTT-2:60]: il est bien dit qu’elle s’éleva audessus de la Terre et non pas sur les eaux ENDQUOTE
QUOTE[LWTE-1:48]: c'était le seul vaisseau... spatial ENDQUOTE

- **GEN C** [GEN-WOH-7:17, GEN-WOH-7:18, GEN-WOH-8:4] 7:17 has the quoted phrase with its cause — 'the waters increased and lifted up the ark, and it rose above the land' (וַתָּרָם מֵעַל הָאָרֶץ) — and 7:18 continues 'the ark went on the face of the waters' (וַתֵּלֶךְ הַתֵּבָה עַל־פְּנֵי הַמָּיִם); it grounds on Ararat
- **ATR C** [ATRA-WOH-III:i.21, ATRA-WOH-III:ii.33] pitch; 'he cut the mooring-rope and set the boat adrift'
- **GIL C** [GILG-WOH-11:61, GILG-WOH-11:76, GILG-WOH-11:138] punt-poles; launched 'until two-thirds of her had entered the water'; 'On Mount Nimush the boat came to rest'
- **SUM C** [FLS-WOH-D:5] 'the great boat had been tossed by the destructive storms on the great waters'
- **BER C** [CAG-3:17, CAG-3:20] 'trust himself fearlessly to the deep'; stranded in Armenia, bitumen scraped off
- **ENO C** [1ENO-67:1, 1ENO-89:1] 'a wooden (building)'; 'a great vessel ... covered in'
- **JUB C** [JUB-WOH-5:28] rests on Mount Lubar
- **QUR C** [QUR-11:42, QUR-54:13] wa-hiya tajrī bihim fī mawjin ka-l-jibāl (“it ran with them amid waves like mountains”); “a thing of planks and nails” (my glosses)
- Absent (read, nothing found): OTH

Analysis: No library text has a vessel that leaves the Earth; every one that describes it has a boat on water. The canon's proof-text is the first half of Genesis 7:17; the same verse names the waters as what lifts the ark and the next verse puts it on them. Loose congruences only: sealed and roofed 'like the Apsû, so that Shamash may not see within her' (ATRA-WOH-III:i.17–18); the destination 'To the Gods' (CAG-3:17); Enoch lifted to 'a tower raised high above the earth' to watch (1ENO-87:3).

### D26 — What is preserved is a living cell, male and female, of each species; the animals are re-created from them afterwards

Episode: flood. Canon voice: Yahweh; Raël. Class: shared-not-genesis.

QUOTE[TBWTT-2:58]: il suffit d’avoir une cellule vivante de chaque espèce, mâle et femelle, pour reconstituer ensuite l’être tout entier ENDQUOTE
QUOTE[TBWTT-2:68]: chaque animal fut recréé à partir de la cellule préservée dans l’arche ENDQUOTE
QUOTE[LWTE-2:27]: certaines espèces animales dont l'on conserve le code génétique ENDQUOTE

- **GEN p** [GEN-WOH-6:19, GEN-WOH-7:3] living animals, 'two of each'. Purpose clause: 'to keep seed alive' (לְחַיּוֹת זֶרַע)
- **ATR p** [ATRA-WOH-III:ii.19, ATRA-WOH-III:ii.20] flocks, cattle, birds, beasts
- **GIL P** [GILG-WOH-11:27, GILG-WOH-11:80, GILG-WOH-11:82] 'Bring aboard the seed of all living things into the boat' (šūli-ma zēr napšāti kalāma ana libbi eleppi) — and also the animals themselves
- **SUM p** [FLS-WOH-E:10] 'for preserving the small animals and the seed of humankind' (numun nam-lu2-ulu3)
- **BER p** [CAG-3:17] 'all the different animals'
- **ENO p** [1ENO-67:1, ENO-WOH-10:3] 'there shall come forth from it the seed of life' (v. 2, inside refId 1ENO-67:1)
- **QUR p** [QUR-11:40] min kullin zawjayni thnayn (“of each, a pair, two” — my gloss)
- **OTH p** [VID-2:27, VID-2:28] the vara is stocked with taoxma ('seed') of men, cattle, plants and foods, in pairs (mithwaire) — Avestan only in the library; gloss mine, unverified
- Absent (read, nothing found): JUB

Analysis: 'Seed' as the thing carried is a formula of the flood tradition (Gilgamesh XI 27, the Sumerian Flood Story, Vendidad 2) and survives in Genesis 7:3. The canon's 'cellule' reads that word biologically. Re-creation of whole animals from it: no counterpart.

### D27 — Aboard: Noah and one couple of each human race; each race is put back at its place of creation

Episode: flood. Canon voice: Yahweh. Class: unique-and-contradicted.

QUOTE[TBWTT-2:62]: Il y avait à l’intérieur outre Noé, un couple de chaque race humaine de la Terre ENDQUOTE
QUOTE[TBWTT-2:68]: Chaque race humaine fut replacée en son lieu de création ENDQUOTE

- **GEN C** [GEN-WOH-7:1, GEN-WOH-7:23, GEN-WOH-10:32] Noah's household only; the nations descend from his sons
- **ATR C** [ATRA-WOH-III:ii.21] 'His family'
- **GIL C** [GILG-WOH-11:81, GILG-WOH-11:82] family, kin 'and all the craftsmen'
- **BER C** [CAG-3:17] 'his wife, his children, and his friends'
- **ENO C** [1ENO-89:1] three with him
- **QUR C** [QUR-11:40] his household and the few who believed
- Absent (read, nothing found): SUM, JUB, OTH

### D28 — Noah was not believed and was mocked

Episode: flood. Canon voice: Yahweh (ETTMTTP). Class: shared-not-genesis.

QUOTE[ETTMTTP-3:234]: Autrefois Noé ne fut pas cru et les gens se moquaient de lui quand il se préparait pour la destruction ENDQUOTE

- **ATR p** [ATRA-WOH-III:ii.13, ATRA-WOH-III:ii.16] he addresses the elders with a cover story
- **GIL p** [GILG-WOH-11:34, GILG-WOH-11:35, GILG-WOH-11:39] 'But what shall I answer' / '(when) the city, the populace, and the elders (ask me)?'
- **QUR P** [QUR-11:38] wa-kullamā marra ʿalayhi malaʾun min qawmihi sakhirū minhu (“whenever chiefs of his people passed by him they mocked him” — my gloss)
- Absent (read, nothing found): GEN, SUM, BER, ENO, JUB, OTH

Analysis: A small clean case: not in Genesis, explicit in Quran 11:38.

### D29 — Those who ordered the destruction learn only afterwards that life survived, and are alarmed

Episode: flood. Canon voice: Yahweh (TBWTT); contradicted by LWTE-2:28. Class: shared-not-genesis.

QUOTE[TBWTT-2:74]: Ils observaient toujours la terre et s’étaient aperçus que la vie n’avait pas été détruite ENDQUOTE

- **GEN C** [GEN-WOH-8:1] 'The Elohim remembered Noah'
- **ATR P** [ATRA-WOH-III:vi.5, ATRA-WOH-III:vi.6, ATRA-WOH-III:vi.9, ATRA-WOH-III:vi.10] 'When Enlil saw the boat' / 'he was filled with fury at the Igigi' / 'Where did life escape?' (e-eš-ta uṣ-ṣí-a-am na-pí-iš-tum) / 'How did a man survive the catastrophe?'
- **GIL P** [GILG-WOH-11:169, GILG-WOH-11:171, GILG-WOH-11:172] 'Has anyone (here) come out alive? No man was to have survived the destruction!'
- Absent (read, nothing found): BER, ENO, JUB, QUR, OTH

Analysis: In the Mesopotamian texts the discovery is immediate, at the sacrifice; in TBWTT it comes at the Babel episode.

### D30 — The makers promise never again to destroy mankind; the reason

Episode: flood. Canon voice: Yahweh; Raël. Class: genesis-has-it.

QUOTE[TBWTT-2:66]: promirent de ne jamais essayer de les détruire à l’avenir, car ils avaient compris qu’il était normal qu’ils veuillent faire des progrès ENDQUOTE
QUOTE[LWTE-2:28]: C'est alors que les Elohim s'aperçoivent qu'ils ont été eux-mêmes créés de la même manière qu'ils ont créé les hommes ENDQUOTE
QUOTE[LWTE-2:28]: Ils décident alors que plus jamais ils n'essaieront de détruire l'humanité ENDQUOTE

- **GEN P** [GEN-WOH-8:21, GEN-WOH-9:11] 'I will not again strike down every living thing' — reason: 'the inclination of the heart of the human is evil from his youth'
- **ATR p** [ATRA-WOH-III:v.47, ATRA-WOH-III:vi.21, ATRA-WOH-III:vi.22] reproach ('without deliberating'), and lesser instruments 'Instead of your bringing on a flood'
- **GIL p** [GILG-WOH-11:163, GILG-WOH-11:184] 'These days let me remember — for ever, let me not forget!'
- **SUM p** [FLS-WOH-E:1, FLS-WOH-E:2] an oath 'by the life of heaven and the life of earth'
- **ENO P** [ENO-WOH-10:22] 'I will not again send wrath and plague upon it'
- **JUB p** [JUB-WOH-5:32] covenant memorial
- Absent (read, nothing found): BER, QUR, OTH

Analysis: The promise is Genesis'. Both canon reasons are the canon's own: 'progress is normal' re-glosses Genesis 8:21; the discovery that the Elohim were themselves made (LWTE) has no counterpart.

### D31 — The Elohim are themselves created beings (message in an automatic vessel from their own makers)

Episode: flood. Canon voice: Raël (LWTE). Class: unique.

QUOTE[LWTE-2:28]: le message que contenait le vaisseau automatique en provenance du monde des créateurs des Elohim ENDQUOTE

- **OTH p** [EE-1:9, THEO-1] typological only: gods are themselves generated (theogony) — births, not manufacture by an earlier civilisation
- Absent (read, nothing found): GEN, ATR, GIL, SUM, BER, ENO, JUB, QUR

### D32 — Not every species is re-established after the Flood (the great reptiles are left out); geology and coastlines are rewritten

Episode: flood. Canon voice: Marcel Terrusse, guide (LWTE ch. 4). Class: unique.

QUOTE[LWTE-4:54]: certaines, considérées comme monstrueuses ou nuisibles pour le maintien de l'équilibre écologique, ne furent pas réimplantées ENDQUOTE
QUOTE[LWTE-4:49]: ils retrouvèrent des continents complètement ravagés par les destructions, méconnaissables ENDQUOTE

- **GEN C** [GEN-WOH-6:19] 'Of every living thing'
- **GIL p** [GILG-WOH-11:136] '(the world had become) the edge of the sea'
- **BER p** [CAG-3:15] the monstrous first creatures do not survive into the second creation — at the creation, not the flood
- **ENO p** [ENO-WOH-10:9] the giants are destroyed
- Absent (read, nothing found): ATR, SUM, JUB, QUR, OTH

### D33 — The tower is a vehicle for reaching the makers' world, built by the most advanced people with the exiles' help

Episode: babel. Canon voice: Yahweh. Class: shared-not-genesis.

QUOTE[TBWTT-2:72]: il entreprit bientôt de se lancer dans la conquête de l’espace, aidé par les créateurs exilés ENDQUOTE
QUOTE[TBWTT-2:72]: Ils construisirent donc une immense fusée : la Tour de Babel ENDQUOTE

- **GEN p** [GEN-WOH-11:4] 'a tower with its top in the skies'; stated aim: a name, and not to be scattered
- **BER P** [CAG-3:34, CAG-3:28] the Sibyl: 'a large and lofty tower, that they might climb up into heaven'; 'when it approached the heaven'
- **JUB P** [JUB-WOH-10:19] 'Let us ascend by it into heaven' (wa-yəbēlu nəʿrəg bottu samāya)
- Absent (read, nothing found): ENO, QUR, OTH

Analysis: Ascent into heaven as the stated purpose is explicit in Jubilees and the Sibylline fragment, only implied in Genesis. Divine helpers in the building: no text.

### D34 — The purpose is to obtain the exiles' pardon by showing mankind grateful and peaceful

Episode: babel. Canon voice: Yahweh. Class: shared-not-genesis.

QUOTE[TBWTT-2:72]: Ces derniers voulaient que les hommes aillent sur la planète des créateurs afin d’obtenir leur pardon en montrant que les hommes étaient intelligents et scientifiques mais reconnaissants et pacifiques ENDQUOTE

- **GEN D** [GEN-WOH-11:4] 'let us make for ourselves a name'
- **BER C** [CAG-3:28] 'glorying in their own strength and size and despising the gods'
- **ENO p** [ENO-WOH-13:4, ENO-WOH-13:6, ENO-WOH-14:3, ENO-WOH-16:4] a different episode with the same shape: the condemned Watchers ask a man to carry 'a memorial of petition for them, that they might find forgiveness' before the Lord of heaven (ἵνα γένηται αὐτοῖς ἄφεσις); he is borne up into heaven; the answer is 'There shall be no peace for you'
- **JUB C** [JUB-WOH-10:18] 'evil purpose'
- Absent (read, nothing found): QUR, OTH

Analysis: No Babel text has a pardon motive; those that state a motive state defiance. The pardon-petition-carried-to-heaven shape exists in 1 Enoch 13–16, attached to the Watchers before the Flood, with the opposite outcome.

### D35 — The home world is alarmed, comes, removes the most learned and scatters them among peoples whose languages already differ, and destroys the equipment

Episode: babel. Canon voice: Yahweh. Class: shared-not-genesis.

QUOTE[TBWTT-2:74]: Les gens de la planète eurent peur en apprenant la chose ENDQUOTE
QUOTE[TBWTT-2:76]: les dispersèrent sur tout le continent, dans des peuplades primitives, dans des pays où aucun ne pouvait se faire comprendre car le langage y était différent et ils détruisirent les appareillages scientifiques ENDQUOTE

- **GEN p** [GEN-WOH-11:6, GEN-WOH-11:7, GEN-WOH-11:8, GEN-WOH-10:5] alarm and scattering present; the one language is itself confounded (the canon has languages that already differ); the building merely stops; Genesis 10:5 already has nations 'each by his tongue'
- **BER P** [CAG-3:28, CAG-3:34, CAG-9:264] destruction: 'the winds assisted the gods, and overthrew the work upon its contrivers'; the cuneiform fragment printed by Smith: 'he confounded their speech'
- **JUB P** [JUB-WOH-10:26, JUB-WOH-10:23] 'the Lord sent forth a great wind against the tower, and overthrew it upon the earth'; 'we descended with him'
- Absent (read, nothing found): ENO, QUR, OTH

Analysis: Physical destruction of the structure is in Jubilees and the Berossus/Sibyl fragments, not in Genesis. The canon's pre-existing language diversity agrees with Genesis 10 against Genesis 11 and against all the Babel parallels.

### D36 — The exiles are then pardoned, return home and plead for mankind

Episode: babel. Canon voice: Yahweh (TBWTT: after Babel); Raël (LWTE: amnesty offered before the Flood). Class: canon-contradicts-older.

QUOTE[TBWTT-2:78]: Les créateurs exilés furent pardonnés et eurent le droit de revenir sur leur planète d’origine où ils plaidèrent la cause de leur magnifique création ENDQUOTE
QUOTE[LWTE-2:26]: en permettant à l'équipe de Lucifer de revenir sur la planète des Elohim en les amnistiant de leur condamnation à l'exil ENDQUOTE

- **ATR p** [ATRA-WOH-III:vi.17] Enki is never expelled; he answers for himself in the assembly
- **GIL p** [GILG-WOH-11:190] Ea prevails: 'take counsel for him'
- **ENO C** [ENO-WOH-12:5, ENO-WOH-13:2, ENO-WOH-16:4] 'There shall be no peace for them upon the earth, nor any forgiveness of sins'
- **JUB C** [JUB-WOH-5:6] 'bound there until the day of the great judgment'
- **QUR C** [QUR-15:37] respite, not pardon
- **OTH C** [THEO-732] 'For them there is no way out'
- Absent (read, nothing found): GEN, SUM, BER

Analysis: Every tradition that has a confined heavenly group denies it release. The two canon books date the amnesty differently.

### D37 — Three roles: the one who presses for destruction (Satan), the president who decides (Yahweh), the faction that saves (Lucifer's group); Yahweh is also one of the makers

Episode: structure. Canon voice: Yahweh; Raël. Class: shared-not-genesis.

QUOTE[TBWTT-2:24]: Je suis l’un de ceux qui ont créé la vie sur la Terre ENDQUOTE
QUOTE[LWTE-2:26]: Yahvé décide de faire ce que demande Satan ENDQUOTE
QUOTE[LWTE-2:22]: désobéissant aux ordres de Yahvé, le président du conseil des Eternels ENDQUOTE

- **GEN C** [GEN-WOH-6:7, GEN-WOH-6:13, GEN-WOH-8:21] one subject decides, warns, saves and promises
- **ATR P** [ATRA-WOH-I:7, ATRA-WOH-I:8, ATRA-WOH-II:vii.5, ATRA-WOH-II:viii.2, ATRA-WOH-III:vi.18] Anu the king who administers the oath; Enlil who proposes the flood; Enki who preserves life
- **GIL P** [GILG-WOH-11:15, GILG-WOH-11:16, GILG-WOH-11:19] 'Their father Anu bound them by oath, their counsellor — the warrior Enlil ... Prince Ea was with them'
- **SUM p** [FLS-WOH-C:9, FLS-WOH-C:25] An, Enlil, Enki, Ninhursaĝa
- **ENO p** [ENO-WOH-9:1, ENO-WOH-10:1] accusers, judge; no saving faction
- Absent (read, nothing found): BER, JUB, QUR, OTH

Analysis: A role-structure observation only. It is not a per-figure identification, which core 0002 and 0008 exclude. In Mesopotamia the maker of man (Enki) and the destroyer (Enlil) are different gods; in LWTE the destroyer-president is himself a maker (TBWTT-2:24).


## The shared-but-not-in-Genesis details, strongest first, with the competing explanations

For every item four explanations compete. They are listed once here and then referred to by letter.

- **E1 — French-language availability.** The canon drew on knowledge of these texts or of popular retellings in circulation in France by 1973. The only part of this that the project has verified is core claim 0072: Jean Sendy's books, inspected in French, share with the first Message the serpent grounded on Earth, Babel as a launch site and a deliberate technological Flood. That French translations or popular accounts of Atrahasis, Gilgamesh XI, 1 Enoch and Jubilees were available to a general reader by 1973 is [outside knowledge — unverified, needs source].
- **E2 — common interpretive tradition.** The detail is ordinary post-biblical Genesis lore (catechism, sermon, apocrypha, Quran), reachable without any ancient Near Eastern text. That a given item was commonplace in French Catholic culture is [outside knowledge — unverified, needs source].
- **E3 — convergent rationalisation.** Any reading that splits "Elohim" into a distant authority and a local faction, and keeps Genesis' plot, generates the detail by itself.
- **E4 — the canon's own claim.** The older texts and the canon report the same events, and the older texts kept what Genesis dropped (TBWTT-2:3, TBWTT-5:54).

| Rank | Detail | Where | What each explanation has to carry | What would discriminate |
|---|---|---|---|---|
| 1 | D23 dissident warns the survivor | ATR, GIL (P); GEN, ENO, JUB, QUR (C) | E3 is strong: the split premise forces it. E1 needs a route to Gilgamesh XI. E2 fails (the tradition has the destroyer warn). E4 has to explain why the warner is an insider there and an exile here. | Whether Sendy has a dissident warner (the 0072 map says his "factional structure differs"). |
| 2 | D29 deciders discover survival afterwards | ATR, GIL (P); GEN (C) | Not forced by the premise, so E3 is weak. E1 or E4. | Same check in Sendy and in French popular accounts of the Deluge tablet. LWTE-2:28 drops the detail, which E4 must also explain. |
| 3 | D18 arming of mankind through the women | ENO (P); GEN (A) | E1 or E2 (Enochic lore), or E4. E3 fails: nothing forces weapons or women. Appears only in 1979. | What Enochic material was in French print between 1974 and 1979; whether the detail is in Sendy. |
| 4 | D09 makers fed by human produce | ATR, GIL, SUM (P); GEN (p) | E3 partly (physical beings must eat). E1/E4 otherwise. | Whether the motive is stated in the precursor literature. |
| 5 | D20 Flood because of forbidden knowledge | ENO 65:6 (P); GEN (D); ATR (C) | E3 is strong: it follows from reading "evil" as "science" (TBWTT-2:57). | Low discriminating power. |
| 6 | D19 accusation before a presiding figure | ENO (P); ATR, GIL (p) | E2 is strong: the canon builds Satan from Job 1 (TBWTT-3:250). | Low. |
| 7 | D15 heavenly group confined to Earth | ENO, JUB, QUR, OTH (p) | E1 is documented for Sendy (0072). E2 (fallen angels) is also available. | Already under study in 0072. |
| 8 | D14 the discloser is one of the makers and is benevolent | ENO, QUR (identity); ATR, SUM, OTH (valence) | E3 (Genesis 3:22 confirms the serpent). E2 for the identity half. | Low. |
| 9 | D10, D11, D12, D28 the Qur'anic cluster | QUR, JUB (P) | E2 suffices. TBWTT-5:54 names "Islamique" among its witnesses. | None needed. |
| 10 | D33, D35 ascent and demolition at Babel | JUB, BER (P) | E2 or E3 (a rocket implies both). | Low. |
| 11 | D04, D05 contest and failed makes | SUM, BER (P/p) | E3 (a laboratory implies trial and error; 0072 records the same in Sendy). | Low. |
| 12 | D16 conferred longevity, attached to rulers | SUM, GIL (p) | E3 (needed to explain Genesis 5). | Low. |
| 13 | D26 seed | GIL, SUM, OTH (P/p); GEN (p) | Genesis 7:3 suffices. | None. |
| 14 | D22 sudden fiery cataclysm | GIL, ATR (p) | E3 (a nuclear strike is sudden). | Low. |
| 15 | D37 three roles | ATR, GIL (P) | Follows from D23 plus the Job-derived Satan. | Low. |
| 16 | D34 pardon petition carried to heaven | ENO 13–16 (p, other episode, opposite outcome) | Shape only. | Low. |

Pattern (b). Two items resist the cheap explanations: D29 and D18. D29 is Mesopotamian and in the 1974 book. D18 is Enochic and in the 1979 book only. Everything else in the list is either forced by the canon's own premise (E3) or is common post-biblical lore (E2). The record supports neither dependence nor independence. It shows where a test would have purchase.

## Where the canon contradicts the older texts

| Detail | Canon | Older texts |
|---|---|---|
| D25 the vessel | leaves the Earth and orbits (TBWTT-2:58, 2:60) | a boat on water in GEN 7:18, ATR, GIL, FLS, BER, ENO, JUB, QUR |
| D27 the passengers | a couple of each race (TBWTT-2:62) | one household, with kin and craftsmen in GIL |
| D08 purpose of man | the makers' ambition (TBWTT-2:25) | labor for the gods (ATR, ENM, SOTH) |
| D01, D10 reception of the project | forbidden, then conditional (TBWTT-2:2; LWTE-2:18) | acclaimed in assembly (ATRA-WOH-I:220) |
| D20 Flood motive | progress (TBWTT) | noise and numbers (ATRA-WOH-II:i.6); wickedness (GEN) |
| D36 fate of the confined group | pardoned (TBWTT-2:78) | never released (ENO, JUB, QUR, THEO) |
| D17 the offspring | exceptional (TBWTT-2:55) | devouring giants (ENO-WOH-7:4) |
| D17 order of sentence and unions | sentence, then unions | unions, then sentence (ENO, JUB) |
| D35 languages | already different (TBWTT-2:76) | one, then confounded (GEN 11, JUB, BER) |
| D22 duration | 150 days, following Genesis (TBWTT-2:61) | seven days (ATR, GIL, FLS) |
| D16 tree of life | given to the chiefs (TBWTT-2:49) | barred (GEN-WOH-3:22–24) |
| D12 naming | the makers teach the names (TBWTT-2:32) | Adam names (GEN-WOH-2:19) |

## Details with no ancient counterpart in the library

Home-world prohibition and emigration (D01); discovery rather than making of the Earth (D02); the continent raised by explosions and its later break-up (D03); earlier attempts on other planets and two other seeded worlds (D06); laboratory, test-tube and chemicals (D07); one team per human race (TBWTT-2:25) and Israel chosen by a scientific jury (TBWTT-2:43); nuclear missiles and fallout (D22); the orbiting vessel (D25); a couple of each race aboard and each race returned to its place of creation (D27); re-creation of animals from cells (D26); the Elohim as themselves created, with a message from their makers (D31); the dinosaurs deliberately not restored (D32); helpers from the exiled group at Babel and the pardon motive there (D33, D34); the pardon and return of the exiles (D36).

## Tensions and null results

- **Null: the canon's narrative never uses Enoch.** Genesis 5:24 (GEN-WOH-5:24) is not cited in TBWTT ch. 2. No Watcher name, Hermon, the number two hundred or the giants' size appears anywhere in the three books.
- **Null: no Mesopotamian name or text in TBWTT or ETTMTTP.** The only mentions are Terrusse's at LWTE-4:105 and 4:108.
- **Null: the slain god.** The Atrahasis and Berossus motif of a god killed and his blood mixed into man (ATRA-WOH-I:223–225; CAG-3:15) has no counterpart in the canon.
- **Null: the survivor's apotheosis.** Utnapishtim, Ziusudra and Xisuthrus are given the gods' life or taken to live with them (GILG-WOH-11:196; FLS-WOH-E:7–8; CAG-3:19). The canon's Noah is not.
- **Null: graded earlier punishments.** Atrahasis has plague and famine before the Flood (ATRA-WOH-II:i.8, II:iii.7). The canon has none.
- **Counter-example to finding 2:** Jubilees gives the Watchers a legitimate first mission — they came "that they might instruct the sons of men" (JUB-WOH-4:10). That is closer to the canon's makers than 1 Enoch is, and it weakens any claim that the canon tracks 1 Enoch specifically.
- **Canon-internal:** the Babel builders are already Israel and "the Jews", before Abraham appears at TBWTT-2:89. QUOTE[TBWTT-2:72]: le peuple le plus intelligent, le peuple d’Israël ENDQUOTE QUOTE[TBWTT-2:76]: prirent les Juifs qui avaient le plus de connaissances scientifiques ENDQUOTE
- **Canon-internal, outside this question but adjacent:** LWTE-1:47 dates the real Flood to about five thousand years ago. QUOTE[LWTE-1:47]: datant d'environ cinq mille ans, ce qui correspondrait à la période du «déluge » réel ENDQUOTE Core 0019 dates the antediluvian span to c. 11,375–6,690 BCE. I have not checked how 0003 reconciles these.
- **Voice:** LWTE-4:40–56 (continental break-up, species not restored) is Terrusse's essay, not Yahweh's or Raël's voice. D03 (second half) and D32 rest on it.

## Relation to existing core records

- **woh-claim-0010 (flood-as-reset).** The evidence map's procedural table has "Warned survivor with instructions" as present in all four texts. This note adds the distinction that matters for the canon: *who* warns. Mesopotamia has the dissenter; Genesis and the Watchers have the destroyer. It also adds D29, D09 and D22 with locators, and the contradiction at D25. The map cites "TBWTT ch. 2" for the craft; the proof-text problem at GEN-WOH-7:17–18 is not recorded there. The map says its feature wordings "should be re-verified against the in-house renderings"; the register does that for the Mesopotamian side.
- **woh-claim-0008 (council-serpentine-conflict).** Supports the record's own internal objection: the canon gives episodes, and the two books disagree on their linkage (amnesty before the Flood in LWTE, after Babel in TBWTT). Adds the three-role observation (D37) as structure only. The record's Hebrew-memory layer has no Enochic rows; D14, D15, D18 and D19 would supply them, with the valence reversal noted.
- **woh-claim-0012 (watchers-nephilim-unions).** The record already states that the canon's unions and the Enochic descent are separate stories mapped by the framework. This note adds two specifics for that objection: the reversed order of sentence and union (D17), and the reversed valuation of the offspring. It adds the positive correspondences the record does not list: arming, transmission through the women, accusation before the presiding figure (D18, D19) — all from LWTE, not from "TBWTT ch. 2", which is the only canon locator the map gives. The record's scope refuses to read the forbidden-arts catalogue as a technology inventory; LWTE-2:25 itself singles out weapons, and that is canon text, not corpus inference.
- **woh-claim-0034 (labor-anthropogony).** D08: the canon's stated creation motive is not labor. D09: the provisioning relationship is in the canon, after the exile and after the Flood. The record's "Sumerian texts, currently held at metadata_only" can be raised: `enki-and-ninmah-woh` and `song-of-the-hoe-woh` are in the library and were read in full here (ENM-WOH-1:9, 1:23, 1:30, 1:37; SOTH-WOH-1:19, 1:31).
- **woh-claim-0017 (babel-pardon-expedition).** The pardon motive is canon-explicit at TBWTT-2:72, not inferred. What is unsupported is any ancient attestation of it: the Babel parallels state defiance. Jubilees and the Sibylline fragment supply ascent and demolition (D33, D35).
- **woh-claim-0002 (anunnaki-elohim-identity).** The matrix supplies the "shared features and important mismatches" that the record's step 4 asks for, at collective level only. The mismatches (D01, D08, D10, D20, D25) are as numerous as the matches (D09, D23, D29, D37).
- **woh-claim-0072 (Sendy comparison).** Three of the items here (serpent grounded, Babel launch, technological Flood) are already documented there with a verified French precursor. This note did not inspect Sendy.

## Candidate claims or revisions for founder review

Proposals only.

1. **0017 evidence map:** regrade the pardon motive from "inferred" to canon-explicit with locator TBWTT-2:72, and move the "inferred" label to the reading of Genesis 11. Add a row: no ancient Babel text attests the motive; CAG-3:28 and JUB-WOH-10:18 state the contrary.
2. **0010 evidence map:** split "Warned survivor" into "warned by the decider" (Genesis, Watchers, Jubilees, Quran) and "warned by a dissenter under oath" (Atrahasis, Gilgamesh XI); add rows for D29, D09 and for the D25 contradiction with GEN-WOH-7:17–18.
3. **0012 evidence map:** add LWTE-2:25–27 as canon locators; add rows for the order reversal and the offspring valuation; add 1ENO-69:4 (v. 6).
4. **0034:** record that the canon does not state the labor motive (TBWTT-2:25) and that its provisioning passages are TBWTT-2:48 and 2:64; raise the Sumerian source notes from metadata_only to project_digitization.
5. **0008:** record the TBWTT/LWTE discrepancies of finding 6 as canonical-context complications (the record lists "canonical-context failure of the systematization" as a revision trigger).
6. **Possible new research question (not a claim):** "Which primeval details enter the canon only in 1979?" The LWTE additions are the Satan/Lucifer names and parties, the arming through women, the accusation before the Council, the violence motive, the pre-Flood amnesty and the created-creators discovery.
7. **Library housekeeping (not core):** the `eridu-genesis` slug holds Langdon's 1915 *Sumerian Epic of Paradise, the Flood, and the Fall of Man*, which is a reading of the Enki and Ninhursag tablet, not the text now called the Eridu Genesis (that is `flood-story-woh`).

## Open questions and what would discriminate

- Do Sendy's books (held and inspected for 0072) contain D29, D18 or D09? A yes moves those items to E1 with a verified source. A no leaves E1 resting on unverified availability.
- What was in French print on 1 Enoch between 1974 and 1979, and did Raël or his circle cite it? [outside knowledge — unverified, needs source]. Terrusse's list at LWTE-4:102–108 shows the circle knew the titles by 1979.
- Is there any canon detail that matches an ancient text unpublished or untranslated in 1973? None was found in this register. Finding one would be the strongest evidence against E1; its absence is not evidence for E1.
- Does the canon reproduce any error or peculiarity of a specific modern translation? Not tested; it needs the French editions.

## Limitations

- The library's Akkadian, Sumerian, Aramaic/Greek Enoch and Ge'ez Jubilees originals are marked best-effort reconstructions pending collation. Original-language snippets are quoted as the library gives them; one (ADP-WOH-B:50) looks unreliable and only its English is used.
- Gilgamesh is held for Tablet XI only. Enuma Elish is King's 1902 text in broken OCR; the Tablet VI anthropogony is not usable. `book-of-enoch-woh` covers chapters 1–36 and 72–82; the Parables, Dream Visions and Noah fragments come from Charles 1917, whose refIds group several verses. `jubilees-woh` covers chapters 1–12.
- The Quran and Vendidad are held without English. Glosses of the Arabic and Avestan are mine and are marked; the Avestan gloss in particular is unverified.
- Berossus, the Sibyl and the Babel fragment are read through Smith's 1876 book, an obsolete edition.
- The rest of the Hebrew Bible was not searched systematically. The canon itself brings Job 1 into the primeval story (TBWTT-3:250).
- Sendy and all other modern precursors were not inspected.
- "Absent" means not found in the library holding as read, not absent from the tradition.
- The partial/contrary grades are judgments. The register gives the wording so that each can be re-graded.
