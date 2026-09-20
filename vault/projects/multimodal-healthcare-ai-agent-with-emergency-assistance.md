---
slug: "multimodal-healthcare-ai-agent-with-emergency-assistance"
url: "https://devpost.com/software/multimodal-healthcare-ai-agent-with-emergency-assistance"
title: "Multimodal Healthcare AI Agent with Emergency Assistance"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 749
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Multimodal Healthcare AI Agent with Emergency Assistance

> Multimodal healthcare AI agent that understands speech and images, delivers voice responses, enables medical chat ,generates reports and save report history, and provides emergency hospital guidance.

[Devpost](https://devpost.com/software/multimodal-healthcare-ai-agent-with-emergency-assistance) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** agent-based, elevenlabs, google-maps, gradio, groq-(speech-&-vision), python, sqlalchemy, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for multimodal healthcare ai agent with emergency assistance

## Body

Personal health dashboard where users can upload medical reports and automatically extract key health metrics for monitoring. Secure login and signup system allowing users to create accounts and access their personal AI healthcare assistant and health dashboard. When an emergency is detected, the system recommends nearby hospitals with directions and contact details for immediate help. The AI doctor understands patient queries and responds in Hindi, demonstrating multilingual consultation support for regional accessibility. The dashboard visualizes blood pressure, sugar, and cholesterol trends with severity indicators to track patient health over time. The AI doctor provides consultation responses in Bangla, showing the system’s multilingual capability for better accessibility. Inspiration Many people find it difficult to explain their symptoms by typing everything manually. In stressful situations, speaking or sharing a medical image is much easier. Most healthcare tools also lack memory and cannot track a patient's health over time. We wanted to build an AI assistant that feels more like a real healthcare helper — one that understands voice, images, and text, remembers past interactions, and helps users monitor their health. What it does Our project is a multimodal healthcare AI agent that allows users to interact using speech, chat, or medical images. The system simulates a structured medical consultation and provides intelligent responses similar to a doctor. Users can: • Speak symptoms or type questions to the AI doctor • Upload medical images for visual analysis • Receive doctor-like responses with realistic voice output • Generate structured medical reports • Save and access previous consultation reports We also introduced a Health Dashboard where users can upload medical reports such as blood test reports. The system automatically extracts key medical parameters like: Blood Pressure Blood Sugar Cholesterol It then classifies the severity (Normal, Warning, High Risk) and stores these metrics over time. The dashboard visualizes health trends through graphs, helping users monitor their condition and detect potential health risks early. The system also includes an emergency assistance agent that detects urgent situations and recommends nearby hospitals with directions and contact information. Additionally, the platform now supports multiple languages, allowing users to receive consultation responses and voice output in their preferred language, making the system more accessible for regional users. How we built it The system uses an agent-based architecture. Speech is transcribed using Groq, and medical images and reports are analyzed using a multimodal vision-language model. To improve reliability, we integrated WHO guideline–based Retrieval Augmented Generation (RAG) so responses are grounded in medical knowledge. Health metrics extracted from reports are stored in a database and visualized in the dashboard. For emergencies, a dedicated agent uses the Google Maps API to locate nearby hospitals. We also integrated ElevenLabs for natural doctor voice responses and built the interface using Gradio. Challenges we ran into Handling multiple input types in one workflow was challenging. We had to design a reliable intent routing system, extract structured data from different medical report formats, and maintain conversation memory while coordinating multiple AI agents. Accomplishments that we're proud of We’re proud that the project evolved beyond a simple chatbot into a complete AI-powered healthcare workflow. Key features we successfully implemented include: • Multimodal consultation with speech, chat, and image inputs • AI-generated structured medical reports • Persistent report history and user dashboard • Automated extraction of health metrics from uploaded reports • Severity classification for blood pressure, blood sugar, and cholesterol • Health trend visualization through interactive graphs • Emergency hospital discovery and navigation support • Multilingual responses with realistic doctor voice output These capabilities make the system feel more like a practical healthcare assistant rather than just a prototype. What we learned Through this project we learned how to design AI agent workflows, integrate multimodal AI systems, build retrieval-based medical reasoning pipelines, and structure LLM outputs for real-world applications. We also gained experience connecting AI models with backend systems, APIs, databases, and user interfaces to create a full end-to-end product. What's next for Multimodal Healthcare AI Agent with Emergency Assistance Moving forward, we plan to expand the system with more advanced healthcare features. Future improvements include: • Advanced patient severity scoring and risk prediction • A doctor dashboard for monitoring multiple patients • Support for additional regional languages • Integration with wearable health devices for real-time monitoring • Offline-capable versions for rural healthcare environments • Expanded medical knowledge integration to further align responses with WHO clinical guidelines Our long-term goal is to create a scalable AI healthcare assistant that improves accessibility, early detection, and patient awareness worldwide. <div