---
slug: "halo-93qrf7"
url: "https://devpost.com/software/halo-93qrf7"
title: "Halo"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 881
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/transcript_audio"
---

# Halo

> Reduce hospital administrative work by helping automate patient monitoring and doctor coordination.

[Devpost](https://devpost.com/software/halo-93qrf7) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[transcript_audio]]

**stack** fastapi, flask, ibm-stt, ibm-tts, ibm-watson, mediapipe, mistral, mongodb, next.js, opencv, opensmile, python, react, rest

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we accomplished
- challenges we faced
- what we learned
- what’s next

## Body

Hospital 3D Rendering Doctor Page Body Inspiration Clinicians in Canada spend an enormous portion of their time on administrative work, documentation, and routine follow-ups instead of direct patient care, while nurses in hospitals and long-term care facilities struggle to monitor multiple patients simultaneously. Based on a January 2026 report by the Canadian Medical Association and the Canadian Federation of Independent Business, Canadian physicians alone spend roughly 42.7 million hours annually on administrative tasks. This creates dangerous gaps. A patient’s subtle symptoms can be overlooked. A fall might go unnoticed for minutes. A routine follow-up that could have identified complications early may never happen because staff simply do not have enough time. We designed Halo to reduce this friction across the clinical workflow. Instead of replacing clinicians, Halo acts as an AI assistant that handles routine communication, continuously gathers patient information, and surfaces important signals in real time. By connecting automated patient outreach with live hospital monitoring, Halo gives healthcare teams the visibility and efficiency they need to focus their time where it matters most: patient care. What It Does Halo improves clinical efficiency by automating routine patient interactions while providing clinicians with real-time visibility across hospital environments. For physicians, Halo provides an AI telephony assistant that can call patients to complete recovery check-ins and health questionnaires. Using IBM Watson Speech-to-Text and Text-to-Speech, patients can respond naturally to simple questions about their symptoms or recovery status. The system processes these responses with IBM Watsonx to normalize symptoms, evaluate urgency, and generate structured clinical notes. For nurses and clinical staff, Halo provides a live hospital monitoring dashboard. A real-time 3D floor plan of the facility shows rooms color-coded by urgency. Staff can quickly identify which patients require attention and drill down into individual records. Halo also integrates a computer vision module that continuously monitors for fall events using OpenCV and MediaPipe. If a fall is detected, the system triggers an automated check-in and sends an alert to staff immediately. All collected information feeds into a unified clinical interface where patient symptoms are visualized and mapped onto a 3D anatomical model, helping clinicians quickly understand patient status and prioritize care. Since Halo is built using IBM Watsonx infrastructure, all patient data is processed using PIPEDA-compliant systems designed to protect healthcare information and ensure privacy. How We Built It Halo is built as a modular system combining voice AI, computer vision, and large language model reasoning. The backend is implemented in Python using FastAPI and Flask, with MongoDB used to store call histories, patient responses, and structured clinical outputs. The voice pipeline uses IBM Watson Speech-to-Text for real-time transcription and IBM Watson Text-to-Speech to generate natural spoken responses during automated patient calls. Patient responses are processed using IBM Watsonx running the Mistral Small model, which converts transcripts into structured clinical outputs such as symptom summaries and urgency levels. OpenSMILE runs in parallel to extract acoustic features such as pitch, jitter, and pause patterns, allowing the system to analyze vocal cues that may indicate distress or fatigue. For safety monitoring, a computer vision module built with OpenCV and MediaPipe analyzes body pose to detect fall events and trigger automated alerts. On the frontend, a real-time hospital monitoring interface renders a 3D floor plan of the facility where rooms are color-coded by urgency. Clinicians can explore individual patients and view symptoms mapped onto a 3D anatomical model built using 3GS. All system components communicate through FastAPI REST endpoints, and sensitive patient data is handled using IBM Watsonx’s PIPEDA-compliant infrastructure to ensure healthcare privacy protections. What We Accomplished During the hackathon, we successfully built a working prototype that connects automated patient outreach with real-time hospital monitoring. We implemented a live nurse alert system that triggers in real time based on patient responses during AI-driven check-ins. We also deployed a fall detection module capable of identifying potential fall events and immediately initiating automated alerts and follow-up communication. Most importantly, we demonstrated how Halo can transform patient conversations into structured clinical insights and visual triage data that clinicians can act on immediately. Challenges We Faced One of the main challenges was coordinating three concurrent AI pipelines: voice processing, computer vision monitoring, and LLM reasoning. Ensuring that these components could run simultaneously without blocking each other required careful system design and asynchronous processing. Another challenge involved building the 3D hospital environment and anatomical visualization system. Creating a realistic floor model and integrating it with live patient data required learning new visualization tools while ensuring the interface remained intuitive for clinical use. What We Learned During the hackathon, we learned how to integrate IBM Watsonx APIs into a real-time clinical workflow system. We also explored how enterprise AI systems must be designed with strict privacy protections. IBM Watsonx’s PIPEDA-compliant infrastructure ensures that sensitive healthcare data is processed securely and handled according to Canadian privacy standards, which is essential when building systems intended for clinical environments. What’s Next In future iterations, we plan to extend Halo’s capabilities by leveraging historical patient data stored securely within IBM Watsonx’s PIPEDA-compliant infrastructure. Using this data, Halo could introduce predictive modeling to anticipate symptom deterioration or disease progression before it occurs. By identifying patterns across previous patient interactions and recovery trajectories, the system could alert clinicians earlier and allow preventative interventions to be put in place. <div