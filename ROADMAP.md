# Roadmap

This roadmap orders work by dependency. It does not assign artificial dates or
turn document production into evidence.

## Stage 1 — Foundation and governance

- Establish scope, epistemic principles, terminology, claim semantics,
  evidence status, versioning, RFCs, ADRs, and source-note conventions.
- Record representative existing claims without promoting them.
- Validate stable links to the existing Wheel source registry.

**Exit evidence:** a contributor can distinguish project adoption, source
content, inference, and evidence maturity, and can propose a change without
silently rewriting the framework.

## Stage 2 — Framework inventory

- Identify the smallest defensible set of framework components and claims.
- Map dependencies among the central hypothesis, chronology, philological
  readings, comparative identities, and derived narratives.
- Record public pages and API resources derived from each claim.
- Preserve disagreements and unresolved boundaries.

**Exit evidence:** every central public assertion points to a versioned core
record, and each core record exposes its dependencies and derivatives.

## Stage 3 — Source-note and evidence mapping

- Create source notes for foundational, primary, scholarly, scientific,
  comparative, and critical sources used by each core claim.
- Record access level and locators.
- Distinguish independent evidence from repeated use of the same source or
  assumption.
- Build evidence maps that include contradictory and null material.

**Exit evidence:** a reviewer can reconstruct what was inspected, what each
source reports, and what Wheel inferred from it.

## Stage 4 — Reproducible review

- Define question-specific search and selection protocols.
- Run structured reviews for philological, historical, comparative, and
  scientific subclaims.
- Record screening, extraction, limitations, and reviewer sign-off.
- Revise, split, narrow, or retire claims where the review warrants it.

**Exit evidence:** claims marked `reviewed` have reproducible review records;
the label is never granted by narrative confidence alone.

## Stage 5 — Publication integration

- Define an explicit export or cross-reference contract for `data-content`.
- Add core claim IDs and versions to selected public pages without changing
  URLs or reader-facing badges prematurely.
- Expose core provenance through the public API where useful.
- Detect derivative pages that disagree with their controlling claim record.

**Exit evidence:** public outputs identify the exact core version they render,
and compatibility failures are visible before publication.

## Immediate programme

1. Review the two pilot claims and their source notes.
2. Decide through RFC whether the claim model is sufficient for the wider
   corpus.
3. Add a chronology claim as the next deliberately different pilot.
4. Inventory the current `framework`-labelled pages and group them into
   candidate core claims without bulk migration.
5. Convert durable conceptual decisions from operational notes into individual
   RFCs or ADRs while preserving the original history.
