---
title: Research programme
status: accepted
version: 0.2.0
last_reviewed: 2026-11-22
---

# Research programme

How Wheel of Heaven generates new research from its foundational claims.
Proposed by [RFC 0009](../../rfcs/0009-research-programme.md) and adopted
by [ADR 0017](../../decisions/0017-research-programme-adoption.md). The charters are harness-agnostic, like the
[production roles](production-roles.md): they define obligations and
outputs. Orchestration wiring (skills, subagent definitions) lives in the
workspace and must point back here.

Every role inherits the [epistemic principles](../foundations/epistemic-principles.md)
and [`CLAUDE.md`](../../CLAUDE.md) in full.

## The kernel

The **kernel** is the set of `accepted` claims whose `framework_relation` is
`foundational`. It is read from the records, never listed by hand:

```
python3 scripts/research/programme.py kernel
```

Research under this programme takes the kernel as given and asks what
follows from it. A cycle does not rule on a kernel claim. It rules on
**expectations** derived from one. Changing a kernel claim, or adding one,
remains a founder decision by RFC and ADR.

## The expectation

An **expectation** is one consequence of a claim, written down before
anyone looks: *if the claim holds, a named source should show a stated
thing*. It is a record under `model/expectations/woh-exp-NNNN.json`,
validated by `model/schemas/expectation.schema.json`. Its parts:

| Part | Purpose |
| --- | --- |
| `statement`, `derivation` | What is expected and why it follows from the claim at the stated version |
| `target` | The source, edition or dataset and the locator scope to be inspected |
| `question`, `protocol` | A neutral question and search procedure. This is all the Locator receives |
| `criteria` | What counts as hit, miss and partial, fixed at registration |
| `rivals`, `discrimination` | What each recorded alternative predicts for the same target |
| `novelty`, `prior_knowledge` | Whether core already records the target for this claim, and what the Deriver already knew |

Two properties decide whether a result can count as progress.

**Discrimination.** For each alternative on the claim record, the Deriver
states whether it predicts the `same` result, a `different` one, or is
`silent` (it commits to nothing about this target). If no alternative
predicts a different result, `discrimination` is `none`: the expectation may still be worth checking, but a hit favours
nothing. Plural verbs in Genesis 1:26 are expected by the framework reading
and by the divine-council reading alike.

**Novelty.** `retrodiction` means core already records the target, under
this claim or any other claim, evidence map or research dossier; the
expectation restates known ground. `unrecorded` means no core record
does. Agents carry general knowledge of famous texts, so `unrecorded` is a
statement about the project's records, and the Deriver must say in
`prior_knowledge` what it already believes the target contains.
Registration prevents selective reporting. It cannot prevent prior
knowledge.

**Auxiliary assumptions.** Where the derivation needs a premise the claim
record does not state, the Deriver lists it in `auxiliary_assumptions`.
A miss on such an expectation may count against the added premise and
leave the claim untouched, so the scoreboard reports these apart.

**Families.** Expectations that apply one test to several targets are not
independent. They share a `family` id, are located by one Locator under one
inclusion rule, and are read as one result with several instances. The
scoreboard counts a family once.

**Scoring.** Every expectation is `scored` unless registered otherwise. A
`control` calibrates the Locator and Critic: it has `discrimination: none`
by construction and is reported apart. A `source_report` expectation tests
what a source says where no claim's scope covers it (for example the
consistency of the canonical books with one another); it is reported apart
and its result feeds source notes and future claims.

**A favouring result.** An expectation counts as discriminating only if
its criteria name a result that would favour the claim over at least one
rival *as the protocol measures it*. A test whose only discriminating
outcome is its own failure (every rival predicts the hit; one predicts the
miss) is registered with `discrimination: none`, or redesigned.

## The cycle

One cycle takes one claim and about ten expectations through five stages.
Each stage has one role and stops at its output.

| Stage | Role | Sees | Produces |
| --- | --- | --- | --- |
| 1. Derive | Deriver | Claim record, specification, evidence map, prior research | Expectation records, `status: registered`, committed before stage 2 |
| 2. Locate | Locator | `question`, `target`, `protocol` only | A finding file with locators, quotations, access level and an answer to the question |
| 3. Assess | Recorder | Record and finding | `assessment`: the registered criteria applied mechanically |
| 4. Contest | Critic | Record, finding, assessment | A contest file: the strongest case that the result means less than it seems, or that a miss was unfairly scored |
| 5. Rule | Founder | Cycle digest | `ruling`: `hit`, `miss`, `narrowed`, `open` or `void` |

**Pre-registration check.** Before the registration commit, an agent that
did not derive the set reads each draft record and answers three
questions: does any rival marked `different` really predict a different
result on this target, as the protocol measures it; does the `question` or
`protocol` let the hoped answer show; and is the selection rule tight
enough that two Locators would select the same cases. Records that fail
are revised or dropped before registration, and the check is noted in the
cycle README.

Registration is a commit. The Locate stage starts only after the commit
that registers the expectations exists, so git history shows the order.
Records are not edited after registration except to add `finding`,
`assessment`, `contest`, `ruling` and `outputs`. A mistaken expectation is
`withdrawn` with a reason and stays in the register. Two annotations may also be added later, because they classify the record without changing what was registered: `family` and `scoring`. The fields that fix what was expected (`statement`, `derivation`, `target`, `question`, `protocol`, `criteria`, `rivals`, `discrimination`, `novelty`) never change.

Files for a cycle live in `docs/research/programme/cycle-NNNN/`: a
`README.md` digest for the founder, and one `woh-exp-NNNN-finding.md` and
`woh-exp-NNNN-contest.md` per expectation.

