# Finding: woh-exp-0009

- Date: 2026-11-22
- Source and edition inspected: D. G. Gibson et al., 'Creation of a bacterial
  cell controlled by a chemically synthesized genome', *Science* 329:5987
  (2 July 2010), pp. 52-56, DOI 10.1126/science.1190719, PMID 20488990. Text
  inspected: the published **abstract** as held in the NLM/PubMed record,
  retrieved through the NCBI E-utilities `efetch` endpoint
  (`db=pubmed&id=20488990&rettype=abstract&retmode=text`), saved locally as
  `.../scratchpad/dl-0009/pubmed.txt`. Abstract content independently
  corroborated against the Europe PMC `search` REST record for `EXT_ID:20488990`
  and against the Edge.org repost of the paper's front matter
  (`https://www.edge.org/print/node/21381`). The full text was **not** inspected.
- Access achieved: `abstract`
- Search performed:
  - NCBI E-utilities `efetch` for PMID 20488990 (abstract, text mode) — succeeded,
    full abstract retrieved.
  - NCBI `elink` pubmed→pmc for PMID 20488990 — returned only `pubmed_pmc_refs`
    (papers citing it); **no** PMC copy of the article itself.
  - Publisher page `https://www.science.org/doi/10.1126/science.1190719` — HTTP 403
    from this environment (both via direct request and via the fetch tool).
  - `https://europepmc.org/article/MED/20488990` — HTTP 403.
  - Europe PMC REST `search?query=EXT_ID:20488990&resultType=core` — succeeded:
    `isOpenAccess: N`, `inEPMC: N`; listed full-text URLs are
    `http://www.sciencemag.org/cgi/content/abstract/329/5987/52` (free, abstract
    only) and `http://www.sciencemag.org/cgi/content/full/329/5987/52`
    (subscription required).
  - Semantic Scholar Graph API `DOI:10.1126/science.1190719` — `isOpenAccess:
    false`, `openAccessPdf.status: "CLOSED"`, empty URL.
  - Web search for a free full text located one third-party course copy of the
    PDF (University of Ferrara teaching page) and an Edge.org repost; the Ferrara
    PDF could not be parsed by the fetch tool (repeated "Duplicate Content-Length"
    errors) and the Edge.org page reproduces only title, authors, affiliations and
    abstract, not the body.
  - An attempt to reach an archived sciencemag.org full-text page was blocked by
    this environment's permission layer, so no archived full text was inspected.
  - Also read, as clearly-labelled secondary material from the authors'
    institution: `https://www.jcvi.org/first-self-replicating-synthetic-bacterial-cell`.
  - Scope note: the brief's scope was "Abstract; methods and results as far as
    accessible". The abstract was reached in full; the Methods and Results
    sections were **not** accessible (paywalled, not in PMC, no open-access copy
    listed by Unpaywall-class indexes). Step 1's "full text if you can reach it"
    could not be completed, and consequently the parts of step 2 that would be
    answered from Methods/Results are answered from the abstract only.

## Answer

In the vocabulary of the protocol, and on the evidence of the abstract alone:

- Genome: `chemically_synthesized`. The abstract reports the "design, synthesis,
  and assembly" of the 1.08-Mbp *Mycoplasma mycoides* JCVI-syn1.0 genome
  "starting from digitized genome sequence information", and states that "[t]he
  only DNA in the cells is the designed synthetic DNA sequence".
- Recipient cell (cytoplasm, membrane): `pre_existing_cell`. The abstract reports
  "transplantation into a *M. capricolum* recipient cell" — i.e. the synthetic
  chromosome was placed into an existing cell of a different *Mycoplasma*
  species. The abstract does not itemise the recipient's cytoplasm, membrane,
  ribosomes or proteins; it says only that the recipient was a cell and that the
  only *DNA* in the resulting cells is synthetic (see "Absent or ambiguous").
- Replication: `continuous_self_replication_reported`. The abstract states that
  the new cells "are capable of continuous self-replication".

## Quotations

All three quotations are from the abstract of Gibson et al., *Science*
329:5987 (2010), p. 52, as held in the PubMed record for PMID 20488990
(NCBI `efetch`, retrieved 2026-11-22). The abstract is a single paragraph;
I give it whole, then mark the three protocol-relevant clauses.

Full abstract:

> "We report the design, synthesis, and assembly of the 1.08-mega-base pair
> Mycoplasma mycoides JCVI-syn1.0 genome starting from digitized genome sequence
> information and its transplantation into a M. capricolum recipient cell to
> create new M. mycoides cells that are controlled only by the synthetic
> chromosome. The only DNA in the cells is the designed synthetic DNA sequence,
> including "watermark" sequences and other designed gene deletions and
> polymorphisms, and mutations acquired during the building process. The new
> cells have expected phenotypic properties and are capable of continuous
> self-replication."

(a) How the genome was produced, and from what sequence information
(abstract, sentences 1 and 2):

> "We report the design, synthesis, and assembly of the 1.08-mega-base pair
> Mycoplasma mycoides JCVI-syn1.0 genome starting from digitized genome sequence
> information…"

