---
layout: post
title: "Sign Language & AI – Recent Papers (March 21, 2026)"
date: 2026-03-21 05:36:04 +0000
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
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

*Generated on March 21, 2026 at 05:36 UTC with 5 papers.*

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
    <tr><td>Sign Language Recognition</td><td>4</td></tr>
    <tr><td>Sign Language Translation</td><td>0</td></tr>
    <tr><td>Sign Language Production</td><td>1</td></tr>
    <tr><td>Other Sign Language Topic</td><td>0</td></tr>
    <tr><td>Co-speech Gesture Generation</td><td>0</td></tr>
    <tr><td>Gesture Recognition</td><td>0</td></tr>
  </tbody>
</table>


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (4)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation" disabled aria-disabled='true'>Sign Language Translation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production">Sign Language Production (1)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic" disabled aria-disabled='true'>Other Sign Language Topic (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (4)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr" disabled aria-disabled='true'>ICLR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl" disabled aria-disabled='true'>ACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp" disabled aria-disabled='true'>EMNLP (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr">CVPR (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
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

<article class="paper-card" data-source="arxiv" data-task="sign-language-production">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Production</span>
  </div>
  <h3>SignSparK: Efficient Multilingual Sign Language Production via Sparse Keyframe Learning</h3>
  <p class="paper-authors"><strong>Authors:</strong> Jianhe Low, Alexandre Symeonidis-Herzig, Maksym Ivashechkin, Ozge Mercanoglu Sincan, Richard Bowden</p>
  <p class="paper-published"><strong>Published:</strong> 2026-03-11</p>
  <p class="paper-tags"><strong>Tags:</strong> avatar, pose-estimation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2603.10446v2" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Generating natural and linguistically accurate sign language avatars remains a formidable challenge. Current Sign Language Production (SLP) frameworks face a stark trade-off: direct text-to-pose models suffer from regression-to-the-mean effects, while dictionary-retrieval methods produce robotic, disjointed transitions. To resolve this, we propose a novel training paradigm that leverages sparse keyframes to capture the true underlying kinematic distribution of human signing. By predicting dense…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper explores methods that can be applied to sign language and AI.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>Geometry-Aware Metric Learning for Cross-Lingual Few-Shot Sign Language Recognition on Static Hand Keypoints</h3>
  <p class="paper-authors"><strong>Authors:</strong> Chayanin Chamachot, Kanokphan Lertniponphan</p>
  <p class="paper-published"><strong>Published:</strong> 2026-03-10</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2603.09213v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language recognition (SLR) systems typically require large labeled corpora for each language, yet the majority of the world's 300+ sign languages lack sufficient annotated data. Cross-lingual few-shot transfer, pretraining on a data-rich source language and adapting with only a handful of target-language examples, offers a scalable alternative, but conventional coordinate-based keypoint representations are susceptible to domain shift arising from differences in camera viewpoint, hand…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
  </div>
</article>

<article class="paper-card" data-source="cvpr" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">CVPR</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>OpenFS: Multi-Hand-Capable Fingerspelling Recognition with Implicit Signing-Hand Detection and Frame-Wise Letter-Conditioned Synthesis</h3>
  <p class="paper-authors"><strong>Authors:</strong> Junuk Cha, Jihyeon Kim, Han-Mu Park</p>
  <p class="paper-published"><strong>Published:</strong> 2026-02-26</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2602.22949v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Fingerspelling is a component of sign languages in which words are spelled out letter by letter using specific hand poses. Automatic fingerspelling recognition plays a crucial role in bridging the communication gap between Deaf and hearing communities, yet it remains challenging due to the signing-hand ambiguity issue, the lack of appropriate training losses, and the out-of-vocabulary (OOV) problem. Prior fingerspelling recognition methods rely on explicit signing-hand detection, which often…
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
  <h3>SignVLA: A Gloss-Free Vision-Language-Action Framework for Real-Time Sign Language-Guided Robotic Manipulation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Xinyu Tan, Ningwei Bai, Harry Gardener, Zhengyang Zhong, Luoyu Zhang, Liuhaichen Yang, Zhekai Duan, Monkgogi Galeitsiwe, Zezhi Tang</p>
  <p class="paper-published"><strong>Published:</strong> 2026-02-26</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition, transformer</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2602.22514v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> We present, to our knowledge, the first sign language-driven Vision-Language-Action (VLA) framework for intuitive and inclusive human-robot interaction. Unlike conventional approaches that rely on gloss annotations as intermediate supervision, the proposed system adopts a gloss-free paradigm and directly maps visual sign gestures to semantic instructions. This design reduces annotation cost and avoids the information loss introduced by gloss representations, enabling more natural and scalable…
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
