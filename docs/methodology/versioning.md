---
title: Versioning
status: accepted
version: 0.1.0
last_reviewed: 2026-08-02
---

# Versioning

## Principles

Git preserves textual history. Document metadata exposes meaningful states.
ADRs preserve why decisions changed. None replaces the others.

## Semantic versions

Independently versioned specifications use `MAJOR.MINOR.PATCH`:

- `PATCH`: clarification without changed proposition or interface;
- `MINOR`: backward-compatible detail, evidence, alternative, or optional
  field;
- `MAJOR`: changed proposition, meaning, required field, dependency, or public
  compatibility.

All initial framework records use `0.y.z` while their boundaries remain draft.

## Stable identifiers

Never reuse a claim ID for a materially different proposition. If one claim
splits, create new IDs and retain a mapping. If claims merge, retain their
earlier records and document the successor.

## Supersession and migration

A breaking change requires:

- an RFC and adopted ADR;
- a concise reason and change summary;
- affected terms, source notes, records, public pages, translations, datasets,
  APIs, and schemas;
- a migration or an explicit statement that migration is impossible;
- retained access to the earlier representation;
- forward and backward supersession links.

## Machine-readable compatibility

Each JSON claim declares a schema version and its controlling human-readable
document. Update both in the same change. The validator detects missing files
and catalog divergence but does not decide semantic equivalence.
