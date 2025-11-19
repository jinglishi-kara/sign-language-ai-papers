---
layout: post
title: "Sign Language & AI – Recent Papers (November 19, 2025)"
date: 2025-11-19 19:38:30 +0000
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
</style>

This digest automatically gathers recent arXiv papers related to sign language translation/recognition and adjacent gesture research. The layout borrows inspiration from [VIPL-SLP/awesome-sign-language-processing](https://github.com/VIPL-SLP/awesome-sign-language-processing) so you can skim by task or venue.

*Generated on November 19, 2025 at 19:38 UTC with 20 papers.*

### Source snapshot
| Source | Papers |
| --- | --- |
| arXiv | 17 |
| NeurIPS | 0 |
| ICML | 0 |
| ICLR | 1 |
| AAAI | 1 |
| IJCAI | 0 |
| ACL | 0 |
| NAACL | 0 |
| EMNLP | 1 |
| COLING | 0 |
| CVPR | 0 |
| ICCV | 0 |
| ECCV | 0 |


### Task spotlight
| Task | Papers |
| --- | --- |
| Sign Language Recognition | 11 |
| Sign Language Translation | 7 |
| Sign Language Production | 0 |
| Other Sign Language Topic | 2 |
| Co-speech Gesture Generation | 0 |
| Gesture Recognition | 0 |


Use the filters below to mix-and-match conference venues and the task-driven taxonomy popularised by the awesome list. Hover over cards to explore summaries or click through to the original paper/code links.

<div class="paper-filter-panel"><div class="filter-group" data-group="task"><strong>Task focus</strong><button class="filter-btn active" data-filter-group="task" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-recognition">Sign Language Recognition (11)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-translation">Sign Language Translation (7)</button><button class="filter-btn" data-filter-group="task" data-filter-value="sign-language-production" disabled aria-disabled='true'>Sign Language Production (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="other-sign-language-topic">Other Sign Language Topic (2)</button><button class="filter-btn" data-filter-group="task" data-filter-value="co-speech-gesture-generation" disabled aria-disabled='true'>Co-speech Gesture Generation (0)</button><button class="filter-btn" data-filter-group="task" data-filter-value="gesture-recognition" disabled aria-disabled='true'>Gesture Recognition (0)</button></div><div class="filter-group" data-group="source"><strong>Conference & source</strong><button class="filter-btn active" data-filter-group="source" data-filter-value="all">All</button><button class="filter-btn" data-filter-group="source" data-filter-value="arxiv">arXiv (17)</button><button class="filter-btn" data-filter-group="source" data-filter-value="neurips" disabled aria-disabled='true'>NeurIPS (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="icml" disabled aria-disabled='true'>ICML (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iclr">ICLR (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="aaai">AAAI (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="ijcai" disabled aria-disabled='true'>IJCAI (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="acl" disabled aria-disabled='true'>ACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="naacl" disabled aria-disabled='true'>NAACL (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="emnlp">EMNLP (1)</button><button class="filter-btn" data-filter-group="source" data-filter-value="coling" disabled aria-disabled='true'>COLING (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="cvpr" disabled aria-disabled='true'>CVPR (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="iccv" disabled aria-disabled='true'>ICCV (0)</button><button class="filter-btn" data-filter-group="source" data-filter-value="eccv" disabled aria-disabled='true'>ECCV (0)</button></div></div>
<div class="paper-grid" id="paper-grid">
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

<article class="paper-card" data-source="emnlp" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">EMNLP</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>POSESTITCH-SLT: Linguistically Inspired Pose-Stitching for End-to-End Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Abhinav Joshi, Vaibhav Sharma, Sanjeet Singh, Ashutosh Modi</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-31</p>
  <p class="paper-tags"><strong>Tags:</strong> neural-network, pose-estimation, transformer, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2511.00270v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language translation remains a challenging task due to the scarcity of large-scale, sentence-aligned datasets. Prior arts have focused on various feature extraction and architectural changes to support neural machine translation for sign languages. We propose POSESTITCH-SLT, a novel pre-training scheme that is inspired by linguistic-templates-based sentence generation technique. With translation comparison on two sign language datasets, How2Sign and iSign, we show that a simple…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
  </div>
</article>

<article class="paper-card" data-source="iclr" data-task="sign-language-recognition">
  <div class="paper-chip-row">
    <span class="chip">ICLR</span>
    <span class="chip">Sign Language Recognition</span>
  </div>
  <h3>GLYPH-SR: Can We Achieve Both High-Quality Image Super-Resolution and High-Fidelity Text Recovery via VLM-guided Latent Diffusion Model?</h3>
  <p class="paper-authors"><strong>Authors:</strong> Mingyu Sung, Seungjae Ham, Kangwoo Kim, Yeokyoung Yoon, Sangseok Yun, Il-Min Kim, Jae-Mo Kang</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-30</p>
  <p class="paper-tags"><strong>Tags:</strong> recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.26339v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Image super-resolution(SR) is fundamental to many vision system-from surveillance and autonomy to document analysis and retail analytics-because recovering high-frequency details, especially scene-text, enables reliable downstream perception. Scene-text, i.e., text embedded in natural images such as signs, product labels, and storefronts, often carries the most actionable information; when characters are blurred or hallucinated, optical character recognition(OCR) and subsequent decisions fail…
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
  <h3>A Critical Study of Automatic Evaluation in Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Shakib Yazdani, Yasser Hamidullah, Cristina España-Bonet, Eleftherios Avramidis, Josef van Genabith</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-29</p>
  <p class="paper-tags"><strong>Tags:</strong> translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.25434v2" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Automatic evaluation metrics are crucial for advancing sign language translation (SLT). Current SLT evaluation metrics, such as BLEU and ROUGE, are only text-based, and it remains unclear to what extent text-based metrics can reliably capture the quality of SLT outputs. To address this gap, we investigate the limitations of text-based SLT evaluation metrics by analyzing six metrics, including BLEU, chrF, and ROUGE, as well as BLEURT on the one hand, and large language model (LLM)-based…
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
  <h3>Seeing, Signing, and Saying: A Vision-Language Model-Assisted Pipeline for Sign Language Data Acquisition and Curation from Social Media</h3>
  <p class="paper-authors"><strong>Authors:</strong> Shakib Yazdani, Yasser Hamidullah, Cristina España-Bonet, Josef van Genabith</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-29</p>
  <p class="paper-tags"><strong>Tags:</strong> ASL, pose-estimation, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.25413v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Most existing sign language translation (SLT) datasets are limited in scale, lack multilingual coverage, and are costly to curate due to their reliance on expert annotation and controlled recording setup. Recently, Vision Language Models (VLMs) have demonstrated strong capabilities as evaluators and real-time assistants. Despite these advancements, their potential remains untapped in the context of sign language dataset acquisition. To bridge this gap, we introduce the first automated…
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
  <h3>Proper Body Landmark Subset Enables More Accurate and 5X Faster Recognition of Isolated Signs in LIBRAS</h3>
  <p class="paper-authors"><strong>Authors:</strong> Daniele L. V. dos Santos, Thiago B. Pereira, Carlos Eduardo G. R. Alves, Richard J. M. G. Tello, Francisco de A. Boldt, Thiago M. Paixão</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-28</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.24887v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> This paper investigates the feasibility of using lightweight body landmark detection for the recognition of isolated signs in Brazilian Sign Language (LIBRAS). Although the skeleton-based approach by Alves et al. (2024) enabled substantial improvements in recognition performance, the use of OpenPose for landmark extraction hindered time performance. In a preliminary investigation, we observed that simply replacing OpenPose with the lightweight MediaPipe, while improving processing speed,…
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
  <h3>Reconnaissance Automatique des Langues des Signes : Une Approche Hybridée CNN-LSTM Basée sur Mediapipe</h3>
  <p class="paper-authors"><strong>Authors:</strong> Fraisse Sacré Takouchouang, Ho Tuong Vinh</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-24</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, recognition, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.22011v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign languages play a crucial role in the communication of deaf communities, but they are often marginalized, limiting access to essential services such as healthcare and education. This study proposes an automatic sign language recognition system based on a hybrid CNN-LSTM architecture, using Mediapipe for gesture keypoint extraction. Developed with Python, TensorFlow and Streamlit, the system provides real-time gesture translation. The results show an average accuracy of 92\%, with very good…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper is relevant because it tackles sign language translation.
  </div>
</article>

<article class="paper-card" data-source="aaai" data-task="other-sign-language-topic">
  <div class="paper-chip-row">
    <span class="chip">AAAI</span>
    <span class="chip">Other Sign Language Topic</span>
  </div>
  <h3>SIGN: Schema-Induced Games for Naming</h3>
  <p class="paper-authors"><strong>Authors:</strong> Ryan Zhang, Herbert Woisetscläger</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-22</p>
  <p class="paper-tags"><strong>Tags:</strong> sign-language-ai</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.21855v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Real-world AI systems are tackling increasingly complex problems, often through interactions among large language model (LLM) agents. When these agents develop inconsistent conventions, coordination can break down. Applications such as collaborative coding and distributed planning therefore require reliable, consistent communication, and scalability is a central concern as systems grow. We introduce Schema-Induced Games for Naming (SIGN), a naming game that examines how lightweight structure…
  </div>
  <div class="paper-summary">
    <strong>Why it matters:</strong> This paper explores methods that can be applied to sign language and AI.
  </div>
</article>

<article class="paper-card" data-source="arxiv" data-task="sign-language-translation">
  <div class="paper-chip-row">
    <span class="chip">arXiv</span>
    <span class="chip">Sign Language Translation</span>
  </div>
  <h3>Spatio-temporal Sign Language Representation and Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Yasser Hamidullah, Josef van Genabith, Cristina España-Bonet</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-22</p>
  <p class="paper-tags"><strong>Tags:</strong> translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.19413v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> This paper describes the DFKI-MLT submission to the WMT-SLT 2022 sign language translation (SLT) task from Swiss German Sign Language (video) into German (text). State-of-the-art techniques for SLT use a generic seq2seq architecture with customized input embeddings. Instead of word embeddings as used in textual machine translation, SLT systems use features extracted from video frames. Standard approaches often do not benefit from temporal features. In our participation, we present a system that…
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
  <h3>SONAR-SLT: Multilingual Sign Language Translation via Language-Agnostic Sentence Embedding Supervision</h3>
  <p class="paper-authors"><strong>Authors:</strong> Yasser Hamidullah, Shakib Yazdani, Cennet Oguz, Josef van Genabith, Cristina España-Bonet</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-22</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.19398v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Sign language translation (SLT) is typically trained with text in a single spoken language, which limits scalability and cross-language generalization. Earlier approaches have replaced gloss supervision with text-based sentence embeddings, but up to now, these remain tied to a specific language and modality. In contrast, here we employ language-agnostic, multimodal embeddings trained on text and speech from multiple languages to supervise SLT, enabling direct multilingual translation. To…
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
  <h3>Sign Language Translation with Sentence Embedding Supervision</h3>
  <p class="paper-authors"><strong>Authors:</strong> Yasser Hamidullah, Josef van Genabith, Cristina España-Bonet</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-22</p>
  <p class="paper-tags"><strong>Tags:</strong> translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.19367v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> State-of-the-art sign language translation (SLT) systems facilitate the learning process through gloss annotations, either in an end2end manner or by involving an intermediate step. Unfortunately, gloss labelled sign language data is usually not available at scale and, when available, gloss annotations widely differ from dataset to dataset. We present a novel approach using sentence embeddings of the target sentences at training time that take the role of glosses. The new kind of supervision…
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
  <h3>Grounding or Guessing? Visual Signals for Detecting Hallucinations in Sign Language Translation</h3>
  <p class="paper-authors"><strong>Authors:</strong> Yasser Hamidullah, Koel Dutta Chowdury, Yusser Al-Ghussin, Shakib Yazdani, Cennet Oguz, Josef van Genabith, Cristina España-Bonet</p>
  <p class="paper-published"><strong>Published:</strong> 2025-10-21</p>
  <p class="paper-tags"><strong>Tags:</strong> pose-estimation, translation</p>
  <p class="paper-links"><a href="http://arxiv.org/abs/2510.18439v1" target="_blank" rel="noopener">Read the paper</a></p>
  <div class="paper-summary">
    <strong>Summary:</strong> Hallucination, where models generate fluent text unsupported by visual evidence, remains a major flaw in vision-language models and is particularly critical in sign language translation (SLT). In SLT, meaning depends on precise grounding in video, and gloss-free models are especially vulnerable because they map continuous signer movements directly into natural language without intermediate gloss supervision that serves as alignment. We argue that hallucinations arise when models rely on…
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
