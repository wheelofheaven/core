---
title: "Canon close reading: the numbers"
status: draft
version: 0.1.0
last_reviewed: 2026-11-12
---

# Numerics of the Raëlian canon — concordance and consistency audit

Key: `numerics` · prepared 2026-11-12 · access level: `project_digitization` (French dumps `texts/{TBWTT,ETTMTTP,LWTE}.fr.txt`; the French is the source of record).

## Exact question

What quantities does the Raëlian canon state — every number, date, duration, age, distance, speed, population, count, percentage, measure — across all three books, and are they consistent with each other? Sub-questions: (1) internal consistency of repeated quantities; (2) derived arithmetic; (3) chronological skeleton; (4) numbers the Wheel of Heaven project uses that the canon does not contain.

## Method

1. Mechanical sweep: every paragraph of the three French dumps containing a digit or a French number/measure word was extracted (703 of 2,070 paragraphs: TBWTT 317, ETTMTTP 131, LWTE 255) and read in context; key paragraphs were then read in full. Helper scripts: `agent-numerics/extract.py`, `win.py`.
2. Targeted null-result searches by regular expression over the whole French text (zodiac names, « précession », « zodia- », 2160, 25920, 21810, 11375, « sept équipes/races », « douze »).
3. Register built in `agent-numerics/reg.py`; every French wording in the register is machine-checked as a verbatim substring of its paragraph. 213 items.
4. Arithmetic recomputed by script. Constants that the text does not itself supply (length of the year in seconds, light-year, astronomical unit, calendar dates of outside events) are marked `[outside knowledge — unverified, needs source]`.
5. Layers are kept apart: **(a) TEXT** = what the paragraph says; **(b) ANALYSIS** = my counts, sums and comparisons; **(c) OPEN** = unresolved questions and what would discriminate.

Voice matters and is recorded per item. LWTE is tagged Narrator throughout in the dump; I distinguish: Questioner (ch. 1 questions), Raël (ch. 1 answers, ch. 2 narrative, ch. 3), Yahweh (ch. 2 "Message de Yahvé", LWTE-2:95–233, reported by Raël), Satan (reported), Editor (LWTE-2:1–2), and the named witnesses of ch. 4 (Terrusse, Le Gendre, Giroux, Beluet, Ndjoga-Awirondjogo, Deydier), who are not the Elohim's voice and not Raël's.

Scope limits of the register: purely grammatical "deux" (« tous deux », « les deux »), ordinals of biblical verse references, postal addresses, and most numerals inside verbatim Bible/Qur'an quotations are omitted unless the canon glosses or computes with them. Biography numerals of no chronological use (prices, room sizes) are sampled, not exhausted.

## Findings (ranked; new relative to core unless stated)

### F1. « 25 000 ans » is one figure doing four different jobs, and the jobs do not all fit together

**TEXT.** The figure occurs in eleven paragraphs (TBWTT-5:56, 7:21, 7:56; ETTMTTP-2:43; LWTE-1:13, 1:15, 1:30, 1:31, 1:56, 1:73, 4:73) with four distinct referents:

- Yahweh's age and body count:

QUOTE[TBWTT-7:56]: Le plus âgé, le président du conseil des Éternels a vingtcinq mille ans et vous l’avez devant vous. J’ai habité 25 corps jusqu’à ce jour et je suis le premier sur qui cette expérience ait été réalisée ENDQUOTE

- the scientific lead:

QUOTE[TBWTT-7:21]: avec nos vingt-cinq mille ans d’avance scientifique pour héritage ENDQUOTE

- the landing on Earth (book 2, Yahweh):

QUOTE[ETTMTTP-2:43]: ceci était vrai il y a vingt-cinq mille ans lorsque nous avons débarqué sur la terre ENDQUOTE

- the creation of life and of the original continent (book 3; the figure is put by the questioner and accepted by Raël in his answer):

QUOTE[LWTE-1:13]: Les Elohim disent avoir créé la vie sur Terre il y a vingtcinq mille ans. ENDQUOTE

QUOTE[LWTE-1:31]: les effets de «l'orage» de la création par nos pères du continent originel ayant eu le temps de s'estomper, en vingtcinq millénaires. ENDQUOTE

**ANALYSIS.** (i) 25,000 years ÷ 25 bodies = 1,000 years per body, which matches « mille de vos années à vivre » (TBWTT-7:30): this sum closes. (ii) Age = time since landing: taken literally, Yahweh was a new-born when the expedition he says he personally directed (« J’ai moi-même dirigé la création de la vie sur la Terre », TBWTT-7:56) landed. (iii) He is « le premier » to have been re-created, so re-creation cannot be older than his first death, roughly 24,000 years ago on the text's own 1,000-year bodies; yet TBWTT-7:31 says the scientists who wanted to create life on other planets « étaient du conseil des éternels » — a council that, on these numbers, did not yet exist at the landing, let alone during the three earlier failed attempts (TBWTT-4:49). (iv) In book 1 nothing is dated 25,000 years ago except Yahweh's birth; the only book-1 dating of the Earth project is 22,000 years (F2). The equation "creation = 25,000 years ago" is first stated in book 2 (as the landing) and generalised in book 3 by a questioner (« En page 28 du premier message il est écrit que les Elohim ont créé, il y a vingt-cinq mille ans, le continent originel », LWTE-1:30 — the cited passage, TBWTT-2:14, contains no date).

**OPEN.** Whether "25,000" is a rounded, emblematic figure (it is never qualified by « environ ») or four independent quantities. Core's Sendy evidence map (woh-claim-0072) already notes that 22,000 and 25,000 "refer to different quantities"; it does not record the four-way spread or the eternals/landing ordering problem.

### F2. The deep chronology closes arithmetically on 25,000 → 13,000, but 22,000 sits off the grid and the canon never states the sum

**TEXT.**

QUOTE[TBWTT-2:10]: Le «jour» correspond à la période pendant laquelle votre soleil se lève sous le même signe le jour de l’équinoxe de printemps, soit deux mille ans terrestres environ. ENDQUOTE

QUOTE[TBWTT-5:4]: Depuis vingt-deux mille ans que les créateurs décidèrent de faire leur œuvre sur Terre tout est prévu, car le mouvement de la galaxie suppose cette connaissance. ENDQUOTE

QUOTE[LWTE-2:208]: Les premiers hommes ayant été créés il y a environ treize mille ans ENDQUOTE

QUOTE[LWTE-1:47]: datant d'environ cinq mille ans, ce qui correspondrait à la période du «déluge » réel ENDQUOTE

**ANALYSIS.** Six "days" × 2,000 years = 12,000 years; landing 25,000 years ago (ETTMTTP-2:43) minus 12,000 = 13,000 years ago, exactly the book-3 date for the first humans (man being the sixth-day work in the Genesis sequence TBWTT ch. 2 follows). The three books' figures therefore fit one scheme — but only if the "day" is the canon's own 2,000 years. With 2,160-year days the same sum gives 25,000 − 12,960 = 12,040. The canon never performs this addition; it is my derivation. The 22,000 figure does not land on a day boundary of that scheme (25,000 − 22,000 = 3,000 years = 1.5 days) and what it dates is a *decision* (« décidèrent de faire leur œuvre »), not an arrival. TBWTT ch. 2 quotes only one day-formula (« premier jour », TBWTT-2:9) and never numbers days two to seven or says how many days the work took; the six-day count is supplied from Genesis, not from the canon's wording.

**OPEN.** Whether the 22,000 was meant as the same event as the 25,000 landing (then the books disagree by 3,000 years) or as a later decision after one and a half "days" of survey (then they agree). The text supports the second reading weakly: the first day is survey (« Ces études prirent pas mal de temps », TBWTT-2:10) and the continent is raised only after further study (TBWTT-2:12–14).

### F3. The canon's own precessional vocabulary is thin: two signs, a "day" of about 2,000 years, no cycle length, no count of signs

**TEXT / NULL RESULT.** Across all three books: the word « précession » occurs 0 times; « zodiaque/zodiacal » 0 times; of the twelve sign names only « Poissons » and « Verseau » occur as ages (TBWTT-5:4, 5:7, 5:12; ETTMTTP-3:172); « douze » never refers to signs or ages; no figure 2,160, 25,920 or 26,000 appears as a cycle (the one « 26 000 ans » is rocket travel time, TBWTT-5:52). The mechanism is described once (TBWTT-2:10, above) and once more for Aquarius:

QUOTE[TBWTT-5:7]: Le moment où le soleil se lève sur la Terre, le jour de l’équinoxe de printemps, «dans» le Verseau. ENDQUOTE

The Pisces boundary is tied to the crucifixion:

QUOTE[TBWTT-5:12]: ont crucifié Jésus par peur de se voir ruinés et anéantis au moment du passage dans l’ère des Poissons ENDQUOTE

**ANALYSIS.** The canon's Pisces therefore runs from about the time of Jesus to 1946, i.e. roughly 1,910–1,950 years, compatible with « deux mille ans … environ » and not with 2,160; the project lattice starts Pisces in 210 BCE. Core `precessional-world-age-chronology.md` already labels 2,160 a model convention; what is new here is that the canon states a *different* figure for the same unit and places the Pisces boundary about two centuries later than the lattice.

### F4. Two epochs for the new era — 1946 (books 1–2) and 1945 (book 3) — and at least two year-count conventions in use

**TEXT.**

QUOTE[TBWTT-5:4]: le Verseau, qui suit, est là depuis 1946, Époque où le peuple d’Israël retrouve son pays ENDQUOTE

QUOTE[ETTMTTP-3:172]: Tu dateras tes écrits en comptant l'an 1946 comme l'an un après Raël, le dernier des prophètes. 1976 sera donc l'an 31 après Raël, ou l'an 31 de l'ère du Verseau, ou l'an 31 de l'âge de l'apocalypse, ou l'an 31 de l'âge d'or. ENDQUOTE

QUOTE[LWTE-2:208]: La génération qui est née au commencement de l'âge de l'Apocalypse en 1945 de l'ère chrétienne était la six cent soixante-sixième ENDQUOTE

QUOTE[LWTE-3:79]: cet âge de l'Apocalypse dans lequel nous sommes entrés. Depuis 1945. ENDQUOTE

QUOTE[LWTE-3:26]: le rassemblement annuel du 6 août pour fêter l'entrée dans l'âge de l'Apocalypse ENDQUOTE

QUOTE[LWTE-4:219]: Cannes, 22 mai 1979, an 33 après Raël. ENDQUOTE

