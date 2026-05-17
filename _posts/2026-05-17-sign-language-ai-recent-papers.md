---
layout: post
title: "Sign Language & AI – Recent Papers (May 17, 2026)"
date: 2026-05-17 07:32:21 +0000
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
paper_count: 14
paper_catalog_json: >-
  [
    {
      "title": "Sign Language Recognition and Translation for Low-Resource Languages: Challenges and Pathways Forward",
      "authors": [
        "Nigar Alishzade",
        "Gulchin Abdullayeva"
      ],
      "published": "2026-05-12",
      "tags": [
        "pose-estimation",
        "recognition",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2605.12096v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign languages are natural, visual-gestural languages used by Deaf communities worldwide. Over 300 distinct sign languages remain severely low-resource due to limited documentation, sparse datasets, and insufficient computational tools. This systematic review synthesizes literature on sign language recognition and translation for under-resourced languages, using Azerbaijan Sign Language (AzSL) as a case study. Analysis of global initiatives extracts eight actionable lessons, including community…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Towards Compact Sign Language Translation: Frame Rate and Model Size Trade-offs",
      "authors": [
        "Kuanwei Chen",
        "Mengfeng Tsai"
      ],
      "published": "2026-05-10",
      "tags": [
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2605.09554v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "Sign Language Translation (SLT) converts sign language videos into spoken-language text, bridging communication between Deaf and hearing communities. Current gloss-free approaches rely on large encoder-decoder models, limiting deployment. We propose a compact 77M-parameter pipeline that couples MMPose skeletal pose extraction with a single linear projection into T5-small. By varying the input frame rate, we expose a practical efficiency trade-off: at 12 fps the model halves its sequence length,…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "CAST: Channel-Aware Spatial Transfer Learning with Pseudo-Image Radar for Sign Language Recognition",
      "authors": [
        "Md. Shakhoyat Rahman Shujon",
        "Sheikh Md. Galib Mahim",
        "Md. Milon Islam",
        "Md Rezwanul Haque",
        "Md Rabiul Islam",
        "Hamdi Altaheri",
        "Fakhri Karray"
      ],
      "published": "2026-05-09",
      "tags": [
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2605.08663v1",
      "source_site": "CVPR",
      "task_category": "Sign Language Recognition",
      "short_summary": "We propose CAST, a dual-stream architecture that utilizes channel-aware spatial transfer learning for isolated sign language recognition addressing the challenges of magnitude-only 60~GHz radar Range-Time Maps (RTM). The proposed framework combines three physics-aware architectures with pretrained vision backbones, which operate under radar-only constraints across clinical and alphabetical gestures. First, an explicit decibel-to-linear inversion is combined with a windowed fast Fourier…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "Neuromorphic visual attention for Sign-language recognition on SpiNNaker",
      "authors": [
        "Sarka Liskova",
        "Olha Vedmedenko",
        "Mazdak Fatahi",
        "Matej Hoffmann",
        "P. Michael Furlong",
        "Giulia D Angelo"
      ],
      "published": "2026-05-07",
      "tags": [
        "ASL",
        "neural-network",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2605.06005v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign-language recognition has achieved substantial gains in classification accuracy in recent years; however, the latency and power requirements of most existing methods limit their suitability for real-time deployment. Neuromorphic sensing and processing offer an alternative paradigm based on sparse, event-driven computation that supports low-latency and energy-efficient perception. In this work, we introduce an end-to-end neuromorphic architecture for American Sign Language (ASL)…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "Tamaththul3D: High-Fidelity 3D Saudi Sign Language Avatars from Monocular Video",
      "authors": [
        "Eyad Alghamdi",
        "Sattam Altuuaim",
        "Obay Ghulam",
        "Abdulrahman Qutah",
        "Yousef Basoodan"
      ],
      "published": "2026-05-06",
      "tags": [
        "avatar",
        "pose-estimation"
      ],
      "url": "http://arxiv.org/abs/2605.05367v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Production",
      "short_summary": "Arabic Sign Language (ArSL) and its dialects serve approximately 400 million Arabic speakers worldwide, yet the community lacks high-quality 3D parametric annotations and specialized reconstruction methods for avatar generation. We address this critical gap through two key contributions: First, we introduce the first high-quality 3D parametric annotations for the Ishara-500 Saudi Sign Language dataset, providing precise SMPL-X parameters for 500 culturally authentic SSL signs. Second, we…",
      "why_it_matters": "This paper explores methods that can be applied to sign language and AI."
    },
    {
      "title": "SignMAE: Segmentation-Driven Self-Supervised Learning for Sign Language Recognition",
      "authors": [
        "Kunyuan Xie",
        "Zhixi Cai",
        "Kalin Stefanov"
      ],
      "published": "2026-05-03",
      "tags": [
        "ASL",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2605.02094v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Subtle hand differences make sign language recognition challenging, yet many existing methods rely on encoders pretrained on generic action datasets that poorly capture such fine-grained cues. We propose a self-supervised pretraining method for sign language recognition that uses segmentation-based masking to adapt to the presence and motion of key body parts, rather than treating hand poses as static visual tokens. The resulting mask-and-reconstruct objective improves fine-grained sign…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "OmniEncoder: See, Hear, and Feel Continuous Motion Like Humans With One Encoder",
      "authors": [
        "Detao Bai",
        "Shimin Yao",
        "Weixuan Chen",
        "Chengen Lai",
        "Yuanming Li",
        "Zhiheng Ma",
        "Xihan Wei"
      ],
      "published": "2026-05-02",
      "tags": [
        "recognition",
        "transformer"
      ],
      "url": "http://arxiv.org/abs/2605.01506v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Recent advances in omni-modal large language models have enabled remarkable progress in joint vision-audio understanding. However, prevailing architectures rely on modality-specific encoders with a \\emph{video-coarse, audio-dense} design -- sampling visual frames at 1--2 fps while processing audio waveforms at 25 fps -- resulting in systems that perceive video \\emph{frame by frame, modality by modality} rather than holistically as humans do. Such a discrepancy leaves models with impoverished…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "Normativity and Productivism: Ableist Intelligence? A Degrowth Analysis of AI Sign Language Translation Tools for Deaf People",
      "authors": [
        "Nina Seron-Abouelfadil",
        "Poppy Fynes"
      ],
      "published": "2026-04-30",
      "tags": [
        "recognition",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2604.28125v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Sign languages, of any geographical or accentual variation, understandably face continuous scrutiny under the ever present popularity of verbal dictation and audism. Through this, many potential problems arise with the current lack of accessible communication for those who rely on such sign languages for essential conversation. Such AI systems regularly take the form of recognition and interpretation models, designed to provide seamless and accurate translation. In reality these systems are…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Targeted Linguistic Analysis of Sign Language Models with Minimal Translation Pairs",
      "authors": [
        "Serpil Karabüklü",
        "Kanishka Misra",
        "Shester Gueuwou",
        "Diane Brentari",
        "Greg Shakhnarovich",
        "Karen Livescu"
      ],
      "published": "2026-04-29",
      "tags": [
        "ASL",
        "recognition",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2604.27232v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "Models of sign language have historically lagged behind those for spoken language (text and speech). Recent work has greatly improved their performance on tasks like sign language translation and isolated sign recognition. However, it remains unclear to what extent existing models capture various linguistic phenomena of sign language, and how well they use cues from the multiple articulators used in sign language (hands, upper body, face). We introduce a new benchmark dataset for American Sign…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
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

*Generated on May 17, 2026 at 07:32 UTC with 14 papers.*

### Source snapshot
<table class="snapshot-table">
  <thead>
    <tr><th>Source</th><th>Papers</th></tr>
  </thead>
  <tbody>
    <tr><td>arXiv</td><td>12</td></tr>
    <tr><td>NeurIPS</td><td>0</td></tr>
    <tr><td>ICML</td><td>0</td></tr>
    <tr><td>ICLR</td><td>0</td></tr>
    <tr><td>AAAI</td><td>0</td></tr>
    <tr><td>IJCAI</td><td>0</td></tr>
    <tr><td>ACL</td><td>1</td></tr>
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
    <tr><td>Sign Language Recognition</td><td>8</td></tr>
    <tr><td>Sign Language Translation</td><td>5</td></tr>
    <tr><td>Sign Language Production</td><td>1</td></tr>
    <tr><td>Other Sign Language Topic</td><td>0</td></tr>
    <tr><td>Co-speech Gesture Generation</td><td>0</td></tr>
    <tr><td>Gesture Recognition</td><td>0</td></tr>
  </tbody>
</table>


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (8)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (5)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production">Sign Language Production (1)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic" disabled aria-disabled='true'>Other Sign Language Topic (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (12)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr" disabled aria-disabled='true'>ICLR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl">ACL (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp" disabled aria-disabled='true'>EMNLP (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr">CVPR (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>Sign Language Recognition and Translation for Low-Resource Languages: Challenges and Pathways Forward</h3>
  <p class="paper-authors"><strong>Authors:</strong> Nigar Alishzade, Gulchin Abdullayeva</p>
  <p class="paper-published"><strong>Published:</strong> 2026-05-12</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2605.12096v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign languages are natural, visual-gestural languages used by Deaf communities worldwide. Over 300 distinct sign languages remain severely low-resource due to limited documentation, sparse datasets, and insufficient computational tools. This systematic review synthesizes literature on sign language recognition and translation for under-resourced languages, using Azerbaijan Sign Language (AzSL) as a case study. Analysis of global initiatives extracts eight actionable lessons, including community…
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
  <h3>Towards Compact Sign Language Translation: Frame Rate and Model Size Trade-offs</h3>
  <p class="paper-authors"><strong>Authors:</strong> Kuanwei Chen, Mengfeng Tsai</p>
  <p class="paper-published"><strong>Published:</strong> 2026-05-10</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2605.09554v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign Language Translation (SLT) converts sign language videos into spoken-language text, bridging communication between Deaf and hearing communities. Current gloss-free approaches rely on large encoder-decoder models, limiting deployment. We propose a compact 77M-parameter pipeline that couples MMPose skeletal pose extraction with a single linear projection into T5-small. By varying the input frame rate, we expose a practical efficiency trade-off: at 12 fps the model halves its sequence length,…
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
  <h3>CAST: Channel-Aware Spatial Transfer Learning with Pseudo-Image Radar for Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Md. Shakhoyat Rahman Shujon, Sheikh Md. Galib Mahim, Md. Milon Islam, Md Rezwanul Haque, Md Rabiul Islam, Hamdi Altaheri, Fakhri Karray</p>
  <p class="paper-published"><strong>Published:</strong> 2026-05-09</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2605.08663v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> We propose CAST, a dual-stream architecture that utilizes channel-aware spatial transfer learning for isolated sign language recognition addressing the challenges of magnitude-only 60~GHz radar Range-Time Maps (RTM). The proposed framework combines three physics-aware architectures with pretrained vision backbones, which operate under radar-only constraints across clinical and alphabetical gestures. First, an explicit decibel-to-linear inversion is combined with a windowed fast Fourier…
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
  <h3>Neuromorphic visual attention for Sign-language recognition on SpiNNaker</h3>
  <p class="paper-authors"><strong>Authors:</strong> Sarka Liskova, Olha Vedmedenko, Mazdak Fatahi, Matej Hoffmann, P. Michael Furlong, Giulia D Angelo</p>
  <p class="paper-published"><strong>Published:</strong> 2026-05-07</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, neural-network, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2605.06005v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign-language recognition has achieved substantial gains in classification accuracy in recent years; however, the latency and power requirements of most existing methods limit their suitability for real-time deployment. Neuromorphic sensing and processing offer an alternative paradigm based on sparse, event-driven computation that supports low-latency and energy-efficient perception. In this work, we introduce an end-to-end neuromorphic architecture for American Sign Language (ASL)…
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
  <h3>Tamaththul3D: High-Fidelity 3D Saudi Sign Language Avatars from Monocular Video</h3>
  <p class="paper-authors"><strong>Authors:</strong> Eyad Alghamdi, Sattam Altuuaim, Obay Ghulam, Abdulrahman Qutah, Yousef Basoodan</p>
  <p class="paper-published"><strong>Published:</strong> 2026-05-06</p>
  <p class="paper-tags"><strong>Tags:</strong> avatar, pose-estimation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2605.05367v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Arabic Sign Language (ArSL) and its dialects serve approximately 400 million Arabic speakers worldwide, yet the community lacks high-quality 3D parametric annotations and specialized reconstruction methods for avatar generation. We address this critical gap through two key contributions: First, we introduce the first high-quality 3D parametric annotations for the Ishara-500 Saudi Sign Language dataset, providing precise SMPL-X parameters for 500 culturally authentic SSL signs. Second, we…
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
  <h3>SignMAE: Segmentation-Driven Self-Supervised Learning for Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Kunyuan Xie, Zhixi Cai, Kalin Stefanov</p>
  <p class="paper-published"><strong>Published:</strong> 2026-05-03</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2605.02094v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Subtle hand differences make sign language recognition challenging, yet many existing methods rely on encoders pretrained on generic action datasets that poorly capture such fine-grained cues. We propose a self-supervised pretraining method for sign language recognition that uses segmentation-based masking to adapt to the presence and motion of key body parts, rather than treating hand poses as static visual tokens. The resulting mask-and-reconstruct objective improves fine-grained sign…
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
  <h3>OmniEncoder: See, Hear, and Feel Continuous Motion Like Humans With One Encoder</h3>
  <p class="paper-authors"><strong>Authors:</strong> Detao Bai, Shimin Yao, Weixuan Chen, Chengen Lai, Yuanming Li, Zhiheng Ma, Xihan Wei</p>
  <p class="paper-published"><strong>Published:</strong> 2026-05-02</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition, transformer</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2605.01506v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Recent advances in omni-modal large language models have enabled remarkable progress in joint vision-audio understanding. However, prevailing architectures rely on modality-specific encoders with a \emph{video-coarse, audio-dense} design -- sampling visual frames at 1--2 fps while processing audio waveforms at 25 fps -- resulting in systems that perceive video \emph{frame by frame, modality by modality} rather than holistically as humans do. Such a discrepancy leaves models with impoverished…
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
  <h3>Normativity and Productivism: Ableist Intelligence? A Degrowth Analysis of AI Sign Language Translation Tools for Deaf People</h3>
  <p class="paper-authors"><strong>Authors:</strong> Nina Seron-Abouelfadil, Poppy Fynes</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-30</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.28125v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign languages, of any geographical or accentual variation, understandably face continuous scrutiny under the ever present popularity of verbal dictation and audism. Through this, many potential problems arise with the current lack of accessible communication for those who rely on such sign languages for essential conversation. Such AI systems regularly take the form of recognition and interpretation models, designed to provide seamless and accurate translation. In reality these systems are…
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
  <h3>Targeted Linguistic Analysis of Sign Language Models with Minimal Translation Pairs</h3>
  <p class="paper-authors"><strong>Authors:</strong> Serpil Karabüklü, Kanishka Misra, Shester Gueuwou, Diane Brentari, Greg Shakhnarovich, Karen Livescu</p>
  <p class="paper-published"><strong>Published:</strong> 2026-04-29</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2604.27232v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Models of sign language have historically lagged behind those for spoken language (text and speech). Recent work has greatly improved their performance on tasks like sign language translation and isolated sign recognition. However, it remains unclear to what extent existing models capture various linguistic phenomena of sign language, and how well they use cues from the multiple articulators used in sign language (hands, upper body, face). We introduce a new benchmark dataset for American Sign…
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