> "The only DNA in the cells is the designed synthetic DNA sequence, including
> "watermark" sequences and other designed gene deletions and polymorphisms, and
> mutations acquired during the building process."

(b) What the genome was placed into, and where that recipient came from
(abstract, sentence 1):

> "…and its transplantation into a M. capricolum recipient cell to create new
> M. mycoides cells that are controlled only by the synthetic chromosome."

(c) Replication of the resulting cells (abstract, final sentence):

> "The new cells have expected phenotypic properties and are capable of
> continuous self-replication."

Title, for the record (same locator, p. 52):

> "Creation of a bacterial cell controlled by a chemically synthesized genome"

## Absent or ambiguous

- **Methods and Results not inspected.** No part of the body of the paper was
  opened. Anything the Methods or Results say about oligonucleotide cassette
  synthesis, the yeast assembly stages, the transplantation procedure, the
  recipient strain's genotype, or growth/passage data is reported here as **not
  inspected**. The paper is closed access (Europe PMC `isOpenAccess: N`;
  Semantic Scholar `CLOSED`), is not in PMC, and the publisher page returned 403
  from this environment.
- **The abstract's claim of exhaustiveness is restricted to DNA.** "The only DNA
  in the cells is the designed synthetic DNA sequence" is a statement about DNA
  only. The abstract makes no statement at all about the provenance of the
  recipient cell's cytoplasm, membrane, lipids, ribosomes, RNA or proteins, and
  does not claim that any of these were synthesized. The protocol value
  `pre_existing_cell` therefore rests on the word "recipient cell" in sentence 1,
  not on an explicit itemisation in the inspected text.
- **"Continuous self-replication" is not quantified in the abstract.** No number
  of generations, passages, or culture duration appears in the abstract; whatever
  quantification exists would be in the Results, which were not inspected.
- **No author statement of limits appears in the inspected scope.** The abstract
  contains no sentence of the form "this is not the creation of life de novo" or
  similar. The brief's step 4 asks how the authors describe the limits of what
  was made; within the abstract they do not, beyond the two implicit limits of
  (i) "controlled only by the synthetic chromosome" (a claim about control, not
  about total construction) and (ii) the acknowledgement of "mutations acquired
  during the building process" — i.e. the synthetic sequence is not identical to
  the designed sequence. Any discussion-section framing of limits is **not
  inspected**.
- **Translation / edition issues:** none. The source is in English and the
  abstract text was identical, word for word, in the NLM record and in the
  Edge.org repost; the Europe PMC record's `abstractText` opened with the same
  wording (the fetch tool would only return the first clause verbatim, citing a
  quotation-length limit, and paraphrased the rest, so Europe PMC counts as
  partial corroboration only).

## Adjacent observations

- **Species asymmetry.** Donor design and resulting cells are *M. mycoides*; the
  recipient cell was a different species, *M. capricolum*. The abstract therefore
  describes a cross-species transplantation, with the resulting cells identified
  as "new M. mycoides cells".
- **The synthetic sequence is not a faithful copy of a natural genome, nor of its
  own design.** The abstract flags three classes of intentional divergence
  ("watermark" sequences, designed gene deletions, designed polymorphisms) and
  one class of unintentional divergence ("mutations acquired during the building
  process").
- **The word "Creation" is the authors' own, in the title**, and is attached in
  that title specifically to "a bacterial cell controlled by a chemically
  synthesized genome" — the qualifier "controlled by" is part of the claim as
  titled.
- **Authors' institutional framing (secondary, not the paper).** The J. Craig
  Venter Institute's own page for the work
  (`https://www.jcvi.org/first-self-replicating-synthetic-bacterial-cell`,
  retrieved 2026-11-22) describes the genome as "constructed from four bottles of
  chemicals that make up DNA", carries a figure caption "The assembly of a
  synthetic M. mycoides genome in yeast", calls the result "the first cell
  controlled completely by a synthetic genome", describes "this first construct —
  dubbed M. mycoides JCVI-syn1.0" as "a proof of concept", and notes that in 2008
  the team "were unable to activate that genome in a cell at that time". This
  page does not name the recipient species. It is cited here as institutional
  secondary material, clearly distinct from the paper's own text; the "yeast
  assembly" and "four bottles of chemicals" statements were **not** verified
  against the paper's Methods.
- **Reception material exists but was not inspected.** The NLM record lists two
  "Comment in" items — *Science* 329:5987 (2010), pp. 38-39, DOI
  10.1126/science.1193749, and *Bioengineered* 7:2 (2016), pp. 53-56, DOI
  10.1080/21655979.2016.1175847. Neither was opened. The second is likely to be
  openly available in PMC if a later locator pass wants published commentary on
  how much of the cell was synthetic.
- **Route for a future full-text pass.** The free routes tried here all failed.
  A full-text pass would need either institutional access to science.org, an
  interlibrary copy, or the paper's free supplementary materials on the publisher
  site (not reachable from this environment). The supplementary material, if
  reachable, is where the cassette-by-cassette synthesis and assembly detail sits.
