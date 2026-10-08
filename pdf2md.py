#!/usr/bin/env python3
"""Convert the XeTeX-built Gaussian 16 PDFs to Markdown using font information."""
import re
import sys
from pathlib import Path

import pymupdf

LIG = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl"}
BULLET_FONTS = ("MSAM10", "CMSY10")
HEADER_Y = 50  # running header band (page number / section title)
FOOTER_Y = 800


def clean(t):
    for k, v in LIG.items():
        t = t.replace(k, v)
    return t.replace("­", "")


def kind(font):
    if "Mon" in font:
        return "code"
    if "Demi" in font:
        return "head"
    return "text"


def style(font):
    b = "Medi" in font or "Bold" in font
    i = "Ital" in font
    return b, i


def render_spans(spans):
    """Join spans of one line into inline markdown, grouping runs of equal style."""
    runs = []  # [key, text]
    for s in spans:
        t = clean(s["text"])
        if not t:
            continue
        f = s["font"]
        key = ("code", False, False) if kind(f) == "code" else ("text",) + style(f)
        if not t.strip():
            if runs:
                runs[-1][1] += t  # whitespace joins the preceding run
            else:
                runs.append([key, t])
            continue
        if runs and runs[-1][0] == key:
            runs[-1][1] += t
        else:
            if runs and runs[-1][1][-1:].isalnum() and t[:1].isalnum() and "Mon" not in f:
                runs[-1][1] += " "  # TeX kerns separate a term from its definition
            runs.append([key, t])
    out = []
    i = 0
    while i < len(runs):
        key, t = runs[i]
        if key[0] == "text" and key[1]:
            # gather consecutive bold runs (italic parts become _x_ inside the bold span)
            j, parts = i, []
            while j < len(runs) and runs[j][0][0] == "text" and runs[j][0][1]:
                k, tt = runs[j]
                core = tt.strip()
                if core and k[2]:
                    core = tt.replace(core, f"_{core}_")
                    parts.append(core)
                else:
                    parts.append(tt)
                j += 1
            joined = "".join(parts)
            core = joined.strip()
            lead = joined[: len(joined) - len(joined.lstrip())]
            trail = joined[len(joined.rstrip()):]
            out.append(lead + (f"**{core}**" if core else "") + trail)
            i = j
            continue
        core = t.strip()
        if not core:
            out.append(t)
        else:
            lead = t[: len(t) - len(t.lstrip())]
            trail = t[len(t.rstrip()):]
            if key[0] == "code":
                core = "`" + core.replace("`", "'") + "`"
            elif key[2]:
                core = f"*{core}*"
            out.append(lead + core + trail)
        i += 1
    return re.sub(r"[ \t]+", " ", "".join(out)).strip()


def page_lines(page):
    d = page.get_text("dict")
    lines, images = [], []
    for b in d["blocks"]:
        if b["type"] == 1:
            images.append(b)
            continue
        for l in b["lines"]:
            if not any(s["text"].strip() for s in l["spans"]):
                continue
            x0, y0, x1, y1 = l["bbox"]
            lines.append({"x": x0, "y": y0, "x1": x1, "spans": l["spans"]})
    lines.sort(key=lambda l: (round(l["y"] / 3), l["x"]))
    return lines, images


def merge_rows(lines):
    """Merge fragments sharing a baseline (e.g. section number + title)."""
    rows = []
    for l in lines:
        if rows and abs(rows[-1]["y"] - l["y"]) < 3:
            rows[-1]["spans"] += l["spans"]
            rows[-1]["x1"] = max(rows[-1]["x1"], l["x1"])
        else:
            rows.append({**l, "spans": list(l["spans"])})
    return rows


