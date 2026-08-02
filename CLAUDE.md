# Wheel of Heaven Core — Claude Instructions

This repository is a durable research corpus, not a prompt to complete or
defend a theory. Claude and any other AI coding or research agent working here
must protect its epistemic boundaries, declared stance, provenance, and
history.

## Required behaviour

1. Read the relevant foundation, framework, methodology, source notes, RFCs,
   decisions, glossary entries, and machine-readable records before changing
   substantive content.
2. Make the smallest change that satisfies the task. Do not opportunistically
   elaborate adjacent theory.
3. Keep claim kind, framework relation, evidence status, lifecycle, and public
   label separate. Never infer one automatically from another.
4. Represent the Raëlian canon as Wheel of Heaven's declared interpretive
   centre. Do not misrepresent that stance as empirical validation or academic
   consensus.
5. Distinguish what a source reports from what Wheel of Heaven infers. Use
   stable source IDs and locators. Never invent citations, identifiers,
   quotations, translations, results, or consensus.
6. Record uncertainty, disagreement, alternative explanations, and revision
   triggers. Do not weaken criticism merely because it challenges the framework.
7. Treat cross-tradition resemblance, dependence, typology, and identity as
   different claims. Similarity alone does not establish common origin or
   shared referents.
8. Keep philological, historical, scientific, canonical, and comparative
   reasoning visibly distinct.
9. Preserve history through versions, deprecation, supersession, RFCs, ADRs,
   and migrations. Never silently reuse an identifier for a different meaning.
10. Update affected human-readable specifications, model records, catalog
    entries, glossary terms, source notes, and decisions together.

## Changes requiring explicit human direction

Do not independently:

- promote a draft claim, framework specification, RFC, or decision;
- change the foundational-canon stance;
- add a new foundational claim or identify two historical figures, traditions,
  or beings as the same referent;
- invent a chronology, causal mechanism, translation, etymology, source
  relationship, or empirical test result;
- suppress recorded dissent or remove a superseded conceptual state;
- select a new license, governance authority, institutional affiliation, or
  religious position;
- introduce an application framework, database, frontend, or service.

An agent may scaffold a clearly marked draft or research question when asked,
but must not fill unknowns with authoritative-looking content.

## Working conventions

- Follow `CONTRIBUTING.md` and the nearest more-specific `CLAUDE.md`.
- Use Markdown, JSON, JSON Schema, CSV, and other documented open formats.
- Human-readable framework specifications control meaning. Machine-readable
  records control interchange. Any disagreement between them is an error to
  resolve explicitly.
- Major conceptual, compatibility, or repository-process changes begin as an
  RFC. Add an ADR only after a decision has actually been made.
- Do not edit quoted source text except to correct a verified transcription.
- Run `mise run check` (or `python3 scripts/validate.py`) before finishing a
  change. Report validation performed and unresolved gaps.

## GitHub account isolation

- Do not run `gh auth switch` or rewrite global GitHub CLI authentication.
- Use the `gh` wrapper from `PATH`; it selects the isolated configuration for
  this repository.
- Keep Wheel of Heaven remotes on the `github-zarazinsfuss` SSH alias.
- If authentication is missing, ask the user to run
  `github-agent-login zarazinsfuss`.
