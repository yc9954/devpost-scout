---
slug: "subrevision"
url: "https://devpost.com/software/subrevision"
title: "SubRevision"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 735
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# SubRevision

> Upload. Learn. Revise. Repeat.

[Devpost](https://devpost.com/software/subrevision) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[deterministic_policy]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[education]] [[scientific_research]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** fastapi, groq, nextjs, python

## How they structured the write-up

- 📘 project story
- ✍️ project description - what you built and why it matters
- 👥 team members
- 🤖 ai tools disclosure

## Body

📘 Project Story Inspiration SubRevision was born from a personal need: quickly turning lecture PDFs into usable study materials. The goal was simple — reduce friction between reading course material and actively learning it. The result is an AI-first assistant that converts PDFs into summaries, quizzes, flashcards, mind maps and study plans so students can focus on learning instead of formatting. What I learned Building a full-stack AI product end-to-end (FastAPI backend + Next.js frontend) and keeping it lightweight. Practical vector/embedding workflows: chunking text, generating embeddings, storing/hot-loading vectors. Working with multiple LLM providers and handling quota/caching issues. Robust UI patterns for interactive study tools (click-to-reveal answers, flip cards, tree views). Debugging real-world problems: CORS, font/import ordering, Turbopack caches, and parsing AI outputs reliably. How it was built Backend (FastAPI): handles PDF upload, text extraction (PyPDF2), chunking, embedding generation, and orchestration of AI prompts. Responses are validated and parsed to structured JSON before returning to the frontend. Vector store: lightweight JSON-based storage for embeddings (easy local dev). The architecture allows replacing storage with a production vector DB later. AI layer: initially integrated Gemini/Groq; implementation is modular so providers can be swapped based on quota/performance. Frontend (Next.js + Tailwind): pixel-inspired UI with interactive components — quiz cards, flippable flashcards, and expandable mind map views. All API interactions include clear loading/error states and graceful fallbacks. Challenges & how they were solved Quota limits: swapped providers and implemented a modular AI adapter so switching is easy. Backend returned AI outputs as text blobs — fixed by enforcing strict JSON-only responses and parsing AI outputs server-side. Frontend showed raw JSON: implemented structured renderers (quiz cards, flashcards, mind maps) and state resets on tab change. Dev tooling issues (Next/Turbopack cache, CSS @import rules): fixed by clearing caches and moving @import to top or using system fonts. PDF edge cases (image-only PDFs): added empty-document detection and clear error messages. ✍️ Project Description - What you built and why it matters SubRevision is an AI-powered study assistant that transforms static PDF documents into practical learning resources — summaries, searchable sections, quizzes, flashcards, mind maps, and day-by-day study plans. The project addresses a common pain point for students and professionals: turning passive reading into active learning. Instead of manually extracting notes, creating question sets, or designing study schedules, SubRevision automates those steps and presents them in an interactive UI that encourages retrieval practice and spaced review. At its core SubRevision extracts text from PDFs, splits content into context-aware chunks, creates embeddings for semantic lookup, and uses an LLM backend to generate structured outputs (quizzes, flashcards, summaries, etc.). This pipeline makes it easy to ask context-specific questions and receive grounded answers, which is particularly useful for long technical documents, lecture notes, and research papers. The result is a faster feedback loop from content → comprehension → practice. Why it matters: active recall and regular testing are proven learning techniques; SubRevision lowers the barrier to apply them by automating resource creation. For instructors, it speeds preparation of study materials; for students it reduces the time between reading and effective study. The design emphasizes privacy and local-first development (lightweight JSON vector store, optional switch to production vector DB), modular AI adapters so providers can be swapped when quotas or costs change, and an accessible pixel-inspired UI. SubRevision is built to be extendable: add user accounts, multi-document libraries, or alternative models without reworking the pipeline. 👥 Team Members Vansh Agarwal Atharva Katiyar 🤖 AI Tools Disclosure SubRevision uses the following AI tools and services: ChatGPT — used for high-level research, brainstorming prompts, and guidance on user-facing language and feature decisions. Primarily used to iterate on UX text, task breakdowns, and design choices. Claude — used to assist with refactoring and removing redundant code, reviewing prompt structure, and improving code clarity in complex backend functions. Groq API — used as the main inference provider for generation tasks (summaries, quizzes, flashcards, mind maps, study plans). Groq handles the LLM inference calls; prompts are carefully constrained to return well-formed JSON for reliable parsing. How AI is used in the product: Content generation (summaries, quizzes, flashcards, mind maps, study plans) is produced by the LLM using document context retrieved from embeddings. A deterministic parsing layer enforces JSON-only responses so the frontend can render structured interactive components instead of raw text. AI is used as a productivity assistant during development (research, code cleanup, prompt engineering), not for storing or exposing user secrets. <div