---
layout: default
title: "Sign Language & AI Date Browser"
---

{% assign latest_post = site.posts.first %}

<style>
:root {
  --browser-ink: #13212b;
  --browser-muted: #5f6971;
  --browser-border: rgba(19, 33, 43, 0.1);
  --browser-surface: #ffffff;
  --browser-soft: #f6f1e6;
  --browser-mist: #edf5ef;
  --browser-accent: #0f7a5c;
  --browser-accent-deep: #0a5640;
  --browser-accent-soft: #d8eee5;
  --browser-gold: #e2b060;
  --browser-shadow: 0 24px 60px rgba(19, 33, 43, 0.08);
}

.date-browser-shell {
  color: var(--browser-ink);
  font-family: "Avenir Next", "Segoe UI", sans-serif;
  padding: 2rem 0 3rem;
}

.date-browser-hero {
  position: relative;
  overflow: hidden;
  margin-bottom: 1.4rem;
  border: 1px solid var(--browser-border);
  border-radius: 1.85rem;
  padding: 2rem;
  background:
    radial-gradient(circle at top right, rgba(15, 122, 92, 0.14), transparent 32%),
    linear-gradient(135deg, #fffdf7 0%, #f1f8f3 54%, #f8efe0 100%);
  box-shadow: var(--browser-shadow);
}

.date-browser-hero::after {
  content: "";
  position: absolute;
  right: -4rem;
  bottom: -4rem;
  width: 13rem;
  height: 13rem;
  border-radius: 999px;
  background: rgba(226, 176, 96, 0.16);
}

.hero-inner {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: minmax(0, 1.6fr) minmax(280px, 0.9fr);
  gap: 1.25rem;
}

.eyebrow {
  margin: 0 0 0.8rem;
  color: var(--browser-accent-deep);
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.hero-title,
.panel-title,
.results-title,
.selected-date-title {
  margin: 0;
  font-family: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif;
}

.hero-title {
  max-width: 12ch;
  font-size: clamp(2.4rem, 5vw, 4.2rem);
  line-height: 0.98;
}

.hero-copy p {
  max-width: 60ch;
  margin: 1rem 0 0;
  color: var(--browser-muted);
  font-size: 1.03rem;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.35rem;
}

.hero-link,
.selected-link,
.latest-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  padding: 0.82rem 1.15rem;
  text-decoration: none;
  font-weight: 700;
}

.hero-link {
  background: var(--browser-accent);
  color: #fff;
  box-shadow: 0 16px 30px rgba(15, 122, 92, 0.18);
}

.hero-note {
  display: inline-flex;
  align-items: center;
  border: 1px solid rgba(15, 122, 92, 0.18);
  border-radius: 999px;
  padding: 0.82rem 1.1rem;
  background: rgba(255, 255, 255, 0.76);
  color: var(--browser-accent-deep);
  font-weight: 600;
}

.hero-stats {
  display: grid;
  gap: 0.85rem;
}

.hero-stat {
  border: 1px solid var(--browser-border);
  border-radius: 1.2rem;
  padding: 1rem 1.05rem;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(8px);
}

.hero-stat span {
  display: block;
  color: var(--browser-muted);
  font-size: 0.92rem;
}

.hero-stat strong {
  display: block;
  margin-top: 0.3rem;
  font-size: 1.95rem;
  line-height: 1;
}

.browser-layout {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(320px, 0.95fr);
  gap: 1.2rem;
}

.browser-panel,
.papers-panel {
  border: 1px solid var(--browser-border);
  border-radius: 1.55rem;
  background: var(--browser-surface);
  box-shadow: var(--browser-shadow);
}

.browser-panel {
  padding: 1.25rem;
}

.panel-heading {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.panel-title {
  font-size: 1.65rem;
}

.panel-copy,
.selected-copy,
.results-copy,
.calendar-note,
.search-note,
.feedback-message,
.empty-state {
  color: var(--browser-muted);
  line-height: 1.6;
}

.panel-copy {
  margin: 0.55rem 0 0;
}

.nav-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  margin-top: 1.15rem;
}

.latest-button {
  border: 0;
  background: var(--browser-accent);
  color: #fff;
  cursor: pointer;
}

.jump-field {
  display: grid;
  gap: 0.35rem;
}

.jump-field label,
.search-label,
.scope-label {
  color: var(--browser-accent-deep);
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.jump-field input,
.search-shell input {
  min-height: 2.9rem;
  border: 1px solid rgba(19, 33, 43, 0.12);
  border-radius: 1rem;
  padding: 0.7rem 0.9rem;
  background: #fbfaf6;
  color: var(--browser-ink);
  font: inherit;
  box-sizing: border-box;
}

.jump-field input:focus,
.search-shell input:focus {
  outline: 2px solid rgba(15, 122, 92, 0.18);
  border-color: rgba(15, 122, 92, 0.35);
}

.month-strip {
  display: flex;
  gap: 0.65rem;
  overflow-x: auto;
  margin-top: 1.2rem;
  padding-bottom: 0.2rem;
}

.month-strip::-webkit-scrollbar {
  height: 0.55rem;
}

.month-strip::-webkit-scrollbar-thumb {
  border-radius: 999px;
  background: rgba(19, 33, 43, 0.12);
}

.month-chip {
  min-width: 8.75rem;
  border: 1px solid rgba(19, 33, 43, 0.09);
  border-radius: 1.05rem;
  padding: 0.85rem 0.95rem;
  background: linear-gradient(180deg, #ffffff 0%, #f7f2e8 100%);
  color: var(--browser-ink);
  text-align: left;
  cursor: pointer;
  transition: transform 160ms ease, border-color 160ms ease, box-shadow 160ms ease;
}

.month-chip:hover,
.month-chip:focus-visible {
  transform: translateY(-1px);
  border-color: rgba(15, 122, 92, 0.3);
  box-shadow: 0 14px 26px rgba(19, 33, 43, 0.08);
  outline: none;
}

.month-chip.active {
  border-color: transparent;
  background: linear-gradient(135deg, var(--browser-accent) 0%, #17956f 100%);
  color: #fff;
}

.month-chip-label,
.month-chip-meta {
  display: block;
}

.month-chip-label {
  font-weight: 700;
}

.month-chip-meta {
  margin-top: 0.35rem;
  font-size: 0.9rem;
  opacity: 0.82;
}

.calendar-shell {
  margin-top: 1.2rem;
  border: 1px solid rgba(19, 33, 43, 0.08);
  border-radius: 1.35rem;
  padding: 1rem;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.98) 0%, rgba(247, 242, 232, 0.96) 100%);
}

.calendar-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 0.95rem;
}

.calendar-title-wrap {
  min-width: 0;
}

.calendar-title {
  margin: 0;
  font-size: 1.25rem;
}

.calendar-note {
  margin: 0.25rem 0 0;
  font-size: 0.92rem;
}

.calendar-nav {
  display: inline-flex;
  gap: 0.55rem;
}

.calendar-nav button,
.scope-button {
  border: 1px solid rgba(19, 33, 43, 0.1);
  border-radius: 999px;
  background: #fff;
  color: var(--browser-ink);
  cursor: pointer;
  font: inherit;
}

.calendar-nav button {
  min-width: 2.75rem;
  min-height: 2.75rem;
  padding: 0.4rem 0.8rem;
  font-weight: 700;
}

.calendar-nav button:hover,
.calendar-nav button:focus-visible,
.scope-button:hover,
.scope-button:focus-visible {
  border-color: rgba(15, 122, 92, 0.28);
  outline: none;
}

.calendar-nav button:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}

