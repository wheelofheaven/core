---
title: "Review: continental breakup at the Flood"
claim_id: woh-claim-0071
review_id: woh-claim-0071-review-0001
status: draft
components_complete:
  - authorship-attribution
  - edition-collation
  - citation-verification
  - scientific-and-critical-appraisal
components_outstanding: []
recommended_status: reviewed
signed_by: null
signed_date: null
supersedes: null
---

# Review: continental breakup at the Flood

Second review drafted against the format adopted in
[RFC 0007](../../rfcs/0007-reproducible-review-records.md) /
[ADR 0009](../../decisions/0009-reproducible-review-records.md). It is
**unsigned**. Claim
[`woh-claim-0071`](../framework/continental-breakup-at-the-flood.md) has not
moved and remains `scoped` and `contested`; the reviewer's recommendation
is recorded in the frontmatter and takes effect only on sign-off.

The review was directed first at the two questions the record left open
when it was accepted ([ADR 0010](../../decisions/0010-continental-breakup-promotion.md)):
whose text the "New Hypothesis" passage is, and whether the petroleum-ring
study it cites exists and says what the passage says it says. Both were
settled on 2026-09-15 at the level of the witnesses held. The fourth
component named by the [evidence map](../evidence/woh-claim-0071-evidence.md)
— reading the scientific and critical rows against their sources — was
performed the same day against the sources reachable without acquisition,
and its limits are recorded.

## Question

The proposition reviewed, quoted from the claim record:

> Per the canon, the single continent the Elohim raised from the seabed was
> broken by the home-planet strike the canon identifies as the Flood: the
> blasts sent its fragments 'drifting outwards from the centre of the
> shock', swept the whole land surface, and buried the living matter —
> forests, animals, humans — 'immediately and all together' in a ring around
> the impact; the corpus reads today's continental configuration and its
> ongoing drift as the residue of that displacement, and the fossil-bearing
> strata as the burial sequence of what died when in the aftermath of the
> initial explosion, while accepting the planet's own deep age and
> registering, in its own voice, that mainstream plate tectonics and
> radiometric dating place the Pangaean breakup roughly 195 million years
> ago.

Components 1–3 concern the *canonical basis* of that proposition — where
the breakup-and-burial account comes from and what its one external
citation is. Component 4 concerns the *corpus reading* — whether the
mainstream and critical accounts the record names as alternatives say
what the record says they say, and what discriminates between them and
the claim.

## Protocol

**Witnesses, components 1–3.**

| Witness | Identity | Access |
| --- | --- | --- |
| **D** — project digitization | `data-library/lets-welcome-the-extraterrestrials/chapter-4.json` (312 paragraphs; `text` = French base, `i18n.en` = English) | Held |
| **E** — English printed edition | *Intelligent Design: Message from the Designers*, 2005 combined volume, 407 PDF pages; book three *Let's Welcome the Extra-Terrestrials*, ch. 4 at printed pp. 327 ff. | Held, `data-sources/pdf/_combined/intelligent-design-en.pdf` |
| **F** — French printed edition | *Le Message donné par les Extra-terrestres*, 2005 combined volume, 222 PDF pages | Held, `data-sources/pdf/_combined/` |
| **R** — the cited study | Richard Nehring, *Giant Oil Fields and World Oil Resources*, R-2284-CIA, The Rand Corporation, June 1978, 188 PDF pages, scanned images without a text layer | Public; downloaded 2026-09-15 from `rand.org/content/dam/rand/pubs/reports/2006/R2284.pdf` (7,130,277 bytes); not yet held in `data-sources` |
| **W** — web attribution | `crea-science.blogspot.com/2006/01/la-drive-des-continents.html` (2006 repost of the French passage with attribution) | Public, secondary |

**Witnesses, component 4** (all accessed 2026-09-15; registry IDs in
`data/sources.json`).

