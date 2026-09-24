---
layout: post
title: "Sign Language & AI – Recent Papers (September 24, 2026)"
date: 2026-09-24 09:39:41 +0000
categories: [sign-language, ai]
tags: [sign-language, AI, ASL, research]
paper_count: 9
paper_catalog_json: >-
  [
    {
      "title": "Isolated Sign Language Recognition for Icelandic Sign Language: Experiments in a Low-resource Setting",
      "authors": [
        "Finnur Ágúst Ingimundarson",
        "Guðný Björk Þorvaldsdóttir",
        "Mathias Müller",
        "Sarah Ebling"
      ],
      "published": "2026-09-22",
      "tags": [
        "ASL",
        "pose-estimation",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2609.25862v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "We present the first experiments on isolated sign language recognition (ISLR) for Icelandic Sign Language (ÍTM). We use ÍTM SignWiki, a dataset derived from a bilingual Icelandic--ÍTM online dictionary. It is genuinely low-resource: 1,845 videos cover 849 classes, 86% of which have only two examples, making the full task effectively one-shot recognition across signers. We compare two open-source ISLR frameworks, OpenHands and SPOTER, on three tasks of increasing vocabulary size (22, 117 and 849…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
    {
      "title": "SignGPT: Toward LLM-Mediated Sign Language Interaction through Gloss-Free Translation and Generation",
      "authors": [
        "Ronghui Li",
        "Jun Dong",
        "Zhongyuan Hu",
        "Zunnan Xu",
        "Jun Zhou",
        "Liyuan Chen",
        "Shuoling Liu",
        "Jiangpeng Yan",
        "Jie Guo",
        "Xiu Li",
        "Linchao Bao"
      ],
      "published": "2026-09-18",
      "tags": [
        "ASL",
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2609.21709v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "Large language models (LLMs) provide limited support for sign language interaction. Unifying sign language translation (SLT) and generation (SLG) to enable sign language as both input and output can reduce switching between separate models during sign-text interaction. We present SignGPT, a unified, pose-based framework for gloss-free SLT and SLG. SignGPT integrates part-aware hierarchical representations of body, hand, and facial motion into a shared language model and employs asymmetric…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Investigating Temporal Motion Features for Pose-to-Text Indian Sign Language Translation",
      "authors": [
        "Manav Dhamecha",
        "Praveen Kumar Chandaliya",
        "Pruthwik Mishra"
      ],
      "published": "2026-09-11",
      "tags": [
        "pose-estimation",
        "translation"
      ],
      "url": "http://arxiv.org/abs/2609.12993v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Translation",
      "short_summary": "We investigate the effect of pretrained T5 model scale and explicit motion features on pose-to-text Indian Sign Language Translation (SLT) for the WSLP 2026 Shared Task. Pose sequences are projected into the embedding space of T5 through a lightweight pose encoder, with the complete model fine-tuned to generate English text. The shared task data used for this work consists of a test set with 5,334 examples and a validation set with 5,257 examples. We compare T5-small, T5-base, and T5-large, and…",
      "why_it_matters": "This paper is relevant because it tackles sign language translation."
    },
    {
      "title": "Learning Sign Language Recognition under Label Noise: A Study of Noise-Robust Losses for Isolated and Continuous Settings",
      "authors": [
        "Akihisa Shitara",
        "Yoichi Ochiai"
      ],
      "published": "2026-09-11",
      "tags": [
        "ASL",
        "recognition"
      ],
      "url": "http://arxiv.org/abs/2609.12885v1",
      "source_site": "arXiv",
      "task_category": "Sign Language Recognition",
      "short_summary": "In sign language recognition, the isolated (ISLR) classification loss treats a single label as ground truth, as does the frame-level auxiliary classifier over pseudo-labels we add to continuous (CSLR) methods, which lack one. Stylistic variation blurs ISLR annotation and the lack of temporal boundaries in CSLR forces pseudo-labels; both are noisy. We therefore apply symmetric and generalized cross entropy (SCE, GCE), robust alternatives to cross entropy (CE) from image classification, not to…",
      "why_it_matters": "This paper is relevant because it advances sign language recognition."
    },
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

*Generated on September 24, 2026 at 09:39 UTC with 9 papers.*

### Source snapshot
<table class="snapshot-table">
  <thead>
    <tr><th>Source</th><th>Papers</th></tr>
  </thead>
  <tbody>
    <tr><td>arXiv</td><td>8</td></tr>
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
    <tr><td>Sign Language Recognition</td><td>5</td></tr>
    <tr><td>Sign Language Translation</td><td>4</td></tr>
    <tr><td>Sign Language Production</td><td>0</td></tr>
    <tr><td>Other Sign Language Topic</td><td>0</td></tr>
    <tr><td>Co-speech Gesture Generation</td><td>0</td></tr>
    <tr><td>Gesture Recognition</td><td>0</td></tr>
  </tbody>
</table>


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (5)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (4)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production" disabled aria-disabled='true'>Sign Language Production (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic" disabled aria-disabled='true'>Other Sign Language Topic (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (8)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr" disabled aria-disabled='true'>ICLR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl" disabled aria-disabled='true'>ACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp">EMNLP (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr" disabled aria-disabled='true'>CVPR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>Isolated Sign Language Recognition for Icelandic Sign Language: Experiments in a Low-resource Setting</h3>
  <p class="paper-authors"><strong>Authors:</strong> Finnur Ágúst Ingimundarson, Guðný Björk Þorvaldsdóttir, Mathias Müller, Sarah Ebling</p>
  <p class="paper-published"><strong>Published:</strong> 2026-09-22</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2609.25862v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> We present the first experiments on isolated sign language recognition (ISLR) for Icelandic Sign Language (ÍTM). We use ÍTM SignWiki, a dataset derived from a bilingual Icelandic--ÍTM online dictionary. It is genuinely low-resource: 1,845 videos cover 849 classes, 86% of which have only two examples, making the full task effectively one-shot recognition across signers. We compare two open-source ISLR frameworks, OpenHands and SPOTER, on three tasks of increasing vocabulary size (22, 117 and 849…
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
  <h3>SignGPT: Toward LLM-Mediated Sign Language Interaction through Gloss-Free Translation and Generation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Ronghui Li, Jun Dong, Zhongyuan Hu, Zunnan Xu, Jun Zhou, Liyuan Chen, Shuoling Liu, Jiangpeng Yan, Jie Guo, Xiu Li, Linchao Bao</p>
  <p class="paper-published"><strong>Published:</strong> 2026-09-18</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2609.21709v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Large language models (LLMs) provide limited support for sign language interaction. Unifying sign language translation (SLT) and generation (SLG) to enable sign language as both input and output can reduce switching between separate models during sign-text interaction. We present SignGPT, a unified, pose-based framework for gloss-free SLT and SLG. SignGPT integrates part-aware hierarchical representations of body, hand, and facial motion into a shared language model and employs asymmetric…
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
  <h3>Investigating Temporal Motion Features for Pose-to-Text Indian Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Manav Dhamecha, Praveen Kumar Chandaliya, Pruthwik Mishra</p>
  <p class="paper-published"><strong>Published:</strong> 2026-09-11</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2609.12993v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> We investigate the effect of pretrained T5 model scale and explicit motion features on pose-to-text Indian Sign Language Translation (SLT) for the WSLP 2026 Shared Task. Pose sequences are projected into the embedding space of T5 through a lightweight pose encoder, with the complete model fine-tuned to generate English text. The shared task data used for this work consists of a test set with 5,334 examples and a validation set with 5,257 examples. We compare T5-small, T5-base, and T5-large, and…
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
  <h3>Learning Sign Language Recognition under Label Noise: A Study of Noise-Robust Losses for Isolated and Continuous Settings</h3>
  <p class="paper-authors"><strong>Authors:</strong> Akihisa Shitara, Yoichi Ochiai</p>
  <p class="paper-published"><strong>Published:</strong> 2026-09-11</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2609.12885v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> In sign language recognition, the isolated (ISLR) classification loss treats a single label as ground truth, as does the frame-level auxiliary classifier over pseudo-labels we add to continuous (CSLR) methods, which lack one. Stylistic variation blurs ISLR annotation and the lack of temporal boundaries in CSLR forces pseudo-labels; both are noisy. We therefore apply symmetric and generalized cross entropy (SCE, GCE), robust alternatives to cross entropy (CE) from image classification, not to…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>

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
