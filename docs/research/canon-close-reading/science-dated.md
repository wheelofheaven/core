---
title: "Canon close reading: scientific statements against the dated record"
status: draft
version: 0.1.0
last_reviewed: 2026-11-12
---

# The canon's "science has just found / will soon do" statements against the dated published record (key: `science-dated`)

Follow-up to `science.md` (its finding 3 and its table "Candidates for dated comparison"). All outside sources accessed 2026-11-12.

## Exact question

For the canon's statements that lean on what terrestrial science had "just" discovered or was about to achieve, what did the published science actually say, and when? Each statement's exact French wording is set beside the dated record and classified: wording **matches** the then-current published state / **goes beyond** it / **lags** it / rests on a result **later abandoned** / **not determinable**.

## Method

- Canon wording: re-read from the French dumps; every quotation is a `QUOTE[REF]` line and was run through `verify_quotes.py`.
- Outside record: only pages actually retrieved. Three retrieval routes, marked on every source:
  - **[direct]** — text pulled as plain text (NCBI E-utilities for PubMed records; Wikipedia API plain-text extracts; one PDF converted with `pdftotext`). Quotations are verbatim from that text.
  - **[fetch]** — page read through the WebFetch tool, which returns short quoted fragments; the fragments are given as the tool returned them.
  - **[search-summary]** — only a search-engine summary was seen; treated as a lead, never as a fact, and labelled *unverified*.
- Source kinds: PubMed/MEDLINE bibliographic records and abstracts (primary-literature metadata); a journal-abstract database (EarthRef); Google Books bibliographic feed; one history-of-neuroscience review abstract; magazine articles; Wikipedia (tertiary — used for dates and for general state-of-the-field statements where no primary abstract was reachable; flagged each time).
- Not reachable from this environment (null results, see Limitations): BnF catalogue, SUDOC, WorldCat result lists, nature.com and royalsocietypublishing.org article pages, apa.org, Encyclopaedia Iranica.
- Dates of the canon: TBWTT dictated December 1973 (published 1974); ETTMTTP 1975; LWTE 1979. "Then-current" means published before those dates.
- No verdict is given beyond what the two wordings support. Classification labels are mine (analysis layer).

## Findings (ranked)

### 1. The rat memory-transfer sentence matches a real, then-recent published claim — which was contested in print from its first year and later abandoned

(a) Canon.

QUOTE[TBWTT-7:61]: grâce à une découverte scientifique importante que vos savants commencent à entrevoir on peut apprendre à un sujet ses leçons chirurgicalement ENDQUOTE
QUOTE[TBWTT-7:62]: Vos savants viennent de découvrir que l’on peut en injectant dans le cerveau d’un rat le liquide de la mémoire d’un rat éduqué, faire en sorte que le rat qui n’a rien appris, sache ce que l’autre savait ENDQUOTE
QUOTE[LWTE-4:132]: L'étude du mécanisme du codage de l'information dans les molécules d'A.R.N. nous amènera à comprendre, puis à utiliser les substances mémorielles contenues dans notre cerveau... Substances qui pourront être transférées d'un individu à un autre. ENDQUOTE

(b) Published record (dated).

| Date | Who / where | What the record says (verbatim) | Src |
|---|---|---|---|
| 6 Aug 1965 | Babich, Jacobson, Bubash, Jacobson, *Science* 149:656–7 | "Ribonucleic acid was extracted from the brains of these rats and injected into untrained rats. The untrained rats then manifested a significant tendency (as compared with controls) to approach the food cup when the click, unaccompanied by food, was presented." | S01 |
| 29 Oct 1965 | Jacobson et al., *Science* 150:636–7 | "On the average, the response appeared to be specific to the stimulus employed during training." | S02 |
| 24 Dec 1965 | Gross & Carey, *Science* 150:1749 | Title: "Transfer of learned response by RNA injection: failure of attempts to replicate." | S03 |
| 18 Feb 1966 | Luttges, Johnson, Buck, Holland, McGaugh, *Science* 151:834–7 | "Nucleic acid extracted from brains of trained animals and injected intraperitoneally into naive animals produced no \"transfer of learning\" effect on several tasks under many conditions. […] Even intraventricular injections of nucleic acid produced no \"transfer\" effect." | S04 |
| 5 Aug 1966 | Byrne, Samuel, Bennett, Rosenzweig, Wasserman (as indexed), *Science* 153:658–9 | Title: "Memory transfer." (no abstract in the record; that it reports negative results I saw only in a search summary — *unverified*) | S05 |
| 30 Mar 1968 | Ungar, Galvan, Clark, *Nature* 217:1259–61 | Title: "Chemical transfer of learned fear." | S06 |
| 24 Jul 1970 | Frank, Stein, Rosen, *Science* 169:399–402 | "These results are interpreted in terms of stress, rather than a memory transfer hypothesis." | S11 |
| 10 Sep 1971 | Goldstein, Sheehan, Goldstein, *Nature* 233:126–9 | Title: "Unsuccessful attempts to transfer morphine tolerance and passive avoidance by brain extracts." | S09 |
| 28 Jul 1972 | Ungar, Desiderio, Parr, *Nature* 238:198–202 | Title: "Isolation, identification and synthesis of a specific-behaviour-inducing brain peptide." | S07 |
| 28 Jul 1972 | Stewart, *Nature* 238:202–10 (same issue, following pages) | Title: "Comments on the chemistry of scotophobin." | S08 |
| 15 Dec 1972 | Malin & Guttman, *Science* 178:1219–20 | "Two independent research groups replicate alteration of dark preference to dark avoidance by mice injected with synthetic scotophobin, a pentadecapeptide." | S10 |
| 1978 | Wójcik & Niemierko, *Acta Neurobiol Exp* 38:25–30 | "Thus the effect of scotophobin on the behavior of animals is not specific and this substance can not be considered responsible for the \"memory transfer\"." | S13 |
| May 1978 | Misslin, Ropartz, Ungerer, Mandel (Strasbourg), *Behav Processes* 3:45–56 | Title: "Non-reproducibility of the behavioural effects induced by scotophobin." Abstract: "Only one of these samples gave results similar to those described previously by Ungar et al. (1972)." | S12 |
| 1997 | Setlow, *J Hist Neurosci* 6:181–92 | "The idea that memories could be transferred from one organism to another by administration of a \"trained\" donor brain to a naive recipient seized both scientific and public attention in the 1960's and early 1970's." | S14 |
| 2021 | *Science News* (retrospective on its 6 Nov 1971 item) | scotophobin as a memory store was met with "intense skepticism" and "eventually discredited by neuroscientists" | S15 |
| (current) | Wikipedia, "Scotophobin" | "According to the current knowledge, scotophobin cannot have the effect attributed to it." Experimental set-up: "an extract was prepared from their brains, which was injected into mice". | S16 |
| 21 May 2018 | Bédécarrats … Glanzman, *eNeuro* 5(3) | "RNA extracted from the central nervous system of Aplysia given long-term sensitization (LTS) training induced sensitization when injected into untrained animals" | S17 |

(c) Comparison (analysis).

- **Existence and date: matches.** In December 1973 there was a published claim of exactly this kind, in rats, eight years old (1965), with a fresh high-profile restatement seventeen and twelve months earlier (*Nature*, July 1972; *Science*, December 1972). "Viennent de découvrir" fits the 1972 publications better than the 1965 ones.
- **Standing in 1973: the canon's wording is firmer than the record.** The same journals carried failures to replicate from December 1965 onward, and the 1972 *Nature* paper was printed with a referee's critical commentary immediately behind it. The canon says "découvrir"; the record in 1973 was a disputed claim.
- **Scope: goes beyond.** The published positive claim is a "significant tendency" in one conditioned response. The canon's "sache ce que l'autre savait" and the schooling by injection built on it (TBWTT-7:62) are not in any record I retrieved.
- **Route: not settled by what I could open.** Canon: "dans le cerveau". The 1965 abstracts say only "injected into untrained rats"; Luttges et al. 1966 name the intraperitoneal route as the one tested and add that intraventricular (into-the-brain) injection also gave nothing. Wikipedia describes Ungar's design as rat-brain extract injected into mice (route not stated). Whether any positive report used intracerebral injection in rats: **not determinable** from retrieved pages.
- **Later fate: abandoned.** Non-reproducibility was in print by 1977–78 (one of the reports from Strasbourg); the 2021 retrospective and the encyclopaedia entry treat the result as discredited. One partial modern echo exists (2018, sea slugs, RNA, sensitization — a non-associative effect, not learned content).
- **Terrusse 1979 (LWTE-4:132)** is a forecast in the future tense, in RNA vocabulary. It was written after the non-reproducibility reports of 1977–78 and rests on the same research line. Classification: forecast resting on a result later abandoned; the 2018 report is the only retrieved item in its direction.

