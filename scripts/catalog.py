"""Render the bilingual indexes and scenario pages from data/catalog.json."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data/catalog.json"
LANGUAGES = ("en", "zh")
HOME = {"en": "README.md", "zh": "README.zh-CN.md"}
PREFIX = {"en": "", "zh": "zh-CN/"}
LANG_LINK = {"en": "简体中文", "zh": "English"}
SOURCE_TYPES = {
    "report": {"en": "Author account", "zh": "作者自述", "points": 2},
    "output": {"en": "Author's published output", "zh": "作者公开产物", "points": 2},
    "recipe": {"en": "Community recipe", "zh": "社区做法", "points": 1},
    "guide": {"en": "Product guide", "zh": "产品做法", "points": 1},
    "index": {"en": "Collection summary", "zh": "合集摘要", "points": 1},
}
SCENE_HEADINGS = {
    "en": ("Sample result", "Try it with material you have", "With a connected tool",
           "How to check it", "Decision boundary", "How the cases fit together",
           "Sources", "Building blocks"),
    "zh": ("先看结果", "手头有材料就能试", "已经接了工具", "怎么验收", "做到哪一步",
           "这些案例怎么合在一起", "来源", "搭建方法"),
}
LINK = re.compile(r"\]\(([^\s)]+)\)")


def scene_path(scene, lang):
    return f"{PREFIX[lang]}scenes/{scene['id']}.md"


def evidence_score(scene, sources):
    return max(SOURCE_TYPES[sources[id]["kind"]]["points"] for id in scene["sources"])


def validate(catalog):
    groups = {group["id"] for group in catalog["groups"]}
    patterns = {pattern["id"] for pattern in catalog["patterns"]}
    upstreams = {upstream["id"] for upstream in catalog["upstreams"]}
    scenes, sources = catalog["scenes"], catalog["sources"]
    ids = [scene["id"] for scene in scenes]
    if len(set(ids)) != len(ids) or catalog["featured"]["id"] not in ids:
        raise ValueError("Scenario IDs must be unique, and the featured ID must exist.")
    used = set()
    originals = set()
    for id, source in sources.items():
        key = source.get("original", source["url"]).rstrip("/")
        if key in originals:
            raise ValueError(f"Duplicate source for {id}. Keep all mirrors in one record.")
        if source["upstream"] not in upstreams or source["kind"] not in SOURCE_TYPES:
            raise ValueError(f"Unknown upstream or source kind for {id}")
        originals.add(key)
    for scene in scenes:
        id = scene["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", id):
            raise ValueError(f"Invalid scenario ID: {id}")
        if scene["group"] not in groups:
            raise ValueError(f"Unknown group for {id}")
        if not scene["sources"] or len(set(scene["sources"])) != len(scene["sources"]):
            raise ValueError(f"{id} needs distinct supporting sources")
        if not set(scene["sources"]) <= sources.keys() or not set(scene["patterns"]) <= patterns:
            raise ValueError(f"Missing source or building block for {id}")
        if not all(scene[key] in (1, 2) for key in ("reuse", "first_run")):
            raise ValueError(f"Use an editorial score of 1 or 2 for {id}")
        used.update(scene["sources"])
        for lang in LANGUAGES:
            local = scene[lang]
            fields = ("title", "outcome", "result", "trial", "connected", "verify",
                      "boundary", "analysis", "variants")
            if not all(local[field] for field in fields):
                raise ValueError(f"Incomplete {lang} scenario: {id}")
    if used != set(sources):
        raise ValueError(f"Sources without a scenario: {sorted(set(sources)-used)}")


def render_home(catalog, lang):
    zh = lang == "zh"
    other = "en" if zh else "zh"
    scenes, sources = catalog["scenes"], catalog["sources"]
    featured = catalog["featured"]
    first_scene = next(s for s in scenes if s["id"] == featured["id"])
    featured_link = f"[{featured[lang]['label']}]({scene_path(first_scene, lang)})"
    if zh:
        lines = [
            "# 个人 Agent 用例库",
            "",
            "先选一件最近遇到的事。每个场景都有一份能直接试的样例，也写明怎样核对结果。",
            "",
            f"[English]({HOME[other]}) · [怎么搭](zh-CN/BUILDER.md) · "
            "[案例来源与筛选](zh-CN/EVIDENCE.md) · [设计](ARCHITECTURE.md) · [贡献](CONTRIBUTING.md)",
            "",
            f"**先试 {featured_link}**。{featured[lang]['description']}",
            "",
        ]
    else:
        lines = [
            "# Awesome Personal Agent Use Cases",
            "",
            "Start with something you need to do. Each scenario shows a result, gives you a sample to try, and explains how to check it.",
            "",
            f"[简体中文]({HOME[other]}) · [Builder guide](BUILDER.md) · "
            "[Sources and selection](EVIDENCE.md) · [Design](ARCHITECTURE.md) · [Contribute](CONTRIBUTING.md)",
            "",
            f"**Start with {featured_link}** {featured[lang]['description']}",
            "",
        ]
    for group in catalog["groups"]:
        items = [s for s in scenes if s["group"] == group["id"]]
        items.sort(key=lambda s: -(s["reuse"] + s["first_run"] + evidence_score(s, sources)))
        lines += [
            f"## {group[lang]}", "",
            "| 场景 | 你会拿到什么 |" if zh else "| Scenario | What you get |",
            "| --- | --- |",
        ]
        for s in items:
            lines.append(f"| [{s[lang]['title']}]({scene_path(s, lang)}) | {s[lang]['outcome']} |")
        lines.append("")
    archive = "https://github.com/cubxxw/awesome-personal-agent-practices"
    lines.append(
        f"查产品、开源项目和研究，见 [Awesome Personal Agent Practices]({archive}/blob/main/README.zh-CN.md)。"
        if zh else f"For products, open-source projects, and research, see [Awesome Personal Agent Practices]({archive})."
    )
    return "\n".join(lines) + "\n"


def render_scene(catalog, scene, lang):
    zh = lang == "zh"
    other = "en" if zh else "zh"
    root = "../../" if zh else "../"
    local = scene[lang]
    result, trial, connected, verify, boundary, analysis, sources, patterns = SCENE_HEADINGS[lang]
    lines = [
        f"# {local['title']}",
        "",
        f"[{'首页' if zh else 'Home'}]({root}{HOME[lang]}) · "
        f"[{LANG_LINK[lang]}]({root}{scene_path(scene, other)})",
        "",
        local["outcome"],
        "",
        f"## {result}", "",
        *[f"- {line}" for line in local["result"]], "",
        f"## {trial}", "",
        "复制下面整段。里面的材料都是虚构样例。" if zh else
        "Paste the full block below. The input is fictional.",
        "",
        "```text", local["trial"], "```", "",
        f"## {connected}", "", local["connected"], "",
        f"## {verify}", "", local["verify"], "",
        f"## {boundary}", "", local["boundary"], "",
        f"## {analysis}", "", local["analysis"], "",
        *[f"- {line}" for line in local["variants"]], "",
        f"## {sources}", "",
    ]
    for id in scene["sources"]:
        source = catalog["sources"][id]
        kind = SOURCE_TYPES[source["kind"]][lang]
        original = (" · " + f"[{'原始发布入口' if zh else 'Original post'}]({source['original']})"
                    if source.get("original") else "")
        lines.append(f"- **{kind}**。{source['note'][lang]} [{source['title'][lang]}]({source['url']}){original}"
                     if zh else
                     f"- **{kind}.** {source['note'][lang]} [{source['title'][lang]}]({source['url']}){original}")
    pattern_labels = {p["id"]: p[lang] for p in catalog["patterns"]}
    links = [f"[{pattern_labels[id]}](../usecases/{id}.md)" for id in scene["patterns"]]
    lines += ["", f"## {patterns}", "",
              " · ".join(links + [f"[{'平台怎么选' if zh else 'Platform routes'}](../BUILDER.md)"])]
    return "\n".join(lines) + "\n"


def render_evidence(catalog, lang):
    zh = lang == "zh"
    other_url = "../EVIDENCE.md" if zh else "zh-CN/EVIDENCE.md"
    home_url = "../README.zh-CN.md" if zh else "README.md"
    scenes, sources = catalog["scenes"], catalog["sources"]
    lines = [
        "# 案例来源与筛选" if zh else "# Sources and selection",
        "",
        f"[{'首页' if zh else 'Home'}]({home_url}) · [{LANG_LINK[lang]}]({other_url})",
        "",
        f"这版把 {len(sources)} 条去重后的来源记录归入 {len(scenes)} 个场景。"
        "记录含作者自述、公开产物、搭建做法和合集摘要。试用样例另写，各平台的自动化需要分别验收。"
        if zh else
        f"This edition maps {len(sources)} distinct source records to {len(scenes)} scenarios. "
        "Records include author accounts, published outputs, setup guides, and collection summaries. "
        "The starter examples are fictional, and live automation is a separate check.",
        "",
        "## 核对过的入口" if zh else "## Source collections reviewed",
        "",
    ]
    for u in catalog["upstreams"]:
        count = sum(s["upstream"] == u["id"] for s in sources.values())
        count_label = f"收录 {count} 条" if zh else f"{count} selected records"
        lines.append(f"- {u['scope'][lang]} **{count_label}**。 [{u['title']}]({u['url']})" if zh else
                     f"- {u['scope'][lang]} **{count_label}.** [{u['title']}]({u['url']})")
    lines += ["", "## 首次上手排序" if zh else "## First-run ranking", "",
              "复用、上手、来源各最多两分。并列沿用编辑顺序。"
              if zh else "Reuse, first run, and source strength each contribute up to two points. Ties keep editorial order.",
              "",
              "| 场景 | 复用 | 上手 | 来源 | 合计 |" if zh else "| Scenario | Reuse | First run | Source | Total |",
              "| --- | ---: | ---: | ---: | ---: |"]
    ranked = sorted(scenes, key=lambda s: -(s["reuse"] + s["first_run"] + evidence_score(s, sources)))
    for s in ranked:
        e = evidence_score(s, sources)
        lines.append(f"| [{s[lang]['title']}](scenes/{s['id']}.md) | {s['reuse']} | {s['first_run']} | {e} | {s['reuse'] + s['first_run'] + e} |")
    lines += ["", "## 记录与对应场景" if zh else "## Source-to-scenario map", "",
              "| 来源 | 证据类型 | 用在 |" if zh else "| Source | Evidence | Used in |", "| --- | --- | --- |"]
    for id, s in sources.items():
        linked = ", ".join(f"[{item[lang]['title']}](scenes/{item['id']}.md)"
                           for item in scenes if id in item["sources"])
        lines.append(f"| [{s['title'][lang]}]({s['url']}) | {SOURCE_TYPES[s['kind']][lang]} | {linked} |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check the generated content and local links.")
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    validate(catalog)
    rendered = {}
    for lang in LANGUAGES:
        rendered[HOME[lang]] = render_home(catalog, lang)
        rendered[PREFIX[lang] + "EVIDENCE.md"] = render_evidence(catalog, lang)
        for scene in catalog["scenes"]:
            rendered[scene_path(scene, lang)] = render_scene(catalog, scene, lang)
    if not args.check:
        for name, content in rendered.items():
            output = ROOT / name
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(content, encoding="utf-8")
        return
    problems = []
    for name, content in rendered.items():
        path = ROOT / name
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            problems.append(f"Stale or missing page: {name}")
    for lang in LANGUAGES:
        for path in (ROOT / (PREFIX[lang] + "scenes")).glob("*.md"):
            if path.relative_to(ROOT).as_posix() not in rendered:
                problems.append(f"Orphaned scenario: {path.relative_to(ROOT)}")
    for path in ROOT.rglob("*.md"):
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            url = urlsplit(target)
            if not url.scheme and url.path and not (path.parent / unquote(url.path)).is_file():
                problems.append(f"Broken relative link in {path.relative_to(ROOT)}: {target}")
    if problems:
        raise SystemExit("\n".join(problems))
    print(f"Checked {len(catalog['scenes'])} scenarios, {len(catalog['sources'])} sources, and {len(rendered)} rendered pages.")


if __name__ == "__main__":
    main()