def convert(pdf, outdir, name):
    doc = pymupdf.open(pdf)
    imgdir = outdir / "images" / name
    md = []  # list of blocks (strings)
    para = []  # current paragraph lines
    code = []
    nimg = 0

    def flush_para():
        nonlocal para
        if para:
            txt = ""
            for ln in para:
                if txt.endswith("-") and ln[:1].islower() and re.search(r"[a-z]-$", txt):
                    txt = txt[:-1] + ln
                else:
                    txt = (txt + " " + ln) if txt else ln
            md.append(txt)
            para = []

    def flush_code():
        nonlocal code
        if code:
            md.append("```\n" + "\n".join(code).rstrip() + "\n```")
            code = []

    for pno, page in enumerate(doc):
        lines, images = page_lines(page)
        rows = merge_rows(lines)
        if re.search(r"(?:\. ){6,}", page.get_text()):
            continue  # table-of-contents page
        prev_y = None
        for r in rows:
            allspans = r["spans"]
            spans = [s for s in allspans if s["text"].strip()]
            if not spans:
                continue
            if r["y"] < HEADER_Y and pno > 2:
                continue  # running header
            if r["y"] > FOOTER_Y:
                continue
            first = spans[0]
            if ". . . ." in "".join(x["text"] for x in spans):
                continue  # table-of-contents leader line
            fonts = {kind(s["font"]) for s in spans}
            text = re.sub(r"\s+", " ", clean(" ".join(s["text"].strip() for s in spans))).strip()
            gap = None if prev_y is None else r["y"] - prev_y
            prev_y = r["y"]

            # headings: Gothic Demi (section number + title) or chapter titles
            if fonts == {"head"} and re.match(r"^(\d+(\.\d+)*|[A-Z](\.\d+)*)\b", text) and len(text) < 120:
                flush_para(); flush_code()
                m = re.match(r"^(\S+)\s+(.*)$", text)
                num, title = (m.group(1), m.group(2)) if m else (text, "")
                level = min(num.count(".") + 2, 6) if "." in num else 2
                md.append("#" * level + " " + num + " " + title)
                continue
            if fonts == {"head"} and first["size"] > 11.5:
                flush_para(); flush_code()
                md.append("## " + text)
                continue

            if fonts == {"code"} or (kind(first["font"]) == "code" and r["x"] > 60 and "text" not in fonts):
                flush_para()
                code.append(clean("".join(s["text"] for s in spans)).rstrip())
                continue
            # code with trailing italic comment
            if kind(first["font"]) == "code" and r["x"] > 60 and (fonts <= {"code", "text"}):
                flush_para()
                code.append(" ".join(clean(s["text"]).strip() for s in spans if s["text"].strip()))
                continue
            flush_code()

            # bullet items
            if first["font"].startswith(BULLET_FONTS) and len(first["text"].strip()) <= 2:
                flush_para()
                items, cur = [], []
                for sp in allspans:
                    if sp["font"].startswith(BULLET_FONTS) and len(sp["text"].strip()) <= 2:
                        if cur:
                            items.append(cur)
                        cur = []
                    else:
                        cur.append(sp)
                items.append(cur)
                for it in items:
                    flush_para()
                    para.append("- " + render_spans(it))
                continue

            line = render_spans(allspans)
            # a line made entirely of bold text starts its own paragraph (keyword terms)
            all_bold = style(first["font"])[0] and kind(first["font"]) == "text"
            if all_bold and r["x"] < 70:
                flush_para()
                md.append(line)
                continue
            if gap is not None and gap > 24 and r["x"] < 100 or (para and r["x"] > 75 and r["x"] < 82 and not para[-1].startswith("- ") and gap and gap > 19):
                flush_para()
            para.append(line)

        flush_para(); flush_code()
        # images
        for im in images:
            try:
                imgdir.mkdir(parents=True, exist_ok=True)
                nimg += 1
                ext = im.get("ext", "png")
                fn = imgdir / f"p{pno + 1:03d}_{nimg}.{ext}"
                fn.write_bytes(im["image"])
                md.append(f"![]({fn.relative_to(outdir)})")
            except Exception as e:  # noqa
                print("image fail", pno, e, file=sys.stderr)

    out = outdir / f"{name}.md"
    text = "\n\n".join(md) + "\n"
    # merge consecutive bullet paragraphs into a tight list
    text = re.sub(r"(?m)^(- .*)\n\n(?=- )", r"\1\n", text)
    out.write_text(text, encoding="utf-8")
    print(name, len(doc), "pages ->", out, f"({len(text)//1024} KB, {nimg} images)")


if __name__ == "__main__":
    src = Path(sys.argv[1])
    outdir = Path(sys.argv[2])
    outdir.mkdir(parents=True, exist_ok=True)
    convert(src, outdir, src.stem)
