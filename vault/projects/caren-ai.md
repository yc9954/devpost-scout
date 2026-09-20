---
slug: "caren-ai"
url: "https://devpost.com/software/caren-ai"
title: "Caren AI"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 812
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/regulation_legal_text"
---

# Caren AI

> Because everyone deserves someone who cares

[Devpost](https://devpost.com/software/caren-ai) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[health_clinical]] [[labor_employment]]
**user** [[clinician]] [[general_public]] [[patient_family]]
**substrate** [[document_pdf]] [[regulation_legal_text]]

**stack** ai, ai-agents, dart, elevenlabs, firebase, flutterflow, gemini, perplexity, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for caren ai

## Body

Login Dashboard Select tone of AI voice model Patient's AI calling to Insurance Company Dashboard 2 Personalized ElevenLabs Knowledge Base FireBase Twilio Phone Number of Patient's AI (Caren AI) AI Agents Architecture Market Size Business Model Inspiration Every year, 850 million insurance claims are denied in the U.S., leaving patients with unexpected medical bills and financial stress. Shockingly, less than 1% of these denied claims are ever appealed not because they lack merit, but because the appeal process is frustrating, time-consuming, and complicated (Wall Street Journal). As a result, nearly 1/3 of Americans contribute to $220 billion in medical debt, often due to denied or mishandled claims (Consumer Financial Protection Bureau). We wanted to level the playing field by putting AI in the patient’s corner. What if an AI negotiator could read the fine print, fight back against denials, and handle everything seamlessly? That’s how Caren AI was born—to empower patients, recover their rightful coverage, and eliminate unfair medical debt. What it does Caren AI automates the insurance claim appeal process and negotiates with insurance providers on behalf of patients. Our AI reads insurance denial letters, cross-references them with Evidence of Coverage (EOC) documents, and calls insurance companies to dispute denials using legally backed arguments. Key Features: AI-Powered Claim Negotiation – Caren AI analyzes insurance policies and denial letters, then calls the insurance provider via Twilio to dispute the claim. Automated Healthcare Scheduling – The AI finds available doctor appointments and books them for the patient in seconds. Intelligent Appeals Processing – Uses ElevenLabs Conversational AI, trained on insurance documents, to craft strong, evidence-based appeal arguments. Caren AI features two AI agents dedicated to simplifying healthcare management: Sam (Scheduling AI) – Helps users book and manage doctor appointments based on availability and medical history. Noa (Negotiation AI) – Calls insurance providers, disputes denied claims, and negotiates fair settlements to reduce costs. Result: Patients save thousands on medical bills without the hassle of navigating complex insurance policies themselves. How we built it We designed Caren AI as a full-stack AI-powered assistant, ensuring seamless automation of insurance claim disputes and healthcare scheduling. Frontend : FlutterFlow (Dart) – A clean, user-friendly interface for patients. AI Backend : ElevenLabs Conversational AI – Trained on insurance policy documents for intelligent claim analysis. Fastest AI Model : Gemini 2.0 Flash – Parses complex medical and insurance documentation. Live Call Automation : Twilio API – AI negotiates claims directly with insurers via automated phone calls. Authentication : Firebase Authentication – Secure user logins and data protection. By combining AI, automation, and real-time negotiation, we eliminated the need for manual claim appeals, making the process fast, accurate, and effortless for patients. Challenges we ran into Training AI on Complex Insurance Policies – Extracting accurate insights from dense, jargon-heavy documents required custom model fine-tuning. Real-Time Insurance Call Handling – Ensuring AI could hold a live, logical conversation with insurers using Twilio without sounding robotic was a key challenge. Using Flutter for the First Time – Since our team was new to FlutterFlow, we had to learn its UI-building framework and state management quickly to build a seamless frontend experience. Through iterative testing, API optimizations, and AI refinement, we successfully overcame these hurdles to create a seamless patient experience. Accomplishments that we're proud of Built a Fully Functional AI-Powered Claim Negotiator – Our AI successfully disputes insurance claims in real-time. Implemented End-to-End Automation – From claim upload to resolution, everything happens without manual intervention. Integrated Live Twilio Call Handling – Caren AI makes phone calls to insurers, delivering legally sound counterarguments. Designed a Scalable, Patient-Friendly Platform – Built using FlutterFlow, making it accessible to all users, regardless of tech expertise. Our solution doesn’t just solve a problem it revolutionizes patient advocacy in healthcare. What we learned The Healthcare System is Stacked Against Patients – Insurance denials are often not justified, but most patients don’t have the knowledge or time to fight back. AI Can Level the Playing Field – With intelligent claim analysis and negotiation, AI can recover thousands of dollars for patients. User Experience Matters – Many users aren't tech-savvy, so creating a seamless, intuitive interface was crucial. Real-Time Communication with Insurers is Game-Changing – Automating insurance negotiations was far more effective than just document-based appeals. Caren AI isn’t just an app—it’s a movement. By leveraging AI negotiation, we’re fighting for patient rights and bringing fairness back to healthcare. Join the revolution, and let AI handle the hassle, so you can focus on your health. What's next for Caren AI Callback Feature for Dropped Calls – If an insurance call disconnects, Caren AI will automatically redial and resume the negotiation. Multilingual Support – Expanding beyond English to support Spanish, French, and more to help non-native speakers navigate insurance issues. Family Insurance Management – A family plan feature that allows users to track and manage multiple insurance claims in one place. <div