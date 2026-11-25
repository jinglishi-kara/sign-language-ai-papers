---
layout: post
title: "Sign Language & AI – Recent Papers (November 25, 2026)"
date: 2026-11-25 15:13:45 +0000
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
paper_count: 6
paper_catalog_json: >-
  [
    {
      "title": "BCP: A Lightweight Boundary-Controlled Framework for Online Sign Language Recognition and Translation",
      "authors": [
        "Xiao Ma",
        "Lin Li",
        "Shiqing Wu",
        "Wang Gao",
        "Chuanbo Liu",
        "Jianquan Liu"
      ],
      "published": "2026-11-24",
      "tags": [
        "pose-estimation",
        "recognition",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2611.32471v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Online sign language recognition (SLR) and translation (SLT) incrementally produce gloss sequences or natural language text from sign video as it arrives, a capability essential for real-time communication and live captioning. However, powerful pretrained offline models cannot be directly deployed in this setting, while existing online methods typically retrain the entire model on simulated streaming prefixes constructed from offline videos, incurring high costs. To address this challenge, we…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "MoGloss: Joint Motion and Pseudo-Gloss Pretraining for American Sign Language Understanding",
      "authors": [
        "Rui Hong",
        "Jana Košecká"
      ],
      "published": "2026-11-19",
      "tags": [
        "ASL",
        "pose-estimation",
        "recognition",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2611.25333v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign language translation and recognition have been shown to benefit from various pretraining approaches. We propose a novel two-stage pretraining approach for the motion encoder, which first learns to reconstruct masked motion, followed by joint masked prediction of pseudo-gloss units and motion. Pseudo-glosses serve as an intermediate structured representation of natural language text and are obtained from the captions by a large language model. We curate a corpus of about 1,100 hours of…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "IsharaBART: An efficient BART-Based Framework for Low-Resource Bangla Sign Language Translation",
      "authors": [
        "Aonmoy Das",
        "Ananna Dev Aishi",
        "Md. Fazlul Kader"
      ],
      "published": "2026-11-12",
      "tags": [
        "transformer",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2611.16359v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "Millions of Bangla Sign Language (BdSL) users lack reliable automatic translation tools. Existing systems are limited by data scarcity, unidirectional design, and computationally expensive architectures that are not suitable for low-resource deployment. We introduce IsharaBART, a bidirectional generative framework for gloss-sentence translation in BdSL. IsharaBART uses Bidirectional and Auto-Regressive Transformers (BART)-based conditional language modeling with denoising learning objectives.…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Compact Quantum Channel Attention for Static ASL Recognition: A Controlled Study with Parameter-Matched Baselines",
      "authors": [
        "Ronak Bhalgami",
        "Deep Kothadiya",
        "Nikita Bhatt"
      ],
      "published": "2026-11-07",
      "tags": [
        "ASL",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2611.10544v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Hybrid quantum-classical models often report good accuracy on image tasks, but it is rarely clear whether the quantum part is responsible. This paper proposes QCA-DenseNet, a static American Sign Language (ASL) recognition pipeline in which an eight-qubit variational circuit acts as a channel-attention gate on DenseNet121 features. The quantum channel attention (QCA) gate has 17,464 parameters, 7.51 times fewer than a squeeze-and-excitation (SE) block. The pipeline is tested on 1,815 MU…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "Znaki: A Russian Fingerspelling Recognition Dataset",
      "authors": [
        "Petr Surovtsev",
        "Pavel Korotaev",
        "Alexander Nagaev",
        "Alexander Kapitanov"
      ],
      "published": "2026-11-02",
      "tags": [
        "ASL",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2611.03136v1",
      "source_site": "ACL",
      "task_category": "Sign Language Recognition",
      "short_summary": "Fingerspelling - the sequential signing of letters that compose proper names, technical terms, and out-of-vocabulary words - is an integral component of any sign language. Despite Russian Sign Language (RSL) being used by more than 150,000 native signers, no public fingerspelling dataset for RSL exists, in contrast to American, British, German, and several other sign languages. We introduce Znaki the first open RSL fingerspelling dataset: 37,252 video recordings (35.4 hours) of 1,593 unique…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "BEACON: Distilled Begin/End-Aware Structured Decoding for Continuous Sign Language Segmentation",
      "authors": [
        "Guohou Zhang",
        "Kalin Stefanov"
      ],
      "published": "2026-10-29",
      "tags": [
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2610.39553v2",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "In segmentation-based continuous sign language recognition, an untrimmed video is first partitioned into lexical units; segmentation is therefore a means to an end---downstream recognition. However, segmenters are usually judged by local boundary detection rather than by the quality of the lexical segments and the recognition they enable. We present BEACON, a begin/end-aware segmenter that combines four-class Outside/Begin/Inside/End (BIOE) labeling, constrained Viterbi decoding over eight…",
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

*Generated on November 25, 2026 at 15:13 UTC with 6 papers.*

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
    <tr><td>ACL</td><td>1</td></tr>
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
    <tr><td>Sign Language Recognition</td><td>5</td></tr>
    <tr><td>Sign Language Translation</td><td>1</td></tr>
    <tr><td>Sign Language Production</td><td>0</td></tr>
    <tr><td>Other Sign Language Topic</td><td>0</td></tr>
    <tr><td>Co-speech Gesture Generation</td><td>0</td></tr>
    <tr><td>Gesture Recognition</td><td>0</td></tr>
  </tbody>
</table>


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (5)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (1)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production" disabled aria-disabled='true'>Sign Language Production (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic" disabled aria-disabled='true'>Other Sign Language Topic (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (5)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr" disabled aria-disabled='true'>ICLR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl">ACL (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp" disabled aria-disabled='true'>EMNLP (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr" disabled aria-disabled='true'>CVPR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>BCP: A Lightweight Boundary-Controlled Framework for Online Sign Language Recognition and Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Xiao Ma, Lin Li, Shiqing Wu, Wang Gao, Chuanbo Liu, Jianquan Liu</p>
  <p class="paper-published"><strong>Published:</strong> 2026-11-24</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2611.32471v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Online sign language recognition (SLR) and translation (SLT) incrementally produce gloss sequences or natural language text from sign video as it arrives, a capability essential for real-time communication and live captioning. However, powerful pretrained offline models cannot be directly deployed in this setting, while existing online methods typically retrain the entire model on simulated streaming prefixes constructed from offline videos, incurring high costs. To address this challenge, we…
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
  <h3>MoGloss: Joint Motion and Pseudo-Gloss Pretraining for American Sign Language Understanding</h3>
  <p class="paper-authors"><strong>Authors:</strong> Rui Hong, Jana Košecká</p>
  <p class="paper-published"><strong>Published:</strong> 2026-11-19</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2611.25333v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language translation and recognition have been shown to benefit from various pretraining approaches. We propose a novel two-stage pretraining approach for the motion encoder, which first learns to reconstruct masked motion, followed by joint masked prediction of pseudo-gloss units and motion. Pseudo-glosses serve as an intermediate structured representation of natural language text and are obtained from the captions by a large language model. We curate a corpus of about 1,100 hours of…
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
  <h3>IsharaBART: An efficient BART-Based Framework for Low-Resource Bangla Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Aonmoy Das, Ananna Dev Aishi, Md. Fazlul Kader</p>
  <p class="paper-published"><strong>Published:</strong> 2026-11-12</p>
  <p class="paper-tags"><strong>Tags:</strong> transformer, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2611.16359v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Millions of Bangla Sign Language (BdSL) users lack reliable automatic translation tools. Existing systems are limited by data scarcity, unidirectional design, and computationally expensive architectures that are not suitable for low-resource deployment. We introduce IsharaBART, a bidirectional generative framework for gloss-sentence translation in BdSL. IsharaBART uses Bidirectional and Auto-Regressive Transformers (BART)-based conditional language modeling with denoising learning objectives.…
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
  <h3>Compact Quantum Channel Attention for Static ASL Recognition: A Controlled Study with Parameter-Matched Baselines</h3>
  <p class="paper-authors"><strong>Authors:</strong> Ronak Bhalgami, Deep Kothadiya, Nikita Bhatt</p>
  <p class="paper-published"><strong>Published:</strong> 2026-11-07</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2611.10544v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Hybrid quantum-classical models often report good accuracy on image tasks, but it is rarely clear whether the quantum part is responsible. This paper proposes QCA-DenseNet, a static American Sign Language (ASL) recognition pipeline in which an eight-qubit variational circuit acts as a channel-attention gate on DenseNet121 features. The quantum channel attention (QCA) gate has 17,464 parameters, 7.51 times fewer than a squeeze-and-excitation (SE) block. The pipeline is tested on 1,815 MU…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>

<article class="paper-card" data-source="acl" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">ACL</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>Znaki: A Russian Fingerspelling Recognition Dataset</h3>
  <p class="paper-authors"><strong>Authors:</strong> Petr Surovtsev, Pavel Korotaev, Alexander Nagaev, Alexander Kapitanov</p>
  <p class="paper-published"><strong>Published:</strong> 2026-11-02</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2611.03136v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Fingerspelling - the sequential signing of letters that compose proper names, technical terms, and out-of-vocabulary words - is an integral component of any sign language. Despite Russian Sign Language (RSL) being used by more than 150,000 native signers, no public fingerspelling dataset for RSL exists, in contrast to American, British, German, and several other sign languages. We introduce Znaki the first open RSL fingerspelling dataset: 37,252 video recordings (35.4 hours) of 1,593 unique…
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
  <h3>BEACON: Distilled Begin/End-Aware Structured Decoding for Continuous Sign Language Segmentation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Guohou Zhang, Kalin Stefanov</p>
  <p class="paper-published"><strong>Published:</strong> 2026-10-29</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2610.39553v2" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> In segmentation-based continuous sign language recognition, an untrimmed video is first partitioned into lexical units; segmentation is therefore a means to an end---downstream recognition. However, segmenters are usually judged by local boundary detection rather than by the quality of the lexical segments and the recognition they enable. We present BEACON, a begin/end-aware segmenter that combines four-class Outside/Begin/Inside/End (BIOE) labeling, constrained Viterbi decoding over eight…
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
