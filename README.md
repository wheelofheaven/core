# Wheel of Heaven Core

Wheel of Heaven Core is the durable research corpus and conceptual
specification behind the Wheel of Heaven project.

It records what the framework claims, where those claims come from, how the
project reasons from sources, which alternatives and objections matter, and
how meanings change over time. It is intentionally separate from the reading
website, its translations, the source-text library, the bibliography database,
and the software that publishes them.

## Purpose

Wheel of Heaven reads ancient creation traditions through a declared Raëlian
interpretive lens and tests that reading against primary texts, scholarship,
scientific and historical context, comparative traditions, and criticism.
This repository makes that work inspectable without pretending that the
project's adopted framework is the same thing as external validation.

The core is authoritative for:

- framework definitions and their dependencies;
- precisely stated claims and their current research status;
- distinctions among source reports, observations, models, hypotheses,
  interpretations, and normative proposals;
- evidence maps, source notes, limitations, challenges, and revision triggers;
- research questions and methods;
- conceptual versions, RFCs, and durable decisions.

## Repository boundaries

| Repository | Owns |
| --- | --- |
| `core` | Conceptual meaning, research state, source interpretation, and decision history |
| `data-sources` | Raw upstream PDFs, scans, and source artifacts |
| `data-library` | Digitized texts, translations, passages, and stable textual references |
| `data-bibliography` | Bibliographic identity, source metadata, and licensing fields |
| `data-content` | Reader-facing prose, articles, wiki entries, and translations |
| `www.wheelofheaven.world` | Web presentation and the aggregated public source registry |
| `api.wheelofheaven.world` | Public machine distribution |
| `docs.wheelofheaven.world` | Contributor, architecture, and developer documentation |

The core references stable Wheel source IDs. It does not duplicate raw texts or
bibliographic records. Source notes add research interpretation and access
status while pointing back to those IDs.

## Declared stance

Wheel of Heaven is not neutral about its interpretive starting point. The
Raëlian source material is its foundational canon. That project commitment is
recorded explicitly and is kept separate from empirical support, scholarly
acceptance, and document maturity.

An internally adopted premise may remain externally contested, empirically
unverified, or unsupported. Conversely, an empirical observation does not
become part of the framework merely because it is well established. The core
records both axes.

## Repository map

| Path | Purpose |
| --- | --- |
| `docs/foundations/` | Scope, epistemic principles, and conceptual architecture |
| `docs/framework/` | Human-readable specifications for framework claims and components |
| `docs/methodology/` | Claim typing, evidence, source use, comparison, and versioning |
| `docs/research/` | Research agenda, questions, and review programmes |
| `model/` | Machine-readable catalog, claim records, and schemas |
| `source-notes/` | Notes separating source content from project interpretation |
| `rfcs/` | Open proposals and structured requests for comment |
| `decisions/` | Adopted Architecture Decision Records (ADRs) |
| `GLOSSARY.md` | Canonical research terminology |
| `ROADMAP.md` | Dependency-ordered research stages |
| `CONTRIBUTING.md` | Contribution and review workflow |
| `AGENTS.md` | Constraints for AI coding and research agents |

## Current status

This is a version `0.1.0` foundation and pilot. The repository establishes the
governance and claim model, and records two representative framework claims:

1. the Elohim-civilization hypothesis;
2. the proposed identity of the Anunnaki and the Elohim.

Both records are drafts. They document existing Wheel of Heaven positions; they
do not newly validate those positions. Their evidence maps are `scoped` and
`contested`, not systematic reviews.

## Validation

Run:

```sh
mise run check
```

or directly:

```sh
python3 scripts/validate.py
```

When the repository is checked out beside the other Wheel repositories, the
validator also checks source IDs against
`www.wheelofheaven.world/data/sources.json`.

## License

CC0-1.0. Source texts and quoted material retain their own rights and licensing
conditions; this dedication applies only to original material in this
repository.
