---
title: "ADR 0010: Promotion of woh-claim-0071 (continental breakup at the Flood)"
status: accepted
date: 2026-09-12
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0003-artifact-derivation-contract.md
---

# ADR 0010: Promotion of woh-claim-0071 (continental breakup at the Flood)

## Context

The Explainer *The Signature and the Designers* (published 2026-09-01)
described the canon's Flood as "a reset and not a rewriting of the rocks".
On 2026-09-10 the founder corrected this as contradicting the canon: the
home-planet strike broke the single Elohim-raised continent into today's
drifting continents and buried the living surface at once, and the corpus
reads the fossil beds as the burial sequence of that aftermath. The article
was corrected in all ten languages the same day.

The correction exposed a catalog gap. The consequence was stated across
the corpus — `wiki/pangaea.md`, `wiki/great-flood.md`, the Age of Gemini
timeline chapter — but no record carried it: `woh-claim-0010` (the Flood
as deliberate reset) excludes "historicity or dating of a global flood as
a geological claim" by design, and the Pangaea candidate that ADR 0006 and
ADR 0007 left open had never been drafted. Under the RFC 0003 contract the
record was drafted on 2026-09-12 as `woh-claim-0071` with its controlling
specification and a scoped evidence map, and the four derivative pages
were bound to it at `0.1.0`. The draft was presented to the founder the
same day.

## Decision drivers

- The catalog had carried no draft records since ADR 0008; a standing
  draft with live page bindings is the state the contract tells agents to
  pause in, not to remain in.
- The record's canonical basis splits across two layers of source — the
  message text (TBWTT ch. 2 ¶14, ¶58) and the commentaries printed with
  the third message (*Let's Welcome the Extraterrestrials* ch. 4 ¶35 and
  following). The draft keeps that split visible as an alternative and a
  revision trigger rather than resolving it.
- Acceptance is the founder's confirmation that the record states the
  corpus position correctly. It is not a finding about the geology.

## Options considered

### Option A — Promote as drafted

Accept the record at 0.1.0 with its `framework` label, `scoped` and
`contested` evidence status, five alternatives-and-triggers commitments,
and the commentary-versus-message question left open.

### Option B — Hold pending source criticism of LWTE ch. 4

Leave the record `draft` until a reproducible review (RFC 0007) settles
whose text the "New Hypothesis" commentary is. Cleaner canonical weight;
but the corpus position does not depend on the answer, and the pages
already state it.

## Decision

The founder directed **option A** on 2026-09-12: `woh-claim-0071` is
promoted from `draft` to `accepted` lifecycle.

Acceptance means what the claim model says it means: the record is the
current project specification of what the framework claims about the
Flood's geological consequence — not a validation, not an upgrade of any
evidence status.

Unchanged by this decision: the record's version (page bindings at
`0071@0.1.0` stand), public label, evidence status (`scoped` and
`contested`), scope, alternatives, and revision triggers. The evidence map
keeps `draft` status as a living research artifact, per the ADR 0005
convention. The commentary-versus-message authorship question and the
unverified petroleum-ring citation remain open as recorded.

## Consequences

### Enables

- The catalog again carries no draft records: 71 claims, all `accepted`.
- Prose can state the continental breakup and the fossil-burial reading
  directly, citing an accepted record, and the species boundary with
  young-earth Flood geology has a controlling specification to quote.
- The source-critical question about LWTE ch. 4 is now a well-formed
  candidate for a reproducible review record.

### Costs and risks

- Accepted status can misread as validation; the record's own scope and
  the claim model's "lifecycle is not truth" rule are the standing answer.
- The record inherits the Model-C lattice risk of `woh-claim-0059` and
  `woh-claim-0019` for its dating; those records' revision triggers
  propagate.

## Validation and review

The catalog validates end to end after the flip (71 records;
specification synced to lifecycle; publication integration checked with
no version disagreement across the four bound pages). Review this ADR if
the LWTE ch. 4 authorship review lands, if the petroleum-ring citation is
located or shown absent, or if the corpus adopts a mechanism for the
radiometric discrepancy — each is a recorded trigger.

## References

- [Controlling specification](../docs/framework/continental-breakup-at-the-flood.md)
- [Evidence map](../docs/evidence/woh-claim-0071-evidence.md)
- [ADR 0008](0008-pilot-claims-promotion.md) (promotion precedent)
- [RFC 0003](../rfcs/0003-artifact-derivation-contract.md) (drafting and binding contract)
- [Claim model](../docs/methodology/claim-model.md) (lifecycle semantics)