### 2. The nearest-star objection printed in LWTE is the published state, then and now; the canon's distance conflicts with it, and a 2014 infrared survey excludes a large body at that range

(a) Canon.

QUOTE[TBWTT-5:52]: Notre planète est à 30 millions de parasanges soit neuf mille milliards de kilomètres environ ou un peu moins d’une année lumière ENDQUOTE
QUOTE[TBWTT-5:53]: La planète des créateurs est éloignée de son soleil de 236 000 parasanges, soit 70 milliards huit cent millions de kilomètres, c’est la «hauteur du créateur», par rapport à son soleil, un grosse étoile. ENDQUOTE
QUOTE[LWTE-1:26]: Les scientifiques terrestres actuels disent que la plus proche étoile en dehors de notre soleil est située à environ quatre années-lumière ENDQUOTE
QUOTE[LWTE-1:27]: J'y ajouterai que la lumière ne se déplace pas à la même vitesse dans toutes les couches de l'univers, car rien n'est constant ni dans l'espace ni dans le temps ENDQUOTE
QUOTE[LWTE-4:121]: Toutes les distances en années-lumière calculées par les méthodes traditionnelles sont surévaluées. ENDQUOTE

(b) Published record.

- Alpha Centauri parallax: "eventually published them in 1839" (Henderson); "now reckoned at 4.396 light-years" (S71, Wikipedia, tertiary).
- Proxima Centauri: "Discovered in 1915 by Robert Innes"; "the nearest star to Earth after the Sun, located 4.25 light-years (1.3 parsecs) away"; "Based on a parallax of 768.0665±0.0499 mas, published in 2020 in Gaia Data Release 3, Proxima Centauri is 4.2465 light-years" (S70).
- Light-year: "equal to exactly 9460730472580.8 km" (S74).
- WISE all-sky infrared survey, reported March 2014 (K. Luhman): "no object the size of Saturn or larger exists out to a distance of 10,000 astronomical units (AU)"; no object larger than Jupiter out to 26,000 AU; "The outer solar system probably does not contain a large gas giant planet or a small companion star" (S72, magazine report of the study). Wikipedia on the same survey: "WISE can detect 150-kelvin brown dwarfs out to 10 light-years, and the closer a brown dwarf is, the easier it is to detect." (S73).
- Speed of light: "Prior to 1983, the meter was defined separately from the second and the speed of light was measured experimentally."; since 1983 fixed "at 299792458 m/s by definition" (S75).

(c) Comparison.

- LWTE-1:26 (the questioner's sentence, "environ quatre années-lumière"): **matches** the published state of 1979 and of today.
- TBWTT-5:52 arithmetic: 30,000,000 × 300,000 km = 9 × 10^12 km; a light-year is 9.46 × 10^12 km, so "un peu moins d'une année lumière" is internally consistent (≈ 0.95 ly) (my arithmetic).
- A "grosse étoile" at under one light-year **conflicts with** the published record both in 1973 (nearest star 4.2–4.4 ly, measured since 1839/1915) and after (2014 survey). 9 × 10^12 km is about 60,000 AU `[outside knowledge — unverified, needs source: 1 AU ≈ 149.6 million km]`; the quoted planet limits reach 26,000 AU, the quoted brown-dwarf sensitivity reaches 10 light-years. The canon itself offers the reply that the location is withheld (LWTE-1:27).
- LWTE-1:27 / 4:121 (variable light speed; distances overestimated): **goes beyond**; I retrieved no published result supporting either, and the constant has been fixed by definition since 1983. Not tested further here.
- QUOTE[TBWTT-5:52]: Avec vos fusées actuelles qui ne se déplacent qu’à 40 000 km/h ENDQUOTE — **matches**: Apollo 10 "set the record for the highest speed attained by a crewed vehicle relative to the Earth's surface: 39,897 kilometers per hour […] on May 26, 1969" (S76).

### 3. The parasang of the historical record is a walking-distance unit of about 5–6 km; the canon's parasang is 300,000 km

(a) Canon.

QUOTE[TBWTT-5:52]: Le parasange qui, comme le parsec, est une unité de mesure, équivaut à la distance que parcourt la lumière en une seconde soit environ 300 000 kilomètres. ENDQUOTE
QUOTE[TBWTT-5:51]: En particulier une description dans le Cantique des Cantiques (V) de la planète des créateurs ainsi que la distance qui la sépare de la Terre. ENDQUOTE

(b) Record (Wikipedia "Parasang", tertiary; citing Bivar 1985, Smith 1870 — not opened): "a historical Iranian unit of walking distance"; Herodotus equates it to "30 stadia"; "either 5.7 km (Olympic measure) or 5.3 km (Attic measure)"; the Hebrew form *parsah* "finds use in the Babylonian Talmud" (S80, [fetch]). Parsec: "coined by the British astronomer Herbert Hall Turner in 1913"; "approximately equal to 3.26 light-years" (S81). Shi'ur Qomah: "an exegetical analysis of Song of Songs 5:11-16" (S82, [fetch]; the page gives no parasang figures — null for the numbers; core `woh-claim-0021` already records them as attested).

(c) Comparison. "Est une unité de mesure" and the parsec comparison: **match** (both are real units of length). The value "distance que parcourt la lumière en une seconde": **does not match the historical unit** — a factor of roughly 50,000–57,000 (300,000 ÷ 5.3–5.7; my arithmetic). In the canon the value is Yahweh's gloss, not attributed to the source text. The pointer "Cantique des Cantiques (V)" agrees with the encyclopaedia's description of the Shi'ur Qomah as exegesis of Song 5:11–16 (favourable to the canon's bibliographic pointer; says nothing about the gloss). This is the "units retrofit" alternative already listed in core 0021, now with a sourced value for the historical unit.

### 4. Ararat wood: published radiocarbon ages are about 1,200–1,700 years (about A.D. 260–790); the canon says 700 years / "l'an mille deux cents"

(a) Canon.

QUOTE[LWTE-1:45]: l'on a trouvé voici quelques années dans un glacier du mont Ararat les restes d'un bateau ENDQUOTE
QUOTE[LWTE-1:46]: Les morceaux de bois qui ont été retrouvés ont été récemment analysés, et l'on s'est aperçu qu'ils n'étaient vieux que de sept cents ans, ce qui placerait cette arche de Noé aux environs de l'an mille deux cents. ENDQUOTE

(b) Record.

- Finds: Navarra 1955 ("En 1955, il découvrit des morceaux de bois « sciés à la main » dans une profonde crevasse", S105); SEARCH expedition 1969, wood "found July 31 and August 2", at "some 13,000 feet above sea level on the slopes of Mount Ararat"; the earlier timber then "believed to be about 4,000 years old (according to carbon tests)" (*Christianity Today*, 12 Sep 1969; S103, [fetch]).
- Radiocarbon, as reported in *Bible and Spade* 6:3, Summer 1977 (secondary report; S100, [fetch]): UCLA (R. Berger), tree "chopped down around A.D. 700"; UC Riverside (R. E. Taylor), lignin fraction "1,210 ± 90 years"; UK National Physical Laboratory, "1,190 ± 90 years".
- Wikipedia, "Searches for Noah's Ark" (S102, [direct], tertiary): "The 1955 samples were analyzed by five institutions, with results dating the wood to approximately 1,200-1,700 years ago. Two analyses of the 1969 samples dated the wood to about 1,350 years ago." Also: "Analyses based on color, density, and lignitization reportedly indicated the wood was about 5,000 years old".
- TalkOrigins CH504.2 (critical secondary, citing Bailey 1989 and LaHaye & Morris 1976 — not opened; S101, [fetch]): one lab 260 C.E. ±120; three labs roughly 720–790 C.E.; 1969 samples about 650 C.E. and 630 C.E.
- The peer-reviewed statement is Taylor & Berger, "The date of 'Noah's Ark'", *Antiquity* 54(210): 34–36, March 1980 (S104: citation seen; article text behind paywall — figures **not** verified from it).

