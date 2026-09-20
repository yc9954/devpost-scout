---
slug: "echo-health"
url: "https://devpost.com/software/echo-health"
title: "Echo Health"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 597
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/medical_record"
  - "substrate/transcript_audio"
---

# Echo Health

> Echo Health listens to patient visits and generates notes and referrals automatically. Less paperwork, smoother transitions between providers.

[Devpost](https://devpost.com/software/echo-health) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[health_clinical]]
  <sub>weak: mental_health</sub>
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[medical_record]] [[transcript_audio]]
  <sub>weak: structured_db</sub>

**stack** arize, bytedance, livekit, next.js, postgresql, supabase, typescript

## Body

LOGO 🩺 Echo Health AI-Powered Ambient Clinical Documentation — transforming patient encounters into comprehensive, compliant medical records in real time. Built for NexHacks using Next.js, Supabase, LiveKit, and OpenAI. 💡 Inspiration Healthcare professionals spend over (2+) hours per day on documentation — time that could be spent with patients. Nurses manually transcribe conversations, doctors review mountains of paperwork, and administrative burden leads directly to burnout. We asked a simple question: what if AI could handle documentation while clinicians focus on care? Echo Health was born from the vision of ambient intelligence in healthcare — an AI assistant that listens, understands, and documents in real time so medical staff can be fully present with their patients. 🎯 What It Does Echo Health is a comprehensive ambient clinical documentation platform that supports nurses, doctors, and patients throughout an encounter. For nurses, Echo Health provides real-time transcription using LiveKit, smart clinical analysis that suggests follow-up questions, instant draft SOAP notes, automated ICD-10 and CPT billing code detection, one-click doctor assignment, and AI-drafted specialist referral letters ready for review. For doctors, Echo Health offers a patient dashboard with urgency filtering, consolidated encounter review, and downloadable PDF reports containing SOAP notes, billing codes, and visit summaries. For patients, Echo Health generates plain-language visit summaries with appropriate disclaimers and optional text-to-speech narration for accessibility. All AI-generated content is clearly labeled as DRAFT and is intended to assist — not replace — clinical judgment. 🛠️ How We Built It Echo Health operates as a real-time transformation pipeline: Live Audio → Speech Transcription → Clinical Field Extraction → Structured Clinical Artifacts Live Audio→Speech Transcription→Clinical Field Extraction→Structured Clinical Artifacts LiveKit captures ambient audio during encounters. Supabase Edge Functions process transcripts in real time, while OpenAI GPT-4 extracts clinical fields, drafts SOAP notes, generates referrals, and produces visit summaries. Supabase Realtime subscriptions ensure all dashboards update instantly as the conversation unfolds. Final documentation can be exported as clean, multi-page PDFs. 🧩 Tech Stack Frontend: Next.js 14 (App Router), TypeScript, Tailwind CSS, Framer Motion Backend: Supabase (PostgreSQL, Edge Functions, Realtime, Storage) Real-Time Audio: LiveKit transcription agent AI / ML: OpenAI GPT-4 for clinical analysis and documentation PDF Generation: Custom streaming PDF builder Authentication: Supabase Auth with role-based access (Nurse / Doctor) 🚧 Challenges We Faced Coordinating real-time transcription, AI processing, and UI updates required careful state management to avoid lag or duplication. We also needed to ensure healthcare-safe AI behavior by labeling outputs as drafts and avoiding definitive diagnoses or treatment recommendations. Building reliable, multi-page clinical PDFs under hackathon time constraints and creating a demo-friendly authentication flow while maintaining proper database validation were additional challenges. 🏆 Accomplishments We built a full-stack healthcare platform from zero to demo-ready within a hackathon timeframe. Echo Health supports true ambient documentation with live updates across multiple panels, compliance-first AI outputs, and complete nurse-to-doctor handoff workflows with billing and referrals integrated. 📚 What We Learned This project taught us the importance of prompt engineering in healthcare contexts, how to design real-time systems using Supabase and LiveKit, how to build responsible AI tools under compliance constraints, and why intuitive UX is critical in high-pressure clinical environments. 🚀 What’s Next Planned improvements include hands-free voice commands, multi-language transcription, direct EHR integrations (Epic, Cerner), mobile bedside documentation, analytics on documentation efficiency, and full HIPAA compliance audits. ⚠️ Compliance Notice Echo Health is designed with healthcare compliance in mind. All AI-generated content is labeled as DRAFT, includes “not medical advice” disclaimers where appropriate, and is protected through role-based access controls. This project is a hackathon prototype; production deployment would require HIPAA certification and formal security audits. <div