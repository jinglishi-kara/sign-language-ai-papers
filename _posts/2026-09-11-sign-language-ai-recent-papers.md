---
layout: post
title: "Sign Language & AI – Recent Papers (September 11, 2026)"
date: 2026-09-11 09:17:54 +0000
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
paper_count: 6
paper_catalog_json: >-
  [
    {
      "title": "Rethinking Sign Language Translation: The Impact of Signer Dependence on Model Evaluation",
      "authors": [
        "Keren Artiaga",
        "Sabyasachi Kamila",
        "Haithem Afli",
        "Conor Lynch",
        "Mohammed Hasanuzzaman"
      ],
      "published": "2026-09-07",
      "tags": [
        "ASL",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2609.07965v1",
      "source_site": "EMNLP",
      "task_category": "Sign Language Translation",
      "short_summary": "Sign Language Translation has advanced with deep learning, yet evaluations remain largely signer-dependent, with overlapping signers across train/dev/test. This raises concerns about whether models truly generalise or instead rely on signer-specific regularities. We conduct signer-fold cross-validation on GFSLT-VLP, GASLT, and SignCL, three leading, publicly available, gloss-free SLT models, on CSL-Daily and PHOENIX14T. Under signer-independent evaluation, performance drops sharply: on…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "RAIDAL: Redundancy-Aware Information Density Active Learning for CTC-Based Continuous Sign Language Recognition",
      "authors": [
        "Rafael A. Diniz Augusto",
        "Gabriel L. Oliveira",
        "Erickson R. Nascimento"
      ],
      "published": "2026-09-06",
      "tags": [
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2609.06843v2",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Continuous sign language recognition (CSLR) is a key technology for accessibility, yet its development remains limited by the high cost of annotating continuous video streams. Active learning offers a path toward mitigating this cost, but standard acquisition functions are not designed for weakly aligned sign language videos, where sign executions are interleaved with rest poses, irregular pauses, sign-like motion, and temporally redundant frames. This temporal redundancy can undermine sample…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval",
      "authors": [
        "Santiago Poveda-Gutiérrez",
        "Hideki Nakayama",
        "Mayumi Bono"
      ],
      "published": "2026-09-03",
      "tags": [
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2609.03788v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Isolated Sign Language Recognition (ISLR) is conventionally cast as closed-set classification over gloss labels, which cannot generalize to signs unseen in training and ties every deployment to a gloss-annotated lexicon. We instead recognize signs extracted from continuous signing by (1) captioning a sign-level clip into a free-form procedural description of the articulation with an open-weight vision-language model, and (2) retrieving the closest entry from a vocabulary of target descriptions…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "Beyond BLEU: A Case for Redefining Sign Language Translation Benchmarks",
      "authors": [
        "Oline Ranum",
        "Edward Fish",
        "Simon Hadfield",
        "Richard Bowden"
      ],
      "published": "2026-09-03",
      "tags": [
        "translation"
      ],
      "url": "http://arxiv.org/abs/2609.03734v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "BLEU-4 is the standard metric for evaluating sign language translation (SLT), but spoken-language metrics may not adequately reflect sign language proficiency. The multimodal, low-resource context of SLT allows models to exploit spurious correlations and spoken-language priors, rather than learning stronger sign representations. In this paper, we evaluate the relationship between spatio-temporal understanding and BLEU-4 across six SLT models on Phoenix-2014T and CSL-Daily, showing that gains in…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "SMART: MLLM-guided Temporal Alignment for Unifying Sign Language Recognition and Spotting",
      "authors": [
        "Eunjee Choi",
        "JungHoon Sung",
        "Seongwhan Cho",
        "Chu Xin",
        "Younggeun Choi"
      ],
      "published": "2026-08-26",
      "tags": [
        "neural-network",
        "pose-estimation",
        "recognition",
        "transformer"
      ],
      "url": "http://arxiv.org/abs/2608.25493v2",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Continuous sign language recognition (CSLR) aims to recognize gloss sequences from unsegmented sign videos under weak sequence-level supervision. However, existing methods rely on sentence-level gloss annotations, providing limited temporal and semantic guidance for fine-grained representation learning. Conventional video-text alignment also requires large batch sizes, making it inefficient for memory-intensive sign language video training. In this work, we propose SMART, an MLLM-guided…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "Cross-Sign Language Transfer Learning Using Domain Adaptation with Multi-scale Temporal Alignment",
      "authors": [
        "Keren Artiaga",
        "Yang Li",
        "Ercan Engin Kuruoglu",
        "Wai Kin",
        " Chan"
      ],
      "published": "2026-08-17",
      "tags": [
        "ASL",
        "neural-network",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2608.16804v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign language serves as a vital means of communication for individuals with hearing impairments, yet recognition resources for the over 100 distinct sign languages are severely lacking. In response, we present our work on sign language recognition using transfer learning and the domain adaptation method TA3N, which utilizes the Temporal Relational Network (TRN) module for aligning multi-scale temporal relations. Our findings highlight the superior performance of Domain Adaptation to neural…",
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

*Generated on September 11, 2026 at 09:17 UTC with 6 papers.*

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
    <tr><td>EMNLP</td><td>1</td></tr>
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
    <tr><td>Sign Language Translation</td><td>2</td></tr>
    <tr><td>Sign Language Production</td><td>0</td></tr>
    <tr><td>Other Sign Language Topic</td><td>0</td></tr>
    <tr><td>Co-speech Gesture Generation</td><td>0</td></tr>
    <tr><td>Gesture Recognition</td><td>0</td></tr>
  </tbody>
</table>


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (4)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (2)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production" disabled aria-disabled='true'>Sign Language Production (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic" disabled aria-disabled='true'>Other Sign Language Topic (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (5)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr" disabled aria-disabled='true'>ICLR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl" disabled aria-disabled='true'>ACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp">EMNLP (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr" disabled aria-disabled='true'>CVPR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
<article class="paper-card" data-source="emnlp" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">EMNLP</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>Rethinking Sign Language Translation: The Impact of Signer Dependence on Model Evaluation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Keren Artiaga, Sabyasachi Kamila, Haithem Afli, Conor Lynch, Mohammed Hasanuzzaman</p>
  <p class="paper-published"><strong>Published:</strong> 2026-09-07</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2609.07965v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign Language Translation has advanced with deep learning, yet evaluations remain largely signer-dependent, with overlapping signers across train/dev/test. This raises concerns about whether models truly generalise or instead rely on signer-specific regularities. We conduct signer-fold cross-validation on GFSLT-VLP, GASLT, and SignCL, three leading, publicly available, gloss-free SLT models, on CSL-Daily and PHOENIX14T. Under signer-independent evaluation, performance drops sharply: on…
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
  <h3>RAIDAL: Redundancy-Aware Information Density Active Learning for CTC-Based Continuous Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Rafael A. Diniz Augusto, Gabriel L. Oliveira, Erickson R. Nascimento</p>
  <p class="paper-published"><strong>Published:</strong> 2026-09-06</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2609.06843v2" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Continuous sign language recognition (CSLR) is a key technology for accessibility, yet its development remains limited by the high cost of annotating continuous video streams. Active learning offers a path toward mitigating this cost, but standard acquisition functions are not designed for weakly aligned sign language videos, where sign executions are interleaved with rest poses, irregular pauses, sign-like motion, and temporally redundant frames. This temporal redundancy can undermine sample…
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
  <h3>A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval</h3>
  <p class="paper-authors"><strong>Authors:</strong> Santiago Poveda-Gutiérrez, Hideki Nakayama, Mayumi Bono</p>
  <p class="paper-published"><strong>Published:</strong> 2026-09-03</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2609.03788v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Isolated Sign Language Recognition (ISLR) is conventionally cast as closed-set classification over gloss labels, which cannot generalize to signs unseen in training and ties every deployment to a gloss-annotated lexicon. We instead recognize signs extracted from continuous signing by (1) captioning a sign-level clip into a free-form procedural description of the articulation with an open-weight vision-language model, and (2) retrieving the closest entry from a vocabulary of target descriptions…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>Beyond BLEU: A Case for Redefining Sign Language Translation Benchmarks</h3>
  <p class="paper-authors"><strong>Authors:</strong> Oline Ranum, Edward Fish, Simon Hadfield, Richard Bowden</p>
  <p class="paper-published"><strong>Published:</strong> 2026-09-03</p>
  <p class="paper-tags"><strong>Tags:</strong> translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2609.03734v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> BLEU-4 is the standard metric for evaluating sign language translation (SLT), but spoken-language metrics may not adequately reflect sign language proficiency. The multimodal, low-resource context of SLT allows models to exploit spurious correlations and spoken-language priors, rather than learning stronger sign representations. In this paper, we evaluate the relationship between spatio-temporal understanding and BLEU-4 across six SLT models on Phoenix-2014T and CSL-Daily, showing that gains in…
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
  <h3>SMART: MLLM-guided Temporal Alignment for Unifying Sign Language Recognition and Spotting</h3>
  <p class="paper-authors"><strong>Authors:</strong> Eunjee Choi, JungHoon Sung, Seongwhan Cho, Chu Xin, Younggeun Choi</p>
  <p class="paper-published"><strong>Published:</strong> 2026-08-26</p>
  <p class="paper-tags"><strong>Tags:</strong> neural-network, pose-estimation, recognition, transformer</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2608.25493v2" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Continuous sign language recognition (CSLR) aims to recognize gloss sequences from unsegmented sign videos under weak sequence-level supervision. However, existing methods rely on sentence-level gloss annotations, providing limited temporal and semantic guidance for fine-grained representation learning. Conventional video-text alignment also requires large batch sizes, making it inefficient for memory-intensive sign language video training. In this work, we propose SMART, an MLLM-guided…
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
  <h3>Cross-Sign Language Transfer Learning Using Domain Adaptation with Multi-scale Temporal Alignment</h3>
  <p class="paper-authors"><strong>Authors:</strong> Keren Artiaga, Yang Li, Ercan Engin Kuruoglu, Wai Kin,  Chan</p>
  <p class="paper-published"><strong>Published:</strong> 2026-08-17</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, neural-network, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2608.16804v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language serves as a vital means of communication for individuals with hearing impairments, yet recognition resources for the over 100 distinct sign languages are severely lacking. In response, we present our work on sign language recognition using transfer learning and the domain adaptation method TA3N, which utilizes the Temporal Relational Network (TRN) module for aligning multi-scale temporal relations. Our findings highlight the superior performance of Domain Adaptation to neural…
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
