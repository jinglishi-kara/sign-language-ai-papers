---
layout: default
title: "Sign Language & AI Dashboard"
---

{% assign latest_post = site.posts.first %}

<style>
:root {
  --dashboard-ink: #13212b;
  --dashboard-muted: #5a6772;
  --dashboard-surface: #ffffff;
  --dashboard-soft: #f7f4eb;
  --dashboard-mist: #edf5f1;
  --dashboard-accent: #0d7a5f;
  --dashboard-accent-deep: #085744;
  --dashboard-sand: #ecd9bf;
  --dashboard-border: rgba(19, 33, 43, 0.1);
  --dashboard-shadow: 0 24px 60px rgba(19, 33, 43, 0.08);
}

.dashboard-shell {
  font-family: "Avenir Next", "Segoe UI", sans-serif;
  color: var(--dashboard-ink);
  padding: 2rem 0 3rem;
}

.dashboard-hero {
  position: relative;
  overflow: hidden;
  display: grid;
  grid-template-columns: minmax(0, 1.75fr) minmax(280px, 1fr);
  gap: 1.25rem;
  padding: 2rem;
  margin-bottom: 1.5rem;
  border: 1px solid var(--dashboard-border);
  border-radius: 1.75rem;
  background:
    radial-gradient(circle at top right, rgba(13, 122, 95, 0.14), transparent 34%),
    linear-gradient(135deg, #fffdf7 0%, #f3f8f5 55%, #f8efe1 100%);
  box-shadow: var(--dashboard-shadow);
}

.dashboard-hero::after {
  content: "";
  position: absolute;
  right: -5rem;
  bottom: -5rem;
  width: 14rem;
  height: 14rem;
  border-radius: 999px;
  background: rgba(236, 217, 191, 0.35);
  filter: blur(6px);
}

.hero-copy,
.hero-side {
  position: relative;
  z-index: 1;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  margin: 0 0 0.85rem;
  color: var(--dashboard-accent-deep);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.11em;
  text-transform: uppercase;
}

.hero-title,
.results-title {
  margin: 0;
  font-family: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif;
  line-height: 1;
}

.hero-title {
  max-width: 13ch;
  font-size: clamp(2.35rem, 5vw, 4rem);
}

.hero-copy p {
  max-width: 62ch;
  margin: 1rem 0 0;
  color: var(--dashboard-muted);
  font-size: 1.02rem;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin-top: 1.35rem;
}

.hero-link,
.results-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  padding: 0.8rem 1.15rem;
  text-decoration: none;
  font-weight: 700;
}

.hero-link {
  background: var(--dashboard-accent);
  color: #fff;
  box-shadow: 0 14px 30px rgba(13, 122, 95, 0.18);
}

.hero-note {
  display: inline-flex;
  align-items: center;
  border: 1px solid rgba(13, 122, 95, 0.18);
  border-radius: 999px;
  padding: 0.8rem 1.15rem;
  color: var(--dashboard-accent-deep);
  background: rgba(255, 255, 255, 0.72);
  font-weight: 600;
}

.hero-side {
  display: grid;
  gap: 0.85rem;
}

.metric-card {
  border: 1px solid var(--dashboard-border);
  border-radius: 1.3rem;
  padding: 1rem 1.1rem;
  background: rgba(255, 255, 255, 0.76);
  backdrop-filter: blur(10px);
}

.metric-card strong {
  display: block;
  margin-top: 0.25rem;
  font-size: 1.9rem;
  line-height: 1;
}

.metric-card span {
  color: var(--dashboard-muted);
  font-size: 0.94rem;
}

.dashboard-panel {
  margin-top: 1.5rem;
  border: 1px solid var(--dashboard-border);
  border-radius: 1.45rem;
  background: var(--dashboard-surface);
  box-shadow: var(--dashboard-shadow);
}

.control-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr);
  gap: 1.25rem;
  padding: 1.35rem;
}

.panel-block {
  padding: 0.2rem;
}

