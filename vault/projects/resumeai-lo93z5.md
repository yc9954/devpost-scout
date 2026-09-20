---
slug: "resumeai-lo93z5"
url: "https://devpost.com/software/resumeai-lo93z5"
title: "ResumeAI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 539
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# ResumeAI

> Drop any link. Get a resume tailored to your target company. Get a roadmap to get hired.

[Devpost](https://devpost.com/software/resumeai-lo93z5) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** amazon-bedrock-converse-api, amazon-nova-lite, firebase-authentication, next-intl, next.js-15, prisma-orm, react, sqlite, tailwind-css, typescript, zod

## How they structured the write-up

- inspiration
- what i learned

## Body

Inspiration As a 6-year Android developer preparing for my next career move, I spent over 10 hours writing a single resume — and another 2 hours tailoring it for each company. I realized every job seeker faces the same painful process: manually rewriting resumes, guessing what recruiters want, and never knowing if your resume actually matches the job requirements. I wanted to build something that eliminates this entirely. What if AI could read your GitHub, understand your skills, and generate a company-optimized resume in 30 seconds? ## What it does ResumeAI is an AI-powered resume builder that: Drop any link — Paste a GitHub URL and AI instantly analyzes your repositories, tech stack, and project history Company-tailored resume — Paste a job description, and Nova AI generates a resume matched to that specific company's requirements Acceptance roadmap — Get a skill gap analysis, learning paths, and interview preparation guide to actually land the job The entire flow takes under 30 seconds, replacing 10+ hours of manual work. ## How I built it ### Architecture AI Engine : Amazon Nova Lite via Bedrock Converse API with Bearer Token Authentication Frontend : Next.js 15 (App Router) + TypeScript + Tailwind CSS Auth : Firebase Authentication Database : SQLite + Prisma ORM (lightweight, single EC2 deployable) i18n : Full Korean + English support with next-intl ### Multi-pass AI Generation Instead of a single AI call, ResumeAI uses a 2-pass generation pipeline : Pass 1 : Analyze GitHub profile → extract structured data (skills, projects, experience) Pass 2 : Generate company-optimized resume from structured data This approach significantly improves accuracy and reduces hallucination. ### Anti-Hallucination Validation Nova Lite tends to fabricate metrics (e.g., "10,000 monthly active users") when none exist in the source data. I implemented strict prompt rules: COPY EXACTLY rules for names, URLs, and repository data Explicit prohibition of fabricated metrics (MAU, downloads, revenue) English-only output enforcement to prevent language mixing ## Challenges I faced ### 1. Korean Text Corruption Amazon Nova Lite garbles Korean text when prompts are written in Korean (e.g., "퓨쳐다임" → "이주도"). Solution : Write ALL prompts in English with explicit copy-preservation rules. Korean text in the input is preserved perfectly when the prompt itself is English. ### 2. Hallucinated Metrics Nova would confidently generate fake statistics like "Monthly active users: 1,000" for hobby projects with zero users. Solution : Added NEVER fabricate metrics rules and OVERRIDE ALL PREVIOUS LANGUAGE RULES blocks to suppress this behavior. ### 3. Bedrock API Integration The Bearer Token API uses the Converse endpoint ( /model/{modelId}/converse ), not the Invoke endpoint. Authentication uses Authorization: Bearer {token} header with 12-hour token expiry. Documentation was sparse, so this required significant trial and error. What I learned Prompt engineering for accuracy matters more than model size — Nova Lite with well-crafted prompts outperforms larger models with vague prompts Multi-pass generation is essential for structured output — single-pass calls produce inconsistent results AI hallucination is a feature-level problem , not just a model problem — you need validation at the application layer Bedrock Converse API is powerful but under-documented for Bearer Token auth ## What's next LinkedIn and YouTube profile analysis support PDF resume export with professional templates Real-time job market matching Mobile app (Flutter) <div