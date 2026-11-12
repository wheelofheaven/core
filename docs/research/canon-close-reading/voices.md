---
title: "Canon close reading: who is speaking"
status: draft
version: 0.1.0
last_reviewed: 2026-11-12
---

# Voices and modes of transmission in Raël's three books (key: `voices`)

## Exact question

Who is actually speaking in each paragraph of the three books, how does the text itself mark the change of voice and the mode of transmission, and where do the speaker tags in the project's library data disagree with the text?

## Method

- Source of record: the French dumps `texts/{TBWTT,ETTMTTP,LWTE}.fr.txt` (2,070 paragraphs: 759 + 475 + 836). The English dumps were used only as a reading aid.
- Every paragraph received one voice label from textual signals only: guillemets and dashes, inquits (*me dit-il*, *Iahvé parla*), person reference (who is *je*, *nous*, *vous*, *tu*), section headings, footnote markers, bylines.
- Reading coverage: TBWTT ch. 1, 2, 7 and all chapter boundaries read in full; TBWTT ch. 3–6 read by paragraph openings plus a signal scan of every paragraph. ETTMTTP ch. 1 read by paragraph head and tail, ch. 2 read in full, ch. 3 read by paragraph openings with all person-shift paragraphs in full. LWTE ch. 1 and 3 read by head and tail; ch. 2 read in full for 2:1–2:105 and 2:226–2:235, the Apocalypse commentary 2:106–2:225 by openings plus pronoun scan; ch. 4 by openings and all bylines. Where a paragraph was read only by its opening, a voice shift in the unread middle could have been missed (see Limitations).
- Scripture quotations were separated mechanically (paragraph is wholly a quotation, or a bare reference line, or the tail of a quotation split over several paragraphs) and then spot-checked. Mixed paragraphs (speech plus narration in one paragraph) were given their dominant voice and flagged.
- Word counts are whitespace token counts of the French. A mixed paragraph counts wholly toward its dominant voice, so the per-voice word totals are accurate to roughly ±1 %.
- Layers are kept apart below: **(a) text** = what the paragraph says; **(b) analysis** = my counts and inferences; **(c) open** = what would discriminate.
- Helpers and the per-paragraph register: `agent-voices/build.py`, `voices.json`.

Voice codes: **Y** Yahweh speech · **YQ** scripture read out inside Yahweh speech · **E** other Eloha (Satan) · **RN** Raël narration · **RS** Raël's own lines in dialogue · **RC** Raël commentary in his own name · **RI** the "Les Clés" text presented as inspired writing · **SQ** scripture or other quotation inside Raël/Clés text · **ED** editorial (headings, caption, footnotes, addresses, third-person chapter introductions) · **C** signed contributor · **O** reported speech of others (robot, interviewers, a quoted author).

## Findings (ranked)

### 1. "Les Clés" speaks as a created human, not as Yahweh; the library tags 258 of its 266 paragraphs `Yahweh`

(a) Text. The frame is a single paragraph at the end of ch. 2:

QUOTE[ETTMTTP-2:132]: je me mis à écrire en observant tout ce que j'écrivais et en le découvrant comme un lecteur. J'écrivais mais je ne me sentais pas l'auteur de ce qui apparaissait sur le papier. Les Elohim commençaient à… ENDQUOTE

The sentence breaks off on an ellipsis; it does not say what the Elohim were beginning to do. Inside ch. 3 the Elohim are in the third person and the speaker counts himself among their creatures:

QUOTE[ETTMTTP-3:5]: - par rapport aux Elohim nos pères, nos créateurs ; ENDQUOTE
QUOTE[ETTMTTP-3:11]: les Elohim nous ont créés à leur image ENDQUOTE
QUOTE[ETTMTTP-3:15]: Même nos créateurs ne nous traitent pas en enfants mais en individus ENDQUOTE
QUOTE[ETTMTTP-3:194]: d'autres êtres plus avancés que nous ENDQUOTE
QUOTE[ETTMTTP-3:205]: ce que nous sommes : de pauvres primitifs bornés. ENDQUOTE
QUOTE[ETTMTTP-3:219]: lorsqu'ils comprirent qu'ils avaient été créés comme nous, ils se mirent à nous aimer comme leurs propres enfants ENDQUOTE
QUOTE[ETTMTTP-3:253]: les Elohim, nos créateurs, nous aiment, nous leurs enfants ENDQUOTE

(b) Analysis. 36 paragraphs of ch. 3 carry an explicit human-"we" marker of this kind; the word *Elohim* occurs 59 times in the chapter, always as a third party except in two paragraphs (finding 2). The data tag `Yahweh` therefore names a speaker the grammar excludes. The chapter is 14,297 words, 42.7 % of the book; as currently tagged, 65 % of the book's words carry the `Yahweh` tag; by this study's reading Yahweh speech is 22 %.

(c) Open. See the for/against table in "Analysis of Les Clés" below.

### 2. Inside "Les Clés" the first person shifts three ways

(a) Text. *Je* is Raël in three paragraphs:

QUOTE[ETTMTTP-3:174]: De nombreux médiums sont venus me voir en me demandant ce qu'ils devaient faire ENDQUOTE
QUOTE[ETTMTTP-3:175]: J'attends avec impatience que tous les médiums qui ont reçu l'ordre de se mettre en rapport avec moi le fassent ENDQUOTE
QUOTE[ETTMTTP-3:208]: Qui croient en ce qui m'a été révélé et en ce qui a été révélé avant moi ENDQUOTE

Elsewhere Raël is a third person (QUOTE[ETTMTTP-3:257]: Raël existe, il est bien vivant ENDQUOTE). In two paragraphs *nous/notre* is the Elohim:

QUOTE[ETTMTTP-3:241]: Respectez notre prophète et ne portez pas de jugement sur ses actions et sur ses paroles, car nous entendons par ses oreilles, nous voyons par ses yeux et nous parlons par sa bouche. ENDQUOTE
QUOTE[ETTMTTP-3:259]: ce sont les conseils de tes créateurs, transmis par la bouche de Raël, notre ambassadeur ENDQUOTE

The second follows directly on a human-"we" sentence: QUOTE[ETTMTTP-3:258]: il est l'ambassadeur des Elohim, nos créateurs, nos pères qui sont dans les cieux. ENDQUOTE. Even 3:241 opens with the Elohim in the third person: QUOTE[ETTMTTP-3:241]: Vous qui croyez, ne portez pas de jugements sur les actions ou les paroles des Elohim. ENDQUOTE

(b) Analysis. Three stances coexist in one chapter: anonymous human "we" (dominant), Raël's "I" (3:174–175, 3:208, 3:264), Elohim "we" (3:241, 3:259; 3:69 *notre ambassade terrestre* is ambiguous). The shifts are unmarked: no dash, guillemet or inquit.

### 3. The first book narrates five sessions, while three passages say six

(a) Text. Return and departure frames in TBWTT: day 1 (1:1–1:64); then

