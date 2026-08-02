---
title: Conceptual architecture
status: accepted
version: 0.1.0
last_reviewed: 2026-08-02
---

# Conceptual architecture

Wheel of Heaven Core is a set of versioned claims and replaceable explanatory
components connected by explicit dependencies. It is not a narrative in which
one attractive correspondence automatically validates the next.

## Documentation layers

The core separates:

1. foundations that govern inquiry;
2. framework specifications that control conceptual meaning;
3. machine-readable claim records and catalogs;
4. research questions and review programmes;
5. methodology for sources, evidence, comparison, and change;
6. source notes that separate reported content from interpretation;
7. open proposals and criticism;
8. adopted decisions and historical rationale;
9. public derivatives maintained elsewhere.

Human-readable specifications control semantics. JSON records control
interchange. If they disagree, both are considered inconsistent until a review
resolves the difference.

## Cross-repository flow

```text
data-sources ──► data-library ───────────────┐
                    │                        │
data-bibliography ──┴─► source IDs ──► core │
                                             ▼
                                      data-content
                                        │      │
                                        ▼      ▼
                                       www    api
```

The arrows show provenance and derivation, not causal proof. The core may cite
source IDs and passage references but does not own the underlying texts.

## Claim interface

Each mature claim should identify:

- a stable identifier and exact proposition;
- claim kind and framework relation;
- lifecycle, evidence status, and public label;
- scope and exclusions;
- source references with locators and roles;
- dependencies on other claims or definitions;
- strongest alternatives and objections;
- revision triggers and invalid shortcuts;
- controlling human-readable document and version;
- public pages, datasets, or API resources that derive from it.

## Initial claim map

| Claim | Relation | Depends on | Does not establish |
| --- | --- | --- | --- |
| `woh-claim-0001` Elohim-civilization hypothesis | Foundational | Raëlian source reports; identification of the source's `Elohim` with the framework subject | Empirical existence or occurrence merely because the source reports it |
| `woh-claim-0002` Anunnaki–Elohim identity | Comparative | Claim 0001; Mesopotamian source interpretation; criteria for referential identity | Every deity mapping, Sitchin's apparatus, or identity from resemblance alone |
| `woh-claim-0003` Precessional world-age chronology | Foundational | Observed axial precession (idealized); canonical threshold report; the project anchor convention | Astronomical reality of age boundaries, ancient precessional knowledge, or any event placement |

This three-claim map is a pilot, not a settled decomposition of the whole
framework.

## Public compatibility

Existing `direct`, `framework`, `inferred`, and `speculative` badges remain a
public presentation contract. The core records them but does not yet derive
them automatically. A future RFC may define a safe projection after the pilot
shows which distinctions survive publication.
