---
layout: post
title: "Sign Language & AI – Recent Papers (June 14, 2026)"
date: 2026-06-14 08:37:52 +0000
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
paper_count: 5
paper_catalog_json: >-
  [
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
    },
    {
      "title": "What's the Point? Spatial Grammar & Index Resolution for Sign Language Processing",
      "authors": [
        "Oline Ranum",
        "Simon Hadfield",
        "Richard Bowden"
      ],
      "published": "2026-06-06",
      "tags": [
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2606.08056v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign language models are predominantly trained with gloss-sequence or text supervision, thereby under-modeling non-lexical and productive constructions. One comparatively tractable instance is spatial indexing: pointing gestures that assign discourse entities to spatial loci for subsequent co-reference, which lexicon-centric objectives largely fail to capture. We present a targeted evaluation of indexing in Sign Language Recognition, showing that despite comprising 10-15% of signing content,…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "SLU-2K: A Question-Based Benchmark for Semantic Evaluation of Sign Language Translation",
      "authors": [
        "Zeno Testa",
        "Antonino Furnari",
        "Lorenzo Baraldi",
        "Natalia Díaz-Rodríguez"
      ],
      "published": "2026-06-02",
      "tags": [
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2606.03788v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "Sign Language Translation (SLT) is typically evaluated with surface-form metrics such as BLEU and ROUGE, which reward lexical overlap but do not directly measure whether a translation preserves the meaning of the source sign sequence. This is in contrast with the final objective of integrating SLT in assistive technology. In this work, we shift the focus from Sign Language Translation (SLT) to Sign Language Understanding (SLU), with particular emphasis on semantic understanding. Specifically,…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Target-Side Paraphrase Augmentation for Sign Language Translation with Large Language Models",
      "authors": [
        "Pedro Dal Bianco",
        "Jean Paul Nunes Reinhold",
        "Oscar Stanchi",
        "Facundo Quiroga",
        "Franco Ronchetti",
        "Ulisses Brisolara Corrêa"
      ],
      "published": "2026-05-29",
      "tags": [
        "pose-estimation",
        "transformer",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2605.31393v1",
      "source_site": "CVPR",
      "task_category": "Sign Language Translation",
      "short_summary": "Sign language translation (SLT) remains constrained by limited paired sign-video/text corpora and heavy-tailed target vocabularies. We study target-side augmentation in which GPT-4o generates controlled paraphrase variants of reference sentences while the sign input remains unchanged. A Signformer-style pose-based Transformer is trained under a two-stage schedule: pre-training on the augmented corpus followed by fine-tuning on the original references. We evaluate on three datasets spanning…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Direct Translation between Sign Languages",
      "authors": [
        "Zetian Wu",
        "Bowen Xie",
        "Wuyang Meng",
        "Milan Gautam",
        "Stefan Lee",
        "Liang Huang"
      ],
      "published": "2026-05-20",
      "tags": [
        "ASL",
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2605.20588v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "The field of sign language translation has witnessed significant progress in the translation between sign and spoken languages, but the translation between sign languages remains largely unexplored and out of reach. The latter can help 1.5 billion deaf and hard-of-hearing (DHH) people worldwide communicate across language barriers without relying on hearing interpreters or written-language fluency. The cascade approach composing separate sign-to-text, text-to-text, and text-to-sign systems…",
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

*Generated on June 14, 2026 at 08:37 UTC with 5 papers.*

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
    <tr><td>CVPR</td><td>1</td></tr>
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
    <tr><td>Sign Language Recognition</td><td>1</td></tr>
    <tr><td>Sign Language Translation</td><td>4</td></tr>
    <tr><td>Sign Language Production</td><td>0</td></tr>
    <tr><td>Other Sign Language Topic</td><td>0</td></tr>
    <tr><td>Co-speech Gesture Generation</td><td>0</td></tr>
    <tr><td>Gesture Recognition</td><td>0</td></tr>
  </tbody>
</table>


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (1)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (4)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production" disabled aria-disabled='true'>Sign Language Production (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic" disabled aria-disabled='true'>Other Sign Language Topic (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (4)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr" disabled aria-disabled='true'>ICLR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl" disabled aria-disabled='true'>ACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp" disabled aria-disabled='true'>EMNLP (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr">CVPR (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
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

<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>What's the Point? Spatial Grammar & Index Resolution for Sign Language Processing</h3>
  <p class="paper-authors"><strong>Authors:</strong> Oline Ranum, Simon Hadfield, Richard Bowden</p>
  <p class="paper-published"><strong>Published:</strong> 2026-06-06</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2606.08056v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language models are predominantly trained with gloss-sequence or text supervision, thereby under-modeling non-lexical and productive constructions. One comparatively tractable instance is spatial indexing: pointing gestures that assign discourse entities to spatial loci for subsequent co-reference, which lexicon-centric objectives largely fail to capture. We present a targeted evaluation of indexing in Sign Language Recognition, showing that despite comprising 10-15% of signing content,…
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
  <h3>SLU-2K: A Question-Based Benchmark for Semantic Evaluation of Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Zeno Testa, Antonino Furnari, Lorenzo Baraldi, Natalia Díaz-Rodríguez</p>
  <p class="paper-published"><strong>Published:</strong> 2026-06-02</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2606.03788v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign Language Translation (SLT) is typically evaluated with surface-form metrics such as BLEU and ROUGE, which reward lexical overlap but do not directly measure whether a translation preserves the meaning of the source sign sequence. This is in contrast with the final objective of integrating SLT in assistive technology. In this work, we shift the focus from Sign Language Translation (SLT) to Sign Language Understanding (SLU), with particular emphasis on semantic understanding. Specifically,…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
  </div>
</article>

<article class="paper-card" data-source="cvpr" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">CVPR</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>Target-Side Paraphrase Augmentation for Sign Language Translation with Large Language Models</h3>
  <p class="paper-authors"><strong>Authors:</strong> Pedro Dal Bianco, Jean Paul Nunes Reinhold, Oscar Stanchi, Facundo Quiroga, Franco Ronchetti, Ulisses Brisolara Corrêa</p>
  <p class="paper-published"><strong>Published:</strong> 2026-05-29</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, transformer, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2605.31393v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language translation (SLT) remains constrained by limited paired sign-video/text corpora and heavy-tailed target vocabularies. We study target-side augmentation in which GPT-4o generates controlled paraphrase variants of reference sentences while the sign input remains unchanged. A Signformer-style pose-based Transformer is trained under a two-stage schedule: pre-training on the augmented corpus followed by fine-tuning on the original references. We evaluate on three datasets spanning…
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
  <h3>Direct Translation between Sign Languages</h3>
  <p class="paper-authors"><strong>Authors:</strong> Zetian Wu, Bowen Xie, Wuyang Meng, Milan Gautam, Stefan Lee, Liang Huang</p>
  <p class="paper-published"><strong>Published:</strong> 2026-05-20</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2605.20588v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> The field of sign language translation has witnessed significant progress in the translation between sign and spoken languages, but the translation between sign languages remains largely unexplored and out of reach. The latter can help 1.5 billion deaf and hard-of-hearing (DHH) people worldwide communicate across language barriers without relying on hearing interpreters or written-language fluency. The cascade approach composing separate sign-to-text, text-to-text, and text-to-sign systems…
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