QUOTE[TBWTT-2:1]: Le lendemain, j’étais au rendez-vous avec un cahier, un stylo et la Bible. ENDQUOTE
QUOTE[TBWTT-3:2]: Le lendemain je retrouvais mon interlocuteur, et il continua son récit : ENDQUOTE
QUOTE[TBWTT-4:118]: Et il repartit comme les fois précédentes. ENDQUOTE
QUOTE[TBWTT-5:2]: Le lendemain il revint comme les fois précédentes et il parla. ENDQUOTE
QUOTE[TBWTT-5:68]: Et il repartit comme les autres matins. ENDQUOTE
QUOTE[TBWTT-6:1]: Le lendemain je le rencontrai de nouveau et il parla. ENDQUOTE
QUOTE[TBWTT-7:2]: Avant que nous nous quittions pour la dernière fois avez-vous des questions à me poser ? ENDQUOTE

There is no frame between ch. 3 and ch. 4 (3:304 is a Zechariah quotation, 3:305 a caption, 4:1 a heading, 4:2 continues the exposition) and none between ch. 6 and ch. 7 (6:29 ends the instructions, 7:1 is a heading, 7:2 continues in the same speech). The guillemets agree: the speech opened at 2:2 closes at 2:91; the next closing guillemet is at 4:117; the speech opened at 6:2 closes at 7:71. The count stated by the text:

QUOTE[TBWTT-7:16]: Nous nous sommes rencontrés six jours de suite ENDQUOTE
QUOTE[TBWTT-7:76]: on ne peut pas rêver six jours de suite ni inventer tout cela. ENDQUOTE
QUOTE[ETTMTTP-2:10]: Le même engin que j'avais vu à six reprises au mois de décembre 1973 ENDQUOTE

and a fourth passage that, read literally, makes seven (first meeting plus six):

QUOTE[ETTMTTP-1:63]: l'Eloha (au pluriel Elohim) que je devais revoir six jours de suite au même endroit et qui, à chaque fois pendant une heure environ, me dicta Le Livre qui dit la Vérité ENDQUOTE

(b) Analysis. Four *Le lendemain* frames after 13 December give five narrated mornings: ch. 1 · ch. 2 · ch. 3–4 · ch. 5 · ch. 6–7. The digitised text asserts six and shows five.

(c) Open. Either a session frame was never written, or one was lost in a later edition or in digitisation. A first-edition (1974) copy checked at the ch. 3/4 and ch. 6/7 joins would discriminate. I did not check one.

### 4. The canon describes four different modes of transmission, and the fourth has no reception scene

(a) Text.
1. Notes during speech (TBWTT): QUOTE[TBWTT-1:63]: Revenez demain avec la Bible, à la même heure, et amenez de quoi prendre des notes. ENDQUOTE · QUOTE[TBWTT-7:80]: ce livre que j’ai écrit en essayant de reproduire le plus fidèlement possible tout ce qui m’a été dit ENDQUOTE · QUOTE[ETTMTTP-1:64]: Je mis tout d'abord au propre les notes que j'avais prises le mieux possible, mais beaucoup trop vite pendant que mon interlocuteur parlait. ENDQUOTE
2. Memory fixed by a technical means, written afterwards (ETTMTTP ch. 2): QUOTE[ETTMTTP-2:22]: Vous n'avez rien pour prendre des notes, mais n'ayez pas peur, tout ce que je vais vous dire restera gravé dans votre esprit ENDQUOTE · QUOTE[ETTMTTP-2:131]: Les mots étaient restés comme gravés dans mon esprit, comme cela m'avait été annoncé au commencement. ENDQUOTE
3. Writing without feeling himself the author (ETTMTTP ch. 3): 2:132, quoted above.
4. Speech "through the mouth" with no scene (LWTE 2:94–2:235): QUOTE[LWTE-2:95]: Moi Yahvé, par la bouche de mon prophète Raël, je m'adresse aux hommes de la Terre. ENDQUOTE

The second book itself reports a transcription error in the first: QUOTE[ETTMTTP-2:23]: il faut rectifier un passage du message que vous avez mal retranscrit ENDQUOTE

(b) Analysis. "Dictation" is the text's own word for mode 1 only (ETTMTTP-1:63 *me dicta*; ETTMTTP-2:22 *celui que je vous ai dicté en décembre 1973*). Mode 4 is announced in advance at ETTMTTP-2:98 (*nous parlerons par votre bouche*) but LWTE gives no date, place or manner for the 4,685-word message.

### 5. Yahweh's "tu" appears once, in LWTE, and nothing in the three books contradicts the stated switch

(a) Text. QUOTE[LWTE-2:85]: Cessant subitement de me vouvoyer comme il l'avait toujours fait lorsqu'il s'adressait à moi, il dit: – Celui que tu prenais pour ton père n'était pas ton père. ENDQUOTE

(b) Analysis. Every Yahweh-to-Raël address in TBWTT and in ETTMTTP ch. 2 is *vous* (null result for *tu*; details in section "Address forms"). After the switch no further Yahweh-to-Raël address exists anywhere in the three books, so the statement is uncontradicted but also untested.

### 6. ETTMTTP ch. 2 has six paragraphs tagged `Yahweh` that are narration, Raël's reply, or a robot

2:70, 2:74, 2:77 are narration; 2:76 is Raël's answer; 2:93 is the robot guide. Details and quotes in the data-fix list.

### 7. LWTE contains two Eloha speakers, six signed contributors and an unsigned third-person editor, all tagged `Narrator`

Satan speaks 11 paragraphs (749 words) in 2:59–2:73. Ch. 4 has six named authors; one of them (Yvan Giroux, 4:148–4:176) is easy to miss because his byline is fused into a heading paragraph in the middle of what looks like Terrusse's second essay.

### 8. Later-edition layers are visible in all three books

Post-1998 footnotes are fused into the running text of LWTE at five places, including the middle of Satan's speech (2:60) and the middle of a narrative sentence (2:83). ETTMTTP carries 14 orphaned footnote markers on *MADECH1*. TBWTT names the movement *Mouvement Raélien* in a December 1973 speech, while ETTMTTP calls it MADECH in June–October 1975. Full list in section "Later-edition material".

## Counts per voice per book


**TBWTT** — 759 paragraphs, 29635 words

| Voice | Paragraphs | Words | % words |
|---|---:|---:|---:|
| Y — Yahweh-speech | 390 | 19886 | 67.1 |
| YQ — scripture-quotation (inside Yahweh speech) | 251 | 6988 | 23.6 |
| RN — Raël-narration | 18 | 1200 | 4.0 |
| RS — Raël-direct-speech (dialogue) | 55 | 509 | 1.7 |
| RC — Raël-commentary | 10 | 834 | 2.8 |
| ED — editorial (heading, caption, footnote, address, 3rd-person intro) | 35 | 218 | 0.7 |

**ETTMTTP** — 475 paragraphs, 33443 words

| Voice | Paragraphs | Words | % words |
|---|---:|---:|---:|
| Y — Yahweh-speech | 75 | 7472 | 22.3 |
| YQ — scripture-quotation (inside Yahweh speech) | 6 | 188 | 0.6 |
| RN — Raël-narration | 125 | 11428 | 34.2 |
| RS — Raël-direct-speech (dialogue) | 1 | 17 | 0.1 |
| RC — Raël-commentary | 2 | 65 | 0.2 |
| RI — Raël-inspired-writing (Les Clés) | 260 | 14105 | 42.2 |
| SQ — scripture/other quotation (inside Raël or Clés text) | 3 | 117 | 0.3 |
| ED — editorial (heading, caption, footnote, address, 3rd-person intro) | 1 | 10 | 0.0 |
| O — reported-speech-of-others | 2 | 41 | 0.1 |

