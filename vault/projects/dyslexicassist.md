---
slug: "dyslexicassist"
url: "https://devpost.com/software/dyslexicassist"
title: "DyslexicAssist"
hackathon: "NextStep Hacks 2025"
organization: "HackAlphaX"
winner: true
words: 649
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# DyslexicAssist

> Limitless reading, anywhere.

[Devpost](https://devpost.com/software/dyslexicassist) · hackathon [[NextStep Hacks 2025]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[accessibility]] [[education]] [[health_clinical]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[video_visual]]

**stack** expo.io, github, googlevisionapi, json, llm, node.js, ocr, openaiapi, react-native, typescript, visual-studio

## How they structured the write-up

- inspiration
- what i learned
- how i built it
- challenges i faced

## Body

DyslexicAssist: Turn Any Page Into Your Page Inspiration DyslexicAssist grew from seeing bright students lose time, confidence, and independence at the moment of need —staring at a printed worksheet, a dense paragraph, or a menu they couldn’t easily decode or adapt. Late or missed identification (broad dyslexic traits ≈15–20%, strict diagnoses ≈3–7%) leaves a large population under-supported. I wanted a single tool that removes three recurring barriers simultaneously : Format Access – physical print vs. customizable screen. Visual Crowding – tightly packed letters/lines that slow decoding. Linguistic Complexity – sentences and vocabulary that overload working memory. Instead of forcing users to juggle multiple apps (scanner → reader → TTS → simplifier), DyslexicAssist fuses them into one continuous capture-to-comprehension flow. What I Learned Product & Accessibility Design Evidence matters: increased letter spacing can reduce visual crowding for some readers—so flexibility > prescribing a single “dyslexia font.” Minimal, consistent navigation (large feature tiles + bottom bar) reduces search time and cognitive load. Providing optional color/phoneme cues (with non-color fallback like underline/bold) respects diverse perceptual preferences and accessibility guidelines. Engineering & Architecture Component isolation in React Native + Expo sped iteration: Scanner, Adaptive Reader, TTS Karaoke, and Summarizer each evolved independently but compose cleanly. Lightweight personalization (multi-armed bandit over discrete layout settings gated by comprehension) is a pragmatic early alternative to heavy ML. Retrieval-Augmented Generation (RAG) significantly improves trust—grounded prompts reduced hallucination risk versus naive summarization. Process & Iteration Early scope trimming (e.g., static AR snapshot before continuous tracking) preserved reliability. Instrumenting words-correct-per-minute (WCPM) and comprehension first gave objective signals to judge whether UI tweaks actually helped. Rapid cycles: implement → micro user test → measure WCPM / replay counts → adjust; far more productive than speculative polishing. How I Built It Tech Stack Overview Frontend: React Native + Expo (cross-platform, hot reload). Vision Layer: Google Vision Document Text Detection → structured blocks/paragraphs. Post-Processing: Perspective (homography) correction, hyphen merge, line/paragraph reconstruction, canonical text string. Adaptive Layout Engine: Applies user-selected font (e.g., Lexend), letter & line spacing, background tint; computes new line wraps. Smart Scanner (AR Re-flow): Captures image → OCR → reflow → overlays accessible text back onto the page region. TTS Karaoke: TTS audio + word timing metadata → synchronized word (and optional phoneme) highlighting; tap-to-repeat & adjustable speed. Simplify & Summarize: Retrieval chunking (semantic embeddings) feeds a grounded prompt to OpenAI gpt-4o-mini to produce grade-level rewrite + concise bullet summary; entity/number diff check for fidelity. Personalization Metrics: Session WCPM, comprehension quiz score, replay counts, setting combination ID → stored locally; bandit recommends better setting bundles over time. Storage: Local async store caches user settings, recent scans, simplified variants for offline continuity. Key Data Flow Camera Capture → OCR & Cleanup → Canonical Text → (a) Adaptive Reader (live metrics) (b) Summarizer (RAG) (c) TTS Alignment → Unified Output / Dashboard Challenges I Faced Challenge Impact Risk Resolution / Lesson Debated “one magic dyslexia font” myth Could mislead design & limit personalization Implemented adjustable parameter set (font, spacing, tint) + data-driven recommendations. OCR variability (lighting, perspective, hyphenation) Fragmented text → poor summaries & timing Added homography correction, artifact cleanup, confidence gating, and line reconstruction. Latency (OCR + LLM) in a single flow User drop-off during “processing” Parallelized preprocessing; showed progressive status; cached previous layout & settings. Avoiding hallucinated simplifications Inaccurate assistance undermines trust Adopted RAG grounding + entity/number diff check + low-temperature prompts. Balancing speed vs comprehension Risk of optimizing for speed alone Coupled WCPM logging with a post-read comprehension quiz; bandit discards high-speed / low-comprehension arms. Feature Creep (continuous AR tracking, gaze metrics) Diluted polish within 1-week window Enforced MVP: static snapshot AR first; backlog future enhancements. Highlight Accessibility (color dependence) Excluding color-blind or contrast-sensitive users Dual signals (color + underline/bold); optional phoneme coloring toggle. Cost & Offline Concerns Reliance on cloud APIs for core flows Designed modular abstraction to later swap in on-device OCR / distilled summarizer models. <div