**ANALYSIS.** Book 2 makes the era of Aquarius, the age of the Apocalypse and the golden age one count from 1946. Book 3 starts the age of the Apocalypse in 1945 (Hiroshima, 6 August). The stated rule (1946 = 1; 1976 = 31) gives 1975 = 30 and 1979 = 34, and LWTE-1:2 (« le 7 octobre 30 (1975) ») and LWTE-2:2 (« l'an 34 (1979) ») follow it. The witness dateline LWTE-4:219 (22 May 1979 = an 33) does not: under the rule it should read an 34. It fits a count of completed years since 6 August 1945 that turns over each 6 August; that reading also reproduces 7 Oct 1975 = 30, so the two conventions are indistinguishable except for dates between 1 January and 5 August. The epoch itself is explained three ways: birth year of Raël (TBWTT-5:7), « Époque » of Israel's return (TBWTT-5:4; the State of Israel dates from 1948 [outside knowledge — unverified, needs source]), and — from book 2 on — the conception date 25 December 1945 as « la véritable naissance » (ETTMTTP-1:7). The project's working boundary of 1950 appears nowhere in the canon.

**OPEN.** Which convention the movement actually used in 1979; a dated letter or bulletin from January–July of any year would discriminate. Related core record: `year-one-unsealing.md` speaks of "the 1945/1946 threshold" without separating the two epochs by book.

### F5. The distance-and-speed block is internally exact; its tension is external and the canon raises it itself

**TEXT.**

QUOTE[TBWTT-5:52]: Notre planète est à 30 millions de parasanges soit neuf mille milliards de kilomètres environ ou un peu moins d’une année lumière. ENDQUOTE

QUOTE[TBWTT-5:53]: en moins de deux mois grâce à un mode de propulsion utilisant l’atome et nous permettant de nous déplacer à la vitesse de rayons qui sont sept fois plus rapides que la lumière ENDQUOTE

QUOTE[TBWTT-5:53]: La planète des créateurs est éloignée de son soleil de 236 000 parasanges, soit 70 milliards huit cent millions de kilomètres ENDQUOTE

**ANALYSIS (all sums recomputed).** 30,000,000 × 300,000 km = 9.0 × 10^12 km — closes. 236,000 × 300,000 km = 7.08 × 10^10 km — closes to the stated « 70 milliards huit cent millions ». At 300,000 km/s the trip takes 3.0 × 10^7 s = 347 days — « presque un an », closes. At 40,000 km/h it takes 2.25 × 10^8 h ≈ 25,670 years — « près de 26 000 ans », closes. At seven times light speed it takes 49.6 days — « moins de deux mois », closes. With a light-year of 9.46 × 10^12 km [outside knowledge — unverified, needs source] the distance is 0.95 light-year — « un peu moins d'une année lumière », closes. Every stated conversion in this block is arithmetically correct. Implied but unstated: the home planet orbits its « grosse étoile » at about 473 astronomical units [outside knowledge — unverified, needs source], i.e. 2.7 light-days.

Tensions: (i) book 3 itself records the objection that the nearest star is about four light-years away and answers with a members' hypothesis, not an Elohim statement:

QUOTE[LWTE-1:27]: Certains scientifiques membres de notre Mouvement ont émis l'hypothèse que la distance entre leur planète et la nôtre serait bien de quatre années-lumière en suivant la lumière qui se déplacerait en suivant une courbe très prononcée, mais ne serait que d'une année-lumière en ne suivant plus la courbure des ondes lumineuses mais en allant tout droit. ENDQUOTE

(ii) the same answer opens « Les Elohim ne veulent absolument pas que nous sachions où se situe leur planète » (LWTE-1:27), and TBWTT-5:57 refuses radio contact so that the planet cannot be located — yet TBWTT-5:52 gives its distance to three significant figures. (iii) Book 1 states the 7c speed and the two-month journey in the present tense (« Nous avons les moyens »); book 2 back-dates both to 25,000 years ago and replaces them with « quelques instants » (ETTMTTP-2:43). (iv) The distance of the *planet of the eternals* — the only world Raël says he visited — is never given; book 1 puts the residence « sur notre planète », book 2 corrects this to a separate planet (ETTMTTP-2:50) and lists the two planets separately (ETTMTTP-3:193).

Relation to core: `kabbalah-shiur-qomah-anchor.md` (woh-claim-0021) labels the light-second gloss "the article's development, inferred". On the French text that is an under-attribution: the equation parasang = light-second, both km conversions, the light-year comparison and the two travel times are all in Yahweh's voice in TBWTT-5:52–53.

### F6. The demographic figures for the home planet do not close with the stated lifespans

**TEXT.**

QUOTE[TBWTT-7:46]: À ces sept cents éternels il faut ajouter deux cent dix stagiaires (environ soixante-dix par an soit dix par province). Sur les sept milliards d’habitants il n’y a que quarante millions d’enfants environ. Ce n’est qu’une fois majeurs (entre dix-huit et vingt et un ans suivant les sujets) que les enfants subissent l’opération qui leur donne une longévité de plus de sept cent cinquante ans. ENDQUOTE

QUOTE[TBWTT-7:31]: Durant trois existences, l’éternel est stagiaire ENDQUOTE

QUOTE[TBWTT-7:30]: Entre sept cent cinquante et mille deux cents ans. ENDQUOTE

**ANALYSIS.** (i) *Children.* In a constant population (« 2 parents, 2 enfants, ce qui fait que notre population est constante », TBWTT-7:13) the share of minors equals childhood ÷ lifespan. With majority at 18–21 and lifespans of 750–1,200 years that is 1.5–2.8 %, i.e. 105–196 million children among 7 billion. The text gives 40 million (0.57 %), which would need lifespans of 3,150–3,675 years or a childhood of 4–7 years. Off by a factor of roughly 2.6–4.9. (ii) *Probationers.* 7 provinces × 10 = 70 per year closes. But 210 probationers = three *years* of intake, whereas probation lasts three *existences* (about 3,000 years on the text's figures), which at 70 a year would give a standing stock of about 210,000. (iii) *Council.* A perpetual council fed at up to 70 a year since the first eternal would number far more than 700 unless almost every probationer is refused; the text states no admission rate. (iv) *What does close:* 7 provinces + 2 officers = 9 aboard (TBWTT-7:19); 8,400 + 700 = 9,100 = « un peu plus de neuf mille », × about ten robots each = « environ quatre-vingt-dix mille » (ETTMTTP-2:50, 2:54); "fiftieth generation" needs 50 × 18 = 900 years, inside the upper part of the stated range; 20 loaves × 5 = 100 men (TBWTT-3:138); 21 + 49 = 70 (TBWTT-6:8); 20 cubits = 9 m and 10 cubits = 4.50 m (same 0.45 m cubit, TBWTT-3:234–235).

Lifespan itself is stated five ways: ×10 (TBWTT-7:13, 7:30), 750–1,200 (7:30), 1,000 per body (7:30), « plus de sept cent cinquante » (7:46), and in book 2 « de sept-cents ans environ » (ETTMTTP-2:53). With the stated human mean of 75, ×10 = 750, the bottom of the range; 1,000 is ×13.3; book 2's 700 is below book 1's floor.

### F7. 666: the canon publishes the multiplication the core record declines to publish; the product closes, the premises sit uneasily with other canon numbers

**TEXT.**

QUOTE[LWTE-2:208]: si l'on multiplie la durée d'une génération humaine estimée à vingt ans par six cent soixante-six on obtient un total de treize mille trois cent vingt ans ENDQUOTE

**ANALYSIS.** 666 × 20 = 13,320 — closes. Counting back from the stated 1945 gives 11,375 BCE as an astronomical year number; that date is *not* in the canon (no BCE date for the creation of man is printed anywhere), it is the project's subtraction. « environ treize mille ans » counted from the 1979 publication gives about 11,020 BCE; the two differ by about 350 years, and they fall on opposite sides of the project lattice's Virgo/Leo boundary (11,010 BCE): 11,375 BCE is in the lattice's Age of Virgo, not Leo. The twenty-year generation is the canon's own stated assumption (« estimée à vingt ans »), in Yahweh's voice. It sits beside TBWTT-2:49, where the first humans' leaders live 930, 912 and 905 years, and beside the Elohim's own majority at 18–21. Core `number-of-man.md` (woh-claim-0050) forbids "publishing verification arithmetic"; the record should note that the arithmetic it withholds is in the source, with the multiplier stated.

### F8. "Seven teams" is not in the canon; "seven bases" and "seven provinces" are

**TEXT.**

QUOTE[TBWTT-2:25]: Le nombre d’équipes de créateurs est facile à trouver; chaque race humaine correspond à une équipe de créateurs. ENDQUOTE

QUOTE[TBWTT-3:292]: Les bases des créateurs étaient au nombre de sept : ENDQUOTE

QUOTE[TBWTT-7:19]: Sept, sur notre planète il y a sept provinces. ENDQUOTE

**ANALYSIS / NULL RESULT.** No passage gives a number of teams or of human races; « sept équipes » and « sept races » occur 0 times. The only "seven peoples" is Raël's question about the *home planet* (« Les sept peuples de votre monde », TBWTT-7:65), answered by « différentes races et différentes cultures » organised as provinces (TBWTT-7:66). Seven teams can be reached only by inference (teams = bases, or teams = home provinces); the text draws neither equation. Seven is nonetheless the canon's dominant number on the Elohim side: 7 bases, 7 indicator lights, 7 provinces, 7 + 2 crew, 7 billion inhabitants, 700 eternals, 70 probationers a year, 7c, waves 7× radio, a 7-metre craft, 7 guest rooms, 21 seats, 49-year leases, 7 Elohim at table (ETTMTTP-2:48), 8,400 = 12 × 700 re-created humans, 700 movement members in 1975 (ETTMTTP-1:3). This is a pattern observation; I draw no inference from it.

### F9. Continental chronology: three passages, three clocks

**TEXT.** Raël, book 3 ch. 1: drift is the fading aftermath of the *creation* of the continent over 25 millennia (LWTE-1:31, quoted in F1), with initial rates of « plusieurs centaines de kilomètres chaque année ». Terrusse, book 3 ch. 4: the continent broke at the *Flood*:

QUOTE[LWTE-4:42]: Pendant les milliers d'années qui séparèrent la création du continent originel par les Elohim de la période du déluge et des destructions ENDQUOTE

Yahweh, book 1: after the Flood and after Babel the scientists are scattered « sur tout le continent » (TBWTT-2:76) — the single continent is still spoken of as one.

**ANALYSIS.** With the Flood at about 5,000 years ago (LWTE-1:47, Raël), Terrusse's breakup leaves about 5,000 years for the Atlantic to open — an average on the order of a kilometre a year — where Raël's answer in the same book allows 25,000. The two book-3 voices assign the drift to different events. Core `continental-breakup-at-the-flood.md` (woh-claim-0071, review 0001) already attributes the breakup passage to Terrusse and cites the 25,000-year question; the TBWTT-2:76 counter-wording and the "5,000 years" interval implied by LWTE-1:47 are worth adding if not already carried.

### F10. Smaller tensions

- **"First atomic explosion".** TBWTT-1:47 dates the choice of a messenger « après la première explosion atomique qui eut lieu en 1945 »; book 3 specifies « le 6 août 1945 à Hiroshima » (LWTE-2:79) and words it more narrowly as « la première utilisation à des fins meurtrières » (LWTE-2:209). The first nuclear explosion was the Trinity test of July 1945 [outside knowledge — unverified, needs source].
- **Six days.** « six jours de suite » is stable (TBWTT-7:16, 7:76; ETTMTTP-1:63, 2:10). The narrative marks only four « Le lendemain » breaks (TBWTT-2:1, 3:2, 5:2, 6:1), i.e. five sittings; the sixth must be an unmarked break at ch. 4 or ch. 7.
- **Created worlds.** Book 1: three failures then three successes (TBWTT-4:49). Book 3, Yahweh: « nous qui avons l'habitude de créer la vie sur une infinité de planètes » (LWTE-2:98); Raël: « une infinité de créations sur notre planète » (LWTE-1:15).
- **Odds.** Humanity's chance of survival is 1 in 100 (LWTE-1:72, 2:96, 2:231) in Raël's and Yahweh's voices, but 1 in 10 in Raël's reply to Satan (« neuf chances sur dix », LWTE-2:68).
- **The council.** 700 members (TBWTT-7:45; ETTMTTP-2:50); before John, Yahweh sits with « vingt-quatre autres éternels représentant le conseil » (LWTE-2:128) — compatible, the 24 being delegates.
- **Hertz.** A witness dates Hertz's discovery to « les années 1920 » (LWTE-4:73, Terrusse); Hertz's experiments were in the 1880s [outside knowledge — unverified, needs source].
- **Conception to birth.** 25 December 1945 to 30 September 1946 is 279 days (ETTMTTP-1:7) — unremarkable.
- **Second contact.** Departure around midnight on 7 October 1975, return at « minuit » (ETTMTTP-2:9, 2:131): about 24 hours, matching LWTE-1:2.

## Sub-question (3): chronological skeleton

Ordered oldest first. "BP" = years before the statement; no BCE date below is in the canon.

| When (text's own anchor) | Event | REF | Voice |
|---|---|---|---|
| undated, before all else | Elohim themselves created by visitors; creators' ship lands automatically when their world is destroyed | TBWTT-7:25 (cf. LWTE-2:28, where the Elohim learn this only at the Flood) | Yahweh / Raël |
| undated | synthetic life made on the home planet; banned; Satan's party | LWTE-2:6–7 | Raël |
| undated | three failed off-world attempts, then Earth; two other successes | TBWTT-4:49; LWTE-2:10–17 | Yahweh / Raël |
| 10,000–20,000 years before the arrival (hypothetical) | an earlier, destroyed creation on Earth | LWTE-1:15 | Raël |
| 25,000 BP | Yahweh born (age 25,000); landing on Earth; travel at 7c | TBWTT-7:56; ETTMTTP-2:43 | Yahweh |
| 25,000 BP | life / original continent created (book-3 usage) | LWTE-1:13, 1:30–31 | Questioner, Raël |
| 22,000 BP | creators "decided to do their work on Earth" | TBWTT-5:4 | Yahweh |
| each "day" ≈ 2,000 years | survey; continent; plants; astronomy; sea life and birds; land animals; man | TBWTT-2:10–25 | Yahweh |
| ≈ 13,000 BP (13,320 before 1945) | first humans made in the laboratories | LWTE-2:208 | Yahweh |
| "thousands of years" | interval from the continent's creation to the Flood | LWTE-4:42 | Terrusse |
| ≈ 5,000 BP | the real Flood; ark in orbit a few thousand km up | LWTE-1:47; TBWTT-2:58 | Raël; Yahweh |
| after the Flood (undated) | Babel; Sodom; Moses; the prophets | TBWTT-2:72–3:303 | Yahweh |
| ≈ 2,000 BP | Jesus; passage into the age of Pisces at the crucifixion | TBWTT-5:12; ETTMTTP-2:62 | Yahweh |
| 1945 (6 August) | Hiroshima; decision to send the last prophet; age of the Apocalypse begins; 666th generation born | TBWTT-1:47; LWTE-2:79, 2:85, 2:208–209, 3:79 | Yahweh / Raël |
| 25 December 1945 | Raël conceived | ETTMTTP-1:7 | Raël |
| 1946 | year 1; Aquarius begins; Israel "regains its land" | TBWTT-5:1, 5:4; ETTMTTP-3:172 | Narrator / Yahweh |
| 30 September 1946, about 02:00 | Raël born at Vichy | ETTMTTP-1:7 | Raël |
| 1947 | grandmother's sighting over Ambert | ETTMTTP-1:10 | Raël |
| age 7, 9, 14, 15, 18, 22 (c. 1953–1968) | childhood and career milestones | ETTMTTP-1:13–53 | Raël |
| c. 1970–71 ("three years ago" in 1973) | motoring magazine founded | TBWTT-1:1; ETTMTTP-1:61 | Raël |
| 13 December 1973, then six days running | first contact; dictation about an hour a day | TBWTT-1:2, 7:16; ETTMTTP-1:63 | Raël |
| autumn 1974 | first book printed | ETTMTTP-1:70 | Raël |
| June 1975; 31 July; 6 August 1975 | resignation from MADECH; sighting; gathering | ETTMTTP-2:1, 2:5, 2:7 | Raël |
| 7 October 1975 (year 30), about 23:00 to midnight next day | second contact; about 24 hours away | ETTMTTP-2:9, 2:131; LWTE-1:2 | Raël / Questioner |
| late 1975 | 700 members; about 40 lectures | ETTMTTP-1:3, 1:5 | Raël |
| 1976 = year 31 | dating rule's worked example | ETTMTTP-3:172 | Yahweh |
| October 1975 + 3 years | embargo on the Satan test and the paternity disclosure expires | LWTE-2:1, 2:90 | Editor / Raël |
| 1979 = year 34 (22 May 1979 = "an 33") | book 3; 3,000 members | LWTE-2:2, 3:76, 4:219 | Editor / Raël / Deydier |
| future, undated | 144,000 sealed before any final cataclysm; Raëlism dominant in "the third millennium" | LWTE-2:158–159, 1:36 | Yahweh / Raël |

## Sub-question (4): project numbers checked against the canon

| Project figure | In the canon? | What the canon says instead |
|---|---|---|
| Ages of 2,160 years | No (0 occurrences) | « deux mille ans terrestres environ » (TBWTT-2:10) |
| Great Year 25,920; twelve ages; named ages other than Pisces/Aquarius | No | no cycle length, no count of signs, only Poissons and Verseau |
| Cycle opening c. 21,810 BCE (Capricorn) | No | 22,000 years since a *decision* (TBWTT-5:4); 25,000 years since the landing (ETTMTTP-2:43). 21,810 BCE is 23,760 years before 1950, matching neither |
| Aquarius 1950–4110 | No | « depuis 1946 » (TBWTT-5:4); age of the Apocalypse « Depuis 1945 » (LWTE-3:79); no end date |
| Pisces from 210 BCE | No | passage into Pisces at the crucifixion (TBWTT-5:12) |
| 11,375 BCE | No (derived) | 13,320 years, and 1945, both stated in LWTE-2:208; the subtraction is the project's |
| 666 generations × ? | Yes | × 20 years = 13,320, multiplication printed in the text (LWTE-2:208) |
| Seven teams | No | number of teams = number of human races, unstated (TBWTT-2:25); seven *bases* (TBWTT-3:292) |
| Flood / breakup at the opening of Gemini, c. 6,690 BCE (core `continental-breakup-at-the-flood.md`) | No | « environ cinq mille ans » ago (LWTE-1:47, Raël), i.e. about 3,000 BCE — some 3,700 years later, inside the lattice's Age of Taurus |
| Creation of man at the Leo boundary | Partly | 13,000 years before 1979 ≈ 11,020 BCE is within about ten years of the lattice's Leo start (11,010 BCE); 13,320 before 1945 is not |

## Tensions and null results (summary list)

1. 25,000 = age of Yahweh = lead = landing = creation of life/continent (F1). Tension.
2. Eternals initiate off-world creation (TBWTT-7:31) but the first eternal is only as old as the landing (TBWTT-7:56; ETTMTTP-2:43). Tension.
3. 22,000 (decision) vs 25,000 (landing). Reconcilable, not reconciled by the text (F2).
4. 25,000 − 6 × 2,000 = 13,000. Closes; sum never stated (F2).
5. Day = about 2,000 years, not 2,160; Pisces from the crucifixion (F3). Canon vs project.
6. Era epoch 1946 vs 1945; "an 33" vs "an 34" in 1979 (F4). Tension.
7. Under one light-year vs nearest star at about four (LWTE-1:26–27). Raised and left hypothetical by the canon.
8. Distance published vs location withheld (TBWTT-5:52 vs 5:57; LWTE-1:27). Tension.
9. 7c and two months: present tense in book 1, back-dated 25,000 years in book 2. Revision between books.
10. Residence of the eternals: « sur notre planète » (book 1) vs a separate planet (book 2). Revision, flagged by book 2 itself.
11. 40 million children; 210 probationers; 700 perpetual members (F6). Sums do not close.
12. Lifespan: 700 / >750 / 750–1,200 / 1,000 / ×10. Loose.
13. Twenty-year generations vs 900-year patriarchs (F7). Tension of premises.
14. Continental drift: since the creation (25,000) vs since the Flood (about 5,000) vs one continent after Babel (F9). Tension across voices.
15. Three successes vs "an infinity" of created planets. Tension.
16. Survival odds 1/100 vs 1/10. Loose.
17. Null: no precession term, no zodiac term, no 2,160/25,920, no BCE date of any kind, no number of teams or races, no distance for the planet of the eternals, no end date for Aquarius, no date for Babel, Sodom, Moses or any prophet other than Jesus (« deux mille ans »).
18. Closing sums: all five parasang/speed conversions; 25 bodies × 1,000; 7 + 2 = 9; 8,400 + 700; 9,100 × 10; 666 × 20; 21 + 49; cubit conversions; loaves × 5; era rule 1946 = 1 → 1975 = 30, 1976 = 31, 1979 = 34.

## Relation to existing core records

- `precessional-world-age-chronology.md` (woh-claim-0003): consistent with its statement that 2,160 and the 1950 anchor are conventions. New: the canon's own unit (about 2,000), its Pisces boundary (crucifixion), the absence of any twelve-fold or cycle statement, and the two competing canon figures (22,000, 25,000) against which 21,810 BCE is not a rounding of either.
- `creation-week-ages.md` (woh-claim-0059): the record's "roughly 2,160 years" is the lattice's figure; the canon's is « deux mille ans … environ ». The 25,000 → 13,000 closure (F2) holds only on the canon's figure.
- `number-of-man.md` (woh-claim-0050): the multiplication and the 20-year multiplier are canon-explicit (F7).
- `kabbalah-shiur-qomah-anchor.md` (woh-claim-0021) and its evidence map: the light-second gloss is canon-explicit in TBWTT-5:52, not an article development (F5).
- `continental-breakup-at-the-flood.md` (woh-claim-0071): compatible; adds TBWTT-2:76 and the 5,000-year interval (F9).
- `menorah-base-network.md`: consistent ("the canon's seven and no site"). F8 adds that teams are a different, unnumbered quantity.
- `scientific-immortality.md` / woh-claim-0029 (8,400 re-created): consistent; adds the 144,000 ceiling « y compris ceux qui ont déjà été recréés » (LWTE-2:158) and the 700/210/70 figures with their non-closure.
- `year-one-unsealing.md`: its "1945/1946 threshold" should be split by book (F4).
- woh-claim-0072 evidence map (Sendy): already separates 22,000 from 25,000; this note adds the book-by-book distribution.

## Candidate claims or revisions for founder review (proposals, not decisions)

- **P1 (revision, woh-claim-0021).** Re-grade the parasang = light-second equation and its conversions from "article development, inferred" to "canon-explicit (TBWTT-5:52–53)"; keep the units-retrofit objection.
- **P2 (revision, woh-claim-0003 / 0059).** Add a "canon's own figures" paragraph: day ≈ 2,000 years; Pisces from the crucifixion; Aquarius from 1946; no cycle length; 22,000 and 25,000 as the only deep anchors. State that the lattice is the project's, at a declared offset from each.
- **P3 (revision, woh-claim-0050).** Record that LWTE-2:208 prints 666 × 20 = 13,320 with 1945 as terminus; "11,375 BCE" to be labelled a project subtraction wherever it appears, with the 11,020 alternative.
- **P4 (new descriptive record, candidate).** "The canon's numerical chronology": a `direct`-about-the-source record listing 25,000 / 22,000 / 13,000 / 5,000 / 2,000 / 1945–46 with voices, plus the F1 and F2 observations, as the auditable base under the timeline.
- **P5 (new descriptive record, candidate).** "The 25,000 figure": the four referents and the eternals/landing ordering problem, tensions carried, no resolution asserted.
- **P6 (editorial check).** Any public page that says "seven teams" or "seven races" as canon: re-word to "seven bases" or mark as inference.
- **P7 (editorial check).** Timeline placement of the Flood (c. 6,690 BCE in core) against LWTE-1:47's « environ cinq mille ans »; the canon's 13,000 − 5,000 leaves about 8,000 antediluvian years, the lattice about 4,700.
- **P8 (note for woh-claim-0031 or the era record).** Separate the 1946 epoch (books 1–2, Aquarius/year 1) from the 1945 epoch (book 3, Apocalypse/6 August) and record the "an 33/an 34" discrepancy.

## Limitations

- Read from the project's French digitization, not from the 1974/1975/1979 printings; typographic variants (« vingtcinq », « ving-cinq », « 236 000» parasanges» ») are the dump's. Later-edition intrusions exist in LWTE (the "Depuis 1998…" notes), so some page references in LWTE ch. 1 are editorial.
- The sweep keyed on digits and number words; a quantity expressed without either (e.g. « longtemps », « bientôt ») is not registered. Numerals inside Bible quotations are sampled.
- Demographic "closure" tests assume a stationary population and uniform lifespans; the text asserts constancy (TBWTT-7:13) but not uniformity.
- No outside source was consulted; every outside constant is marked as such and needs a source before use.
- The Shi'ur Qomah attestation of 236,000 and 30,000,000 was not re-checked here (core woh-claim-0021 covers it).
- I did not check the English translation against the French for numerals.

## Full register (213 items)

Class key: K canon doctrine/cosmology · C contact narrative · B biography/movement · Q biblical or quoted figure glossed by the canon · H hypothetical/illustration · P prescription · W third-party witness (LWTE ch. 4). Structured copy: `numerics.json`.

- **N001** `TBWTT-1:1` · 9 · years (age) · age at which Raël's passion for motor sport began · voice: Raël · class B

  QUOTE[TBWTT-1:1]: Depuis l’âge de neuf ans ENDQUOTE

- **N002** `TBWTT-1:1` · 3 · years · time since he founded his motoring magazine (i.e. c. 1970-71) · voice: Raël · class B

  QUOTE[TBWTT-1:1]: voilà trois ans ENDQUOTE

- **N003** `TBWTT-1:1` · ~10 · trophies · racing cups won · voice: Raël · class B

  QUOTE[TBWTT-1:1]: une dizaine de coupes ENDQUOTE

- **N004** `TBWTT-1:2` · 1973-12-13 · date · first encounter · voice: Raël · class C

  QUOTE[TBWTT-1:2]: ce matin du 13 décembre 1973 ENDQUOTE

- **N005** `TBWTT-1:3` · a few thousand · years ago · when lava last flowed at the Auvergne volcano (Raël's own remark) · voice: Raël · class B

  QUOTE[TBWTT-1:3]: voici quelques milliers d’années ENDQUOTE

- **N006** `TBWTT-1:4` · ~20 · m · altitude of craft when first seen as flattened · voice: Raël · class C

  QUOTE[TBWTT-1:4]: une vingtaine de mètres d’altitude ENDQUOTE

- **N007** `TBWTT-1:4` · ~7 · m · diameter of the small craft · voice: Raël · class C

  QUOTE[TBWTT-1:4]: environ sept mètres de diamètre ENDQUOTE

- **N008** `TBWTT-1:4` · ~2.5 · m · height of the small craft · voice: Raël · class C

  QUOTE[TBWTT-1:4]: haute d’environ deux mètres cinquante ENDQUOTE

- **N009** `TBWTT-1:5` · 2 · m · hover height · voice: Raël · class C

  QUOTE[TBWTT-1:5]: s’immobilisa à deux mètres du sol ENDQUOTE

- **N010** `TBWTT-1:6` · ~1.20 · m · stature of the Eloha · voice: Raël · class C

  QUOTE[TBWTT-1:6]: sa taille voisine d’un mètre vingt ENDQUOTE

- **N011** `TBWTT-1:6` · ~10 · m · distance at which the Eloha stopped · voice: Raël · class C

  QUOTE[TBWTT-1:6]: une dizaine de mètres de moi ENDQUOTE

- **N012** `TBWTT-1:22` · 2 · children · Raël's children in 1973 · voice: Yahweh · class B

  QUOTE[TBWTT-1:22]: père de deux enfants ENDQUOTE

- **N013** `TBWTT-1:41` · 2 · seats · seats in small craft · voice: Raël · class C

  QUOTE[TBWTT-1:41]: deux fauteuils face à face ENDQUOTE

- **N014** `TBWTT-1:47` · 1945; 1946 · years · first atomic explosion; Raël's birth year · voice: Yahweh · class K

  QUOTE[TBWTT-1:47]: la première explosion atomique qui eut lieu en 1945 et vous êtes né en 1946 ENDQUOTE

- **N015** `TBWTT-1:64` · ~400 · m · altitude before craft vanished (day 1) · voice: Raël · class C

  QUOTE[TBWTT-1:64]: jusqu’à environ 400 mètres ENDQUOTE

- **N016** `TBWTT-2:10` · ~2,000 · Earth years · length of a Genesis "day" = period the sun rises in the same sign at the spring equinox · voice: Yahweh · class K

  QUOTE[TBWTT-2:10]: soit deux mille ans terrestres environ ENDQUOTE

- **N017** `TBWTT-2:25` · unspecified ("easy to find") · teams · number of creator teams = number of human races; no figure given · voice: Yahweh · class K

  QUOTE[TBWTT-2:25]: chaque race humaine correspond à une équipe de créateurs ENDQUOTE

- **N018** `TBWTT-2:43` · x10 · ratio · hypothetical human lifespan with life-extension · voice: Yahweh · class K

  QUOTE[TBWTT-2:43]: dix fois plus longtemps ENDQUOTE

- **N019** `TBWTT-2:49` · 930; 912; 905 · years · Genesis 5 lifespans, accepted as real ("tree of life") · voice: Yahweh · class Q

  QUOTE[TBWTT-2:49]: Adam neuf cent trente ans, Seth neuf cent douze ans, Énosh neuf cent cinq ans ENDQUOTE

- **N020** `TBWTT-2:52` · 120 · years · Gen 6:3, quoted · voice: Yahweh · class Q

  QUOTE[TBWTT-2:52]: Ses jours seront de cent vingt ans ENDQUOTE

- **N021** `TBWTT-2:58` · a few thousand · km · orbital altitude of the ark during the Flood strike · voice: Yahweh · class K

  QUOTE[TBWTT-2:58]: à quelques milliers de kilomètres au-dessus de la Terre ENDQUOTE

- **N022** `TBWTT-2:61` · 150 · days · Gen 7:24, quoted · voice: Yahweh · class Q

  QUOTE[TBWTT-2:61]: durant cent cinquante jours ENDQUOTE

- **N023** `TBWTT-2:62` · 3 · stages · the ark as three-stage rocket (from Gen 6:16) · voice: Yahweh · class K

  QUOTE[TBWTT-2:62]: la fusée à trois étages ENDQUOTE

- **N024** `TBWTT-2:62` · 1 couple per race · people · human cargo of the ark besides Noah · voice: Yahweh · class K

  QUOTE[TBWTT-2:62]: un couple de chaque race humaine ENDQUOTE

- **N025** `TBWTT-2:78` · 2 · persons · scouts sent to Sodom · voice: Yahweh · class K

  QUOTE[TBWTT-2:78]: deux espions ENDQUOTE

- **N026** `TBWTT-2:92` · ~400 · m · altitude at which craft glowed and vanished (day 2) · voice: Raël · class C

  QUOTE[TBWTT-2:92]: à 400 mètres environ ENDQUOTE

- **N027** `TBWTT-3:75` · 300 · men · Gideon's men (Judges 7) · voice: Yahweh · class Q

  QUOTE[TBWTT-3:75]: les 300 hommes ENDQUOTE

- **N028** `TBWTT-3:138` · x5 · ratio · expansion of dehydrated synthetic food · voice: Yahweh · class K

  QUOTE[TBWTT-3:138]: correspond à cinq fois plus de volume ENDQUOTE

- **N029** `TBWTT-3:138` · 20 -> 100 · loaves -> men · gloss on 2 Kings 4:42-44 · voice: Yahweh · class Q

  QUOTE[TBWTT-3:138]: Avec vingt petits «pains», il y a suffisamment de nourriture pour cent hommes ENDQUOTE

- **N030** `TBWTT-3:145` · 6 (2+2+2) · thrusters · seraph's "six wings" as suit thrusters · voice: Yahweh · class K

  QUOTE[TBWTT-3:145]: six petits réacteurs : deux dans le dos, deux aux mains et deux aux pieds ENDQUOTE

- **N031** `TBWTT-3:163` · 4 · persons · Ezekiel's four living beings · voice: Yahweh · class K

  QUOTE[TBWTT-3:163]: Quatre créateurs ENDQUOTE

- **N032** `TBWTT-3:165` · 4 · portholes · "four faces" as helmet ports · voice: Yahweh · class K

  QUOTE[TBWTT-3:165]: ses quatre hublots ENDQUOTE

- **N033** `TBWTT-3:207` · 3 · men · Daniel 3 furnace (a fourth = a creator) · voice: Yahweh · class Q

  QUOTE[TBWTT-3:207]: trois hommes ENDQUOTE

- **N034** `TBWTT-3:225` · a few tens · years ago · creation of the State of Israel, relative to 1973 · voice: Yahweh · class K

  QUOTE[TBWTT-3:225]: voici quelques dizaines d’années ENDQUOTE

- **N035** `TBWTT-3:229` · 3 · days and nights · Jonah in the "fish" (submarine) · voice: Yahweh · class Q

  QUOTE[TBWTT-3:229]: trois jours et trois nuits ENDQUOTE

- **N036** `TBWTT-3:234` · 20 · cubits · flying scroll length (Zech 5) · voice: Yahweh · class Q

  QUOTE[TBWTT-3:234]: d’une longueur de vingt coudées ENDQUOTE

- **N037** `TBWTT-3:235` · 9; 4.50 (10 cubits) · m · conversion of the cubits -> 0.45 m per cubit · voice: Yahweh · class Q

  QUOTE[TBWTT-3:235]: (9 mètres) et d’une largeur de dix coudées (4,50 mètres) ENDQUOTE

- **N038** `TBWTT-3:238` · 2 · persons · Zech 5:9 women · voice: Yahweh · class K

  QUOTE[TBWTT-3:238]: Deux compagnes féminines ENDQUOTE

- **N039** `TBWTT-3:292` · 7 · bases · number of the creators' bases on Earth · voice: Yahweh · class K

  QUOTE[TBWTT-3:292]: Les bases des créateurs étaient au nombre de sept ENDQUOTE

- **N040** `TBWTT-3:294` · 7 · indicator lights · HQ console = menorah · voice: Yahweh · class K

  QUOTE[TBWTT-3:294]: un central comportant sept témoins lumineux ENDQUOTE

- **N041** `TBWTT-4:48` · 100; 60; 30 · yield · Matt 13:8, quoted · voice: Yahweh · class Q

  QUOTE[TBWTT-4:48]: celle-ci cent, celle-là soixante, celle-là trente ENDQUOTE

- **N042** `TBWTT-4:49` · 3 · failed attempts · life-creation attempts on other planets that failed · voice: Yahweh · class K

  QUOTE[TBWTT-4:49]: trois tentatives échouèrent ENDQUOTE

- **N043** `TBWTT-4:49` · 4th · attempt · first success · voice: Yahweh · class K

  QUOTE[TBWTT-4:49]: la quatrième tentative fut un succès ENDQUOTE

- **N044** `TBWTT-4:49` · 3 · successes · inhabited created worlds (Earth + 2) · voice: Yahweh · class K

  QUOTE[TBWTT-4:49]: il y a eu trois succès ENDQUOTE

- **N045** `TBWTT-4:49` · 2 · planets · other worlds with humans made by the same creators · voice: Yahweh · class K

  QUOTE[TBWTT-4:49]: sur deux autres planètes relativement proches ENDQUOTE

- **N046** `TBWTT-4:55` · 3 · planets · worlds in competition for the heritage · voice: Yahweh · class K

  QUOTE[TBWTT-4:55]: Les trois planètes où la vie a été créée ont été mises en compétition ENDQUOTE

- **N047** `TBWTT-4:64` · thousands · men · loaves miracle as concentrated food · voice: Yahweh · class Q

  QUOTE[TBWTT-4:64]: de quoi nourrir des milliers d’hommes ENDQUOTE

- **N048** `TBWTT-4:71` · a few tens · years · how long humanity has been on the road of scientific development · voice: Yahweh · class K

  QUOTE[TBWTT-4:71]: depuis quelques dizaines d’années ENDQUOTE

- **N049** `TBWTT-4:81` · 5 (then 2, 1) · talents · Matt 25 parable = three planets · voice: Yahweh · class Q

  QUOTE[TBWTT-4:81]: Le premier a reçu cinq talents ENDQUOTE

- **N050** `TBWTT-4:91` · >12 · legions · Matt 26:53, quoted · voice: Yahweh · class Q

  QUOTE[TBWTT-4:91]: plus de douze légions d’anges ENDQUOTE

- **N051** `TBWTT-5:1` · 1946 = year 1 · era · chapter title: epoch of the new era · voice: Narrator · class K

  QUOTE[TBWTT-5:1]: 1946, an 1 de l’ère nouvelle ENDQUOTE

- **N052** `TBWTT-5:4` · 22,000 · years · time since the creators decided to do their work on Earth · voice: Yahweh · class K

  QUOTE[TBWTT-5:4]: Depuis vingt-deux mille ans que les créateurs décidèrent de faire leur œuvre sur Terre ENDQUOTE

- **N053** `TBWTT-5:4` · 1946 · year · Aquarius begins; "epoch when Israel regains its land" · voice: Yahweh · class K

  QUOTE[TBWTT-5:4]: le Verseau, qui suit, est là depuis 1946 ENDQUOTE

- **N054** `TBWTT-5:7` · 1946 · year · Raël's birth year tied to Aquarius · voice: Yahweh · class K

  QUOTE[TBWTT-5:7]: si vous êtes né en 1946 ce n’est pas par hasard ENDQUOTE

- **N055** `TBWTT-5:51` · 236,000 · parasangs · "height of the creator" (attributed to Kabbalah / Song of Songs V) · voice: Yahweh · class K

  QUOTE[TBWTT-5:51]: la «hauteur du créateur» est de 236 000» parasanges» ENDQUOTE

- **N056** `TBWTT-5:51` · 30,000,000 · parasangs · "height of his heels" · voice: Yahweh · class K

  QUOTE[TBWTT-5:51]: la «hauteur de ses talons» est de 30 millions de «parasanges» ENDQUOTE

- **N057** `TBWTT-5:52` · ~300,000 · km (= 1 light-second) · definition of the parasang · voice: Yahweh · class K

  QUOTE[TBWTT-5:52]: la distance que parcourt la lumière en une seconde soit environ 300 000 kilomètres ENDQUOTE

- **N058** `TBWTT-5:52` · ~9 x 10^12; <1 · km; light-year · distance home planet - Earth · voice: Yahweh · class K

  QUOTE[TBWTT-5:52]: soit neuf mille milliards de kilomètres environ ou un peu moins d’une année lumière ENDQUOTE

- **N059** `TBWTT-5:52` · ~1 (just under) · year · travel time at light speed · voice: Yahweh · class K

  QUOTE[TBWTT-5:52]: vous mettriez presque un an ENDQUOTE

- **N060** `TBWTT-5:52` · 40,000 · km/h · speed of current terrestrial rockets · voice: Yahweh · class K

  QUOTE[TBWTT-5:52]: qui ne se déplacent qu’à 40 000 km/h ENDQUOTE

- **N061** `TBWTT-5:52` · ~26,000 · years · rocket travel time to the home planet · voice: Yahweh · class K

  QUOTE[TBWTT-5:52]: près de 26 000 ans ENDQUOTE

- **N062** `TBWTT-5:53` · <2 · months · Elohim travel time, home planet - Earth · voice: Yahweh · class K

  QUOTE[TBWTT-5:53]: en moins de deux mois ENDQUOTE

- **N063** `TBWTT-5:53` · 7c · speed · speed of the carrier "rays" · voice: Yahweh · class K

  QUOTE[TBWTT-5:53]: sept fois plus rapides que la lumière ENDQUOTE

- **N064** `TBWTT-5:53` · 70.8 x 10^9 · km · distance of the home planet from its sun ("a large star") · voice: Yahweh · class K

  QUOTE[TBWTT-5:53]: 236 000 parasanges, soit 70 milliards huit cent millions de kilomètres ENDQUOTE

- **N065** `TBWTT-5:56` · 25,000 · years · scientific head-start humans would gain · voice: Yahweh · class K

  QUOTE[TBWTT-5:56]: en leur faisant ainsi gagner 25 000 ans ENDQUOTE

- **N066** `TBWTT-5:57` · x7 · ratio · speed of Elohim communication waves vs radio · voice: Yahweh · class K

  QUOTE[TBWTT-5:57]: sept fois plus rapides que les ondesradioélectriques ENDQUOTE

- **N067** `TBWTT-5:57` · x1.5 (=> 10.5 x radio) · ratio · new waves under trial · voice: Yahweh · class K

  QUOTE[TBWTT-5:57]: une fois et demie plus rapide que ces dernières ENDQUOTE

- **N068** `TBWTT-6:5` · +50% · IQ above mean · eligibility threshold for office (geniocracy) · voice: Yahweh · class P

  QUOTE[TBWTT-6:5]: supérieur de 50% à la moyenne ENDQUOTE

- **N069** `TBWTT-6:5` · +10% · IQ above mean · threshold to vote · voice: Yahweh · class P

  QUOTE[TBWTT-6:5]: supérieur de 10% à la moyenne ENDQUOTE

- **N070** `TBWTT-6:7` · 49 · years · maximum lease of any property · voice: Yahweh · class P

  QUOTE[TBWTT-6:7]: loués pour quarante-neuf ans ENDQUOTE

- **N071** `TBWTT-6:8` · 70 = 21 + 49 · years (age) · age at which the house is paid off · voice: Yahweh · class P

  QUOTE[TBWTT-6:8]: À soixante-dix ans (21 +49) ENDQUOTE

- **N072** `TBWTT-6:8` · 100,000 · francs · example house value · voice: Yahweh · class H

  QUOTE[TBWTT-6:8]: cent mille francs ENDQUOTE

- **N073** `TBWTT-6:11` · 7 x 7 = 49 · years · Lev 25:8, source of the 49 · voice: Yahweh · class Q

  QUOTE[TBWTT-6:11]: sept fois sept années : (...) quarante-neuf ans ENDQUOTE

- **N074** `TBWTT-6:21` · 7 · rooms · guest rooms of the residence (embassy) · voice: Yahweh · class P

  QUOTE[TBWTT-6:21]: comprenant sept chambres ENDQUOTE

- **N075** `TBWTT-6:21` · >=21 · persons · conference-room and dining-room capacity · voice: Yahweh · class P

  QUOTE[TBWTT-6:21]: au moins vingt et une personnes ENDQUOTE

- **N076** `TBWTT-6:21` · >=1000 · m · distance residence - perimeter wall · voice: Yahweh · class P

  QUOTE[TBWTT-6:21]: au moins à 1000 mètres du mur ENDQUOTE

- **N077** `TBWTT-6:21` · 12 · m · craft the roof terrace must take · voice: Yahweh · class P

  QUOTE[TBWTT-6:21]: un engin de douze mètres de diamètre ENDQUOTE

- **N078** `TBWTT-7:13` · 2 · children per woman · prescribed birth limit · voice: Yahweh · class P

  QUOTE[TBWTT-7:13]: n’autorisant les femmes à avoir que deux enfants ENDQUOTE

- **N079** `TBWTT-7:13` · 75 · years · average human lifespan · voice: Yahweh · class K

  QUOTE[TBWTT-7:13]: soixante-quinze ans en moyenne ENDQUOTE

- **N080** `TBWTT-7:13` · x10 · ratio · Elohim lifespan after the operation · voice: Yahweh · class K

  QUOTE[TBWTT-7:13]: dix fois plus longtemps que vous ENDQUOTE

- **N081** `TBWTT-7:15` · ~7 x 10^9 · persons · population of the home planet · voice: Yahweh · class K

  QUOTE[TBWTT-7:15]: Nous sommes environ 7 milliards ENDQUOTE

- **N082** `TBWTT-7:16` · 6 · consecutive days · meetings of December 1973 · voice: Raël · class C

  QUOTE[TBWTT-7:16]: six jours de suite ENDQUOTE

- **N083** `TBWTT-7:19` · 7 · provinces · divisions of the home planet · voice: Yahweh · class K

  QUOTE[TBWTT-7:19]: il y a sept provinces ENDQUOTE

- **N084** `TBWTT-7:19` · 9 (7 + 2) · persons · crew of the base ship near Earth · voice: Yahweh · class K

  QUOTE[TBWTT-7:19]: nous sommes en permanence neuf ENDQUOTE

- **N085** `TBWTT-7:21` · 25,000 · years · Elohim scientific lead · voice: Yahweh · class K

  QUOTE[TBWTT-7:21]: nos vingt-cinq mille ans d’avance scientifique ENDQUOTE

- **N086** `TBWTT-7:30` · 750-1,200 · years · Elohim bodily lifespan · voice: Yahweh · class K

  QUOTE[TBWTT-7:30]: Entre sept cent cinquante et mille deux cents ans ENDQUOTE

- **N087** `TBWTT-7:30` · 1,000 · years · life expectancy of each re-created body · voice: Yahweh · class K

  QUOTE[TBWTT-7:30]: mille de vos années à vivre ENDQUOTE

- **N088** `TBWTT-7:31` · 3 · lives · probation before perpetual council membership · voice: Yahweh · class K

  QUOTE[TBWTT-7:31]: Durant trois existences, l’éternel est stagiaire ENDQUOTE

- **N089** `TBWTT-7:45` · 700 · persons · eternals among 7 billion · voice: Yahweh · class K

  QUOTE[TBWTT-7:45]: il n’y a que sept cents éternels ENDQUOTE

- **N090** `TBWTT-7:46` · 210; ~70/yr; 10/province · persons · probationer eternals and intake rate · voice: Yahweh · class K

  QUOTE[TBWTT-7:46]: deux cent dix stagiaires (environ soixante-dix par an soit dix par province) ENDQUOTE

- **N091** `TBWTT-7:46` · ~40 x 10^6 · children · children among 7 billion · voice: Yahweh · class K

  QUOTE[TBWTT-7:46]: quarante millions d’enfants environ ENDQUOTE

- **N092** `TBWTT-7:46` · 18-21 · years (age) · majority / age of the longevity operation · voice: Yahweh · class K

  QUOTE[TBWTT-7:46]: entre dix-huit et vingt et un ans ENDQUOTE

- **N093** `TBWTT-7:46` · >750 · years · longevity conferred · voice: Yahweh · class K

  QUOTE[TBWTT-7:46]: une longévité de plus de sept cent cinquante ans ENDQUOTE

- **N094** `TBWTT-7:46` · 50th · generation · descendants the oldest ordinary inhabitants live to know · voice: Yahweh · class K

  QUOTE[TBWTT-7:46]: jusqu’à la cinquantième génération ENDQUOTE

- **N095** `TBWTT-7:46` · ~10^6 · persons · inactive (mostly under ~6 months' treatment) · voice: Yahweh · class K

  QUOTE[TBWTT-7:46]: qu’un million d’inactifs ENDQUOTE

- **N096** `TBWTT-7:47` · 500,000 · inhabitants · average city · voice: Yahweh · class K

  QUOTE[TBWTT-7:47]: en moyenne de cinq cent mille habitants ENDQUOTE

- **N097** `TBWTT-7:47` · ~1 · km (cube edge) · size of a "city-house" · voice: Yahweh · class K

  QUOTE[TBWTT-7:47]: à peu près un kilomètre de côté et de haut ENDQUOTE

- **N098** `TBWTT-7:47` · x20 · ratio · footprint of an Earth city of 500,000 vs theirs · voice: Yahweh · class K

  QUOTE[TBWTT-7:47]: couvre vingt fois plus de surface ENDQUOTE

- **N099** `TBWTT-7:56` · 25,000 · years (age) · age of Yahweh, oldest eternal · voice: Yahweh · class K

  QUOTE[TBWTT-7:56]: a vingtcinq mille ans ENDQUOTE

- **N100** `TBWTT-7:56` · 25 · bodies · Yahweh's successive bodies · voice: Yahweh · class K

  QUOTE[TBWTT-7:56]: J’ai habité 25 corps jusqu’à ce jour ENDQUOTE

- **N101** `TBWTT-7:76` · 6 · consecutive days · meetings (Raël's afterword) · voice: Raël · class C

  QUOTE[TBWTT-7:76]: six jours de suite ENDQUOTE

- **N102** `ETTMTTP-1:3` · ~2 · years · since the first encounter (writing late 1975) · voice: Raël · class B

  QUOTE[ETTMTTP-1:3]: Bientôt deux ans ENDQUOTE

- **N103** `ETTMTTP-1:3` · 700 · members · movement membership, late 1975 · voice: Raël · class B

  QUOTE[ETTMTTP-1:3]: ils sont sept cents à l'heure où je mets ces lignes au propre ENDQUOTE

- **N104** `ETTMTTP-1:3` · 4 x 10^9 · persons · Earth population · voice: Raël · class B

  QUOTE[ETTMTTP-1:3]: quatre milliards d'hommes ENDQUOTE

- **N105** `ETTMTTP-1:3` · 2,000 · years ago · Jesus · voice: Raël · class K

  QUOTE[ETTMTTP-1:3]: il y a deux mille ans ENDQUOTE

- **N106** `ETTMTTP-1:5` · ~40 · lectures · in two years · voice: Raël · class B

  QUOTE[ETTMTTP-1:5]: à peu près quarante conférences ENDQUOTE

- **N107** `ETTMTTP-1:7` · 1946-09-30 ~02:00 · date · Raël's birth · voice: Raël · class B

  QUOTE[ETTMTTP-1:7]: le 30 septembre 1946 vers les deux heures du matin ENDQUOTE

- **N108** `ETTMTTP-1:7` · 1945-12-25 · date · Raël's conception · voice: Raël · class B

  QUOTE[ETTMTTP-1:7]: j'ai été conçu le 25 décembre 1945 ENDQUOTE

- **N109** `ETTMTTP-1:10` · 1947 · year · grandmother's sighting over Ambert · voice: Raël · class B

  QUOTE[ETTMTTP-1:10]: en 1947 ENDQUOTE

- **N110** `ETTMTTP-1:13` · 7 · years (age) · "counting to nine" episode · voice: Raël · class B

  QUOTE[ETTMTTP-1:13]: J'avais sept ans ENDQUOTE

- **N111** `ETTMTTP-1:15` · 9 · years (age) · age of several turning points; nine flagged as a recurring "code" number · voice: Raël · class B

  QUOTE[ETTMTTP-1:15]: à neuf ans (encore le neuf) ENDQUOTE

- **N112** `ETTMTTP-1:31` · 14 · years (age) · boarding school at Le Mont-Dore · voice: Raël · class B

  QUOTE[ETTMTTP-1:31]: A quatorze ans ENDQUOTE

- **N113** `ETTMTTP-1:33` · 15 · years (age) · leaves for Paris · voice: Raël · class B

  QUOTE[ETTMTTP-1:33]: j'avais quinze ans ENDQUOTE

- **N114** `ETTMTTP-1:37` · 3 · years · street-singing years · voice: Raël · class B

  QUOTE[ETTMTTP-1:37]: durant trois ans ENDQUOTE

- **N115** `ETTMTTP-1:39` · 18 · years (age) · driving licence · voice: Raël · class B

  QUOTE[ETTMTTP-1:39]: à dix-huit ans précis ENDQUOTE

- **N116** `ETTMTTP-1:53` · 22 · years (age) · still no race entered · voice: Raël · class B

  QUOTE[ETTMTTP-1:53]: à vingt-deux ans ENDQUOTE

- **N117** `ETTMTTP-1:61` · 3 · years · running the magazine before Dec 1973 · voice: Raël · class B

  QUOTE[ETTMTTP-1:61]: trois merveilleuses années ENDQUOTE

- **N118** `ETTMTTP-1:63` · 6 · consecutive days · meetings of December 1973 · voice: Raël · class C

  QUOTE[ETTMTTP-1:63]: six jours de suite ENDQUOTE

- **N119** `ETTMTTP-1:63` · ~1 · hour · length of each dictation session · voice: Raël · class C

  QUOTE[ETTMTTP-1:63]: pendant une heure environ ENDQUOTE

- **N120** `ETTMTTP-1:70` · autumn 1974 · date · first book printed · voice: Raël · class B

  QUOTE[ETTMTTP-1:70]: à l'automne 1974 ENDQUOTE

- **N121** `ETTMTTP-1:74` · >3,000 · persons · turnout at first Paris lecture · voice: Raël · class B

  QUOTE[ETTMTTP-1:74]: plus de trois mille personnes ENDQUOTE

- **N122** `ETTMTTP-1:75` · >2,000 · persons · second lecture · voice: Raël · class B

  QUOTE[ETTMTTP-1:75]: plus de deux mille personnes ENDQUOTE

- **N123** `ETTMTTP-2:1` · June 1975 · date · Raël resigns MADECH presidency · voice: Raël · class B

  QUOTE[ETTMTTP-2:1]: au mois de juin 1975 ENDQUOTE

- **N124** `ETTMTTP-2:5` · [1975]-07-31 · date · sighting in Périgord · voice: Raël · class C

  QUOTE[ETTMTTP-2:5]: le 31 juillet ENDQUOTE

- **N125** `ETTMTTP-2:5` · ~500 · m · distance of the craft · voice: Raël · class C

  QUOTE[ETTMTTP-2:5]: à environ cinq cents mètres de nous ENDQUOTE

- **N126** `ETTMTTP-2:6` · ~3 · cm · red mark on Raël's arm · voice: Raël · class C

  QUOTE[ETTMTTP-2:6]: d'environ trois centimètres de diamètre ENDQUOTE

- **N127** `ETTMTTP-2:7` · [1975]-08-06 · date · MADECH gathering at Puy-de-Lassolas · voice: Raël · class B

  QUOTE[ETTMTTP-2:7]: La réunion du 6 août ENDQUOTE

- **N128** `ETTMTTP-2:9` · [1975]-10-07 ~23:00 · date · leaves house; arrives Roc Plat "vers minuit" · voice: Raël · class C

  QUOTE[ETTMTTP-2:9]: Le 7 octobre, vers 23 heures ENDQUOTE

- **N129** `ETTMTTP-2:10` · 6 · times · sightings of the craft, Dec 1973 · voice: Raël · class C

  QUOTE[ETTMTTP-2:10]: à six reprises au mois de décembre 1973 ENDQUOTE

- **N130** `ETTMTTP-2:11` · 2 · years · probation period 1973-75 · voice: Yahweh · class C

  QUOTE[ETTMTTP-2:11]: Ces deux années ENDQUOTE

- **N131** `ETTMTTP-2:14` · ~15; ~10 · m · docking room in the relay base · voice: Raël · class C

  QUOTE[ETTMTTP-2:14]: d'une quinzaine de mètres de diamètre et d'une dizaine de mètres de haut ENDQUOTE

- **N132** `ETTMTTP-2:16` · ~100 · m · domed hall · voice: Raël · class C

  QUOTE[ETTMTTP-2:16]: une centaine de mètres de diamètre ENDQUOTE

- **N133** `ETTMTTP-2:28` · ~30 · years · time since advanced nations ceased to be wholly primitive (=> c. 1945) · voice: Yahweh · class K

  QUOTE[ETTMTTP-2:28]: cela fait à peine trente ans ENDQUOTE

- **N134** `ETTMTTP-2:43` · 7c; 25,000 · speed; years ago · the 7c figure back-dated to the landing on Earth 25,000 years ago · voice: Yahweh · class K

  QUOTE[ETTMTTP-2:43]: sept fois plus vite que la lumière, ceci était vrai il y a vingt-cinq mille ans lorsque nous avons débarqué sur la terre ENDQUOTE

- **N135** `ETTMTTP-2:43` · moments vs ~2 months · time · present vs former journey time · voice: Yahweh · class K

  QUOTE[ETTMTTP-2:43]: quelques instants pour effectuer le trajet que nous mettions près de deux mois à parcourir ENDQUOTE

- **N136** `ETTMTTP-2:44` · ~12 · m · larger craft (4 seats) · voice: Raël · class C

  QUOTE[ETTMTTP-2:44]: une douzaine de mètres de diamètre extérieur ENDQUOTE

- **N137** `ETTMTTP-2:44` · ~10 · minutes · duration of the cold sensation on the second leg · voice: Raël · class C

  QUOTE[ETTMTTP-2:44]: une dizaine de minutes environ ENDQUOTE

- **N138** `ETTMTTP-2:47` · ~40 · persons · guests at the meal (prophets) · voice: Raël · class C

  QUOTE[ETTMTTP-2:47]: une quarantaine de convives ENDQUOTE

- **N139** `ETTMTTP-2:48` · 6 (+ Yahweh = 7) · persons · Elohim at table · voice: Raël · class C

  QUOTE[ETTMTTP-2:48]: des six autres Elohim ENDQUOTE

- **N140** `ETTMTTP-2:50` · 8,400 · persons · re-created Earth people on the planet of the eternals · voice: Yahweh · class K

  QUOTE[ETTMTTP-2:50]: huit mille quatre cents Terriens ENDQUOTE

- **N141** `ETTMTTP-2:50` · 700 · persons · council of eternals · voice: Yahweh · class K

  QUOTE[ETTMTTP-2:50]: les sept cents Elohim membres du conseil des éternels ENDQUOTE

- **N142** `ETTMTTP-2:53` · ~700 · years · lifespan "similar to ours" (robots and Elohim) after the operation · voice: Yahweh · class K

  QUOTE[ETTMTTP-2:53]: de sept-cents ans environ ENDQUOTE

- **N143** `ETTMTTP-2:54` · >9,000 · persons · inhabitants of the planet of eternals · voice: Yahweh · class K

  QUOTE[ETTMTTP-2:54]: un peu plus de neuf mille Terriens et Elohim ENDQUOTE

- **N144** `ETTMTTP-2:54` · ~90,000 · biological robots · about ten per inhabitant · voice: Yahweh · class K

  QUOTE[ETTMTTP-2:54]: environ quatre-vingt-dix mille ENDQUOTE

- **N145** `ETTMTTP-2:62` · 2,000 · years ago · Jesus's mission · voice: Yahweh · class K

  QUOTE[ETTMTTP-2:62]: il y a deux mille ans ENDQUOTE

- **N146** `ETTMTTP-2:67` · ~20 · m · belt-flight altitude · voice: Raël · class C

  QUOTE[ETTMTTP-2:67]: à environ vingt mètres au-dessus de l'herbe ENDQUOTE

- **N147** `ETTMTTP-2:67` · ~100 · km/h · belt-flight speed · voice: Raël · class C

  QUOTE[ETTMTTP-2:67]: peut-être une centaine de kilomètres à l'heure ENDQUOTE

- **N148** `ETTMTTP-2:102` · Sunday ~11:00 · time · telepathic contact gathering · voice: Yahweh · class P

  QUOTE[ETTMTTP-2:102]: le dimanche matin vers onze heures ENDQUOTE

- **N149** `ETTMTTP-2:131` · 00:00 · time · return to Roc Plat (=> absence of about 24 h) · voice: Raël · class C

  QUOTE[ETTMTTP-2:131]: il était minuit ENDQUOTE

- **N150** `ETTMTTP-3:16` · 7 (and 14) · years (age) · limits on corporal punishment · voice: Yahweh · class P

  QUOTE[ETTMTTP-3:16]: A partir de sept ans ENDQUOTE

- **N151** `ETTMTTP-3:69` · 33 · mm · location of the frontal bone to be preserved · voice: Yahweh · class P

  QUOTE[ETTMTTP-3:69]: à 33 mm au-dessus du milieu de l'axe reliant tes deux pupilles ENDQUOTE

- **N152** `ETTMTTP-3:69` · >=1 · cm^2 · bone sample · voice: Yahweh · class P

  QUOTE[ETTMTTP-3:69]: au moins un centimètre carré de cet os ENDQUOTE

- **N153** `ETTMTTP-3:84` · +50% (and +10%) · IQ above mean · geniocracy thresholds restated · voice: Yahweh · class P

  QUOTE[ETTMTTP-3:84]: supérieur de 50 % à la moyenne ENDQUOTE

- **N154** `ETTMTTP-3:101` · ~50,000 · inhabitants · recommended town size on Earth · voice: Yahweh · class P

  QUOTE[ETTMTTP-3:101]: environ cinquante mille habitants ENDQUOTE

- **N155** `ETTMTTP-3:172` · 1946 = year 1 · era · dating rule · voice: Yahweh · class P

  QUOTE[ETTMTTP-3:172]: en comptant l'an 1946 comme l'an un après Raël ENDQUOTE

- **N156** `ETTMTTP-3:172` · 1976 = year 31 · era · worked example (inclusive count) · voice: Yahweh · class P

  QUOTE[ETTMTTP-3:172]: 1976 sera donc l'an 31 après Raël ENDQUOTE

- **N157** `ETTMTTP-3:245` · 50,000 -> 500 (in 50 yrs) · seminarians · decline of vocations; "49,500 unhappy beings" · voice: Yahweh · class K

  QUOTE[ETTMTTP-3:245]: Il y a cinquante ans, il y avait cinquante mille séminaristes, maintenant il n'y en a plus que cinq cents ENDQUOTE

- **N158** `ETTMTTP-3:266` · 4 dates · annual gatherings · feast calendar · voice: Yahweh · class P

  QUOTE[ETTMTTP-3:266]: le premier dimanche d'avril, le 6 août, le 7 octobre et le 13 décembre ENDQUOTE

- **N159** `LWTE-1:2` · year 30 = 1975 · era · second encounter dated in the new era · voice: Questioner · class C

  QUOTE[LWTE-1:2]: le 7 octobre 30 (1975) ENDQUOTE

- **N160** `LWTE-1:2` · ~24 · hours · length of stay · voice: Questioner · class C

  QUOTE[LWTE-1:2]: près de vingt-quatre heures sur la planète des éternels ENDQUOTE

- **N161** `LWTE-1:13` · 25,000 · years ago · creation of life on Earth (questioner's summary of the messages) · voice: Questioner · class K

  QUOTE[LWTE-1:13]: il y a vingtcinq mille ans ENDQUOTE

- **N162** `LWTE-1:13` · hundreds of thousands · years · age of animal remains (objection) · voice: Questioner · class H

  QUOTE[LWTE-1:13]: plusieurs centaines de milliers d'années ENDQUOTE

- **N163** `LWTE-1:15` · 10,000-20,000 · years before arrival · hypothetical earlier, destroyed creation · voice: Raël · class K

  QUOTE[LWTE-1:15]: dix ou vingt mille ans avant leur venue ENDQUOTE

- **N164** `LWTE-1:15` · infinite · creations · prior creations and destructions on Earth · voice: Raël · class K

  QUOTE[LWTE-1:15]: Il y a eu une infinité de créations sur notre planète ENDQUOTE

- **N165** `LWTE-1:26` · ~4 · light-years · nearest star per terrestrial science (objection) · voice: Questioner · class H

  QUOTE[LWTE-1:26]: environ quatre années-lumière ENDQUOTE

- **N166** `LWTE-1:27` · 4 vs 1 · light-years · members' hypothesis: curved light path vs straight line · voice: Raël · class K

  QUOTE[LWTE-1:27]: quatre années-lumière en suivant la lumière ENDQUOTE

- **N167** `LWTE-1:30` · 25,000 · years ago · creation of the original continent (questioner) · voice: Questioner · class K

  QUOTE[LWTE-1:30]: les Elohim ont créé, il y a vingt-cinq mille ans, le continent originel ENDQUOTE

- **N168** `LWTE-1:30` · 25 km at 1 m/yr · km · objection: drift at today's rate · voice: Questioner · class H

  QUOTE[LWTE-1:30]: en ving-cinq mille ans l'on obtiendrait vingt-cinq mille mètres, soit ving-cinq kilomètres ENDQUOTE

- **N169** `LWTE-1:31` · hundreds · km/yr · initial continental separation rate · voice: Raël · class K

  QUOTE[LWTE-1:31]: ils s'éloignaient de plusieurs centaines de kilomètres chaque année ENDQUOTE

- **N170** `LWTE-1:31` · 25 · millennia · time since the "storm" of the continent's creation · voice: Raël · class K

  QUOTE[LWTE-1:31]: en vingtcinq millénaires ENDQUOTE

- **N171** `LWTE-1:36` · 3rd millennium · era · forecast for Raëlism · voice: Raël · class K

  QUOTE[LWTE-1:36]: la religion dominante dans le monde du troisième millénaire ENDQUOTE

- **N172** `LWTE-1:46` · 700 · years · dated age of the Ararat wood · voice: Raël · class H

  QUOTE[LWTE-1:46]: ils n'étaient vieux que de sept cents ans ENDQUOTE

- **N173** `LWTE-1:47` · ~5,000 · years ago · date of the real Flood · voice: Raël · class K

  QUOTE[LWTE-1:47]: datant d'environ cinq mille ans, ce qui correspondrait à la période du «déluge » réel ENDQUOTE

- **N174** `LWTE-1:56` · 25,000 · years · Elohim lead (question) · voice: Questioner · class K

  QUOTE[LWTE-1:56]: les Elohim ont vingt-cinq mille ans d'avance sur nous ENDQUOTE

- **N175** `LWTE-1:72` · 1/100 · probability · that humanity chooses wisdom · voice: Raël · class K

  QUOTE[LWTE-1:72]: qu'une chance sur cent ENDQUOTE

- **N176** `LWTE-1:73` · 25,000 · years · Elohim lead · voice: Raël · class K

  QUOTE[LWTE-1:73]: vingt-cinq mille ans d'avance sur nous ENDQUOTE

- **N177** `LWTE-1:176` · 10% · share · brain capacity ordinary people use · voice: Raël · class K

  QUOTE[LWTE-1:176]: dix pour cent des possibilités de son cerveau ENDQUOTE

- **N178** `LWTE-2:1` · 3 · years · embargo on the ch. 2 revelations after the 1975 voyage · voice: Editor · class C

  QUOTE[LWTE-2:1]: trois années ENDQUOTE

- **N179** `LWTE-2:2` · year 34 = 1979 · era · date of writing · voice: Editor · class C

  QUOTE[LWTE-2:2]: nous sommes en l'an 34 (1979) ENDQUOTE

- **N180** `LWTE-2:11` · 2 (after the first) · failures · failed planets before Earth · voice: Raël · class K

  QUOTE[LWTE-2:11]: après deux nouveaux échecs ENDQUOTE

- **N181** `LWTE-2:17` · 2 · planets · other created worlds · voice: Raël · class K

  QUOTE[LWTE-2:17]: sur deux autres planètes à cette époque ENDQUOTE

- **N182** `LWTE-2:63` · 10^9 - 10^10 · [currency unstated] · sum offered by Satan in the test · voice: Satan (reported) · class C

  QUOTE[LWTE-2:63]: un milliard, cinq milliards, dix milliards ENDQUOTE

- **N183** `LWTE-2:68` · 9/10 · probability · of self-destruction (Raël's reply to Satan) · voice: Raël · class C

  QUOTE[LWTE-2:68]: neuf chances sur dix ENDQUOTE

- **N184** `LWTE-2:68` · 1/1000 · probability · hypothetical chance of escaping destruction · voice: Raël · class H

  QUOTE[LWTE-2:68]: une chance sur mille ENDQUOTE

- **N185** `LWTE-2:77` · <=12 · men · men like Raël on Earth (Satan's estimate) · voice: Satan (reported) · class C

  QUOTE[LWTE-2:77]: plus d'une douzaine d'hommes comme moi ENDQUOTE

- **N186** `LWTE-2:79` · 1945-08-06 · date · the explosion after which a messenger was chosen · voice: Raël · class K

  QUOTE[LWTE-2:79]: l'explosion atomique qui eut lieu le 6 août 1945 à Hiroshima ENDQUOTE

- **N187** `LWTE-2:90` · 3 · years · embargo on the paternity revelation · voice: Raël · class C

  QUOTE[LWTE-2:90]: avant que trois années soient écoulées ENDQUOTE

- **N188** `LWTE-2:96` · 1/100 · probability · of humanity not destroying itself · voice: Yahweh · class K

  QUOTE[LWTE-2:96]: qu'une chance sur cent pour que votre humanité ne s'auto-détruise pas ENDQUOTE

- **N189** `LWTE-2:118` · 7 · craft · Rev 1 "seven lamps" · voice: Yahweh · class Q

  QUOTE[LWTE-2:118]: Il voit sept engins volants ENDQUOTE

- **N190** `LWTE-2:128` · 24 · eternals · "representing the council" before John (Rev 4) · voice: Yahweh · class K

  QUOTE[LWTE-2:128]: j'étais entouré de vingt-quatre autres éternels ENDQUOTE

- **N191** `LWTE-2:132` · 7 · chapters · seals = chapters of human history · voice: Yahweh · class K

  QUOTE[LWTE-2:132]: des sept sceaux, ou encore des sept chapitres de l'histoire de l'humanité ENDQUOTE

- **N192** `LWTE-2:147` · a few thousand · persons · Earth people already re-created · voice: Yahweh · class K

  QUOTE[LWTE-2:147]: aux quelques milliers de terriens que nous avons recréés ENDQUOTE

- **N193** `LWTE-2:158` · ~144,000 · persons · total "sealed on the forehead", incl. those already re-created · voice: Yahweh · class K

  QUOTE[LWTE-2:158]: sera d'à peu près cent quarante-quatre mille ENDQUOTE

- **N194** `LWTE-2:163` · 1/3 · share · Rev 8 trumpets as nuclear effects · voice: Yahweh · class Q

  QUOTE[LWTE-2:163]: Le tiers de la terre est brûlé par la radioactivité ENDQUOTE

- **N195** `LWTE-2:193` · 4 · loudspeakers · Rev 9:13 "four horns" · voice: Yahweh · class K

  QUOTE[LWTE-2:193]: les quatre haut-parleurs ENDQUOTE

- **N196** `LWTE-2:208` · 666 · generations · since the creation of the first humans in the laboratories · voice: Yahweh · class K

  QUOTE[LWTE-2:208]: Six cent soixante-six, c'est le nombre de générations humaines ENDQUOTE

- **N197** `LWTE-2:208` · ~13,000 · years ago · creation of the first humans · voice: Yahweh · class K

  QUOTE[LWTE-2:208]: Les premiers hommes ayant été créés il y a environ treize mille ans ENDQUOTE

- **N198** `LWTE-2:208` · 20 · years · assumed generation length · voice: Yahweh · class K

  QUOTE[LWTE-2:208]: la durée d'une génération humaine estimée à vingt ans ENDQUOTE

- **N199** `LWTE-2:208` · 13,320 · years · 666 x 20, computed in the text · voice: Yahweh · class K

  QUOTE[LWTE-2:208]: un total de treize mille trois cent vingt ans ENDQUOTE

- **N200** `LWTE-2:208` · 1945 · year · start of the age of Apocalypse; birth of the 666th generation · voice: Yahweh · class K

  QUOTE[LWTE-2:208]: au commencement de l'âge de l'Apocalypse en 1945 de l'ère chrétienne ENDQUOTE

- **N201** `LWTE-2:209` · 1945-08-06 · date · first murderous use of nuclear energy · voice: Yahweh · class K

  QUOTE[LWTE-2:209]: le 6 août de cette année 1945 à Hiroshima ENDQUOTE

- **N202** `LWTE-2:231` · 99% · probability · of the final cataclysm · voice: Yahweh · class K

  QUOTE[LWTE-2:231]: quatre-vingt-dix-neuf pour cent de chance ENDQUOTE

- **N203** `LWTE-3:26` · 6 August · date · annual feast of the era's opening · voice: Raël · class P

  QUOTE[LWTE-3:26]: le rassemblement annuel du 6 août pour fêter l'entrée dans l'âge de l'Apocalypse ENDQUOTE

- **N204** `LWTE-3:45` · 60% (US); >70% (Europe); 85% (Germany) · share · Milgram obedience figures as reported by Raël · voice: Raël · class H

  QUOTE[LWTE-3:45]: soixante pour cent des sujets ENDQUOTE

- **N205** `LWTE-3:76` · 3,000 · members · movement size, 1979 · voice: Raël · class B

  QUOTE[LWTE-3:76]: je suis trois mille ENDQUOTE

- **N206** `LWTE-3:79` · 1945 · year · entry into the age of Apocalypse · voice: Raël · class K

  QUOTE[LWTE-3:79]: Depuis 1945 ENDQUOTE

- **N207** `LWTE-4:32` · 2,000 · m · thickness of coal accumulations · voice: Terrusse · class W

  QUOTE[LWTE-4:32]: deux mille mètres dans le Nord de la France ENDQUOTE

- **N208** `LWTE-4:40` · a few · cm/yr · present drift rate (residual of the Flood breakup) · voice: Terrusse · class W

  QUOTE[LWTE-4:40]: quelques centimètres par an ENDQUOTE

- **N209** `LWTE-4:42` · thousands · years · interval continent-creation to Flood · voice: Terrusse · class W

  QUOTE[LWTE-4:42]: Pendant les milliers d'années qui séparèrent la création du continent originel par les Elohim de la période du déluge ENDQUOTE

- **N210** `LWTE-4:73` · 1920s · date · Hertz's discovery of radio waves, as stated · voice: Terrusse · class W

  QUOTE[LWTE-4:73]: dans les années 1920 ENDQUOTE

- **N211** `LWTE-4:73` · 25,000 · years · Elohim lead · voice: Terrusse · class W

  QUOTE[LWTE-4:73]: les Elohim nous devancent de vingt cinq mille ans ENDQUOTE

- **N212** `LWTE-4:90` · ~40 · prophets · prophets who will return · voice: Le Gendre · class W

  QUOTE[LWTE-4:90]: près d'une quarantaine ENDQUOTE

- **N213** `LWTE-4:219` · year 33 = May 1979 · era · dateline of a guide's testimony · voice: Deydier · class W

  QUOTE[LWTE-4:219]: Cannes, 22 mai 1979, an 33 après Raël ENDQUOTE

