#!/usr/bin/env python3
"""Split the combined partN.md files into chapter dirs / section files."""
import re
import sys
from pathlib import Path


def pad(n):
    return n.zfill(2) if n.isdigit() else n


def slug(t):
    t = re.sub(r"[^\w]+", "_", t, flags=re.A).strip("_")
    return t[:48].rstrip("_") or "hash"


def split(src, outroot):
    part = src.stem
    base = outroot / part
    chunks = []  # (kind, num, title, lines)
    cur = ("front", "", "", [])
    fence = False
    for line in src.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"(#{2,3}) (\S+) (.*)$", line)
        if m and m.group(1) == "###" and re.match(r"^[0-9A-Z]+(\.\d+)*\.?$", m.group(2)):
            chunks.append(cur)
            num, title = m.group(2), m.group(3)
            kind = "chapter" if num.endswith(".") else "section"
            cur = (kind, num.rstrip("."), title, [line])
        elif m and m.group(1) == "##" and m.group(2) == "Bibliography":
            chunks.append(cur)
            cur = ("chapter", "Bib", "Bibliography", [line])
        else:
            cur[3].append(line)
    chunks.append(cur)

    chapdir = base
    index = []
    for kind, num, title, lines in chunks:
        body = "\n".join(lines).strip()
        if not body:
            continue
        if kind == "front":
            path = base / "00_front.md"
            depth = 1
        elif kind == "chapter":
            chapdir = base / f"{pad(num)}_{slug(title)}"
            path = chapdir / "00_intro.md"
            depth = 2
            index.append(f"- **{num}. {title}**")
        else:
            parts = num.split(".")
            fn = ".".join(pad(p) for p in parts) + f"_{slug(title)}.md"
            path = chapdir / fn
            depth = 2
            index.append(f"  - [{num} {title}]({path.relative_to(base).as_posix()})")
        path.parent.mkdir(parents=True, exist_ok=True)
        up = "../" * depth
        body = body.replace("](images/", f"]({up}images/")
        path.write_text(body + "\n", encoding="utf-8")
        if kind == "chapter":
            index[-1] = f"- **[{num}. {title}]({path.relative_to(base).as_posix()})**"
    (base / "README.md").write_text(f"# {part}\n\n" + "\n".join(index) + "\n", encoding="utf-8")
    print(part, "->", sum(1 for _ in base.rglob("*.md")), "files")


if __name__ == "__main__":
    out = Path(sys.argv[2])
    split(Path(sys.argv[1]), out)
