---
slug: "polyterminal"
url: "https://devpost.com/software/polyterminal"
title: "Irreduce"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 165
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
---

# Irreduce

> Remove what never mattered

[Devpost](https://devpost.com/software/polyterminal) · hackathon [[NexHacks]]

## Facets

  <sub>weak: retrieval_grounding</sub>
**substrate** [[document_pdf]]
  <sub>weak: video_visual</sub>

**stack** chroma, css, fastapi, huggingface, pillow, pydantic, python, typscript, uv, uvicorn

## Body

Irreduce Irreduce is a token-aware prompt compressor for long-context inputs. It heavily compresses text input while maintaining performance and information density. Audience Irreduce has a massive potential audience as is it can help tens of millions or hundreds of millions of users across all industries using search, support, agents, RAG, and any other intelligent systems incorporating LLMs Model The Irreduce model compresses tokens by: Splitting the document into spans and compute BM25 (classic IR scoring) to measure how well each span matches the context Innovatively converting text tokens into image tokens containing, compressing semantic meaning Computing a TF‑IDF similarity between each span and the full document (coverage/centrality). Rewarding rare terms (IDF density) and lexical diversity (information density). Selecting spans under a token budget and grouping them into windows to ensure coverage across the document Applying a redundancy penalty (Jaccard overlap) to avoid near‑duplicates. Challenges The primary challenges we faced includes balancing compression vs performance, and generalizing to different domains including math and web info. <div