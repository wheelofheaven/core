---
title: Atrahasis III vi in the project text and the Sippar edition
status: draft
version: 0.1.1
last_reviewed: 2026-11-22
---

# Atrahasis III vi in the project text and the Sippar edition

This note follows up the alignment question left open by the
[procedural comparison](procedural-comparison.md) and by
[ADR 0015](../../../decisions/0015-flood-claim-0010-revision.md): whether
the lion and famine alternatives printed in the project text at
`ATRA-WOH-III:vi.21–24` correspond to anything in Atrahasis.

## Sources

- **Project text:** `data-library/atrahasis-woh/chapter-3.json`, segment
  `enlil-rage-and-enki-defense`, lines `ATRA-WOH-III:vi.5–24`, at library
  commit `1dd31c5` (the pin used by the site). Its metadata calls it a
  "provisional composite reconstruction citing Lambert & Millard 1969 and
  Foster 2005"; "individual readings and edition coordinates remain
  unverified".
- **SEAL no. 1517**, *Atraḫasis OB III (Sippar)*,
  <https://seal.huji.ac.il/node/1517?tid=80>, read 2026-11-21. Manuscript
  BM 78942+78971+80385 (+) MAH 16064, sigla C1 (+) C2. SEAL lists
  Lambert/Millard 1969 for the copy (after p. 198) and among its editions,
  with George/al-Rawi 1996 and Wasserman 2020. Column vi is C1.
- **Not inspected:** the printed Lambert–Millard 1969 transliteration and
  translation, and Millard's 1966 thesis (the SOAS repository refused
  automated access with HTTP 403; the former `eprints.soas.ac.uk` host no
  longer resolves). Foster's translation as adapted by Livius does not
  include column vi.

## Comparison

SEAL's transliteration of C1 vi 16–27 was read in full. The SEAL
translation of column vi was not retrieved verbatim; the content
descriptions below rest on the transliteration and are kept general.

| Project line | Project transliteration (abridged) and English | SEAL C1 | Finding |
| --- | --- | --- | --- |
| vi.15–16 | Enki opens his mouth and addresses the great gods | vi 16–17 | Same content; project numbering is one line lower. |
| vi.17 | *i-na ba-li-ku-nu-ma e-te-pu-uš*, "I did it, indeed, against your will" | vi 18, *[lu-ú e]-pu-uš i-na pa-ni-ku-n[u]* | Different wording. SEAL's line has *ina pānīkunu*, not *ina balīkunu*. |
| vi.18 | *aš-šum na-ap-ša-tim uš-te-ṣi*, "I saw to it that life was preserved" | vi 19, *[ú-uš-t]a-ṣi-ra na-pí-iš-[tam …]* | Same sense; different verb form and spelling. |
| — | (no counterpart) | vi 20–24 | Enki's address to Enlil as sage of the gods, the flood brought about (restored *[ki-i la ta-am-li-ik-ma a-b]u-ba*), and a saying about the heart. Not represented in the project text. |
| vi.19–20 | "Lay the penalty on the wrongdoer, and his punishment on the transgressor" | vi 25, *[be-el ar-n]im šu-ku-un še-re-et-ka* | The penalty line is attested, but at vi 25, after the address, and as one line. |
| vi.21–24 | *aš-šu la ta-ša-ak-ka-nu a-bu-ba / li-ib-ši-ma la-ab-bu-um-ma ni-ši li-im-ṭi* …, "Instead of your bringing on a flood, let a lion arise …; … let famine arise …" | vi 20–27 preserved; vi 28–37 lost | **No counterpart.** No line in the SEAL transliteration of Tablet III contains a lion, wolf, famine or plague alternative. The preserved lines at this point carry other content. |
| (segment note) | "Enki's proposal of measured checks (lion, wolf, famine, plague)" in the lacuna before vii | vi 28–37 lost | The note supplies content for a gap that the edition does not restore. |

The lion and famine lines resemble Ea's speech in Gilgamesh XI
(Kovacs/Livius 11.180–197; project `GILG-WOH-11:179–187`), where the
four alternatives are attested. Their wording does not match the project's
Gilgamesh transliteration either: `GILG-WOH-11:184` reads *ki-i lā taš-ku-na
a-bu-ba nēšu lit-bā-ma nišī liṣaḫḫir*, against the Atrahasis file's *aš-šu la
ta-ša-ak-ka-nu a-bu-ba / li-ib-ši-ma la-ab-bu-um-ma ni-ši li-im-ṭi* (a
different lion word, verb and refrain). This describes the resemblance; it
is not a finding about how the lines were produced.

## Conclusion

1. `ATRA-WOH-III:vi.21–24` does not correspond to the Sippar manuscript as
   edited in SEAL, whose copy is Lambert and Millard's. The preserved text
   at that point differs, and no Atrahasis line inspected in this project
   (SEAL I–III, Livius/Foster) names the four alternatives.
2. The project's `vi.15–20` follow the passage's sense with different
   readings and a one-line offset, and omit SEAL vi 20–24.
3. The segment note supplying "lion, wolf, famine, plague" for the gap
   before column vii has no edition support.
4. For `woh-claim-0010` 0.2.0 nothing changes: the record already cites
   the list to Gilgamesh XI and excludes attributing it to Atrahasis. The
   revision trigger for an Atrahasis edition is met as far as the SEAL
   edition goes; the exclusion should stay until the printed 1969 edition
   is checked, since that is the edition the project text cites.

## Limits

This is a comparison of transliterations, not a collation of the tablet
or a new reading. It does not establish what Lambert and Millard 1969
print at vi 21–24, although SEAL's edition of the same manuscript, with
their copy, gives no basis for the project lines. It proposes no
correction to the library text; repairing column vi requires the
library's translation pipeline and the founder's sign-off.

## Library status

On 2026-11-22 the founder chose to withdraw the four lines rather than
keep them under a warning (data-library `dfaa634`, pinned by www
`d9513d16b5a` and api `68cc125`). `ATRA-WOH-III:vi.21–24` no longer exist
in the library text. Segment `withdrawn-lines-vi-21-24` of
`atrahasis-woh/chapter-3.json` and `source-akk-3.json` keeps their place
with no lines and a note naming what the Sippar manuscript preserves
there (SEAL C1 vi 20–24). Those lines are not rendered: SEAL's edition is
published under "a Creative Commons (CC) BY-NC-ND license" (no version
stated; "No commercial use is allowed") and cannot enter the CC0 library without the
editors' permission, and no openly licensed edition of Tablet III has
been found. The reviewer verdicts for the withdrawn line ids stay in
`chapter-3.json` as audit record.
