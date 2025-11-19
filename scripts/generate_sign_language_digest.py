#!/usr/bin/env python3
"""
Generate a 'Sign Language & AI' research digest post for a Jekyll blog.

Run from the repo root:
    python scripts/generate_sign_language_digest.py
"""

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from textwrap import shorten

import arxiv

# Canonical ordering for source-site groupings in the output.
SOURCE_SITES = [
    "arXiv",
    "NeurIPS",
    "ICML",
    "ICLR",
    "AAAI",
    "IJCAI",
    "ACL",
    "NAACL",
    "EMNLP",
    "COLING",
    "CVPR",
    "ICCV",
    "ECCV",
]


# Simple slug helper for HTML data attributes.
def slugify(value: str) -> str:
    return (
        value.lower()
        .replace("&", "and")
        .replace("/", "-")
        .replace(" ", "-")
        .replace(",", "")
    )


# Task groupings inspired by VIPL-SLP/awesome-sign-language-processing.
TASK_CATEGORIES = [
    "Sign Language Recognition",
    "Sign Language Translation",
    "Sign Language Production",
    "Other Sign Language Topic",
    "Co-speech Gesture Generation",
    "Gesture Recognition",
]

# -------- Agent 0: Topic Agent -------- #


def topic_agent():
    """
    Returns the core topics & keywords we care about.
    You can edit this list anytime.
    """
    topics = [
        "sign language translation",
        "sign language recognition",
        "sign language and AI",
        "american sign language translation",
        "american sign language recognition",
        "ASL translation",
        "ASL recognition",
        "fingerspelling recognition",
        "sign language avatar",
        "sign language avatar synthesis",
    ]
    return topics


# -------- Agent 1: Research Agent (arXiv) -------- #


def build_arxiv_query(topics):
    """
    Build an arXiv query string focusing on title/abstract.
    We OR the keywords together.
    """
    parts = []
    for t in topics:
        # search in title or abstract
        t_clean = t.replace('"', "")
        parts.append(f'ti:"{t_clean}"')
        parts.append(f'abs:"{t_clean}"')

    # Join them with OR
    query = " OR ".join(parts)

    # Focus on CS / CV / AI-ish categories (optional)
    # You can tune or remove this filter if it seems too strict.
    categories = "(cat:cs.CL OR cat:cs.CV OR cat:cs.AI OR cat:cs.LG OR cat:eess.SP)"
    full_query = f"({query}) AND {categories}"
    return full_query


def research_agent(max_results=20, days_back=30):
    """
    Use arXiv to fetch recent papers related to sign language & AI.
    Sorted by newest first (SubmittedDate).
    """
    topics = topic_agent()
    query = build_arxiv_query(topics)

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    client = arxiv.Client(page_size=max_results, delay_seconds=3)
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days_back)

    results = []
    seen_ids = set()

    for result in client.results(search):
        if result.entry_id in seen_ids:
            continue
        seen_ids.add(result.entry_id)

        # Filter by date (only keep last N days)
        published = result.published  # datetime
        if published is not None and published < cutoff:
            continue

        paper = {
            "id": result.entry_id,
            "title": result.title.strip(),
            "summary": result.summary.strip(),
            "authors": [a.name for a in result.authors],
            "published": published,
            "updated": result.updated,
            "url": result.entry_id,
            "primary_category": result.primary_category,
            "comment": getattr(result, "comment", "") or "",
        }
        results.append(paper)

    return results


# -------- Agent 2: Analysis Agent -------- #

from datetime import timedelta


def simple_heuristic_summary(abstract, max_chars=500):
    """
    Cheap, LLM-free 'summary': truncate to ~max_chars and keep whole sentences.
    You can later swap this for a real LLM call.
    """
    abstract = " ".join(abstract.split())
    return shorten(abstract, width=max_chars, placeholder="…")


def infer_source_site(paper):
    """
    Guess which source site (conference/journal) the paper belongs to.
    Falls back to 'arXiv' if nothing else is detected.
    """
    combined_text = " ".join(
        [
            paper.get("title", ""),
            paper.get("summary", ""),
            paper.get("comment", ""),
        ]
    ).lower()

    for site in SOURCE_SITES:
        if site.lower() == "arxiv":
            continue
        if site.lower() in combined_text:
            return site
    return "arXiv"


