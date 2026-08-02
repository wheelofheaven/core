---
title: "RFC 0002: Publication integration contract"
status: draft
authors:
  - project founder
created: 2026-08-02
review_until: null
related_adrs: []
supersedes: []
superseded_by: null
---

# RFC 0002: Publication integration contract

## Review question

Should a public `data-content` page be allowed to declare which core claim(s)
and versions it renders, and should the core validator detect when a page
disagrees with its controlling claim record?

## Summary

Define a minimal, opt-in frontmatter contract — `core_claim_ids` and
`core_versions` — that a `data-content` page may add to bind itself to one or
more core claims at an exact version. Extend the core validator so that, when
the sibling repositories are checked out, a declared version that no longer
matches the claim record is reported as a compatibility failure.

This RFC pilots the contract on a single page (`wiki/elohim.md` bound to
`woh-claim-0001`). It does not backfill the other `framework` pages and does
not change URLs, reader-facing badges, or templates.

## Problem and scope

Stage 5 of the roadmap requires that "public outputs identify the exact core
version they render, and compatibility failures are visible before
publication." Today a derivative page can silently drift from the claim it
expresses: if a claim's proposition, scope, or version changes, nothing flags
the pages that still render the old wording.

Scope: one new opt-in frontmatter contract, one validator check, one pilot
page. Non-goals: template changes, badge derivation, API exposure, and bulk
migration of the ~60 current `framework` pages.

## Claim kinds and evidence

This is a repository-process and compatibility decision, not evidence for a
substantive Wheel claim. The motivating observation is the existing
`public_derivatives` lists in the claim records, which currently point outward
without any reciprocal, versioned link back.

## Detailed proposal

### Frontmatter fields (data-content)

A page opts in by adding, in its TOML `[extra]` table:

```toml
[extra]
core_claim_ids = ["woh-claim-0001"]
core_versions = { woh-claim-0001 = "0.1.0" }
```

- `core_claim_ids`: an array of core claim IDs the page renders.
- `core_versions`: a table mapping each declared ID to the claim version the
  page was written against. Every ID in `core_claim_ids` must have a matching
  key in `core_versions`.

Both fields are optional. A page without them is "not yet integrated" and is
never an error. The fields are inert at render time until a later, separate
decision defines any template use.

### Reciprocal record (core)

Each claim already lists its `public_derivatives`. The contract adds no new
core field: the derivative path is the join key. A page may declare a claim it
is not yet listed under; the validator warns rather than errors, so pages and
records can be reconciled incrementally.

### Validator behaviour

When a derivative page is resolvable under `--wheel-root`, for each page that
declares the fields the validator checks:

1. every declared `core_claim_id` exists in the catalog — else error;
2. every declared ID has a `core_versions` entry — else error;
3. the declared version equals the current claim record version — else a
   **disagreement** error naming the page, claim, declared version, and
   current version;
4. if the page declares a claim that does not list the page in its
   `public_derivatives`, a warning (not an error).

When the sibling repositories are absent, the check is skipped with a warning,
exactly like the external source-registry check.

## Alternatives

### Status quo (one-way derivatives)

Keep `public_derivatives` as an outward pointer only. Simple, but leaves Stage
5's compatibility requirement unmet: drift stays invisible.

### Store the binding in core instead of the page

Record page-version bindings in the claim JSON. This keeps data-content
untouched but puts publication state in the research core and forces a core
commit for every page edit — the coupling this repository is meant to avoid.

### Derive public badges now

Project `direct`/`framework`/`inferred`/`speculative` from core fields
immediately. Premature: the claim model states the public taxonomy blends
axes and needs a human decision; that is out of scope here.

## Risks, limitations, and dissent

- Two representations (page frontmatter, claim record) can still drift between
  validator runs; the check catches it only when run.
- An opt-in field invites partial adoption and inconsistent coverage until a
  later backfill decision.
- Version-equality is a blunt signal: a `PATCH` clarification that does not
  change meaning will still trip the check, prompting a mechanical version bump
  on the page. This is acceptable for a pilot and revisited if noisy.
- The contract assumes the derivative path in `public_derivatives` matches the
  page's real location across the standalone `data-content` repo and the `www`
  content submodule.

## Compatibility and migration

Additive. No existing page changes except the single pilot page, which gains
two inert `[extra]` fields. No URL, badge, template, schema, or claim-ID
change. If accepted, backfill of other pages is a later, separate decision.

## Validation plan

- Run `mise run check` with the sibling repositories present and confirm the
  pilot page passes (declared `0.1.0` matches the record).
- Temporarily bump the claim version and confirm the validator reports the
  disagreement, then restore it.
- Decide, after the pilot, whether version-equality is the right signal or
  whether a compatibility range is needed before any backfill.

## Resolution

Open. This RFC is a draft pilot; it must not be treated as accepted until the
project founder decides and an ADR records the decision.