.section-label {
  margin: 0 0 0.45rem;
  color: var(--dashboard-accent-deep);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.panel-title {
  margin: 0;
  font-family: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif;
  font-size: 1.6rem;
}

.panel-copy {
  margin: 0.65rem 0 0;
  color: var(--dashboard-muted);
  line-height: 1.6;
}

.search-shell {
  margin-top: 1rem;
}

.search-shell input {
  width: 100%;
  border: 1px solid rgba(19, 33, 43, 0.12);
  border-radius: 1.15rem;
  padding: 0.95rem 1rem;
  background: #fbfaf7;
  color: var(--dashboard-ink);
  font: inherit;
  box-sizing: border-box;
}

.search-shell input:focus {
  outline: 2px solid rgba(13, 122, 95, 0.18);
  border-color: rgba(13, 122, 95, 0.35);
}

.search-hint {
  margin: 0.65rem 0 0;
  color: var(--dashboard-muted);
  font-size: 0.92rem;
}

.digest-rail {
  display: flex;
  gap: 0.75rem;
  overflow-x: auto;
  padding-bottom: 0.15rem;
  margin-top: 1rem;
}

.digest-rail::-webkit-scrollbar {
  height: 0.55rem;
}

.digest-rail::-webkit-scrollbar-thumb {
  background: rgba(19, 33, 43, 0.12);
  border-radius: 999px;
}

.digest-pill {
  min-width: 9.5rem;
  border: 1px solid rgba(19, 33, 43, 0.1);
  border-radius: 1.15rem;
  padding: 0.95rem 1rem;
  background: linear-gradient(180deg, #ffffff 0%, #f7f4eb 100%);
  color: var(--dashboard-ink);
  text-align: left;
  cursor: pointer;
  transition: transform 160ms ease, border-color 160ms ease, box-shadow 160ms ease;
}

.digest-pill:hover,
.digest-pill:focus-visible {
  transform: translateY(-1px);
  border-color: rgba(13, 122, 95, 0.35);
  box-shadow: 0 14px 26px rgba(19, 33, 43, 0.08);
  outline: none;
}

.digest-pill.active {
  border-color: transparent;
  background: linear-gradient(135deg, var(--dashboard-accent) 0%, #16936d 100%);
  color: #fff;
  box-shadow: 0 16px 30px rgba(13, 122, 95, 0.2);
}

.digest-pill-label,
.digest-pill-meta {
  display: block;
}

.digest-pill-label {
  font-weight: 700;
}

.digest-pill-meta {
  margin-top: 0.4rem;
  font-size: 0.9rem;
  opacity: 0.8;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.1rem;
  padding: 0 1.35rem 1.35rem;
}

.summary-card {
  border: 1px solid rgba(19, 33, 43, 0.08);
  border-radius: 1.25rem;
  padding: 1rem;
  background: linear-gradient(180deg, #fff 0%, #fbfaf7 100%);
}

.summary-card h2 {
  margin: 0 0 0.75rem;
  font-size: 1rem;
}

.summary-chip-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
}

.summary-chip,
.tag-chip,
.paper-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  border-radius: 999px;
  font-size: 0.84rem;
}

.summary-chip {
  border: 1px solid rgba(13, 122, 95, 0.15);
  padding: 0.4rem 0.7rem;
  background: var(--dashboard-mist);
  color: var(--dashboard-accent-deep);
  font-weight: 600;
}

.summary-chip strong {
  font-size: 0.78rem;
}

.results-panel {
  padding: 1.35rem;
}

.results-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.results-title {
  font-size: clamp(1.8rem, 4vw, 2.35rem);
}

.results-meta {
  margin: 0.55rem 0 0;
  color: var(--dashboard-muted);
  line-height: 1.6;
}

.results-link {
  border: 1px solid rgba(13, 122, 95, 0.18);
  color: var(--dashboard-accent-deep);
  background: #f6fbf8;
  white-space: nowrap;
}

.paper-browser-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin-top: 1.25rem;
}

.browser-card {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  min-height: 100%;
  border: 1px solid rgba(19, 33, 43, 0.08);
  border-radius: 1.35rem;
  padding: 1.05rem;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.96) 0%, rgba(251, 250, 247, 0.96) 100%);
}

