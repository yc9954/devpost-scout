---
slug: "crosscheck-dxn3v5"
url: "https://devpost.com/software/crosscheck-dxn3v5"
title: "crosscheck"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 498
team_size: 1
has_repo: false
has_live: true
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

# crosscheck

> Real-time streaming Q&A with vision OCR, 6-stage JSON recovery, and personality training from chat logs

[Devpost](https://devpost.com/software/crosscheck-dxn3v5) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** gemini, pdfjs-dist, react, supabase, tailwindcss, typescript, vite, vitest

## How they structured the write-up

- the problem
- what we built
- how we built it
- key challenges & solutions
- what we learned
- stack

## Body

UI interaction Dashboard The Problem Most study tools are passive. You answer multiple-choice questions, get a score, and move on. They don't expose what you actually know versus what you think you know. Real understanding shows up under pressure in exams, in conversation, and when someone asks a follow-up. CrossCheck interrogates you the way an examiner would. Conversationally. With follow-ups. With escalating rigor. What We Built A conversational knowledge audit tool that: Extracts your knowledge —Upload notes (PDF, text, images). Gemini Vision reads them and maps topics automatically. **Audits your life—An AI examiner walks through each topic in real-time conversation. Mode escalates as you progress: Friend → Tutor → Instructor → Examiner. The pressure matches your confidence. Finds your gaps —Every topic gets classified as Strong / Weak / Needs Revisit with evidence. Weak topics expand to show the exact concepts to study. **Surface answers—One tap gives you the correct answer + explanation if you're stuck. Topic marks as weak automatically. No penalty, just honesty. Repeats on demand —Re-run sessions on the same notes in one click. How We Built It Frontend: React 19 + TypeScript + Vite for fast iteration and type safety. AI: Google Gemini 2.5 Flash with streaming (via generateContentStream ). Handles both text understanding and multi-image vision OCR in a single call. Auth & Storage: Supabase for user auth + session reports stored in localStorage (last 20 sessions persisted). Robustness: A 6-stage JSON recovery pipeline to handle Gemini's mid-stream truncation without restarting sessions. Direct parse → clean formatting → slice recovery → structure repair → fallback truncation → regex extraction. UX polish: Full light/dark theming with CSS variables. Optional personality mode (trains from exported chat logs to match speech patterns in Friend mode). Key Challenges & Solutions Challenge 1: Streaming JSON truncation Gemini truncates midstream when outputting structured data. Standard SDK-level parsing fails. We built a 6-stage recovery pipeline that cleans, repairs, and extracts fields progressively instead of failing fast. Challenge 2: Personality mode without overtraining We wanted persona customization but didn't want users to upload 100 chat logs for marginal gain. Solution: Extract speech patterns, phrases, and humor style from a single exported chat log via Gemini itself. Gate it (PIN + email) so it stays an opt-in feature. Challenge 3: Multi-format input (PDF + text + images) Different formats require different extraction strategies. Solution: Single Gemini Vision call with inline base64 for all formats. No separate endpoints, no sequential processing. Fast and unified. What We Learned Streaming is worth it. Batch processing feels slow for examiners. Stream every call. JSON recovery beats retries. When Gemini truncates, restarting the conversation is user-facing friction. Defensive parsing on the client keeps the session alive. Personality is a toggle, not mandatory. Most users want the core audit. Personality should enhance, not complicate onboarding. Escalating difficulty mirrors real learning. Friend → Examiner mode progression isn't just UX flavor—it's pedagogically sound. Pressure reveals gaps. Stack React 19, TypeScript, Vite, Google Gemini 2.5 Flash, Supabase, pdfjs-dist, and TailwindCSS <div