---
slug: "healthflow-flaqzg"
url: "https://devpost.com/software/healthflow-flaqzg"
title: "Healthflow"
hackathon: "Student Innovators Without Borders Hacks (Students; Open Ended)"
organization: "Batch 09"
winner: true
words: 620
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Healthflow

> AI-enhanced medical management. From analyzing lab reports and ai imaging to generating notes, HealthFlow automates the complex, letting doctors focus on care and patients focus on health.

[Devpost](https://devpost.com/software/healthflow-flaqzg) · hackathon [[Student Innovators Without Borders Hacks -Students- Open Ended-]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: on_device_local, sensor_fusion, vision_ocr</sub>
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[video_visual]]
  <sub>weak: sensor_telemetry</sub>

**stack** api, css, gemini, genkit, lucide, n8n, next.js, react, shadcn/ui, tailwind, typescript

## Body

1)Inspiration In a world driven by data, healthcare often lags behind, burdened by fragmented systems and manual processes. We were inspired by the potential of Generative AI to bridge this gap, not just to digitize records, but to actively interpret them. We wanted to build a platform that doesn't just store data but understands it, transforming complex lab reports and medical imaging into actionable insights for both patients and providers. HealthFlow was born from the desire to create a "seamless connection" where technology acts as an intelligent partner in the care journey. 2)What it does HealthFlow is a comprehensive healthcare orchestration platform connecting patients and doctors through two distinct, specialized portals. For Patients: It acts as a personal health companion. Beyond booking appointments and viewing history, patients can upload complex lab reports or medical scans. Our AI Lab Analyzer breaks down dense metrics into understandable summaries, while the AI Imaging Model provides preliminary context for scans. For Doctors: It streamlines the administrative burden. The Medical Notes feature listens to or takes raw input from consultations and auto-generates structured, professional clinical notes (SOAP format), allowing doctors to focus on the patient rather than the paperwork. 3)How we built it We prioritized a high-performance tech stack to ensure speed, security, and scalability: Frontend: Built with Next.js and TypeScript for a robust, type-safe architecture. We used Tailwind CSS and Shadcn/UI to create a premium, dark-mode aesthetic, featuring a custom WebGL "Orb" for a distinct visual identity. AI orchestration: We integrated Genkit to power our reasoning engines. Lab Report Analysis: Uses multimodal capabilities to parse PDF/Image text and cross-reference with medical baselines. Imaging Model:Leverages computer vision models to identify anomalies in X-rays or MRI slices (for educational/triage context). Backend & Automation: We utilized Firebase for real-time data syncing and authentication, ensuring that patient-doctor interactions are instantaneous. n8n was used to handle complex workflows, such as scheduling automations and cross-platform notifications. 4)Challenges we ran into Multimodal AI Consistency: Getting the AI to reliably extract specific numerical values from diverse lab report layouts was difficult. We had to refine our system prompts and implement strict validation layers (Check: $Value \in [Range_{min}, Range_{max}]$) to ensure accuracy. Real-time Synchronization: ensuring that a doctor's update to a medical note reflected instantly on the patient's dashboard without page reloads required deep diving into Firebase's snapshot systems. The "Orb" Performance: Implementing the interactive 3D orb on the landing page looked great, but initially caused high CPU usage. We had to optimize the rendering loop and implement dynamic quality scaling to ensure it ran smoothly on all devices. 5) Accomplishments that we're proud of Seamless AI Integration: Successfully implementing the "Medical Notes" generator that can save doctors estimated hours of paperwork per week. Visual Polish: Achieving a "pixel-perfect" UI that feels professional and trustworthy, distinguishing it from typical sterile medical software. Secure Data Flow: Building a robust role-based access control system that strictly separates Patient and Doctor data while allowing necessary interactions. 6)What we learned The Power of Context: We learned that raw AI models are powerful, but their utility in healthcare depends entirely on the context provided. Fine tuning the prompts with medical constraints was crucial. User Trust: In healthcare, UI isn't just about looks, it's about trust. A glitchy interface makes users doubt the medical backend, so we learned to prioritize stability and "clean" interactions above all else. 7) What's next for Healthflow Telemedicine Integration: Adding secure, in browser video calls directly within the appointment slots. Wearable Sync: Integrating with APIs from Apple Health and Fitbit to feed real-time vitals into the AI analyzer for preventative alerts. Local LLM Deployment: Exploring on-device models for extreme privacy, ensuring sensitive medical notes never have to leave the doctor's machine for processing. <div