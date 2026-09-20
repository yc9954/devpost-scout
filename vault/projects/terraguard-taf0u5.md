---
slug: "terraguard-taf0u5"
url: "https://devpost.com/software/terraguard-taf0u5"
title: "TerraGuard"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 501
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "user/government_staff"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# TerraGuard

> 9 AI agents audit corporate sustainability reports for greenwashing, compliance gaps & climate risk powered by LangGraph, RAG, and GPT-4o-mini.

[Devpost](https://devpost.com/software/terraguard-taf0u5) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[climate_energy]] [[finance_payments]]
**user** [[government_staff]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** fastapi, langraph, langsmith, llamaparse, next.js, ollama, open-meteo, openai, postgresql, pymupdf, python, qdrant, react, reportlab

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next
- built with
- try it out

## Body

Inspiration Corporate sustainability reports are notoriously hard to verify. Companies publish hundreds of pages of ESG claims with no standardized way to cross-check them against international standards like GRI, TCFD, or IFRS S2. Greenwashing is rampant, and regulators can't keep up. We wanted to build something that could read these reports the way a panel of experts would — simultaneously, rigorously, and at scale. What it does TerraGuard accepts any corporate sustainability PDF and runs it through a pipeline of 9 specialized AI agents that work in coordinated waves: Claims Extractor identifies every environmental commitment in the document with confidence scores Evidence Retriever cross-references those claims against a RAG corpus of 15 regulatory standards documents Standards Auditor checks compliance against GRI 305, TCFD, IFRS S1/S2, and IPCC AR6 Climate Risk Assessor pulls live weather and seismic data to contextualize the company's geographic exposure Equity Analyst queries World Bank indicators to surface environmental justice concerns Peer Benchmark compares performance against sector reports Scenario Modeller projects IPCC SSP-based outcomes under status quo vs. intervention Environmental Expert produces a concrete infrastructure remediation plan with cost estimates Scoring Engine synthesizes everything into a composite accountability score with a downloadable PDF/DOCX verdict The entire pipeline streams live to a React dashboard via Server-Sent Events, so users watch each agent complete in real time. How we built it The backend is a LangGraph fan-out/fan-in orchestration pipeline running 3 parallel waves of agents, each with structured Pydantic outputs and LangSmith tracing. We built a dual-collection RAG architecture on Qdrant Cloud with 1,087 vectors embedded via a local Ollama qwen3-embedding:4b model (2560 dimensions), achieving 100% retrieval accuracy across 28 test queries. The FastAPI backend streams agent events over SSE to a React + TypeScript + Tailwind frontend. Reports persist to Supabase with JSONB verdicts. Challenges we ran into Orchestrating 9 agents in parallel waves without race conditions required careful LangGraph state design. Getting consistent structured outputs from GPT-4o-mini across agents with very different schemas pushed us to invest heavily in Pydantic v2 validation. Embedding 15 dense regulatory PDFs locally with meaningful chunking — especially for tabular standards content — required a custom paragraph-aware chunker with section detection. Accomplishments we're proud of Fully working end-to-end pipeline from PDF upload to comprehensive accountability report in under 2 minutes 100% RAG retrieval accuracy on regulatory standards Live streaming dashboard that makes AI reasoning transparent instead of a black box What we learned Multi-agent orchestration at this level requires treating inter-agent state as a first-class design concern from day one. RAG quality depends far more on chunking strategy than embedding model choice. What's next Expanding the RAG corpus to cover EU CSRD and SEC climate disclosure rules Adding a public company database for side-by-side company comparison Fine-tuning a smaller model on ESG audit tasks to reduce API costs Built With Python, FastAPI, LangGraph, LangChain, GPT-4o-mini, Qdrant, Ollama, React, TypeScript, Vite, Tailwind CSS, Supabase, LangSmith, Pydantic, ReportLab, LlamaParse, PyMuPDF, Server-Sent Events, Open-Meteo API, World Bank API, USGS API Try It Out 👉 https://github.com/omarfh111/TerraGuard <div