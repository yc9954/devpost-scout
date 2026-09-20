---
slug: "health-nfedwy"
url: "https://devpost.com/software/health-nfedwy"
title: "Emi"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 806
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/genomic_bio"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Emi

> Emi: Your AI-powered triage nurse 🤖💓

[Devpost](https://devpost.com/software/health-nfedwy) · hackathon [[NexHacks]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]] [[health_clinical]]
**user** [[clinician]] [[patient_family]] [[social_worker]]
**substrate** [[genomic_bio]] [[medical_record]] [[structured_db]] [[transcript_audio]]
  <sub>weak: web_dom</sub>

**stack** base, elevenlabs, html, javascript, kairo, react, solidity, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for emi

## Body

Emi: Your digital intake nurse companion EMI: Verifiable, AI-Powered Medical Intake Before the Appointment Inspiration Modern medical booking is built on an assumption: that patients can accurately remember and describe their symptoms days after they occur. In reality, this creates a diagnostic blind spot . Patients book an appointment and wait days or weeks. By the time they see a doctor, critical information is lost. Symptoms blur together, timelines fade, and severity is often misremembered. Doctors then spend the first 8 minutes of a 15-minute visit asking, “So, what’s wrong?” instead of diagnosing and treating. Even worse, today’s intake process creates serious trust and liability gaps: Subjective memory fade: Patients forget when symptoms started or how intense they were. Administrative friction: Clinicians waste time reconstructing narratives instead of acting. The vitals gap: Doctors lack objective physiological data from the moment symptoms actually occurred. Data integrity issues: There is no immutable record of what the patient said versus what was later transcribed into the EMR. We realized the core problem isn’t access to doctors or even AI — it’s timing and trust . What if intake happened before the appointment, while symptoms were still fresh, and produced data that doctors could rely on as a true source of record? That question led to EMI . What it does EMI transforms a standard appointment confirmation into a live, adaptive pre-screening session that captures symptoms, vitals, and intent in real time — and locks them into a verifiable medical record. For Patients Speak naturally with an AI nurse through a voice-first experience. No forms, no typing, no medical jargon. Passive vitals capture through the webcam while speaking. Complete the intake from home in minutes, at the moment symptoms are fresh. For Doctors Receive a structured, clinician-ready medical report before the appointment. See objective vitals alongside subjective symptom descriptions. View automatically flagged red signals and anomalies. Spend appointment time diagnosing, not extracting information. For Healthcare Systems Tamper-proof intake records reduce disputes and liability. Immutable timestamps prove exactly what was reported and when. Higher-quality, higher-signal data entering downstream EMR systems. In essence, EMI closes the diagnostic blind spot by replacing rushed questioning with verified, real-time clinical context. How we built it We built EMI as a multi-modal intake system that combines voice, vision, AI reasoning, and blockchain verification into a single seamless flow. The Face — ElevenLabs: Uses Conversational AI for low-latency, empathetic voice interaction. It doesn’t just speak — it listens and asks medically relevant follow-up questions based on patient responses. The Vitals — Presage Tech: Uses rPPG (remote photoplethysmography) to extract heart rate, respiratory rate, HRV, and oxygen saturation directly from the webcam while the patient is speaking — fully contactless. The Brain — Gemini API: Synthesizes the structured transcript and numerical vitals data into a professional SOAP note , flags red-flag symptoms, and highlights areas requiring clinician attention. The Shield — Kairo: The final intake report is hashed using SHA-256 and recorded via a Verifiable Intake smart contract. This creates a timestamped, immutable source of truth without storing any sensitive PHI on-chain. The result is a system that is clinically useful, legally defensible, and frictionless for patients. Challenges we ran into Synchronizing real-time voice interaction, vitals extraction, and transcription without introducing latency. Ensuring AI-driven follow-up questions remained clinically appropriate without crossing diagnostic boundaries. Structuring multi-modal data so the medical reasoning engine produced consistent, reliable summaries. Designing an on-chain verification layer that proves integrity while preserving patient privacy. Maintaining a simple, human-centered UX despite a complex, multi-system architecture. Accomplishments that we’re proud of Built a live, voice-first medical intake experience with passive vitals capture. Successfully merged subjective symptom reporting with objective physiological data. Generated clinician-ready SOAP notes before the appointment occurs. Implemented immutable intake verification using on-chain hashing. Created a workflow that saves doctors time while improving diagnostic accuracy and trust. What we learned This project taught us that better healthcare outcomes often come from better timing , not just better models. Capturing data at the moment symptoms occur dramatically improves its accuracy and usefulness. We also learned that blockchain is most powerful in healthcare when used narrowly and intentionally — not as a database, but as a trust anchor for critical medical records. Most importantly, we learned that AI works best in healthcare when it augments clinicians rather than replacing them. What’s next for EMI EMR Integration: Push verified intake reports directly into existing EMR systems. Regulatory Alignment: Expand toward HIPAA-compliant storage and audit workflows. Longitudinal Tracking: Link repeated intakes to track symptom progression over time. Expanded Vitals: Add blood pressure estimation and advanced stress biomarkers. Clinical Pilots: Partner with real clinics to measure time saved, diagnostic accuracy, and patient outcomes. EMI’s long-term vision is to eliminate the diagnostic blind spot by ensuring doctors begin every appointment with trusted, verified, and actionable patient data already in hand. <div