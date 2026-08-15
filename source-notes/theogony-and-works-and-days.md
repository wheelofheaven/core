---
title: "Source note: Theogony and Works and Days"
source_id: theogony-and-works-and-days
note_status: draft
source_access: project_digitization
reviewed_by: []
last_reviewed: 2026-08-15
---

# Theogony and Works and Days (Hesiod)

## Source identity and access

Wheel source ID `theogony-and-works-and-days`. The project holds an in-house
English translation of the *Theogony* (`theogony-woh`), produced through the
Translation Program pipeline (Translator → Editor → Reviewer → human
sign-off) and published in the public library at `/library/theogony-woh/`.
Access is therefore `project_digitization` for the *Theogony*. *Works and
Days* is covered by the registry record but has no in-house translation;
claims must not cite `THEO-WOH` locators for it.

Locator convention: `THEO-WOH-1:NNN`, where chapter 1 spans the whole poem
and verse numbers follow the standard Greek line numbering, so `THEO-WOH`
locators remain comparable with scholarly citations of the Greek text.

## Source type and purpose

Archaic Greek hexameter poetry attributed to Hesiod (conventionally c. 700
BCE). The *Theogony* is a systematic divine genealogy: the origin of the
cosmos, the succession of divine rulers (Ouranos → Kronos → Zeus), the
Titanomachy, the Typhoeus combat, and the ordering of the Olympian world. It
is the closest thing archaic Greece has to a systematic statement of the
cosmology the Homeric poems assume without explaining.

## Reported content

Passages this repository currently relies on (all `THEO-WOH-1`):

- `26–28` — the Muses' statement that they can speak both convincing
  falsehood and truth: the poem's own epistemic disclaimer.
- `154–182` — the castration of Ouranos by Kronos from ambush.
- `453–467` — Kronos swallowing his children; Rhea hiding Zeus; the return.
- `561–569` — Prometheus stealing fire in the fennel-stalk against Zeus's
  embargo.
- `617–720` — the Titanomachy; the defeated elder generation confined below.
- `820–868` — the Typhoeus combat; the storm god against the serpentine
  challenger.

These are source reports about the poem's content. None of them establishes
that any reported event occurred.

## Basis or method

The in-house translation was produced against the Greek text with the
project's glossary discipline; divergent renderings carry per-verse
commentary in the library apparatus. The translation is a project rendering:
where a canonical gloss departs from consensus lexical derivation, the
apparatus is required to label it (see
[epistemic principles](../docs/foundations/epistemic-principles.md),
philological discipline).

## Limitations and criticism

- Composition and transmission: the poem crystallised from an oral tradition;
  its text, like Homer's, is the visible end of a transmission line, not a
  datable authorial manuscript.
- The proem's truth/falsehood statement (26–28) is the text's own warning
  against reading it as chronicle.
- The succession-myth material has a documented Anatolian forerunner (the
  Song of Kumarbi); scholarly consensus treats the Hesiodic version as
  downstream of Near Eastern tradition. Any use of the *Theogony* as an
  independent witness must account for this dependence.

## Wheel interpretation

Claim `woh-claim-0004` reads the poem's conflict architecture (succession,
Titanomachy, Typhoeus, Prometheus) as transformed memory of the
Council–Serpentine conflict. That is an `interpretation` supplied by the
framework; the poem reports the myths, not their referent. The inferential
step from source report to remembered event is the claim's entire burden and
is not carried by this source.

## Related sources and dependencies

- `the-hittite-version-of-the-hurrian-kumarbi-myths-oriental-forerunners-of-hesiod`
  (Güterbock 1948) — establishes the Anatolian forerunner.
- `the-east-face-of-helicon-west-asiatic-elements-in-greek-poetry-and-myth`
  (West 1997) — the wider Near Eastern context of Hesiodic material.
- `odyssey-greek-text` — the Homeric cosmology the *Theogony* systematises.
- The in-house *Baal Cycle* translation — the Ugaritic instance of the combat
  armature.

## Verification log

- 2026-08-15 — Claude (reverse-pilot for RFC 0003): confirmed the in-house
  translation exists and is published; passage list keyed to the locators
  used by `woh-claim-0004` and the public Odyssey Explainer. Line-level
  re-verification of each passage against the library apparatus not yet
  performed.
