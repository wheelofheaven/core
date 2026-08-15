---
title: Production roles
status: draft
version: 0.1.0
last_reviewed: 2026-08-15
---

# Production roles

Role charters for producing Wheel of Heaven artifacts under the
[artifact derivation contract](../../rfcs/0003-artifact-derivation-contract.md).
The charters are harness-agnostic: they define obligations and outputs, not
tools. Claude Code, Codex, any other agent system, or a human contributor
performing a role follows the same charter; orchestration wiring (subagent
definitions, skills, prompts) lives in the workspace repositories and must
point back here rather than restating these rules.

Every role inherits the
[epistemic principles](../foundations/epistemic-principles.md) and the
constraints in [`CLAUDE.md`](../../CLAUDE.md) in full. The charters add only
what is specific to each role. Two rules are global:

- **Stage boundaries are real.** A role produces its output and stops. A
  writer who discovers a missing claim does not mint one inline; the work
  returns to the Researcher.
- **Founder gates are not pipeline stages.** Where a charter says "pause for
  founder review," no downstream stage may start against the unreviewed
  output.

## Researcher

Owns the Ground stage.

**Obligations.**

- Resolve the artifact's load-bearing assertions against `model/catalog.json`;
  read the full record, controlling specification, and evidence map for every
  hit — not the catalog line alone.
- For each miss, draft the claim record, controlling specification, and a
  scoped evidence map, `lifecycle: draft`, then **pause for founder review**.
- Record what a source reports, at access levels actually verified. Never
  upgrade access (`metadata_only` → `excerpt`) without inspecting the source.
- Map evidence dependencies: repeated citations of the same text, translation,
  or authorial tradition are one source, not several.
- State the strongest fair version of every objection encountered; file
  alternatives and revision triggers with the record, not in prose margins.

**Outputs.** Claim records + specifications + evidence maps (drafts), source
notes, and a grounding report listing: claims matched (with versions), claims
drafted (awaiting review), and assertions found to be incidental rather than
load-bearing.

**Must not.** Promote lifecycles; identify referents across traditions on own
initiative; fill unknowns with authoritative-looking content; tune a record's
scope so a desired artifact sentence becomes expressible.

## Writer

Owns the artifact's prose or brief.

**Obligations.**

- Write only within the scope and public label of the bound records. The test:
  every load-bearing sentence must be quotable from, or a bounded projection
  of, a claim record. Canon-internal claims are stated directly; comparative,
  scientific, and critical layers stay hedged — per the records, not per
  instinct.
- Preserve irreducible differences between traditions; where a record's scope
  excludes something (routes, individual mappings, historicity), the prose
  must not gesture at it either.
- Carry the record's alternatives into the artifact where the form allows a
  counter-case section; an artifact that presents a contested claim without
  its live alternatives misrepresents the record.
- Follow the publication-side voice and sourcing rules of the target section;
  those rules are owned by the workspace, not this charter.

**Outputs.** The draft artifact with `core_claim_ids` + `core_versions`
declared (or `core_depiction_ids` for briefs under
[RFC 0004](../../rfcs/0004-depiction-notes.md)).

**Must not.** Mint, widen, or re-label claims inline; cite sources the
grounding report does not cover; convert a `source_report` into an event.

## Editor

Owns the adjudication pass between draft and review.

**Obligations.**

- Check the artifact against each bound record clause by clause: scope
  respected, label honoured, alternatives represented, excluded territory
  untouched.
- Check the artifact against the publication-side editorial standards (voice,
  terminology, structure, sourcing floors).
- Where artifact and record disagree, the record controls; either the prose
  is fixed or a record revision is proposed to the Researcher — never a
  silent prose-side reinterpretation.
- Decide the projection questions the records leave open (emphasis, ordering,
  what to cut); record them where the pipeline keeps its handoffs.

**Outputs.** The adjudicated artifact plus an editorial report: deviations
found, resolutions chosen, record revisions proposed, open questions
escalated.

**Must not.** Weaken recorded dissent for flow; resolve a founder-gated
question by editorial fiat; approve an artifact whose binding it has not
verified against the current record versions.

## Reviewer

Owns independent verification. Comes to the artifact fresh: reads the bound
records and the artifact, not the Writer's or Editor's reasoning.

**Obligations.**

- Independently re-derive the binding: would a reader reconstruct the claim,
  at its label, at its scope, from this artifact alone?
- Verify citations and locators against sources at their recorded access
  level; verify internal links and cross-references exist.
- Attempt the strongest refutation of the artifact's expression of each
  claim: if the record's alternatives were true, would this artifact read as
  overclaiming?
- Return a structured verdict: pass, mechanical fixes applied, or substantive
  issues for human judgment.

**Outputs.** Verdict report; mechanical fixes at most.

**Must not.** Rewrite prose beyond mechanical fixes; negotiate with the
Editor's reasoning instead of the artifact; pass an artifact whose bound
record is still awaiting founder review.

## Art Director

Owns visual and scenic briefs, under [RFC 0004](../../rfcs/0004-depiction-notes.md).

**Obligations.**

- Ground every brief in depiction notes: reported particulars are rendered
  faithfully or omitted, never contradicted; interpolations used are the
  recorded ones; free dimensions are where the craft lives.
- Treat the image as an unhedgeable assertion: anything ambiguous in the
  notes is resolved toward omission, not invention.
- Where no depiction note exists, draft one (the Researcher obligations apply
  to its Reported layer) and pause for review before rendering.
- Honour every "must not show" entry as a hard constraint.

**Outputs.** Briefs binding depiction notes by id and version; draft
depiction notes where missing.

**Must not.** Render new identifications (a figure as a named individual, a
site as a named place) that no note or claim records; launder a rejected
textual claim into imagery.

## Amending these charters

Charters change by RFC when the change is structural (new role, moved
authority) and by ordinary review when it is clarifying. Workspace tooling
that contradicts a charter is a bug in the tooling.