| Witness | Identity | Access level used |
| --- | --- | --- |
| **L** | Lyell, *Principles of Geology*, vol. 1 (1830), Google-scanned text via `archive.org/download/principlesgeolo01lyelgoog/…_djvu.txt` (2,997,869 bytes) | Full text, OCR quality poor |
| **U** | Kious and Tilling, *This Dynamic Earth* (USGS, 1996; online edition), pages `historical.html`, `understanding.html`, `developing.html` | Full text |
| **DH** | Dietz and Holden, "Reconstruction of Pangaea: Breakup and Dispersion of Continents, Permian to Present", *J. Geophys. Res.* 75 (1970) 4939–4956 | Abstract (OpenAlex) |
| **DG** | DeMets, Gordon and Argus, "Geologically current plate motions", *Geophys. J. Int.* 181 (2010) 1–80 | Abstract (OpenAlex) |
| **KU** | Klemme and Ulmishek, "Effective Petroleum Source Rocks of the World", *AAPG Bulletin* 75 (1991) 1809–1851 | Abstract (OpenAlex) |
| **MG** | Mann, Gahagan and Gordon, "Tectonic Setting of the World's Giant Oil and Gas Fields", AAPG Memoir 78 (2003) 15–105 | Abstract (OpenAlex) |
| **FS** | Firestone et al., "Evidence for an extraterrestrial impact 12,900 years ago…", *PNAS* 104 (2007) 16016–16021 | Abstract (NCBI E-utilities, PMID 17901202) |
| **MO** | Montgomery, *The Rocks Don't Lie* (2012) | Publisher description (Open Library work OL16654065W) |
| **WM** | Whitcomb and Morris, *The Genesis Flood* (1961) | Not read; characterised through MO and the registry record |

**Procedure, components 1–3.**

1. *Authorship attribution.* In D, list every paragraph of ch. 4 under 70
   characters or matching a heading pattern, in both columns, to expose
   bylines and section titles; delimit the span of the essay containing
   the passage by the preceding and following bylines. In E, extract the
   text layer with `pdftotext -layout` (poppler; no OCR needed) and read
   the pages carrying the chapter opening, the passage, and the next
   signed piece. In F, search the text layer for the essay's author,
   section title, and cited names.
2. *Edition collation.* For every D paragraph of 40 characters or more in
   `n=1..80`, normalise (NFC; typographic quotes and dashes folded;
   non-word characters removed; lowercased) and seek the opening 60
   normalised characters in the correspondingly normalised text of E PDF
   pp. 349–356. Count the two columns' paragraphs over the same range.
3. *Citation verification.* Identify the study named in D `n=26–27, 30, 38`
   (French) and E p. 330 (English) by web search on the surname, the CIA,
   and the subject; obtain the report; OCR it (`pdftoppm -r 150 -gray`,
   then `tesseract --psm 6 -l eng` per page, output joined with form feeds);
   search the OCR text for `Pangea`, `ring of`, `circle`, `reassembl`,
   `continental drift`, `Tethys`, `Hudson`, `prepared for`; read the pages
   that hit in full.

**Procedure, component 4.**

4. For each scientific and critical row of the evidence map, obtain the
   source at the access level stated above (L and U by `curl`; DH, DG, KU,
   MG by the OpenAlex works API, reconstructing the abstract from its
   inverted index; FS by NCBI `efetch` in XML; MO by the Open Library
   works API). Search L for `universal deluge`, `Mosaic`, `catastroph`;
   search U for `200 million`, `Pangaea`, `GPS`, `centimeters per year`,
   `magnetic strip`. Extract, for each source, (a) what it states about
   the timing and manner of the Pangaean breakup, (b) what it states about
   present-day plate rates against geologically averaged rates, (c) what it
   states about the stratigraphic and tectonic distribution of petroleum,
   and (d) whether it says anything about a single recent breakup. Then
   test each of the record's four alternatives against the extractions.

The scripts are short standard-library filters over the JSON, the text
layers, the OCR text and the API responses; they are reproducible from
this description. Fetched material lives in the session scratch and is not
committed.

**What would have counted against the claim's basis (1–3).** The passage
appearing in Raël's message text rather than in a signed contribution;
no byline or a byline naming Raël; the cited study not existing, or
existing without any ring-shaped or plate-reconstruction content; a printed
edition wording that removes the breakup, the burial ring, or the drift.

**What would have counted for the claim's reading (4).** Any source
reporting present-day plate velocities materially higher than, or
decaying relative to, the rates recorded by seafloor magnetic anomalies;
any source dating the separation of all the Pangaean fragments to a
single event; any source treating the world's petroleum as the product of
one burial; any mainstream catastrophist source proposing a Holocene
continental-scale breakup.

