---
title: "RFC 0003: Artifact derivation contract"
status: accepted
authors:
  - project founder
  - Claude (drafting agent, at founder direction)
created: 2026-08-15
review_until: null
related_adrs:
  - ../decisions/0002-artifact-derivation-contract.md
supersedes: []
superseded_by: null
---

# RFC 0003: Artifact derivation contract

## Review question

Should every newly produced Wheel of Heaven artifact — article, wiki entry,
timeline chapter, dispatch, dataset description, illustration brief,
audio-play scene — be required to derive its load-bearing assertions from
core claim records (existing or newly drafted), and to declare that
derivation via the RFC 0002 binding?

## Summary

RFC 0002 defined an opt-in, page-level binding (`core_claim_ids` +
`core_versions`) and piloted it on one page. This RFC proposes to turn the
binding from an integrity check into a **production contract**: new artifacts
begin from claim records rather than ending at them. Concretely, a "Ground"
stage is inserted at the front of every production pipeline — resolve the
topic against the catalog, read the relevant records and evidence maps, draft
missing records as `draft` claims — and the finished artifact declares what
it renders. The insight lives in the record; the artifact is a bounded public
projection of it, in the sense already defined by the
[epistemic principles](../docs/foundations/epistemic-principles.md).

Adoption is ratcheting, not retroactive: the contract binds new artifacts
and fundamental rewrites; the existing corpus is grandfathered exactly as
`claim_type` and `editorial_pass` were.

## Problem and scope

The project currently has two constitutions that do not talk to each other.
The publication side (workspace rules, editorial standards, the article and
translation pipelines) governs *how things are said*. The core governs *what
may be claimed and on what basis* — but only one page in the corpus is bound
to it. In practice an article's load-bearing insights are invented at write
time, disciplined by voice rules alone, and the claim-typing decision
(`claim_type`) is made per page, per author, per day.

The motivating case is the reverse pilot recorded in
[`woh-claim-0004`](../docs/framework/greek-theomachy-memory.md): the Odyssey
Explainer was written first and its central reading extracted into a claim
record afterwards. The extraction worked, but it surfaced exactly the costs
of writing prose before records: an unrecorded dependency (the
Council–Serpentine conflict account exists as corpus prose, not as a claim),
a public label chosen without a controlling record, and falsifiability terms
that lived only inside one article's closing sections.

Scope: a production-order norm, a Ground-stage definition, and an extension
of the RFC 0002 binding beyond its single-page pilot. Non-goals: badge
derivation from core fields (still a human decision); any core-side service,
build step, or template involvement (the core stays inert at render time);
retroactive backfill of the existing corpus; any change to founder gates.

## Claim kinds and evidence

This is a repository-process proposal (`normative_recommendation`), not
evidence for a substantive Wheel claim. The supporting observations:

- the RFC 0002 pilot validated the binding mechanics (validator check,
  version drift detection) on `wiki/elohim.md`;
- the reverse pilot (`woh-claim-0004`, bound from
  `articles/the-world-behind-the-odyssey.md`) validated that a real
  article's speculative layer can be captured as a conforming record with
  alternatives, revision triggers, and an evidence map;
- the translation program demonstrates that staged pipelines with structured
  handoffs and human sign-off gates work at corpus scale in this project.

## Detailed proposal

### 1. The derivation norm

For any new artifact, or any fundamental rewrite of an existing one:

1. **Scope** — identify the artifact's load-bearing assertions: the claims
   the artifact would be wrong about if they were wrong. Incidental
   background does not count.
2. **Ground** — resolve each load-bearing assertion against
   `model/catalog.json`:
   - if a record exists, read the record, its controlling specification, and
     its evidence map; the artifact must express the claim within the
     record's scope and public label;
   - if no record exists, draft one (`lifecycle: draft`), with its
     controlling specification and at least a scoped evidence map, before
     the artifact's prose is written. Drafting is within agent authority;
     promotion is not (see §4).
3. **Produce** — write the artifact under the existing publication-side
   rules (voice, sourcing floors, section structure).
4. **Bind** — declare `core_claim_ids` and `core_versions` in the
   artifact's frontmatter per RFC 0002, and add the artifact to each claim's
   `public_derivatives`.

The norm's test is simple: **an artifact's insight must be quotable from a
claim record, not only from the artifact.**

### 2. Extension of the RFC 0002 binding