.calendar-weekdays,
.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, minmax(0, 1fr));
  gap: 0.55rem;
}

.calendar-weekdays {
  margin-bottom: 0.55rem;
}

.calendar-weekday {
  text-align: center;
  color: var(--browser-muted);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.calendar-cell {
  min-height: 4.9rem;
}

.calendar-day,
.calendar-blank {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  width: 100%;
  min-height: 4.9rem;
  border-radius: 1rem;
  box-sizing: border-box;
}

.calendar-blank {
  background: transparent;
}

.calendar-day {
  border: 1px solid rgba(19, 33, 43, 0.08);
  padding: 0.7rem;
  background: rgba(255, 255, 255, 0.88);
  color: var(--browser-ink);
}

.calendar-day.has-post {
  cursor: pointer;
  background: linear-gradient(180deg, #ffffff 0%, #eef7f2 100%);
}

.calendar-day.has-post:hover,
.calendar-day.has-post:focus-visible {
  border-color: rgba(15, 122, 92, 0.3);
  transform: translateY(-1px);
  box-shadow: 0 14px 24px rgba(19, 33, 43, 0.08);
  outline: none;
}

.calendar-day.selected {
  border-color: transparent;
  background: linear-gradient(135deg, var(--browser-accent) 0%, #17956f 100%);
  color: #fff;
  box-shadow: 0 16px 28px rgba(15, 122, 92, 0.2);
}

.calendar-day.muted {
  background: rgba(245, 243, 238, 0.8);
  color: #a0a5aa;
}

.calendar-day-number {
  font-size: 0.95rem;
  font-weight: 700;
}

.calendar-day-meta {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  border-radius: 999px;
  padding: 0.23rem 0.56rem;
  background: rgba(15, 122, 92, 0.1);
  color: var(--browser-accent-deep);
  font-size: 0.78rem;
  font-weight: 700;
}

.calendar-day.selected .calendar-day-meta {
  background: rgba(255, 255, 255, 0.16);
  color: #fff;
}

.feedback-message {
  min-height: 1.4rem;
  margin: 0.9rem 0 0;
  font-size: 0.92rem;
}

.selection-panel {
  display: grid;
  gap: 1rem;
}

.selected-summary-card,
.search-card,
.meta-card {
  border: 1px solid rgba(19, 33, 43, 0.08);
  border-radius: 1.35rem;
  padding: 1rem;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.98) 0%, rgba(248, 244, 235, 0.98) 100%);
}

.selected-date-title {
  font-size: clamp(1.7rem, 3.4vw, 2.45rem);
}

.selected-copy {
  margin: 0.55rem 0 0;
}

.selected-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin-top: 1rem;
}