**Locators.** D uses `LWTE-4:<n>`. Because the two columns of D are not
aligned (see Extraction, finding 4), every D locator below states its
column. E is cited by printed page number (PDF page = printed page + 22
in this range; confirmed by the running page numbers on pp. 327–339). R is
cited by its printed page number (PDF page = printed page + 26 in the body;
front matter unnumbered). Abstract-level witnesses are cited by
publication and, where a passage is quoted, as "abstract".

## Screening

**Examined.** D ch. 4 in full (both columns); E PDF pp. 347–361 by hand
and pp. 349–356 by collation; F searched in full; R front matter (PDF
pp. 1–4), list of figures (p. xvii), pp. 39–41 and the bibliography entry
on p. 93 (PDF 119); W in full; L by search of the whole scanned volume;
U's three pages in full; DH, DG, KU, MG, FS at abstract level; MO's
publisher description.

**Excluded, with reason.** The 1979 first editions (French *Accueillir les
Extra-terrestres*, English *Let's Welcome the Extra-Terrestrials*) — no copy
held; D's French column is the only witness to the 1979 text and its
digitization provenance is not recorded in `_meta.json`. F beyond a text
search — it does not contain the commentaries chapter (see finding 2). R
beyond the pages that hit — the review needed the ring passage, not the
resource estimates. Dietz and Holden's *Scientific American* version
(November 1970), which R adapts for its figure — not accessible; the
authors' JGR paper of the same year (DH) was read instead. The full texts
of DG, KU, MG and FS — paywalled or not held; the abstracts carry the
figures the appraisal uses. WM — not held; its thesis is taken from MO and
the registry description, and no finding below depends on its wording.
Terrusse's later writings and the movement's later restatements of the
theory — outside the question; W was used only to confirm that the
movement itself attributes the passage to Terrusse.

## Extraction

**1. Byline (authorship settled).** D, French column, `LWTE-4:1`:
*"Le Raëlisme sous l'œil de la science par Marcel TERRUSSE,"* — the
chapter's first paragraph, before the essay's first section. E p. 327:

> 4 COMMENTARIES AND TESTIMONIALS OF RAELIANS
> Raelism Through the Eyes of Science
> MARCEL TERUSSE – Chemical Engineer & Raelian Guide
> 1: EVOLUTION, OBSCURANTISM AND THE NEO-DARWINIAN MYTH

E p. 339 opens the same author's second piece: *"Yes... I am Raelian —
MARCEL TERRUSSE – Chemical Engineer and Raelian Guide"* (the byline is
spelled *Terusse* on p. 327 and *Terrusse* on p. 339; D and W read
*Terrusse*). W: *"Voici ci-dessous l'hypothèse de Marcel Terrusse
(scientifique Raëlien / Ingénieur chimiste) sur cette question. Tirée du
livre 'Accueillir les Extra-terrestres'."*