def infer_task_category(paper):
    """
    Roughly classify a paper into a task bucket inspired by
    VIPL-SLP/awesome-sign-language-processing.
    """
    text = " ".join(
        [
            paper.get("title", ""),
            paper.get("summary", ""),
            " ".join(paper.get("tags", [])),
        ]
    ).lower()

    mapping = [
        ("Sign Language Recognition", ["recognition", "islr", "cslr", "classifier"]),
        ("Sign Language Translation", ["translation", "translate", "slt"]),
        (
            "Sign Language Production",
            ["production", "avatar", "generation", "synthesis", "signer"],
        ),
        ("Co-speech Gesture Generation", ["co-speech", "gesture generation"]),
        ("Gesture Recognition", ["gesture recognition", "gesture dataset"]),
    ]

    for category, keywords in mapping:
        for keyword in keywords:
            if keyword in text:
                return category
    return "Other Sign Language Topic"


def analysis_agent(papers):
    """
    Enrich each paper with:
      - short_summary
      - naive 'why it matters' note
      - tags guessed from title/abstract
    """
    analyzed = []
    for p in papers:
        abstract = p["summary"]
        title_lower = p["title"].lower()
        text = (p["title"] + " " + abstract).lower()

        short_summary = simple_heuristic_summary(abstract)

        tags = []
        if "american sign language" in text or "asl" in text:
            tags.append("ASL")
        if "translation" in text:
            tags.append("translation")
        if "recognition" in text:
            tags.append("recognition")
        if "avatar" in text or "signing avatar" in text:
            tags.append("avatar")
        if "pose" in text or "skeleton" in text:
            tags.append("pose-estimation")
        if "transformer" in text:
            tags.append("transformer")
        if "graph neural" in text or "gnn" in text:
            tags.append("GNN")
        if "neural" in text or "network" in text:
            tags.append("neural-network")

        tags = sorted(set(tags))

        if "translation" in tags:
            why = "This paper is relevant because it tackles sign language translation."
        elif "recognition" in tags:
            why = (
                "This paper is relevant because it advances sign language recognition."
            )
        else:
            why = "This paper explores methods that can be applied to sign language and AI."

        enriched = {
            **p,
            "short_summary": short_summary,
            "why_it_matters": why,
            "tags": tags,
        }
        enriched["source_site"] = infer_source_site(enriched)
        enriched["task_category"] = infer_task_category(enriched)
        analyzed.append(enriched)
    return analyzed