.selected-stat,
.meta-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  border-radius: 999px;
  font-size: 0.84rem;
}

.selected-stat {
  padding: 0.45rem 0.75rem;
  background: var(--browser-mist);
  color: var(--browser-accent-deep);
  font-weight: 700;
}

.selected-link {
  width: 100%;
  margin-top: 1rem;
  background: var(--browser-accent);
  color: #fff;
}

.search-shell {
  margin-top: 0.8rem;
}

.search-note {
  margin: 0.55rem 0 0;
  font-size: 0.92rem;
}

.scope-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin-top: 0.85rem;
}

.scope-button {
  padding: 0.55rem 0.85rem;
}

.scope-button.active {
  border-color: transparent;
  background: var(--browser-accent);
  color: #fff;
}

.meta-card h3,
.search-card h3 {
  margin: 0;
  font-size: 1rem;
}

.meta-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin-top: 0.75rem;
}

.meta-chip {
  padding: 0.35rem 0.65rem;
  background: #eef6f2;
  color: var(--browser-accent-deep);
  font-weight: 700;
}

.papers-panel {
  margin-top: 1.2rem;
  padding: 1.25rem;
}

.results-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.results-title {
  font-size: clamp(1.9rem, 4vw, 2.55rem);
}

.results-copy {
  margin: 0.55rem 0 0;
}

.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin-top: 1.2rem;
}

.paper-card {
  display: flex;
  flex-direction: column;
  gap: 0.78rem;
  min-height: 100%;
  border: 1px solid rgba(19, 33, 43, 0.08);
  border-radius: 1.35rem;
  padding: 1.05rem;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.98) 0%, rgba(250, 247, 240, 0.98) 100%);
}

.paper-top {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.paper-chip,
.tag-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  border-radius: 999px;
  font-size: 0.8rem;
}

.paper-chip {
  padding: 0.28rem 0.62rem;
  background: #eef6f2;
  color: var(--browser-accent-deep);
  font-weight: 700;
}

.paper-date-chip {
  background: #f7ebd9;
  color: #88591c;
}

.paper-card h3 {
  margin: 0;
  font-size: 1.08rem;
  line-height: 1.45;
}

.paper-meta,
.paper-summary {
  margin: 0;
  color: var(--browser-muted);
  font-size: 0.93rem;
  line-height: 1.6;
}

