# Brief: check the first Raëlian Message's biblical commentary against one Sendy book

Context: Wheel of Heaven is comparing Raël's first Message, *Le Livre qui dit la vérité* (encounter dated 13 Dec 1973, printed autumn 1974), with Jean Sendy's books (1963–1970). The question is: how much of the Message's biblical commentary could Sendy's books have supplied? The answer must be evidence-based in both directions. Do not try to prove borrowing or independence; report what the book contains.

Inputs:
- Inventory of the Message's commentary: `/private/tmp/claude-501/-Users-zara-Development-github-com-wheelofheaven/ee99cb14-1f81-4f66-b75e-0eef5019b810/scratchpad/inventory/tbwtt-inventory.json` (226 items; fields: id, tbwtt, bible_ref, topic, quoted, message_reading, distinctive_detail, search_terms_fr).
- French Message text if you need more context: `/private/tmp/sendy-study/the-book-which-tells-the-truth.txt` (one paragraph per line, prefixed `TBWTT-c:p`).
- YOUR assigned Sendy book (one only) — given in your task message. It is a later digital edition (EPUB/PDF extraction); treat it as such.

Method:
1. Read your book through enough to know its structure (chapter headings; the extraction has `### OEBPS/PLn.xhtml` markers for EPUBs). For each inventory item, search the book with the item's search terms, biblical names, verse numbers in Sendy's style (e.g. `GEN. VI, 7`, `Ez`, `Ézéchiel`), and synonyms; then read the hits in context. Do not decide "absent" from one failed grep — try several terms.
2. Classify each item for this book:
   - `same` — Sendy treats the same passage with substantially the same specific technological/historical reading (quote the French).
   - `similar` — same passage, related technological reading, but a materially different mechanism, agent, or purpose (quote + one-line difference).
   - `mentioned` — the passage/figure is mentioned or discussed, but without the Message's kind of reading (or with a non-technological reading).
   - `absent` — not found after a real search.
3. Reverse direction: list Sendy's own distinctive biblical or mythological readings in this book that do NOT appear in the Message (e.g. kesheth/bow on the Moon, Nefilim as "Tombés", Gérants, Iahvé as Principle). Up to ~25, each with a locator and short French quote.

Output — write JSON to `/private/tmp/claude-501/-Users-zara-Development-github-com-wheelofheaven/ee99cb14-1f81-4f66-b75e-0eef5019b810/scratchpad/inventory/check-<BOOK_KEY>.json`:
```
{ "book": "...", "book_key": "...",
  "items": [ { "id": "I001", "status": "same|similar|mentioned|absent", "locator": "chapter n / PLn / line or page", "quote_fr": "short verbatim quote or null", "note": "one line" } ...all 226... ],
  "sendy_only": [ { "locator": "...", "passage": "Gen 9:13", "reading": "one line", "quote_fr": "..." } ] }
```
Every item id in the inventory must appear exactly once. Quotes must be verbatim from your book file (short; under ~40 words). Be conservative: only `same` when the specific reading — not just the broad premise of "visitors from the sky" — matches.

Also write a ~300-word markdown summary to `check-<BOOK_KEY>.md` in the same directory: counts by status, the strongest `same` items, and notable Sendy-only readings.

Do not edit any other file. Do not commit. Final message: counts by status and the path.
