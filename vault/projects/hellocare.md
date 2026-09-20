---
slug: "hellocare"
url: "https://devpost.com/software/hellocare"
title: "Hellocare"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1037
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Hellocare

> Left the doctor confused or worried you forgot something? Your grandparents probably have. Hellocare schedules, explains, and turns paperwork into clear next steps, so you focus on health, not stress.

[Devpost](https://devpost.com/software/hellocare) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]] [[transcript_audio]] [[video_visual]]

**stack** assemblyai, claude, firebase, nextjs, openai, react, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hellocare

## Body

Onboarding Step 1 Onboarding Finish Onboarding Step 3 Onboarding Step 2 Onboarding Start Start Recording Conversation Summary Recording Continue Conversation Retry Conversation Visit Summary Chat Home Inspiration When my grandpa’s memory loss started to progress, doctor’s visits became overwhelming. He couldn’t remember what the doctor said, what medications changed, or what he was supposed to do next. My family tried to fill in the gaps, but between rushed appointments, medical jargon, and dense discharge paperwork, critical details slipped through the cracks. This isn’t unique to us. Around 82% of older adults say the healthcare system isn’t prepared to meet their needs (Source 1), and nearly 1 in 4 seniors report avoiding care because it’s confusing or hard to navigate (Source 2). For patients with cognitive decline, that kind of friction isn’t just frustrating, it’s also dangerous. Missed instructions can mean missed medications, missed follow ups, or in the worst case, worsening health. Hellocare was built because of that reality. We created a healthcare copilot that manages the entire doctor’s visit lifecycle: we schedule appointments, capture and explain visits, and turn complex paperwork into clear, structured next steps. That way, patients with memory challenges and their families don’t have to rely on memory recall alone. This isn’t just about efficiency. It’s about protecting dignity, reducing stress, and ensuring that no family navigating dementia has to guess what comes next. As a result, we built an app that would give people – especially the elderly or those with limited english proficiency (LEP) – a one-stop-shop to understand and act on their own health information. Our app aims to simplify the end-to-end process of planning for, scheduling, and understanding the results of a patient’s doctor’s appointment. To achieve this goal, we focused on simplifying this process by capturing data (patient/doctor conversations, day-to-day health notes, documents, etc), and parsing these into more readily understandable formats, especially to elders and those with LEP. Source 1: https://www.johnahartford.org/images/uploads/resources/The_Growing_Demand_for_Age-Friendly_Care_Report_FINAL.pdf Source 2: https://pubmed.ncbi.nlm.nih.gov/29249189 What it does Health Notes & Action Items Record a visit or health concern by voice. The app converts it into structured notes and automatically extracts follow-up tasks. Context-Aware AI Chat Assistant Answers questions strictly using the user’s own data (notes, appointments, documents, past sessions). If information isn’t available, it asks for further information and doesn’t try to guess. Respects the user’s preferred language. Document Scanning Upload or photograph labs, prescriptions, or summaries. A vision LLM generates concise, searchable summaries stored for future reference. Appointments & Visit Flow Schedule and manage appointments. After visits, record or paste conversations to generate structured summaries with key topics and action items. Voice Everywhere Real-time speech-to-text for notes and chat, plus outbound call flows directly from the app. Automatic Voice Agent Scheduling An AI voice agent can call clinics or hospitals to schedule, confirm, or reschedule appointments on the user’s behalf. Multilingual Support UI and AI responses available in multiple languages, including English, Spanish, Mandarin, Cantonese, Korean, Japanese, Vietnamese, Tagalog, Arabic, Portuguese, and more. How we built it Frontend Next.js 16 (App Router), React 19, Tailwind CSS, and Motion for animations. The dashboard includes navigation to home, action items, health notes, appointments, sessions, visit flow, and documents. Backend & Data Next.js API routes with Firebase Auth and Firestore for user data, notes, tasks, sessions, appointments, and document summaries. Firestore security rules enforce per-user access control. AI Layer Vercel AI SDK with OpenAI models (GPT-4o-mini for chat, GPT-4o for vision). Structured outputs enforced with Zod schemas for visit summaries, action items, note extraction, and document parsing. System prompts are constructed from user-specific context with strict “use only this information” and anti-hallucination rules. Voice AssemblyAI streaming transcription for in-app speech input. Vapi SDK for outbound AI voice calls to clinics with customizable patient and assistant names. Internationalization (i18n) Language preferences propagate across UI and all LLM calls to ensure summaries and chat responses match the user’s selected language. Challenges we ran into Keeping the Chat Grounded Ensuring the model only used provided context required strict prompt structure, explicit “do not invent” rules, and clear sectioning of user data. Turning Voice into Structured Data Separating clinical content from small talk and consistently outputting schema-validated summaries required careful prompt engineering. Real-Time Transcription UX Handling streaming transcripts, turn detection, token provisioning, and error states while maintaining responsiveness. **Document Pipeline Accuracy Balancing summary accuracy with token efficiency so vision outputs could reliably feed into future chat context. Accomplishments that we're proud of End-to-end voice and document pipelines that convert raw input into structured, queryable data A grounded, context-aware chat assistant with explicit anti-hallucination safeguards Structured LLM outputs across the app for reliability and frontend simplicity Multilingual support built into both UI and AI layers Vision-based document scanning integrated directly into conversational workflows What we learned Product & AI Design Learnings Filtering clinical content requires explicit exclusion rules and speaker attribution guidance. Clear prompt sectioning significantly reduces hallucination. Structured outputs are more reliable than parsing free text in healthcare workflows. Technical Learnings Designing for elderly users increases complexity. Simple UI patterns like dropdowns or loading states can create confusion. Accessibility and cognitive load directly impact architecture decisions. We also learned that integrating AI into healthcare requires guardrails, determinism, and transparency. Trust matters more than model sophistication. Broader Learnings Healthcare challenges are often coordination failures rather than treatment failures. Many frustrations stem from document comprehension, not clinical effectiveness. Trust is earned through reliability and clarity. Care involves multiple stakeholders: patients, providers, and caregivers. Humanity remains central to healthcare. Even powerful AI must support, not replace, human relationships. What's next for Hellocare HIPAA Compliance Expansion Firebase Auth and Firestore are HIPAA-compliant, and our scheduling voice assistant infrastructure supports compliance. The next step is integrating fully HIPAA-compliant LLM providers that sign BAAs to ensure end-to-end protection. Deeper System Integration Connect with hospital systems (e.g., FHIR, patient portals) for real-time syncing of appointments and results. Care Circle Allow users to securely share selected summaries or documents with family members and care coordinators. Proactive Reminders Send reminders and surface “questions to ask” based on upcoming appointments and recent notes. Richer Document Support Enable multi-page PDF uploads and structured extraction of medications, labs, and timelines. Accessibility & Transparency Expand voice-first workflows and add “show source” explanations for AI-generated answers. <div