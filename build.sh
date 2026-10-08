#!/bin/sh
# Rebuild the static site: search indexes -> staging + configs -> EN site (site/) -> ZH site (site/zh/)
set -e
cd "$(dirname "$0")"
python3 -I rag/index.py
python3 -I gen_site.py
mkdocs build -q -f mkdocs.yml
mkdocs build -q -f mkdocs-zh.yml
echo "built: site/ (EN) and site/zh/ (ZH)"
