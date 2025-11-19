#!/usr/bin/env python3
"""
Generate a 'Sign Language & AI' research digest post for a Jekyll blog.

Run from the repo root:
    python scripts/generate_sign_language_digest.py
"""

import os
from datetime import datetime, timezone
from pathlib import Path
from textwrap import shorten

import arxiv
from dateutil import parser as date_parser

# Canonical ordering for source-site groupings in the output.
SOURCE_SITES = [
    "arXiv",
    "NeurIPS",
    "ICML",
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

        analyzed.append(
            {
                **p,
                "short_summary": short_summary,
                "why_it_matters": why,
                "tags": tags,
                "source_site": infer_source_site(p),
            }
        )
    return analyzed


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

    body_lines = []
    body_lines.append(
        "This digest automatically gathers recent arXiv papers related to "
        "sign language, sign language translation/recognition, and sign language & AI. "
        "Findings are grouped by likely source site below.\n"
    )

    if not analyzed_papers:
        body_lines.append("*No recent papers were found for this time window.*\n")
    else:
        body_lines.append(
            "Below are the papers grouped by their likely source sites.\n"
        )
        grouped = {site: [] for site in SOURCE_SITES}
        for p in analyzed_papers:
            site = p.get("source_site", "arXiv") or "arXiv"
            grouped.setdefault(site, []).append(p)

        for site in SOURCE_SITES:
            papers_for_site = grouped.get(site, [])
            body_lines.append(f"## {site}\n")

            if not papers_for_site:
                body_lines.append(
                    "_No recent papers from this source in the selected window._\n"
                )
                continue

            for i, p in enumerate(papers_for_site, start=1):
                if isinstance(p["published"], datetime):
                    pub_date = p["published"].strftime("%Y-%m-%d")
                else:
                    pub_date = str(p["published"])

                authors = ", ".join(p["authors"]) if p["authors"] else "Unknown"
                tag_str = ", ".join(p["tags"]) if p["tags"] else "sign-language-ai"

                section = f"""### {i}. {p['title']}

- **Authors:** {authors}
- **Published:** {pub_date}
- **Link:** [{p['id']}]({p['url']})
- **Tags:** {tag_str}

**Summary**

{p['short_summary']}

**Why it matters**

{p['why_it_matters']}

---

"""
                body_lines.append(section)

    markdown = front_matter + "\n".join(body_lines)
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
