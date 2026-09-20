---
slug: "vidyachitra"
url: "https://devpost.com/software/vidyachitra"
title: "VidyaChitra"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 680
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# VidyaChitra

> AI study companion that turns any Indian school textbook PDF into a summary, animated video, audio narration, and board-pattern exam questions — in the student's own regional language, instantly.

[Devpost](https://devpost.com/software/vidyachitra) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** docker, fastapi, gemini-tts, google, google-cloud, google-gemini-2.5-flash, manim, pymupdf, python, react, sse, tailwindcss, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next

## Body

Inspiration Engine How it looks Tech Flow Tech Stack Impact What's Next Inspiration India has over 250 million school students studying in regional languages — Kannada, Hindi, Tamil, Telugu, Marathi. Yet almost every EdTech tool is built for English-speaking students. A Class 10 student in rural Karnataka studying from a Kannada textbook has no YouTube explainer, no AI tutor, no animated diagram — just a dense PDF and an overworked teacher. We built VidyaChitra because that student deserves the same quality of learning aid as anyone else. The name means "picture of knowledge" in Sanskrit. What It Does VidyaChitra takes any school textbook chapter PDF and automatically generates a complete study kit in the student's own language: Chapter summary streamed to the screen within seconds Animated explainer video — AI writes a Manim animation script for the key concept, rendered as an MP4 with labels in the student's language Audio narration — a teacher-style spoken explanation synthesised using Gemini TTS Board-pattern exam questions — MCQs and short-answer questions framed exactly as they appear in Karnataka SSLC, CBSE, Maharashtra SSC, or Tamil Nadu board exams Grounded AI chat — answers questions strictly from the chapter content, no hallucinations No configuration needed. Upload a PDF — language, board, and class level are all detected automatically. How We Built It Backend : Python 3.11 + FastAPI. All AI is powered by Google Gemini 2.5 Flash via the google-genai SDK — a single API key drives everything. PDF Understanding : We pass the raw PDF bytes to Gemini with mime_type="application/pdf" (native PDF mode). Gemini reads all pages, Indic scripts, diagrams, and formulas in one API call — no OCR, no page-by-page image rendering. Video Pipeline (two-step) : Gemini reads the chapter summary (already in the student's language) and writes a structured 3-step JSON concept script with controlled text lengths Gemini writes a Python Manim scene from that script, which is rendered to MP4 Audio : Gemini writes a 200-word spoken narration, then Gemini TTS synthesises it. Gemini returns raw 16-bit PCM at 24 kHz which we wrap in a WAV container using Python's wave module. Streaming : All three pipelines (video, audio, questions) run concurrently via asyncio.create_task . Results are pushed to the frontend via Server-Sent Events the moment each one finishes. Frontend : React 18 + TypeScript + Vite + TailwindCSS. A custom useSSEStream hook manages the EventSource lifecycle. Challenges We Ran Into Indic text in Manim on Windows : Cairo (Manim's renderer) crashes when rendering Kannada/Hindi/Tamil glyphs at partial opacity — which is exactly what FadeIn() and Write() do (they interpolate opacity 0→1). The fix was to use self.add() instead, which places text at full opacity instantly. Shapes still use Create() for visual animation. Language detection : Gemini returns language names in free-form ("Kannada", "kn", "kannada") rather than BCP-47 codes. We built a normalisation lookup table to map these to kn-IN , hi-IN , etc. before any downstream use. Video in wrong language : Key concepts extracted from PDFs are always returned in English by Gemini. We solved this by grounding the video script prompt in summary_text (which is in the textbook's own language) rather than key_concepts . SSE connection drops : Manim renders take 60–180 seconds. Browsers drop silent SSE connections. We added a 15-second queue timeout that yields a ping keepalive event, keeping the connection alive throughout the render. What We Learned Gemini's native PDF mode is dramatically better than OCR for Indic-script textbooks — it handles complex Unicode, embedded fonts, and diagram context in a single pass Two-step AI pipelines (structured script → code generation) produce far more reliable output than single-step "generate everything" prompts Cairo renders Indic Unicode at full opacity perfectly, but crashes at partial opacity — a platform-specific quirk that took significant debugging to isolate What's Next Offline mode — cache generated materials for no-internet study More Indian state boards — Andhra Pradesh, Telangana, West Bengal More languages — Odia, Punjabi, Gujarati, Bengali Voice chat — speak questions to the AI tutor in regional languages Teacher dashboard — bulk upload entire textbooks, generate lesson plans <div