---
title: "ADR 0002: Artifact derivation contract"
status: accepted
date: 2026-08-15
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs:
  - ../rfcs/0002-publication-integration-contract.md
  - ../rfcs/0003-artifact-derivation-contract.md
---

# ADR 0002: Artifact derivation contract

## Context

RFC 0002 defined the opt-in page↔claim binding (`core_claim_ids` +
`core_versions`) and piloted it on `wiki/elohim.md`. RFC 0003 proposed
turning that binding into a production contract: new artifacts ground their
load-bearing assertions in claim records before prose is written, drafting
missing records with a founder pause, and declare the binding on
publication. The reverse pilot (`woh-claim-0004`, extracted from the
published Odyssey Explainer and bound back to it) validated that a real
article's speculative layer can be captured as a conforming record, and
surfaced the cost of prose-first production (an unrecorded dependency, a
label chosen without a controlling record).

## Decision drivers

- Close the two-constitutions split: publication rules governed voice while
  claim discipline stayed per-page editorial judgment.
- Make founder review reusable: review a claim record once instead of every
  artifact and language that expresses it.
- Keep the core inert at render time and keep all founder gates unchanged.
- Avoid stalling production: adoption must ratchet, not backfill.

## Options considered

The full alternatives are recorded in RFC 0003: status quo (opt-in binding,
prose-first production), mandatory retroactive backfill, binding stored in
core, and full autonomy without the founder pause.

## Decision

Accept RFC 0003 as proposed. New artifacts and fundamental rewrites follow
the derivation norm (Scope → Ground → Produce → Bind); newly drafted claim
records pause for founder review before prose is written against them; the
existing corpus is grandfathered; translations inherit their source page's
binding; dispatches may bind but need not.

Accepting RFC 0003 also **closes RFC 0002 by adoption**: RFC 0003
incorporates the RFC 0002 contract unchanged and lifts its single-page pilot
restriction, so no separate decision on RFC 0002 remains open.

The role charters in
[production roles](../docs/methodology/production-roles.md) are promoted to
`accepted` as part of this decision; workspace tooling that contradicts a
charter is a bug in the tooling.

## Consequences

### Enables

- An artifact's insight is quotable from a claim record, not only from the
  artifact; `claim_type` badges gain a controlling record.
- The catalog grows monotonically with production instead of by campaign.
- Any agent harness (Claude Code, Codex, human) can run the same pipeline
  from the same charters.

### Costs and risks

- A founder pause now prices every novel-insight artifact; the tax falls as
  the catalog grows but starts high with a four-claim catalog.
- Pressure to publish may produce thin records; the `woh-claim-0004`
  evidence map is the review floor.
- Version-equality binding ripples PATCH bumps to bound pages (known from
  RFC 0002; revisit with a compatibility range if noisy).

## Compatibility and migration

Additive. No identifier, schema, URL, badge, or template changes. The
validator's RFC 0002 behaviour needs no modification. Grandfathered pages
remain valid indefinitely; backfill follows the reverse-pilot pattern at
editor's discretion.

## Validation and review

The forward pilot named in RFC 0003 — one new artifact produced
grounding-first through the workspace pipeline, including a founder pause on
at least one newly drafted record — is now the first implementation step.
Review this ADR if the pause proves to stall production rather than price
it, or if record quality degrades under publication pressure.

## References

- [RFC 0003](../rfcs/0003-artifact-derivation-contract.md)
- [RFC 0002](../rfcs/0002-publication-integration-contract.md)
- [Production roles](../docs/methodology/production-roles.md)
- [`woh-claim-0004`](../docs/framework/greek-theomachy-memory.md) (reverse pilot)