**LWTE** — 836 paragraphs, 42026 words

| Voice | Paragraphs | Words | % words |
|---|---:|---:|---:|
| Y — Yahweh-speech | 65 | 3451 | 8.2 |
| YQ — scripture-quotation (inside Yahweh speech) | 81 | 1641 | 3.9 |
| E — other-Eloha-speech (Satan) | 11 | 749 | 1.8 |
| RN — Raël-narration | 12 | 836 | 2.0 |
| RS — Raël-direct-speech (dialogue) | 5 | 495 | 1.2 |
| RC — Raël-commentary | 278 | 21779 | 51.8 |
| SQ — scripture/other quotation (inside Raël or Clés text) | 23 | 781 | 1.9 |
| ED — editorial (heading, caption, footnote, address, 3rd-person intro) | 106 | 776 | 1.8 |
| C — contributor | 219 | 9606 | 22.9 |
| O — reported-speech-of-others | 36 | 1912 | 4.5 |

Contributors in LWTE ch. 4 (paragraphs / words): Marcel Terrusse 133 / 4,286 (two essays) · Yvan Giroux 29 / 1,744 · Victor Le Gendre 14 / 1,537 · Michel Beluet 17 / 968 · Michel Deydier 16 / 882 · Jean-Bernard Ndjoga-Awirondjogo 10 / 189.

Yahweh speech excluding the scripture he reads out: 67.4 % of TBWTT, 22.3 % of ETTMTTP, 8.2 % of LWTE. Including it: 90.7 %, 22.9 %, 12.1 %.

## Full register 1 — voice map by REF range

### TBWTT

| Range | Voice | Signal for the boundary |
|---|---|---|
| 1:1–1:6 | RN | First-person past narration; 1:6 ends *je lui demandai:* |
| 1:7–1:63 | RS / Y alternating, RN at 1:8, 1:14, 1:41 | Question-and-answer turns; inquit at 1:8; no dashes survive in the dump |
| 1:64 | RN | *Il me laissa redescendre* |
| 2:1 | RN | *Le lendemain* … *commença à parler.* |
| 2:2–2:91 | Y with YQ (48 Y, 38 YQ, 4 ED headings) | Opening guillemet at 2:2, closing at 2:91 |
| 2:92 | RN | *Le petit homme prit à nouveau congé de moi* |
| 3:1 | ED | Heading *Moïse* |
| 3:2 | RN + Y (mixed) | Narration up to the colon, then the speech begins in the same paragraph |
| 3:3–3:304 | Y with YQ (153 Y, 140 YQ, 9 ED headings) | No opening guillemet; no closing guillemet at chapter end |
| 3:305 | ED | Caption; Raël in third person |
| 4:1–4:117 | Y with YQ (67 Y, 45 YQ, 5 ED headings) | Continues ch. 3 without frame; closing guillemet at 4:117 |
| 4:118 | RN | *Et il repartit* |
| 5:1 | ED | Heading |
| 5:2 | RN | *Le lendemain il revint* |
| 5:3–5:67 | Y with YQ (34 Y, 24 YQ, 6 ED headings, 1 ED footnote 5:44) | Opening guillemet at 5:3; no closing guillemet at 5:67 |
| 5:68 | RN | *Et il repartit comme les autres matins.* |
| 6:1 | RN | *Le lendemain je le rencontrai de nouveau* |
| 6:2–6:29 | Y with YQ (22 Y, 4 YQ, 2 ED headings) | Opening guillemet at 6:2; none closing at 6:29 |
| 7:1–7:71 | Y / RS alternating (38 Y, 29 RS, 3 ED headings) | Same speech continues (7:2); closing guillemet at 7:71 |
| 7:72 | RN | *Alors le petit homme me salua pour la dernière fois* |
| 7:73 | ED | Heading *Mouvement Raélien* |
| 7:74–7:83 | RC | Address to readers in his own name (*À vous qui ne me croirez pas, je dis*) |

