---
title: "ADR 0003: Depiction notes"
status: accepted
date: 2026-08-15
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0004-depiction-notes.md
---

# ADR 0003: Depiction notes

## Context

The project produces visual and scenic artifacts — hero images,
illustrations, gallery renders, audio-play staging — with no core-side
grounding: every image quietly makes claims, and an image cannot hedge.
RFC 0004 proposed a `depictions/` document class separating what sources
visually report from what the project interpolates and what is free art
direction, with briefs binding notes the way pages bind claims.

## Decision drivers

- Extend the derivation contract (ADR 0002) to artifacts where labels are
  invisible and hedging is impossible.
- Keep the reported/interpolated boundary in the core, where that
  distinction is already policed, rather than in a publication-side style
  bible.
- Keep style, palette, and craft on the publication side; the core records
  claims, not taste.

## Options considered

Recorded in RFC 0004: status quo (art direction decides), folding depiction
content into claim records, and a publication-side style bible without core
involvement.

## Decision

Accept RFC 0004 as proposed. `depictions/{slug}.md` becomes the fourth core
document class, with the fixed four-layer body (Reported / Interpolated /
Free / Must not show), lifecycle frontmatter, and optional `claim_ids`.
Briefs bind via `core_depiction_ids` + `core_depiction_versions`; rendered
assets inherit their brief's binding. Founder gates are unchanged: agents
draft, layer-2 interpolations embedding new identifications require founder
direction, promotion is founder-only.

The pilot named in the RFC — `elohim-individual` and `typhoeus-combat`,
each bound by one real brief — is the first implementation step, and the
validator extension is specified only after the pilot has run.

## Consequences

### Enables

- Illustrations and scenery derive from records; canon drift in imagery
  becomes auditable across languages and pipelines.
- "Free" becomes a recorded decision, protecting art direction from both
  false constraint and silent claim-making.

### Costs and risks

- A fourth document class grows the core's surface; expansion beyond the
  pilot only on demonstrated use.
- Sources underdetermine most depictions; the mandatory Free layer is the
  guard against false precision.
- Until validator support lands, the binding is normative only.

## Compatibility and migration

Additive: new directory, new optional brief frontmatter fields. Existing
imagery is grandfathered; audits happen opportunistically at fundamental
rewrites, per the ADR 0002 ratchet.

## Validation and review

After the two pilot notes are authored and one asset is regenerated from a
bound brief, the founder compares the render against the note's layers: does
the record change what gets rendered, and is the Free layer wide enough?
Revisit this ADR if notes prove to flatten the visual language or go unused
by the image pipeline.

## References

- [RFC 0004](../rfcs/0004-depiction-notes.md)
- [ADR 0002](0002-artifact-derivation-contract.md)
- [Production roles](../docs/methodology/production-roles.md) (Art Director charter)
