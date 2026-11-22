---
title: "ADR 0016: Founder decisions from research cycle-0001 (first set)"
status: accepted
date: 2026-11-22
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0009-research-programme.md
---

# ADR 0016: Founder decisions from research cycle-0001 (first set)

## Context

[Research cycle-0001](../docs/research/programme/cycle-0001/README.md), the
pilot of the research programme proposed in RFC 0009, took ten expectations
derived from `woh-claim-0001` through registration, blind location and
contest. Five passages it surfaced were put to the founder on 2026-11-22.
This ADR records the five decisions. RFC 0009 itself remains a draft; the
decisions concern claim 0001, its evidence map and one expectation.

The passages:

1. `LWTE-1:15`: « la vie qui se trouve actuellement Terre n'est pas la
   première qui y fut créée et n'est pas la dernière qui y sera créée. Il y
   a eu une infinité de créations sur notre planète ». `LWTE-1:14` says the
   Elohim created « toutes les formes de vie que nous connaissons, y
   compris l'homme ». Claim 0001 says they designed "terrestrial life".
2. `LWTE-1:107`: present humans are « le fruit d'une longue sélection
   naturelle », survivors of epidemics and wars.
3. `TBWTT-3:71` reports Joshua 10:13 as saying the war lasted « presque un
   jour entier »; in the Hebrew the phrase is said of the sun.
4. *The Book Which Tells the Truth* never quotes Genesis 2:7, while the
   evidence map of claim 0001 carried a row attributing to the canon a
   reading of that verse.
5. `TBWTT-2:30` reads « science » in Genesis 2:17 as « livres
   scientifiques »; the Hebrew is *da'at*.

## Decision drivers

- A claim record must not state more than its canonical basis carries.
- An evidence-map row that names a canonical interpretation needs a
  canonical locator.
- A ruling is entered only where the founder gave one.

## Options considered

For each passage the founder was offered three or four options, including
no change. They are listed in the cycle digest and in the session of
2026-11-22. The chosen options follow.

## Decision

1. **Claim 0001 keeps its wording and gains a scope note.** The statement
   is unchanged. Its scope now excludes creations of life on Earth before
   the one the canon attributes to the Elohim, citing `LWTE-1:14` and
   `LWTE-1:15`. The proposition concerns the life now living, humanity
   included. Version 0.2.0 → 0.2.1 (clarification without changed
   proposition).
2. **Natural selection within a created kind is compatible with design.**
   `LWTE-1:107` is not an undirected origin. Expectation `woh-exp-0008` is
   ruled `narrowed`: the canon attributes the origin of the kinds now
   living to the Elohim and allows selection within them. This decides how
   that passage is read for the expectation. It does not decide where the
   canon's position on macroevolution sits among the claims, which remains
   open.
3. **Joshua 10:13: compare with the French Bible the canon quotes before
   any ruling.** The comparison could not be made: the project holds only
   Genesis 1–3 of the Dhorme translation (`dhorme-bible`, access
   `excerpt`). Expectation `woh-exp-0001` stays unruled, and Dhorme's
   Joshua 10 is recorded as an acquisition need.
4. **The Genesis 2:7 row is removed from the evidence map of claim 0001.**
   Subclaim D now has no passage row and says why. Evidence map 0.2.0 →
   0.3.0. The earlier row remains in the repository history.
5. **A new test is registered** for dependence of the canon's readings on
   the French wording: `woh-exp-0011` in cycle-0002, with the two known
   instances excluded.

Unresolved: rulings on `woh-exp-0001` to `0007`, `0009` and `0010`.

## Consequences

### Enables

- Public prose can state the design premise directly while placing earlier
  creations outside it, with a canonical locator.
- The evidence map no longer attributes to the canon a reading it does not
  make.

### Costs and risks

- Pages bound to `woh-claim-0001` declare 0.2.0 and will show as drift
  until their `core_versions` are bumped.
- Subclaim D now rests visibly on the report layer alone, which the map's
  independence summary already said.
- The Joshua comparison depends on access to a volume in copyright.

## Compatibility and migration

- `model/claims/woh-claim-0001.json`, `model/catalog.json`,
  `docs/framework/elohim-civilization-hypothesis.md`: 0.2.1.
- `docs/evidence/woh-claim-0001-evidence.md`: 0.3.0.
- `model/expectations/woh-exp-0008.json`: ruled. `woh-exp-0011.json`:
  registered against claim version 0.2.1.
- Public derivatives of claim 0001 (seven pages, with their translations)
  need `core_versions` set to 0.2.1 when this is merged. No public prose
  changes are required by the scope note; pages that say the Elohim
  created all life on Earth may be reviewed against it.

## Validation and review

`python3 scripts/validate.py` passes on the branch. Revisit decision 1 if a
review of the three books finds a passage that attributes earlier creations
to the Elohim themselves. Revisit decision 3 when Dhorme's Joshua is
inspected.

## References

- [RFC 0009](../rfcs/0009-research-programme.md)
- [Cycle-0001 digest](../docs/research/programme/cycle-0001/README.md)
- [`woh-exp-0008` contest](../docs/research/programme/cycle-0001/woh-exp-0008-contest.md)
- [`woh-exp-0004` contest](../docs/research/programme/cycle-0001/woh-exp-0004-contest.md)
- [ADR 0007](0007-split-canonical-contact-report.md)