(c) Comparison.

- Finding and place ("voici quelques années", glacier, Ararat): **matches**.
- Direction of the result (wood far too young for a Flood-era ship): **matches**.
- The number: **does not match** any report I retrieved. No source gives an age of 700 years or a date near A.D. 1200. The published values are an age of about 1,200 years and a calendar date of about A.D. 700. Raël's pair (age 700, date 1200) contains the same two numbers with roles exchanged. That is an observation; whether it is a transposition, a different report, or a French press figure I did not find is **not determinable** here.
- Raël's own arithmetic (700 × 3 ≈ 2,000 → "début de l'ère chrétienne") follows from his figure. With the published ages (about 1,200–1,700 years) the same tripling gives about 3,600–5,100 years (my arithmetic), which reaches the "environ cinq mille ans" he assigns to the real Flood (LWTE-1:47); with those figures the "ne colle toujours pas" step of the printed argument would not follow as stated.
- "Récemment analysés" (1979): the reported US re-tests were published by 1977; the first tests date from the 1950s–60s. Fits loosely.

### 5. "Evolution ou Création": most probably Flori & Rasolofomasoandro, Éditions SDT, 1974 — identified from a bibliographic feed, not from a national-library catalogue; what it says about dating was not retrievable

(a) Canon.

QUOTE[LWTE-1:28]: Il existe d'ailleurs un ouvrage très intéressant qui développe tout cela très sérieusement pour les scientifiques que cela intéresse, je veux parler de Evolution ou Création (voir bibliographie en fin d'ouvrage). ENDQUOTE
QUOTE[LWTE-1:28]: l'erreur de ces méthodes de datation est de partir du principe que le comportement atomique actuel a toujours été le même ENDQUOTE

(b) Record.

- Google Books bibliographic feed (S90, [fetch]): "Évolution ou création?" — authors Jean Flori, Henri Rasolofomasoandro; publisher "Dammarie les Lys : Éditions SDT"; date 1974; 381 pages; LCCN 75510211 (two further stub records for the same title/year, one with LCCN 74182820).
- Same feed, the only other pre-1979 French title match: "Evolution ou création", Arthur Dubois and Odette Fribault, 1957, 496 pages, OCLC 460428376 (no publisher shown).
- An independent French critical dossier, "Le créationnisme est-il scientifiquement recevable ?" (C. Nitschelm, D. Geney, L. Plateaux, P. Roux; dated in the text "Paris, avril 1987 / Genève, décembre 1988"; S91, [direct] from PDF) lists as its creationist source I: "Flori, J. & Rasolofomasoandro, H.: 1974 , “ Évolution ou Création? ”, éditions S.D.T., Dammarie-les-Lys, France." and calls it "ouvrage créationniste typique". Plateaux's remarks on the book: "L'interprétation littérale du déluge vue dans ce livre est inconciliable avec la répartition des espèces." The dossier's general section on creationist dating arguments (not tied to this book by page): "Les créationnistes, cherchant à “ prouver ” l'âge peu élevé de la Terre, environ dix mille ans selon eux, essaient de trouver des failles dans les mesures et dans la logique de ces méthodes." and "La datation au carbone 14 est en particulier un de leurs chevaux de bataille".
- Standard account of the assumption Raël attacks (Wikipedia "Radiometric dating", tertiary; S92): "For most radioactive nuclides, the half-life depends solely on nuclear properties and is essentially constant. This is known because decay constants measured by different techniques give consistent values within analytical errors and the ages of the same materials are consistent from one method to another."

(c) Comparison.

- **Update 2026-11-12:** confirmed by the book's own bibliography in the held 2001 French and 2005 English editions; see [editions.md](editions.md) section 4.1. The paragraph below is kept as first written.
- Identification: **probable, not confirmed.** Title, country, date (five years before LWTE) and subject fit Flori & Rasolofomasoandro 1974; the 1957 Dubois–Fribault title is a second candidate I could not characterise. LWTE's own bibliography (not in the dump) would settle it. `[outside knowledge — unverified, needs source: Éditions SDT = "Signes des Temps", the French Seventh-day Adventist publishing house at Dammarie-lès-Lys; Jean Flori later a medieval historian.]`
- What the book argues about dating: **not determinable** from retrieved pages. The 1987–88 dossier shows it is a young-Earth, literal-Flood creationist work and that such works attack radiometric and carbon-14 dating; it does not quote the book's dating chapter. Whether the book makes Raël's specific argument (atomic behaviour not constant over time) is unverified.
- Raël's premise against the record: mainstream sources state decay constancy as measured and cross-checked (S92). Raël's sentence denies it without a cited measurement. Classification: **goes beyond / contradicts** the published state of 1979 and of today. If the identification holds, the awkward corollary is that the one terrestrial book the canon recommends on dating is a young-Earth creationist work whose framework (a recent divine creation, a literal ship-borne Flood) the canon itself rejects; Raël cites it for the critique of dating only.

### 6. Continental fit: the single-continent idea was 60 years old in 1973; its acceptance was 5–8 years old; the "perfect fit" wording has a 1965 counterpart

(a) Canon.

QUOTE[TBWTT-2:14]: À l’origine, il n’y avait qu’un continent sur la Terre et vos savants viennent d’ailleurs de s’apercevoir que tous les continents qui ont dérivé s’emboîtent parfaitement pour n’en former qu’un seul. ENDQUOTE
QUOTE[LWTE-1:30]: le continent américain continuant de s'écarter de l'Europe de quelques centimètres par an selon certains scientifiques, d'un mètre selon d'autres ENDQUOTE
QUOTE[LWTE-1:31]: Il y a eu récemment un tremblement de terre près de la péninsule arabique, et l'on a eu la surprise de constater qu'une faille s'était créée, écartant deux régions de plus d'un mètre en une seule nuit! ENDQUOTE

(b) Record (Wikipedia unless stated; tertiary).

- 1596: the page attributes the first speculation about drifted continents to Abraham Ortelius (S33, [fetch]; tool paraphrase, not a verbatim quotation).
- 1912/1915: "hypothesised, with corroborating evidence, by Alfred Wegener […] in three 1912 academic journal articles"; in the 1915 book "all the continents had formed a single supercontinent that he called the Urkontinent" (S30).
- Reception: "Wegener's work was initially not widely accepted" (S31); French article: "Les travaux de Wegener ont assez peu de succès auprès de la communauté géologique et géophysique" (S34).
- 1965: "A symposium on continental drift was held at the Royal Society of London in 1965 which must be regarded as the official start of the acceptance of plate tectonics by the scientific community"; "Edward Bullard and co-workers showed with a computer calculation how the continents along both sides of the Atlantic would best fit to close the ocean, which became known as the famous \"Bullard's Fit\"." (S31). On Bullard: "By doing this he discovered a near perfect fit among the continents put together." (S32).
- 1965–68: "The theory of plate tectonics was defined in a series of papers between 1965 and 1967."; Le Pichon's six-plate model "marked the final acceptance by the scientific community of plate tectonics" (S31). French article: "forgée par la communauté géologique et géophysique internationale à la fin des années 1960" (S34).
- Rates: Mid-Atlantic Ridge "average spreading rate of about 2.5 centimetres (1 in) per year" (S35).
- Afar: Ruegg, Kasser, Lépine, Tarantola, "Geodetic measurements of rifting associated with a seismo-volcanic crisis in Afar", *Geophys. Res. Lett.* 6 (1979): the resurvey "shows an horizontal extension of about 2 m and a vertical movement up to 70 cm" (S36, [fetch]). The associated eruption: "from November 7 to 14, 1978"; "Preceding the onset of the eruption, a total of 800 earthquakes of magnitude less than 3.3 occurred for 24 hours" (S37).

(c) Comparison.

