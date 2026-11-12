---
title: Research
status: draft
version: 0.1.0
last_reviewed: 2026-08-02
---

# Research

This directory contains open research questions and review programmes. It does
not contain accepted findings merely because a question matters to the
framework.

- [Research agenda](research-agenda.md)
- [Research question template](research-question-template.md)
- [Should claim 0001 be split into four claims?](decompose-claim-0001.md)
- [Canon close reading (November 2026)](canon-close-reading/README.md) — draft notes from a paragraph-level reading of the three books; proposals pending founder review

## Review desk

`mise run review` (or `python3 scripts/build_review_app.py`) writes
`build/review/index.html`: one local file that shows every claim record with its
specification and evidence map, all documents, the canon passages cited, and the
review queue (`canon-close-reading/review-queue.json`). Decisions made in the
app stay in the browser until exported; save the export as
`review-decisions.json` beside the queue and the next build shows them as
recorded. The app never writes to the repository.
