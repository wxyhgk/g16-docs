# Gaussian 16 Users Reference — 中英文静态站

- `md/`  英文 Markdown(按章节拆分)+ `md/images/`
- `md_zh/`  中文译文(目录结构与 `md/` 相同,文件名带 `_zh`)
- `rag/`  页面内「AI 问答」小部件(纯前端:浏览器内检索 + 浏览器直连你填写的大模型接口)
- `pdf2md.py`、`split_md.py`  PDF → Markdown → 按章节拆分(一次性工具)
- `gen_site.py`、`build.sh`  生成站点配置并构建

## 本地构建与预览
```bash
pip install mkdocs mkdocs-material pyyaml
./build.sh                                # 输出 site/(英文)和 site/zh/(中文)
python3 -m http.server -d site 8000       # http://localhost:8000
```

## 发布到 GitHub Pages(与 GaussView6 / Multiwfn 同一套做法)
1. 把项目推到 GitHub 仓库的 `main` 分支(建议仓库名风格:`gview6-docs`、`multiwfn-docs` → 例如 `g16-docs`)。
2. 仓库 Settings → Pages → Source 选 **Deploy from a branch**,分支 `gh-pages`,目录 `/ (root)`。
3. 之后每次 push 到 `main`,`.github/workflows/docs.yml` 会运行 `./build.sh`,再用 `ghp-import` 把 `site/` 强制推到 `gh-pages`。

## AI 问答
点页面右下角「AI 问答」,在 ⚙ 里填接口类型、地址、模型和密钥(只保存在访问者自己的浏览器里)。
注意:浏览器直连要求接口支持 CORS;Pages 是 https,所以接口也必须是 https(localhost 除外)。

## 仓库
- GitHub: https://github.com/wxyhgk/g16-docs (Pages: https://wxyhgk.github.io/g16-docs/)
- 本地 GitLab: http://ds720.local:2224/wxyhgk/g16-docs
- `git push` 会同时推送到两个远程(origin 配置了两个 push 地址)。