The speaker is never named in TBWTT. He identifies himself by office only (QUOTE[TBWTT-7:56]: Le plus âgé, le président du conseil des Éternels a vingtcinq mille ans et vous l’avez devant vous. ENDQUOTE). The name comes in the second book (QUOTE[ETTMTTP-2:61]: Mon guide, Iahvé s'interrompit un instant puis reprit : ENDQUOTE), so the `Yahweh` tag on TBWTT is a retrospective identification.

(b) Analysis of Yahweh's self-reference in TBWTT: of 392 non-quotation Yahweh paragraphs, 119 speak of *les créateurs* in the third person, 88 use *nous/notre/nos*, 15 do both. The explicit bridge is rare (QUOTE[TBWTT-3:284]: Nous les créateurs, ne voulons nous montrer officiellement ENDQUOTE).

### ETTMTTP

| Range | Voice | Signal |
|---|---|---|
| 1:1–1:77 | RN (1:41–1:45 are his own song lyric, quoted) | First-person autobiography and publication history |
| 2:1–2:10 | RN | 2:10 ends *et il parla :* |
| 2:11 | Y | Opening dash, closing guillemet |
| 2:12, 2:14–2:18, 2:20–2:21 | RN | Inquits *Mon guide … me dit alors :* |
| 2:13, 2:19 | Y | Quoted one-liners |
| 2:22–2:43 | Y | Guillemet opens 2:22, closes 2:43 |
| 2:44–2:49 | RN | *Je me levai et suivis mes trois guides.* |
| 2:50–2:60 | Y | Guillemets 2:50 … 2:60 |
| 2:61, 2:63, 2:65, 2:67–2:68 | RN | First naming of Iahvé at 2:61 |
| 2:62, 2:64, 2:66, 2:69 | Y | Guillemets |
| 2:70 | RN (tagged Yahweh) | *Il fit un signe à l'un des robots* … *Iahvé parla :* |
| 2:71, 2:73 | Y; 2:72 YQ | Ezekiel quotation inside |
| 2:74 | RN (tagged Yahweh) | *ce que j'avais vu* |
| 2:75 | Y | Question to Raël |
| 2:76 | RS (tagged Yahweh) | Opening dash, *ma mère* |
| 2:77 | RN (tagged Yahweh) | *Il me la montra* … *Iahvé me dit :* |
| 2:78, 2:80, 2:82–2:83 | Y | Guillemets |
| 2:79, 2:81, 2:84–2:85, 2:87–2:92, 2:94–2:95, 2:97 | RN | Narration |
| 2:86 | O (robot) | *demanda le robot* |
| 2:93 | O (robot; tagged Yahweh) | 2:92 ends *Mon robot me dit :* |
| 2:96, 2:98–2:129 | Y (2:106–2:109, 2:111 YQ: Qur'an, Matthew) | Guillemet opens 2:98, closes 2:129; contains rules in *tu* (2:116–2:120) and an address to Israel (2:122–2:128) |
| 2:130–2:132 | RN | Return, writing-up, and the frame for ch. 3 |
| 3:1–3:263 | RI (3:184, 3:232, 3:239 SQ; 3:120–3:132 a model prayer) | No quotation marks, no inquit, no headings in the dump |
| 3:264, 3:266 | RC | *écris-moi* |
| 3:265 | ED | Postal address |

### LWTE

| Range | Voice | Signal |
|---|---|---|
| 1:1 | ED | Raël in third person |
| 1:2–1:200 | O (questions, 29 ¶) / RC (answers, 163 ¶) / ED (7 headings) | *Question:* … *Réponse de Raël:* (1:5), then *Réponse:* |
| 1:201 | ED | Post-1998 footnote |
| 2:1–2:2 | ED | Raël in third person; *nous sommes en l'an 34 (1979)* |
| 2:3–2:57 | RC with SQ (34 RC, 21 SQ: Matthew, Job) | Impersonal exposition (*L'on sait que*) |
| 2:58 | RN | *A la fin de l'entretien que j'avais eu avec Yahvé* |
| 2:59–2:67 | E (Satan); 2:59 opens with narration | *il dit: –* |
| 2:68–2:70 | RS | *Je lui répondis : –* |
| 2:71, 2:73 | E | *me demanda mon interlocuteur* / *reprit-il* |
| 2:72, 2:74 | RS | Dashes |
| 2:75 | RN | *Yahvé apparut … Il me dit:* |
| 2:76 | Y | Dash; names Satan and Lucifer |
| 2:77–2:84 | RN (2:77 reports Satan indirectly) | |
| 2:85–2:88 | Y; 2:85 opens with narration | *il dit: –* ; switch to *tu* |
| 2:89–2:90 | RN | |
| 2:91–2:93 | RC | *Moi, Raël, je vous montre* |
| 2:94 | ED | Heading *Message de Yahvé aux hommes de la terre* |
| 2:95–2:235 | Y with YQ (60 Y / 3,044 w; 81 YQ / 1,641 w, Apocalypse) | *Moi Yahvé* opens (2:95) and closes (2:232) |
| 3:1–3:87 | RC (3:35–3:36 SQ; 3:47–3:53 O: Milgram quoted) | *Vous les Raëliens, si moi-même* |
| 3:88 | ED | Postal address |
| 4:1–4:79 | C — Marcel Terrusse | Byline in 4:1 |
| 4:80–4:93 | C — Victor Le Gendre | Byline 4:81–4:82 |
| 4:94–4:147 | C — Marcel Terrusse | Byline 4:95 |
| 4:148–4:176 | C — Yvan Giroux | Byline fused into 4:148 |
| 4:177–4:193 | C — Michel Beluet | Byline 4:177–4:179 |
| 4:194–4:203 | C — Jean-Bernard Ndjoga-Awirondjogo | Signature at the end, 4:203 |
| 4:204–4:219 | C — Michel Deydier | Byline 4:204; dateline 4:219 |
| 4:220–4:312 | ED | Address list of national movements |

Byline evidence:

QUOTE[LWTE-4:1]: par Marcel TERRUSSE, Ingénieur chimiste, Guide Raëlien. ENDQUOTE
QUOTE[LWTE-4:81]: Par Victor LE GENDRE, ENDQUOTE
QUOTE[LWTE-4:95]: Par Marcel TERRUSSE, Ingénieur chimiste, guide raëlien. ENDQUOTE
QUOTE[LWTE-4:148]: Par Yvan Giroux, ex-Prêtre catholique romain, ex-professeur de catéchèse, guide raëlien au Québec. ENDQUOTE
QUOTE[LWTE-4:177]: Par Michel BELUET, ENDQUOTE
QUOTE[LWTE-4:203]: Jean-Bernard NDJOGA-AWIRONDJOGO, Diplômé en sciences politiques, ex-Marxiste, Guide continental pour l'Afrique. ENDQUOTE
QUOTE[LWTE-4:204]: Par Michel DEYDIER, Psychologue, Guide raëlien. ENDQUOTE

## Full register 2 — data-fix list for the data-library maintainers

Conventions in the current data: `Yahweh` = the Eloha's speech; `Raël` = Raël's lines in dialogue; `Narrator` = Raël's narration and everything else. The proposals keep those three values where they suffice and name a new value only where none fits.

### A. Unambiguous fixes

| REF | Current | Proposed | Evidence |
|---|---|---|---|
| TBWTT-1:27 | Narrator | Raël | It is the answer to the question in 1:26 and continues at 1:29 |
| TBWTT-3:2 | Narrator | split: narration to the colon = Narrator; remainder = Yahweh | Speech begins after *il continua son récit :* |
| TBWTT-3:305 | Yahweh | editorial / caption (not speech) | Raël in third person; dated 1973 |
| TBWTT-5:44 | Yahweh | editorial / footnote | Asterisk keyed to 5:40 |
| ETTMTTP-2:70 | Yahweh | Narrator | Third-person narration of Yahweh's gesture; ends with an inquit |
| ETTMTTP-2:74 | Yahweh | Narrator | *ce que j'avais vu* |
| ETTMTTP-2:76 | Yahweh | Raël | Answers 2:75; *ma mère* |
| ETTMTTP-2:77 | Yahweh | Narrator | *Il me la montra* |
| ETTMTTP-2:86 | Narrator | other speaker: robot (with inquit) | *demanda le robot* |
| ETTMTTP-2:93 | Yahweh | other speaker: robot | Preceding paragraph ends *Mon robot me dit :* |
| ETTMTTP-3:1–3:4, 3:262 | Narrator | same value as 3:5–3:261 and 3:263, whatever that value is | 3:4 ends on a colon that 3:5 completes; 3:262 is one of a run of identical *Toi qui…* appeals (3:261, 3:262) |
| ETTMTTP-3:174, 3:175, 3:208 | Yahweh | Raël | *me voir*, *avec moi*, *ce qui m'a été révélé* |
| ETTMTTP-3:264 | Narrator | Raël | *écris-moi* |
| ETTMTTP-3:265 | Narrator | editorial / address | Postal address |
| LWTE-1:1, 2:1, 2:2 | Narrator | editorial (third-person introduction) | Raël named in third person |
| LWTE ch. 1 questions (29 ¶: 1:2–1:4, 1:13, 1:17, 1:20–1:21, 1:26, 1:30, 1:33, 1:35, 1:37, 1:39, 1:42, 1:45, 1:49, 1:56, 1:62, 1:71, 1:75, 1:83, 1:89, 1:104, 1:111, 1:142, 1:184, 1:189, 1:194, 1:197) | Narrator | other speaker: interviewer | *Question:*; Raël addressed as *vous* |
| LWTE ch. 1 answers (163 ¶) and ch. 3 (78 ¶) | Narrator | Raël | *Réponse de Raël:* |
| LWTE-2:59 | Narrator | split: narration to *il dit:* = Narrator; remainder = Satan | |
| LWTE-2:60–2:67, 2:71, 2:73 | Narrator | other Eloha: Satan (2:71 and 2:73 carry inquits) | Identified at 2:76 |
| LWTE-2:68–2:70, 2:72, 2:74 | Narrator | Raël | *Je lui répondis : –* |
| LWTE-2:76 | Narrator | Yahweh | *Il me dit: –* after *Yahvé apparut* |
| LWTE-2:85 | Narrator | split: narration to *il dit:* = Narrator; remainder = Yahweh | |
| LWTE-2:86–2:88 | Narrator | Yahweh | Continuation of the speech |
| LWTE-2:95–2:235 | Narrator | Yahweh (60 ¶ of speech; 81 ¶ are Apocalypse quotations read out, same treatment as the Bible quotations in TBWTT) | *Moi Yahvé* at 2:95, 2:128, 2:232 |
| LWTE-3:47–3:53 | Narrator | quotation (S. Milgram) | Source line at 3:53 |
| LWTE-4:1–4:219 | Narrator | contributor, by name (ranges in the voice map) | Bylines |
| LWTE-1:201, 3:88, 4:220–4:312 | Narrator | editorial (footnote; addresses) | |
| LWTE-1:21, 2:60, 2:83, 3:26 | Narrator | remove the fused footnote text from the paragraph into a footnote field | Footnote text interrupts the sentence |

Evidence quotes for section A:

QUOTE[TBWTT-1:26]: Pourquoi êtes-vous venu ici en ce froid matin d’hiver? ENDQUOTE
QUOTE[TBWTT-1:27]: Je ne sais pas... envie de faire un peu de marche au grand air... ENDQUOTE
QUOTE[TBWTT-3:2]: il continua son récit : Dans la Genèse, XXVIII, se trouve une autre description de notre présence. ENDQUOTE
QUOTE[TBWTT-3:305]: Symbole que Raël a vu représenté sur la soucoupe volante en 1973. ENDQUOTE
QUOTE[TBWTT-5:40]: Vous ne pouvez vous asservir à Dieu et à Mamon*. ENDQUOTE
QUOTE[TBWTT-5:44]: *Mamon : la richesse en araméen. ENDQUOTE
QUOTE[ETTMTTP-2:70]: Il fit un signe à l'un des robots, situé près de la machine ENDQUOTE
QUOTE[ETTMTTP-2:74]: Effectivement, ce que j'avais vu correspondait parfaitemet à la description d'Ezéchiel. ENDQUOTE
QUOTE[ETTMTTP-2:76]: - Oui, j'ai la photo de ma mère dans mon portefeuille, qui est resté dans mes vêtements». ENDQUOTE
QUOTE[ETTMTTP-2:77]: Il me la montra en me demandant s'il s'agissait bien de celle-ci. ENDQUOTE
QUOTE[ETTMTTP-2:86]: «Désirez-vous des compagnes ?» demanda le robot. ENDQUOTE
QUOTE[ETTMTTP-2:93]: «Avec de l'entraînement on arrive à créer une histoire et à la faire se dérouler. ENDQUOTE
QUOTE[ETTMTTP-3:4]: il faut toujours considérer les choses par rapport à quatre plans, tout d'abord : ENDQUOTE
QUOTE[ETTMTTP-3:264]: Si tu veux m'aider à réaliser les objectifs fixés par les Elohim, écris-moi: ENDQUOTE
QUOTE[LWTE-1:1]: des journalistes ayant interviewé Raël à la radio et à la télévision ENDQUOTE
QUOTE[LWTE-2:1]: des révélations que Raël n'avait pas le droit d'annoncer avant que trois années se soient écoulées ENDQUOTE
QUOTE[LWTE-2:59]: il dit: – Je dois vous avertir qu'il n'existe pas chez nous les Elohim qu'une tendance ENDQUOTE
QUOTE[LWTE-2:59]: Moi et ceux qui me soutiennent et qui sont nombreux, nous pensons que les hommes sont mauvais ENDQUOTE
QUOTE[LWTE-2:68]: Je lui répondis : – Je ne suis pas du tout persuadé que l'humanité va s'autodétruire ENDQUOTE
QUOTE[LWTE-2:71]: - Vous refusez donc ma proposition? me demanda mon interlocuteur. ENDQUOTE
QUOTE[LWTE-2:76]: mais Satan, notre frère, qui vient de vous mettre ainsi à l'épreuve ENDQUOTE
QUOTE[LWTE-2:128]: Ce personnage, c'était moi Yahvé et j'étais entouré de vingt-quatre autres éternels ENDQUOTE
QUOTE[LWTE-3:53]: (Soumission à l'autorité, S. Milgram, Paris, 1974.) ENDQUOTE

### B. Too coarse (the tag is defensible but hides a second layer)

| REF | Current | Note |
|---|---|---|
| TBWTT: 33 section headings (2:46, 2:71, 2:77, 2:88, 3:1, 3:60, 3:76, 3:102, 3:117, 3:136, 3:157, 3:213, 3:248, 3:262, 4:1, 4:17, 4:41, 4:65, 4:78, 5:1, 5:8, 5:24, 5:36, 5:50, 5:55, 5:61, 6:15, 6:18, 7:1, 7:11, 7:28, 7:59, 7:73) | Narrator | Headings interrupt a continuous quoted speech; they are neither narration nor speech. A `heading` type would let a reader or an audio renderer skip them |
| TBWTT: 249 paragraphs (6,911 words) that are wholly Bible quotation | Yahweh | He is reading out; a `quotation` flag would separate the Bible text from his commentary |
| ETTMTTP-2:72, 2:106–2:109, 2:111 | Yahweh | Ezekiel, Qur'an, Matthew read out |
| ETTMTTP-2:116–2:120 | Yahweh | Rules worded in *tu* for the follower, embedded in a *vous* address to Raël |
| ETTMTTP-2:122–2:128 | Yahweh | Apostrophe to the people of Israel |
| ETTMTTP-1:41–1:45 | Narrator | Raël's own song lyric |
| ETTMTTP-3:120–3:132 | Yahweh | Model prayer: the *je* is the praying follower, the *vous* the Elohim |
| ETTMTTP-3:184, 3:232, 3:239 | Yahweh | Tibetan Book of the Dead and Qur'an quotations |
| LWTE-2:9, 2:12–2:16, 2:33, 2:36–2:37, 2:39–2:41, 2:44–2:46, 2:49–2:50, 2:53–2:56, 3:35–3:36 | Narrator | Matthew and Job quotations inside Raël's commentary |
| LWTE: 19 paragraphs where a section heading is fused to the following text (list in `voices.json`, field `mixed`) | Narrator | Segmentation defect in the digitisation |
| LWTE ch. 4: quotations of Rostand, Muller and others inside Terrusse's essays | Narrator | Not separated in this study |

### C. Needs judgement

| REF | Question | Evidence one way | Evidence the other way |
|---|---|---|---|
| ETTMTTP-3:5–3:261, 3:263 (the bulk of the 258 ¶ tagged Yahweh, minus the items in A and B) | What value? | Frame 2:132 disowns authorship and names the Elohim; 2:98 announces speech through his mouth; 3:241 and 3:259 speak as Elohim | Elohim in third person throughout; 36 ¶ with human "we"; Raël's "I" at 3:174–175, 3:208; cross-references such as *la première partie de ce livre* |
| ETTMTTP-3:241, 3:259 | Yahweh or same as the rest? | *notre prophète*, *nous parlons par sa bouche*, *notre ambassadeur* | Both stand inside unmarked human-"we" context (3:258, 3:260) |
| ETTMTTP-3:69 | Whose *notre ambassade terrestre*? | Elsewhere the embassy is *leur* (the Elohim's) | A human movement can also say "our embassy" |
| ETTMTTP-3:262–3:266 | Part of the inspired text or Raël's own closing? | 3:262–3:263 match the preceding style | 3:264 *écris-moi*, the address, and *(adresses en fin de volume)* are practical matter |
| ETTMTTP-2:99 | Still addressed to Raël? | Inside the quoted speech 2:98–2:129 | Addresses readers and names Raël in the third person |
| TBWTT-5:44 | Whose footnote? | Could be the author's 1974 note | Could come from the Bible edition quoted or a later editor; the text does not say |
| LWTE-2:6–2:31 | Raël's commentary or relayed revelation? | Written impersonally in his own exposition | 2:1 calls the chapter's content *révélations*; no source scene is given for the Satan and three-planets material |
| LWTE-2:77 | Narrator or Satan? | Indirect speech (*Satan me dit alors qu'il ne pensait pas*) | Carries Satan's content |
| LWTE-1:1, 2:1–2:2 | Editor or Raël writing of himself? | Third person | *nous sommes en l'an 34* could be Raël's own formula |
| TBWTT-7:74–7:83, ETTMTTP ch. 1 | Keep `Narrator`? | Same person as `Raël` | The data uses `Raël` only for dialogue lines; a consistent rule is the maintainers' call |

Evidence quotes for section C:

QUOTE[ETTMTTP-2:98]: À partir de maintenant nous verrons par vos yeux, nous entendrons par vos oreilles et nous parlerons par votre bouche. ENDQUOTE
QUOTE[ETTMTTP-2:99]: Vous qui lirez ce message, dites-vous bien que vous pouvez avoir accès à ce monde merveilleux ENDQUOTE
QUOTE[ETTMTTP-3:69]: afin qu'il le préserve dans notre ambassade terrestre ENDQUOTE
QUOTE[ETTMTTP-3:84]: Comme cela est dit dans la première partie de ce livre ENDQUOTE
QUOTE[ETTMTTP-3:262]: Écris au Guide des guides, à Raël; il te recevra ENDQUOTE
QUOTE[LWTE-2:17]: L'on sait que les Elohim ont créé également la vie sur deux autres planètes à cette époque ENDQUOTE

## Analysis of "Les Clés" (ETTMTTP ch. 3)

(a) What the text says about how it was written. After the return at midnight he writes the narrative from engraved memory (2:131), and then, *lorsque j'eus terminé la narration*, something *se déclenchait* and he writes as an observer of his own writing (2:132). The frame sentence is unfinished. The chapter opens by naming itself: QUOTE[ETTMTTP-3:1]: Ces écrits sont des clés qui permettent d'ouvrir les esprits ENDQUOTE

(b) Who is *nous*. A human collective that includes the writer and the reader: created by the Elohim (3:11), judged by them (3:26, 3:88), less advanced than some other worlds (3:194), *de pauvres primitifs bornés* (3:205), their children (3:253). *Nos créateurs* / *nos pères* are the Elohim (36 paragraphs).

(b) Who is addressed. *Tu* in 115 paragraphs: an individual follower, in places grammatically a woman (QUOTE[ETTMTTP-3:54]: ne te crois pas condamnée pour autant à vivre définitivement seule ENDQUOTE). *Vous* without *tu* in 25 paragraphs: a couple (QUOTE[ETTMTTP-3:63]: Lorsque vous ne vous entendrez plus ne restez pas ensemble ENDQUOTE), mourners (3:72), humanity (QUOTE[ETTMTTP-3:99]: Vous êtes arrivés à l'âge d'or. ENDQUOTE), scoffers (3:218, 3:222–3:223), believers (3:240–3:241), clergy (3:246–3:247), and the Elohim themselves inside the model prayer (3:120–3:132). Vocatives by religion at 3:226–3:229 and 3:260 (QUOTE[ETTMTTP-3:226]: Et toi, chrétien, tu as relu cent fois que Jésus reviendrait ENDQUOTE). 126 paragraphs are impersonal.

(b) Where the voice shifts. Listed in finding 2. The prayer is introduced as a template (QUOTE[ETTMTTP-3:119]: Voici un modèle de texte à dire en pensant intensément les mots qui le composent ENDQUOTE; QUOTE[ETTMTTP-3:124]: Elohim, je vous reconnais pour créateur ENDQUOTE).

| Reading Les Clés as Yahweh's speech — evidence for | Evidence against |
|---|---|
| The frame denies authorship and its last words are *Les Elohim commençaient à…* (2:132) | The frame is unfinished and does not name a speaker |
| 2:98 announces *nous parlerons par votre bouche* the same morning | No *Moi Yahvé* formula, unlike LWTE-2:95 and 2:232, where that mode is explicit |
| 3:241 and 3:259 use Elohim "we" | Those are 2 paragraphs of 266; the other first-person plurals are human |
| Imperative, legislative register continues 2:116–2:120 (rules in *tu* given by Yahweh) | Yahweh is never named or self-identified in the chapter; Elohim are *eux* (QUOTE[ETTMTTP-3:15]: Même nos créateurs ne nous traitent pas en enfants mais en individus ENDQUOTE) |
| | Raël's own "I" intrudes (3:174–3:175, 3:208) |
| | Refers to the earlier message as a book (QUOTE[ETTMTTP-3:80]: décrits dans Le Livre qui dit la Vérité ENDQUOTE; QUOTE[ETTMTTP-3:71]: Conformément à ce qui est écrit dans le Livre ENDQUOTE) |
| | Dates itself from the human side (QUOTE[ETTMTTP-3:172]: 1976 sera donc l'an 31 après Raël ENDQUOTE) |

(b) My reading: the text presents ch. 3 as writing produced under inspiration, in a human voice that speaks about the Elohim; it does not present it as Yahweh's direct speech. That is an inference from grammar, not a statement of the text.

(c) Open. A first edition might show the missing end of 2:132, and section headings for ch. 3 that the dump lacks; either could settle the label.

## Address forms

(a) Yahweh to Raël, *vous*: all of TBWTT (e.g. 1:20–1:63, 5:66 *Vous Claude Vorilhon*, 6:19–6:29, 7:2–7:71); ETTMTTP 2:11, 2:13, 2:19, 2:22–2:43, 2:50–2:83, 2:96–2:105, 2:112–2:115, 2:121, 2:129 (QUOTE[ETTMTTP-2:121]: Vous, Raël, vous êtes notre ambassadeur sur Terre ENDQUOTE; QUOTE[ETTMTTP-2:129]: Voilà, j'ai terminé. Vous serez capable de commenter tout cela par vous- même une fois sur Terre. ENDQUOTE); LWTE 2:76.

(a) Yahweh to Raël, *tu*: LWTE 2:85–2:88 only (QUOTE[LWTE-2:88]: A partir de maintenant tu pourras t'adresser à moi en disant tu, car tu es mon fils et je suis ton père. ENDQUOTE).

(b) Check against the statement at LWTE-2:85. I scanned every Yahweh paragraph of TBWTT and ETTMTTP ch. 2 for second-person-singular forms outside quotation marks. Thirteen paragraphs have them and none addresses Raël: TBWTT-2:30 (paraphrase of Genesis 2), 3:80, 4:14, 6:12 (tails of split Bible quotations); ETTMTTP-2:116–2:119 (rules for the follower: QUOTE[ETTMTTP-2:116]: - Tu te présenteras au moins une fois dans ta vie devant le Guide des guides ENDQUOTE); ETTMTTP-2:124–2:128 (Israel: QUOTE[ETTMTTP-2:124]: Peuple d'Israël, nous t'avons fait sortir des griffes des Egyptiens ENDQUOTE). Null result: no counter-example.

(b) Chronology. LWTE places the *tu* scene on the planet of the Eternals, after the session in the chair (QUOTE[LWTE-2:81]: après être sorti en douceur du laboratoire où l'on avait modifié mon esprit dans un étrange fauteuil coquille ENDQUOTE) and after the address to Israel (QUOTE[LWTE-2:80]: à la fin de son exposé qui est rapporté en page 90 du deuxième message(*), s'adressant plus particulièrement au peuple d'Israël. ENDQUOTE). That is after ETTMTTP-2:129, the last *vous* in the second book. ETTMTTP itself moves from 2:129 straight to *Je restai encore plusieurs heures* (2:130) with no trace of the scene; LWTE-2:90 gives the reason for the silence (QUOTE[LWTE-2:90]: Ensuite il me demanda de ne pas révéler ce lien de parenté aux hommes avant que trois années soient écoulées. ENDQUOTE). LWTE-2:76 (*vous*) is set earlier the same journey, in the relay vessel, so it is consistent.

(b) One oddity inside the *vous* address: QUOTE[ETTMTTP-2:100]: Mais soyez sévères quant à leur sélection ENDQUOTE has a plural adjective although Raël alone is addressed in the sentence before.

(a) Others. Satan to Raël: *vous* (LWTE 2:59–2:67). Robot to Raël: *vous* (ETTMTTP-2:86). Interviewers to Raël: *vous* (LWTE-1:2). Raël to Yahweh: *vous* in TBWTT ch. 1 and 7; no direct speech to him after LWTE-2:88. Raël to Giroux, as Giroux reports it: *tu* (LWTE-4:171).

(a) Plural addressees. Readers at large: TBWTT 7:77–7:83 (Raël); ETTMTTP-2:99 (inside Yahweh's speech); LWTE 3:56, 3:82–3:87. *Hommes de la Terre*: LWTE 2:95–2:235 (Yahweh), with Raëlians singled out at 2:231 (QUOTE[LWTE-2:231]: vous qui nous reconnaissez comme vos créateurs et qui reconnaissez Raël comme notre messager ENDQUOTE) and spoken of in the third person at 2:96 (QUOTE[LWTE-2:96]: tout raëlien doit agir comme si les hommes allaient finalement avoir la sagesse ENDQUOTE). Raëlians: LWTE 3:59, 3:79 (QUOTE[LWTE-3:59]: Vous les Raëliens, si moi-même demain je vous demandais de tuer quelqu'un ENDQUOTE). People of Israel as a collective *tu*: ETTMTTP 2:124–2:128, where the speaker slips once from *nous* to *je* (QUOTE[ETTMTTP-2:124]: j'ai fait venir tes fils et tes filles des extrémités de la Terre ENDQUOTE). In TBWTT Yahweh's *vous* often means humanity rather than Raël (*votre monde*, *vos savants*); I did not separate those paragraph by paragraph.

## Passages with no reported reception scene

| Range | Words | What is missing | What the text does give |
|---|---:|---|---|
| LWTE-2:94–2:235, "Message de Yahvé aux hommes de la terre" | 4,685 (3,044 speech + 1,641 Apocalypse) | When, where and how received; no narration before 2:95 or after 2:235 | Heading 2:94; formula *par la bouche de mon prophète Raël* at 2:95 and 2:232; chapter introduction dated *l'an 34 (1979)* |
| LWTE-2:6–2:31, Satan / Lucifer / three planets | 1,583 | Source of the information; stated as *L'on sait que* | 2:1 attributes the chapter to revelations withheld for three years after the 1975 voyage |
| ETTMTTP-3:1–3:266 | 14,297 | Place and duration; the frame sentence is cut off | 2:132: after finishing the narrative, at home, same night |
| LWTE ch. 1 answers that add doctrine (e.g. 1:27, 1:34, 1:36, 1:40) | not separated | Presented as Raël's answers, no reception claim | *Réponse de Raël* |

The two scenes that LWTE does frame are both back-dated into the October 1975 journey: the temptation (2:58–2:78: QUOTE[LWTE-2:58]: L'un des deux autres Elohim me demanda alors de le suivre. ENDQUOTE; QUOTE[LWTE-2:78]: comme cela est relaté dans le livre contenant le deuxième message. ENDQUOTE) and the paternity disclosure (2:79–2:90). Satan's offer includes a dictation of its own (QUOTE[LWTE-2:61]: Votre rôle consistera à faire publier les livres que je vous dicterais ENDQUOTE).

QUOTE[LWTE-2:94]: Message de Yahvé aux hommes de la terre : l'apocalypse du cataclysme nucléaire final ENDQUOTE
QUOTE[LWTE-2:232]: j'adresse ce message aux hommes de la terre par la bouche de mon prophète Raël. ENDQUOTE
QUOTE[LWTE-2:2]: Maintenant que nous sommes en l'an 34 (1979) ces choses peuvent être connues de tous. ENDQUOTE

## Later-edition material inside the digitised text

| REF | Sign | Text |
|---|---|---|
| TBWTT-3:305 | Caption in the body, Raël in third person | QUOTE[TBWTT-3:305]: Symbole que Raël a vu représenté sur la soucoupe volante en 1973. ENDQUOTE |
| TBWTT-6:29, 7:73, 7:81, 7:83 | Movement named *Mouvement Raélien* in a 1973 speech and 1974 epilogue, while the 1975 book calls it MADECH | QUOTE[TBWTT-6:29]: Votre mouvement vous l’appellerez le Mouvement Raélien. ENDQUOTE vs QUOTE[ETTMTTP-2:1]: démissionner du poste de président du MADECH1 ENDQUOTE |
| TBWTT-5:44 | Footnote line in the body | quoted above |
| TBWTT-7:81, 7:83 | *écrivez-moi* with no address anywhere in the dump | — |
| ETTMTTP-1:4, 1:76, 1:77, 2:1, 2:2, 2:3, 2:4, 2:7, 2:8 (14 occurrences in 9 paragraphs) | Orphaned footnote marker *MADECH1*; the note text is absent | — |
| ETTMTTP-1:63 | Orphaned marker *révélations1* | — |
| ETTMTTP-2:24, 2:35 | Orphaned marker *svastika1* | — |
| ETTMTTP-3:33 | Stray dagger *expliquer‡* | — |
| ETTMTTP-2:105 vs 2:114 | Two names for the movement inside one speech | QUOTE[ETTMTTP-2:105]: le mouvement que vous avez créé, le Mouvement Raëlien ENDQUOTE vs QUOTE[ETTMTTP-2:114]: créez un monastère des guides du MADECH près du lieu où vous résidez. ENDQUOTE |
| ETTMTTP-3:265 | Geneva address, *Religion Raëlienne* | QUOTE[ETTMTTP-3:265]: Raël, Religion Raëlienne, Siège International, C.P. 225, 1211 Genève 8. ENDQUOTE |
| ETTMTTP-3:266 | Reference to an address appendix not in the dump | QUOTE[ETTMTTP-3:266]: en écrivant au Mouvement Raëlien de ton pays (adresses en fin de volume). ENDQUOTE |
| LWTE-1:17, 1:197, 2:58, 2:80, 3:26 | Footnote markers *(*)* | QUOTE[LWTE-1:17]: en page 84 du deuxième message(*) ENDQUOTE |
| LWTE-1:21, 1:201, 2:60, 2:83, 3:26 | Footnote text naming the 1998, 1999 and 2000 editions, with new page numbers (234, 263, 240, 237) | QUOTE[LWTE-1:21]: (*) Depuis 1998 les deux premiers livres de Raël sont regroupés en un volume ENDQUOTE; QUOTE[LWTE-2:60]: Si vous continuez à accomplir la mission que (*) Voir le livre Les extra-terrestres m'ont emmené sur leur planète, deuxième livre de Rael, groupé, depuis 1998 ENDQUOTE; QUOTE[LWTE-2:83]: (*) Depuis 1998 les deux premiers livres de Raël sont regroupés en un volume ENDQUOTE |
| LWTE-3:88 | Geneva address | QUOTE[LWTE-3:88]: RAEL Religion Raelienne Siège International Case postale 225 CH-1211 Genève 8 ENDQUOTE |
| LWTE-4:220–4:312 | Address list with e-mail addresses on 18 lines | QUOTE[LWTE-4:226]: australia@rael.org ENDQUOTE |
| Spelling across books | *Iahvé* in TBWTT (61) and ETTMTTP (10), *Yahvé* in LWTE (47); *Raélien* in TBWTT (4), *Raëlien/raëlien* in ETTMTTP (4) and LWTE (76) | — |

(b) Analysis. The 1998–2000 footnotes and the e-mail addresses are dated by their own content. The *Mouvement Raélien* reading in TBWTT is an inference from the conflict with ETTMTTP; `[outside knowledge — unverified, needs source]` the 1974 first edition is commonly said to have named the movement MADECH at this point. The original page references in LWTE (*page 34 du premier message*, *page 84 du deuxième message*) survive beside the new ones, so the body text was not repaginated, only annotated.

(b) A dating tension inside LWTE: the editor's introduction equates 1979 with year 34, a contributor dates May 1979 as year 33 (QUOTE[LWTE-4:219]: Cannes, 22 mai 1979, an 33 après Raël. ENDQUOTE). ETTMTTP-3:172 sets 1946 as year 1 and 1976 as year 31, and LWTE-1:2 gives *le 7 octobre 30 (1975)*; on that rule 1979 is year 34.

## Tensions and null results

- Six sessions asserted, five narrated (finding 3); ETTMTTP-1:63 literally implies seven.
- No *tu* from Yahweh to Raël anywhere before LWTE-2:85 (null); no Yahweh-to-Raël address at all after it, so the rule cannot be tested forward.
- No explicit statement anywhere in ETTMTTP ch. 3 that Yahweh or the Elohim are speaking (null), apart from the two "we" paragraphs.
- No reception scene for LWTE 2:94–2:235 (null).
- The "one October night" of the second contact: the narrative contains a night and a following morning on the planet (ETTMTTP-2:94–2:95), and LWTE-1:2 says *près de vingt-quatre heures*, yet he leaves about 23:00 (2:9) and is back at midnight (2:131). The text does not explain the two clocks.
- ETTMTTP-2:23 has Yahweh say the first message was mis-transcribed at one point; the text thereby concedes that mode 1 was fallible.
- The movement has two names inside one 1975 speech (ETTMTTP-2:105, 2:114).
- TBWTT's speaker is unnamed; `Yahweh` rests on ETTMTTP-2:61 and LWTE-2:79.

QUOTE[ETTMTTP-2:131]: Je rentrai chez moi où je me mis immédiatement au travail pour écrire tout ce qui m'avait été dit. ENDQUOTE
QUOTE[TBWTT-7:75]: en mettant de l’ordre dans les notes que j’avais prises, en les classant et en les recopiant ENDQUOTE
QUOTE[TBWTT-1:44]: Vous écrirez tout ce que je vous dirai et ferez publier le livre regroupant ces écrits. ENDQUOTE
QUOTE[TBWTT-7:33]: vous pouvez nous appeler des «Elohim» puisque nous sommes «venus du ciel». ENDQUOTE

## Relation to existing core records

- **woh-claim-0035 (serial dictation).** The statement says "six mornings in 1973, one October night in 1975" and "a consistent principal speaker". (i) The frames give five narrated mornings against a stated six. (ii) "Dictation" covers the first book only in the text's own vocabulary; the second book adds engraved memory and inspired writing, the third an unframed "through the mouth" message. (iii) The principal speaker's share falls from 67 % to 22 % to 8 % of words (speech proper), and the largest block of book 2 is not his speech by its own grammar. (iv) "The reporter retained editorial control" is supported in a new way: ETTMTTP-2:23, the 1998–2000 footnotes, the renamed movement. None of this touches the record's independence clause.
- **woh-claim-0020 (contact reports as provenance).** Its "six-day teaching" inherits the same five-versus-six question. The 1975 report is dated consistently (7 October; LWTE-1:2).
- **woh-claim-0070 (canonical contact report).** TBWTT-1:53 and 2:5 are both correctly tagged as the Eloha's speech; 2:5 is his commentary, not a Bible quotation. The record's phrase "its speakers" is safe: the speaker is one unnamed being who says *nous*.
- I found no existing core record on the voice of Les Clés, the address forms, or the edition layers.

## Candidate claims or revisions for founder review (proposals, not decisions)

1. **Revise 0035's session wording** from "six mornings" to "six mornings as stated, five as narrated in the project digitisation", pending a first-edition check.
2. **New source_report candidate:** "The second book frames its third chapter as writing its reporter did not feel he authored (ETTMTTP-2:132); within it the Elohim are third persons and the speaker counts himself among the created." Label `direct`.
3. **New interpretation candidate:** "The canon presents four modes of transmission (notes under dictation; engraved memory; inspired writing; speech through the prophet's mouth), with decreasing narrative framing." Label `inferred`.
4. **New source_report candidate:** "LWTE states that Yahweh used *vous* to Raël until the paternity disclosure; the earlier books contain no counter-example." Label `direct` for the statement, `inferred` for the null-result check.
5. **Data-library change request:** apply list A; decide list C; consider `heading`, `quotation`, `footnote` and `contributor` paragraph types.
6. **Source-note addition** for each book: the edition layers listed above, so that citations to these REFs are not mistaken for 1974/1975/1979 wording.

## Limitations

- I read the digitisation, not a printed first edition. Every statement about "later-edition" material is about what this dump contains.
- Dialogue dashes are missing from the TBWTT dump; ch. 1 and ch. 7 turn-taking was assigned from content. I found one mis-tag (1:27) and cannot exclude another among the very short turns.
- Paragraphs read by opening only (most of TBWTT ch. 3–6, LWTE 2:106–2:225, LWTE ch. 1, 3, 4, ETTMTTP ch. 1 and parts of ch. 3) were also pattern-scanned for inquits, pronoun shifts, dates and markers, but an unmarked voice shift in the middle of a long paragraph could have escaped.
- Scripture-quotation detection is mechanical. Paragraphs that mix quotation and commentary count as speech; about ten short TBWTT paragraphs sit on that border.
- Quotations by contributors in LWTE ch. 4 were not separated from the contributors' own words.
- Word counts are whitespace tokens; mixed paragraphs count toward the dominant voice.
- Outside knowledge was used once and is marked.
