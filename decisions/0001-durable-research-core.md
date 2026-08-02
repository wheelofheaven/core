---
title: "ADR 0001: Durable research core"
status: accepted
date: 2026-08-02
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0001-establish-wheel-of-heaven-core.md
---

# ADR 0001: Durable research core

## Context

Wheel of Heaven has mature source, content, publication, API, and documentation
repositories but no dedicated authoritative layer for its framework semantics,
research state, source interpretation, or conceptual history. These concerns
are distributed across public content and tool-specific operational documents.

## Decision drivers

- Preserve Wheel's declared canonical stance without confusing it with
  empirical validation.
- Separate research meaning from public prose and software.
- Make claims, evidence, alternatives, source access, and revisions auditable.
- Reuse stable source IDs and existing repositories rather than duplicate data.
- Keep the initial system plain, inspectable, and cheap to revise.

## Options considered

The full alternatives are recorded in RFC 0001: status quo, `data-content`, the
docs site, `.claude`, and a dedicated core.

## Decision

Create `wheelofheaven/core` as a Markdown-first durable research corpus with
JSON claim records, source notes, RFCs, ADRs, and minimal validation.

The repository distinguishes:

- claim kind;
- framework relation;
- lifecycle;
- evidence status;
- public label.

The first release is additive and pilots two existing claims. It does not
change existing public content or automatically derive public badges.

## Consequences

### Enables

- Framework claims can change without silent public redefinition.
- Project adoption and evidential support can be represented together without
  conflation.
- Source access limits and interpretive steps become visible.
- Public derivatives can eventually declare controlling claim versions.
- Durable conceptual decisions no longer need to live only in tool-specific
  operational files.

### Costs and risks

- A new repository adds maintenance and cross-linking work.
- Formal records can create false confidence if review remains superficial.
- Human and JSON forms can diverge despite validation.
- The claim decomposition may prove wrong after more pilots.

## Compatibility and migration

No existing repository is changed by this decision. Existing source IDs,
public URLs, badges, and schemas remain intact. A later RFC is required for
bulk migration or publication integration.

## Validation and review

Review after the two pilot claims have undergone human criticism and after a
third, chronologically structured pilot has been attempted. Supersede this ADR
if the separate repository obscures rather than clarifies authority.

## References

- [RFC 0001](../rfcs/0001-establish-wheel-of-heaven-core.md)
- [Conceptual architecture](../docs/foundations/conceptual-architecture.md)
- [Claim model](../docs/methodology/claim-model.md)