### Rulings

| Outcome | Meaning |
| --- | --- |
| `hit` | The target shows what the registered criteria required |
| `miss` | The target was inspected and does not show it |
| `narrowed` | The result holds only in a narrower form than registered; the note states the form |
| `open` | The target could not be inspected adequately, or the result is genuinely mixed |
| `void` | The expectation was badly formed (criteria ambiguous, target already inspected by the Deriver, derivation does not follow) |

A miss is a finding. It may point to a claim that states more than its
sources carry, as with `woh-claim-0010` in ADR 0015, and then it feeds a
review under RFC 0007. When the founder accepts a Critic's downgrade, the ruling records the
accepted `discrimination`; the registered value stays as it was, and the
scoreboard uses the ruled one. Rulings never change a claim's `evidence_status`,
`lifecycle` or statement by themselves.

## Where expectations come from

1. **Derivation.** A Deriver works out consequences of a kernel claim or of
   a claim that depends on one.
2. **Sweeps.** An exhaustive pass over a corpus (every passage of a
   canonical book, every row of a dataset) tags what bears on which claim.
   Sweep output is a list of candidate questions, each of which becomes an
   expectation only by registration.
3. **Audits.** Cell-level dataset audits against named editions, as in the
   flood concordance and Divine Council Index.
4. **Literature watch.** New publications checked against the points where
   claims meet checkable evidence.

Whatever the intake, nothing is scored that was not registered first.

## From rulings to content

Only ruled expectations feed production. A `hit` with its passage in hand
may become an article seed, a wiki revision or a dataset row, entered in
the record's `outputs` and produced through the
[artifact derivation contract](../../rfcs/0003-artifact-derivation-contract.md).
A `miss` or `narrowed` ruling may become a claim review. No synthesis is
drafted on an expectation that is still `registered`, `located` or
`contested`.

## The scoreboard

```
python3 scripts/research/programme.py status
```

prints rulings by discrimination and novelty, counting each family once
and reporting controls and source-report expectations apart. The figure
that measures
whether the programme is finding anything is the count of ruled `hit`s
that are both `unrecorded` and discriminating, set beside the misses in
the same class. Hits with `discrimination: none` are reported separately
and are not progress. The scoreboard measures the programme's yield. It is
not a probability that any claim is true, and it must never be quoted as
one.

## Role charters

### Deriver

**Obligations.**

- Read the claim record, its controlling specification, its evidence map
  and the research dossiers that already bear on it before deriving
  anything.
- Derive consequences that follow from the claim at its recorded version
  and scope. An expectation resting on something the claim excludes belongs
  to another claim.
- Name a target that can actually be inspected: a project holding, a
  registered source with known access, or a public edition. Record the
  expected access level.
- Write the `question` so that someone ignorant of the expectation could
  answer it and so that either answer is reportable. Write `criteria`
  before any inspection.
- State what each recorded alternative predicts, at its strength, on this
  target as the protocol measures it. Where none differs, set
  `discrimination: none` and say so. Where the only result that would
  separate the claim from a rival is the expectation's own miss, the
  expectation does not discriminate in the claim's favour: say so, and
  redesign it or register it as `none`.
- Give a `family` id to expectations that apply one test to several
  targets, and register controls and source-report work with the matching
  `scoring`.
- Make the selection rule explicit: which passages count as commentary on
  a quotation (before as well as after), what is in and out of scope, and
  how borderline cases are decided.
- Declare prior knowledge of the target candidly.

**Must not.** Open the target passage while deriving; register an
expectation whose hit criterion any result would satisfy; draft claims,
theses or article pitches; tune a target's scope around a known
counter-example.

### Locator

**Obligations.**

- Work only from the brief printed by
  `python3 scripts/research/programme.py brief woh-exp-NNNN`.
- Follow the protocol. Quote the source in the edition inspected, with
  locators, and record the access level actually achieved.
- Report what is there, what is absent, and what is ambiguous. "Not found"
  and "could not access" are complete answers.
- Report anything adjacent that a careful reader would want to know, kept
  apart from the answer.

**Must not.** Read the expectation record, the claim's evidence map or
other findings; judge whether the result helps or harms the framework;
paraphrase where quotation is possible; cite a passage from memory.

### Recorder

**Obligations.**

- Apply the registered criteria to the finding and enter `assessment`:
  `meets_hit`, `meets_partial`, `meets_miss`, or `inaccessible`. Where the
  criteria do not settle it, enter `mixed`.
- Write the cycle digest: per expectation, the question, the quotation or
  datum, the assessment, the Critic's objection, and what a ruling either
  way would touch.
- Keep the register and the files consistent; run the validator.

**Must not.** Reinterpret criteria after seeing the finding; enter a
ruling; soften the Critic's case in the digest.

### Critic

**Obligations.**

- For an assessment of `meets_hit`: argue that the finding is weaker than
  it looks. Check the quotation against its context, test whether an
  alternative predicts the same result after all, and check independence
  from sources already counted.
- For `meets_miss`: argue whether the expectation was fairly formed and the
  search adequate, without rescuing it by reinterpretation.
- Verify the Locator's quotations and locators against the source.
- Recommend `sustain`, `downgrade` or `void` with reasons.

**Must not.** Defer to the framework reading or to the Deriver's reasoning;
introduce an alternative without stating it in a form its proponents would
accept.

### Founder gate

Only the founder rules. An unruled expectation has no outcome, whatever its
assessment. Claim changes that follow from rulings go through an ADR.

## Amending this document

Structural changes (a new role, a new ruling outcome, a change to what the
Locator sees) go through an RFC. Clarifications go through ordinary review.