- TBWTT-2:14: relative to **acceptance** (1965–68) "viennent de s'apercevoir" **matches**; relative to the **idea** (1912–15; the coastline fit noticed earlier) it **lags** by about sixty years. "S'emboîtent parfaitement" has a counterpart in the 1965 computer fit as the encyclopaedia words it ("near perfect"). The record's fit concerns the Atlantic margins and a continent that broke up over geological time; the canon's mechanism (explosions) and its 25,000-year scale are not in the record, as the question at LWTE-1:30 itself points out.
- LWTE-1:30, "quelques centimètres par an": **matches** (2.5 cm/yr). "D'un mètre selon d'autres": no source found — **not determinable**.
- LWTE-1:31, the Arabian-peninsula earthquake: **matches a published event**, if it is the Asal–Ghoubbet (Djibouti) crisis of November 1978 — an identification that is my inference from date, place and magnitude; the text names neither. Published extension about 2 m (canon: "plus d'un mètre"). "En une seule nuit" is not confirmed by what I retrieved (the crisis ran about a week). Favourable to the report's factual core; the inference Raël draws from it (hundreds of km per year formerly) is not in the record.

### 7. Terrusse's 1979 genetic-engineering sentence matches the record closely; Raël's "bientôt" for synthetic genetic codes partly lags it

(a) Canon.

QUOTE[LWTE-4:129]: Prenez conscience que l'on a synthétisé des gènes par assemblage de nucléotides; que des segments de molécules d'A.D.N. ont été implantés à l'intérieur de chromosomes bactériens; que le transfert de matériel génétique d'un organisme à un autre nous devient familier... ENDQUOTE
QUOTE[LWTE-1:152]: l'homme, qui sera bientôt capable de créer synthétiquement de nouveaux codes génétiques, de nouveaux plans, à partir de matière inanimée ENDQUOTE
QUOTE[LWTE-4:131]: sur la création d'espèces animales nouvelles, et à terme sur la synthèse d'humanoïdes à notre image ENDQUOTE

(b) Record (PubMed, [direct]).

- 4 Jul 1970: Agarwal … Khorana … et al., *Nature* 227:27–34, "Total synthesis of the gene for an alanine transfer ribonucleic acid from yeast." (S40). (Wikipedia dates the "first complete gene" to 1972 — S46; the *Nature* title is 1970.)
- Oct 1972: Jackson, Symons, Berg, *PNAS* 69:2904–9: "We have developed methods for covalently joining duplex DNA molecules to one another" (S41).
- Nov 1973: Cohen, Chang, Boyer, Helling, *PNAS* 70:3240–4: "Newly constructed plasmids that are inserted into Escherichia coli by transformation are shown to be biologically functional replicons" (S42).
- 9 Dec 1977: Itakura … Boyer, *Science* 198:1056–63: "This represents the first synthesis of a functional polypeptide product from a gene of chemically synthesized origin." (S43).
- 16 Feb 1979: Khorana, *Science* 203:614–25, "Total synthesis of a gene": "All the segments are chemically synthesized starting with protected nucleosides and mononucleotides." (S44).
- 10 Jul 1979: Ryan … Khorana, *J Biol Chem* 254:5817–26: the synthetic gene "has also been shown to suppress bacterial amber mutations after it had been incorporated into the E. coli chromosome as part of a lambda prophage." (S45).
- 2010: Gibson … Venter, *Science* 329:52–6: "We report the design, synthesis, and assembly of the 1.08-mega-base pair Mycoplasma mycoides JCVI-syn1.0 genome starting from digitized genome sequence information and its transplantation into a M. capricolum recipient cell" (S51). 2016: Hutchison … Venter, *Science* 351: "JCVI-syn3.0 (531 kilobase pairs, 473 genes), which has a genome smaller than that of any autonomously replicating cell found in nature." (S52).

(c) Comparison.

- LWTE-4:129: **matches** on all three clauses — gene synthesis from nucleotides (1970, 1977, 1979); DNA put into bacteria (1973 as plasmids; 1979 into the chromosome via a prophage); inter-organism transfer (1972–73). It is a report of published work, in the past tense, one to nine years after the events. The only loose point is "chromosomes bactériens" for what in 1973 were plasmids.
- LWTE-1:152 (Raël, same book): in its minimal sense (synthetic genes from non-living precursors) the thing was already published — the wording **lags** the record that Terrusse reports 100 pages later. In its strong sense (newly designed genomes) it was realised in 2010/2016, 31–37 years after "bientôt"; whether that satisfies "bientôt" is a judgement the sources do not make.
- LWTE-4:131 ("espèces animales nouvelles", "humanoïdes"): forecast; **goes beyond** 1979 and, for humanoids, beyond anything retrieved.

### 8. "Living cells from chemicals — soon": beyond the 1973 record, and by the retrieved sources still not done in the strict sense

(a) Canon.

QUOTE[TBWTT-2:2]: les hommes étaient arrivés à un niveau technique et scientifique comparable à celui que vous aurez bientôt. Ils commencèrent à créer des formes primitives et embryonnaires de vie, des cellules vivantes en éprouvettes. ENDQUOTE
QUOTE[TBWTT-2:16]: des cellules végétales à partir de rien d’autre que des produits chimiques ENDQUOTE
QUOTE[LWTE-2:102]: lorsqu'ils seraient capables de s'égaler à ce qu'ils prenaient pour «dieu » en créant des êtres synthétiques en laboratoire ENDQUOTE

(b) Record.

- Dec 1967: Goulian, Kornberg, Sinsheimer, *PNAS* 58:2321–8, "Enzymatic synthesis of DNA, XXIV. Synthesis of infectious phage phi-X174 DNA." (S50) — a viral genome copied in vitro, not a cell.
- 2010 and 2016: synthetic genome transplanted into an existing recipient cell (S51, S52).
- Wikipedia, "Artificial cell" (tertiary; S53): "A bottom-up approach to build an artificial cell would involve creating a protocell de novo, entirely from non-living materials."; of the strict, living, bottom-up kind: "This kind of artificial cell has not yet been made."

(c) Comparison. In 1973 no living cell had been made from chemicals; the nearest published step was the 1967 in-vitro synthesis of infectious viral DNA. The canon's "bientôt" **goes beyond** the 1973 record. Fifty-three years on, the retrieved sources show a cell run by a chemically synthesised genome (2010) but not a cell built "à partir de rien d'autre que des produits chimiques". LWTE-2:102 lists "êtres synthétiques" among markers already defining the present age in 1979 — **beyond** the record for that item (see finding 10 for the other two markers).

### 9. Whole organism from one cell: the principle was in print before 1973 (frogs, plants); the mammal from an adult cell came in 1996–97; the canon's version (any cell, no egg, memories included) has no counterpart

(a) Canon.

QUOTE[TBWTT-2:58]: En réalité, et vos connaissances scientifiques vous permettront bientôt de le comprendre, il suffit d’avoir une cellule vivante de chaque espèce, mâle et femelle, pour reconstituer ensuite l’être tout entier. ENDQUOTE
QUOTE[TBWTT-7:30]: à partir de n’importe quelle cellule d’un corps on peut recréer l’être tout entier avec de la matière vivante neuve ENDQUOTE
QUOTE[TBWTT-3:186]: Tout cela est très facile à réaliser et vous le ferez un jour. ENDQUOTE
QUOTE[TBWTT-3:283]: Les espèces qui disparaissent pourront revivre quand vous saurez les recréer. ENDQUOTE

(b) Record (PubMed [direct] unless stated).

- May 1952: Briggs & King, *PNAS* 38:455–63, "Transplantation of Living Nuclei From Blastula Cells into Enucleated Frogs' Eggs." (S60).
- 1958: plants — Steward "established that plants could be totally regenerated from one cell" (Wikipedia, tertiary; S67).
- Dec 1962: Gurdon, *J Embryol Exp Morphol* 10:622–40, "The developmental capacity of nuclei taken from intestinal epithelium cells of feeding tadpoles." (S61).
- Aug 1975: Gurdon, Laskey, Reeves: nuclei from adult frog skin cells — "None of the first transfer embryos developed as far as tadpoles." and "We conclude that cell specialization does not involve any loss, irreversible inactivation or permanent change in chromosomal genes required for development." (S62).
- 14 Dec 1984: McGrath & Solter, *Science* 226:1317–9: mouse nuclei from four-cell stage onward "did not" support development (S63).
- Mar 1986: Willadsen, *Nature* 320:63–5: sheep, embryo-cell nuclei, "fully viable embryos may be obtained by this procedure" (S64).
- 27 Feb 1997: Wilmut et al., *Nature* 385:810–3: "The fact that a lamb was derived from an adult cell confirms that differentiation of that cell did not involve the irreversible modification of genetic material required for development to term." (S65).
- 2003 / 2009: Folch et al., *Theriogenology* 71:1026–34: "The newborn died some minutes after birth due to physical defects in lungs. […] To our knowledge, this is the first animal born from an extinct subspecies." (S66).

