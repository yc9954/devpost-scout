---
slug: "medibuddy-y7t65f"
url: "https://devpost.com/software/medibuddy-y7t65f"
title: "MediBuddy"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 834
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# MediBuddy

> Empowering Doctors, Guiding Patients.

[Devpost](https://devpost.com/software/medibuddy-y7t65f) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[developer_tools]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[patient_family]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[transcript_audio]]

**stack** asi-1, convex, gemini, groq, react, tailwind-css, typescript, vercel

## How they structured the write-up

- inspiration 🧠
- what it does 💡
- how we built it 🛠️
- challenges we ran into 🤯
- accomplishments that we're proud of 🏆
- what we learned 📚
- what's next for medibuddy 🔮
- the impact 🌟

## Body

Home Page Inspiration 🧠 Every year, thousands of clinical trials go under-enrolled, not because patients are unwilling, but because they’re unaware. Doctors often don’t have time to search eligibility criteria or explain options during short appointments, they also have on additional overhead of taking notes of the medical history of patients during the visit. We asked ourselves: What if trial matching could happen automatically in the background during a normal doctor visit? That question led us to build MediBuddy - an autonomous, privacy-first platform that turns doctor-patient conversations into life-saving trial opportunities. What it does 💡 MediBuddy listens to doctor-patient appointments via voice, transcribes the conversation in real-time, structures the medical information, generates a report, and uses autonomous agents to match patients with relevant clinical trials. If a match is found, the patient can securely consent to share limited data with the sponsor all without leaving the app. The platform supports: 📅 Appointment Booking (with doctor approval) 🎙️ Speech-to-text Transcription (via Groq (Whisper v3 Large Turbo)) 🧾 Summarization and Structuring (via Google Gemini) 🧬 Clinical Trial Matching via AI Agents (ASI-1 by Fetch.ai) ✅ Consent Management for trials 🧑‍⚕️ Role-based Dashboards for Doctors and Patients How we built it 🛠️ We began by designing user flows for both patients and doctors to make sure the system felt simple, secure, and intuitive. Once the core flows were clear, we: Built the frontend using React + Typescript + Tailwind CSS , with a dynamic dashboard for both roles Used Convex for the backend and database to power real-time data, user roles, and appointment logic Integrated Groq’s API(Whisper v3 Large Turbo) to transcribe voice input during doctor appointments Passed transcriptions to Google Gemini to generate structured summaries (conditions, age, comorbidities, etc.) Used ASI-1 SDK by Fetch.ai to simulate sponsor agents and match trials based on extracted patient data Designed a consent interface where patients explicitly approve before data is sent to sponsor agents Deployed the full app to Vercel for fast and easy hosting We built MediBuddy to prove that even complex, regulated workflows like trial enrollment can be simplified with the right blend of AI, agent systems, and thoughtful UX. Key Features Implemented 🧱 Auth system for Patients and Doctors Doctor dashboard to manage appointment requests and suggest trials Patient dashboard to review transcripts, summaries/reports, and suggested trials Speech capture from doctor interactions, transcribed and summarized Structured data extraction for trial matching Agent-based communication for querying trial sponsors Consent flow that notifies sponsors upon patient approval Challenges we ran into 🤯 Agent interoperability : Designing a flexible message format for Fetch.ai agents to exchange patient-trial matching data while preserving privacy was tricky. On-device vs. API trade-offs : We wanted to minimize cloud-based PII(Personally Identifiable Information) exposure, so we had to carefully architect our pipeline to process transcription and summarization securely. Natural language variability : Doctor conversations are unstructured, turning them into structured trial-relevant data was challenging. We fine-tuned prompt strategies for Gemini to extract accurate conditions, age, and comorbidities. Convex learning curve : Convex’s serverless model and schema system were powerful but took some iteration to model complex relationships like appointments, consent, and role-based access correctly. Accomplishments that we're proud of 🏆 Built a fully functional end-to-end prototype in under 24 hours Successfully integrated voice transcription (Whisper) with structured summarization (Gemini) Designed and implemented a real-time doctor-patient workflow with Convex’s reactive backend Created an agent-based trial matching system using ASI-1 SDK by Fetch.ai Preserved privacy-first data flows with patient-controlled consent Designed an intuitive UI for both patients and doctors using React + Tailwind CSS Simulated a real-world clinical use case with minimal friction for the end user What we learned 📚 Voice is a powerful interface , it lowers the barrier to data collection and enables richer insights, especially in clinical contexts. AI agents + human interfaces can work in harmony. We built trust-first experiences by keeping the user in control (e.g., explicit consent before trial sharing). Convex is great for rapid prototyping : real-time updates, integrated database, and strong typing helped us move fast once we were over the initial learning curve. Healthcare UX matters , we focused on keeping flows intuitive, secure, and frictionless, especially for sensitive actions like consent and data sharing. What's next for MediBuddy 🔮 🧬 Custom agent logic for more nuanced trial filtering (e.g., co-morbidities, stage-specific trials) 🔐 Biometric consent mechanisms (e.g., voice or face verification) 📈 Doctor-side analytics dashboard for trial recommendation insights 🎁 Token-based reward system for trial participation and consent engagement ☁️ Optional encrypted backup using IPFS for decentralized storage of summaries and transcripts The Impact 🌟 With MediBuddy , we hope to: Make clinical trials more accessible , especially for patients who never knew they qualified Reduce doctor workload by enabling passive trial discovery and transcription & summarization of the conversation. Push forward agent-based automation in a space where trust and privacy are paramount We believe MediBuddy is not just a hackathon project, it's a real step toward bringing AI-powered clinical access into everyday care. <div