#!/usr/bin/env python3
"""Check every `QUOTE[REF]: … ENDQUOTE` line of a note against the French canon dumps.

Usage: python3 verify_quotes.py <dump dir from dump_canon.py> <note.md> [<note.md> ...]
A quotation passes when each of its parts (split at […] / …) is a substring of the cited
paragraph after whitespace, quote-mark and case normalisation. Exit status 1 on any failure.
"""
import re, sys, unicodedata

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a in "’«»“”":
        s = s.replace(a, "'" if a == "’" else '"')
    return re.sub(r"\s+", " ", s).strip().lower()

def main(dumps, notes):
    paras = {}
    for sig in ("TBWTT", "ETTMTTP", "LWTE"):
        for line in open(f"{dumps}/{sig}.fr.txt", encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) == 3:
                paras[p[0]] = p[2]
    pat = re.compile(r"QUOTE\[((?:TBWTT|ETTMTTP|LWTE)-\d+:\d+)\]:\s*(.+?)\s*(?:ENDQUOTE|$)")
    bad = 0
    for note in notes:
        ok = 0
        for i, line in enumerate(open(note, encoding="utf-8"), 1):
            for m in pat.finditer(line):
                ref, q = m.group(1), m.group(2)
                parts = [x for x in re.split(r"\s*(?:\[\.\.\.\]|\[…\]|…)\s*", q) if x.strip()]
                src = norm(paras.get(ref, ""))
                if src and all(norm(x) in src for x in parts):
                    ok += 1
                else:
                    bad += 1
                    print(f"FAIL {note}:{i} {ref}: {q[:90]}")
        print(f"{note}: {ok} quotes verified")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