.paper-meta strong,
.paper-summary strong {
  color: var(--browser-ink);
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.tag-chip {
  padding: 0.28rem 0.56rem;
  background: #f1eee6;
  color: #5c5b56;
  font-weight: 600;
}

.paper-card a {
  margin-top: auto;
  color: var(--browser-accent);
  font-weight: 700;
  text-decoration: none;
}

.paper-card a:hover,
.paper-card a:focus-visible,
.hero-link:hover,
.hero-link:focus-visible,
.selected-link:hover,
.selected-link:focus-visible {
  text-decoration: underline;
}

.loading-card {
  min-height: 16rem;
  border-radius: 1.35rem;
  background:
    linear-gradient(110deg, rgba(247, 242, 232, 0.95) 8%, rgba(255, 255, 255, 0.95) 18%, rgba(247, 242, 232, 0.95) 33%);
  background-size: 200% 100%;
  animation: browser-shimmer 1.2s linear infinite;
}

.empty-state {
  margin-top: 1.2rem;
  border: 1px dashed rgba(19, 33, 43, 0.15);
  border-radius: 1.2rem;
  padding: 1rem 1.1rem;
  background: #fbfaf6;
}

.noscript-panel {
  margin-top: 1.2rem;
  padding: 1rem 1.1rem;
}

@keyframes browser-shimmer {
  to {
    background-position: -200% 0;
  }
}

@media (max-width: 980px) {
  .hero-inner,
  .browser-layout {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 720px) {
  .date-browser-hero,
  .browser-panel,
  .papers-panel {
    padding: 1rem;
  }

  .calendar-shell {
    padding: 0.8rem;
  }

  .calendar-grid,
  .calendar-weekdays {
    gap: 0.4rem;
  }

  .calendar-cell {
    min-height: 4.2rem;
  }

  .calendar-day {
    min-height: 4.2rem;
    padding: 0.55rem;
  }

  .results-head,
  .calendar-top {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>

<div class="date-browser-shell">
  <section class="date-browser-hero">
    <div class="hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">Date-First Archive</p>
        <h1 class="hero-title">Browse papers by day, not by a long feed.</h1>
        <p>
          I redesigned the homepage around date selection first. Pick a month, click a published day in the calendar, and the paper list opens immediately below. If you know the exact day, jump there directly with the date picker.
        </p>
        <div class="hero-actions">
          {% if latest_post %}
            <a class="hero-link" href="{{ latest_post.url | relative_url }}">Open latest digest</a>
          {% endif %}
          <span class="hero-note">Calendar drill-down is inspired by GitHub-style day selection and Airtable-style date navigation.</span>
        </div>
      </div>
      <div class="hero-stats">
        <div class="hero-stat">
          <span>Latest digest</span>
          <strong>{% if latest_post %}{{ latest_post.date | date: "%b %d" }}{% else %}--{% endif %}</strong>
        </div>
        <div class="hero-stat">
          <span>Archive days</span>
          <strong>{{ site.posts | size }}</strong>
        </div>
        <div class="hero-stat">
          <span>Visible papers</span>
          <strong id="metric-visible-papers">{% if latest_post and latest_post.paper_count %}{{ latest_post.paper_count }}{% else %}--{% endif %}</strong>
        </div>
        <div class="hero-stat">
          <span>Indexed archive</span>
          <strong id="metric-archive-papers">Loading</strong>
        </div>
      </div>
    </div>
  </section>

  {% if site.posts.size > 0 %}
    <section class="browser-layout">
      <section class="browser-panel">
        <div class="panel-heading">
          <div>
            <p class="eyebrow">Select a Date</p>
            <h2 class="panel-title">Calendar navigation for digest days</h2>
            <p class="panel-copy">
              The archive is grouped by month. Only days with published digests are active, so date selection stays compact even when the archive grows.
            </p>
          </div>
        </div>

        <div class="nav-controls">
          <button class="latest-button" id="jump-latest" type="button">Jump to latest</button>
          <div class="jump-field">
            <label for="jump-date">Go to date</label>
            <input id="jump-date" type="date">
          </div>
        </div>

        <div class="month-strip" id="month-strip"></div>

        <div class="calendar-shell">
          <div class="calendar-top">
            <div class="calendar-title-wrap">
              <h3 class="calendar-title" id="calendar-title">Loading month</h3>
              <p class="calendar-note" id="calendar-note">Choose a day with a digest to open its paper list.</p>
            </div>
            <div class="calendar-nav">
              <button id="prev-month" type="button" aria-label="Previous month">&larr;</button>
              <button id="next-month" type="button" aria-label="Next month">&rarr;</button>
            </div>
          </div>

          <div class="calendar-weekdays">
            <div class="calendar-weekday">Sun</div>
            <div class="calendar-weekday">Mon</div>
            <div class="calendar-weekday">Tue</div>
            <div class="calendar-weekday">Wed</div>
            <div class="calendar-weekday">Thu</div>
            <div class="calendar-weekday">Fri</div>
            <div class="calendar-weekday">Sat</div>
          </div>

          <div class="calendar-grid" id="calendar-grid"></div>
          <p class="feedback-message" id="date-feedback"></p>
        </div>
      </section>

      <section class="selection-panel">
        <div class="browser-panel selected-summary-card">
          <p class="eyebrow">Selected Day</p>
          <h2 class="selected-date-title" id="selected-date-label">Loading date</h2>
          <p class="selected-copy" id="selected-summary">Preparing papers for the selected digest.</p>
          <div class="selected-stats" id="selected-stats"></div>
          <a class="selected-link" id="selected-digest-link" href="{% if latest_post %}{{ latest_post.url | relative_url }}{% else %}#{% endif %}">
            Open full digest
          </a>
        </div>

        <div class="browser-panel search-card">
          <p class="eyebrow">Paper Search</p>
          <h3>Search by paper title</h3>
          <div class="search-shell">
            <label class="search-label" for="paper-search">Paper title</label>
            <input id="paper-search" type="search" placeholder="Try: translation, hallucinations, WLASL, pose, Bangla" autocomplete="off">
            <p class="search-note">Default search stays on the selected date. Switch to archive search if you want to search all indexed papers.</p>
          </div>
          <div class="scope-row" id="scope-row">
            <span class="scope-label">Search scope</span>
          </div>
        </div>

        <div class="browser-panel meta-card">
          <p class="eyebrow">At a Glance</p>
          <h3>Task and source mix</h3>
          <div class="meta-cloud" id="meta-cloud"></div>
        </div>
      </section>
    </section>

    <section class="papers-panel">
      <div class="results-head">
        <div>
          <p class="eyebrow">Paper List</p>
          <h2 class="results-title" id="results-title">Loading papers</h2>
          <p class="results-copy" id="results-copy">Preparing the selected list.</p>
        </div>
      </div>
      <div class="results-grid" id="paper-results"></div>
      <div class="empty-state" id="paper-empty" hidden></div>
    </section>
  {% else %}
    <section class="browser-panel noscript-panel">
      No digests have been published yet. Run <code>python scripts/generate_sign_language_digest.py</code> to create the first one.
    </section>
  {% endif %}

  {% if latest_post %}
    <noscript>
      <section class="browser-panel noscript-panel">
        JavaScript is required for the date browser. You can still open the latest digest <a href="{{ latest_post.url | relative_url }}">here</a>.
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
        dateValue: {{ post.date | date: "%Y-%m-%d" | jsonify }},
        dateLabel: {{ post.date | date: "%b %d, %Y" | jsonify }},
        paperCount: {% if post.paper_count %}{{ post.paper_count }}{% else %}null{% endif %},
        papers: {% if post.paper_catalog_json %}{{ post.paper_catalog_json | strip }}{% else %}null{% endif %}
      }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  const elements = {
    jumpLatest: document.getElementById("jump-latest"),
    jumpDate: document.getElementById("jump-date"),
    monthStrip: document.getElementById("month-strip"),
    prevMonth: document.getElementById("prev-month"),
    nextMonth: document.getElementById("next-month"),
    calendarTitle: document.getElementById("calendar-title"),
    calendarNote: document.getElementById("calendar-note"),
    calendarGrid: document.getElementById("calendar-grid"),
    dateFeedback: document.getElementById("date-feedback"),
    selectedDateLabel: document.getElementById("selected-date-label"),
    selectedSummary: document.getElementById("selected-summary"),
    selectedStats: document.getElementById("selected-stats"),
    selectedDigestLink: document.getElementById("selected-digest-link"),
    paperSearch: document.getElementById("paper-search"),
    scopeRow: document.getElementById("scope-row"),
    metaCloud: document.getElementById("meta-cloud"),
    resultsTitle: document.getElementById("results-title"),
    resultsCopy: document.getElementById("results-copy"),
    paperResults: document.getElementById("paper-results"),
    paperEmpty: document.getElementById("paper-empty"),
    metricVisiblePapers: document.getElementById("metric-visible-papers"),
    metricArchivePapers: document.getElementById("metric-archive-papers")
  };

  if (!digestSeeds.length) {
    return;
  }

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
      .map(function(item) {
        return item.trim();
      })
      .filter(Boolean);
  }

  function formatDateLong(dateValue) {
    const date = new Date(dateValue + "T00:00:00Z");
    return new Intl.DateTimeFormat("en-US", {
      month: "long",
      day: "numeric",
      year: "numeric",
      timeZone: "UTC"
    }).format(date);
  }

  function formatMonthLabel(year, monthIndex) {
    return new Intl.DateTimeFormat("en-US", {
      month: "long",
      year: "numeric",
      timeZone: "UTC"
    }).format(new Date(Date.UTC(year, monthIndex, 1)));
  }

  function getDateParts(dateValue) {
    const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(dateValue);
    return {
      year: Number(match[1]),
      monthIndex: Number(match[2]) - 1,
      day: Number(match[3])
    };
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
      digestId: digest.id,
      digestTitle: digest.title,
      digestUrl: digest.url,
      digestDateIso: digest.dateIso,
      digestDateValue: digest.dateValue,
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
      const summaries = Array.from(card.querySelectorAll(".paper-summary"));

      return normalizePaper(
        {
          title: card.querySelector("h3") ? card.querySelector("h3").textContent.trim() : "",
          authors: extractFieldText(card.querySelector(".paper-authors"), "Authors"),
          published: extractFieldText(card.querySelector(".paper-published"), "Published"),
          tags: extractFieldText(card.querySelector(".paper-tags"), "Tags"),
          url: card.querySelector(".paper-links a") ? card.querySelector(".paper-links a").href : "",
          source_site: chips[0] || "Unknown",
          task_category: chips[1] || "Other Sign Language Topic",
          short_summary: extractFieldText(summaries[0], "Summary"),
          why_it_matters: extractFieldText(summaries[1], "Why it matters")
        },
        digest
      );
    }).filter(function(paper) {
      return paper.title;
    });
  }

  function compareDatesDesc(left, right) {
    return Date.parse(right) - Date.parse(left);
  }

  const digests = digestSeeds.map(function(seed) {
    const parts = getDateParts(seed.dateValue);
    const initialPapers = Array.isArray(seed.papers) ? seed.papers.map(function(paper) {
      return normalizePaper(paper, seed);
    }) : null;

    return {
      id: seed.id,
      title: seed.title,
      url: seed.url,
      dateIso: seed.dateIso,
      dateValue: seed.dateValue,
      dateLabel: seed.dateLabel,
      dateLong: formatDateLong(seed.dateValue),
      year: parts.year,
      monthIndex: parts.monthIndex,
      day: parts.day,
      monthKey: seed.dateValue.slice(0, 7),
      monthLabel: formatMonthLabel(parts.year, parts.monthIndex),
      paperCount: typeof seed.paperCount === "number" ? seed.paperCount : (initialPapers ? initialPapers.length : null),
      papers: initialPapers,
      loaded: Boolean(initialPapers),
      loadingPromise: null
    };
  }).sort(function(left, right) {
    return compareDatesDesc(left.dateIso, right.dateIso);
  });

  const digestById = new Map();
  const digestByDate = new Map();
  digests.forEach(function(digest) {
    digestById.set(digest.id, digest);
    digestByDate.set(digest.dateValue, digest);
  });

  const months = [];
  const monthMap = new Map();
  digests.forEach(function(digest) {
    if (!monthMap.has(digest.monthKey)) {
      const item = {
        key: digest.monthKey,
        label: digest.monthLabel,
        year: digest.year,
        monthIndex: digest.monthIndex,
        digests: []
      };
      monthMap.set(digest.monthKey, item);
      months.push(item);
    }
    monthMap.get(digest.monthKey).digests.push(digest);
  });

  months.forEach(function(month) {
    month.digests.sort(function(left, right) {
      return left.day - right.day;
    });
  });

  months.sort(function(left, right) {
    return compareDatesDesc(left.key + "-01T00:00:00Z", right.key + "-01T00:00:00Z");
  });

  const state = {
    activeDigestId: digests[0].id,
    activeMonthKey: digests[0].monthKey,
    query: "",
    searchScope: "selected",
    feedback: "",
    renderToken: 0
  };

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
        renderMonthStrip();
        renderCalendar();
        refreshArchiveMetric();
        return digest;
      })
      .catch(function() {
        digest.papers = [];
        digest.paperCount = 0;
        digest.loaded = true;
        renderMonthStrip();
        renderCalendar();
        refreshArchiveMetric();
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

    return Array.from(unique.values()).sort(function(left, right) {
      const leftDate = left.published || left.digestDateValue;
      const rightDate = right.published || right.digestDateValue;
      const delta = compareDatesDesc(leftDate + "T00:00:00Z", rightDate + "T00:00:00Z");
      if (delta !== 0) {
        return delta;
      }
      return left.title.localeCompare(right.title);
    });
  }

  function refreshArchiveMetric() {
    const allLoaded = digests.every(function(digest) {
      return digest.loaded;
    });

    if (!allLoaded) {
      elements.metricArchivePapers.textContent = "Loading";
      return;
    }

    elements.metricArchivePapers.textContent = String(buildUniqueArchive().length);
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

  function getActiveDigest() {
    return digestById.get(state.activeDigestId) || digests[0];
  }

  function getActiveMonth() {
    return monthMap.get(state.activeMonthKey) || months[0];
  }

  function findClosestDigest(dateValue) {
    const target = Date.parse(dateValue + "T00:00:00Z");
    let closest = digests[0];
    let distance = Math.abs(Date.parse(closest.dateIso) - target);

    digests.forEach(function(digest) {
      const nextDistance = Math.abs(Date.parse(digest.dateIso) - target);
      if (nextDistance < distance) {
        closest = digest;
        distance = nextDistance;
      }
    });

    return closest;
  }

  function applySearch(papers) {
    if (!state.query) {
      return papers;
    }

    const query = state.query.toLowerCase();
    return papers.filter(function(paper) {
      return paper.title.toLowerCase().indexOf(query) !== -1;
    });
  }

  function renderMonthStrip() {
    const html = months.map(function(month) {
      return [
        '<button class="month-chip' + (month.key === state.activeMonthKey ? " active" : "") + '" type="button" data-month-key="' + escapeHtml(month.key) + '">',
        '  <span class="month-chip-label">' + escapeHtml(month.label) + "</span>",
        '  <span class="month-chip-meta">' + escapeHtml(month.digests.length) + ' update days</span>',
        "</button>"
      ].join("");
    }).join("");

    elements.monthStrip.innerHTML = html;
    Array.from(elements.monthStrip.querySelectorAll(".month-chip")).forEach(function(button) {
      button.addEventListener("click", function() {
        const monthKey = button.getAttribute("data-month-key");
        state.activeMonthKey = monthKey;
        const month = monthMap.get(monthKey);
        if (month && !month.digests.some(function(digest) { return digest.id === state.activeDigestId; })) {
          state.activeDigestId = month.digests[month.digests.length - 1].id;
        }
        state.feedback = "";
        renderCalendar();
        renderSelectedSummary();
        render();
      });
    });
  }

  function renderCalendar() {
    const month = getActiveMonth();
    const activeDigest = getActiveDigest();
    const monthIndexInList = months.findIndex(function(item) {
      return item.key === month.key;
    });
    const firstWeekday = new Date(Date.UTC(month.year, month.monthIndex, 1)).getUTCDay();
    const daysInMonth = new Date(Date.UTC(month.year, month.monthIndex + 1, 0)).getUTCDate();
    const digestByDay = new Map();

    month.digests.forEach(function(digest) {
      digestByDay.set(digest.day, digest);
    });

    elements.calendarTitle.textContent = month.label;
    elements.calendarNote.textContent = month.digests.length + " published day" + (month.digests.length === 1 ? "" : "s") + " in this month.";
    elements.dateFeedback.textContent = state.feedback;
    elements.prevMonth.disabled = monthIndexInList >= months.length - 1;
    elements.nextMonth.disabled = monthIndexInList <= 0;

    const cells = [];
    for (let i = 0; i < firstWeekday; i += 1) {
      cells.push('<div class="calendar-cell"><div class="calendar-blank"></div></div>');
    }

    for (let day = 1; day <= daysInMonth; day += 1) {
      const digest = digestByDay.get(day);
      if (digest) {
        cells.push([
          '<div class="calendar-cell">',
          '  <button class="calendar-day has-post' + (digest.id === activeDigest.id ? " selected" : "") + '" type="button" data-digest-id="' + escapeHtml(digest.id) + '" aria-label="Open papers for ' + escapeHtml(digest.dateLong) + '">',
          '    <span class="calendar-day-number">' + escapeHtml(day) + "</span>",
          '    <span class="calendar-day-meta">' + escapeHtml(digest.paperCount === null ? "..." : digest.paperCount) + " papers</span>",
          "  </button>",
          "</div>"
        ].join(""));
      } else {
        cells.push([
          '<div class="calendar-cell">',
          '  <div class="calendar-day muted" aria-hidden="true">',
          '    <span class="calendar-day-number">' + escapeHtml(day) + "</span>",
          "  </div>",
          "</div>"
        ].join(""));
      }
    }

    elements.calendarGrid.innerHTML = cells.join("");
    Array.from(elements.calendarGrid.querySelectorAll(".calendar-day.has-post")).forEach(function(button) {
      button.addEventListener("click", function() {
        state.activeDigestId = Number(button.getAttribute("data-digest-id"));
        state.feedback = "";
        renderCalendar();
        renderSelectedSummary();
        render();
      });
    });
  }

  function renderSelectedSummary() {
    const digest = getActiveDigest();
    const countText = digest.paperCount === null ? "Paper count is loading for this digest." : digest.paperCount + " papers are available for this digest day.";
    elements.selectedDateLabel.textContent = digest.dateLong;
    elements.selectedSummary.textContent = countText + " Open this day to read the full digest, or scan the paper cards below directly on the homepage.";
    elements.selectedDigestLink.href = digest.url;
    elements.jumpDate.value = digest.dateValue;

    const stats = [
      '<span class="selected-stat">' + escapeHtml(digest.paperCount === null ? "Loading" : digest.paperCount) + " papers</span>",
      '<span class="selected-stat">' + escapeHtml(digest.monthLabel) + "</span>"
    ];

    if (state.searchScope === "all") {
      stats.push('<span class="selected-stat">Archive search enabled</span>');
    }

    elements.selectedStats.innerHTML = stats.join("");
  }

  function renderScopeButtons() {
    const buttons = [
      { key: "selected", label: "Selected date" },
      { key: "all", label: "All dates" }
    ];

    const markup = buttons.map(function(button) {
      return '<button class="scope-button' + (button.key === state.searchScope ? " active" : "") + '" type="button" data-scope="' + button.key + '">' + escapeHtml(button.label) + "</button>";
    }).join("");

    elements.scopeRow.innerHTML = '<span class="scope-label">Search scope</span>' + markup;
    Array.from(elements.scopeRow.querySelectorAll(".scope-button")).forEach(function(button) {
      button.addEventListener("click", function() {
        const nextScope = button.getAttribute("data-scope");
        if (nextScope === state.searchScope) {
          return;
        }
        state.searchScope = nextScope;
        renderSelectedSummary();
        render();
      });
    });
  }

  function renderMetaCloud(papers) {
    const taskCounts = buildCounts(papers, "task_category").slice(0, 3);
    const sourceCounts = buildCounts(papers, "source_site").slice(0, 3);
    const chips = [];

    taskCounts.forEach(function(item) {
      chips.push('<span class="meta-chip">' + escapeHtml(item[0]) + " · " + escapeHtml(item[1]) + "</span>");
    });

    sourceCounts.forEach(function(item) {
      chips.push('<span class="meta-chip">' + escapeHtml(item[0]) + " · " + escapeHtml(item[1]) + "</span>");
    });

    elements.metaCloud.innerHTML = chips.length ? chips.join("") : '<span class="meta-chip">No metadata yet</span>';
  }

  function buildPaperCard(paper, showDateChip) {
    const tags = paper.tags.slice(0, 4).map(function(tag) {
      return '<span class="tag-chip">' + escapeHtml(tag) + "</span>";
    }).join("");

    const dateChip = showDateChip ? '<span class="paper-chip paper-date-chip">' + escapeHtml(formatDateLong(paper.digestDateValue)) + "</span>" : "";

    return [
      '<article class="paper-card">',
      '  <div class="paper-top">',
      '    <span class="paper-chip">' + escapeHtml(paper.source_site) + "</span>",
      '    <span class="paper-chip">' + escapeHtml(paper.task_category) + "</span>",
           dateChip,
      "  </div>",
      '  <h3>' + escapeHtml(paper.title) + "</h3>",
      '  <p class="paper-meta"><strong>Published:</strong> ' + escapeHtml(paper.published || paper.digestDateValue) + "</p>",
      '  <p class="paper-meta"><strong>Authors:</strong> ' + escapeHtml(paper.authors.join(", ") || "Unknown") + "</p>",
      (paper.short_summary ? '  <p class="paper-summary"><strong>Summary:</strong> ' + escapeHtml(paper.short_summary) + "</p>" : ""),
      (tags ? '  <div class="tag-row">' + tags + "</div>" : ""),
      '  <a href="' + escapeHtml(paper.url || paper.digestUrl) + '" target="_blank" rel="noopener">Read the paper</a>',
      "</article>"
    ].join("");
  }

  function renderLoadingState(title, copy) {
    elements.resultsTitle.textContent = title;
    elements.resultsCopy.textContent = copy;
    elements.paperEmpty.hidden = true;
    elements.paperResults.innerHTML = [
      '<div class="loading-card"></div>',
      '<div class="loading-card"></div>',
      '<div class="loading-card"></div>'
    ].join("");
  }

  function renderEmptyState(message) {
    elements.paperResults.innerHTML = "";
    elements.paperEmpty.textContent = message;
    elements.paperEmpty.hidden = false;
    elements.metricVisiblePapers.textContent = "0";
    renderMetaCloud([]);
  }

  function moveMonth(step) {
    const currentIndex = months.findIndex(function(month) {
      return month.key === state.activeMonthKey;
    });
    const nextIndex = currentIndex + step;
    if (nextIndex < 0 || nextIndex >= months.length) {
      return;
    }

    const month = months[nextIndex];
    state.activeMonthKey = month.key;
    if (!month.digests.some(function(digest) { return digest.id === state.activeDigestId; })) {
      state.activeDigestId = month.digests[month.digests.length - 1].id;
    }
    state.feedback = "";
    renderMonthStrip();
    renderCalendar();
    renderSelectedSummary();
    render();
  }

  async function render() {
    const currentToken = ++state.renderToken;
    const digest = getActiveDigest();
    const searchMode = state.searchScope;
    renderScopeButtons();
    renderSelectedSummary();

    if (searchMode === "selected") {
      renderLoadingState(digest.dateLong, "Loading papers from the selected digest.");
      await loadDigest(digest);
      if (currentToken !== state.renderToken) {
        return;
      }

      renderSelectedSummary();
      const sourcePapers = (digest.papers || []).slice();
      const visiblePapers = applySearch(sourcePapers);
      elements.metricVisiblePapers.textContent = String(visiblePapers.length);
      renderMetaCloud(sourcePapers);
      elements.resultsTitle.textContent = digest.dateLong;
      elements.resultsCopy.textContent = visiblePapers.length + " of " + sourcePapers.length + " papers visible for the selected day." + (state.query ? ' Matching title "' + state.query + '".' : "");

      if (!visiblePapers.length) {
        renderEmptyState("No papers match this title search for the selected date.");
        return;
      }

      elements.paperEmpty.hidden = true;
      elements.paperResults.innerHTML = visiblePapers.map(function(paper) {
        return buildPaperCard(paper, false);
      }).join("");
      return;
    }

    renderLoadingState("All indexed dates", "Loading papers across the archive.");
    await ensureAllDigestsLoaded();
    if (currentToken !== state.renderToken) {
      return;
    }

    renderSelectedSummary();
    const archivePapers = buildUniqueArchive();
    const visibleArchive = applySearch(archivePapers);
    elements.metricVisiblePapers.textContent = String(visibleArchive.length);
    renderMetaCloud(archivePapers);
    elements.resultsTitle.textContent = "All indexed dates";
    elements.resultsCopy.textContent = visibleArchive.length + " of " + archivePapers.length + " papers visible across the archive." + (state.query ? ' Matching title "' + state.query + '".' : "");

    if (!visibleArchive.length) {
      renderEmptyState("No archive papers match this title search.");
      return;
    }

    elements.paperEmpty.hidden = true;
    elements.paperResults.innerHTML = visibleArchive.map(function(paper) {
      return buildPaperCard(paper, true);
    }).join("");
    refreshArchiveMetric();
  }

  elements.jumpLatest.addEventListener("click", function() {
    state.activeDigestId = digests[0].id;
    state.activeMonthKey = digests[0].monthKey;
    state.feedback = "Jumped to the latest published digest.";
    renderMonthStrip();
    renderCalendar();
    renderSelectedSummary();
    render();
  });

  elements.jumpDate.min = digests[digests.length - 1].dateValue;
  elements.jumpDate.max = digests[0].dateValue;
  elements.jumpDate.value = digests[0].dateValue;
  elements.jumpDate.addEventListener("change", function(event) {
    const value = event.target.value;
    if (!value) {
      return;
    }

    const exact = digestByDate.get(value);
    if (exact) {
      state.activeDigestId = exact.id;
      state.activeMonthKey = exact.monthKey;
      state.feedback = "Opened the digest published on " + exact.dateLong + ".";
    } else {
      const closest = findClosestDigest(value);
      state.activeDigestId = closest.id;
      state.activeMonthKey = closest.monthKey;
      state.feedback = "No digest exists on " + formatDateLong(value) + ". Showing the closest available date: " + closest.dateLong + ".";
      elements.jumpDate.value = closest.dateValue;
    }

    renderMonthStrip();
    renderCalendar();
    renderSelectedSummary();
    render();
  });

  elements.paperSearch.addEventListener("input", function(event) {
    state.query = event.target.value.trim();
    render();
  });

  elements.prevMonth.addEventListener("click", function() {
    moveMonth(1);
  });

  elements.nextMonth.addEventListener("click", function() {
    moveMonth(-1);
  });

  renderMonthStrip();
  renderCalendar();
  renderSelectedSummary();
  renderScopeButtons();
  render();

  const prefetchArchive = function() {
    ensureAllDigestsLoaded().then(function() {
      refreshArchiveMetric();
      if (state.searchScope === "all") {
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
