---
slug: "cortexflow-w3ry5d"
url: "https://devpost.com/software/cortexflow-w3ry5d"
title: "CortexFlow"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 716
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# CortexFlow

> Cognitive signal analysis platform

[Devpost](https://devpost.com/software/cortexflow-w3ry5d) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[realtime_stream]] [[voice_speech]]
**domain** [[elder_child_care]] [[finance_payments]] [[health_clinical]] [[housing_homeless]]
**user** [[clinician]] [[patient_family]]
**substrate** [[genomic_bio]] [[geospatial]] [[medical_record]] [[structured_db]] [[transcript_audio]]

**stack** css, docker, gemini, javascript, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cortexflow
- note

## Body

Loading / CortexFlow screen Voice and text input interface for capturing samples and initiating real-time cognitive analysis. Cognitive dashboard showing domain-level analysis, biomarker trends, and real-time cognitive load insights. Interactive 3D brain workspace mapping linguistic signals to region-level cognitive activity and indicators. Inspiration Neurological disorders often go undetected until significant cognitive decline has already occurred. Traditional clinical assessments are infrequent, stressful, and heavily reliant on manual evaluation. We wanted to build a bridge between cutting-edge AI and deterministic clinical analysis, empowering patients to self-monitor comfortably while providing healthcare providers and caregivers with real-time, deep neurological insights. The goal was to transform raw, everyday speech and text into a structured, proactive health ecosystem. What it does CortexFlow is a highly sophisticated, full-stack cognitive signal analysis platform that creates a massive, interconnected digital health ecosystem across three specialized dashboards: Patient Portal : Allows individuals to perform low-friction cognitive assessments via text or browser-based voice capture, maintaining a secure "Memory Lane" of their historical scores. Healthcare Provider Dashboard : A clinical-grade command center where neurologists can view deep speech analysis—mapping pause timings, lexical, semantic, prosody, and affective domains—and track longitudinal cognitive trends. Caregiver Dashboard : Provides proactive monitoring, task coordination, and automated alerts for sudden deviations in a patient's cognitive load. How we built it We utilized a robust, modern tech stack designed for global scale and security: Frontend : Next.js 16 (App Router), React 19, and Tailwind CSS v4. Deployed on Vercel to guarantee sub-second interactions and instantaneous page hydration via edge computing. Backend : Python 3.11+ and FastAPI, containerized with Docker and orchestrated by Amazon ECS to effortlessly scale during complex cognitive inference spikes. AI & Neuro-Analysis Engine : A dual-layered engine utilizing the Google Gemini API for high-fidelity audio transcription, paired with our custom Python backend to compute deterministic linguistic biomarkers. Database & Data Layer : Supabase (PostgreSQL) for complex multi-tenant relationships (provider-patient schemas), real-time notifications, and secure storage, with Firebase overlaying robust authentication. Data Visualization : We built a custom Three.js visualizer that maps computed biomarker intensities onto an interactive 3D brain workspace (MNI152 normalization), alongside a WebGL-powered fluid noise background. Challenges we ran into Complex Data Schemas : Managing the immense complexity of three distinct user types (Patients, Providers, Caregivers), their secure inter-linking, and granular access control revocations in PostgreSQL. Dual-Layered Inference Bottlenecks : Processing heavy cognitive inference without lagging the frontend. We solved this by using AWS ECS to automatically provision new backend containers during load spikes. Translating Data to 3D Space : Accurately mapping abstract deterministic linguistic biomarkers onto a normalized 3D MNI152 brain cortex using Three.js required deep mathematical and graphical tuning. Strict Aesthetics Requirements : Achieving a premium, clinically reassuring, and fluid user experience meant deeply optimizing our WebGL backgrounds and glassmorphism UI components without sacrificing React's render performance. Accomplishments that we're proud of Successfully orchestrating a completely unified data layer that syncs insights and alerts seamlessly across three distinct, highly specialized dashboards in real-time. Building our bespoke interactive 3D Cortex Atlas that translates raw speech data into visually comprehensible neurological anomalies. Developing a non-diagnostic, clinically safe backend payload that extracts highly deterministic features (syntax, prosody, semantics) from raw AI transcriptions. Creating an incredibly fluid and beautiful user interface that feels both cutting-edge and deeply comforting for patients. What we learned We gained profound experience in structuring complex Next.js 16 applications using React Server Components to maintain high performance with heavy dashboards. We learned how to deeply integrate Three.js with React to build responsive 3D environments. We discovered the nuances of orchestrating containerized Python backends on AWS ECS to handle variable, computationally heavy workloads. We learned how to architect secure, HIPAA-compliant-ready relational databases using Supabase row-level security. What's next for CortexFlow Multimodal Expansion : We plan to incorporate facial tracking and gaze-analysis to capture an even wider spectrum of neurological biomarkers. EHR Integration : Seamlessly integrating our system with standard Electronic Health Records so clinical orders, lab results, and CortexFlow data live in a unified physician workspace. Clinical Validation : Running large-scale, anonymized beta tests to further validate our deterministic baseline models against standardized clinical cognitive benchmarks. Note We recorded the youtube video when the platform was in its early stage now it features multiple interconnected dashboards and tons of new and useful features please check the deployment link. <div