(c) Comparison.

- "Vous permettront bientôt de le comprendre" (TBWTT-2:58): the principle that a single cell's nucleus carries the whole plan was already published for frogs (1952, 1962) and whole plants from single cells (1958). For that principle the wording **lags** the record; for a mammal from an adult body cell the record came 23 years later (**goes beyond 1973, later realised**).
- "N'importe quelle cellule" and "il suffit d'avoir une cellule": every retrieved method needs an enucleated egg (and, in animals, a surrogate); the adult-frog work of 1975 did not get past tadpoles. **Goes beyond**, then and now, as worded.
- Recreation as an adult "avec toutes ses connaissances" (TBWTT-7:30; see `science.md` finding 2): no counterpart in any retrieved record; not a dated-comparison item.
- TBWTT-3:283: one partial instance (an extinct subspecies, born 2003, lived minutes; cells taken before extinction). **Beyond 1973; partially and narrowly realised.**

### 10. Smaller items: one clear slip, several matches, two overstated "already" claims

| REF, voice | Canon wording | Dated record | Class |
|---|---|---|---|
| TBWTT-3:111, Yahweh | see QUOTE below | Delgado's radio-stimulated bull "conducted in Spain in 1963" (S21, [fetch]); "The bull charged Delgado, who pressed a remote control button which caused the bull to stop its charge." (S20); Delgado, "Radio-controlled behavior", *N Y State J Med*, 1 Feb 1969 (S22). Steered navigation: Talwar et al., *Nature* 2 May 2002, "Rat navigation guided by remote control." — "Free animals can be 'virtually' trained by microstimulating key areas of their brains." (S23) | **Matches** as to the research line (ten years old in 1973; "commencez" is loose but fair). The specific feat glossed (animals steered to deliver food) is nearer the 2002 result than anything retrieved from before 1973: **beyond** in that respect. Not abandoned. |
| LWTE-4:73, Terrusse | see QUOTE below | "Between 1886 and 1889 Hertz conducted a series of experiments"; "He died on 1 January 1894" (S110) | **Does not match**: off by some 35–40 years; Hertz was dead by the 1920s. |
| LWTE-4:73, Terrusse | "la résonance magnétique nucléaire n'est connue que depuis 1946" | "In 1946, Felix Bloch and Edward Mills Purcell expanded the technique for use on liquids and solids" (S111) | **Matches** (the same page credits earlier molecular-beam work to Rabi; not pursued). |
| LWTE-4:10, Terrusse | "H.-J. Muller, prix Nobel 1946" | "awarded the 1946 Nobel Prize in Physiology or Medicine" (S112) | **Matches**. The quotation attributed to Muller was not checked. |
| LWTE-2:102, Yahweh | "faire porter leur voix par-delà les océans en fabriquant des satellites de télécommunication" | Telstar 1 "launched […] on July 10, 1962, and relayed the first television pictures, telephone calls, and telegraph images through space" (S113) | **Matches** (17 years old in 1979). |
| LWTE-2:102, Yahweh | "faire voir les aveugles en fabriquant des prothèses électroniques" | Brindley & Lewin 1968: "it will be possible, by improving our prototype, to make a useful prosthesis"; Dobelle et al., *Science* 1 Feb 1974: "the hope that a functional visual prosthesis can be developed, although many problems remain to be solved" (S114) | **Matches** the experimental state (phosphenes, simple patterns); **beyond** it as a statement that the blind were being made to see. |
| LWTE-1:169, Raël | "Des scientifiques viennent de mettre au point un ordinateur équipé de batteries électriques […] se branche tout seul" | Johns Hopkins Beast, "built in the 1960s"; "it would seek black wall outlets. When it found one it would plug in and recharge."; "It did not use a computer." (S115, tertiary) | Self-recharging: **lags** (done in the 1960s). The specific camera-guided crate-lifting machine of c. 1979: **not determinable** (not identified). |
| ETTMTTP-2:37, Yahweh | "Déjà, dans vos usines les plus modernes […] une personne suffit qui surveille simplement un ordinateur qui commande et réalise toutes les opérations de fabrication de la voiture" | Unimate "worked on a General Motors assembly line […] in 1961"; "FANUC, a Japanese robotics company, has been a lights-out factory since 2001" (S116, tertiary) | **Goes beyond** the retrieved record for 1975: robots on car lines existed; no source found for a car plant run by one person. Weak sourcing — a history of automotive automation was not consulted. |
| ETTMTTP-2:30, Yahweh | "On a pu constater qu'un être perd quelques grammes au moment de sa mort" | "a study published in 1907 by Duncan MacDougall"; "widely regarded as flawed and unscientific due to the small sample size" (S117, tertiary) | **Matches a published claim (1907) that was never accepted** — nearest to "later abandoned". The canon gives its own explanation (energy leaving). |
| TBWTT-5:52, Yahweh | "fusées actuelles […] 40 000 km/h" | Apollo 10: 39,897 km/h (S76) | **Matches**. |

QUOTE[TBWTT-3:111]: Un exemple de téléguidage des animaux par électrode, comme vous commencez à le découvrir ENDQUOTE
QUOTE[LWTE-4:73]: Rappelez-vous que Hertz n'a découvert les ondes qui portent son nom que dans les années 1920 ENDQUOTE
QUOTE[LWTE-4:73]: la résonance magnétique nucléaire n'est connue que depuis 1946 ENDQUOTE
QUOTE[LWTE-4:10]: H.-J. Muller, prix Nobel 1946 ENDQUOTE
QUOTE[LWTE-2:102]: faire porter leur voix par-delà les océans en fabriquant des satellites de télécommunication ENDQUOTE
QUOTE[LWTE-2:102]: faire voir les aveugles en fabriquant des prothèses électroniques ENDQUOTE
QUOTE[LWTE-1:169]: Des scientifiques viennent de mettre au point un ordinateur équipé de batteries électriques. ENDQUOTE
QUOTE[LWTE-1:169]: Aussitôt, il roule vers la prise de courant, se branche tout seul ENDQUOTE
QUOTE[ETTMTTP-2:37]: Déjà, dans vos usines les plus modernes ENDQUOTE
QUOTE[ETTMTTP-2:37]: une personne suffit qui surveille simplement un ordinateur qui commande et réalise toutes les opérations de fabrication de la voiture ENDQUOTE
QUOTE[ETTMTTP-2:30]: On a pu constater qu'un être perd quelques grammes au moment de sa mort ENDQUOTE

## Full register — classification summary

Classes: M = matches then-current published state; B = goes beyond it; L = lags it; A = rests on a result later abandoned / never accepted; X = conflicts with the published state then and now; ND = not determinable from retrieved sources. Voice from `science.md`.

