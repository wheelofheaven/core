---
title: "Review: the canonical contact report"
claim_id: woh-claim-0070
review_id: woh-claim-0070-review-0001
status: draft
components_complete:
  - edition-collation
  - internal-consistency
components_outstanding:
  - genre-and-source-critical-appraisal
recommended_status: null
signed_by: null
signed_date: null
supersedes: null
---

# Review: the canonical contact report

First review drafted against the format adopted in
[RFC 0007](../../rfcs/0007-reproducible-review-records.md) /
[ADR 0009](../../decisions/0009-reproducible-review-records.md). It is
**unsigned**.
Claim [`woh-claim-0070`](../framework/canonical-contact-report.md) has not
moved and remains `scoped`.

Two of the three review components named by the
[evidence map](../evidence/woh-claim-0070-evidence.md) were performed. The
third could not be, and the reason is recorded under Limitations rather than
papered over.

## Question

The proposition reviewed, quoted from the claim record:

> The Book Which Tells the Truth explicitly reports that its speakers are
> biological beings like terrestrial humans living on another planet, glosses
> Elohim as those who came from the sky, and reports that the civilization's
> scientists selected Earth and artificially created terrestrial life,
> including humanity; this record asserts what the source reports, not that the
> reported events occurred.

The claim is a `source_report`. What is at issue is only whether the record
accurately states what the source says, and whether that report is stable
across the representations the project can reach. Whether the reported events
occurred is not in scope and belongs to `woh-claim-0001`.

Two declared alternatives are under test:

- `alt-0070-misreading` — the cited passages do not support this summary.
- `alt-0070-edition-variance` — printed French and English editions differ
  materially from the inspected project digitization.

## Protocol

**Representations compared.** Three witnesses were available:

| Witness | Identity | Access |
| --- | --- | --- |
| **D** — project digitization | `data-library/the-book-which-tells-the-truth/chapter-{1..7}.json` | Held |
| **F** — French printed edition | *Le Message donné par les Extra-terrestres*, 2005 combined volume, 228 pp. | Held, `data-sources/pdf/_combined/` |
| **E** — English printed edition | *Intelligent Design: Message from the Designers*, 2005 combined volume, 412 pp. | Held, `data-sources/pdf/_combined/` |

**Procedure.** Text layers were extracted from F and E with `pdftotext
-layout` (poppler). Both PDFs carry a genuine text layer; no OCR was required
and none was performed. Each of D's paragraphs of 40 characters or more was
normalised (Unicode NFC; typographic quotes and dashes folded; French
typographic spacing before `; : ! ?` removed; punctuation stripped; all
whitespace removed, which neutralises line-wrap and hyphenation artifacts) and
sought in the correspondingly normalised printed text. Matches were scored with
`difflib.SequenceMatcher`. Every case scoring below 0.95, and every case whose
opening 50 characters were not found at all, was then read by hand against the
printed page to classify it as a genuine textual variant or an extraction
artifact.

The comparison scripts are in the session scratch and are reproducible from
this description; they are three short filters over the two text layers and the
seven chapter files, using only the standard library.

**What would have counted against the claim.** Any of: the two cited passages
absent from a printed edition; a printed edition wording that removes the
plural of *Elohim*, removes the "came from the sky" gloss, removes the
selection of Earth, or removes the creation of life; or a divergence between
witnesses large enough that no single report layer could be said to exist.

**Locators.** D uses project-internal `refId`s (`TBWTT-1:53`). The printed
editions have no verse numbering, so printed page numbers are given for every
quotation. Page numbers were resolved per PDF page and cross-checked against
each volume's own pagination; for E they were additionally confirmed against
the volume's index, which lists "those who came from the sky 11, 57, 309–311,
335" — agreeing with the page found for `TBWTT-2:5`.

## Screening