The RFC 0002 contract (fields, validator behaviour, warning semantics) is
adopted unchanged for all text artifact types in `data-content`: wiki,
articles, timeline, news, datasets, library apparatus. The single-page pilot
restriction is lifted. The Odyssey binding performed in this RFC's reverse
pilot is the first instance under the extended scope.

Non-page artifacts (illustration briefs, audio-play scenes) bind at the
brief level, not the rendered-asset level; their format is defined in
[RFC 0004](0004-depiction-notes.md) and out of scope here.

### 3. Ratcheting adoption

- **Binds:** artifacts created after this RFC's acceptance; fundamental
  rewrites (the `editorial_pass` threshold — the same event that already
  triggers a pass stamp).
- **Grandfathered:** the existing corpus. Backfill is editor's call,
  incremental, and follows the reverse-pilot pattern: extract the record
  from the artifact, then bind.
- **Exempt:** translations (they inherit the source page's binding);
  mechanical edits; dispatches *may* bind but are not required to (they are
  time-anchored readings, and their canon anchor is already mandatory via
  `canon_links`).

### 4. Authority boundaries (unchanged, restated)

The contract does not move any founder gate. Agents may draft claim records,
specifications, evidence maps, and research questions as clearly marked
drafts. Agents must not promote a lifecycle, add a foundational claim,
identify referents across traditions on their own initiative, or weaken
recorded dissent. A production pipeline that reaches a missing-record
situation drafts and **pauses for founder review of the record before prose
is written on top of it**. This is the contract's entire value: founder
review moves from "is this article's argument sound" to "is this claim
record sound" — once, reusable across every artifact and language that later
cites it.

### 5. Pipeline integration

The workspace-side entry point (the `woh-produce` skill and the role
charters in
[production roles](../docs/methodology/production-roles.md)) implements this
contract for both Claude Code and other agent harnesses. The core does not
depend on that tooling; the contract is satisfiable by hand.

## Alternatives

### Status quo (opt-in binding, prose-first production)

Keeps production fast. Leaves the two-constitution split in place: claim
discipline remains per-page editorial judgment, and insights continue to
live only in artifacts. The reverse pilot shows extraction-after-the-fact is
possible but costs more than grounding-first, and does not scale to a
corpus-wide guarantee.

### Mandatory retroactive backfill

Maximal integrity, but ~100 wiki entries and a dozen articles against a
four-claim catalog would stall production for months and force
batch-authored records of exactly the kind the core exists to prevent.

### Bind in core instead of in the artifact

Rejected for the same coupling reasons as in RFC 0002.

### Full autonomy (no founder pause at Ground)

Faster, but structurally violates the core's authority model: new claims
minted and rendered in one motion reintroduces authoritative-looking content
without review — the failure mode CLAUDE.md exists to prevent.

## Risks, limitations, and dissent

- **Bottleneck risk.** Grounding adds a stage and a founder pause to every
  novel-insight artifact. Mitigation: the pause prices only *new claims*;
  artifacts expressing existing records proceed without it, and the catalog
  grows monotonically, so the tax falls over time.
- **Record inflation.** Pressure to publish may produce thin, pro-forma
  records. Mitigation: a record without scoped evidence and real
  alternatives fails review; the `woh-claim-0004` map sets the floor.
- **Scope creep of "load-bearing."** Authors may under-declare to avoid
  grounding. The `editorial_pass` review is the audit point.
- **Version churn.** Every claim PATCH ripples a version bump across bound
  pages. Known from RFC 0002; acceptable at current scale, revisit with a
  compatibility range if noisy.
- **The claim model may not fit all artifact types.** Visual and scenic
  artifacts derive from depictions as much as from claims; RFC 0004 exists
  because this RFC alone cannot carry them.

## Compatibility and migration

Additive. No identifier, schema, URL, badge, or template changes. The
RFC 0002 fields are reused unchanged; its validator behaviour needs no
modification (the pilot restriction was procedural, not enforced in code).
Grandfathered pages remain valid indefinitely.

## Validation plan

- Reverse pilot (completed with this draft): `woh-claim-0004` extracted from
  the Odyssey Explainer; article bound; validator run with siblings present.
- Forward pilot (before acceptance): produce one new artifact
  grounding-first through the `woh-produce` pipeline, including a founder
  pause on at least one newly drafted record, and record friction.
- After both pilots, founder decides; an ADR records the decision.

## Resolution

Accepted by the project founder on 2026-08-15. Recorded in
[ADR 0002](../decisions/0002-artifact-derivation-contract.md), which also
closes RFC 0002 by adoption. The forward pilot in the validation plan is now
the first implementation step rather than a precondition of acceptance.
