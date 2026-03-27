---
layout: post
title: "Sign Language & AI – Recent Papers (December 01, 2025)"
date: 2025-12-01 05:24:07 +0000
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

*Generated on December 01, 2025 at 05:24 UTC with 15 papers.*

### Source snapshot
<table class="snapshot-table">
  <thead>
    <tr><th>Source</th><th>Papers</th></tr>
  </thead>
  <tbody>
    <tr><td>arXiv</td><td>15</td></tr>
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
    <tr><td>Sign Language Recognition</td><td>11</td></tr>
    <tr><td>Sign Language Translation</td><td>2</td></tr>
    <tr><td>Sign Language Production</td><td>0</td></tr>
    <tr><td>Other Sign Language Topic</td><td>2</td></tr>
    <tr><td>Co-speech Gesture Generation</td><td>0</td></tr>
    <tr><td>Gesture Recognition</td><td>0</td></tr>
  </tbody>
</table>


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (11)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (2)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production" disabled aria-disabled='true'>Sign Language Production (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic">Other Sign Language Topic (2)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (15)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr" disabled aria-disabled='true'>ICLR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai" disabled aria-disabled='true'>AAAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl" disabled aria-disabled='true'>ACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp" disabled aria-disabled='true'>EMNLP (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr" disabled aria-disabled='true'>CVPR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
<article class="paper-card" data-source="arxiv" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>EASL: Multi-Emotion Guided Semantic Disentanglement for Expressive Sign Language Generation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Yanchao Zhao, Jihao Zhu, Yu Liu, Weizhuo Chen, Yuling Yang, Kun Peng</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-27</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.22135v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Large language models have revolutionized sign language generation by automatically transforming text into high-quality sign language videos, providing accessible communication for the Deaf community. However, existing LLM-based approaches prioritize semantic accuracy while overlooking emotional expressions, resulting in outputs that lack naturalness and expressiveness. We propose EASL (Emotion-Aware Sign Language), a multi-emotion-guided generation architecture for fine-grained emotional…
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
  <h3>Bangla Sign Language Translation: Dataset Creation Challenges, Benchmarking and Prospects</h3>
  <p class="paper-authors"><strong>Authors:</strong> Husne Ara Rubaiyeat, Hasan Mahmud, Md Kamrul Hasan</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-26</p>
  <p class="paper-tags"><strong>Tags:</strong> translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.21533v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Bangla Sign Language Translation (BdSLT) has been severely constrained so far as the language itself is very low resource. Standard sentence level dataset creation for BdSLT is of immense importance for developing AI based assistive tools for deaf and hard of hearing people of Bangla speaking community. In this paper, we present a dataset, IsharaKhobor , and two subset of it for enabling research. We also present the challenges towards developing the dataset and present some way forward by…
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
  <h3>ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction</h3>
  <p class="paper-authors"><strong>Authors:</strong> Qineng Wang, Wenlong Huang, Yu Zhou, Hang Yin, Tianwei Bao, Jianwen Lyu, Weiyu Liu, Ruohan Zhang, Jiajun Wu, Li Fei-Fei, Manling Li</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-26</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.20937v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Embodied cognition argues that intelligence arises from sensorimotor interaction rather than passive observation. It raises an intriguing question: do modern vision-language models (VLMs), trained largely in a disembodied manner, exhibit signs of embodied cognition? We introduce ENACT, a benchmark that casts evaluation of embodied cognition as world modeling from egocentric interaction in a visual question answering (VQA) format. Framed as a partially observable Markov decision process (POMDP)…
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
  <h3>MHB: Multimodal Handshape-aware Boundary Detection for Continuous Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Mingyu Zhao, Zhanfu Yang, Yang Zhou, Zhaoyang Xia, Can Jin, Xiaoxiao He, Carol Neidle, Dimitris N. Metaxas</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-25</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.19907v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> This paper presents a multimodal approach for continuous sign recognition that first uses machine learning to detect the start and end frames of signs in videos of American Sign Language (ASL) sentences, and then recognizes the segmented signs. For improved robustness, we use 3D skeletal features extracted from sign language videos to capture the convergence of sign properties and their dynamics, which tend to cluster at sign boundaries. Another focus of this work is the incorporation of…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="other-sign-language-topic">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Other Sign Language Topic</span>
  </div>
  <h3>PropensityBench: Evaluating Latent Safety Risks in Large Language Models via an Agentic Approach</h3>
  <p class="paper-authors"><strong>Authors:</strong> Udari Madhushani Sehwag, Shayan Shabihi, Alex McAvoy, Vikash Sehwag, Yuancheng Xu, Dalton Towers, Furong Huang</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-24</p>
  <p class="paper-tags"><strong>Tags:</strong> sign-language-ai</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.20703v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Recent advances in Large Language Models (LLMs) have sparked concerns over their potential to acquire and misuse dangerous or high-risk capabilities, posing frontier risks. Current safety evaluations primarily test for what a model \textit{can} do - its capabilities - without assessing what it $\textit{would}$ do if endowed with high-risk capabilities. This leaves a critical blind spot: models may strategically conceal capabilities or rapidly acquire them, while harboring latent inclinations…
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
  <h3>Enhancing LLM-based Autonomous Driving with Modular Traffic Light and Sign Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Fabian Schmidt, Noushiq Mohammed Kayilan Abdul Nazar, Markus Enzweiler, Abhinav Valada</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-18</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.14391v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Large Language Models (LLMs) are increasingly used for decision-making and planning in autonomous driving, showing promising reasoning capabilities and potential to generalize across diverse traffic situations. However, current LLM-based driving agents lack explicit mechanisms to enforce traffic rules and often struggle to reliably detect small, safety-critical objects such as traffic lights and signs. To address this limitation, we introduce TLS-Assist, a modular redundancy layer that augments…
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
  <h3>Robustness of Structured Data Extraction from Perspectively Distorted Documents</h3>
  <p class="paper-authors"><strong>Authors:</strong> Hyakka Nakada, Yoshiyasu Tanaka</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-18</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.17607v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Optical Character Recognition (OCR) for data extraction from documents is essential to intelligent informatics, such as digitizing medical records and recognizing road signs. Multi-modal Large Language Models (LLMs) can solve this task and have shown remarkable performance. Recently, it has been noticed that the accuracy of data extraction by multi-modal LLMs can be affected when in-plane rotations are present in the documents. However, real-world document images are usually not only in-plane…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it advances sign language recognition.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="other-sign-language-topic">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Other Sign Language Topic</span>
  </div>
  <h3>Mind the Gap: Evaluating LLM Understanding of Human-Taught Road Safety Principles</h3>
  <p class="paper-authors"><strong>Authors:</strong> Chalamalasetti Kranti</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-17</p>
  <p class="paper-tags"><strong>Tags:</strong> sign-language-ai</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.13909v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Following road safety norms is non-negotiable not only for humans but also for the AI systems that govern autonomous vehicles. In this work, we evaluate how well multi-modal large language models (LLMs) understand road safety concepts, specifically through schematic and illustrative representations. We curate a pilot dataset of images depicting traffic signs and road-safety norms sourced from school text books and use it to evaluate models capabilities in a zero-shot setting. Our preliminary…
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
  <h3>A Comparative Analysis of Recurrent and Attention Architectures for Isolated Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Nigar Alishzade, Gulchin Abdullayeva</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-17</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, neural-network, recognition, transformer</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.13126v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> This study presents a systematic comparative analysis of recurrent and attention-based neural architectures for isolated sign language recognition. We implement and evaluate two representative models-ConvLSTM and Vanilla Transformer-on the Azerbaijani Sign Language Dataset (AzSLD) and the Word-Level American Sign Language (WLASL) dataset. Our results demonstrate that the attention-based Vanilla Transformer consistently outperforms the recurrent ConvLSTM in both Top-1 and Top-5 accuracy across…
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
  <h3>RoCoISLR: A Romanian Corpus for Isolated Sign Language Recognition</h3>
  <p class="paper-authors"><strong>Authors:</strong> Cătălin-Alexandru Rîpanu, Andrei-Theodor Hotnog, Giulia-Stefania Imbrea, Dumitru-Clementin Cercel</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-16</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition, transformer</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.12767v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Automatic sign language recognition plays a crucial role in bridging the communication gap between deaf communities and hearing individuals; however, most available datasets focus on American Sign Language. For Romanian Isolated Sign Language Recognition (RoISLR), no large-scale, standardized dataset exists, which limits research progress. In this work, we introduce a new corpus for RoISLR, named RoCoISLR, comprising over 9,000 video samples that span nearly 6,000 standardized glosses from…
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
  <h3>BdSL-SPOTER: A Transformer-Based Framework for Bengali Sign Language Recognition with Cultural Adaptation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Sayad Ibna Azad, Md. Atiqur Rahman</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-15</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition, transformer</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.12103v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> We introduce BdSL-SPOTER, a pose-based transformer framework for accurate and efficient recognition of Bengali Sign Language (BdSL). BdSL-SPOTER extends the SPOTER paradigm with cultural specific preprocessing and a compact four-layer transformer encoder featuring optimized learnable positional encodings, while employing curriculum learning to enhance generalization on limited data and accelerate convergence. On the BdSLW60 benchmark, it achieves 97.92% Top-1 validation accuracy, representing a…
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
  <h3>Large Sign Language Models: Toward 3D American Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Sen Zhang, Xiaoxiao He, Di Liu, Zhaoyang Xia, Mingyu Zhao, Chaowei Tan, Vivian Li, Bo Liu, Dimitris N. Metaxas, Mubbasir Kapadia</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-11</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.08535v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> We present Large Sign Language Models (LSLM), a novel framework for translating 3D American Sign Language (ASL) by leveraging Large Language Models (LLMs) as the backbone, which can benefit hearing-impaired individuals' virtual communication. Unlike existing sign language recognition methods that rely on 2D video, our approach directly utilizes 3D sign language data to capture rich spatial, gestural, and depth information in 3D scenes. This enables more accurate and resilient translation,…
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
  <h3>Introducing A Bangla Sentence - Gloss Pair Dataset for Bangla Sign Language Translation and Research</h3>
  <p class="paper-authors"><strong>Authors:</strong> Neelavro Saha, Rafi Shahriyar, Nafis Ashraf Roudra, Saadman Sakib, Annajiat Alim Rasel</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-11</p>
  <p class="paper-tags"><strong>Tags:</strong> transformer, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.08507v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Bangla Sign Language (BdSL) translation represents a low-resource NLP task due to the lack of large-scale datasets that address sentence-level translation. Correspondingly, existing research in this field has been limited to word and alphabet level detection. In this work, we introduce Bangla-SGP, a novel parallel dataset consisting of 1,000 human-annotated sentence-gloss pairs which was augmented with around 3,000 synthetically generated pairs using syntactic and morphological rules through a…
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
  <h3>Sign language recognition from skeletal data using graph and recurrent neural networks</h3>
  <p class="paper-authors"><strong>Authors:</strong> B. Mederos, J. Mejía, A. Medina-Reyes, Y. Espinosa-Almeyda, J. D. Díaz-Roman, I. Rodríguez-Mederos, M. Mejía-Carreon, F. Gonzalez-Lopez</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-08</p>
  <p class="paper-tags"><strong>Tags:</strong> neural-network, pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.05772v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> This work presents an approach for recognizing isolated sign language gestures using skeleton-based pose data extracted from video sequences. A Graph-GRU temporal network is proposed to model both spatial and temporal dependencies between frames, enabling accurate classification. The model is trained and evaluated on the AUTSL (Ankara university Turkish sign language) dataset, achieving high accuracy. Experimental results demonstrate the effectiveness of integrating graph-based spatial…
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
  <h3>Smart-Hiring: An Explainable end-to-end Pipeline for CV Information Extraction and Job Matching</h3>
  <p class="paper-authors"><strong>Authors:</strong> Kenza Khelkhal, Dihia Lanasri</p>
  <p class="paper-published"><strong>Published:</strong> 2025-11-04</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.02537v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Hiring processes often involve the manual screening of hundreds of resumes for each job, a task that is time and effort consuming, error-prone, and subject to human bias. This paper presents Smart-Hiring, an end-to-end Natural Language Processing (NLP) pipeline de- signed to automatically extract structured information from unstructured resumes and to semantically match candidates with job descriptions. The proposed system combines document parsing, named-entity recognition, and contextual text…
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
