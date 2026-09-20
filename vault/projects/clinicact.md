---
slug: "clinicact"
url: "https://devpost.com/software/clinicact"
title: "ClinicAct"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 968
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/government_staff"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/medical_record"
  - "substrate/transcript_audio"
---

# ClinicAct

> ClinicAct turns doctor-patient conversations into ready-to-sign EMR actions and clear patient follow-up, eliminating documentation friction while keeping clinicians fully in control.

[Devpost](https://devpost.com/software/clinicact) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[finance_payments]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[government_staff]] [[patient_family]] [[social_worker]]
**substrate** [[medical_record]] [[transcript_audio]]
  <sub>weak: code_repository, web_dom</sub>

**stack** css, deepgram, gemini, html, javascript, medplum, mongodb, next.js, react, toolio, typescript

## How they structured the write-up

- clinicact
- problem
- inspiration
- what it does
- how we built it (healthcare-first)
- system flow (high level)
- challenges we faced
- accomplishments we’re proud of
- what we learned
- what’s next for clinicact
- tech stack
- repository

## Body

ClinicAct An AI Clinical Copilot for Documentation, Orders, Referrals, and Patient Follow-Up Problem Modern EMRs force clinicians to act as data entry clerks, spending hours clicking through fragmented workflows to perform basic clinical tasks. This administrative friction disrupts care delivery, increases burnout, and pulls attention away from patients. ClinicAct addresses this by acting as a clinical action layer . It listens to patient visits and converts medical intent into structured, ready-to-sign EMR actions. With one-click approval, documentation and orders move at the speed of the conversation—while keeping clinicians fully in control. Inspiration ClinicAct was inspired by a real experience shared by one of our teammate’s older siblings, a pharmacist. They described how much time clinicians lose to manual documentation, repetitive form filling, and navigating fragmented healthcare systems. This constant friction not only slows care delivery but contributes directly to burnout. We also observed a major patient-side gap. Patients often leave visits confused about medications, labs, or follow-up steps. After-visit summaries are usually static and easy to forget, leaving patients unsure about what to do next. ClinicAct was built to reduce clinician workload while improving patient understanding , without replacing doctors or disrupting existing EMR systems. What It Does ClinicAct is an AI-powered clinical copilot that works alongside existing Electronic Medical Record (EMR) systems. During the visit Listens to doctor–patient conversations in real time Transcribes speech and analyzes clinical intent Automatically generates draft medical orders , including: Medications Lab tests Imaging Referrals Presents all drafts to physicians for one-click review and approval After the visit Generates a clear, patient-friendly visit summary Sends it via email and a follow-up phone call Allows patients to call back and ask questions in plain language Answers questions using only information from that specific visit Physicians remain fully in control. Nothing is written to the EMR without explicit approval. How We Built It (Healthcare-First) We designed ClinicAct as a real healthcare product, prioritizing safety, interoperability, and usability. Medplum (FHIR R4 Clinical Data) Medplum serves as ClinicAct’s clinical data backbone . Stores patients, encounters, medications, labs, referrals, insurance , and pharmacy information Uses FHIR R4 , the same interoperability standard used by modern EMRs Converts AI-detected intents into structured FHIR resources Supports real clinical entities such as: MedicationRequest ServiceRequest Coverage (insurance) Organization (pharmacies and providers) This ensures ClinicAct produces clinically usable data , not just text summaries. Local Doctor Lookup API (Referral Automation) To automate referrals, ClinicAct integrates a local doctor lookup API . Finds nearby specialists based on: Medical specialty Geographic location Insurance compatibility (when available) Automatically fills FHIR referral fields such as: ServiceRequest Practitioner Eliminates manual searching and copy-pasting during referrals This allows physicians to generate accurate, location-aware referrals directly from the conversation . Deepgram (Speech-to-Text and Voice AI) Deepgram powers ClinicAct’s audio intelligence across the system. Transcribes doctor–patient conversations in real time Converts AI responses into natural-sounding speech Used for both clinical transcription and patient phone call voice responses Optimized for low-latency medical conversations This enables ClinicAct to understand spoken clinical language and communicate clearly with patients. Twilio Voice API (Patient Phone Calls) Twilio handles ClinicAct’s telephony infrastructure. Places outbound follow-up phone calls to patients with real phone numbers Manages live call flow and speech capture Works in tandem with Deepgram , which provides speech recognition and voice synthesis during calls Allows patients to interact without needing an app or patient portal This improves accessibility, especially for older patients or those less comfortable with technology. Google Gemini (Clinical Reasoning and Summarization) Gemini is the reasoning engine behind ClinicAct. Extracts structured clinical intents from conversations Generates draft orders and referrals Produces patient-friendly summaries Powers the secure, voice-based Q&A system The AI is intentionally constrained to: Use only visit-specific information Keep responses short and medically safe Always require physician approval Security and Authentication Patients receive a secure, temporary PIN PINs expire after 24 hours Prevents unauthorized access to medical information No patient accounts or apps required -Designed with HIPAA principles in mind, using access-controlled, session-based workflows and keeping clinicians fully in control of what is written to the EMR. This balances accessibility with healthcare-grade security. System Flow (High Level) Doctor–Patient Conversation → Live Transcription → Clinical Intent Detection → Structured FHIR Orders & Referrals → Local Doctor Lookup → Physician Review → EMR Integration → Patient Summary → Follow-Up Phone Call → Secure AI Q&A Challenges We Faced Ensuring AI never acts independently in a high-stakes healthcare environment Handling unstructured, interrupted spoken medical language Coordinating real-time transcription, reasoning, voice synthesis, and telephony Integrating multiple external systems while maintaining data consistency and trust Accomplishments We’re Proud Of Built a complete end-to-end clinical workflow within a hackathon timeframe Used real healthcare standards (FHIR) instead of mock data Automated referrals using real local provider data Integrated insurance and pharmacy data into clinical workflows Enabled voice-based patient follow-ups without requiring apps Designed AI to reduce burnout, not replace clinicians What We Learned How to build AI systems for high-stakes healthcare environments Why interoperability matters more than surface-level automation How to keep humans in the loop while still automating workflows How to design systems clinicians actually trust What’s Next for ClinicAct Next, we plan to expand ClinicAct into pre-visit patient triage . Patients could: Describe symptoms conversationally to an AI Receive guidance for minor concerns Be directed to schedule visits when appropriate Combined with our physician workflow, ClinicAct could support the entire care journey , from intake to follow-up, while maintaining safety and human oversight. Tech Stack Next.js – Web application and orchestration Medplum (FHIR R4) – Clinical data, insurance, and pharmacy integration Local Doctor Lookup API – Referral automation Deepgram – Medical speech transcription and voice AI Twilio Voice API – Secure patient phone calls Google Gemini – Clinical reasoning and summaries MongoDB Atlas – Session and authentication data TypeScript / Node.js – Backend logic Repository https://github.com/shreyaskommuri/ClinicAct <div