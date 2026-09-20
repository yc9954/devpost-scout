---
slug: "deepsint"
url: "https://devpost.com/software/deepsint"
title: "Deepsint"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 409
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/security_privacy"
  - "user/researcher"
  - "substrate/video_visual"
---

# Deepsint

> An OSINT tool specializes in generating an accurate profile card from a username by leveraging artificial intelligence.

[Devpost](https://devpost.com/software/deepsint) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[graph_reasoning]] [[provenance_signing]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[security_privacy]]
**user** [[researcher]]
**substrate** [[video_visual]]

**stack** cohere, python, sqlite, streamlit

## How they structured the write-up

- 🌟 inspiration
- ⚙️ what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments
- 📚 what we learned
- 🚀 what’s next for deepsint

## Body

Main search page History page 🕵️ Deepsint One username → one trusted profile card. Turning scattered OSINT signals into explainable insights, fast. 🌟 Inspiration We all hear the warnings of data breaches and the dangers of the internet . We've also heard that someone can reconstruct everything about you using OSINT tools—without ever meeting you. But in practice, existing OSINT tools are powerful yet slow, complex, and fragmented across 30 different tabs . We wanted something simpler: ➡️ A single-click experience. ➡️ One username → one trusted profile card. ⚙️ What It Does Input → a single username. Crawl → Blackbird scans the open web for likely matches. Collect → a web scraper gathers relevant, publicly available data from each hit. Reason → Cohere embeddings correlate personas, detect behavioral patterns, and connect fuzzy signals. Synthesize → outputs an explainable profile card : Clean facts Source links Timestamps Per-claim confidence scores Guardrails → public data only, PII redaction, audit trail, and sensitive inferences disabled by default. 🛠️ How We Built It Pipeline architecture: Discovery → Blackbird for username enumeration and candidate gathering. Extraction → site-aware scraping of bios, handles, links, timestamps. Normalization → unify fields, dedupe items, standardize time/text. Correlation → reasoning models score cross-platform matches using: Handle similarity Cross-linked bios Writing-style cues Semantic similarity Evidence Grading → assign confidence based on independent signals + recency. Profile Card → concise summary with sources, timestamps, and caveats. 🚧 Challenges We Ran Into Entity resolution is hard → avoiding false positives requires careful scoring & explicit caveats. Noisy & incomplete data → profiles change, vanish, or contradict each other. Anti-automation & rate limits → building a polite, robust collector without brittle hacks. UX for trust → making confidence, evidence, and caveats visible without overwhelming users . 🏆 Accomplishments Built a usable “username → trusted profile card” in minutes, not hours . Evidence-first design → every claim is traceable, timestamped, and scored. Cross-platform correlation beyond exact string matches: Semantic similarity Image reuse detection A clean, analyst-friendly UI → facts first, exploration second. 📚 What We Learned In OSINT, speed is nothing without explainability . Confidence scores + links build trust —and catch mistakes early. Most value comes from normalization & correlation , not just bigger models. Ethical defaults are essential for adoption and long-term viability. 🚀 What’s Next for Deepsint Name-based discovery → privacy-respecting search by name to widen correlation. Image-based discovery → profile picture correlation layered with AI reasoning & embeddings. <div