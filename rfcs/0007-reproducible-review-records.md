---
title: "RFC 0007: Reproducible review records"
status: accepted
authors:
  - project founder
  - Claude (drafting agent, at founder direction)
created: 2026-08-31
review_until: null
related_adrs:
  - ../decisions/0009-reproducible-review-records.md
supersedes: []
superseded_by: null
---

# RFC 0007: Reproducible review records

## Review question

Should the core adopt a review-record artifact — a dated, per-claim document
carrying protocol, screening, extraction, appraisal, limitations, and reviewer
sign-off — as the only instrument that may move a claim's `evidence_status`
beyond `scoped`, and should `claim.schema.json` gain a field binding a claim to
its reviews?

## Summary

[`docs/methodology/evidence-status.md`](../docs/methodology/evidence-status.md)
already states the advancement rule: a claim moves beyond `scoped` only with a
documented search protocol, inclusion criteria, extraction record, appraisal,
limitations, and dated reviewer sign-off. It defines that requirement in prose
and stops there. No artifact carries it, no directory holds it, and no field
links a claim to it.

The consequence is visible in the catalog. Seventy claims are accepted; every
one of them still carries `scoped`; none has ever reached `reviewed`, because
the instrument that would take it there does not exist. Stage 4 of the
[roadmap](../ROADMAP.md) is blocked on a missing file format.

This RFC proposes the smallest artifact that discharges the existing rule. It
adds no new epistemic vocabulary and changes no existing status meaning. It
proposes:

1. a `docs/reviews/` directory holding one record per completed review;
2. a required section structure mirroring the `evidence-status` minimum record;
3. an optional `reviews` array on the claim schema, binding a claim to the
   records that reviewed it;
4. a feedback rule requiring a review to declare the sources it needed as
   `source_references`, so the acquisition wantlist sees them.

A first record drafted against this format accompanies the RFC as
[`woh-claim-0070-review-0001`](../docs/reviews/woh-claim-0070-review-0001.md).
It is a worked example, not a ratified review: it is unsigned, and the claim it
examines has not moved.

## Problem and scope

**In scope.** The artifact format; its directory and naming; the schema
binding; the rule connecting a review to `evidence_status`; the feedback rule
into `source_references`.

**Not in scope.** Changing the `evidence_status` vocabulary or the meaning of
any status. Changing who may sign off — that authority stays with the founder.
Advancing any specific claim, including 0070. Review *methodology* for a given
discipline (philology, archaeoastronomy, comparative method), which belongs to
question-specific protocols under `docs/research/`.

**The current gap, precisely.** Three things are missing and this RFC supplies
all three:

- *No artifact.* The minimum record is specified in a table cell.
- *No binding.* `claim.schema.json` sets `additionalProperties: false` and has
  no field pointing at review evidence, so even a hand-written review would be
  unreachable from the record it reviews.
- *No feedback path.* `scripts/wantlist.py` derives acquisition needs from
  `source_references`. A claim whose review requires a critical source it does
  not cite reports as unblocked while being, in fact, blocked. Claim 0070 is
  exactly this case: its evidence map names a source-critical appraisal as a
  review component, the claim cites only its own canonical basis, and the
  wantlist therefore does not list 0070 against the critical literature it
  needs.

## Claim kinds and evidence

This RFC is a **normative recommendation** about repository process. It makes
no assertion about the world, the canon, or any tradition, and it does not
license any change to a claim's substance.

One **observation** motivates it, and is independently checkable: of the 70
accepted claims in `model/claims/`, 11 carry `evidence_status: ["scoped"]` and
59 carry `["scoped", "contested"]`. Every claim in the catalog still sits at
`scoped`; none has ever reached `reviewed`. (`contested` is an orthogonal flag,
not a rung above `scoped` — a claim may be both `reviewed` and `contested`.)

The proposal deliberately does **not** make review outcomes self-executing. A
review record reports findings; a founder's dated sign-off, recorded in an ADR,
is what moves a status. Keeping those separate is what prevents an agent from
promoting a claim by writing a confident document — the failure mode
[`CLAUDE.md`](../CLAUDE.md) forbids.

## Detailed proposal

### Location and naming

Review records live in `docs/reviews/`, named:

```
docs/reviews/woh-claim-NNNN-review-MMMM.md
```

`NNNN` is the claim ID; `MMMM` is a per-claim sequence starting at `0001`. A
claim may accumulate several reviews over time. Records are append-only: a
signed record is never edited to reflect a later view. A superseding review
gets the next sequence number and links back.

### Frontmatter

```yaml
---
title: "Review: <claim title>"
claim_id: woh-claim-0070
review_id: woh-claim-0070-review-0001
status: draft            # draft | signed | superseded
components_complete: []  # the review components actually performed
components_outstanding: []
recommended_status: null # the reviewer's recommendation; not self-executing
signed_by: null
signed_date: null
supersedes: null
---
```

`status: signed` may only be set together with `signed_by` and `signed_date`.
The validator enforces this pairing.

### Required sections

The section list is the `evidence-status` minimum record, made concrete. Each
is required; a section with nothing to report says so explicitly rather than
being omitted.

| Section | Carries |
| --- | --- |
| Question | The exact proposition reviewed, quoted from the claim record |
| Protocol | What was searched, in which representations, by what procedure, and what would have counted as a disconfirming result |
| Screening | What was examined and what was excluded, with the reason |
| Extraction | The findings themselves, at passage level, with locators |
| Appraisal | What the findings mean for the claim, including for its declared alternatives |
| Limitations | What the review could not reach, and what that leaves open |
| Outcome | What the reviewer recommends, and what must change in which files |
| Sign-off | Reviewer, date, and the status granted — blank until signed |

