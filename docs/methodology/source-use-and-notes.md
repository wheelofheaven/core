---
title: Source use and source notes
status: accepted
version: 0.1.0
last_reviewed: 2026-08-02
---

# Source use and source notes

## Stable identity

Use the existing Wheel source ID. The current comprehensive public registry is
generated at `www.wheelofheaven.world/data/sources.json`; older records may
originate in `data-bibliography`, while other IDs are harvested from structured
content references.

The core does not mint a replacement ID for an existing source. A missing or
ambiguous ID is a source-registry issue to resolve before substantive use.

## Access levels

Every source note declares one of:

- `full_text`: the cited edition was inspected in full;
- `project_digitization`: Wheel's digitized or translated representation was
  inspected;
- `excerpt`: only identified passages were inspected;
- `abstract`: only an abstract or structured summary was inspected;
- `metadata_only`: bibliographic metadata was checked but the work was not
  substantively inspected;
- `secondary_citation`: knowledge came through another source.

Access level limits what the note may assert.

## Required separation

A source note distinguishes:

1. source identity and access;
2. what the source reports or argues;
3. method, genre, edition, translation, or textual basis;
4. limitations and criticism;
5. Wheel interpretation and relevance;
6. related sources and dependencies;
7. verification history.

## Locators

Use the most precise stable locator available: Wheel `refId`, chapter and
paragraph, book and verse, tablet and line, page, section, DOI, or archival
identifier. Do not cite a whole work for a narrow claim when a locator exists.

## Source roles

Machine-readable claim records use source roles such as `canonical_basis`,
`primary_text`, `scholarly_context`, `scientific_context`, `comparative`, and
`critical`. These roles describe the use in that claim, not the source's
inherent quality.
