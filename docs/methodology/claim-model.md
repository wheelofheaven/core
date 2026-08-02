---
title: Claim model
status: accepted
version: 0.1.0
last_reviewed: 2026-08-02
---

# Claim model

The core uses separate axes so that source provenance, project commitment,
evidence, maturity, and public rhetoric do not collapse into one badge.

## Claim kind

| Kind | Records | Must not silently become |
| --- | --- | --- |
| `source_report` | What a named source explicitly says or depicts | An observation that the reported event occurred |
| `empirical_observation` | A documented textual, linguistic, historical, or scientific result | A causal explanation or universal fact |
| `model` | A selective representation connecting constructs or records | Reality itself |
| `hypothesis` | A proposed testable relationship or explanation | A finding because it is canonical or plausible |
| `interpretation` | Meaning inferred from sources, observations, or models | Direct source content |
| `normative_recommendation` | A proposed goal, preference, or action | A conclusion forced by descriptive evidence |

A framework specification may contain several kinds. Its machine record names
the primary kind of its exact proposition; the prose must expose transitions.

## Framework relation

| Relation | Meaning |
| --- | --- |
| `foundational` | Defines the declared interpretive starting point |
| `derived` | Follows within the framework through stated dependencies |
| `comparative` | Connects the framework with another tradition, text, or model |
| `contextual` | Supplies relevant philological, historical, or scientific context without becoming a framework premise |
| `critical` | Challenges, limits, or offers an alternative to a framework claim |

Framework relation is not evidence strength.

## Lifecycle

`draft`, `proposed`, `accepted`, `deprecated`, and `superseded` describe the
repository's use of a record. They do not describe empirical support.

## Evidence status

Evidence status is a list because a claim can be both `reviewed` and
`contested`. See [Evidence status](evidence-status.md).

## Public label

Wheel's publishing surfaces currently use:

- `direct`: explicit source content or mainstream-uncontroversial fact;
- `framework`: a foundational or derived Wheel premise not endorsed by
  mainstream scholarship;
- `inferred`: a bounded interpretation consistent with its source basis;
- `speculative`: a synthesis or hypothesis beyond any single source.

These labels are retained for compatibility but are not inferred mechanically.
The current public taxonomy blends several axes, so a human editorial decision
remains required.

## Invalid transitions

- Source report to historical occurrence without independent evidence.
- Morphological form to full syntactic meaning without contextual analysis.
- Lexical possibility to intended referent without argument.
- Resemblance to historical dependence or identity without discriminating
  evidence.
- Scientific possibility to actual terrestrial history.
- Framework acceptance to empirical validation.
- Citation quantity to independent confirmation.
- Public badge to evidence status.
