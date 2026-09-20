---
slug: "sehat-guftagu-health-talks"
url: "https://devpost.com/software/sehat-guftagu-health-talks"
title: "Sehat Guftagu (Health Talks)"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 858
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/developer"
  - "user/educator_student"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Sehat Guftagu (Health Talks)

> Apki Sehat, Humari tarji (Your Health, Our Priority)

[Devpost](https://devpost.com/software/sehat-guftagu-health-talks) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[voice_speech]]
  <sub>weak: retrieval_grounding</sub>
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[health_clinical]] [[labor_employment]]
**user** [[clinician]] [[developer]] [[educator_student]] [[patient_family]] [[social_worker]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[transcript_audio]]

**stack** elevenlabs, google-gemini-api, google-web-authentication, groq, javascript, langchain, langgraph, nextjs, pinecone-rag, prisma, supabase, typescript, uplift-ai

## How they structured the write-up

- ai-powered clinical conversations that help doctors catch what matters early
- inspiration
- 1. description of the idea
- 2. target group
- 3. features & functions
- 4. value proposition & usp
- 5. visualization
- 6. user feedback
- 7. business model
- 8. implementation & feasibility
- 9. data requirements & privacy
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next
- team information
- contact
- update (june 2026):

## Body

Presents Front-end Interface How it works Why choose us Medical History Session Voice Agent Patient Dashboard Doctor Dashboard SOAP Report with red flags highlighted on Doctor End System Architecture Design Sehat Guftagu AI-powered clinical conversations that help doctors catch what matters early Inspiration Many people suffer from serious health complications not because doctors lack expertise, but because critical details are missed early in the process. This usually happens due to: Overburdened doctors with only 2–3 minutes per consultation. Helpline workers and clinics are failing to ask the right follow-up questions. Patients struggling to explain symptoms clearly, often due to language barriers. The gap we observed On average, there is only 1 doctor per 1,000 people globally. Around 50–70% of medical errors are linked to communication failures. Language differences (English vs Urdu, Punjabi, Pashto, Sindhi, etc.) further widen the gap. We imagined a system where patients could calmly explain their problems in their own language, while doctors receive a clear, structured summary before meeting them. 1. Description of the Idea Sehat Guftagu is an AI-powered health assistant that conducts structured medical interviews with patients in their preferred language and converts those conversations into clear, doctor-ready clinical reports. Our solution focuses on early symptom clarity , better communication , and time efficiency for healthcare providers. By collecting accurate information before a consultation, we help reduce missed red flags and improve medical decision-making. 2. Target Group We designed Sehat Guftagu for: Patients , especially those with language or communication barriers Doctors and clinicians who face time pressure Clinics and hospitals managing high patient volumes Telemedicine platforms needing structured intake data 3. Features & Functions Core features include: 5–15-minute guided clinical interviews in the patient’s language Voice and text interaction support Automated detection of medical red flags Generation of structured SOAP reports (Subjective, Objective, Assessment, Plan) Doctor-ready summaries available before consultation Technology used AI and Large Language Models for reasoning and translation Speech-to-Text and Text-to-Speech for voice interaction Multi-agent orchestration for interview flow and documentation 4. Value Proposition & USP What makes Sehat Guftagu different: We focus on pre-consultation clarity , not diagnosis replacement Patients speak naturally, in their own language Doctors receive structured, clinically useful summaries Red flags are highlighted early instead of buried in conversation Unlike generic chatbots, we are not trying to “act like a doctor”. We help doctors do their job better by giving them better information upfront. 5. Visualization Our MVP includes: A clean, responsive web interface Real-time progress indicators during interviews Dynamic sections showing interview stages 6. User Feedback We validated the idea informally with: Medical students and junior doctors General users with prior telemedicine experience Early feedback Doctors appreciated receiving structured summaries instead of long patient explanations Users felt more comfortable speaking in their native language Many mentioned they remembered details they usually forget during real consultations This feedback directly shaped our interview flow and report format. 7. Business Model Possible monetization paths: B2B licensing for clinics and hospitals Subscription plans for telemedicine platforms Freemium model for individuals with paid advanced reports Future integration with insurance or employer health programs Our goal is affordability without sacrificing quality. 8. Implementation & Feasibility Sehat Guftagu is already implemented as an MVP. Current state Fully working frontend and backend Multilingual AI interviews Report generation pipeline Deployed using free-tier services Next steps Clinical validation with doctors Improving medical accuracy with fine-tuning Adding condition-based doctor recommendations Scaling infrastructure for production use 9. Data Requirements & Privacy We handle sensitive health data carefully. Data involved Patient symptoms (text and voice) Conversation transcripts Generated clinical summaries Privacy & security No unnecessary data collection Encrypted storage using PostgreSQL on Supabase Designed with GDPR/DSGVO principles in mind Clear consent before any data processing We aim to remain compliant and transparent as the system scales. How We Built It Frontend: Next.js with TailwindCSS Backend: Next.js API routes with Prisma ORM AI & LLM: Groq LLaMA models for reasoning and translation Voice Services: ElevenLabs, Uplift AI, Groq Whisper Database: PostgreSQL (Supabase) Agent Orchestration: LangGraph for multi-agent workflows Challenges We Ran Into Medical-grade translation between Urdu and English Balancing AI automation with human oversight API rate limits on free tiers Low-latency voice processing Accomplishments We’re Proud Of End-to-end multi-agent interview pipeline Real-time adaptive UI Multilingual support from day one Scalable system design What We Learned Clear communication saves lives Healthcare AI must support humans, not replace them Simple UX matters more than complex features Free-tier constraints force better engineering decisions What’s Next Condition-based doctor recommendations City-level hospital suggestions Budget-friendly care options WhatsApp integration Secure lifelong medical history tracking Team Information Kaleemullah Younas Role: Full-Stack AI Engineer GitHub Muhammad Umer Role: Web Developer & DevOps GitHub Contact Primary Contact Email: Contact us Disclaimer This is an MVP deployed on free-tier services. The live version may occasionally face rate limits (HTTP 429). We plan to upgrade the infrastructure for reliability and scale. Update (June 2026): The live demo link is currently unavailable. The application was previously hosted using free cloud credits, which have since expired, and the hosting instance has been decommissioned. The source code and project details still remains available for review. Thank you for your understanding. <div