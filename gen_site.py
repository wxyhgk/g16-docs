#!/usr/bin/env python3
"""Stage two independent mkdocs sites (EN: md/, ZH: md_zh/) and write their configs.

Build with:  ./build.sh   (rag/index.py -> gen_site.py -> mkdocs build EN, then ZH)
Output: site/ (English) and site/zh/ (Chinese). Each site has its own nav and search index.
"""
import re
import shutil
from pathlib import Path

import yaml

EN, ZH = Path("md"), Path("md_zh")
STAGE_EN, STAGE_ZH = Path("_docs_en"), Path("_docs_zh")

LABELS = {
    "en": {
        "part1": "Part One — Introduction & Running",
        "part2": "Part Two — Keywords & Utilities",
        "part3": "Part Three — Appendix",
        "home": "Home", "front": "Front Matter", "overview": "Overview",
        "title": "Gaussian 16 Users Reference",
        "blurb": "Gaussian 16 Rev. B.01 用户手册的 Markdown 版本。",
    },
    "zh": {
        "part1": "第一部分 — 简介与运行",
        "part2": "第二部分 — 关键字与实用程序",
        "part3": "第三部分 — 附录",
        "home": "首页", "front": "封面", "overview": "概述",
        "title": "Gaussian 16 用户手册",
        "blurb": "Gaussian 16 Rev. B.01 用户手册的中文翻译(Haiku 4.5 机器翻译,仅供参考,以英文原文为准)。",
    },
}

JS = r"""(function () {
  var KEY = "lang-switch-pos";

  function headings() {
    return Array.prototype.slice.call(
      document.querySelectorAll(".md-content__inner h1, .md-content__inner h2, .md-content__inner h3, .md-content__inner h4, .md-content__inner h5, .md-content__inner h6"));
  }

  // where the reader is: last heading above the viewport top, plus offset inside that section
  function capture() {
    var hs = headings(), y = window.scrollY, idx = -1, delta = 0;
    for (var i = 0; i < hs.length; i++) {
      var top = hs[i].getBoundingClientRect().top + y;
      if (top - 80 <= y) { idx = i; delta = y - (top - 80); } else break;
    }
    var max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    return { idx: idx, delta: delta, ratio: y / max, n: hs.length };
  }

  function restore(key) {
    var raw; try { raw = sessionStorage.getItem(KEY); sessionStorage.removeItem(KEY); } catch (e) {}
    if (!raw) return;
    var s; try { s = JSON.parse(raw); } catch (e) { return; }
    if (!s || s.to !== key) return;
    var hs = headings(), y;
    if (s.n === hs.length && s.idx >= 0) {
      y = hs[s.idx].getBoundingClientRect().top + window.scrollY - 80 + s.delta;
    } else if (s.n === hs.length) {
      y = s.delta;
    } else {
      y = s.ratio * Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    }
    window.scrollTo(0, Math.max(0, y));
  }

  function init() {
    // The ZH site lives in <root>/zh/ ; the EN site in <root>/ .
    var scope = (typeof __md_scope !== "undefined" && __md_scope.pathname) || "/";
    var isZh = /\/zh\/$/.test(scope);
    var enRoot = isZh ? scope.replace(/zh\/$/, "") : scope;
    var zhRoot = isZh ? scope : scope + "zh/";
    var path = location.pathname;
    if (path.indexOf(scope) !== 0) return;
    var rel = path.slice(scope.length);
    if (!rel || rel === "index.html") {
      rel = "index.html";
    }
    var target = isZh
      ? enRoot + rel.replace(/_zh\.html$/, ".html")
      : zhRoot + (rel === "index.html" ? "index.html" : rel.replace(/\.html$/, "_zh.html"));
    restore(path);
    var a = document.createElement("a");
    a.className = "lang-switch";
    a.textContent = isZh ? "EN" : "中文";
    a.title = isZh ? "Switch to English" : "切换到中文";
    a.href = target;
    a.addEventListener("click", function () {
      var s = capture(); s.to = target;
      try { sessionStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {}
    });
    var inner = document.querySelector(".md-header__inner");
    var search = inner && inner.querySelector(".md-search");
    if (!inner) return;
    inner.insertBefore(a, search || null);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
"""

CSS = """.lang-switch {
  align-self: center;
  margin: 0 .4rem;
  padding: .15rem .6rem;
  border: 1px solid currentColor;
  border-radius: .3rem;
  color: inherit;
  font-size: .75rem;
  font-weight: 600;
  white-space: nowrap;
}
.lang-switch:hover { background: rgba(255, 255, 255, .15); }
"""


