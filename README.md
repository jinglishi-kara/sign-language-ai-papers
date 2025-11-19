# sign-language-ai-papers

This repo automatically curates recent sign-language & AI papers and publishes them as a Jekyll blog post.

## Highlights

- 🔎 **Conference + task filters** – every digest now mirrors the structure of [VIPL-SLP/awesome-sign-language-processing](https://github.com/VIPL-SLP/awesome-sign-language-processing). Readers can toggle between venue (arXiv, NeurIPS, ICML, ICLR, AAAI, IJCAI, ACL, NAACL, EMNLP, COLING, CVPR, ICCV, ECCV) and task buckets such as recognition, translation, production, gesture generation, and more.
- 📊 **Live snapshot tables** – the post header summarizes per-source and per-task paper counts so visitors can spot where the latest activity concentrates.
- 🧾 **Rich paper cards** – each paper is rendered as a responsive card that surfaces authors, publication date, tags, and quick links without scrolling a long list.
- 🧭 **Why-it-matters nudges** – lightweight heuristics keep the commentary focused for sign-language practitioners looking for translation vs. recognition breakthroughs.

## Usage

```bash
pip install -r requirements.txt
python scripts/generate_sign_language_digest.py
```

Running the script produces a new `_posts/<date>-sign-language-ai-recent-papers.md` entry with the interactive layout.
