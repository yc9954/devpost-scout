---
slug: "awwscribe"
url: "https://devpost.com/software/awwscribe"
title: "AwwScribe"
hackathon: "AI Partner Catalyst: Accelerate Innovation"
organization: "Google"
winner: true
words: 679
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# AwwScribe

> AwwScribe turns vet appointments into SOAP notes in 30 seconds. Vets just record their conversation, and our AI extracts vitals, medications, diagnoses—everything structured and ready to attest.

[Devpost](https://devpost.com/software/awwscribe) · hackathon [[AI Partner Catalyst- Accelerate Innovation]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[voice_speech]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]] [[transcript_audio]]

**stack** elevenlabs, gemini, nextjs, vertex

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for awwscribe

## Body

SOAP Notes AwwScribe Inspiration My best friend is a veterinarian, and I watched her spend 2-3 hours every evening charting, time that should've been spent resting or with family. When she told me "the paperwork is harder than the medicine," I knew there had to be a better way. With Google's Gemini 3.0 Flash (advanced reasoning), the technology finally exists to solve this. AwwScribe is my love letter to veterinarians everywhere who deserve to spend their time healing, not typing. What it does AwwScribe is an AI-powered clinical documentation assistant for veterinary practices that automatically generates professional SOAP notes from ambient conversations and helps clinic staff work more efficiently through an intelligent AI chat assistant. Core Features Live Scribe - Real-time transcription using ElevenLabs Scribe v2 with sub-100ms latency and veterinary terminology optimization SOAP Documentation - Google Gemini 3.0 Flash processes transcripts and structures the veterinarian's stated findings into organized clinical notes: Vitals as reported by the veterinarian (temperature, heart rate, respiratory rate, weight) Medications prescribed by the veterinarian (name, dosage, frequency, duration, route) Diagnoses made by the veterinarian (with codes and severity) Follow-up recommendations from the veterinarian Provider attestation AI Chat Assistant - Context-aware assistance for retrieving patient history and reference information Beautiful UX - Color-coded vitals cards, animated SOAP sections, full-screen workflows Workflow: Record → Veterinarian speaks naturally during exam → Stop → AI structures the veterinarian's findings into SOAP format → Veterinarian reviews and approves in 30 seconds Important: AwwScribe is a documentation tool that captures and organizes what veterinarians say—it does not provide diagnoses, treatment recommendations, or medical advice. All clinical decisions remain with the licensed veterinarian. How it was built Tech Stack Frontend: Next.js 16, React 19, TypeScript, Tailwind CSS, shadcn/ui, Framer Motion AI/ML: ElevenLabs Scribe v2 (real-time transcription), Google Vertex AI (Gemini 3.0 Flash) Database: Firebase Firestore (real-time patient data) Infrastructure: Vercel (deployment), Google Cloud (AI services) Architecture Authentication Flow: Server-side API route generates single-use ElevenLabs tokens (15-min expiration) to keep API keys secure Real-Time Transcription: React hook connects to Scribe v2 WebSocket with Voice Activity Detection (2-second silence threshold for segmentation) SOAP Structuring: Next.js API route sends transcript + patient context to Gemini 3.0 Flash with structured prompt engineering to organize the veterinarian's verbal findings into standard SOAP format UI/UX: Implemented responsive panels with ResizablePanelGroup, full-screen chat mode (ESC to exit), and staggered animations for SOAP sections Challenges we ran into Medical Terminology Accuracy: Initial transcription struggled with veterinary terms like "carpus," "borborygmi," "pruritus." Solved by upgrading to ElevenLabs Scribe v2's veterinary-optimized model. Structured Output Consistency: Early SOAP notes had inconsistent formatting. Implemented JSON schema enforcement with Gemini 3.0 Flash's structured generation and detailed prompt engineering to ensure consistent documentation format while preserving the veterinarian's clinical findings. Provider Control: Ensuring the system serves as a documentation assistant rather than a decision-making tool—all clinical content must originate from the veterinarian's spoken statements. Accomplishments that we're proud of ✅ Sub-100ms transcription latency - Real-time transcript display as you speak ✅ High-fidelity documentation - Accurately captures and structures veterinarian's verbal findings ✅ Beautiful, polished UX - Color-coded cards, animations, full-screen workflows that veterinarians actually want to use ✅ Time savings - Reduces documentation time from 8-10 minutes to 30-second review What we learned Technical ElevenLabs Scribe v2's Voice Activity Detection is incredibly powerful for natural conversation segmentation Google Gemini 3.0 Flash's advanced reasoning and structured output mode excels at organizing unstructured speech into standardized documentation formats The importance of clear boundaries: our AI structures what veterinarians say, it doesn't make clinical decisions Domain-Specific Veterinarians value tools that save time without removing their clinical authority Quality documentation is about organization and completeness, not AI-generated recommendations The best AI tools for healthcare are those that augment professional judgment, not replace it What's next for AwwScribe Multi-user support - Practice-wide deployment with role-based access Enhanced Review Tools - More intuitive editing and amendment workflows for SOAP notes Integration APIs - Connect with existing practice management systems Phone Documentation - Extend transcription capabilities to telephone consultations Compliance Features - Enhanced audit trails and attestation workflows for regulatory requirements <div