def build_post_body(analyzed_papers, now: datetime) -> str:
    """
    Assemble the creative Markdown/HTML body for the digest.
    """
    style_block = """
<style>
:root {
  --card-border: #e0e4ec;
  --card-bg: #f9fafc;
  --chip-bg: #eef2ff;
  --chip-text: #162447;
  --accent: #3d5afe;
}
.paper-filter-panel {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin: 1.5rem 0;
  border: 1px solid var(--card-border);
  border-radius: 0.75rem;
  padding: 1rem;
  background: #fff;
}
.filter-group {
  flex: 1 1 240px;
}
.filter-group strong {
  display: block;
  margin-bottom: 0.5rem;
}
.filter-btn {
  border: 1px solid var(--card-border);
  border-radius: 999px;
  padding: 0.35rem 0.9rem;
  margin: 0.25rem 0.35rem 0 0;
  background: #fff;
  cursor: pointer;
  font-size: 0.9rem;
}
.filter-btn.active {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}
.filter-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}
.paper-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  margin: 1.5rem 0;
}
.paper-card {
  border: 1px solid var(--card-border);
  border-radius: 1rem;
  padding: 1.1rem;
  background: var(--card-bg);
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}
.paper-chip-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  font-size: 0.8rem;
}
.chip {
  background: var(--chip-bg);
  color: var(--chip-text);
  border-radius: 999px;
  padding: 0.1rem 0.65rem;
}
.paper-links a {
  text-decoration: none;
  color: var(--accent);
  font-weight: 600;
}
.paper-summary {
  font-size: 0.92rem;
  line-height: 1.35rem;
}
.snapshot-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.95rem;
}
.snapshot-table th,
.snapshot-table td {
  border: 1px solid var(--card-border);
  padding: 0.45rem 0.6rem;
  text-align: left;
}
.snapshot-table thead {
  background: var(--card-bg);
}
</style>
"""

    intro = "This digest compiles recent arXiv publications on sign-language translation, recognition, and related gesture research. The content is structured to make it easy to browse by task or venue.\n"

    if not analyzed_papers:
        return (
            style_block
            + intro
            + "*No recent papers were found for this time window.*\n"
        )

    total = len(analyzed_papers)
    timestamp = (
        f"*Generated on {now.strftime('%B %d, %Y at %H:%M %Z')} "
        f"with {total} papers.*\n"
    )

    source_counts = Counter([p["source_site"] for p in analyzed_papers])
    task_counts = Counter([p["task_category"] for p in analyzed_papers])

    source_table = [
        "### Source snapshot\n",
        '<table class="snapshot-table">\n',
        "  <thead>\n",
        "    <tr><th>Source</th><th>Papers</th></tr>\n",
        "  </thead>\n",
        "  <tbody>\n",
    ]
    for site in SOURCE_SITES:
        source_table.append(
            f"    <tr><td>{site}</td><td>{source_counts.get(site, 0)}</td></tr>\n"
        )
    source_table.append("  </tbody>\n</table>\n")

    task_table = [
        "\n### Task spotlight\n",
        '<table class="snapshot-table">\n',
        "  <thead>\n",
        "    <tr><th>Task</th><th>Papers</th></tr>\n",
        "  </thead>\n",
        "  <tbody>\n",
    ]
    for task in TASK_CATEGORIES:
        task_table.append(
            f"    <tr><td>{task}</td><td>{task_counts.get(task, 0)}</td></tr>\n"
        )
    task_table.append("  </tbody>\n</table>\n")

    filter_intro = (
        "\nUse the filters below to mix-and-match conference venues and the task-driven "
        "taxonomy popularised by the awesome list. Hover over cards to explore summaries "
        "or click through to the original paper/code links.\n"
    )

    def build_filter_group(group_label, group_key, options, counts):
        buttons = [
            f'<button class="filter-btn active" data-filter-group="{group_key}" '
            'data-filter-value="all">All</button>'
        ]
        for option in options:
            count = counts.get(option, 0)
            slug = slugify(option)
            disabled_attr = " disabled aria-disabled='true'" if count == 0 else ""
            buttons.append(
                f'<button class="filter-btn" data-filter-group="{group_key}" '
                f'data-filter-value="{slug}"{disabled_attr}>{option} ({count})</button>'
            )
        return (
            f'<div class="filter-group" data-group="{group_key}">'
            f"<strong>{group_label}</strong>" + "".join(buttons) + "</div>"
        )

    task_filter = build_filter_group(
        "Task focus",
        "task",
        TASK_CATEGORIES,
        task_counts,
    )
    source_filter = build_filter_group(
        "Conference & source",
        "source",
        SOURCE_SITES,
        source_counts,
    )
    filter_panel = f'<div class="paper-filter-panel">{task_filter}{source_filter}</div>'

    cards = ['<div class="paper-grid" id="paper-grid">']
    for p in analyzed_papers:
        site = p.get("source_site", "arXiv")
        task = p.get("task_category", "Other Sign Language Topic")
        site_slug = slugify(site)
        task_slug = slugify(task)
        authors = ", ".join(p["authors"]) if p["authors"] else "Unknown"
        if isinstance(p["published"], datetime):
            pub_date = p["published"].strftime("%Y-%m-%d")
        else:
            pub_date = str(p["published"])
        tag_str = ", ".join(p["tags"]) if p["tags"] else "sign-language-ai"

        card = f"""
<article class="paper-card" data-source="{site_slug}" data-task="{task_slug}">
  <div class="paper-chip-row">
    <span class="chip">{site}</span>
    <span class="chip">{task}</span>
  </div>
  <h3>{p['title']}</h3>
  <p class="paper-authors"><strong>Authors:</strong> {authors}</p>
  <p class="paper-published"><strong>Published:</strong> {pub_date}</p>
  <p class="paper-tags"><strong>Tags:</strong> {tag_str}</p>
  <p class="paper-links"><a href="{p['url']}" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> {p['short_summary']}
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> {p['why_it_matters']}
  </div>
</article>
"""
        cards.append(card)

    cards.append("</div>")

    script_block = """
<script>
(function() {
  const grid = document.getElementById('paper-grid');
  if (!grid) return;
  const cards = Array.from(grid.querySelectorAll('.paper-card'));
  const filterState = { task: 'all', source: 'all' };

  function applyFilters() {
    cards.forEach(card => {
      const taskMatch = filterState.task === 'all' || card.dataset.task === filterState.task;
      const sourceMatch = filterState.source === 'all' || card.dataset.source === filterState.source;
      card.style.display = taskMatch && sourceMatch ? 'flex' : 'none';
    });
  }

  document.querySelectorAll('.filter-group').forEach(group => {
    const groupKey = group.getAttribute('data-group');
    const buttons = Array.from(group.querySelectorAll('.filter-btn'));
    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        if (btn.disabled) return;
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterState[groupKey] = btn.getAttribute('data-filter-value');
        applyFilters();
      });
    });
  });
})();
</script>
"""

    parts = [
        style_block,
        intro,
        timestamp,
        "".join(source_table),
        "".join(task_table),
        filter_intro,
        filter_panel,
        "".join(cards),
        script_block,
    ]
    return "\n".join(parts)


