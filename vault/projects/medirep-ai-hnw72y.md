---
slug: "medirep-ai-hnw72y"
url: "https://devpost.com/software/medirep-ai-hnw72y"
title: "MediRep-AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 274
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/video_visual"
---

# MediRep-AI

> AI-native medical intelligence for fast, grounded decisions across chat, vision, and voice.

[Devpost](https://devpost.com/software/medirep-ai-hnw72y) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[finance_payments]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[video_visual]]

**stack** fastapi, gemini, groq, next.js, python, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- what’s next

## Body

thumbnail thumnail logo Inspiration Clinical decisions are often made under time pressure, with fragmented sources and noisy inputs (voice notes, blurry pill images, incomplete patient history). We wanted to build system that feels as fast as a conversation but behaves like a disciplined medical copilot. What it does MediRep AI is a multimodal medical intelligence platform that supports: Context-aware chat with strict operating modes (general, insurance, mechanism-of-action, pharma rep) Pill identification from images Prescription OCR and structured extraction Drug interaction analysis with actionable clinical guidance Grounded retrieval from large drug datasets and trusted medical sources How we built it We built a Next.js + FastAPI architecture with Gemini as the core reasoning engine: FastAPI orchestrates chat, vision, OCR, interaction, and context services Gemini handles multimodal understanding + clinical response generation Turso + Qdrant power hybrid retrieval for drug and medical context Supabase handles auth, sessions, chat persistence, and user workflows Fallback/guardrail paths improve reliability under timeout or provider issues Challenges we faced Balancing speed with safe, grounded outputs Handling ambiguity in pill images and OCR text Enforcing strict mode boundaries to reduce off-topic responses Designing clean fallbacks without breaking UX What we learned Multimodal AI is strongest when constrained by retrieval + structured context Prompt quality matters, but orchestration quality matters more Safety is not one feature; it is a system design choice What’s next Stronger citation UX with source freshness indicators Better regional protocol packs and local-language support Deeper pharmacist collaboration workflows and outcome tracking For interaction severity, we also expose a transparent PK-style estimate: $$ R = 1 + \frac{[I]}{K_i} $$ to communicate why a risk level is classified as minor/moderate/major. <div