---
layout: post
title: "Sign Language & AI – Recent Papers (April 10, 2026)"
date: 2026-04-10 06:50:48 +0000
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
paper_count: 5
paper_catalog_json: >-
  [
    {
      "title": "SyriSign: A Parallel Corpus for Arabic Text to Syrian Arabic Sign Language Translation",
      "authors": [
        "Mohammad Amer Khalil",
        "Raghad Nahas",
        "Ahmad Nassar",
        "Khloud Al Jallad"
      ],
      "published": "2026-03-31",
      "tags": [
        "translation"
      ],
      "url": "http://arxiv.org/abs/2603.29219v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "Sign language is the primary approach of communication for the Deaf and Hard-of-Hearing (DHH) community. While there are numerous benchmarks for high-resource sign languages, low-resource languages like Arabic remain underrepresented. Currently, there is no publicly available dataset for Syrian Arabic Sign Language (SyArSL). To overcome this gap, we introduce SyriSign, a dataset comprising 1500 video samples across 150 unique lexical signs, designed for text-to-SyArSL translation tasks. This…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "LA-Sign: Looped Transformers with Geometry-aware Alignment for Skeleton-based Sign Language Recognition",
      "authors": [
        "Muxin Pu",
        "Mei Kuan Lim",
        "Chun Yong Chong",
        "Chen Change Loy"
      ],
      "published": "2026-03-30",
      "tags": [
        "ASL",
        "pose-estimation",
        "recognition",
        "transformer"
      ],
      "url": "http://arxiv.org/abs/2603.29057v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Skeleton-based isolated sign language recognition (ISLR) demands fine-grained understanding of articulated motion across multiple spatial scales, from subtle finger movements to global body dynamics. Existing approaches typically rely on deep feed-forward architectures, which increase model capacity but lack mechanisms for recurrent refinement and structured representation. We propose LA-Sign, a looped transformer framework with geometry-aware alignment for ISLR. Instead of stacking deeper…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "Development of ML model for triboelectric nanogenerator based sign language detection system",
      "authors": [
        "Meshv Patel",
        "Bikash Baro",
        "Sayan Bayan",
        "Mohendra Roy"
      ],
      "published": "2026-03-26",
      "tags": [
        "neural-network",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2604.06220v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign language recognition (SLR) is vital for bridging communication gaps between deaf and hearing communities. Vision-based approaches suffer from occlusion, computational costs, and physical constraints. This work presents a comparison of machine learning (ML) and deep learning models for a custom triboelectric nanogenerator (TENG)-based sensor glove. Utilizing multivariate time-series data from five flex sensors, the study benchmarks traditional ML algorithms, feedforward neural networks,…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "Recognising BSL Fingerspelling in Continuous Signing Sequences",
      "authors": [
        "Alyssa Chan",
        "Taein Kwon",
        "Andrew Zisserman"
      ],
      "published": "2026-03-19",
      "tags": [
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2603.19523v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Fingerspelling is a critical component of British Sign Language (BSL), used to spell proper names, technical terms, and words that lack established lexical signs. Fingerspelling recognition is challenging due to the rapid pace of signing and common letter omissions by native signers, while existing BSL fingerspelling datasets are either small in scale or temporally and letter-wise inaccurate. In this work, we introduce a new large-scale BSL fingerspelling dataset, FS23K, constructed using an…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "STARK: Spatio-Temporal Attention for Representation of Keypoints for Continuous Sign Language Recognition",
      "authors": [
        "Suvajit Patra",
        "Soumitra Samanta"
      ],
      "published": "2026-03-17",
      "tags": [
        "neural-network",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2603.16163v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Continuous Sign Language Recognition (CSLR) is a crucial task for understanding the languages of deaf communities. Contemporary keypoint-based approaches typically rely on spatio-temporal encoding, where spatial interactions among keypoints are modeled using Graph Convolutional Networks or attention mechanisms, while temporal dynamics are captured using 1D convolutional networks. However, such designs often introduce a large number of parameters in both the encoder and the decoder. This paper…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    }
  ]
---


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

This digest compiles recent arXiv publications on sign-language translation, recognition, and related gesture research. The content is structured to make it easy to browse by task or venue.

*Generated on April 10, 2026 at 06:50 UTC with 5 papers.*

### Source snapshot
<table class="snapshot-table">
  <thead>
    <tr><th>Source</th><th>Papers</th></tr>
  </thead>
  <tbody>
    <tr><td>arXiv</td><td>5</td></tr>
    <tr><td>NeurIPS</td><td>0</td></tr>
    <tr><td>ICML</td><td>0</td></tr>
    <tr><td>ICLR</td><td>0</td></tr>
    <tr><td>AAAI</td><td>0</td></tr>
    <tr><td>IJCAI</td><td>0</td></tr>
    <tr><td>ACL</td><td>0</td></tr>
    <tr><td>NAACL</td><td>0</td></tr>
    <tr><td>EMNLP</td><td>0</td></tr>
    <tr><td>COLING</td><td>0</td></tr>
    <tr><td>CVPR</td><td>0</td></tr>
    <tr><td>ICCV</td><td>0</td></tr>
    <tr><td>ECCV</td><td>0</td></tr>
  </tbody>
</table>


### Task spotlight
<table class="snapshot-table">
  <thead>
    <tr><th>Task</th><th>Papers</th></tr>
  </thead>
  <tbody>
    <tr><td>Sign Language Recognition</td><td>4</td></tr>
    <tr><td>Sign Language Translation</td><td>1</td></tr>
    <tr><td>Sign Language Production</td><td>0</td></tr>
    <tr><td>Other Sign Language Topic</td><td>0</td></tr>
    <tr><td>Co-speech Gesture Generation</td><td>0</td></tr>
    <tr><td>Gesture Recognition</td><td>0</td></tr>
  </tbody>
</table>


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (4)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (1)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production" disabled aria-disabled='true'>Sign Language Production (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic" disabled aria-disabled='true'>Other Sign Language Topic (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (5)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr" disabled aria-disabled='true'>ICLR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl" disabled aria-disabled='true'>ACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp" disabled aria-disabled='true'>EMNLP (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr" disabled aria-disabled='true'>CVPR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
<article class="paper-card" data-source="arxiv" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>SyriSign: A Parallel Corpus for Arabic Text to Syrian Arabic Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Mohammad Amer Khalil, Raghad Nahas, Ahmad Nassar, Khloud Al Jallad</p>
  <p class="paper-published"><strong>Published:</strong> 2026-03-31</p>
  <p class="paper-tags"><strong>Tags:</strong> translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2603.29219v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language is the primary approach of communication for the Deaf and Hard-of-Hearing (DHH) community. While there are numerous benchmarks for high-resource sign languages, low-resource languages like Arabic remain underrepresented. Currently, there is no publicly available dataset for Syrian Arabic Sign Language (SyArSL). To overcome this gap, we introduce SyriSign, a dataset comprising 1500 video samples across 150 unique lexical signs, designed for text-to-SyArSL translation tasks. This…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>LA-Sign: Looped Transformers with Geometry-aware Alignment for Skeleton-based Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Muxin Pu, Mei Kuan Lim, Chun Yong Chong, Chen Change Loy</p>
  <p class="paper-published"><strong>Published:</strong> 2026-03-30</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition, transformer</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2603.29057v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Skeleton-based isolated sign language recognition (ISLR) demands fine-grained understanding of articulated motion across multiple spatial scales, from subtle finger movements to global body dynamics. Existing approaches typically rely on deep feed-forward architectures, which increase model capacity but lack mechanisms for recurrent refinement and structured representation. We propose LA-Sign, a looped transformer framework with geometry-aware alignment for ISLR. Instead of stacking deeper…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>Development of ML model for triboelectric nanogenerator based sign language detection system</h3>
  <p class="paper-authors"><strong>Authors:</strong> Meshv Patel, Bikash Baro, Sayan Bayan, Mohendra Roy</p>
  <p class="paper-published"><strong>Published:</strong> 2026-03-26</p>
  <p class="paper-tags"><strong>Tags:</strong> neural-network, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.06220v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language recognition (SLR) is vital for bridging communication gaps between deaf and hearing communities. Vision-based approaches suffer from occlusion, computational costs, and physical constraints. This work presents a comparison of machine learning (ML) and deep learning models for a custom triboelectric nanogenerator (TENG)-based sensor glove. Utilizing multivariate time-series data from five flex sensors, the study benchmarks traditional ML algorithms, feedforward neural networks,…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>Recognising BSL Fingerspelling in Continuous Signing Sequences</h3>
  <p class="paper-authors"><strong>Authors:</strong> Alyssa Chan, Taein Kwon, Andrew Zisserman</p>
  <p class="paper-published"><strong>Published:</strong> 2026-03-19</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2603.19523v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Fingerspelling is a critical component of British Sign Language (BSL), used to spell proper names, technical terms, and words that lack established lexical signs. Fingerspelling recognition is challenging due to the rapid pace of signing and common letter omissions by native signers, while existing BSL fingerspelling datasets are either small in scale or temporally and letter-wise inaccurate. In this work, we introduce a new large-scale BSL fingerspelling dataset, FS23K, constructed using an…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>STARK: Spatio-Temporal Attention for Representation of Keypoints for Continuous Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Suvajit Patra, Soumitra Samanta</p>
  <p class="paper-published"><strong>Published:</strong> 2026-03-17</p>
  <p class="paper-tags"><strong>Tags:</strong> neural-network, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2603.16163v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Continuous Sign Language Recognition (CSLR) is a crucial task for understanding the languages of deaf communities. Contemporary keypoint-based approaches typically rely on spatio-temporal encoding, where spatial interactions among keypoints are modeled using Graph Convolutional Networks or attention mechanisms, while temporal dynamics are captured using 1D convolutional networks. However, such designs often introduce a large number of parameters in both the encoder and the decoder. This paper…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>
</div>

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
