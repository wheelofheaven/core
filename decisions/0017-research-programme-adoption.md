---
title: "ADR 0017: Adopt the research programme of registered expectations (RFC 0009)"
status: accepted
date: 2026-11-22
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0009-research-programme.md
---

# ADR 0017: Adopt the research programme of registered expectations (RFC 0009)

## Context

[RFC 0009](../rfcs/0009-research-programme.md) proposed a standing research
programme: expectations derived from the foundational claims, registered by
commit before any source is inspected, located by an agent that sees only a
neutral brief, contested by a Critic, and ruled by the founder alone.

Two cycles tested it on 2026-11-22. [Cycle-0001](../docs/research/programme/cycle-0001/README.md)
ran ten expectations on `woh-claim-0001`; the Critics changed five of ten
mechanical assessments, and the passages it surfaced led to
[ADR 0016](0016-cycle-0001-rulings.md). Its digest listed what failed in the
method and proposed five amendments. [Cycle-0002](../docs/research/programme/cycle-0002/README.md)
ran one expectation designed with three of those amendments applied by hand,
and it produced the programme's first result that a rival predicts
differently from the claim.

The founder directed adoption on 2026-11-22 ("commit and push, do it all, 1
through 5"), item 5 being acceptance of RFC 0009 by ADR.

## Decision drivers

- Research done by agents needs a structural guard against confirming a
  hypothesis handed to it.
- Misses and null results have to be kept as carefully as hits.
- The founder's attention per cycle has to stay bounded.

## Options considered

### Option A — adopt RFC 0009 with the pilot's amendments

The method as proposed, plus the five amendments the pilot showed were
needed.

### Option B — adopt RFC 0009 as originally drafted

Leaves known failure modes in place: overstated discrimination, families
located under different rules, controls counted as progress.

### Option C — leave it a draft for further cycles

Keeps the method provisional while it is already in use and wired into the
workspace.

## Decision

Option A. RFC 0009 is accepted, and
[docs/methodology/research-programme.md](../docs/methodology/research-programme.md)
becomes `accepted` at version 0.2.0 with these amendments:

1. **Pre-registration check.** An agent that did not derive the set checks
   each draft record for real discrimination, leakage of the hoped answer
   and the tightness of the selection rule before the registration commit.
2. **A favouring result.** An expectation counts as discriminating only if
   its criteria name a result that would favour the claim over a rival as
   the protocol measures it. A test whose only discriminating outcome is
   its own failure is `discrimination: none` or is redesigned.
3. **Families.** Expectations applying one test to several targets share a
   `family` id, are located by one Locator under one inclusion rule, and
   count once on the scoreboard.
4. **Controls apart.** Controls carry `scoring: control` and are reported
   apart from the scoreboard.
5. **Source-report intake.** Work that tests what a source says outside
   any claim's scope carries `scoring: source_report` and feeds source
   notes, not a claim's scoreboard.

`family` and `scoring` may be added to a record after registration because
they classify it without changing what was expected. They were added to
cycle-0001's records (families `speaker-hebrew` and `hinge-word`; controls
`woh-exp-0009` and `0010`). No frozen field of any registered record changed.

RFC 0008 (the standing claim-review cycle) is not decided by this ADR.

## Consequences

### Enables

- Agent sessions can run research cycles under an accepted method through
  the `woh-research` skill and its agent definitions.
- The scoreboard counts a family once and keeps controls out.

### Costs and risks

- A pre-registration check adds one agent run per cycle.
- The scoreboard remains a measure of the programme's yield, never of a
  claim's truth.

## Compatibility and migration

Additive. Schema gains two optional fields; the validator checks them;
`programme.py status` groups families and reports controls apart. No claim
record changes.

## Validation and review

Revisit after three further cycles, per RFC 0009's validation plan: whether
any expectation reaches the progress class, whether any cycle produces a
miss and an output, and whether the pre-registration check catches what
the cycle-0001 Critics caught.

## References

- [RFC 0009](../rfcs/0009-research-programme.md)
- [ADR 0016](0016-cycle-0001-rulings.md)
- [Cycle-0001 digest](../docs/research/programme/cycle-0001/README.md)
