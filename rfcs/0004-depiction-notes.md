---
title: "RFC 0004: Depiction notes"
status: accepted
authors:
  - project founder
  - Claude (drafting agent, at founder direction)
created: 2026-08-15
review_until: null
related_adrs:
  - ../decisions/0003-depiction-notes.md
supersedes: []
superseded_by: null
---

# RFC 0004: Depiction notes

## Review question

Should the core add a **depiction notes** document class — per-entity and
per-scene records of what the sources visually and scenically report — so
that illustrations, hero images, and audio-play scenery derive from records
rather than from ad-hoc art direction?

## Summary

The project produces visual and scenic artifacts (hero images, wiki and
article illustrations, gallery renders, audio-play ambience and staging) with
no core-side grounding: today their canon-consistency depends entirely on
whoever writes the image prompt or scene description. This RFC proposes
`depictions/` as a new top-level document class recording, for each depicted
entity or scene, three separated layers:

1. **Reported** — what a named source explicitly says about appearance,
   setting, sound, or staging, with locators (`source_report` discipline);
2. **Interpolated** — bounded inference the project adopts for depiction
   consistency where sources are silent, each with its rationale;
3. **Free** — dimensions declared open to art direction, where variation
   carries no claim content.

A visual or scenic brief then cites its depiction notes the way a text
artifact cites claim records under
[RFC 0003](0003-artifact-derivation-contract.md), whose derivation norm this
RFC extends to non-text artifacts.

## Problem and scope

Concretely: what may an illustration of the Elohim show? The canon reports
specific visual particulars (small stature, appearance described at defined
TBWTT locators); the *Theogony* reports Typhoeus's serpent heads and the
melting earth at `THEO-WOH-1:820–868`; the Odyssey reports the Phaeacians
feasting beside undisguised gods. An illustrator — human or model — currently
has no record separating what is reported from what is invented, so every
image quietly makes claims. A hero image that shows the wrong thing is a
public assertion with no controlling record; repeated across the gallery
pipeline and nine languages, drift compounds.

Scope: the document class, its three-layer structure, its binding rule, and
one pilot. Non-goals: style guides (palette, composition, rendering technique
belong to the publication side); any image pipeline change; retroactive audit
of existing imagery.

## Claim kinds and evidence

The proposal itself is a `normative_recommendation`. The records it defines
are dominated by `source_report` content (layer 1), with layer 2 holding
clearly labelled `interpretation` entries. The class exists precisely to keep
those two kinds from blending inside an image, where labels are invisible —
an image cannot hedge, so the record must hedge for it.

## Detailed proposal

### Document class

`depictions/{slug}.md`, one file per depicted entity, place, or recurring
scene (e.g. `elohim-individual`, `eden-laboratory`, `council-assembly`,
`typhoeus-combat`). Frontmatter: `title`, `status` (lifecycle values),
`version`, `last_reviewed`, optional `claim_ids` linking to the claims whose
content the depiction expresses.

Body sections, fixed order:

1. **Reported** — table of source, locator, and the exact visual/scenic
   particular reported. Same locator discipline as evidence maps. A
   particular that is contested across sources is listed per source, not
   harmonised.
2. **Interpolated** — each entry: the interpolation, its rationale, and its
   revision trigger. Interpolations are project decisions, reviewable like
   any interpretation.
3. **Free** — dimensions explicitly released to art direction (style,
   palette, framing, era-neutral incidentals), so that "free" is a recorded
   decision rather than an absence.
4. **Must not show** — negative constraints: particulars that would
   contradict a reported layer or an existing claim record (e.g. imagery
   asserting a transmission route the bound claim excludes).

### Binding rule

A visual or scenic brief (image prompt file, audio-play scene spec, gallery
entry) declares the depiction notes it renders, mirroring RFC 0002 fields:
`core_depiction_ids` + `core_depiction_versions`. Rendered assets inherit
their brief's binding; assets are never bound directly. Validator support
follows the RFC 0002 pattern (existence, version equality, reciprocal-list
warning) and is added only if this RFC is accepted.

### Authority

Depiction notes follow the same gates as everything else in the core: agents
may draft; layer-2 interpolations that embed a new identification or
contradict a claim record require founder direction; promotion is
founder-only.

### Pilot

One entity note (`elohim-individual`, the highest-traffic depiction) and one
scene note (`typhoeus-combat`, exercising the `woh-claim-0004` material),
each bound by one real brief from the existing image pipeline, before any
wider adoption.

## Alternatives

### Status quo (art direction decides)

Zero overhead; every image remains an unaudited claim. The cost is invisible
until an image contradicts the canon in a high-traffic place, and it is
already unauditable at nine languages.

### Fold depiction content into claim records

No new class; but claim records answer "what do we claim" and would bloat
with staging detail that has no propositional content. Appearance particulars
are mostly `source_report`s about texts, not claims about history — a
different grain.

### Publication-side style bible (no core involvement)

Keeps the core small; but the reported/interpolated boundary is exactly the
distinction the core exists to keep honest, and a www-side bible would
re-create the two-constitutions split this programme is closing.

## Risks, limitations, and dissent

- **Class proliferation.** A fourth document class grows the core's surface.
  Mitigation: the pilot is two notes; expansion only on demonstrated use.
- **False precision.** Sources underdetermine most depictions; a note can
  imply more constraint than exists. The Free layer is mandatory for this
  reason.
- **Enforcement gap.** Nothing technical prevents an unbound image; the
  contract is normative until validator support lands, and normative-only
  for any hand-made asset.
- **Aesthetic chilling.** Over-constrained notes could flatten the visual
  language. The class records claims, not taste; style stays on the
  publication side.

## Compatibility and migration

Additive: new directory, new optional frontmatter fields on briefs, no
existing identifier or page affected. Existing imagery is grandfathered and
audited only opportunistically (when a page is fundamentally rewritten, per
the RFC 0003 ratchet).

## Validation plan

- Author the two pilot notes as drafts; bind one real brief each.
- Regenerate one asset from a bound brief and have the founder compare
  against the note's layers: does the record actually change what gets
  rendered, and is the Free layer wide enough?
- Founder decides; an ADR records the decision and, if accepted, the
  validator extension is specified then.

## Resolution

Accepted by the project founder on 2026-08-15. Recorded in
[ADR 0003](../decisions/0003-depiction-notes.md). The two pilot notes and
the validator extension proceed as implementation steps in that order.
