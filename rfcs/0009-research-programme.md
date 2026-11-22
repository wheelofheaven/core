---
title: "RFC 0009: A research programme of registered expectations"
status: accepted
authors:
  - project founder
  - Claude (drafting agent, at founder direction)
created: 2026-11-22
review_until: null
related_adrs:
  - ../decisions/0016-cycle-0001-rulings.md
  - ../decisions/0017-research-programme-adoption.md
supersedes: []
superseded_by: null
---

# RFC 0009: A research programme of registered expectations

## Review question

Should core adopt a standing research programme in which agents derive
consequences of the foundational claims, register them as expectations
before any source is inspected, have them located blind and contested, and
bring them to the founder for ruling, with ruled expectations as the only
intake for new content?

## Summary

Core can record a claim, map its evidence, review it (RFC 0007) and, if
RFC 0008 is accepted, review claims on a schedule. Each of those
instruments maintains what the project already asserts. None of them
produces new insight, and the founder's request of 2026-11-22 is for
exactly that: a way, native to agent work, of taking a core set of premises
as possibly true and pushing them further.

This RFC proposes:

1. a **kernel**: the accepted claims marked `foundational`, read from the
   records, which research takes as given;
2. the **expectation** as a first-class record: one consequence of a claim,
   with its target, a neutral question, hit and miss criteria, and what
   each alternative predicts, registered by commit before anyone looks;
3. a **five-stage cycle** with separated roles: Deriver, Locator, Recorder,
   Critic, and the founder as the only one who rules;
4. a **scoreboard** that counts hits and misses by whether the expectation
   discriminated between the claim and its alternatives and whether its
   target was new to the project's records;
5. a **content rule**: only ruled expectations become article seeds, wiki
   revisions, dataset rows or claim reviews.

The operating text is
[docs/methodology/research-programme.md](../docs/methodology/research-programme.md).
A first cycle on `woh-claim-0001` accompanies this RFC as its test.

## Problem and scope

**The gap.** `model/` holds 79 accepted claims. Four are `foundational`
(`woh-claim-0001`, `0003`, `0023`, `0070`); `0001` alone has 38 dependents.
Nothing states that these are the premises research starts from, and
nothing records what they lead one to expect. New lines of inquiry arise
in conversation and live in dossier prose under `docs/research/`.

**Why agent work makes this urgent.** An agent asked to find support for a
thesis returns support. On 2026-11-20 the founder rejected a synthesis
linking his reading on artificial intelligence to the canon: the thesis was
the drafting agent's own, and the quotation it rested on was never found.
The inverse case is ADR 0015, where re-reading the canon passage itself
showed that `woh-claim-0010` contradicted it. In both cases the passage
decided the matter. A research method for agents has to make the passage
arrive before the thesis, by construction and without relying on good
intentions.

**Scope.** Accepted claims and what follows from them; the expectation
register; the cycle and its roles; the path from ruling to content. Out of
scope: the truth of any kernel claim, RFC 0007's rule for advancing
`evidence_status`, public prose, and the translation programme.

## Claim kinds and evidence

The programme asks different things of different claim kinds, and an
expectation's `kind` records which sort of contact it makes:

- **Canon expectations** test what the canonical books say, voice by voice.
  A hit establishes a `source_report`. It says nothing about events.
- **Primary-text and philological expectations** test what an ancient text
  or its language shows in a named edition. A hit is an observation about a
  text, to be read against what the alternatives also predict.
- **Historical and scientific expectations** test dated statements against
  the record or the literature. A hit shows compatibility or anticipation.
  It does not show that the reported events occurred.
- **Dataset expectations** test cells against named editions.

The evidence map of `woh-claim-0001` already observes that its biblical
rows become evidence for the hypothesis only after the framework
identification is granted, and that parallels do not accumulate into
confirmation. The programme takes that seriously through the
`discrimination` field: an expectation every alternative shares is
recorded as such and cannot count as progress.

The method borrows from Lakatos's account of research programmes (a hard
core held fixed, judged over time by whether it keeps predicting facts not
already in hand) only as an organizing analogy. A programme can be
productive in that sense and its core still be false.

## Detailed proposal

### 1. The kernel

The kernel is every claim with `lifecycle: accepted` and
`framework_relation: foundational`, printed by
`scripts/research/programme.py kernel`. No separate list exists, so the
kernel cannot drift from the records. Research under the programme assumes
the kernel for the purpose of derivation. Whether a premise belongs in the
kernel is decided where it always was: by a claim record's
`framework_relation`, changed by RFC and ADR.

One such decision is already open. Whether the canon's position on
macroevolution is a foundational premise or a scientific layer to be kept
in its own voice determines whether expectations may be derived from it.
This RFC does not decide it.

### 2. Expectation records

`model/expectations/woh-exp-NNNN.json`, schema
`model/schemas/expectation.schema.json`, checked by `scripts/validate.py`.
Identifiers are sequential and never reused. The fields and their purposes
are set out in the methodology document. Three rules carry the design:

- **Registration is a commit.** Locating begins only after the commit that
  adds the records. A record is not edited afterwards except to add its
  finding, assessment, contest, ruling and outputs. A mistaken expectation
  is `withdrawn` and kept.
- **The question is neutral and separate.** The Deriver writes a `question`
  that someone ignorant of the expectation could answer, and `criteria`
  that fix in advance what counts as hit and miss. The Locator receives the
  question, target and protocol through `programme.py brief` and nothing
  else.
- **Rivals are stated.** For each alternative on the claim record the
  Deriver records whether it predicts the same result, a different one, or
  nothing. The validator refuses a `partial` or `strong` discrimination
  that names no differing rival.

### 3. The cycle