.browser-card-top {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.paper-chip {
  padding: 0.28rem 0.65rem;
  background: #eef6f2;
  color: var(--dashboard-accent-deep);
  font-weight: 700;
}

.paper-digest-stamp {
  background: #f7ecde;
  color: #8a5a17;
}

.browser-card h3 {
  margin: 0;
  font-size: 1.1rem;
  line-height: 1.4;
}

.paper-meta {
  margin: 0;
  color: var(--dashboard-muted);
  font-size: 0.92rem;
  line-height: 1.55;
}

.paper-summary {
  margin: 0;
  color: var(--dashboard-muted);
  font-size: 0.94rem;
  line-height: 1.6;
}

.paper-summary strong,
.paper-meta strong {
  color: var(--dashboard-ink);
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.tag-chip {
  padding: 0.28rem 0.6rem;
  background: #f1efe8;
  color: #5f5d55;
  font-weight: 600;
}

.browser-card a {
  margin-top: auto;
  color: var(--dashboard-accent);
  font-weight: 700;
  text-decoration: none;
}

.browser-card a:hover,
.browser-card a:focus-visible,
.hero-link:hover,
.hero-link:focus-visible,
.results-link:hover,
.results-link:focus-visible {
  text-decoration: underline;
}

.empty-state {
  margin-top: 1.25rem;
  border: 1px dashed rgba(19, 33, 43, 0.15);
  border-radius: 1.25rem;
  padding: 1.2rem;
  background: #fbfaf7;
  color: var(--dashboard-muted);
}

.loading-card {
  min-height: 15rem;
  border-radius: 1.35rem;
  background:
    linear-gradient(110deg, rgba(247, 244, 235, 0.92) 8%, rgba(255, 255, 255, 0.92) 18%, rgba(247, 244, 235, 0.92) 33%);
  background-size: 200% 100%;
  animation: dashboard-shimmer 1.2s linear infinite;
}

.empty-summary {
  color: var(--dashboard-muted);
  font-size: 0.94rem;
}

.noscript-card {
  padding: 1rem 1.2rem;
}

@keyframes dashboard-shimmer {
  to {
    background-position: -200% 0;
  }
}

@media (max-width: 860px) {
  .dashboard-hero,
  .control-grid,
  .summary-grid {
    grid-template-columns: 1fr;
  }

  .results-head {
    flex-direction: column;
  }

  .results-link {
    width: 100%;
  }
}
</style>

<div class="dashboard-shell">
  <section class="dashboard-hero">
    <div class="hero-copy">
      <p class="eyebrow">Research Dashboard</p>
      <h1 class="hero-title">Browse papers, not a long stack of daily posts.</h1>
      <p>
        This homepage now works like a paper browser. Pick a digest date when you need a specific update, switch to the full archive when you want the wider picture, and search paper titles directly instead of scanning day-by-day pages.
      </p>
      <div class="hero-actions">
        {% if latest_post %}
          <a class="hero-link" href="{{ latest_post.url | relative_url }}">Open latest digest</a>
        {% endif %}
        <span class="hero-note">Title search works across the selected digest or the full archive.</span>
      </div>
    </div>
    <div class="hero-side">
      <div class="metric-card">
        <span>Latest refresh</span>
        <strong>{% if latest_post %}{{ latest_post.date | date: "%b %d" }}{% else %}--{% endif %}</strong>
      </div>
      <div class="metric-card">
        <span>Digests tracked</span>
        <strong>{{ site.posts | size }}</strong>
      </div>
      <div class="metric-card">
        <span>Indexed papers</span>
        <strong id="metric-indexed-count">Loading</strong>
      </div>
      <div class="metric-card">
        <span>Visible right now</span>
        <strong id="metric-scope-count">{% if latest_post and latest_post.paper_count %}{{ latest_post.paper_count }}{% else %}--{% endif %}</strong>
      </div>
    </div>
  </section>

  {% if site.posts.size > 0 %}
    <section class="dashboard-panel">
      <div class="control-grid">
        <div class="panel-block">
          <p class="section-label">Title Search</p>
          <h2 class="panel-title">Find papers by title</h2>
          <p class="panel-copy">
            Search is intentionally narrow and fast: it checks paper titles only, which keeps results precise even when multiple digests cover overlapping papers.
          </p>
          <div class="search-shell">
            <label class="section-label" for="paper-search">Search paper titles</label>
            <input id="paper-search" type="search" placeholder="Try: translation, WLASL, pose, Bangla, hallucinations" autocomplete="off">
            <p class="search-hint">Default scope is the latest digest. Choose “All papers” to search across the archive.</p>
          </div>
        </div>
        <div class="panel-block">
          <p class="section-label">Digest Picker</p>
          <h2 class="panel-title">Jump between updates without scrolling</h2>
          <p class="panel-copy">
            The archive is compressed into digest chips. Open a single update when you want the daily view, or switch to all papers for a deduplicated cross-digest browse.
          </p>
          <div class="digest-rail" id="digest-rail"></div>
        </div>
      </div>
      <div class="summary-grid">
        <div class="summary-card">
          <h2>Task mix</h2>
          <div class="summary-chip-cloud" id="task-summary"></div>
        </div>
        <div class="summary-card">
          <h2>Source mix</h2>
          <div class="summary-chip-cloud" id="source-summary"></div>
        </div>
      </div>
    </section>

    <section class="dashboard-panel results-panel">
      <div class="results-head">
        <div>
          <p class="section-label">Paper Browser</p>
          <h2 class="results-title" id="results-title">Loading latest digest</h2>
          <p class="results-meta" id="results-meta">Preparing the current paper set.</p>
        </div>
        <a class="results-link" id="active-digest-link" href="{% if latest_post %}{{ latest_post.url | relative_url }}{% else %}#{% endif %}">
          Open latest digest
        </a>
      </div>
      <div class="paper-browser-grid" id="paper-results"></div>
      <div class="empty-state" id="paper-empty" hidden></div>
    </section>
  {% else %}
    <section class="dashboard-panel noscript-card">
      No digests have been published yet. Run <code>python scripts/generate_sign_language_digest.py</code> to create the first one.
    </section>
  {% endif %}

  {% if latest_post %}
    <noscript>
      <section class="dashboard-panel noscript-card">
        JavaScript is required for the searchable dashboard. You can still open the latest digest <a href="{{ latest_post.url | relative_url }}">here</a>.
      </section>
    </noscript>
  {% endif %}
</div>

{% if site.posts.size > 0 %}
<script>
(function() {
  const digestSeeds = [
    {% for post in site.posts %}
      {
        id: {{ forloop.index0 }},
        title: {{ post.title | jsonify }},
        url: {{ post.url | relative_url | jsonify }},
        dateIso: {{ post.date | date_to_xmlschema | jsonify }},
        dateLabel: {{ post.date | date: "%b %d, %Y" | jsonify }},
        paperCount: {% if post.paper_count %}{{ post.paper_count }}{% else %}null{% endif %},
        papers: {% if post.paper_catalog_json %}{{ post.paper_catalog_json | strip }}{% else %}null{% endif %}
      }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  const elements = {
    digestRail: document.getElementById("digest-rail"),
    searchInput: document.getElementById("paper-search"),
    taskSummary: document.getElementById("task-summary"),
    sourceSummary: document.getElementById("source-summary"),
    resultsGrid: document.getElementById("paper-results"),
    resultsTitle: document.getElementById("results-title"),
    resultsMeta: document.getElementById("results-meta"),
    emptyState: document.getElementById("paper-empty"),
    activeDigestLink: document.getElementById("active-digest-link"),
    metricIndexedCount: document.getElementById("metric-indexed-count"),
    metricScopeCount: document.getElementById("metric-scope-count")
  };

  if (!digestSeeds.length) {
    return;
  }

  const digests = digestSeeds.map(function(seed) {
    const initialPapers = Array.isArray(seed.papers) ? seed.papers.map(function(paper) {
      return normalizePaper(paper, seed);
    }) : null;

    return {
      id: seed.id,
      title: seed.title,
      url: seed.url,
      dateIso: seed.dateIso,
      dateLabel: seed.dateLabel,
      paperCount: typeof seed.paperCount === "number" ? seed.paperCount : (initialPapers ? initialPapers.length : null),
      papers: initialPapers,
      loaded: Boolean(initialPapers),
      loadingPromise: null
    };
  });

  const state = {
    activeScope: "digest-" + String(digests[0].id),
    query: "",
    renderToken: 0
  };

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function escapeRegExp(value) {
    return String(value).replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function normalizeList(value) {
    if (Array.isArray(value)) {
      return value.map(function(item) {
        return String(item).trim();
      }).filter(Boolean);
    }

    if (!value) {
      return [];
    }

    return String(value)
      .split(",")
      .map(function(item) { return item.trim(); })
      .filter(Boolean);
  }

  function normalizePaper(paper, digest) {
    return {
      title: String(paper.title || "").trim(),
      authors: normalizeList(paper.authors),
      published: String(paper.published || "").trim(),
      tags: normalizeList(paper.tags),
      url: String(paper.url || "").trim(),
      source_site: String(paper.source_site || "Unknown").trim(),
      task_category: String(paper.task_category || "Other Sign Language Topic").trim(),
      short_summary: String(paper.short_summary || "").trim(),
      why_it_matters: String(paper.why_it_matters || "").trim(),
      digestTitle: digest.title,
      digestUrl: digest.url,
      digestDateIso: digest.dateIso,
      digestDateLabel: digest.dateLabel
    };
  }

  function extractFieldText(node, label) {
    if (!node) {
      return "";
    }

    const text = node.textContent.replace(/\s+/g, " ").trim();
    return text.replace(new RegExp("^" + escapeRegExp(label) + "\\s*:?\\s*", "i"), "").trim();
  }

  function parseDigestHtml(html, digest) {
    const doc = new DOMParser().parseFromString(html, "text/html");
    const cards = Array.from(doc.querySelectorAll(".paper-card"));

    return cards.map(function(card) {
      const chips = Array.from(card.querySelectorAll(".paper-chip-row .chip")).map(function(chip) {
        return chip.textContent.trim();
      });
      const summaryBlocks = Array.from(card.querySelectorAll(".paper-summary"));

      return normalizePaper(
        {
          title: card.querySelector("h3") ? card.querySelector("h3").textContent.trim() : "",
          authors: extractFieldText(card.querySelector(".paper-authors"), "Authors"),
          published: extractFieldText(card.querySelector(".paper-published"), "Published"),
          tags: extractFieldText(card.querySelector(".paper-tags"), "Tags"),
          url: card.querySelector(".paper-links a") ? card.querySelector(".paper-links a").href : "",
          source_site: chips[0] || "Unknown",
          task_category: chips[1] || "Other Sign Language Topic",
          short_summary: extractFieldText(summaryBlocks[0], "Summary"),
          why_it_matters: extractFieldText(summaryBlocks[1], "Why it matters")
        },
        digest
      );
    }).filter(function(paper) {
      return paper.title;
    });
  }

  function loadDigest(digest) {
    if (digest.loaded) {
      return Promise.resolve(digest);
    }

    if (digest.loadingPromise) {
      return digest.loadingPromise;
    }

    digest.loadingPromise = fetch(digest.url)
      .then(function(response) {
        if (!response.ok) {
          throw new Error("Unable to load digest: " + digest.url);
        }
        return response.text();
      })
      .then(function(html) {
        digest.papers = parseDigestHtml(html, digest);
        digest.paperCount = digest.paperCount || digest.papers.length;
        digest.loaded = true;
        renderDigestRail();
        refreshIndexedMetric();
        return digest;
      })
      .catch(function() {
        digest.papers = [];
        digest.paperCount = 0;
        digest.loaded = true;
        renderDigestRail();
        refreshIndexedMetric();
        return digest;
      })
      .finally(function() {
        digest.loadingPromise = null;
      });

    return digest.loadingPromise;
  }

  function ensureAllDigestsLoaded() {
    return Promise.all(digests.map(loadDigest));
  }

  function compareDates(a, b) {
    const timeA = Date.parse(a || "");
    const timeB = Date.parse(b || "");
    return (Number.isNaN(timeB) ? 0 : timeB) - (Number.isNaN(timeA) ? 0 : timeA);
  }

  function comparePapers(left, right) {
    const byPublished = compareDates(left.published || left.digestDateIso, right.published || right.digestDateIso);
    if (byPublished !== 0) {
      return byPublished;
    }
    return left.title.localeCompare(right.title);
  }

  function buildUniqueArchive() {
    const unique = new Map();

    digests.forEach(function(digest) {
      (digest.papers || []).forEach(function(paper) {
        const key = (paper.url || paper.title).toLowerCase();
        if (!unique.has(key)) {
          unique.set(key, paper);
        }
      });
    });

    return Array.from(unique.values()).sort(comparePapers);
  }

  function buildCounts(papers, field) {
    const counts = new Map();

    papers.forEach(function(paper) {
      const key = paper[field];
      if (!key) {
        return;
      }
      counts.set(key, (counts.get(key) || 0) + 1);
    });

    return Array.from(counts.entries()).sort(function(left, right) {
      if (right[1] !== left[1]) {
        return right[1] - left[1];
      }
      return left[0].localeCompare(right[0]);
    });
  }

  function renderCountCloud(container, counts, emptyText) {
    if (!counts.length) {
      container.innerHTML = '<p class="empty-summary">' + escapeHtml(emptyText) + "</p>";
      return;
    }

    container.innerHTML = counts.map(function(entry) {
      return '<span class="summary-chip">' + escapeHtml(entry[0]) + ' <strong>' + escapeHtml(entry[1]) + "</strong></span>";
    }).join("");
  }

  function buildPaperCard(paper, showDigestStamp) {
    const tags = paper.tags.slice(0, 4).map(function(tag) {
      return '<span class="tag-chip">' + escapeHtml(tag) + "</span>";
    }).join("");

    const summary = paper.short_summary ? '<p class="paper-summary"><strong>Summary:</strong> ' + escapeHtml(paper.short_summary) + "</p>" : "";
    const whyItMatters = paper.why_it_matters ? '<p class="paper-summary"><strong>Why it matters:</strong> ' + escapeHtml(paper.why_it_matters) + "</p>" : "";
    const digestStamp = showDigestStamp ? '<span class="paper-chip paper-digest-stamp">' + escapeHtml(paper.digestDateLabel) + "</span>" : "";

    return [
      '<article class="browser-card">',
      '  <div class="browser-card-top">',
      '    <span class="paper-chip">' + escapeHtml(paper.source_site) + "</span>",
      '    <span class="paper-chip">' + escapeHtml(paper.task_category) + "</span>",
           digestStamp,
      "  </div>",
      '  <h3>' + escapeHtml(paper.title) + "</h3>",
      '  <p class="paper-meta"><strong>Published:</strong> ' + escapeHtml(paper.published || paper.digestDateLabel) + "</p>",
      '  <p class="paper-meta"><strong>Authors:</strong> ' + escapeHtml(paper.authors.join(", ") || "Unknown") + "</p>",
           summary,
           whyItMatters,
           tags ? '  <div class="tag-row">' + tags + "</div>" : "",
      '  <a href="' + escapeHtml(paper.url || paper.digestUrl) + '" target="_blank" rel="noopener">Read the paper</a>',
      "</article>"
    ].join("");
  }

  function renderLoadingState(title) {
    elements.resultsTitle.textContent = title;
    elements.resultsMeta.textContent = "Loading papers for this view.";
    elements.emptyState.hidden = true;
    elements.resultsGrid.innerHTML = [
      '<div class="loading-card"></div>',
      '<div class="loading-card"></div>',
      '<div class="loading-card"></div>'
    ].join("");
  }

  function renderEmptyState(message) {
    elements.resultsGrid.innerHTML = "";
    elements.emptyState.textContent = message;
    elements.emptyState.hidden = false;
    elements.metricScopeCount.textContent = "0";
    renderCountCloud(elements.taskSummary, [], "No task distribution available for this search.");
    renderCountCloud(elements.sourceSummary, [], "No source distribution available for this search.");
  }

  function refreshIndexedMetric() {
    const allLoaded = digests.every(function(digest) {
      return digest.loaded;
    });

    if (!allLoaded) {
      elements.metricIndexedCount.textContent = "Loading";
      return;
    }

    elements.metricIndexedCount.textContent = String(buildUniqueArchive().length);
  }

  function renderDigestRail() {
    const allLoaded = digests.every(function(digest) {
      return digest.loaded;
    });
    const archiveCount = allLoaded ? buildUniqueArchive().length : null;
    const archiveMeta = archiveCount === null ? "Load archive" : archiveCount + " unique";

    const buttons = [
      '<button class="digest-pill' + (state.activeScope === "all" ? " active" : "") + '" type="button" data-scope="all" aria-pressed="' + (state.activeScope === "all") + '">',
      '  <span class="digest-pill-label">All papers</span>',
      '  <span class="digest-pill-meta">' + escapeHtml(archiveMeta) + "</span>",
      "</button>"
    ];

    digests.forEach(function(digest) {
      const scope = "digest-" + String(digest.id);
      const countText = digest.paperCount === null ? "Loading" : String(digest.paperCount) + " papers";
      buttons.push([
        '<button class="digest-pill' + (state.activeScope === scope ? " active" : "") + '" type="button" data-scope="' + scope + '" aria-pressed="' + (state.activeScope === scope) + '">',
        '  <span class="digest-pill-label">' + escapeHtml(digest.dateLabel) + "</span>",
        '  <span class="digest-pill-meta">' + escapeHtml(countText) + "</span>",
        "</button>"
      ].join(""));
    });

    elements.digestRail.innerHTML = buttons.join("");
    Array.from(elements.digestRail.querySelectorAll(".digest-pill")).forEach(function(button) {
      button.addEventListener("click", function() {
        const nextScope = button.getAttribute("data-scope");
        if (nextScope === state.activeScope) {
          return;
        }
        state.activeScope = nextScope;
        render();
      });
    });
  }

  function applyTitleSearch(papers) {
    if (!state.query) {
      return papers;
    }

    const query = state.query.toLowerCase();
    return papers.filter(function(paper) {
      return paper.title.toLowerCase().indexOf(query) !== -1;
    });
  }

  function renderResults(scopeLabel, sourcePapers, visiblePapers, digestLink, linkLabel, showDigestStamp) {
    elements.resultsTitle.textContent = scopeLabel;
    elements.metricScopeCount.textContent = String(visiblePapers.length);
    elements.activeDigestLink.href = digestLink || digests[0].url;
    elements.activeDigestLink.textContent = linkLabel;

    const searchSuffix = state.query ? ' Matching titles for "' + state.query + '".' : " Search checks titles only.";
    elements.resultsMeta.textContent = visiblePapers.length + " of " + sourcePapers.length + " papers visible." + searchSuffix;

    const summaryBase = state.query ? visiblePapers : sourcePapers;
    renderCountCloud(elements.taskSummary, buildCounts(summaryBase, "task_category"), "No task data for this view.");
    renderCountCloud(elements.sourceSummary, buildCounts(summaryBase, "source_site"), "No source data for this view.");

    if (!visiblePapers.length) {
      renderEmptyState("No papers match this title search. Try a shorter query or switch digest scope.");
      return;
    }

    elements.emptyState.hidden = true;
    elements.resultsGrid.innerHTML = visiblePapers.map(function(paper) {
      return buildPaperCard(paper, showDigestStamp);
    }).join("");
  }

  function getActiveDigest() {
    if (state.activeScope === "all") {
      return null;
    }

    const activeId = Number(state.activeScope.replace("digest-", ""));
    return digests.find(function(digest) {
      return digest.id === activeId;
    }) || digests[0];
  }

  async function render() {
    const currentToken = ++state.renderToken;
    renderDigestRail();

    if (state.activeScope === "all") {
      renderLoadingState("Loading archive");
      await ensureAllDigestsLoaded();
      if (currentToken !== state.renderToken) {
        return;
      }

      const archivePapers = buildUniqueArchive();
      const visiblePapers = applyTitleSearch(archivePapers);
      renderResults(
        "All indexed papers",
        archivePapers,
        visiblePapers,
        digests[0].url,
        "Open latest digest",
        true
      );
      refreshIndexedMetric();
      return;
    }

    const digest = getActiveDigest();
    renderLoadingState("Loading " + digest.dateLabel);
    await loadDigest(digest);
    if (currentToken !== state.renderToken) {
      return;
    }

    const papers = (digest.papers || []).slice().sort(comparePapers);
    const visiblePapers = applyTitleSearch(papers);
    renderResults(
      digest.dateLabel + " digest",
      papers,
      visiblePapers,
      digest.url,
      "Open full digest",
      false
    );
    refreshIndexedMetric();
  }

  elements.searchInput.addEventListener("input", function(event) {
    state.query = event.target.value.trim();
    render();
  });

  renderDigestRail();
  render();

  const prefetchArchive = function() {
    ensureAllDigestsLoaded().then(function() {
      renderDigestRail();
      refreshIndexedMetric();
      if (state.activeScope === "all") {
        render();
      }
    });
  };

  if ("requestIdleCallback" in window) {
    window.requestIdleCallback(prefetchArchive);
  } else {
    window.setTimeout(prefetchArchive, 900);
  }
})();
</script>
{% endif %}
