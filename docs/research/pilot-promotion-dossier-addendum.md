---
title: "Pilot promotion dossier — addendum: the claim 0001 split and woh-claim-0070"
status: accepted
version: 0.1.0
last_reviewed: 2026-08-17
---

# Pilot promotion dossier — addendum: the claim 0001 split and woh-claim-0070

## Purpose

The review dossier for promoting the pilot claims 0001–0004 from `draft` to
`accepted` was presented to the founder on 2026-08-16 and was not acted on
before the record set changed. On 2026-08-17 the founder adopted option 3 of
[the claim 0001 decomposition question](decompose-claim-0001.md), executed
as [RFC 0006](../../rfcs/0006-split-canonical-contact-report.md) and
[ADR 0007](../../decisions/0007-split-canonical-contact-report.md). This
addendum records what that changes for the promotion decision, so the
founder can ratify the set in one pass without re-reviewing what did not
change.

The addendum is decision support. It promotes nothing by itself; promotion
of a draft claim requires explicit founder direction.

## What changed since the dossier was presented

- **`woh-claim-0070` "The canonical contact report" now exists** — a
  `source_report` (framework relation `foundational`, public label
  `direct`, lifecycle `draft`) extracted from claim 0001's report layer.
  Record: [`woh-claim-0070.json`](../../model/claims/woh-claim-0070.json);
  specification:
  [canonical-contact-report.md](../framework/canonical-contact-report.md);
  evidence map:
  [woh-claim-0070-evidence.md](../evidence/woh-claim-0070-evidence.md)
  (carrying the two subclaim-A rows moved out of claim 0001's map).
- **`woh-claim-0001` moved 0.1.0 → 0.2.0.** The statement is unchanged; the
  record gained a dependency on `woh-claim-0070`, excludes the report layer
  from scope, and carries the deferred four-way split as a revision trigger
  in place of the old compoundness trigger. The seven bound derivative
  pages were re-keyed to 0.2.0.
- **Claims 0002, 0003, and 0004 are untouched.** Whatever the dossier said
  about them stands exactly as presented.

## Effect on each pilot's promotion case

| Claim | Version | Change since dossier | Effect on the case |
| --- | --- | --- | --- |
| `woh-claim-0001` | 0.2.0 | Dependency, scope, triggers; statement unchanged | Strengthened: the record no longer forces one `claim_kind` and one `evidence_status` onto the report layer; `scoped, contested` now honestly describes the retained B–D bundle |
| `woh-claim-0002` | 0.1.0 | None | As presented |
| `woh-claim-0003` | 0.1.0 | None | As presented |
| `woh-claim-0004` | 0.2.0 | None (its 0.2.0 predates the dossier) | As presented |
| `woh-claim-0070` | 0.1.0 | New | Joins the set; case below |

## The promotion case for woh-claim-0070

The record asserts what *The Book Which Tells the Truth* explicitly reports
at `TBWTT-1:53` and `TBWTT-2:5` — not that the reported events occurred.
Its acceptance question is therefore narrow: is the report layer accurately
stated, correctly located, and correctly typed?

- **Kind and label follow accepted precedent.** `woh-claim-0020` (the
  contact reports as provenance) established the `source_report` discipline
  and the `direct` label for report-layer records, and was accepted under
  ADR 0006. Claim 0070 applies the same discipline to the content layer,
  with the same one-forbidden-use revision trigger.
- **The content is inspected, not asserted from memory.** Both locators are
  verified against the project digitization (source note, verification log
  2026-08-02). The known limitation — no collation against printed French
  and English editions — is recorded in the source note, named in the
  record's first revision trigger, and reflected in `evidence_status:
  scoped` rather than anything stronger.
- **Alternatives are typed for a source_report.** The record's alternatives
  address the two ways a report-layer record can fail (misreading or
  selective quotation; edition variance) rather than inheriting the
  historicity alternatives, which remain on claim 0001 where they belong.
- **Lifecycle is the only anomaly.** The record is `draft` solely because
  it was born inside the pilot set by extraction; nothing about its content
  is less settled than the accepted `woh-claim-0020`.

## What promotion does and does not do

Per the ADR 0005 precedent: promotion flips lifecycle (and the controlling
specifications' status, which the validator enforces) and nothing else.

- **No version bumps.** Lifecycle is not a meaning change; the page
  bindings at `0001@0.2.0` and elsewhere are unaffected.
- **Evidence statuses are unchanged.** Every record in the set stays
  `scoped` (0001 and 0002 also `contested`). Lifecycle is not truth, and
  acceptance is not review.
- **Open work is not closed.** The first reproducible review (claim 0070's
  source criticism is the load-bearing candidate), the edition collation,
  the access upgrade for the critical literature, and the deferred
  four-way split all remain exactly as open after promotion as before.

## Options

1. **Promote all five together** (`0001`–`0004` and `0070`) in a single
   ADR. The set is internally consistent: 0001 now depends on 0070, and
   accepting the hypothesis record while its foundational `source_report`
   dependency stays draft would invert the natural order of confidence.
2. **Promote 0070 only, hold 0001–0004.** Defensible if the founder's
   reservations from the dossier concern the pilots' propositions rather
   than their record quality; 0070 is the least contestable record in the
   set.
3. **Hold everything.** Costs nothing except that the catalog's three
   foundational claims and its comparative pilot remain `draft` while 65
   later records are `accepted` — the inversion the dossier was written to
   resolve.

**Recommendation:** option 1. The dossier's per-claim cases stand or are
strengthened; 0070 rides on accepted precedent; and a single ADR keeps the
dependency order clean.

## On ratification

Ratification should be recorded as an ADR (next free number) listing the
five records, flipping the five specification statuses in sync, and citing
this addendum and the presented dossier as its basis. If the founder
excludes any record, the ADR records which and why, and the excluded
record's next step.

**Ratified 2026-08-17: the founder adopted option 1.** All five records
are promoted under
[ADR 0008](../../decisions/0008-pilot-claims-promotion.md).
