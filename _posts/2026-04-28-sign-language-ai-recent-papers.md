---
layout: post
title: "Sign Language & AI – Recent Papers (April 28, 2026)"
date: 2026-04-28 07:28:15 +0000
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
paper_count: 11
paper_catalog_json: >-
  [
    {
      "title": "Evaluation of Pose Estimation Systems for Sign Language Translation",
      "authors": [
        "Catherine O'Brien",
        "Gerard Sant",
        "Mathias Müller",
        "Sarah Ebling"
      ],
      "published": "2026-04-27",
      "tags": [
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2604.24609v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "Many sign language translation (SLT) systems operate on pose sequences instead of raw video to reduce input dimensionality, improve portability, and partially anonymize signers. The choice of pose estimator is often treated as an implementation detail, with systems defaulting to widely available tools such as MediaPipe Holistic or OpenPose. We present a systematic comparison of pose estimators for pose-based SLT, covering widely used baselines (MediaPipe Holistic, OpenPose) and newer whole-…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Selective Contrastive Learning For Gloss Free Sign Language Translation",
      "authors": [
        "Changhao Lai",
        "Rui Zhao",
        "Xuewen Zhong",
        "Jinsong Su",
        "Yidong Chen"
      ],
      "published": "2026-04-24",
      "tags": [
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2604.22374v1",
      "source_site": "ACL",
      "task_category": "Sign Language Translation",
      "short_summary": "Sign language translation (SLT) converts continuous sign videos into spoken-language text, yet it remains challenging due to the intrinsic modality mismatch between visual signs and written text, particularly in gloss-free settings. Recent SLT systems increasingly adopt CLIP-like Vision-Language pretraining (VLP) for cross-modal alignment, but the random in-batch contrast provides few, batch-dependent negatives and may mislabel semantically similar (or even identical) pairs as negatives,…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "SignDATA: Data Pipeline for Sign Language Translation",
      "authors": [
        "Kuanwei Chen",
        "Tingyi Lin"
      ],
      "published": "2026-04-22",
      "tags": [
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2604.20357v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "Sign-language datasets are difficult to preprocess consistently because they vary in annotation schema, clip timing, signer framing, and privacy constraints. Existing work usually reports downstream models, while the preprocessing pipeline that converts raw video into training-ready pose or video artifacts remains fragmented, backend-specific, and weakly documented. We present SignDATA, a config-driven preprocessing toolkit that standardizes heterogeneous sign-language corpora into comparable…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "CanonSLR: Canonical-View Guided Multi-View Continuous Sign Language Recognition",
      "authors": [
        "Xu Wang",
        "Shengeng Tang",
        "Wan Jiang",
        "Yaxiong Wang",
        "Lechao Cheng",
        "Richang Hong"
      ],
      "published": "2026-04-20",
      "tags": [
        "neural-network",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2604.18184v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Continuous Sign Language Recognition (CSLR) has achieved remarkable progress in recent years; however, most existing methods are developed under single-view settings and thus remain insufficiently robust to viewpoint variations in real-world scenarios. To address this limitation, we propose CanonSLR, a canonical-view guided framework for multi-view CSLR. Specifically, we introduce a frontal-view-anchored teacher-student learning strategy, in which a teacher network trained on frontal-view data…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "SignDPO: Multi-level Direct Preference Optimisation for Skeleton-based Gloss-free Sign Language Translation",
      "authors": [
        "Muxin Pu",
        "Xiao-Ming Wu",
        "Mei Kuan Lim",
        "Chun Yong Chong",
        "Wei Li",
        "Chen Change Loy"
      ],
      "published": "2026-04-20",
      "tags": [
        "ASL",
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2604.18034v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "We present SignDPO, a novel multi-level Direct Preference Optimisation (DPO) framework designed to enhance the alignment of skeleton-based Sign Language Translation. While current skeleton-based models have made significant progress using Maximum Likelihood Estimation, they are primarily constrained by an imitation-based paradigm that lacks discriminative sensitivity to the fine-grained spatio-temporal nuances of sign language, often leading to semantic drift. To address this, SignDPO shifts…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Think in Latent Thoughts: A New Paradigm for Gloss-Free Sign Language Translation",
      "authors": [
        "Yiyang Jiang",
        "Li Zhang",
        "Xiao-Yong Wei",
        "Li Qing"
      ],
      "published": "2026-04-16",
      "tags": [
        "translation"
      ],
      "url": "http://arxiv.org/abs/2604.15301v2",
      "source_site": "ACL",
      "task_category": "Sign Language Translation",
      "short_summary": "Many SLT systems quietly assume that brief chunks of signing map directly to spoken-language words. That assumption breaks down because signers often create meaning on the fly using context, space, and movement. We revisit SLT and argue that it is mainly a cross-modal reasoning task, not just a straightforward video-to-text conversion. We thus introduce a reasoning-driven SLT framework that uses an ordered sequence of latent thoughts as an explicit middle layer between the video and the…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Sign Language Recognition in the Age of LLMs",
      "authors": [
        "Vaclav Javorek",
        "Jakub Honzik",
        "Ivan Gruber",
        "Tomas Zelezny",
        "Marek Hruz"
      ],
      "published": "2026-04-13",
      "tags": [
        "ASL",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2604.11225v1",
      "source_site": "CVPR",
      "task_category": "Sign Language Recognition",
      "short_summary": "Recent Vision Language Models (VLMs) have demonstrated strong performance across a wide range of multimodal reasoning tasks. This raises the question of whether such general-purpose models can also address specialized visual recognition problems such as isolated sign language recognition (ISLR) without task-specific training. In this work, we investigate the capability of modern VLMs to perform ISLR in a zero-shot setting. We evaluate several open-source and proprietary VLMs on the WLASL300…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "State Space Models are Effective Sign Language Learners: Exploiting Phonological Compositionality for Vocabulary-Scale Recognition",
      "authors": [
        "Bryan Cheng",
        "Austin Jin",
        "Jasper Zhang"
      ],
      "published": "2026-04-09",
      "tags": [
        "ASL",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2604.08761v1",
      "source_site": "ICLR",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign language recognition suffers from catastrophic scaling failure: models achieving high accuracy on small vocabularies collapse at realistic sizes. Existing architectures treat signs as atomic visual patterns, learning flat representations that cannot exploit the compositional structure of sign languages-systematically organized from discrete phonological parameters (handshape, location, movement, orientation) reused across the vocabulary. We introduce PHONSSM, enforcing phonological…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "EfficientSign: An Attention-Enhanced Lightweight Architecture for Indian Sign Language Recognition",
      "authors": [
        "Rishabh Gupta",
        "Shravya R. Nalla"
      ],
      "published": "2026-04-09",
      "tags": [
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2604.08694v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "How do you build a sign language recognizer that works on a phone? That question drove this work. We built EfficientSign, a lightweight model which takes EfficientNet-B0 and focuses on two attention modules (Squeeze-and-Excitation for channel focus, and a spatial attention layer that focuses on the hand gestures). We tested it against five other approaches on 12,637 images of Indian Sign Language alphabets, all 26 classes, using 5-fold cross-validation. EfficientSign achieves the accuracy of…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
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

*Generated on April 28, 2026 at 07:28 UTC with 11 papers.*

### Source snapshot
<table class="snapshot-table">
  <thead>
    <tr><th>Source</th><th>Papers</th></tr>
  </thead>
  <tbody>
    <tr><td>arXiv</td><td>7</td></tr>
    <tr><td>NeurIPS</td><td>0</td></tr>
    <tr><td>ICML</td><td>0</td></tr>
    <tr><td>ICLR</td><td>1</td></tr>
    <tr><td>AAAI</td><td>0</td></tr>
    <tr><td>IJCAI</td><td>0</td></tr>
    <tr><td>ACL</td><td>2</td></tr>
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
    <tr><td>Sign Language Recognition</td><td>5</td></tr>
    <tr><td>Sign Language Translation</td><td>6</td></tr>
    <tr><td>Sign Language Production</td><td>0</td></tr>
    <tr><td>Other Sign Language Topic</td><td>0</td></tr>
    <tr><td>Co-speech Gesture Generation</td><td>0</td></tr>
    <tr><td>Gesture Recognition</td><td>0</td></tr>
  </tbody>
</table>


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (5)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (6)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production" disabled aria-disabled='true'>Sign Language Production (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic" disabled aria-disabled='true'>Other Sign Language Topic (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (7)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr">ICLR (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl">ACL (2)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp" disabled aria-disabled='true'>EMNLP (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr">CVPR (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
<article class="paper-card" data-source="arxiv" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>Evaluation of Pose Estimation Systems for Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Catherine O'Brien, Gerard Sant, Mathias Müller, Sarah Ebling</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-27</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.24609v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Many sign language translation (SLT) systems operate on pose sequences instead of raw video to reduce input dimensionality, improve portability, and partially anonymize signers. The choice of pose estimator is often treated as an implementation detail, with systems defaulting to widely available tools such as MediaPipe Holistic or OpenPose. We present a systematic comparison of pose estimators for pose-based SLT, covering widely used baselines (MediaPipe Holistic, OpenPose) and newer whole-…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
  </div>
</article>

<article class="paper-card" data-source="acl" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">ACL</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>Selective Contrastive Learning For Gloss Free Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Changhao Lai, Rui Zhao, Xuewen Zhong, Jinsong Su, Yidong Chen</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-24</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.22374v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language translation (SLT) converts continuous sign videos into spoken-language text, yet it remains challenging due to the intrinsic modality mismatch between visual signs and written text, particularly in gloss-free settings. Recent SLT systems increasingly adopt CLIP-like Vision-Language pretraining (VLP) for cross-modal alignment, but the random in-batch contrast provides few, batch-dependent negatives and may mislabel semantically similar (or even identical) pairs as negatives,…
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
  <h3>SignDATA: Data Pipeline for Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Kuanwei Chen, Tingyi Lin</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-22</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.20357v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign-language datasets are difficult to preprocess consistently because they vary in annotation schema, clip timing, signer framing, and privacy constraints. Existing work usually reports downstream models, while the preprocessing pipeline that converts raw video into training-ready pose or video artifacts remains fragmented, backend-specific, and weakly documented. We present SignDATA, a config-driven preprocessing toolkit that standardizes heterogeneous sign-language corpora into comparable…
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
  <h3>CanonSLR: Canonical-View Guided Multi-View Continuous Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Xu Wang, Shengeng Tang, Wan Jiang, Yaxiong Wang, Lechao Cheng, Richang Hong</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-20</p>
  <p class="paper-tags"><strong>Tags:</strong> neural-network, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.18184v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Continuous Sign Language Recognition (CSLR) has achieved remarkable progress in recent years; however, most existing methods are developed under single-view settings and thus remain insufficiently robust to viewpoint variations in real-world scenarios. To address this limitation, we propose CanonSLR, a canonical-view guided framework for multi-view CSLR. Specifically, we introduce a frontal-view-anchored teacher-student learning strategy, in which a teacher network trained on frontal-view data…
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
  <h3>SignDPO: Multi-level Direct Preference Optimisation for Skeleton-based Gloss-free Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Muxin Pu, Xiao-Ming Wu, Mei Kuan Lim, Chun Yong Chong, Wei Li, Chen Change Loy</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-20</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.18034v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> We present SignDPO, a novel multi-level Direct Preference Optimisation (DPO) framework designed to enhance the alignment of skeleton-based Sign Language Translation. While current skeleton-based models have made significant progress using Maximum Likelihood Estimation, they are primarily constrained by an imitation-based paradigm that lacks discriminative sensitivity to the fine-grained spatio-temporal nuances of sign language, often leading to semantic drift. To address this, SignDPO shifts…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
  </div>
</article>

<article class="paper-card" data-source="acl" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">ACL</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>Think in Latent Thoughts: A New Paradigm for Gloss-Free Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Yiyang Jiang, Li Zhang, Xiao-Yong Wei, Li Qing</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-16</p>
  <p class="paper-tags"><strong>Tags:</strong> translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.15301v2" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Many SLT systems quietly assume that brief chunks of signing map directly to spoken-language words. That assumption breaks down because signers often create meaning on the fly using context, space, and movement. We revisit SLT and argue that it is mainly a cross-modal reasoning task, not just a straightforward video-to-text conversion. We thus introduce a reasoning-driven SLT framework that uses an ordered sequence of latent thoughts as an explicit middle layer between the video and the…
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
  <h3>Sign Language Recognition in the Age of LLMs</h3>
  <p class="paper-authors"><strong>Authors:</strong> Vaclav Javorek, Jakub Honzik, Ivan Gruber, Tomas Zelezny, Marek Hruz</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-13</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.11225v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Recent Vision Language Models (VLMs) have demonstrated strong performance across a wide range of multimodal reasoning tasks. This raises the question of whether such general-purpose models can also address specialized visual recognition problems such as isolated sign language recognition (ISLR) without task-specific training. In this work, we investigate the capability of modern VLMs to perform ISLR in a zero-shot setting. We evaluate several open-source and proprietary VLMs on the WLASL300…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>

<article class="paper-card" data-source="iclr" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">ICLR</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>State Space Models are Effective Sign Language Learners: Exploiting Phonological Compositionality for Vocabulary-Scale Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Bryan Cheng, Austin Jin, Jasper Zhang</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-09</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.08761v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language recognition suffers from catastrophic scaling failure: models achieving high accuracy on small vocabularies collapse at realistic sizes. Existing architectures treat signs as atomic visual patterns, learning flat representations that cannot exploit the compositional structure of sign languages-systematically organized from discrete phonological parameters (handshape, location, movement, orientation) reused across the vocabulary. We introduce PHONSSM, enforcing phonological…
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
  <h3>EfficientSign: An Attention-Enhanced Lightweight Architecture for Indian Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Rishabh Gupta, Shravya R. Nalla</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-09</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.08694v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> How do you build a sign language recognizer that works on a phone? That question drove this work. We built EfficientSign, a lightweight model which takes EfficientNet-B0 and focuses on two attention modules (Squeeze-and-Excitation for channel focus, and a spatial attention layer that focuses on the hand gestures). We tested it against five other approaches on 12,637 images of Indian Sign Language alphabets, all 26 classes, using 5-fold cross-validation. EfficientSign achieves the accuracy of…
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
