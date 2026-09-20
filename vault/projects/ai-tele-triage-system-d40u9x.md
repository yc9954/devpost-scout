---
slug: "ai-tele-triage-system-d40u9x"
url: "https://devpost.com/software/ai-tele-triage-system-d40u9x"
title: "AI Tele-Triage System"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 443
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/genomic_bio"
  - "substrate/transcript_audio"
---

# AI Tele-Triage System

> AI tele-triage assistant that listens to patients, detects risk from speech and sounds, and automatically generates clinically structured notes so doctors can focus on care instead of intake.

[Devpost](https://devpost.com/software/ai-tele-triage-system-d40u9x) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[voice_speech]]
**domain** [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[genomic_bio]] [[transcript_audio]]

**stack** fastapi, medgemma, nextjs, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai tele-triage system

## Body

Inspiration Healthcare today is burdened by clinician burnout and slow triage workflows — doctors often spend up to half their time on documentation, and thousands of patient calls are manually screened every day. Tele-Triage was inspired by the need to automate clinical intake, early risk detection, and documentation so clinicians can focus on care, not paperwork. By leveraging cutting-edge multimodal medical AI (like Google’s MedGemma) and acoustic biomarkers from audio, we envisioned a system that can hear, interpret, reason, and act autonomously in a clinical context. What it does The Agentic AI Tele-Triage System is an autonomous AI agent that: Listens to patient speech + cough/respiratory sounds. Converts spoken complaints into clinical text (transcription + analysis). Uses MedGemma for medical reasoning and structured note drafting. Synthesizes standard clinical SOAP notes (Subjective, Objective, Assessment, Plan). Prioritizes high-risk cases in a clinician’s queue using acoustic and clinical cues. Operates end-to-end — from patient input to triage outcome and documentation delivery. How we built it Reasoning Engine: MedGemma 4B via Ollama for medical semantic understanding. Speech to Text (ASR): Whisper (Python Transformers) for robust transcription of medical speech. Acoustic Analysis: Custom audio heuristics (e.g., cough/respiratory distress signals). Frontend: Next.js 14 + Tailwind CSS for interactive Patient & Clinician portals. Backend: Python FastAPI serving AI agents, logic, and triage APIs. Deployment: Local & privacy-first stack running entirely on user control. Challenges we ran into Multimodal integration: Combining audio biomarkers with semantic AI reasoning was non-trivial — aligning acoustic features meaningfully with medical context required custom signal processing and heuristic design. Domain accuracy vs privacy: Running MedGemma locally meant balancing medical reasoning power with resource constraints while ensuring patient data never left the local environment. Clinical fidelity: Prompt engineering to elicit medically credible outputs from MedGemma required significant iteration and safety guards to avoid hallucination. Accomplishments that we're proud of Built a true agentic pipeline — system perceives input, reasons clinically, and acts to generate structured medical documentation. Multimodal triage: First prototype combining speech + acoustic signals + LLM reasoning for clinical prioritization. Functional end-to-end interface for both patient input and clinician output — from raw speech to SOAP note with prioritized queue. What we learned Integrating acoustic biomarkers with LLM reasoning opens rich avenues for non-text clinical signals in AI triage. Running advanced models like MedGemma locally (via Ollama) ensures data privacy and control, which is critical in healthcare applications. Prompt design and domain alignment are just as important as model choice — clinical fidelity depends on how we structure and guard the AI’s reasoning process. What's next for AI Tele-Triage System Clinical validation: Pilot deployments with real clinician feedback loops to improve safety and trust. <div