| # | REF | Voice, year | Topic | Class | One-line basis |
|---|---|---|---|---|---|
| 1a | TBWTT-7:62 | Yahweh, 1973 | rat memory transfer exists as a recent finding | M + A | 1965–1972 papers; discredited later |
| 1b | TBWTT-7:62 | Yahweh, 1973 | "sache ce que l'autre savait"; presented as established | B | record = a disputed "significant tendency" |
| 1c | TBWTT-7:62 | Yahweh, 1973 | "dans le cerveau" | ND | abstracts silent; i.p. and intraventricular both named in a negative report |
| 1d | LWTE-4:132 | Terrusse, 1979 | RNA memory substances transferable (future) | B + A | post-dates 1977–78 non-reproducibility reports |
| 2 | TBWTT-3:111 | Yahweh, 1973 | animals guided by electrodes | M (B for steering) | Delgado 1963–69; steering 2002 |
| 3a | TBWTT-2:14 | Yahweh, 1973 | continents fit into one — "viennent de" | M (acceptance) / L (idea) | Wegener 1912–15; Bullard 1965; acceptance 1965–68 |
| 3b | LWTE-1:30 | questioner, 1979 | drift of a few cm a year | M | 2.5 cm/yr |
| 3c | LWTE-1:30 | questioner, 1979 | "d'un mètre selon d'autres" | ND | no source found |
| 3d | LWTE-1:31 | Raël, 1979 | recent rift of >1 m near Arabia | M (probable) | Asal–Ghoubbet, Nov 1978, ~2 m; "one night" unconfirmed |
| 4a | LWTE-4:129 | Terrusse, 1979 | genes synthesised; DNA into bacteria | M | 1970, 1972–73, 1977, 1979 |
| 4b | LWTE-1:152 | Raël, 1979 | synthetic genetic codes "bientôt" | L (weak sense) / B, realised 2010–16 (strong sense) | |
| 4c | LWTE-4:131 | Terrusse, 1979 | new animal species; humanoids | B | forecast |
| 5 | TBWTT-2:2, 2:16 | Yahweh, 1973 | living cells from chemicals "bientôt" | B | not done in strict sense per S53 |
| 6a | TBWTT-2:58 | Yahweh, 1973 | one cell holds the whole being — "bientôt le comprendre" | L (principle) / B, realised 1996–97 (adult mammal) | |
| 6b | TBWTT-7:30, 2:58 | Yahweh, 1973 | any cell suffices | B | all methods need an egg |
| 6c | TBWTT-3:283 | Yahweh, 1973 | extinct species recreated | B, partially realised 2003 | bucardo |
| 7a | LWTE-1:26 | questioner, 1979 | nearest star ≈ 4 ly | M | 4.25 ly |
| 7b | TBWTT-5:52–53 | Yahweh, 1973 | home star < 1 ly | X | parallaxes since 1839/1915; WISE 2014 |
| 7c | LWTE-1:27, 4:121 | Raël; Terrusse, 1979 | light speed varies; distances overestimated | B | no support retrieved |
| 7d | TBWTT-5:52 | Yahweh, 1973 | rockets at 40,000 km/h | M | Apollo 10 |
| 8a | TBWTT-5:52 | Yahweh, 1973 | parasang, parsec are units | M | |
| 8b | TBWTT-5:52 | Yahweh, 1973 | parasang = one light-second | X (vs historical unit) | 5.3–5.7 km |
| 9a | LWTE-1:28 | Raël, 1979 | "Evolution ou Création" exists | M (probable ID) | Flori & Rasolofomasoandro 1974 |
| 9b | LWTE-1:28 | Raël, 1979 | dating wrong because atomic behaviour varied | X | decay constancy as stated in S92 |
| 9c | LWTE-1:28 | Raël, 1979 | the book "développe tout cela" | ND | book not opened |
| 10a | LWTE-1:45–46 | Raël, 1979 | wood found, analysed, too young | M | |
| 10b | LWTE-1:46 | Raël, 1979 | "sept cents ans" / "l'an mille deux cents" | no match found | published ≈ 1,200–1,700 yr; ≈ A.D. 260–790 |
| 11 | LWTE-4:73 | Terrusse, 1979 | Hertz in the 1920s | no match (slip) | 1886–89 |
| 12 | LWTE-4:73; 4:10 | Terrusse, 1979 | NMR 1946; Muller Nobel 1946 | M | |
| 13 | LWTE-2:102 | Yahweh, 1979 | telecom satellites | M | 1962 |
| 14 | LWTE-2:102 | Yahweh, 1979 | prostheses that make the blind see | M (experiments) / B (function) | 1968, 1974 |
| 15 | LWTE-2:102 | Yahweh, 1979 | synthetic beings in the laboratory | B | |
| 16 | LWTE-1:169 | Raël, 1979 | self-recharging mobile computer "viennent de" | L (feature) / ND (machine) | Hopkins Beast, 1960s |
| 17 | ETTMTTP-2:37 | Yahweh, 1975 | one person + computer builds a car "déjà" | B (weakly sourced) | |
| 18 | ETTMTTP-2:30 | Yahweh, 1975 | weight lost at death "on a pu constater" | M + A | MacDougall 1907 |

Counts over the 35 rows (a row can carry more than one label where its wording has separable parts): M 15 (two marked probable); B 13; L 4; A 3; X 3; ND 4; no match found 2.

## Tensions and null results

- **Pattern by voice (analysis).** The past-tense reports of terrestrial science that check out best are Terrusse's (gene synthesis, NMR, Muller) — and the one flat error is also his (Hertz). Yahweh's 1973 "viennent de" statements each have a real published referent (memory transfer 1965–72, brain electrodes 1963–69, continental fit 1965–68), reported at the confidence of the popular account and, for memory transfer, without the dispute that was already in the same journals. Raël's 1979 commentary contains the two numerical items that could not be matched (700-year wood; "un mètre" of drift) and the item that contradicts the record (non-constant atomic behaviour).
- **The one Elohim technology explicitly anchored to a terrestrial experiment is anchored to the one later discredited.** TBWTT-7:61–62 derives schooling-by-injection from the rat result. The record's later verdict is negative (S12, S13, S15, S16), with a narrow 2018 exception in a mollusc (S17).
- **Lag items.** Four statements present as new or forthcoming what was already published: continental drift as an idea (1912), nuclear totipotency (1952–62), self-recharging machines (1960s), and in the weak sense synthetic genes (1970). In each case the *popular* salience was recent; the sources retrieved do not date French popularisation, so "lags the literature" is established, "lags French public knowledge" is not.
- **Favourable items not to be lost:** the Afar rifting report (LWTE-1:31) is confirmed in magnitude by a 1979 geophysics paper; Terrusse's molecular-biology sentence is accurate to the year; the 40,000 km/h rocket figure matches the Apollo record; "environ quatre années-lumière" is right; the Song of Songs 5 pointer agrees with the standard description of the Shi'ur Qomah.
- **Awkward items not to be lost:** the home-star distance against parallax and infrared survey; the parasang value against the historical unit; the Ararat figure; the dating premise and the probable creationist identity of the recommended book; the Hertz date; memory transfer.
- **Null results (searched, not found).** Any report dating Ararat wood to 700 years or to c. A.D. 1200 (queries: Navarra Ararat wood radiocarbon dates laboratories; "Bordeaux" OR "Madrid" OR "Cairo" lignite versus carbon-14; Wikipedia fr/en). Any French press coverage of scotophobin c. 1972–73 (query: "scotophobine" Ungar "Le Monde" OR "Science et Vie" — nothing French returned). A national-library record for the book (BnF SRU endpoint and SUDOC unreachable; WorldCat result list did not render; archive.org title search: 0 hits). The LWTE bibliography itself. A source for drift "d'un mètre" per year. The date and wording of the *New York Times* front-page article on Delgado (secondary sources disagree between 1963 and 1965; not opened). The identity of the c. 1979 self-recharging robot. A positive memory-transfer paper stating intracerebral injection in rats.

## Relation to existing core records

