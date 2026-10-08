#!/usr/bin/env python3
"""Chunk md/ (EN) and md_zh/ (ZH) by heading and write static BM25 indexes:
rag/index-en.js and rag/index-zh.js (loaded lazily by the browser widget).

The tokenizer and scoring here must match rag/widget.js exactly.
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_CHARS = 1800

_word = re.compile(r"[a-z0-9]+")
_cjk = re.compile(r"[一-鿿]+")


def tokenize(text):
    """Latin words + CJK unigrams and bigrams."""
    t = text.lower()
    toks = _word.findall(t)
    for run in _cjk.findall(t):
        toks += list(run)
        toks += [run[i:i + 2] for i in range(len(run) - 1)]
    return toks


def page_url(lang, rel):
    """rel: path of the md file below md/ or md_zh/ -> page URL relative to the site root."""
    h = rel.with_suffix(".html").as_posix()
    return ("zh/" + h) if lang == "zh" else h


def chunks_of(path, lang, rel):
    text = path.read_text(encoding="utf-8")
    cur_title, buf, fence = "", [], False
    sections = []
    for line in text.splitlines():
        if line.startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"(#{1,6}) (.*)", line)
        if m and m.group(2).strip() in ("Bibliography", "参考文献"):
            break  # the citation list at the end of the FAQ file is not useful for Q&A
        if m:
            if buf:
                sections.append((cur_title, "\n".join(buf)))
            cur_title, buf = m.group(2).strip(), []
        else:
            buf.append(line)
    if buf:
        sections.append((cur_title, "\n".join(buf)))
    out = []
    for title, body in sections:
        body = re.sub(r"!\[\]\([^)]*\)", "", body).strip()
        if len(body) < 40:
            continue
        # split long sections on blank lines, keeping fenced blocks whole
        paras, cur, size = [], [], 0
        for blk in re.split(r"\n\s*\n", body):
            if size + len(blk) > MAX_CHARS and cur:
                paras.append("\n\n".join(cur)); cur, size = [], 0
            cur.append(blk); size += len(blk)
        if cur:
            paras.append("\n\n".join(cur))
        for p in paras:
            out.append({"t": title or path.stem, "x": p, "u": page_url(lang, rel), "f": rel.as_posix()})
    return out


def build_lang(chunks):
    """Postings are flat arrays [chunkIdx, tf, chunkIdx, tf, ...] per term; idf is derived from df in the client."""
    post, lens = {}, []
    for i, c in enumerate(chunks):
        # the title is counted twice so heading matches rank higher
        t = tokenize(c["t"] + " " + c["t"] + " " + c["x"])
        lens.append(len(t))
        for w, f in Counter(t).items():
            post.setdefault(w, []).extend((i, f))
    return {"chunks": chunks, "post": post, "lens": lens, "avg": sum(lens) / len(lens)}


def build():
    for lang, root in (("en", ROOT / "md"), ("zh", ROOT / "md_zh")):
        chunks = []
        for f in sorted(root.rglob("*.md")):
            if f.name in ("index.md", "README.md"):
                continue
            chunks += chunks_of(f, lang, f.relative_to(root))
        data = build_lang(chunks)
        out = ROOT / "rag" / f"index-{lang}.js"   # a script, not JSON: <script> loading also works from file://
        payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        out.write_text(f'(window.ASK_IDX=window.ASK_IDX||{{}}).{lang}={payload};', encoding="utf-8")
        print(f"{lang}: {len(chunks)} chunks, {len(data['post'])} terms -> {out.name} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build()
