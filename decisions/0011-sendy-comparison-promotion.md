---
title: "ADR 0011: Promotion of woh-claim-0072 (Sendy and the Messages)"
status: accepted
date: 2026-10-14
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0003-artifact-derivation-contract.md
---

# ADR 0011: Promotion of woh-claim-0072 (Sendy and the Messages)

## Context

The Explainer *Sendy and the Raëlian Messages* compares Jean Sendy's
pre-1974 books with the first Raëlian Message. Its bound record,
`woh-claim-0072`, was drafted at 0.1.0 on 2026-10-14 under the RFC 0003
contract. The same day an independent source review found that 0.1.0
understated several Genesis parallels: the laboratory analogy for life's
record, the ecological order of restoration, hybrid offspring and « le
peuple élu », the deliberate Flood, Iahvé as the Elohim's president, and
an arrival or decision some 22,000 years ago. A full inventory of the
Message's commentary (226 items, `docs/research/sendy-inventory/`) was then
classified against the five pre-1974 Sendy books. It found the Genesis
chapter almost entirely precedented and the commentary on Israel, the
prophets and Jesus largely absent (105 of 147 items). The record was revised
to 0.2.0 to state both results, and the article was rebound at
`0072@0.2.0`.

## Decision drivers

- A published page should not stay bound to a draft record.
- The revision changes the record's statement materially in both
  directions: stronger Genesis resemblance and a narrower scope for any
  Sendy-blueprint account.
- The founder considered having the article conclude that the Message
  arose independently, and chose instead a narrower statement the evidence
  supports: absence from Sendy's books limits a blueprint account but does
  not establish independent composition, and no 1960s control corpus was
  surveyed. The canon's own account of the commentary's origin is reported
  in framework voice and labelled as such.

## Decision

The founder directed promotion of `woh-claim-0072` at 0.2.0 from `draft`
to `accepted` on 2026-10-14.

Acceptance records the project's current specification of the comparison.
It is not a finding about authorship or about the reported encounter.

Unchanged by this decision: the public label (`inferred`), evidence status
(`scoped`, `contested`), alternatives, and revision triggers. The evidence
map keeps `draft` status as a living research artifact, per the ADR 0005
convention. The published companion article (`woh-claim-0042`) states that
Vorilhon had read Sendy's books; the founder chose to leave that wording,
and the new article names the difference openly.

## Consequences

### Enables

- The catalog again carries no draft records.
- The article can publish in all site languages bound to an accepted
  record.

### Costs and risks

- The inventory is agent-coded and conservative; recoding thematic
  parallels would raise the match counts.
- *Les dieux nous sont nés* (1966) and the wider 1960s literature
  (Misraki, Charroux, von Däniken, Blumrich) remain unsurveyed; each is a
  recorded revision trigger.

## Validation and review

The catalog validates after the flip, with the specification synced to the
lifecycle and the article's binding at 0.2.0. Review this ADR when a
control survey is made, when first printings are collated, or when
evidence of access before December 1973 is found.

## References

- [Controlling specification](../docs/framework/sendy-messages-literary-comparison.md)
- [Evidence map](../docs/evidence/woh-claim-0072-evidence.md)
- [Inventory](../docs/research/sendy-inventory/)
- [ADR 0010](0010-continental-breakup-promotion.md) (promotion precedent)