- `woh-claim-0074` (canon-biochemical-layer) and `scientific-immortality`: finding 1 supplies the dated literature behind TBWTT-7:62 and its later standing; finding 9 the cloning record. Neither record currently carries these dates.
- `woh-claim-0071` (continental breakup at the Flood): finding 6 adds the dated acceptance history and identifies a probable referent (Asal–Ghoubbet 1978; Ruegg et al. 1979) for LWTE-1:31, which the evidence map lists only as "a one-night metre-scale rift near Arabia". Finding 5 gives the probable identity of *Évolution ou Création*, which the evidence map cites by title only.
- `woh-claim-0021` (Kabbalah / Shi'ur Qomah anchor): finding 3 gives a sourced value for the historical parasang, bearing on the "units retrofit" alternative already recorded there. No new claim about the Shi'ur Qomah figures is made.
- `life-engineering-convergence`: findings 7–9 give the milestone dates (1970, 1973, 1977, 1979, 1997, 2010, 2016) with abstracts, and mark which canon wordings precede, match or trail them.
- `design-signature-natural-designers`: unaffected, except that the same Terrusse essay whose molecular-biology report is accurate also contains the Hertz slip.

## Candidate claims or revisions for founder review (proposals, not decisions)

1. A `source_report` record: "TBWTT-7:62 refers to the memory-transfer literature of 1965–1972" with the dated table of finding 1, an explicit `later_standing: abandoned` note, and the 2018 Aplysia paper as a recorded alternative reading. Revision trigger: any replication of content-specific transfer in a vertebrate.
2. A note on `woh-claim-0071`'s evidence map: probable referent of LWTE-1:31 (Asal–Ghoubbet, November 1978; inference, not stated in the text) and probable identity of *Évolution ou Création* (Flori & Rasolofomasoandro, 1974), both marked unconfirmed pending the LWTE bibliography.
3. A wantlist item: the printed bibliography of *Accueillir les extra-terrestres* (1979 edition) and a copy of Flori & Rasolofomasoandro 1974, chapter on dating — to settle finding 5.
4. A wantlist item: Taylor & Berger, *Antiquity* 54 (1980) 34–36, and any French press report of 1975–79 on the Ararat wood — to settle whether "sept cents ans" has a printed source.
5. A `source_report` record: "the canon's distance figure against the published stellar-distance record", holding LWTE-1:26's own objection, the three in-canon replies (`science.md` finding 5) and the 2014 survey limit.
6. A research question: when each "viennent de" topic reached French popular science (Science et Vie, Le Monde, Planète, 1965–73). This would turn "lags the literature" into a statement about what a French reader of 1973 would have met.
7. An editorial check on any public page that cites memory transfer, the parasang value, or the Ararat date as corroboration.

## Limitations

- Many dates and state-of-field statements rest on Wikipedia (tertiary), because publisher sites and catalogues were unreachable. PubMed records give titles, dates and abstracts, not full texts; where a record has no abstract (S03, S05–S09) only the title is evidence.
- [fetch] quotations are fragments returned by a summarising tool and were not re-read against the raw page.
- I did not open: Bullard, Everett & Smith 1965; Ungar 1972 or Stewart 1972 full texts; Setlow 1997 full text; Collins & Pinch, *The Golem*; Irwin 2007; Bailey 1989; Taylor & Berger 1980; Luhman 2014 (only a magazine report of it); Flori & Rasolofomasoandro 1974; Bivar 1985.
- The book identification, the Asal identification and the "roles exchanged" reading of the Ararat numbers are my inferences and are labelled as such.
- "Then-current published state" is the research literature, not French public awareness; the canon's "viennent de" may track the latter.
- Classification labels compress wordings with several parts; the per-finding text governs.
- Arithmetic is mine. Nothing here evaluates whether the canon's statements are true of the Elohim; only whether its statements about *terrestrial* science match the dated record.

## Sources (all accessed 2026-11-12)

PubMed records were retrieved as plain text through NCBI E-utilities (`eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<PMID>&rettype=abstract`); the canonical page is given. Wikipedia pages were retrieved as plain-text extracts through the MediaWiki API unless marked [fetch].

| ID | Kind | Title / record | URL |
|---|---|---|---|
| S01 | PubMed record [direct] | Babich et al., Science 1965 Aug 6;149(3684):656-7 | https://pubmed.ncbi.nlm.nih.gov/14331194/ |
| S02 | PubMed [direct] | Jacobson et al., Science 1965 Oct 29;150(3696):636-7 | https://pubmed.ncbi.nlm.nih.gov/5837108/ |
| S03 | PubMed [direct], title only | Gross & Carey, Science 1965 Dec 24;150(3704):1749 | https://pubmed.ncbi.nlm.nih.gov/5858035/ |
| S04 | PubMed [direct] | Luttges et al., Science 1966 Feb 18;151(3712):834-7 | https://pubmed.ncbi.nlm.nih.gov/17746734/ |
| S05 | PubMed [direct], title only | Byrne et al., "Memory transfer", Science 1966 Aug 5;153(3736):658-9 | https://pubmed.ncbi.nlm.nih.gov/5939939/ |
| S06 | PubMed [direct], title only | Ungar, Galvan, Clark, Nature 1968 Mar 30;217(5135):1259-61 | https://pubmed.ncbi.nlm.nih.gov/5643106/ |
| S07 | PubMed [direct], title only | Ungar, Desiderio, Parr, Nature 1972 Jul 28;238(5361):198-202 | https://pubmed.ncbi.nlm.nih.gov/4558348/ |
| S08 | PubMed [direct], title only | Stewart, Nature 1972 Jul 28;238(5361):202-10 | https://pubmed.ncbi.nlm.nih.gov/4558349/ |
| S09 | PubMed [direct], title only | Goldstein et al., Nature 1971 Sep 10;233(5315):126-9 | https://pubmed.ncbi.nlm.nih.gov/12058754/ |
| S10 | PubMed [direct] | Malin & Guttman, Science 1972 Dec 15;178(4066):1219-20 | https://pubmed.ncbi.nlm.nih.gov/4637811/ |
| S11 | PubMed [direct] | Frank, Stein, Rosen, Science 1970 Jul 24;169(3943):399-402 | https://pubmed.ncbi.nlm.nih.gov/5465368/ |
| S12 | PubMed [direct] | Misslin et al., Behav Processes 1978 May;3(1):45-56 | https://pubmed.ncbi.nlm.nih.gov/24924376/ |
| S13 | PubMed [direct] | Wójcik & Niemierko, Acta Neurobiol Exp 1978;38(1):25-30 | https://pubmed.ncbi.nlm.nih.gov/566023/ |
| S14 | PubMed [direct] (review abstract) | Setlow, "Georges Ungar and memory transfer", J Hist Neurosci 1997 Aug;6(2):181-92 | https://pubmed.ncbi.nlm.nih.gov/11619520/ |
| S15 | Magazine [fetch] | A. Abell, "50 years ago, scientists were on the trail of 'memory molecules'", Science News, 5 Nov 2021 | https://www.sciencenews.org/article/50-years-ago-scientists-memory-molecules-storage |
| S16 | Wikipedia [direct] | "Scotophobin" | https://en.wikipedia.org/wiki/Scotophobin |
| S17 | PubMed [direct] | Bédécarrats et al., eNeuro 2018 May 21;5(3) | https://pubmed.ncbi.nlm.nih.gov/29789810/ |
| S20 | Wikipedia [direct] | "José Manuel Rodríguez Delgado" | https://en.wikipedia.org/wiki/Jos%C3%A9_Manuel_Rodr%C3%ADguez_Delgado |
| S21 | Magazine [fetch] | J. El-Hai, "The Man Who Fought a Bull With Mind Control", Discover, 21 Mar 2016 | https://www.discovermagazine.com/the-man-who-fought-a-bull-with-mind-control-803 |
| S22 | PubMed [direct], title only | Delgado, "Radio-controlled behavior", N Y State J Med 1969 Feb 1;69(3):413-7 | https://pubmed.ncbi.nlm.nih.gov/4976614/ |
| S23 | PubMed [direct] | Talwar et al., Nature 2002 May 2;417(6884):37-8 | https://pubmed.ncbi.nlm.nih.gov/11986657/ |
| S30 | Wikipedia [direct] | "Pangaea" | https://en.wikipedia.org/wiki/Pangaea |
| S31 | Wikipedia [direct] | "Plate tectonics" | https://en.wikipedia.org/wiki/Plate_tectonics |
| S32 | Wikipedia [direct] | "Edward Bullard" | https://en.wikipedia.org/wiki/Edward_Bullard |
| S33 | Wikipedia [fetch] | "Continental drift" | https://en.wikipedia.org/wiki/Continental_drift |
| S34 | Wikipedia fr [direct] | "Tectonique des plaques" | https://fr.wikipedia.org/wiki/Tectonique_des_plaques |
| S35 | Wikipedia [direct] | "Mid-Atlantic Ridge" | https://en.wikipedia.org/wiki/Mid-Atlantic_Ridge |
| S36 | Reference database, abstract [fetch] | Ruegg, Kasser, Lépine, Tarantola (1979), Geophys. Res. Lett. 6, doi 10.1029/GL006i011p00817 | http://earthref.org/ERR/7882/ |
| S37 | Wikipedia [direct] | "Ardoukoba" | https://en.wikipedia.org/wiki/Ardoukoba |
| S40 | PubMed [direct], title only | Agarwal et al., Nature 1970 Jul 4;227(5253):27-34 | https://pubmed.ncbi.nlm.nih.gov/5422620/ |
| S41 | PubMed [direct] | Jackson, Symons, Berg, PNAS 1972 Oct;69(10):2904-9 | https://pubmed.ncbi.nlm.nih.gov/4342968/ |
| S42 | PubMed [direct] | Cohen, Chang, Boyer, Helling, PNAS 1973 Nov;70(11):3240-4 | https://pubmed.ncbi.nlm.nih.gov/4594039/ |
| S43 | PubMed [direct] | Itakura et al., Science 1977 Dec 9;198(4321):1056-63 | https://pubmed.ncbi.nlm.nih.gov/412251/ |
| S44 | PubMed [direct] | Khorana, Science 1979 Feb 16;203(4381):614-25 | https://pubmed.ncbi.nlm.nih.gov/366749/ |
| S45 | PubMed [direct] | Ryan et al., J Biol Chem 1979 Jul 10;254(13):5817-26 | https://pubmed.ncbi.nlm.nih.gov/376520/ |
| S46 | Wikipedia [direct] | "Artificial gene synthesis" | https://en.wikipedia.org/wiki/Artificial_gene_synthesis |
| S50 | PubMed [direct], title only | Goulian, Kornberg, Sinsheimer, PNAS 1967 Dec;58(6):2321-8 | https://pubmed.ncbi.nlm.nih.gov/4873588/ |
| S51 | PubMed [direct] | Gibson et al., Science 2010 Jul 2;329(5987):52-6 | https://pubmed.ncbi.nlm.nih.gov/20488990/ |
| S52 | PubMed [direct] | Hutchison et al., Science 2016 Mar 25;351(6280):aad6253 | https://pubmed.ncbi.nlm.nih.gov/27013737/ |
| S53 | Wikipedia [direct] | "Artificial cell" | https://en.wikipedia.org/wiki/Artificial_cell |
| S60 | PubMed [direct], title only | Briggs & King, PNAS 1952 May;38(5):455-63 | https://pubmed.ncbi.nlm.nih.gov/16589125/ |
| S61 | PubMed [direct], title only | Gurdon, J Embryol Exp Morphol 1962 Dec;10:622-40 | https://pubmed.ncbi.nlm.nih.gov/13951335/ |
| S62 | PubMed [direct] | Gurdon, Laskey, Reeves, J Embryol Exp Morphol 1975 Aug;34(1):93-112 | https://pubmed.ncbi.nlm.nih.gov/1102625/ |
| S63 | PubMed [direct] | McGrath & Solter, Science 1984 Dec 14;226(4680):1317-9 | https://pubmed.ncbi.nlm.nih.gov/6542249/ |
| S64 | PubMed [direct] | Willadsen, Nature 1986 Mar 6-12;320(6057):63-5 | https://pubmed.ncbi.nlm.nih.gov/3951549/ |
| S65 | PubMed [direct] | Wilmut et al., Nature 1997 Feb 27;385(6619):810-3 | https://pubmed.ncbi.nlm.nih.gov/9039911/ |
| S66 | PubMed [direct] | Folch et al., Theriogenology 2009 Apr 1;71(6):1026-34 | https://pubmed.ncbi.nlm.nih.gov/19167744/ |
| S67 | Wikipedia [direct] | "Frederick Campion Steward" | https://en.wikipedia.org/wiki/Frederick_Campion_Steward |
| S70 | Wikipedia [direct] | "Proxima Centauri" | https://en.wikipedia.org/wiki/Proxima_Centauri |
| S71 | Wikipedia [direct] | "Alpha Centauri" | https://en.wikipedia.org/wiki/Alpha_Centauri |
| S72 | Magazine [fetch] | "WISE survey finds thousands of new stars, but no 'planet X'", Astronomy, 13 Mar 2014 | https://www.astronomy.com/science/wise-survey-finds-thousands-of-new-stars-but-no-planet-x/ |
| S73 | Wikipedia [direct] | "Nemesis (hypothetical star)" | https://en.wikipedia.org/wiki/Nemesis_(hypothetical_star) |
| S74 | Wikipedia [direct] | "Light-year" | https://en.wikipedia.org/wiki/Light-year |
| S75 | Wikipedia [direct] | "Speed of light" | https://en.wikipedia.org/wiki/Speed_of_light |
| S76 | Wikipedia [direct] | "Apollo 10" | https://en.wikipedia.org/wiki/Apollo_10 |
| S80 | Wikipedia [fetch] | "Parasang" | https://en.wikipedia.org/wiki/Parasang |
| S81 | Wikipedia [direct] | "Parsec" | https://en.wikipedia.org/wiki/Parsec |
| S82 | Wikipedia [fetch] | "Shi'ur Qomah" | https://en.wikipedia.org/wiki/Shi%27ur_Qomah |
| S90 | Bibliographic feed [fetch] | Google Books volumes feed, queries intitle:"Evolution ou création" (+ inauthor:Flori) | https://www.google.com/books/feeds/volumes?q=intitle:%22Evolution+ou+cr%C3%A9ation%22+inauthor:Flori |
| S91 | Critical dossier, PDF [direct] | Nitschelm, Geney, Plateaux, Roux, "Le créationnisme est-il scientifiquement recevable ?" (1987–88) | https://www.lecerveau.ca/flash/capsules/articles_pdf/creationnisme.pdf |
| S92 | Wikipedia [direct] | "Radiometric dating" | https://en.wikipedia.org/wiki/Radiometric_dating |
| S100 | Periodical abstract page [fetch] (secondary) | "From USA: Ararat 'Ark' Wood Dated At A.D. 700", Bible and Spade 6:3 (Summer 1977) 95–96 | https://www.galaxie.com/article/bsp06-3-04 |
| S101 | Critical web archive [fetch] (secondary) | TalkOrigins Index to Creationist Claims, CH504.2 | https://talkorigins.org/indexcc/CH/CH504_2.html |
| S102 | Wikipedia [direct] | "Searches for Noah's Ark" | https://en.wikipedia.org/wiki/Searches_for_Noah%27s_Ark |
| S103 | Magazine [fetch] | "Wood on Mount Ararat Intrigues Explorers", Christianity Today, 12 Sep 1969 | https://www.christianitytoday.com/1969/09/wood-on-mount-ararat-intrigues-explorers/ |
| S104 | Journal landing page [fetch], citation only | Taylor & Berger, "The date of 'Noah's Ark'", Antiquity 54(210):34–36 (1980) | https://www.cambridge.org/core/journals/antiquity/article/date-of-noahs-ark/2D0BA47C12949A055DD314EE975A02DD |
| S105 | Wikipedia fr [fetch] | "Fernand Navarra" | https://fr.wikipedia.org/wiki/Fernand_Navarra |
| S110 | Wikipedia [direct] | "Heinrich Hertz" | https://en.wikipedia.org/wiki/Heinrich_Hertz |
| S111 | Wikipedia [direct] | "Nuclear magnetic resonance" | https://en.wikipedia.org/wiki/Nuclear_magnetic_resonance |
| S112 | Wikipedia [direct] | "Hermann Joseph Muller" | https://en.wikipedia.org/wiki/Hermann_Joseph_Muller |
| S113 | Wikipedia [direct] | "Telstar" | https://en.wikipedia.org/wiki/Telstar |
| S114 | PubMed [direct] | Brindley & Lewin, J Physiol 1968 May;196(2):479-93; Dobelle, Mladejovsky, Girvin, Science 1974 Feb 1;183(4123):440-4 | https://pubmed.ncbi.nlm.nih.gov/4871047/ ; https://pubmed.ncbi.nlm.nih.gov/4808973/ |
| S115 | Wikipedia [direct] | "Johns Hopkins Beast" | https://en.wikipedia.org/wiki/Johns_Hopkins_Beast |
| S116 | Wikipedia [direct] | "Unimate"; "Lights out (manufacturing)" | https://en.wikipedia.org/wiki/Unimate ; https://en.wikipedia.org/wiki/Lights_out_(manufacturing) |
| S117 | Wikipedia [direct] | "21 grams experiment" | https://en.wikipedia.org/wiki/21_grams_experiment |
