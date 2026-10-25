---
title: "ADR 0012: Promotion of woh-claim-0073 (The dragons passage as compositional signature)"
status: accepted
date: 2026-10-25
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0003-artifact-derivation-contract.md
---

# ADR 0012: Promotion of woh-claim-0073 (The dragons passage as compositional signature)

## Context

The Explainer *The Dragon Curve* reads the first Message's dragons
passage (TBWTT 2:22) against Genesis 1:21, the verse the Message never
quotes, and against the canon's own quotation source, Dhorme's Pléiade
Bible, whose rendering of that verse is « Élohim créa donc les grands
dragons ». Its load-bearing record, `woh-claim-0073`, was drafted at 0.1.0
on 2026-10-24 under the RFC 0003 contract, together with its controlling
specification, evidence map and a new source note for `dhorme-bible`
(the Pléiade Genesis 1–3 inspected at excerpt grade).

An independent review the same day changed the record before anything
was published against it, so 0.1.0 was amended in place:

- **Quotation pattern.** From the fourth day onward the exegesis quotes
  only the stage-opening commands (Genesis 1:14, 1:20, 1:24, 1:26) and
  narrates every fulfillment, so the Genesis 1:21 gap is predicted. The
  record now rests the signature reading on that discipline's uniformity
  at the point of maximal incentive, never on the bare omission, and the
  omission alternative carries the pattern in full.
- **Dhorme variances.** TBWTT 2:23 matches Dhorme's 1:24 exactly; 2:19
  and 2:26 carry his 1:20 and 1:26 with one-word variances (*les* for
  *des* volatiles; *Qu'il ait* for *Qu'ils aient*). The record and source
  note no longer claim verbatim copying at those verses.
- **Sendy counter-evidence.** *Ces dieux* carries « l'hippopotame
  successeur du diplodocus raté » (inventory I014, coded *similar*). The
  absence claim is confined to the complex — dragons by name, dissenting
  teams, bird-stage placement — and the counter-evidence is carried.

## Decision drivers

- A published page should not stay bound to a draft record.
- The record states a speculative synthesis and labels it so; the
  deflationary chain (Dhorme supplies the register, popular usage the
  dinosaur gloss, verse order the placement, the quotation pattern the
  gap) stands as a full-strength alternative in record and article alike.
- The founder read the controlling specification and the record and
  approved them as amended.

## Decision

The founder directed promotion of `woh-claim-0073` at 0.1.0 from `draft`
to `accepted` on 2026-10-25.

Acceptance records the project's current specification of the reading.
It is not a finding about authorship, about the reported encounter, or
about the dependence question, which stays where `woh-claim-0072`
leaves it.

Unchanged by this decision: the public label (`speculative`), evidence
status (`scoped`, `contested`), alternatives, and revision triggers. The
evidence map keeps `draft` status as a living research artifact, per the
ADR 0005 convention.

## Consequences

### Enables

- The catalog again carries no draft records.
- *The Dragon Curve* can publish in all site languages bound to an
  accepted record.

### Costs and risks

- Every passage observation holds of the 2005 collected text in the
  project digitization; a first-printing collation is the operative
  revision trigger.
- The Dhorme identification at this passage rests on a partial publisher
  extract (Genesis 1–3); a full collation of the canon's quotation layer
  could qualify it.
- The wider 1960s ancient-astronaut literature remains unsurveyed for a
  dragons-at-the-bird-stage precedent, as for `woh-claim-0072`.

## Validation and review

The catalog validates after the flip, with the specification synced to
the lifecycle and the article's binding at 0.1.0. Review this ADR when
first printings are collated, when the quotation layer is collated, or
when a pre-1974 precedent for the passage is found.

## References

- [Controlling specification](../docs/framework/dragons-passage-signature.md)
- [Evidence map](../docs/evidence/woh-claim-0073-evidence.md)
- [Dhorme source note](../source-notes/dhorme-bible.md)
- [ADR 0011](0011-sendy-comparison-promotion.md) (promotion precedent)
