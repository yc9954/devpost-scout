---
slug: "csgh5"
url: "https://devpost.com/software/csgh5"
title: "StudyForgeAI"
hackathon: "CS Girlies November Hackathon - Make Learning Cool Again! "
organization: "Computer Science Girlies"
winner: true
words: 484
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
---

# StudyForgeAI

> Turn PDFs, videos, and articles into one perfect study guide in an instant.

[Devpost](https://devpost.com/software/csgh5) · hackathon [[CS Girlies November Hackathon - Make Learning Cool Again-]]

## Facets

  <sub>weak: retrieval_grounding</sub>
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[transcript_audio]]

**stack** fastapi, javascript, material-ui, pymupdf, python, react, render, tailwind, trafilatura, uvicorn, vercel, vite

## Body

StudyForgeAI homepage Cline prompt #1 Cline prompt #2 Cline prompt #3 Cline prompt #4 Cline prompt #5 Cline prompt #6 🌟 Inspiration Students juggle PDFs, articles, YouTube lectures, and scattered notes. When exams hit, we waste hours switching between sources, re-reading duplicates, and struggling to build structured notes. We wanted something that automatically understands, organizes, and synthesizes information across formats. That became StudyForgeAI. 🚀 What StudyForgeAI Doe StudyForgeAI turns multiple sources into a polished, unified study guide. Users can upload: PDFs Web articles YouTube video links Raw text The system extracts content, removes duplicates, organizes topics, and generates a clean study guide with summaries, key points, and a table of contents. It helps students save time and reduce overwhelm. 🛠️ How We Built It 🔍 Multi-Source Extraction (Phase 1) A robust extraction engine with detailed logging and per-source error isolation. PDFs: Page-by-page PyMuPDF extraction Whitespace normalization Web Articles: Trafilatura main-content detection YouTube: Regex-based ID detection (works for any format) Multi-language transcripts Graceful handling of private or caption-disabled videos Raw Text: Sanitization and support for structured notes 🧩 Consolidation and Normalization (Phase 2) All extracted content is merged into a single unified document with: Consistent paragraph spacing Whitespace cleanup Traceability via a unique request_id 🧠 AI Pipeline (Phase 3 and 4) Topic Extraction and Deduplication (Gemini 2.5 Flash Lite) Identifies all topics Keeps only unique content Removes exact and near-duplicate phrases Groups related information under structured topics Outputs clean JSON Built-in safeguards: Rate limit handling Exponential backoff Intelligent retry delays Study Guide Generation A single API call produces: Overview Topic summaries Key points Metadata such as topic count, guide type, and content length The system adapts automatically to concise, standard, or comprehensive guides based on input size. 📝 Markdown Formatting (Phase 5) Automatic table of contents Clean layout with headers and section dividers Emoji-based section hierarchy Smooth frontend rendering with Material UI 💻 Frontend React 19, Vite, Material UI, Tailwind Axios interceptors Dark mode and responsive UI Unified dashboard for all upload types 🖥️ Backend FastAPI and Uvicorn PyMuPDF, Trafilatura, YouTube Transcript API Centralized logging and extraction pipelines ⚠️ Challenges Disabled or blocked YouTube captions API rate limits Ensuring deduplication does not remove important context Coordinating extraction, cleaning, AI processing, and formatting seamlessly These challenges led to robust fallback mechanisms and precise prompt engineering. 🏆 Accomplishments Reliable extraction across all source types Custom AI pipeline for topic detection Automatically polished, structured study guides Improved our own studying while testing 📚 What We Learned Integrating advanced LLMs into real-world products Rapid full-stack development Effective collaboration in a fast-paced environment 🚀 What is Next User Accounts: saved guides, history, personalization RAG Powered Pipeline (ChromaDB): larger inputs, faster guides, persistent learning New Learning Tools: AI generated flashcards Personalized study plans Quizzes Progress dashboards Collaborative studying Our long term vision is to build a complete AI study companion that helps students understand, remember, and master what they learn. <div