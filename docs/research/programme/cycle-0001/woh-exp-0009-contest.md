# Contest: woh-exp-0009

- Date: 2026-11-22
- Assessment contested: `meets_hit` (declared control; `discrimination: none`, `novelty: retrodiction`)
- Recommendation: sustain

## Verification

I retrieved the PubMed record for PMID 20488990 through NCBI E-utilities `efetch` (abstract, text mode) on 2026-11-22.

- Bibliographic data agree with the finding: *Science* 2010 Jul 2; 329(5987): 52-6; DOI 10.1126/science.1190719; first author Gibson DG, last author Venter JC.
- The abstract as quoted in the finding is identical to the PubMed text, word for word, in all three sentences. The three excerpts marked (a), (b) and (c) are exact sub-strings of it.
- The title is as quoted.
- The two "Comment in" items the finding lists are in the record with the DOIs given.

No discrepancy was found.
I did not reach the full text. Like the Locator, I have inspected nothing beyond the abstract, so no statement about Methods, Results or Discussion is verified by either of us.

One point of wording: the phrase "chemically synthesized" is in the title only. The abstract says "design, synthesis, and assembly ... starting from digitized genome sequence information".
The protocol value `chemically_synthesized` therefore rests on title and abstract together. That is a fair reading, but the abstract alone does not say how much of the building was chemical and how much was done by living cells; the `prior_knowledge` field mentions assembly in yeast, and the finding rightly leaves it unverified.

## The strongest objection

The hit criteria leave out the one answer that limits the result.
The protocol asked three things: genome, recipient cell, replication. The hit criterion uses only the first and third.
The second, which the Locator answered `pre_existing_cell`, is what determines the meaning of the paper, and it has no effect on the assessment.

Stated as a sceptical biologist would put it, the paper reports the following:

- A genome was synthesized whose sequence is a near-copy of an existing organism's. The abstract describes the "design" as "watermark" sequences and "designed gene deletions and polymorphisms" on a sequence taken from "digitized genome sequence information", which is the sequence of natural *M. mycoides*. It is an edited transcription, not a genome composed from an understanding of how to build an organism.
- The genome was placed in a living cell of a related species. The membrane, cytoplasm, ribosomes and the whole translation apparatus that first read the synthetic DNA were made by a natural cell. "The only DNA in the cells is the designed synthetic DNA sequence" is a statement about DNA and nothing else.
- "Continuous self-replication" is not quantified at the access level achieved.

The derivation calls the result a "necessary condition": "building a working genome to a design must be physically possible".
What the abstract supports is narrower: copying a natural genome with edits, and starting it in a natural cell, is possible.
It does not show that a genome can be designed from first principles, or that a cell can be built without a pre-existing cell. Those are what the design subclaim of `woh-claim-0001` would require of its designers.

On the registered criteria the hit stands regardless.
The gap is between the criteria and any larger use of the paper, and the record already guards against that use: `discrimination: none`, and an evidence-map role of "possibility in principle and nothing more".

**Would an alternative predict otherwise?** No. The naturalistic alternative expects synthetic genomics to work, since it holds that genomes are chemistry. The source-critical alternative is untouched. The record states both correctly.

**Independence.** None. The source is already cited for this claim, and the Deriver knew the answer and said so.

**Does the control calibrate anything?** Only a little.
It checks that the Locator reports what a source says and marks limits: the Locator did, flagging that the exhaustiveness claim is restricted to DNA and that nothing beyond the abstract was read.
It does not calibrate the programme's ability to register a miss, because no result other than a hit was possible.
A control that could fail would say more about the scoreboard than one that could not.

## What the result does and does not show

Shows, at abstract level and verified against PubMed:

- A 1.08-Mbp genome was designed from digitized sequence information, synthesized, assembled, and transplanted into a *M. capricolum* recipient cell.
- The resulting cells are reported as controlled only by the synthetic chromosome and "capable of continuous self-replication".
- The synthetic sequence differs from its design by "mutations acquired during the building process".

Does not show:

- That a cell was synthesized. The recipient was a living cell.
- That a genome was designed de novo. The sequence derives from a natural genome.
- Anything about the origin of terrestrial life, the existence of designers, or the feasibility of what the canon reports.
- Anything from Methods, Results or Discussion, including how the authors themselves limit the result. These were not inspected.

A hit here adds nothing to the count that measures progress. The methodology places it in the non-discriminating, retrodiction class, and it belongs there.

## What the ruling turns on

1. **Whether abstract-level access suffices.** The registered `access_expected` was `abstract` and both criteria terms are answerable from the abstract, so the assessment is well founded on what was registered. A ruling of `hit` should carry the access level with it.
2. **Whether the hit is kept in its declared class.** There is no weaker class to move it to; `none` and `retrodiction` are already the floor. The risk lies downstream: any output that cites this ruling must say "a synthetic genome in a pre-existing cell", not "a synthetic cell", and must not cite the paper beyond its abstract until the full text is in hand.
3. **Whether the evidence-map phrase "possibility in principle" needs narrowing.** The abstract supports the possibility of genome synthesis and transplantation. Whether that is the possibility subclaim D needs is a question for a review of the evidence map, not for this ruling.
