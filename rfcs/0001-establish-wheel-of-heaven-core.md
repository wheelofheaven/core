---
title: "RFC 0001: Establish Wheel of Heaven Core"
status: accepted
authors:
  - project founder
created: 2026-08-02
review_until: null
related_adrs:
  - ../decisions/0001-durable-research-core.md
supersedes: []
superseded_by: null
---

# RFC 0001: Establish Wheel of Heaven Core

## Review question

Should Wheel of Heaven establish a dedicated, Markdown-first research core that
controls conceptual meaning while existing repositories retain sources,
bibliography, public content, documentation, and software?

## Summary

Establish `wheelofheaven/core` as the durable research corpus. Adapt the
successful separation pattern piloted by Human Macroscope while preserving
Wheel's declared Raëlian canonical stance and existing repository ecosystem.

## Problem and scope

Wheel already separates raw sources, digitized texts, bibliography, content,
web presentation, and APIs. Its hypothesis, methodology, evidence status,
source interpretation, and conceptual decisions remain distributed among
public pages and operational `.claude` documents.

This has produced visible drift:

- a three-value claim decision evolved into a four-value public taxonomy;
- public badges mix source explicitness, mainstream acceptance, project stance,
  inference, and evidence;
- source metadata can contain project interpretation;
- framework claims have no independent lifecycle, evidence status, revision
  triggers, or decision history;
- derivative pages can disagree without a controlling specification.

The proposal covers research representation and governance. It does not change
public URLs, content, translations, APIs, or existing source records.

## Claim kinds and evidence

This is a repository and conceptual-architecture decision, not evidence for a
substantive Wheel claim. The motivating observations come from the local
repository structure and current content conventions.

## Detailed proposal

Create a separate repository with:

- foundations, framework specifications, methodology, and research agendas;
- orthogonal claim kind, framework relation, lifecycle, evidence status, and
  public-label fields;
- machine-readable claim records and schemas;
- source notes keyed to existing Wheel source IDs;
- RFC and ADR workflows with supersession;
- validation against the current aggregated source registry;
- two pilot claims before wider migration.

Human-readable specifications control semantics. JSON controls interchange.
The website and API remain downstream consumers only after a later integration
decision.

## Alternatives

### Keep the status quo

Continue using public Markdown pages and `.claude` strategy files as the de
facto specification. This avoids another repository but retains lifecycle,
drift, and audience-mixing problems.

### Use `data-content` as the core

This keeps fewer repositories but makes reader-facing prose and translations
authoritative for research meaning and couples conceptual revisions to
publication concerns.

### Use `docs.wheelofheaven.world` as the core

The docs site is designed for authors, developers, and architecture readers and
explicitly follows a single-current-version model. Making it the research core
would mix contributor instructions with disputed framework semantics.

### Convert `.claude` into the core

This preserves existing plans but keeps durable project meaning under a
tool-specific name and mixes research with operations, publishing queues, and
agent configuration.

## Risks, limitations, and dissent

- A new repository adds navigation and maintenance cost.
- Templates can create bureaucracy without improving actual research.
- Human and machine representations may drift.
- The source registry itself currently has legacy and generated layers.
- A core can make weak claims look formal without making them stronger.
- The Human Macroscope pattern is new and has not yet proven itself over years.

Mitigations are a two-claim pilot, minimal dependencies, explicit draft status,
validation, and no bulk migration.

## Compatibility and migration

The first release is additive. It changes no existing files or URLs. Existing
public badges are recorded but not redefined. Durable conceptual material may
move later through claim-specific migrations that preserve original history.

## Validation plan

- Validate JSON, catalog references, document metadata, source-note IDs, and
  cross-links.
- Check pilot source IDs against the aggregated public source registry.
- Review whether the two pilots expose useful distinctions without excessive
  overhead.
- Require a later RFC before adding publication fields or bulk-migrating claims.

## Resolution

Accepted by explicit project-founder direction on 2026-08-02. Decision recorded
in [ADR 0001](../decisions/0001-durable-research-core.md).