**Examined.** All 7 chapters of D (759 paragraphs, of which 634 met the
40-character floor); the whole of book one in F and E; book two
(*Extraterrestrials Took Me to Their Planet*) and book three (*Let's Welcome
the Extra-Terrestrials*) in E for the internal-consistency component; the
corresponding passages in F.

**Excluded, with reason.** Paragraphs under 40 characters — mostly single-word
dialogue turns and biblical chapter markers — were excluded from the automated
collation because short strings produce false matches against a 200-page text;
they were not excluded from the hand reading of the two cited passages. The
1973 and 1974 first printings were excluded because no copy is held. Palmer's
*Aliens Adored* and the other critical literature were excluded because no copy
is held; this is what leaves the third component outstanding.

## Extraction

### Component 1 — edition collation

**`TBWTT-1:53`.** Printed at F p. 18 and E p. 8, at the identical point in the
dialogue in both (answering "Comment vous appelez-vous ?" / "What are you
called?").

| Witness | Wording |
| --- | --- |
| D (French base) | « Nous sommes des hommes comme vous et nous vivons sur une planète assez semblable à la Terre. » |
| F p. 18 | Identical to D, character for character. |
| E p. 8 | "We are people like you, and we live on a planet similar to Earth." |
| D (English rendering) | "We are men like you, and we live on a planet quite similar to Earth." |

**`TBWTT-2:5`.** Printed at F p. 20 and E p. 11, in both cases immediately
following the quotation of Genesis 1:1.

| Witness | Wording |
| --- | --- |
| D (French base) | « Elohim, injustement traduit dans certaines Bibles par Dieu, veut dire en Hébreu "ceux qui sont venus du ciel" et est bel et bien au pluriel. Cela veut dire que les scientifiques issus de notre monde ont d'abord recherché la planète leur paraissant la plus apte à la réalisation de leurs projets. Ils ont "créé", découvert en réalité, la terre… » |
| F p. 20 | Identical to D apart from one participle agreement (`rendu` / `rendus`). |
| E p. 11 | "Elohim, translated without justification in some Bibles by the word God means in Hebrew 'those who came from the sky', and furthermore the word is a plural. It means that the scientists from our world searched for a planet that was suitable to carry out their projects. They 'created', or in reality discovered the Earth, and realized it contained all the necessary elements for the creation of artificial life…" |

**Whole-book French fidelity (D against F).** 634 paragraphs compared:

| Result | Count |
| --- | --- |
| Exact match after normalisation | 583 |
| Similarity ≥ 0.99 | 12 |
| Similarity 0.95–0.99 | 29 |
| Similarity < 0.95 | 4 |
| Opening 50 characters not found | 6 |

All four sub-0.95 cases and all six probe failures were read against the page.
Every one is an extraction artifact — a running head and printed folio injected
into the middle of a paragraph (`41 la surveillance des élus`), a footnote rule,
a hyphenated line break (`embryon naires`), or the `œ` ligature. **No genuine
textual variant was found anywhere in the book.** The single orthographic
differences observed are `tranquillité` / `tranquilité` and the participle
agreement noted above, neither of which bears on meaning.

**Whole-book English divergence (D against E).** 631 paragraphs of D's English
renderings were compared against the published English:

| Result | Count | Share |
| --- | --- | --- |
| Exact match in the published edition | 4 | 0.6% |
| Opening 50 characters match | 11 | 1.7% |
| No match | 616 | 97.6% |

**The reason is recorded in the digitization itself.** Every chapter file
carries a `translation` block reading `{"method": "ai-assisted", "model":
"claude-opus-4-7", "date": "2026-05-16"}` (chapter 7: `2026-05-17`). D's
English is a machine translation of the French produced in 2026 — not the
published English of any edition.

This is not a quality finding. On `TBWTT-1:61` the AI rendering is the more
faithful of the two: F p. 18 reads « L'atmosphère est **très** différente de la
vôtre », D's English gives "The atmosphere is **very** different from yours",
and E p. 9 drops the intensifier — "the atmosphere is different from yours".
The same volume's book three, quoting the same line at E p. 227, restores it:
"the atmosphere is very different from yours". The published English is
internally inconsistent with itself on this line; the project's rendering is
not.

### Component 3 — internal consistency across later canon

**The canon corrects the first message, and says so.** Book two states at E
p. 150 / F p. 137: "we must correct a passage in the first message we gave you
that **you wrongly transcribed** concerning an eventual intervention on our part
to destroy humanity." The correction is carried in both languages. It does
**not** touch either passage this claim rests on. But it establishes, from
inside the canon, that the first message's text is not treated as an inerrant
transcript, and that the source itself attributes error to the human
transcriber.

**The "planet quite similar" wording is qualified within the first message.**
`TBWTT-1:53` says the speakers live on a planet *assez semblable* to Earth.
Eight turns later `TBWTT-1:61` says a human could not live there because the
atmosphere is very different. `TBWTT-3:42` restates the atmospheric difference;
`TBWTT-7:3` has Raël himself raise the tension; `TBWTT-7:68` answers it with a
residence in which Earth's atmosphere has been reproduced.

**The canon thematises this explicitly.** Book three opens with a section
titled "Seeming Contradictions Between the First and Second Message" (E p. 227)
which takes up this exact atmospheric question, among others, and answers it.
The tension is not one this review imports from outside; it is one the corpus
raises and addresses in its own voice.

## Appraisal

**On `alt-0070-misreading` — not supported.** The claim record's summary of
what the source reports is accurate against all three witnesses. The plural of
*Elohim*, the "those who came from the sky" gloss, the scientists' selection of
Earth, and the creation of artificial life are present in the French base text,
in the printed French, and in the printed English. The record's careful framing
— that it asserts what the source reports, not that the events occurred — is
preserved throughout.

**On `alt-0070-edition-variance` — not supported for the French; qualified for
the English.** D's French is a faithful transcription of the 2005 printed
French: 583 of 634 paragraphs match exactly and not one genuine textual variant
survives inspection. The report layer is stable across the French witnesses.

For the English the picture is different, though not in the way the alternative
anticipated. The divergence is not between printed editions; it is between the
published English and the project's own 2026 machine rendering, which the
evidence map and source note have been quoting as though it were the source's
own words. The substance survives — E p. 8 and E p. 11 independently support
every element of the claim statement — so the claim does not weaken. What
fails is the **quotation practice**, and it fails on the exact strings the
evidence map presents as what "the speaker states".

The gap is not cosmetic. "We are men like you" and "We are people like you"
differ on precisely the register — the gendered noun — that a reader assessing
a claim about "biological beings like terrestrial humans" might weigh. Nothing
in the record told a reader that the English they were reading was generated in
2026 by a language model.

**On the report layer's reliability.** The internal-consistency component
returns a result that constrains rather than confirms. The canon's own
correction at E p. 150 is an admission of defective transcription in the first
message. It leaves `TBWTT-1:53` and `TBWTT-2:5` untouched, so the claim stands
as written, but it means the report layer cannot be treated as a stable
transcript merely because two printed editions agree — the corpus itself says
one passage of it was transcribed wrongly. This is a genuine finding for the
`woh-claim-0001` independence question, which identified source criticism of
this report as load-bearing.

**What this review does not establish.** It says nothing about whether the
encounter occurred, and nothing about how the text came to exist. The
composition-account question — literary, revelatory, psychological,
sociological, fictional, or mistaken — is the outstanding component, and no
finding here bears on it in either direction.

## Limitations

**The first editions were not reached.** Both printed witnesses are 2005
combined volumes. The 1973 French first printing of *Le Livre Qui Dit la
Vérité* and the early English translations were not consulted because no copy
is held. The collation therefore establishes stability between the digitization
and the 2005 state of the text, not stability since 1973. Given that book two
documents at least one deliberate revision to the first message, revision
between 1973 and 2005 is a live possibility this review cannot exclude.

**The source-critical component was not performed.** Palmer, *Aliens Adored:
Raël's UFO Religion* — the standard academic study — is not held. Neither is
Dericquebourg's chapter in the Brill *Handbook of UFO Religions*, nor "Is God a
Space Alien? The Cosmology of the Raëlian Church". Writing a genre appraisal
from these works' titles and reputations would mean inventing citations, which
the repository forbids. The component is therefore recorded as outstanding.

**Extraction artifacts, not page images.** Findings rest on the PDFs' text
layers. Every divergence below 0.95 similarity was inspected in the extracted
text and judged an artifact on internal evidence — an injected running head is
unmistakable — but page images were not rendered for visual confirmation. For
the two passages the claim rests on this is a small risk, since both were read
in full context in both languages; for the aggregate fidelity statistics it is
a real if minor caveat.

**One paragraph could not be matched at all.** `TBWTT-1:41` failed the probe
against F and its cause was not run to ground. It does not bear on either cited
passage.

## Outcome

The claim's **substance is confirmed**; its **quotation practice needs
correction**. No status advance is recommended, because a review with an
outstanding component cannot support one.

Recommended, in order:

1. **Re-attribute the English quotations.** In
   [`docs/evidence/woh-claim-0070-evidence.md`](../evidence/woh-claim-0070-evidence.md)
   and
   [`source-notes/the-book-which-tells-the-truth.md`](../../source-notes/the-book-which-tells-the-truth.md),
   quote the published English (E p. 8, E p. 11) as the English witness, cite
   the French as the base text, and label the digitization's English as an
   AI-assisted project rendering wherever it is shown. This is a factual
   correction and should not wait on the RFC.

2. **Record the digitization's translation provenance in the source note.** The
   note's "Inspected representation" section should state that D's non-French
   text is machine-generated, dated, and attributed to a named model.

3. **Add the critical sources to `source_references`.** `woh-claim-0070` cites
   only its canonical basis, so `scripts/wantlist.py` does not list it against
   the critical literature its own evidence map says a review needs. Adding
   `aliens-adored` and the Dericquebourg chapter with `role: critical` and
   `access: metadata_only` makes the blocker visible to tooling. (This is the
   feedback rule proposed in RFC 0007 §"Feedback into source references".)

4. **Leave `evidence_status` at `scoped`.** Advancement should wait for the
   source-critical component.

5. **Consider whether the 2005-only collation warrants a revision trigger.**
   The claim's existing trigger anticipates that "edition collation … materially
   changes the wording". Collation has now been performed and changed nothing
   material, but only back to 2005. A narrower trigger naming the first editions
   would record what remains open.

Two findings fall outside this claim and are logged for their own repos rather
than actioned here:

- `data-sources/pdf/_combined/intelligent-design-en.json` lists its third
  contained work as *Sensual Meditation*. The volume's own table of contents
  gives book three as *Let's Welcome the Extra-Terrestrials*; *Sensual
  Meditation* is a section inside book two (p. 201). The French sidecar carries
  the same error.
- The bibliography holds three separate records for *Aliens Adored*
  (`aliens-adored`, `aliens-adored-ra-l-s-ufo-religion`, and a third with a
  truncated descriptive slug). They should be merged before the work is
  acquired, or the holding will bind to one and leave two dangling.

## Sign-off

Not signed. All five recommendations in the Outcome section were applied on
2026-08-31 (1 and 2 as quotation corrections, 3 under the feedback rule adopted
by ADR 0009, 4 by leaving the status alone, 5 by narrowing the first revision
trigger to the uncollated first printings). The record itself grants no status:
the claim remains `scoped` pending the outstanding source-critical component.

| Field | Value |
| --- | --- |
| Reviewer | — |
| Date | — |
| Status granted | none; claim remains `scoped` |