Derive, Locate, Assess, Contest, Rule, as specified in the methodology
document, with one role per stage and role charters there. A cycle's files
live in `docs/research/programme/cycle-NNNN/`. The founder reads one
digest and rules each expectation `hit`, `miss`, `narrowed`, `open` or
`void`. The validator rejects a ruling not attributed to the founder.

### 4. Intake

Expectations arise from four kinds of work: derivation from a kernel
claim; exhaustive sweeps of a corpus that tag what bears on which claim;
cell-level dataset audits; and a watch on new literature. All four end in
the same place, a registered expectation. If RFC 0008 is accepted, its
insight log and contact-point register become intake for this register:
an insight is a candidate question, a contact point is where expectations
with a definite answer are found.

### 5. Output

A ruled `hit` with its passage in hand may seed an article, a wiki
revision or a dataset row, produced under RFC 0003. A `miss` or `narrowed`
ruling may open a claim review under RFC 0007. The record's `outputs`
field lists what followed. Rulings do not alter claims; reviews and ADRs
do.

### 6. Measure

`programme.py status` prints rulings in four classes by discrimination and
novelty. The programme's yield is the number of hits against misses among
expectations that were both discriminating and unrecorded. The other
classes are reported and are not counted as progress.

### 7. Cadence

One research cycle a month, alongside the fortnightly review cycle RFC
0008 proposes and the dataset releases. The founder's cost is one digest
and about ten rulings per cycle.

## Alternatives

- **Status quo.** Research questions arise in sessions and are pursued as
  dossiers. Flexible, and it produced the 2026-11 dataset corrections. It
  has no register, keeps no misses, and allowed the 2026-11-20 synthesis.
- **Extend RFC 0008 only.** Treat the insight log as sufficient. The log
  holds candidate readings but fixes no criteria in advance and does not
  separate the one who hopes from the one who looks.
- **Open-ended agent exploration.** Let agents range over the corpus and
  report what they find interesting. This yields volume, and every item
  arrives as a confident narrative with no way to tell a finding from a
  fit.
- **Adversarial review alone.** Keep free-form research and add a critic
  at the end. Cheaper, but the critic then argues against a finished
  synthesis, and selective reporting upstream stays invisible.
- **Formal external pre-registration.** Register expectations with a
  public registry. Stronger against the charge of after-the-fact editing,
  disproportionate for textual research, and git history already gives a
  dated, public order of events.

## Risks, limitations, and dissent

- **Prior knowledge.** Language models have read the famous texts. An
  agent deriving an expectation about Genesis already knows roughly what
  Genesis says, so registration guards against selective reporting and
  does not make the expectation a prediction in the strict sense. The
  `prior_knowledge` field records this per expectation; expectations about
  obscure editions, datasets and passages the project has never opened are
  worth more for that reason.
- **Blindness is partial.** A Locator working in this workspace knows it is
  working for Wheel of Heaven and can guess the hoped answer. The brief
  withholds the criteria; it cannot withhold the context.
- **The scoreboard can be gamed.** Easy expectations raise the hit count.
  The discrimination and novelty classes exist to expose that, and the
  Critic may recommend `void`. A scoreboard that shows only hits after
  several cycles is evidence that the Deriver is choosing safe targets.
- **Yield is not truth.** Hits on canon expectations show that the canon is
  coherent or that the project reads it correctly. Hits on textual
  expectations show what texts contain. Neither converts a `source_report`
  into an event, and the scoreboard must never be quoted as a likelihood
  that the hypothesis is true.
- **One ruler.** The founder alone rules, and the founder holds the
  framework. The contest file is written for an outside reader as well, and
  findings and contests stay in the repository whatever the ruling.
- **Dissent worth recording.** A critic could say that holding the kernel
  fixed is the very thing a sceptic disputes, and that no number of derived
  hits addresses the source-critical alternative to `woh-claim-0001`. That
  is correct. The programme is a way of working out and checking what the
  framework implies. The load-bearing question about the contact report
  itself stays with the review of `woh-claim-0070` and `0001`.
- **Cost.** A cycle of ten expectations uses on the order of ten agent
  runs and one founder session.

## Compatibility and migration

Additive. New: `model/expectations/`, `model/schemas/expectation.schema.json`,
`scripts/research/programme.py`, `docs/methodology/research-programme.md`,
`docs/research/programme/`, validator checks for expectation records, and
glossary terms. No claim record, identifier, schema or public page changes.
Existing dossiers under `docs/research/` stay as they are; questions in
them may be registered as expectations when taken up.

## Validation plan

Before a decision: the pilot cycle on `woh-claim-0001`
([cycle-0001](../docs/research/programme/cycle-0001/README.md)), judged by
whether the founder could rule each expectation from the digest alone,
whether any Locator finding surprised the Deriver, and whether the Critic
changed any assessment.

After three cycles: how many expectations fell in the progress class; the
hit and miss counts there; how many rulings produced an output; how many
misses opened a review. If no cycle produces a miss, or none produces an
output, the method is not working and this RFC should be revised or
withdrawn.

### Pilot result (2026-11-22)

The pilot ran through the Contest stage; its
[digest](../docs/research/programme/cycle-0001/README.md) awaits rulings.
It produced no hit among discriminating expectations. The Critics changed
five of ten mechanical assessments, and the most useful results were
passages found as by-products of reading whole books against a neutral
question. The digest lists what failed in the method (overstated
discrimination at registration, a test design that could only discriminate
by failing, divergent inclusion rules within a family, no claim for
canon-consistency work to attach to) and the amendments it suggests. They
were adopted with the RFC.

## Resolution

Accepted 2026-11-22 with the five amendments from the pilot:
[ADR 0017](../decisions/0017-research-programme-adoption.md).