def title_of(p):
    for line in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"#{1,3} (.*)", line)
        if m:
            return m.group(1).strip()
    return p.stem


def build_nav(part, root, zh):
    lab = LABELS["zh" if zh else "en"]
    base = root / part
    suffix = "_zh.md" if zh else ".md"
    items, links = [], []
    front = base / f"00_front{suffix}"
    if front.exists():
        items.append({lab["front"]: f"{part}/{front.name}"})
    for chap in sorted(d for d in base.iterdir() if d.is_dir()):
        intro = f"00_intro{suffix}"
        sub = []
        for f in sorted(chap.glob("*.md")):
            if f.name == intro:
                sub.insert(0, {lab["overview"]: f"{part}/{chap.name}/{f.name}"})
            else:
                sub.append({title_of(f): f"{part}/{chap.name}/{f.name}"})
        ctitle = title_of(chap / intro) if (chap / intro).exists() else chap.name
        items.append({ctitle: sub})
        links.append(f"- [{ctitle}]({part}/{chap.name}/{intro})")
    return items, links


def stage(zh):
    code = "zh" if zh else "en"
    lab = LABELS[code]
    root, st = (ZH, STAGE_ZH) if zh else (EN, STAGE_EN)
    if st.exists():
        shutil.rmtree(st)
    st.mkdir()
    for part in LABELS[code]:
        if not part.startswith("part"):
            continue
        shutil.copytree(root / part, st / part)
    shutil.copytree(EN / "images", st / "images")
    if zh:  # images live at md/images on disk, at <stage>/images in the site
        for f in st.rglob("*.md"):
            f.write_text(re.sub(r"\]\(((?:\.\./)+)md/images/", lambda m: "](" + m.group(1)[3:] + "images/",
                                f.read_text(encoding="utf-8")), encoding="utf-8")
    nav = [{lab["home"]: "index.md"}]
    home = [f"# {lab['title']}", "", lab["blurb"], ""]
    for part in ("part1", "part2", "part3"):
        items, links = build_nav(part, root, zh)
        nav.append({lab[part]: items})
        home += [f"## {lab[part]}", ""] + links + [""]
    (st / "index.md").write_text("\n".join(home), encoding="utf-8")
    (st / "js").mkdir()
    (st / "js" / "lang-switch.js").write_text(JS, encoding="utf-8")
    (st / "css").mkdir()
    (st / "css" / "lang-switch.css").write_text(CSS, encoding="utf-8")
    shutil.copy("rag/widget.js", st / "js" / "ask-widget.js")
    shutil.copy("rag/widget.css", st / "css" / "ask-widget.css")
    if not zh:  # static search indexes, shared by both sites (the ZH site loads them from the site root)
        (st / "rag").mkdir()
        for lang in ("en", "zh"):
            shutil.copy(f"rag/index-{lang}.js", st / "rag" / f"index-{lang}.js")

    cfg = {
        "site_name": lab["title"],
        "docs_dir": str(st),
        "site_dir": "site/zh" if zh else "site",
        "use_directory_urls": False,
        "theme": {
            "name": "material",
            "language": "zh" if zh else "en",
            "features": [
                "navigation.sections", "navigation.top", "navigation.indexes",
                "navigation.tracking", "search.highlight", "search.suggest",
                "toc.follow", "content.code.copy",
            ],
            "palette": [
                {"media": "(prefers-color-scheme: light)", "scheme": "default",
                 "toggle": {"icon": "material/weather-night", "name": "Dark mode"}},
                {"media": "(prefers-color-scheme: dark)", "scheme": "slate",
                 "toggle": {"icon": "material/weather-sunny", "name": "Light mode"}},
            ],
        },
        "plugins": [{"search": {"lang": ["en", "zh"]}} if zh else "search", "offline"],  # offline: search also works from file://
        "markdown_extensions": ["tables", "admonition", {"toc": {"permalink": True}}],
        "extra_javascript": ["js/lang-switch.js", "js/ask-widget.js"],
        "extra_css": ["css/lang-switch.css", "css/ask-widget.css"],
        "nav": nav,
    }
    out = Path("mkdocs-zh.yml" if zh else "mkdocs.yml")
    out.write_text(yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False, width=200), encoding="utf-8")
    print(code, "staged:", sum(1 for _ in st.rglob("*.md")), "pages ->", out)


stage(False)
stage(True)
