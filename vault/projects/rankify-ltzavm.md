---
slug: "rankify-ltzavm"
url: "https://devpost.com/software/rankify-ltzavm"
title: "Rankify"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 618
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Rankify

> 𝐓𝐮𝐫𝐧 𝐀𝐧𝐲 𝐏𝐃𝐅 𝐢𝐧𝐭𝐨 𝐚𝐧 𝐈𝐧𝐭𝐞𝐫𝐚𝐜𝐭𝐢𝐯𝐞 𝐌𝐨𝐜𝐤 𝐓𝐞𝐬𝐭 [CBT]

[Devpost](https://devpost.com/software/rankify-ltzavm) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[agriculture_food]] [[finance_payments]] [[labor_employment]]
**substrate** [[document_pdf]] [[geospatial]]
  <sub>weak: video_visual</sub>

**stack** dexiedb, gsap, indexeddb, javascript, lenis, open-source, openai, openai-compatible-apis, pdfjs-dist, tailwindcss, typescript, vercel, vite, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Home Image Inspiration My drive is full of question papers. Coaching modules, pre-boards, random PDFs at midnight. Great material — useless format. Practicing them properly meant paying test-series platforms for questions that aren't mine . All I wanted was my own papers, in a real exam interface , without a printer or a payment plan. So I built Rankify. One job: PDF in → CBT out. Free. No account. Nothing leaves your browser. What it does Three steps. That's the whole product. 1. Extract — Drop a PDF. The primary path is our public Gemini GEM : upload there, copy the JSON back, paste here. No key, no signup. Or let the built-in AI Agent read it page-by-page on any free provider — Groq, Mistral, NVIDIA, even local Ollama. Long paper? It checkpoints after every page and resumes after crashes. 2. Review — AI drafts, you approve. Every question is editable before test day. Diagrams are never AI-guessed: you drag a box on the real PDF page and that exact crop ships with the question. 3. Attempt — A genuine CBT. Timer, palette, mark-for-review, auto-save. Submit → per-section analytics instantly. Papers become plain JSON (our UniversalPaper schema) — 9 question types : MCQ, MSQ, numeric, true/false, fill-blank, match, assertion–reason, passage, long answer. Math survives as LaTeX: { "type": "numeric", "text": "Find $\\int_0^1 x^2 dx$", "answer": 0.33 } Privacy is structural, not promised: there is no backend. Papers, answers, results live in your browser's IndexedDB. How we built it Vue 3 + TypeScript + Vite , Tailwind v4 — a plain SPA on Vercel's CDN. pdfjs-dist pulls text per page; empty text layer? Auto-routes through OCR. Dexie / IndexedDB stores papers, test state, checkpoints. Provider manager : BYOK keys stay local; presets hit free tiers via an optional proxy. Custom cropper boxes diagram regions straight off the rendered page. The design is a notebook — ruled paper, washi tape, sticky notes, handwriting fonts, a pencil ink-trail cursor, and a WebGL-dithered footer that ripples under your mouse. GSAP + Lenis underneath, tuned hard (off-screen pausing, transforms only). UI speaks English, हिन्दी and Hinglish — new languages arrive via a GitHub issue form anyone can file. Open source under PolyForm Noncommercial 1.0.0 . Challenges we ran into Models invent things. Confident nonsense options, baseless answers. Fix: strict JSON schema + validation warnings + a review step no question can skip. Diagrams broke trust first. Instead of fighting hallucination and missing diagram, we removed it — manual crops from the actual PDF. Slower, but correct . Free-tier limits vs. 100-page papers. Page-chunked runs with delays and per-page checkpoints. A crash costs one page now, not eighty. Math turned to soup. Naive extraction mangles equations. The schema forces $...$ passthrough verbatim. Accomplishments that we're proud of Whole pipeline — parse, extract, review, attempt, analyze — runs client-side. Zero required servers. Nine question types behind one schema a human can actually read. Same paper on Groq today, Ollama tomorrow, whatever's free ai provider next semester. People mention the sticky notes and dither footer unprompted. The design has fans. What we learned Schema-first prompting beats clever prompting. A rigid contract catches more errors than asking nicely ever will. The UX around failure matters more than accuracy. Every paper breaks some assumption; usable means nothing fails silently. Killing features is shipping. Accounts, cloud sync, auto-diagram-detection — all cut. The demo got less shiny and the product got better. What's next More languages — community translations from the issue-form pipeline land in the switcher. Side-by-side review — question ↔ source-page jump highlighting. Portable papers — export as a single file a friend imports and attempts. Time-per-question heatmaps across attempts. - Robust-Logics across many usecases and scenerios. <div