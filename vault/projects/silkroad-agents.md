---
slug: "silkroad-agents"
url: "https://devpost.com/software/silkroad-agents"
title: "SilkRoad Agents"
hackathon: "ERNIE AI Developer Challenge"
organization: "Baidu"
winner: true
words: 133
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "user/researcher"
  - "substrate/document_pdf"
---

# SilkRoad Agents

> Three bilingual agents turn Chinese market documents into reviewable investment memos.

[Devpost](https://devpost.com/software/silkroad-agents) · hackathon [[ERNIE AI Developer Challenge]]

## Facets

**mechanism** [[vision_ocr]]
  <sub>weak: multi_agent</sub>
**user** [[researcher]]
**substrate** [[document_pdf]]
  <sub>weak: geospatial</sub>

**stack** camel-ai, docker, ernei-4.5, fastapi, javascript, nextjs, paddleocr, python

## Body

Chinese market research is fragmented across filings, reports, and bilingual sources. Analysts spend substantial effort extracting text, reconciling evidence, and turning it into a consistent memo. SilkRoad Agents coordinates three focused roles: Scout gathers and extracts source material, including Chinese PDFs through PaddleOCR. Analyst structures market, company, and risk evidence with ERNIE 4.5. Synthesizer turns the collected findings into a reviewable investment memo. CAMEL-AI manages role-based collaboration. A FastAPI backend streams progress with server-sent events, while the Next.js interface keeps the source-to-memo workflow visible. The implementation also handles asynchronous HTTP requests, PaddleOCR API differences, and model-response normalization so failures remain inspectable. The output is a structured research aid, not a guarantee of financial accuracy or investment performance. Analysts remain responsible for validating sources and conclusions before using the memo in a decision. <div