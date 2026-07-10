---
layout: post
title: "Sign Language & AI – Recent Papers (July 10, 2026)"
date: 2026-07-10 08:16:27 +0000
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
paper_count: 5
paper_catalog_json: >-
  [
    {
      "title": "ViPo-MLLM: Visual-Pose Multimodal LLM for Gloss-Free Sign Language Translation",
      "authors": [
        "Ahmed Abul Hasanaath",
        "Bicheng Xu",
        "Mir Rayat Imtiaz Hossain",
        "Leonid Sigal",
        "Hamzah Luqman"
      ],
      "published": "2026-07-04",
      "tags": [
        "pose-estimation",
        "recognition",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2607.03657v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Gloss-free Sign Language Translation (SLT) translates sign language videos into spoken-language sentences without gloss annotations, avoiding costly labeling but requiring fine-grained modeling of hands, body, and facial cues. Existing methods often use single-modality or weakly fused features, limiting performance. We propose ViPo-MLLM, a framework that integrates spatio-temporal RGB and human pose features. Dedicated encoders model intra-modal dynamics and cross-modal attention captures long-…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Phonological Perception of Sign Language Models",
      "authors": [
        "Kayo Yin",
        "Jessica Carter",
        "Alex Xijie Lu",
        "Annemarie Kocab"
      ],
      "published": "2026-06-27",
      "tags": [
        "ASL",
        "pose-estimation",
        "recognition",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2606.28667v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign languages are compositional systems where meaning arises by combining sublexical phonological parameters, such as handshape, location, and movement. While deep learning models for Sign Language Recognition (SLR) have achieved increased performance on translation benchmarks, it remains unclear whether these models distinguish abstract phonological features or merely rely on low-level statistical correlations. This work evaluates the phonological perception of SLR models trained on American…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "SIGNET: Motion-Level Knowledge Transfer for Cross-Language Sign Language Translation",
      "authors": [
        "Sobhan Asasi",
        "Ozge Mercanoglu Sincan",
        "Richard Bowden"
      ],
      "published": "2026-06-26",
      "tags": [
        "ASL",
        "neural-network",
        "recognition",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2606.28626v1",
      "source_site": "ECCV",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign language translation (SLT) remains challenging due to its high spatio-temporal complexity, long sequences, and the need to model multiple articulators without relying on gloss annotations. Existing approaches are typically tailored to individual datasets or languages and struggle to scale, while overlooking the relationships between sign languages that could inform more effective cross-lingual transfer. We present \\textbf{SIGNET}, a framework that enables motion-level knowledge transfer…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Deep Learning-Based Sign Language Recognition from Videos and Cross-Lingual Translation to Indian Vernaculars",
      "authors": [
        "Ramesh Nandipalli",
        "Chandranath Adak"
      ],
      "published": "2026-06-21",
      "tags": [
        "recognition",
        "transformer",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2606.22494v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign language is a primary mode of communication for the global deaf and hard-of-hearing community, yet automated tools that recognize sign gestures from video and translate them into natural language text remain limited, particularly for low-resource Indian languages. We present a two-stage deep learning pipeline that (i) classifies short sign language video clips into English word labels using a fine-tuned VideoMAE video transformer, and (ii) translates the predicted English label into Hindi,…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Corpus Augmentation for Sign Language Translation via LLM-Guided Video Stitching",
      "authors": [
        "Zsolt Robotka",
        "Ádám Rák",
        "Jalal Al-Afandi",
        "András Horváth",
        "György Cserey"
      ],
      "published": "2026-06-10",
      "tags": [
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2606.11925v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "Sign language translation (SLT) converts sign language video into spoken language text and holds significant promise for improving accessibility and enabling communication between signing and non-signing communities. While large weakly-aligned datasets have enabled pre-training at scale and gloss-free methods have reduced reliance on expert annotation, high-quality parallel sign video-text pairs for fine-tuning remain scarce, limiting generalisation on long-tail vocabulary and unseen…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
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

*Generated on July 10, 2026 at 08:16 UTC with 5 papers.*

### Source snapshot
<table class="snapshot-table">
  <thead>
    <tr><th>Source</th><th>Papers</th></tr>
  </thead>
  <tbody>
    <tr><td>arXiv</td><td>4</td></tr>
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
    <tr><td>ECCV</td><td>1</td></tr>
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

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (4)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (1)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production" disabled aria-disabled='true'>Sign Language Production (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic" disabled aria-disabled='true'>Other Sign Language Topic (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (4)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr" disabled aria-disabled='true'>ICLR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl" disabled aria-disabled='true'>ACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp" disabled aria-disabled='true'>EMNLP (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr" disabled aria-disabled='true'>CVPR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv">ECCV (1)</button></div></div>
<div class="paper-grid" id="paper-grid">
<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>ViPo-MLLM: Visual-Pose Multimodal LLM for Gloss-Free Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Ahmed Abul Hasanaath, Bicheng Xu, Mir Rayat Imtiaz Hossain, Leonid Sigal, Hamzah Luqman</p>
  <p class="paper-published"><strong>Published:</strong> 2026-07-04</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2607.03657v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Gloss-free Sign Language Translation (SLT) translates sign language videos into spoken-language sentences without gloss annotations, avoiding costly labeling but requiring fine-grained modeling of hands, body, and facial cues. Existing methods often use single-modality or weakly fused features, limiting performance. We propose ViPo-MLLM, a framework that integrates spatio-temporal RGB and human pose features. Dedicated encoders model intra-modal dynamics and cross-modal attention captures long-…
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
  <h3>Phonological Perception of Sign Language Models</h3>
  <p class="paper-authors"><strong>Authors:</strong> Kayo Yin, Jessica Carter, Alex Xijie Lu, Annemarie Kocab</p>
  <p class="paper-published"><strong>Published:</strong> 2026-06-27</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2606.28667v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign languages are compositional systems where meaning arises by combining sublexical phonological parameters, such as handshape, location, and movement. While deep learning models for Sign Language Recognition (SLR) have achieved increased performance on translation benchmarks, it remains unclear whether these models distinguish abstract phonological features or merely rely on low-level statistical correlations. This work evaluates the phonological perception of SLR models trained on American…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
  </div>
</article>

<article class="paper-card" data-source="eccv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">ECCV</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>SIGNET: Motion-Level Knowledge Transfer for Cross-Language Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Sobhan Asasi, Ozge Mercanoglu Sincan, Richard Bowden</p>
  <p class="paper-published"><strong>Published:</strong> 2026-06-26</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, neural-network, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2606.28626v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language translation (SLT) remains challenging due to its high spatio-temporal complexity, long sequences, and the need to model multiple articulators without relying on gloss annotations. Existing approaches are typically tailored to individual datasets or languages and struggle to scale, while overlooking the relationships between sign languages that could inform more effective cross-lingual transfer. We present \textbf{SIGNET}, a framework that enables motion-level knowledge transfer…
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
  <h3>Deep Learning-Based Sign Language Recognition from Videos and Cross-Lingual Translation to Indian Vernaculars</h3>
  <p class="paper-authors"><strong>Authors:</strong> Ramesh Nandipalli, Chandranath Adak</p>
  <p class="paper-published"><strong>Published:</strong> 2026-06-21</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition, transformer, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2606.22494v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language is a primary mode of communication for the global deaf and hard-of-hearing community, yet automated tools that recognize sign gestures from video and translate them into natural language text remain limited, particularly for low-resource Indian languages. We present a two-stage deep learning pipeline that (i) classifies short sign language video clips into English word labels using a fine-tuned VideoMAE video transformer, and (ii) translates the predicted English label into Hindi,…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>Corpus Augmentation for Sign Language Translation via LLM-Guided Video Stitching</h3>
  <p class="paper-authors"><strong>Authors:</strong> Zsolt Robotka, Ádám Rák, Jalal Al-Afandi, András Horváth, György Cserey</p>
  <p class="paper-published"><strong>Published:</strong> 2026-06-10</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2606.11925v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language translation (SLT) converts sign language video into spoken language text and holds significant promise for improving accessibility and enabling communication between signing and non-signing communities. While large weakly-aligned datasets have enabled pre-training at scale and gloss-free methods have reduced reliance on expert annotation, high-quality parallel sign video-text pairs for fine-tuning remain scarce, limiting generalisation on long-tail vocabulary and unseen…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
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
