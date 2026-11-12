#!/usr/bin/env python3
"""Build a single-file local review app for the research core.

Usage: python3 scripts/build_review_app.py [--library <data-library dir>] [--out build/review/index.html]

Reads the claim catalog and records, their specifications and evidence maps, source
notes, decisions, RFCs, methodology and research notes, plus every `review-queue.json`
under docs/research, and writes one self-contained HTML file (no network, no server).
With --library, canon paragraphs cited anywhere in the core are embedded so locators
such as TBWTT-2:10 open the French and English text.

The app is read-only towards the repository. Review decisions are kept in the browser
and exported as JSON; save that export as `review-decisions.json` beside a queue file
and the next build shows the decisions as recorded.
"""
import argparse, glob, html, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS = {"TBWTT": "the-book-which-tells-the-truth",
         "ETTMTTP": "extraterrestrials-took-me-to-their-planet",
         "LWTE": "lets-welcome-the-extraterrestrials"}
REF = re.compile(r"\b((?:TBWTT|ETTMTTP|LWTE)-\d+:\d+)\b")
CLAIM = re.compile(r"\b(woh-claim-\d{4})\b")


# ---------- markdown ----------

class MD:
    def __init__(self, path, known):
        self.path, self.known = path, known

    def href(self, url):
        if re.match(r"^[a-z]+:", url):
            return url, True
        target, _, _frag = url.partition("#")
        if not target:
            return None, False
        p = os.path.normpath(os.path.join(os.path.dirname(self.path), target)).replace(os.sep, "/")
        m = re.search(r"model/claims/(woh-claim-\d{4})\.json$", p)
        if m:
            return "#/claim/" + m.group(1), False
        if p in self.known:
            return "#/doc/" + p, False
        if p.rstrip("/") + "/README.md" in self.known:
            return "#/doc/" + p.rstrip("/") + "/README.md", False
        return None, False

    def inline(self, s):
        codes = []
        def stash(m):
            codes.append("<code>" + html.escape(m.group(1)) + "</code>")
            return "\x00%d\x00" % (len(codes) - 1)
        s = re.sub(r"`([^`\n]+)`", stash, s)
        s = html.escape(s, quote=False)
        s = re.sub(r"QUOTE\[([A-Z]+-\d+:\d+)\]:\s*(.+?)\s*ENDQUOTE",
                   lambda m: '<q class="cq">%s</q> <a class="ref" href="#/passage/%s">%s</a>' % (m.group(2), m.group(1), m.group(1)), s)
        def link(m):
            h, ext = self.href(html.unescape(m.group(2)))
            if h is None:
                return m.group(1)
            return '<a href="%s"%s>%s</a>' % (html.escape(h), ' target="_blank" rel="noopener"' if ext else "", m.group(1))
        s = re.sub(r"\[([^\]\n]+)\]\(([^)\s]+)\)", link, s)
        s = re.sub(r"\*\*([^*\n]+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![*\w])\*([^*\n]+?)\*(?!\w)", r"<em>\1</em>", s)
        out, depth = [], 0
        for part in re.split(r"(<[^>]+>)", s):
            if part.startswith("<"):
                if part.startswith("<a"): depth += 1
                elif part.startswith("</a"): depth -= 1
                out.append(part)
            elif depth:
                out.append(part)
            else:
                part = REF.sub(r'<a class="ref" href="#/passage/\1">\1</a>', part)
                part = CLAIM.sub(r'<a class="cid" href="#/claim/\1">\1</a>', part)
                out.append(part)
        s = "".join(out)
        return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], s)

    def blocks(self, lines):
        out, i, n = [], 0, len(lines)
        LI = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
        while i < n:
            ln = lines[i]
            if not ln.strip():
                i += 1; continue
            if ln.lstrip().startswith("```"):
                j = i + 1; buf = []
                while j < n and not lines[j].lstrip().startswith("```"):
                    buf.append(lines[j]); j += 1
                out.append("<pre><code>" + html.escape("\n".join(buf)) + "</code></pre>"); i = j + 1; continue
            m = re.match(r"^(#{1,6})\s+(.*?)\s*#*$", ln)
            if m:
                lv = len(m.group(1))
                out.append("<h%d>%s</h%d>" % (lv, self.inline(m.group(2)), lv)); i += 1; continue
            if re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", ln):
                out.append("<hr>"); i += 1; continue
            if ln.lstrip().startswith("|") and i + 1 < n and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]) and "-" in lines[i + 1]:
                rows = []; j = i
                while j < n and lines[j].lstrip().startswith("|"):
                    rows.append(lines[j]); j += 1
                def cells(r):
                    r = r.strip().strip("|")
                    return [c.strip() for c in re.split(r"(?<!\\)\|", r)]
                t = ["<div class='tw'><table><thead><tr>"] + ["<th>%s</th>" % self.inline(c) for c in cells(rows[0])] + ["</tr></thead><tbody>"]
                for r in rows[2:]:
                    t.append("<tr>" + "".join("<td>%s</td>" % self.inline(c) for c in cells(r)) + "</tr>")
                t.append("</tbody></table></div>"); out.append("".join(t)); i = j; continue
            if ln.lstrip().startswith(">"):
                buf = []; j = i
                while j < n and lines[j].lstrip().startswith(">"):
                    buf.append(re.sub(r"^\s*>\s?", "", lines[j])); j += 1
                out.append("<blockquote>" + self.blocks(buf) + "</blockquote>"); i = j; continue
            m = LI.match(ln)
            if m:
                base = len(m.group(1)); ordered = m.group(2)[0].isdigit(); items = []; j = i
                while j < n:
                    mm = LI.match(lines[j])
                    if mm and len(mm.group(1)) == base:
                        items.append([mm.group(3)]); j += 1
                    elif not lines[j].strip():
                        k = j
                        while k < n and not lines[k].strip(): k += 1
                        if k < n and (len(lines[k]) - len(lines[k].lstrip()) > base):
                            items[-1].append(""); j = k
                        elif k < n and LI.match(lines[k]) and len(LI.match(lines[k]).group(1)) == base:
                            j = k
                        else:
                            break
                    elif len(lines[j]) - len(lines[j].lstrip()) > base:
                        items[-1].append(lines[j]); j += 1
                    elif LI.match(lines[j]) or re.match(r"^(#{1,6}\s|\s*```|\s*\|)", lines[j]):
                        break
                    else:
                        items[-1].append(lines[j]); j += 1  # lazy continuation
                tag = "ol" if ordered else "ul"; li = []
                for it in items:
                    body = [it[0]]
                    rest = it[1:]
                    if rest:
                        ind = min((len(x) - len(x.lstrip()) for x in rest if x.strip()), default=0)
                        body += [x[ind:] if x.strip() else "" for x in rest]
                    inner = self.blocks(body)
                    if inner.count("<p>") == 1 and inner.startswith("<p>") and inner.endswith("</p>"):
                        inner = inner[3:-4]
                    li.append("<li>" + inner + "</li>")
                out.append("<%s>%s</%s>" % (tag, "".join(li), tag)); i = j; continue
            buf = [ln]; j = i + 1
            while j < n and lines[j].strip() and not re.match(r"^(#{1,6}\s|\s*```|\s*>|\s*\|)", lines[j]) and not LI.match(lines[j]):
                buf.append(lines[j]); j += 1
            out.append("<p>" + self.inline(" ".join(x.strip() for x in buf)) + "</p>"); i = j
        return "\n".join(out)

    def render(self, text):
        return self.blocks(text.replace("\r\n", "\n").split("\n"))


