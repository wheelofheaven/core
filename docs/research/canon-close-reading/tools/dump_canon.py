#!/usr/bin/env python3
"""Flatten the three canon books from data-library into one-paragraph-per-line text dumps.

Usage: python3 dump_canon.py <data-library dir> <out dir>
Writes {TBWTT,ETTMTTP,LWTE}.{fr,en}.txt with lines `REF<TAB>[speaker]<TAB>text`.
The French (`text`) is the source of record; `i18n.en` is the project's translation.
"""
import glob, json, re, sys
from pathlib import Path

BOOKS = [("the-book-which-tells-the-truth", "TBWTT"),
         ("extraterrestrials-took-me-to-their-planet", "ETTMTTP"),
         ("lets-welcome-the-extraterrestrials", "LWTE")]

def one(s):
    return " ".join((s or "").split())

def main(lib, out):
    Path(out).mkdir(parents=True, exist_ok=True)
    for book, sig in BOOKS:
        files = sorted(glob.glob(f"{lib}/{book}/chapter-*.json"),
                       key=lambda x: int(re.search(r"(\d+)\.json", x).group(1)))
        with open(f"{out}/{sig}.fr.txt", "w", encoding="utf-8") as fr, \
             open(f"{out}/{sig}.en.txt", "w", encoding="utf-8") as en:
            for f in files:
                d = json.load(open(f, encoding="utf-8"))
                c = re.search(r"(\d+)\.json", f).group(1)
                for o in (fr, en):
                    o.write(f"\n### {sig} chapter {c}: {d.get('title')}\n")
                for p in d["paragraphs"]:
                    fr.write(f"{p['refId']}\t[{p.get('speaker')}]\t{one(p['text'])}\n")
                    en.write(f"{p['refId']}\t[{p.get('speaker')}]\t{one((p.get('i18n') or {}).get('en'))}\n")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