**Reproducibility requirement.** Protocol must be specific enough for a second
reviewer to repeat the procedure and get the same result. Where a review used a
script, the script is included or referenced. Where it used a page image or a
printed edition, the edition and page are named. "Read the source carefully" is
not a protocol.

### Schema binding

Add an optional `reviews` array to `claim.schema.json`:

```json
"reviews": {
  "type": "array",
  "items": {
    "type": "object",
    "additionalProperties": false,
    "required": ["review_id", "path", "status"],
    "properties": {
      "review_id": { "type": "string" },
      "path":      { "type": "string" },
      "status":    { "enum": ["draft", "signed", "superseded"] },
      "components_outstanding": {
        "type": "array", "items": { "type": "string" }
      }
    }
  }
}
```

Because the schema sets `additionalProperties: false`, adding the field is a
compatibility change: `schema_version` goes `0.1.0` → `0.2.0`. The field is
optional, so all 70 existing records stay valid and need no migration.

### The advancement rule, restated

A claim may carry `evidence_status` beyond `scoped` only if it references a
review record whose `status` is `signed` and whose `recommended_status`
supports the change. The validator enforces the mechanical half — that the
referenced record exists, is signed, and covers the claim. It cannot enforce
the judgement, which is the point of requiring a human signature.

A review whose components are not all complete may still be signed, provided
`components_outstanding` is non-empty and the record says what remains. Such a
review may record findings and force corrections without advancing the status.
This RFC expects that to be the common case early on.

### Feedback into source references

If a review establishes that a claim needs a source the claim does not cite,
the review's Outcome section must require adding that source to the claim's
`source_references` with the appropriate `role` and an honest `access` level.
This closes the wantlist gap described above: acquisition need becomes visible
to tooling instead of living only in prose.

## Alternatives

**Status quo — leave the rule in prose.** No new format; reviewers write what
seems right. Rejected: it is the current state, and the current state is that
no claim has ever advanced. The rule as prose has produced zero reviews in the
life of the repository.

**Put the review inside the evidence map.** Evidence maps already exist per
claim, so the review could be a section there. Rejected: evidence maps are
living documents that get rewritten as understanding changes, while a review is
an event with a date and a signature. Mixing an append-only record into a
mutable one loses the audit trail that makes `reviewed` mean anything. The two
should link, not merge.

**Make the record machine-readable (JSON) rather than Markdown.** Rejected for
now: the substance of a review is argument and qualification, which JSON
carries badly. The frontmatter gives tooling the fields it needs. This can be
revisited if review records ever need to be queried in bulk.

**Let a signed review advance the status automatically.** Rejected: it would
let a drafting agent move a claim by producing a document, which is exactly the
authority `CLAUDE.md` reserves to the founder. The separation is deliberate
friction.

## Risks, limitations, and dissent

**The format could become ceremony.** A required eight-section document is
heavy for a small correction. Mitigation: the format is required only for
records that bear on `evidence_status`. A typo fix in a source note remains a
commit, not a review. If the ceremony proves to deter reviews rather than
enable them, that is grounds to revisit — a format nobody uses is worse than
prose.

**Partial reviews could be read as full ones.** A record with outstanding
components still looks authoritative. Mitigation: `components_outstanding` is
frontmatter, not a footnote, and the validator refuses a status advance whose
supporting review leaves a component outstanding without explicit founder
override in the ADR.

**Sign-off concentrates on one person.** Every advance requires the founder.
This is a real bottleneck and is accepted deliberately: the alternative is
automated epistemic promotion, which the project exists to avoid.

**A review can be wrong.** Nothing here makes a signed review correct. The
append-only sequence and the supersession link are the remedy: a later review
supersedes an earlier one and both stay readable.

## Compatibility and migration

- **Identifiers:** no existing identifier changes meaning. `review_id` is a new
  namespace.
- **Schema:** `claim.schema.json` `schema_version` `0.1.0` → `0.2.0`; new field
  is optional; all 70 existing records remain valid; no data migration.
- **Validator:** `scripts/validate.py` gains checks for review-record
  existence, the signed/`signed_by`/`signed_date` pairing, and the advancement
  rule. Until this RFC is accepted the checks are not added.
- **Public pages, translations, APIs:** no effect. Review records are internal
  research apparatus and expose no reader-facing surface. Nothing in
  `data-content` renders them, and no public badge changes.
- **History:** existing evidence maps are unaffected and keep their role.

## Validation plan

**Before a decision.** Confirm the format is sufficient by drafting one real
record against it — done, as
[`woh-claim-0070-review-0001`](../docs/reviews/woh-claim-0070-review-0001.md).
That draft did surface format pressure and the format above reflects it: an
`Outcome` section was added when the 0070 review produced required corrections
that belonged in neither `Appraisal` nor `Limitations`.

**After a decision, before the schema lands.** Run `mise run check` with the
new validator rules against the full catalog and confirm all 70 records still
validate.

**Ongoing.** The first signed record with a status advance is the real test of
the advancement rule. It should be reviewed as a process question after it
happens, not assumed to have worked.

## Resolution

**Accepted** 2026-08-31 by the founder, recorded in
[ADR 0009](../decisions/0009-reproducible-review-records.md). The schema field,
the validator rules, and the feedback rule are implemented.

No claim status changed on the RFC's account. `woh-claim-0070` remains
`scoped`: its review is unsigned and one component is outstanding.
