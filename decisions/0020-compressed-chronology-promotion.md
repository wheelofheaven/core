---
title: "ADR 0020: Promote woh-claim-0080 (the compressed chronology of terrestrial life) to accepted"
status: accepted
date: 2026-11-22
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs: []
---

# ADR 0020: Promote woh-claim-0080 (the compressed chronology of terrestrial life) to accepted

## Context

`woh-claim-0080` was drafted on 2026-11-22 at founder direction. Its
proposition: the planet is old; all terrestrial life, fossils included,
falls within roughly the last twenty-five thousand years; the geologic
time scale is rejected as a chronology of life. Its canonical basis is
dictated text only ([ADR 0018](0018-canon-boundary-dictated-messages.md)).
The founder's decisions on wording and standing are in
[ADR 0019](0019-claim-0080-review-decisions.md). He then directed: "accept
and merge".

## Decision drivers

- The founder holds this position and wants it to be the basis of further
  research.
- A claim must be accepted before a research cycle derives expectations
  from it or a public page binds to it.

## Options considered

### Option A — promote now

The record carries its alternatives at strength and marks every scientific
source as not yet inspected.

### Option B — keep as draft until sources are read

Delays research on the claim for work the research cycle itself will do.

## Decision

Option A. `woh-claim-0080` is `accepted` at 0.1.0, `hypothesis`, `derived`,
public label `framework`, evidence status `scoped` and `contested`.

Acceptance records that Wheel of Heaven adopts the proposition. It is not
a finding that the proposition is true, and the record says that
mainstream geology, palaeontology and geochronology reject it.

## Consequences

### Enables

- A research cycle on the claim under RFC 0009.
- Public pages may bind to it, stating it directly as a framework claim
  with its counter-case.

### Costs and risks

- The evidence map's sections B and C rest on descriptions from general
  knowledge until the sources are inspected; prose must not cite them as
  read.
- The annual-layer records (Greenland ice, Lake Suigetsu) are a serious
  difficulty for the proposition and are recorded as such.

## Compatibility and migration

Catalog gains one accepted record. No existing claim changes here
(`woh-claim-0001` moved to 0.2.2 by ADR 0019). No public derivative yet.

## Validation and review

`python3 scripts/validate.py` passes. The first research cycle on the claim
is its review; rulings there may narrow or revise it.

## References

- [ADR 0018](0018-canon-boundary-dictated-messages.md), [ADR 0019](0019-claim-0080-review-decisions.md)
- `docs/framework/compressed-chronology-of-terrestrial-life.md`
