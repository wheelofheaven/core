---
title: "ADR 0015: Revise woh-claim-0010 to the canon's two-faction account and passage-specific flood features"
status: accepted
date: 2026-11-21
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0003-artifact-derivation-contract.md
---

# ADR 0015: Revise woh-claim-0010 to the canon's two-faction account and passage-specific flood features

## Context

`woh-claim-0010` 0.1.0 ("The Flood as deliberate reset") stated that five
flood texts share one decision procedure (assembly, oath, irrevocability,
dissent, seed-preservation instructions) and that the canon reads the
event as "a deliberate reset decision within the Council's governance".

The [procedural comparison](../docs/research/flood-concordance/procedural-comparison.md)
(2026-11-20, independently reviewed) found that no text attests the full
sequence, and that the alternative-disaster list attributed to Atrahasis
is securely located in Gilgamesh XI. A re-reading of the canon on
2026-11-21 (TBWTT 2:55–74; LWTE 2:25–28) found that the Council's
decision is total destruction, that the preservation is the exiles' act
against it, and that "never again" is a reversal after the event. The
0.1.0 canonical layer contradicted the canon and `woh-claim-0008`.

The [proposal](../docs/research/flood-concordance/claim-0010-revision-proposal.md)
put five questions to the founder.

## Decision

The founder approved the proposal on 2026-11-21 ("ok, go ahead"). Where a
question carried no default, the narrower option was taken:

1. **Title:** "The Flood as a contested decision".
2. **Canonical layer:** the two-step canon account: the home world's
   decision to destroy, the exiles' circumvention, the post-event
   reversal. The two motive statements (progress in TBWTT, violence in
   LWTE) are registered separately.
3. **Comparative observation** (Mesopotamian destroying authority vs.
   rescuing god as a counterpart of Council vs. exiles): **not adopted**;
   recorded as an exclusion.
4. **Geology:** the exclusion now points to `woh-claim-0071`.
5. **Sumerian Flood Story:** no new source ID; cited through the
   concordance keys until an English edition is inspected directly.

`woh-claim-0010` goes to 0.2.0. Its id, kind, framework relation, public
label and evidence status are unchanged. `LWTE-2:25–28` is added as a
canonical basis; the alternatives list is cited to Gilgamesh XI 180–197;
the Atrahasis alignment stays open as a revision trigger.

## Consequences

- Record, catalog entry, specification and evidence map move to 0.2.0.
- Bound pages bump `core_versions` to 0.2.0. The Explainer *The Flood Was
  a Reset, Not a Punishment* is corrected where it states the full
  sequence for "the oldest flood stories" and where it presents the reset
  as the planners' intent. Its title stands: in the canon the event is
  not moral retribution and its outcome is a reset.
- English first; the nine languages follow with translator and reviewer
  per language.

## Validation and review

`mise run check` with publication integration after the page bumps.
Review this ADR when an Atrahasis edition resolves ATRA-WOH-III:vi.21–24,
or if the comparative observation in (3) is proposed again with a source
that states it.

## References

- `woh-claim-0008`, `woh-claim-0060`, `woh-claim-0071`
- [Flood concordance](../docs/research/flood-concordance/README.md)
