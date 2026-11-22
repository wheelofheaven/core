---
title: "ADR 0018: The canon is the dictated Messages; commentary and signed contributions in the third book are not canon"
status: accepted
date: 2026-11-22
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs: []
---

# ADR 0018: The canon is the dictated Messages; commentary and signed contributions in the third book are not canon

## Context

*Let's Welcome the Extraterrestrials* (1979) prints three kinds of text:
Raël's own answers to readers' questions and his essays (chapters 1 and
3), a narrated further encounter (chapter 2), and signed contributions by
other Raëlians (chapter 4, including Marcel Terrusse's essay).

Two earlier decisions gave Raël's commentary canonical standing:
[ADR 0013](0013-wiki-batch-2026-11-promotions.md), decision 4 ("Raël's own
commentary voice … is canon, and every use labels it as his commentary"),
and [ADR 0014](0014-canon-consistency-rulings-2026-11.md), decision 2
(`LWTE-1:28–31` "registered as the canon's commentary layer").
`woh-claim-0071` names the standing of signed contributions as an open
question for the founder and lists it as a revision trigger.

On 2026-11-22, while scoping a claim on the chronology of terrestrial
life, the founder ruled: "Terrusse's essay (LWTE-4:31–37) is not canon,
and I don't think anyone's opinion in LWTE should be considered
canonical." Asked how far that goes, he chose: Raël's opinions are out
too; only the dictated Messages are canon.

## Decision drivers

- The foundational canon should be what the source presents as dictated,
  not what its recipient or his followers think about it.
- Claims that cite an opinion as canonical basis state more than the canon
  carries.

## Options considered

### Option A — only chapter 4 is out

Signed contributions by others carry no canonical weight; Raël's
commentary stays canon, labelled. Keeps ADR 0013 decision 4.

### Option B — Raël's opinions are out too

Only the dictated Messages are canon. Raël's commentary becomes the
author's own view.

### Option C — dictation inside the third book stays, the rest is out

Chapter 2 keeps canonical standing; chapters 1, 3 and 4 do not.

## Decision

Option B.

1. **The canon is the dictated Messages.** Raël's commentary in *Let's
   Welcome the Extraterrestrials* (his answers to questions and his
   essays) is the author's own view. It is a primary source for what Raël
   thought and may be cited as such, labelled as his opinion. It is not
   canonical basis.
2. **Signed contributions by others** printed in that book (chapter 4,
   Terrusse's essay in particular) carry no canonical weight.
3. This supersedes decision 4 of ADR 0013 and the words "the canon's
   commentary layer" in decision 2 of ADR 0014. The rest of both ADRs
   stands.

**Not decided here:** whether the narrated encounter in chapter 2 of the
third book, where it reports words of the Elohim, counts as dictated
Message. Option C would have said yes and was not chosen; Option B's
wording does not say no. Until the founder rules, records should not cite
`LWTE-2` as canonical basis without flagging this.

**Recorded only.** At the founder's direction this ADR states the ruling
and lists what it touches. No claim record, evidence map or public page is
changed by it.

## Consequences

### Enables

- A clear test for `canonical_basis`: is the passage dictated?
- The chronology of terrestrial life can be stated from the dictated text
  (`TBWTT-2:5–16`, `TBWTT-5:62–64`, `ETTMTTP-2:43`) without the commentary's
  qualification about earlier creations.

### Costs and risks

- Records that cite the third book as canonical basis are now out of step
  with this ruling until reviewed (list below).
- Raël's replies on dating methods and early continental drift
  (`LWTE-1:28–31`) can no longer be called canon. They remain usable as his
  commentary.

## Compatibility and migration

Records and decisions to review against this ruling, none changed here:

- `woh-claim-0071` (continental breakup at the Flood): its own revision
  trigger applies. The canonical layer narrows to the message text; the
  breakup-and-burial reading (Terrusse) and the dating commentary
  (`LWTE-1:28–31`) move to the corpus layer.
- `woh-claim-0001` 0.2.1 and [ADR 0016](0016-cycle-0001-rulings.md): the
  scope note added on 2026-11-22 cites `LWTE-1:14–15` with role
  `canonical_basis`. That passage is Raël's commentary. The note and the
  ruling on `woh-exp-0008` (which also rests on `LWTE-1:107`) need
  revisiting.
- `woh-claim-0074`, `0076`, `0077` and `0038` cite `LWTE-1` or `LWTE-3`
  (for example Joseph Smith "named by Raël among the envoys", `LWTE-3:27`).
- `source-notes/lets-welcome-the-extraterrestrials.md` should state the
  standing of each chapter.
- Workspace editorial rules that describe Raël's commentary voice as canon.
- Public pages that present the breakup at the Flood, or any statement
  from the third book's commentary, as canonical.

## Validation and review

`python3 scripts/validate.py` passes. A review of the listed records
should follow; each change to a claim goes through its own ADR.

## References

- [ADR 0013](0013-wiki-batch-2026-11-promotions.md), decision 4
- [ADR 0014](0014-canon-consistency-rulings-2026-11.md), decision 2
- [ADR 0016](0016-cycle-0001-rulings.md)
- `model/claims/woh-claim-0071.json`, revision triggers
