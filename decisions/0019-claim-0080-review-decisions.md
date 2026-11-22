---
title: "ADR 0019: Founder decisions on draft woh-claim-0080; standing of chapter 2 of the third book"
status: accepted
date: 2026-11-22
decision_makers:
  - project founder
supersedes: []
superseded_by: null
related_rfcs: []
---

# ADR 0019: Founder decisions on draft woh-claim-0080; standing of chapter 2 of the third book

## Context

`woh-claim-0080`, "The compressed chronology of terrestrial life", was
drafted on 2026-11-22 at founder direction and put to him with four open
decisions. One of them, the standing of chapter 2 of *Let's Welcome the
Extraterrestrials*, had been left open by
[ADR 0018](0018-canon-boundary-dictated-messages.md). Another concerned a
conflict with the scope note added to `woh-claim-0001` the same day by
[ADR 0016](0016-cycle-0001-rulings.md).

## Decision drivers

- ADR 0018: only dictated text is canonical basis.
- A claim record must not cite an author's opinion as canon.

## Options considered

Each decision was put with two to four options, including the status quo.
The chosen ones follow.

## Decision

1. **Wording.** The proposition of `woh-claim-0080` is accepted as drafted:
   the planet is old; all terrestrial life, fossils included, falls within
   roughly the last twenty-five thousand years; the geologic time scale is
   rejected as a chronology of life; the dating of fossils is mistaken;
   mainstream geology rejects this and its case is recorded with the claim.
2. **Standing.** The claim is `derived` from `woh-claim-0001` and
   `woh-claim-0070`. It does not join the foundational claims.
3. **The scope note on `woh-claim-0001`.** Kept and relabelled: Raël, in
   his own commentary (`LWTE-1:15`), allowed that an earlier creation may
   have left older remains. It is his opinion, not canonical basis. The
   source reference changes role from `canonical_basis` to `primary_text`.
   Claim 0001 moves 0.2.1 → 0.2.2 (clarification).
4. **Chapter 2 of the third book.** Words the chapter reports as spoken by
   the Elohim are dictated Message and canon. Raël's narration around them
   is not. This closes the point ADR 0018 left open.

`woh-claim-0080` remains `lifecycle: draft`. Accepting its wording is not
its promotion; that needs the founder's word.

## Consequences

### Enables

- `LWTE-2` may be cited as canonical basis where the Elohim speak, with
  the speaker identified in the locator.
- Claim 0001 no longer cites an opinion as canon.

### Costs and risks

- The `speaker` field in the library's digitization of the third book is
  "Narrator" throughout, so who speaks in chapter 2 has to be read from the
  text until the field is corrected.
- Raël's opinion (earlier creations) and the project's chronology (none)
  now stand side by side in the records. Prose must not present the first
  as the project's position.

## Compatibility and migration

- `model/claims/woh-claim-0001.json`, `model/catalog.json`,
  `docs/framework/elohim-civilization-hypothesis.md`: 0.2.2.
- Pages bound to claim 0001 (16, with translations) need `core_versions`
  set to 0.2.2 when this is merged.
- `woh-claim-0080`: revision triggers and specification updated.

## Validation and review

`python3 scripts/validate.py` passes. Revisit decision 3 if claim 0080 is
not promoted.

## References

- [ADR 0016](0016-cycle-0001-rulings.md), [ADR 0018](0018-canon-boundary-dictated-messages.md)
- `docs/framework/compressed-chronology-of-terrestrial-life.md`
