# Contributing

Wheel of Heaven Core exists to keep the framework inspectable, challengeable,
and historically legible. Contributions are evaluated for clarity,
provenance, inferential discipline, and compatibility as well as usefulness.

## Before proposing a change

1. Read the controlling framework specification and machine-readable record.
2. Read the relevant methodology, glossary entries, source notes, RFCs, and
   decisions.
3. Search for earlier terminology, objections, and superseded proposals.
4. Identify whether the contribution changes a source report, observation,
   model, hypothesis, interpretation, or normative proposal.
5. State the smallest affected scope.

## Contribution paths

### Small corrections

Typos, broken links, metadata corrections, and clarifications that do not alter
meaning may be proposed directly. Explain why the change is non-semantic.

### Sources and source notes

- Reuse the stable source ID from Wheel's public source registry.
- Record exactly what was inspected: full text, project digitization,
  translation, excerpt, abstract, metadata, or secondary citation.
- Give passage, page, tablet, line, chapter, or paragraph locators.
- Separate reported content from Wheel interpretation and from later uses.
- Preserve limitations, corrections, and access restrictions.

### Claims and framework specifications

A substantive claim change must document:

1. the precise proposition and its scope;
2. claim kind and framework relation;
3. lifecycle and evidence status;
4. supporting source reports or observations;
5. the strongest relevant alternatives and objections;
6. inferential steps and dependencies;
7. what would count against the claim;
8. effects on public pages, translations, APIs, datasets, and identifiers;
9. compatibility and migration requirements.

The human-readable specification and JSON record must change together.

### Major decisions

Use an RFC for an open change to foundational stance, canonical terminology,
claim semantics, component boundaries, evidence standards, schemas, source
relationships, or repository process. When a proposal is adopted, record the
decision in an ADR and cross-link the two records.

## Status changes

Lifecycle status describes repository use, not truth:

- `draft`: incomplete and open to criticism;
- `proposed`: ready for an explicit project decision;
- `accepted`: current project specification;
- `deprecated`: retained but discouraged;
- `superseded`: replaced by a linked successor.

Evidence status is governed separately in
`docs/methodology/evidence-status.md`.

## Review checklist

- Is the exact proposition stable and bounded?
- Are source report, observation, model, hypothesis, and interpretation kept
  distinct?
- Is project adoption clearly separate from empirical support?
- Are canonical, philological, comparative, scientific, and historical bases
  attributed at the correct level?
- Are objections and alternatives represented at full strength?
- Are source IDs and locators valid?
- Are versions, dependencies, migrations, and public derivatives updated?
- Can a future reviewer reconstruct why the change was made?

## Validation

Run `mise run check` before submitting a change. Report any external source
registry that was unavailable during validation.