def title_of(text, fallback):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return re.sub(r"[*`]", "", m.group(1)).strip() if m else fallback


def group_of(p):
    if p.startswith("docs/research/"):
        parts = p.split("/")
        return "Research: " + parts[2].replace("-", " ") if len(parts) > 3 else "Research"
    for pre, g in (("docs/framework/", "Specifications"), ("docs/evidence/", "Evidence maps"),
                   ("source-notes/", "Source notes"), ("decisions/", "Decisions"), ("rfcs/", "RFCs"),
                   ("docs/methodology/", "Methodology"), ("docs/foundations/", "Foundations"),
                   ("docs/reviews/", "Reviews")):
        if p.startswith(pre):
            return g
    return "Repository"


def git(*a):
    try:
        return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--library", help="data-library directory (optional; embeds cited canon paragraphs)")
    ap.add_argument("--out", default="build/review/index.html")
    a = ap.parse_args()
    if not a.library:
        for cand in ("../www.wheelofheaven.world/data/library", "../data-library"):
            if (ROOT / cand / BOOKS["TBWTT"]).is_dir():
                a.library = str(ROOT / cand)
                break

    paths = sorted(str(p.relative_to(ROOT)).replace(os.sep, "/") for p in ROOT.rglob("*.md")
                   if ".git/" not in str(p) and "/build/" not in str(p) and "template" not in p.name)
    known = set(paths)
    docs, alltext = {}, []
    for p in paths:
        text = (ROOT / p).read_text(encoding="utf-8")
        alltext.append(text)
        docs[p] = {"title": title_of(text, p), "group": group_of(p), "html": MD(p, known).render(text),
                   "claims": sorted(set(CLAIM.findall(text)))}

    cat = json.loads((ROOT / "model/catalog.json").read_text(encoding="utf-8"))
    claims = []
    for c in cat["claims"]:
        rec = json.loads((ROOT / "model" / c["record"]).read_text(encoding="utf-8"))
        alltext.append(json.dumps(rec, ensure_ascii=False))
        spec = os.path.normpath(os.path.join("model", c.get("specification", ""))).replace(os.sep, "/") if c.get("specification") else None
        ev = None
        if spec:
            cand = spec.replace("docs/framework/", "docs/evidence/")
            ev = cand if cand in known else None
        for s in rec.get("source_references", []):
            if s.get("note"):
                q = os.path.normpath(os.path.join("model/claims", s["note"])).replace(os.sep, "/")
                s["note_doc"] = q if q in known else None
        rec["_spec"] = spec if spec in known else None
        rec["_evidence"] = ev
        claims.append(rec)

    queues, decisions = [], {}
    for qf in sorted(ROOT.glob("docs/research/**/review-queue.json")):
        q = json.loads(qf.read_text(encoding="utf-8"))
        rel = str(qf.relative_to(ROOT)).replace(os.sep, "/")
        md = MD(rel, known)
        for it in q["items"]:
            it["queue"] = rel
            it["html"] = md.inline(it.get("summary", ""))
            it["title_html"] = md.inline(it["title"])
            alltext.append(" ".join(it.get("refs", [])))
        queues.append({"path": rel, "updated": q.get("updated"), "note": q.get("note"), "items": q["items"]})
        df = qf.with_name("review-decisions.json")
        if df.exists():
            decisions.update(json.loads(df.read_text(encoding="utf-8")).get("decisions", {}))

    passages = {}
    if a.library:
        wanted = set(REF.findall("\n".join(alltext)))
        for sig, slug in BOOKS.items():
            for f in glob.glob(os.path.join(a.library, slug, "chapter-*.json")):
                d = json.load(open(f, encoding="utf-8"))
                for p in d.get("paragraphs", []):
                    if p.get("refId") in wanted:
                        passages[p["refId"]] = {"speaker": p.get("speaker"), "chapter": d.get("title"),
                                                "fr": " ".join((p.get("text") or "").split()),
                                                "en": " ".join(((p.get("i18n") or {}).get("en") or "").split())}

    data = {"built": git("log", "-1", "--format=%cs"), "commit": git("rev-parse", "--short", "HEAD"),
            "branch": git("rev-parse", "--abbrev-ref", "HEAD"), "catalog": {k: cat.get(k) for k in ("catalog_version", "status", "last_reviewed")},
            "claims": claims, "docs": docs, "queues": queues, "recorded": decisions, "passages": passages}
    page = (Path(__file__).with_name("review_app_template.html")).read_text(encoding="utf-8")
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = ROOT / a.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page.replace("/*__DATA__*/null", blob), encoding="utf-8")
    print("wrote %s  (%d claims, %d documents, %d review items, %d passages, %.1f MB)" % (
        out, len(claims), len(docs), sum(len(q["items"]) for q in queues), len(passages), out.stat().st_size / 1e6))


if __name__ == "__main__":
    sys.exit(main())
