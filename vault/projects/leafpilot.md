---
slug: "leafpilot"
url: "https://devpost.com/software/leafpilot"
title: "LeafPilot"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 492
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# LeafPilot

> LeafPilot is an AI-powered LaTeX editor, built for education. Ask about a concept, upload rough notes or record your lecture's audio, and you'll receive clean PDF results with embedded animations!

[Devpost](https://devpost.com/software/leafpilot) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[transcript_audio]] [[web_dom]]

**stack** fastapi, groq, manim, next.js, python, shadcn, tailwind, typescript, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what’s next for leafpilot

## Body

Inspiration For such a widely used typesetting platform (you could format this very blurb in it!), we were surprised that there wasn’t an editor for LaTeX with built-in AI support. We saw a clear opportunity: students and researchers often spend more time debugging formatting than focusing on content. We wanted to change that, especially for students who want to create clean, professional notes, complete with interactive diagrams and even animated visualizations. What it does Think of LeafPilot as Overleaf with Copilot , or Cursor for LaTeX . It allows you to: Generate and compile LaTeX directly in your browser. Seamlessly embed Manim (3Blue1Brown-style) animations into your documents. Upload your own resources (like text notes or even an audio recording ) and have LeafPilot structure, typeset, and enhance them into a polished PDF. In short: LeafPilot turns raw ideas into beautifully formatted, animated documents with AI as your co-pilot. How we built it Frontend : Next.js + Tailwind for speed and flexibility. Backend : Python with FastAPI to handle requests efficiently. AI Integration : Groq as the inference engine powering LaTeX generation, file summarization, mp3 transcription, and embedding-based retrieval. Gemini flash as the reasoner, deciding on agent tool calls, speeding up inference times! Extras : We connected LaTeX compilation and Manim rendering into the pipeline so everything works in-browser without the typical setup headaches. Challenges we ran into Getting LaTeX compilation and Manim rendering to work smoothly in a browser context. Managing asynchronous agent workflows (AI + compilation + file processing) without things breaking mid-stream. Designing a frontend experience that feels fast and intuitive despite the heavy lifting happening behind the scenes. Debugging… lots of debugging. Accomplishments that we're proud of Built a working prototype of an AI-powered LaTeX + Manim editor , something we couldn’t find anywhere else. Successfully integrated multimodal input (notes, documents, audio) into the pipeline. Learned to wrangle AI outputs into valid, compilable LaTeX ! Showed that it’s possible to merge the power of agentic workflows with a typesetting tool students actually want to use. What we learned When working with agentic workflows , it’s critical to design with them in mind from the very beginning. Retrofitting agents into an existing pipeline is messy and inefficient. LaTeX is powerful but extremely sensitive AI outputs need guardrails, validation, and retries to ensure documents actually compile. We got hands-on experience balancing usability (smooth UI/UX) with technical depth (AI, rendering, pipelines). And most importantly: the line between an AI-powered helper and a frustrating black box is thin, design choices matter a lot. What’s next for LeafPilot Expanding agentic workflow support to make the AI more autonomous and context-aware. Adding real-time collaborative editing (think “Google Docs meets Overleaf with AI”). More export options : slides, interactive HTML, and richer animation controls. Improved error handling so users spend less time chasing LaTeX bugs and more time creating. Ultimately, we want LeafPilot to become the go-to AI-powered typesetting environment for students, researchers, and creators. <div