**2. Span of the essay.** The essay runs in three numbered sections:
§1 (E pp. 327–330), §2 *A New Hypothesis for the History of Humanity*
(E pp. 330–332; D English column `n=25`), §3 *Transmission of the Cellular
Plan in the Light of Science* (E p. 332 ff.; D English `n=53`). E's running
head on p. 331 reads *"Commentaries & Testimonials of Raelians – Raelism
Through the Eyes of Science"*. The next signed piece is *Impressions of a
Priest* (D English `n=77`; D French `n=80–82`: *"Impressions d'un
« prêtre » / Par Victor LE GENDRE, Guide régional pour l'Est du Québec,
ex-prêtre catholique romain"*). The breakup passage therefore lies inside
Terrusse's essay, not in any text spoken by Raël or attributed to the
Elohim. F does not contain the chapter at all: the strings *Terrusse*,
*Nehring*, *Hudson* and the section title are absent from its 222 pages;
F p. 209 names *Accueillir les Extra-terrestres (1979)* as the third book
without reproducing the commentaries.

**3. The passage in its two languages.** E p. 331 (identical to D English
`n=35`):

> When the Elohim decided to destroy their bases, their laboratories and
> all that they had created on Earth, they must have used extremely
> powerful methods of destruction, which, as well as breaking up this
> original continent and sending each respective fragment drifting outwards
> from the centre of the shock, must also have swept the whole land surface.
> Since the impact must have spread outwards from the bombs' point of
> impact, all the living matter including immense forests, animals and even
> Man would have been buried deep, immediately and all together under tons
> of earth in a ring shape, circling the central explosion.

D French column `n=34–41` carries the fuller 1979 text. `n=34`: *"Les
Elohim, lorsqu'ils décidèrent de détruire les laboratoires et les bases
qu'ils avaient construites sur la terre ainsi que l'ensemble de leur
création, durent utiliser des moyens de destruction d'une puissance telle
que même nos bombes actuelles ne sont que des pétards d'enfants à côté."*
`n=36`: *"La surface du sol fut balayée par les ondes de choc des
explosions, les forêts et les animaux, la terre superficielle elle-même fut
décapée, ensevelissant sous des tonnes de terre d'innombrables formes de vie
animales et même des hommes..."* `n=38`: *"Et cet immense anneau qui
intrigue tant Nehring aujourd'hui est le bourrelet de matière rejeté vers
l'extérieur par le plus formidable bombardement qu'ait eu à subir
l'humanité..."* `n=39`: *"Le continent originel lui-même ne résista pas au
coup de boutoir et se fragmenta sous l'effet des ondes de choc..."*
`n=40–41`: *"Lors de l'événement, les plaques continentales se séparèrent
brutalement et, dérapant sur leur soubassement de magma visqueux, partirent
dans différentes directions ; d'abord très rapide, leur glissement se
ralentit au fil des années, pour n'être plus aujourd'hui que de quelques
centimètres par an... La vitesse d'écartement des continents que nous
mesurons aujourd'hui est une « vitesse résiduelle », qui tend à décroître
dans le temps."*

The residual-velocity sentences (`n=40–41`) have no counterpart in E,
whose rendering of §2 is shorter and re-paragraphed. The corpus's "residual
momentum" reading of present-day plate motion rests on the French text
alone.

**4. The two columns of D are not aligned.** Over `n=1..80`, D carries 80
French paragraphs and 45 English ones. Collation of the 45 English
paragraphs of 40+ characters against E pp. 349–356 found 42 verbatim (the
three misses are the priest piece, which begins after p. 356). D's English
column is therefore the 2005 printed English; D's French column is the
1979 French; the two share paragraph numbers by position only. `LWTE-4:35`
denotes the breakup paragraph in English and a different sentence
(*"Le continent originel sur lequel ils avaient construit leurs bases … ne
résista pas à ce cataclysme"*) in French. Every locator the claim record,
its specification, and the derivative pages gave for this chapter before
this review was an English-column locator.

**5. The cited study exists, under a different institution.** D French
`n=26–27`: *"La C.I.A. … a confié au Hudson Institut le soin de réaliser
une étude sur la répartition des ressources en charbon, pétrole et gaz
naturel dans le monde. Le professeur Nehring, maître d'œuvre de l'étude,
est arrivé à une constatation qui est une énigme pour lui et pour les
géologues."* E p. 330 gives *"Professor Nebring"* and *"the Hudson
Institute"*. The study is R: title page (OCR p. 1) *"GIANT OIL FIELDS AND
WORLD OIL RESOURCES — PREPARED FOR THE CENTRAL INTELLIGENCE AGENCY —
R-2284-CIA — RICHARD NEHRING — JUNE 1978"*; verso (OCR p. 4): *"The work
upon which this publication is based was performed pursuant to Contract
No. XG-4705 with the Central Intelligence Agency. Reports of The Rand
Corporation do not necessarily reflect the opinions or policies of the
sponsors of Rand research."* It is a RAND report, not a Hudson Institute
one, and nothing in it styles Nehring a professor.

**6. The ring is in the study, on a deep-time reconstruction.** R p. 39:

> One other aspect of the concentration of world oil resources is
> noteworthy. The concentration of world oil resources in an arc from
> Algeria through the Middle East and the central Soviet Union to the Arctic
> Ocean has been emphasized by several authors. An even more striking
> concentration is that of the "ring of oil" (Fig. 3.1). This oval band,
> imposed on a map showing the postulated position of the continental
> plates 180 million years ago, is roughly 800 to 1000 miles wide and
> contains nearly 85% of the known petroleum resources of the world
> (approximately 845 of 1012 billion barrels). Within it are found 14 of
> the 22 major provinces and all of the seven largest provinces. It also
> contains 210 of the 272 known giants with 706.1 of the 776.1 billion
> barrels in these fields. Most of the major nonconventional oil deposits
> of the world are also within the ring, notably the oil (tar) sand deposits
> of the Alberta and Maturin basins and the oil shale deposits of the
> western Rocky Mountain basins. […] This continuity of production exists
> despite considerable differences in province types and in the geologic
> ages of productive formations among the producing provinces within the
> ring. No complete explanation for this phenomenon is yet available.
> However, the concentration of total resources within it is so great and
> the continuity of production is so remarkable that it poses a most
> interesting problem for geologic speculation.

R p. 40, Fig. 3.1 caption: *"The 'ring of oil' — SOURCE: Map of the
postulated position of the continental plates at the end of the Triassic
Period (180 million years ago), adapted from R. S. Dietz and J. C. Holden,
'The Breakup of Pangea,' Scientific American, Vol. 223, No. 5, November
1970, p. 35."* The report's list of figures (p. xvii) and bibliography
(p. 93) confirm both.

Terrusse's summary of the observation is faithful: the ring, the deposits
he lists (Arctic and Alaska, Alberta sands, Colorado shales, Mexico,
Venezuela, the Orinoco heavy oils, Nigeria, Sahara, Libya, Arabia, Iran,
Siberia), the CIA sponsorship, and Nehring's own puzzlement (*"une énigme
pour lui et pour les géologues"* against *"No complete explanation … is yet
available"*). The French `n=28` places the ring *"à la fin de la période
géologique du trias"*, matching R's *"end of the Triassic Period"*; E p. 330
renders this *"the end of the geological tertiary period"*, a
mistranslation in the printed English. What is Terrusse's own, and not
Nehring's, is the reading of the ring as the burial rim of a recent strike:
R draws it on a reconstruction dated 180 million years ago and leaves the
explanation open.

**7. The timing and manner of the breakup (U, DH).** U, `historical.html`:
*"According to the continental drift theory, the supercontinent Pangaea
began to break up about 225-200 million years ago, eventually fragmenting
into the continents as we know them today."* U, `understanding.html`:
*"Seafloor spreading over the past 100 to 200 million years has caused the
Atlantic Ocean to grow from a tiny inlet of water between the continents of
Europe, Africa, and the Americas into the vast ocean that exists today"*;
*"The rate of spreading along the Mid-Atlantic Ridge averages about 2.5
centimeters per year (cm/yr), or 25 km in a million years."* DH (abstract):
*"In the Triassic the breakup of Pangaea commenced. The southwest Indian
Ocean rift was created, which split West Gondwana (South America and
Africa) away from East Gondwana while a Y junction lifted India off
Antarctica. An independent North Atlantic–Caribbean rift also formed, which
lifted Laurasia (North America and Eurasia) off of South America and the
bulge of Africa. In the Jurassic, northward and westward sea-floor
sp[reading]…"* — a staged dispersal in *"a series of five world maps to
depict the breakup and dispersion of continents with each subsequent
geologic period, Triassic to Recent"*. DH is the reconstruction R's figure
is adapted from.

**8. Present-day rates against geologically averaged rates (DG, U).** DG
(abstract): MORVEL's plate motions are determined from *"seafloor
spreading rates and fault azimuths"* estimated *"over the past 0.78 Myr
for intermediate and fast spreading centres and since 3.16 Ma for slow and
ultraslow spreading centres"*; *"by design, almost no kinematic information
is exchanged between the geologically determined and geodetically
constrained subsets"*; and against decadal GPS, *"the MORVEL and GPS
estimates of Pacific-North America plate motion in western North America
differ by only 2.6 ± 1.7 mm yr⁻¹"*, with the summed differences between
GPS and MORVEL angular velocities smaller than for any earlier model. The
same abstract records the one kind of change the data do show —
*"consistent with a progressive slowdown in the eastward component of
Nazca plate motion since 3.16 Ma"* — at the scale of millimetres per year
over millions of years. U, `understanding.html`: magnetic striping lets
scientists, *"knowing the approximate duration of the reversal, … calculate
the average rate of plate movement during a given time span"*; present
motion *"can be tracked directly by means of ground-based or space-based
geodetic measurements"*.

**9. Where the world's petroleum comes from (KU, MG).** KU (abstract):
*"Six stratigraphic intervals, representing one-third of Phanerozoic time,
contain petroleum source rocks that have provided more than 90% of the
world's discovered original reserves of oil and gas"* — Silurian (9%),
Upper Devonian–Tournaisian (8%), Pennsylvanian–Lower Permian (8%), Upper
Jurassic (25%), middle Cretaceous (29%), Oligocene–Miocene (12.5%); *"this
uneven distribution of source rocks in time displays no obvious cyclicity"*;
the controlling factors are *"geologic age, paleolatitude of the
depositional areas, structural forms in which the deposition of source
rocks occurred, and the evolution of biota"*; *"almost 70% of the world's
original reserves of oil and gas has been generated since the Coniacian"*.
MG (abstract): the 877 giant fields *"cluster in 27 regions, or about 30%,
of the earth's land surface"*, and sort by tectonic setting into
*"continental passive margins fronting major ocean basins (304 giants);
continental rifts and overlying sag or 'steer's head' basins (271 giants);
collisional margins produced by terminal collision between two continents
(173 giants)"*, accretion-related collisions (71), strike-slip margins
(50), and subduction margins (8).

**10. The mainstream catastrophist row (FS).** FS (abstract): *"A
carbon-rich black layer, dating to approximately 12.9 ka, has been
previously identified at approximately 50 Clovis-age sites across North
America"*; the authors *"propose that one or more large, low-density ET
objects exploded over northern North America, partially destabilizing the
Laurentide Ice Sheet and triggering YD cooling"*. The event is dated
12,900 years ago, its evidence is North American, and nothing in the
abstract concerns continents, plates, or the breakup of a landmass.

**11. The uniformitarian and critical rows (L, MO).** L, vol. 1, the
chapter summary for Book I: the *"opposite doctrine, which refers
geological phenomena to an uninterrupted series of changes in the organic
and inorganic world, unattended with general catastrophes, or the
development of paroxysmal forces"*; and Lyell's history of the science
lists the seventeenth-century attribution of fossils *"to the Mosaic
deluge"* and *"Woodward's Diluvial theory"* among the positions his own
supersedes. MO (publisher description): Montgomery *"discovered the
counterintuitive role Noah's Flood played in the development of both
geology and creationism … Centuries later, the founders of modern
creationism based their irrational view of a global flood on a perceptive
critique of geology."* WM was not read.

## Appraisal

**For the claim's canonical basis.** The record's third alternative,
*commentary-not-message*, stated a possibility; findings 1–2 make it a
fact. The breakup-and-burial account is Marcel Terrusse's, a chemical
engineer and Raëlian guide, in a signed essay printed as chapter 4 of the
canon's third book, and it is absent from the 2005 French combined edition
of the messages. The message text proper (TBWTT ch. 2 ¶14, ¶58) establishes
the single continent, the later drift, and the nuclear strike — but not that
the strike broke the continent. The record's "canonical layer" therefore
has two tiers of very different standing, and the record and specification
must say so rather than folding them into "the canon is explicit". Whether
a signed guide's essay printed with the message carries canonical weight is
a stance question for the founder, not something a review can settle; the
review only establishes what the text is.

**For the citation.** The alternative's clause *"whose petroleum-ring
citation … is unverified"* is discharged: the study exists, is CIA-sponsored
as stated, and contains the ring. Two errors are Terrusse's or his
translators': the institution (RAND, not the Hudson Institute) and the
title *professor*; the printed English adds a third (*tertiary* for
*Triassic*). None of them touches the observation. The observation itself
cuts both ways for the corpus: it is a real, named anomaly that mainstream
petroleum geology in 1978 called unexplained, which is why Terrusse could
use it; and it sits on a Pangaea reconstruction at 180 million years,
which is the mainstream timescale the record's first alternative asserts.
Nehring's ring supports the *existence* of the pattern, not the recent
strike.

**For locators.** Finding 4 means every `LWTE-4:<n>` locator in the record,
specification, evidence map, and the four bound pages was an English-column
locator and silently missed the French sentences that carry the residual-
velocity reading. The corpus's "residual momentum" claim about present-day
drift is sourced only in French (`n=40–41`).

**For the first alternative, *plate-tectonics*.** The sources say what the
record says they say. U and DH date the onset of breakup to the Triassic,
200 million years ago, and DH describes it as staged — separate rifts,
separate periods, Triassic to Recent — not one displacement. DG is the
decisive row for Terrusse's residual-velocity mechanism (French `n=40–41`):
rates averaged from the seafloor record over 0.78–3.16 million years and
rates measured by GPS over decades agree to a few millimetres per year,
and the only changes the data resolve are slowdowns of that order over
millions of years. A drift that had opened the Atlantic since c. 6,690
BCE would have to have averaged hundreds of metres per year and be
decaying by four orders of magnitude within the geological interval MORVEL
averages over; the reviewer notes that U's account of magnetic striping
(a reversal record whose reversals each last hundreds of thousands of
years) is the independent constraint on such a history, but this inference
is the reviewer's, not a statement in any witness. The alternative stands
as the record states it, and finding 6 adds that the one empirical datum
Terrusse adduces is itself drawn on this timescale.

**For the second alternative, *deep-time-strata*.** KU and MG together
supply what R in 1978 said was not yet available: an account of the
concentration of petroleum. KU locates it in six source-rock intervals
spread across a third of Phanerozoic time with no cyclicity, controlled by
paleolatitude, basin structure and the evolution of biota, most of it
generated in the last 90 million years; MG locates the giants in the
tectonic settings that the staged breakup itself produced — passive
margins and rifts first of all. Neither source describes, or leaves room
for, a single burial. The alternative stands, and the "ring" is on this
reading a consequence of where the Pangaean margins rifted, which is why
it appears on a Pangaean map.

**For the third alternative, *commentary-not-message*.** Now a settled
fact about authorship joined to an open question about weight (above).

**For the fourth alternative, *flood-geology-inheritance*.** MO's
description confirms the genealogy the alternative relies on — modern
creationism's global flood built on a critique of geology — without
supplying wording from WM; the alternative stands as stated, unread.

**For the mainstream catastrophist row.** FS proposes a North American
event 12,900 years ago and nothing about continents; it establishes that
recent catastrophe is discussed in mainstream paleoscience, as the record
says, and nothing more. The corpus's c. 6,690 BCE date is not near it.

**For the claim as a whole.** Nothing read supports the corpus reading of
present-day drift as a decaying residue or of the strata as one burial;
every scientific witness contradicts it on the timescale, and the two
petroleum witnesses explain the very pattern Terrusse used. The claim's
canonical basis is thinner than the record first stated (one signed essay,
plus a message text that gives a strike and a drift but no breakup). None
of this bears on the claim's *lifecycle* or *label*: the record is the
corpus's declared position and stays `framework`. It bears on
`evidence_status`, where `contested` is confirmed and, the search and
appraisal now being reproducible and complete at the access levels stated,
`reviewed` is warranted alongside it.

## Limitations

- The 1979 first editions are not held. D's French column is the only
  witness to the 1979 text, and `_meta.json` does not record which printing
  was digitized or by what process; the byline and the residual-velocity
  sentences rest on that single witness.
- R was read as 150-dpi tesseract output. The quoted passage was checked
  against the page image for the figures and names; other pages were not
  proofread. The file is not yet in `data-sources`.
- DH was read in its JGR form, not the *Scientific American* version R
  cites; the two are the same authors' reconstruction of the same year.
- DG, KU, MG and FS were read at abstract level; the figures quoted are
  the abstracts' own. L is a poor OCR of a Google scan and was searched,
  not read; the quoted summary is from its Book I chapter list.
- WM was not read. MO was read as a publisher description, not as text.
- The reviewer's magnetic-reversal inference under the first alternative is
  marked as such and is not a finding.
- W is a secondary web repost and was used for attribution only.

## Outcome

The claim's **canonical basis is clarified, not confirmed as canon-explicit**;
its **one external citation is verified with corrections**; its **declared
alternatives are confirmed against their sources at the access levels
stated**, and none of the sources read supports the corpus reading on the
timescale. The reviewer recommends `evidence_status: reviewed, contested`.
The recommendation is not self-executing: the record stays `scoped,
contested` until a signature.

Recommended, in order:

1. **Split the canonical layer in the record and specification.** State
   that TBWTT ch. 2 ¶14 and ¶58 supply the single continent, the drift and
   the strike, and that the breakup, the burial ring and the residual
   velocity come from Marcel Terrusse's essay *Raelism Through the Eyes of
   Science*, §2, printed as ch. 4 of *Let's Welcome the Extraterrestrials*
   (E pp. 330–332; D French `n=26–46`). Replace "the canon is explicit that
   it rewrote the rocks" wherever it appears (specification; the four
   derivative pages) with wording that names the essay and its author.
   Refer the *weight* question to the founder as a recorded revision
   trigger rather than deciding it in prose.
2. **Correct the citation everywhere it is paraphrased.** Replace "a Hudson
   Institute study attributed to 'Nebring'" with *Nehring, Richard, Giant
   Oil Fields and World Oil Resources, R-2284-CIA, The Rand Corporation,
   June 1978, prepared for the Central Intelligence Agency; p. 39 and
   Fig. 3.1 (p. 40)*. Under the feedback rule, add the report to
   `source_references` with `role: scientific_context` and an honest
   `access`; the review read the full scan, so `full_text` is accurate for
   the review, but the file should be added to `data-sources` holdings so
   the level is true of the project and not only of one session. The
   report needs a registry ID first (proposed: `nehring-giant-oil-fields-1978`).
3. **Fix the locators.** Give French-column locators (`LWTE-4:26–46`,
   with `n=34–41` for the strike, burial and drift and `n=40–41` for the
   residual velocity) alongside the English ones, and cite E by printed
   page. The Great Flood wiki entry, which quotes the English passage,
   should say which edition it quotes.
4. **Rewrite the third alternative and the first two revision triggers.**
   *commentary-not-message* should now read as the settled fact plus the
   open weight question; the "settle the authorship" and "verify the
   citation" triggers are discharged and should be replaced by: a ruling
   on the canonical weight of signed contributions printed with the
   messages; collation against a 1979 printing; a reading of Dietz and
   Holden (1970).
5. **Add the component-4 witnesses to `source_references`** under the
   feedback rule, with honest access levels: DG, DH, KU and MG as
   `scientific_context` at `abstract`; U as `scientific_context` at
   `full_text`. Registry IDs: `demets-gordon-argus-2010-morvel`,
   `dietz-holden-1970-pangaea`, `klemme-ulmishek-1991-source-rocks`,
   `mann-gahagan-gordon-2003-giant-fields`, `this-dynamic-earth-usgs`. Do
   not add WM beyond its existing `metadata_only` entry; it was not read.
6. **Leave `evidence_status` at `scoped` and `contested` until signed;
   record `reviewed` as the recommendation.** Version: MINOR twice —
   `0.1.0` → `0.2.0` for recommendations 1–4 and `0.2.0` → `0.3.0` for
   recommendation 5 (added evidence and source references; statement, kind,
   relation, label and dependencies unchanged) — which re-keys the four
   bound pages.

Three findings fall outside this claim and are logged for their own repos:

- `data-library/lets-welcome-the-extraterrestrials/chapter-4.json`: the
  French and English columns are different texts (1979 French, 2005
  English) with different paragraphing, stored under shared paragraph
  numbers. Any `LWTE-4:<n>` citation is ambiguous until the book records
  its alignment or the two columns are re-cut.
- The printed 2005 English (E p. 330) reads *"Nebring"* and *"tertiary"*
  where the French and the study read *Nehring* and *Triassic*. These are
  edition facts, not transcription errors, and should not be "corrected" in
  the digitization; a note in the book's `_meta.json` would prevent a
  future editor from doing so.
- The 2005 French combined edition omits the commentaries chapter. The
  project's source note for the combined volumes should say so, since a
  French-first reader will otherwise not find the passage.

## Sign-off

Not signed. Recommendations 1–4 were applied on 2026-09-15 as factual
corrections within agent authority (the record's version moved to
`0.2.0` and the four bound pages were re-keyed); recommendation 5 was
applied the same day (`0.3.0`, re-keyed again); the canonical-weight
question was recorded as a revision trigger and left to the founder. The
record itself grants no status: the claim remains `scoped` and `contested`
until the founder signs, at which point the recommendation is `reviewed`
and `contested`.

| Field | Value |
| --- | --- |
| Reviewer | — |
| Date | — |
| Status granted | none; claim remains `scoped` and `contested`; recommendation `reviewed` + `contested` |