# -------- Agent 3: Editor Agent (Markdown / Jekyll Post) -------- #


def format_date_for_front_matter(dt: datetime) -> str:
    """
    Jekyll likes 'YYYY-MM-DD HH:MM:SS +/-TZ'
    We'll use UTC.
    """
    dt_utc = dt.astimezone(timezone.utc)
    return dt_utc.strftime("%Y-%m-%d %H:%M:%S %z")


def editor_agent(analyzed_papers):
    """
    Build a single Markdown blog post containing all the papers.
    Returns (filename_slug, markdown_text).
    """
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    pretty_date = now.strftime("%B %d, %Y")

    title = f"Sign Language & AI – Recent Papers ({pretty_date})"
    slug = "sign-language-ai-recent-papers"

    # YAML front matter for Jekyll
    front_matter = f"""---
layout: post
title: "{title}"
date: {format_date_for_front_matter(now)}
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
---

"""

    body = build_post_body(analyzed_papers, now)
    markdown = front_matter + body
    filename = f"{date_str}-{slug}.md"
    return filename, markdown


# -------- Agent 4: Publisher Agent (write into _posts) -------- #


def publisher_agent(filename, markdown, posts_dir="_posts"):
    """
    Writes the Markdown into the Jekyll _posts directory.
    """
    posts_path = Path(posts_dir)
    posts_path.mkdir(parents=True, exist_ok=True)

    full_path = posts_path / filename
    with full_path.open("w", encoding="utf-8") as f:
        f.write(markdown)

    return full_path


# -------- Main Orchestrator -------- #


def main():
    print("[Topic Agent] Preparing topics…")
    topics = topic_agent()
    print("  Topics:", topics)

    print("\n[Research Agent] Querying arXiv for recent papers…")
    papers = research_agent(max_results=25, days_back=30)
    print(f"  Found {len(papers)} papers after filters.")

    print("\n[Analysis Agent] Summarizing and tagging papers…")
    analyzed = analysis_agent(papers)

    print("\n[Editor Agent] Building Markdown post…")
    filename, markdown = editor_agent(analyzed)

    print("\n[Publisher Agent] Writing post into _posts/…")
    path = publisher_agent(filename, markdown)

    print(f"\nDone! Created post: {path}")


if __name__ == "__main__":
    main()
