---
slug: "medlens-ai"
url: "https://devpost.com/software/medlens-ai"
title: "MedLens Ai"
hackathon: "ERNIE AI Developer Challenge"
organization: "Baidu"
winner: true
words: 527
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "domain/media_journalism"
  - "domain/mental_health"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# MedLens Ai

> MedLens AI: Humanizing medical reports with AI clarity. Why it works: It focuses on the "human" aspect of healthcare and addresses the problem of complex jargon.

[Devpost](https://devpost.com/software/medlens-ai) · hackathon [[ERNIE AI Developer Challenge]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[health_clinical]] [[media_journalism]] [[mental_health]]
  <sub>weak: developer_tools</sub>
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[medical_record]] [[sensor_telemetry]] [[video_visual]]

**stack** ai-&-machine-learning:-paddleocr-(vision), axios-infrastructure-&-devops:-docker, backend:-python, docker, ernie, fastapi, fastapi-ai-&-machine-learning:-paddleocr-(vision), hugging-face-spaces-(gpu/ram-backend), novica, novita-ai-(llama-3-70b-llm), pymupdf-frontend:-react.js, tailwind-css, vercel, vercel-(frontend)-apis:-novita-ai-openai-compatible-api-data-storage:-local-json-based-persistent-storage-(history)-tools:-git

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for medlens ai

## Body

Inspiration We’ve all been there: sitting in a doctor's waiting room, clutching a piece of paper filled with cryptic abbreviations, complex metrics, and medical jargon. The gap between receiving a medical report and actually understanding it can be filled with anxiety and misinformation from "Dr. Google." We were inspired to build MedLens AI to bridge this gap. Our mission was simple: create a "lens" that translates the complexity of medical documents into clear, actionable, and trustworthy insights that anyone can understand, regardless of their medical background or language. What it does MedLens AI simplifies medical documents into clear, actionable health insights: High-Precision OCR: Instantly extracts text from medical photos and multi-page PDFs. AI Analysis: Summarizes reports, identifies diagnoses, and explains medications . Medical Chatbot: Allows users to ask follow-up questions directly about their document. Multilingual: Supports English, Arabic, and French for global healthcare accessibility. Patient History: Securely tracks and stores past analyses for long-term health monitoring. How we built it MedLens AI is built on a high-performing "AI-First" architecture: The Brain: We integrated ERNIE-4.5-21B-A3B-Thinking via Novita AI to ensure deep medical reasoning. We used advanced prompt engineering to ensure the AI provides structured summaries, extracts diagnoses, and explains medications clearly. The Vision: PaddleOCR was chosen for its exceptional accuracy in recognizing technical medical text and tables, even from low-quality mobile scans. The Engine: A FastAPI backend designed for high-concurrency, handling heavy OCR processing through a Dockerized environment. The Interface: A clean, empathetic React frontend built with a "Step-based" flow to reduce user cognitive load during stressful medical situations. Challenges we ran into One of our biggest hurdles was resource constraints. High-precision OCR models like PaddleOCR are memory-intensive. Deploying a 1GB+ engine on standard "free tier" cloud providers (which often limit RAM to 512MB) caused constant crashes. We solved this by architecting a Dockerized backend for Hugging Face Spaces, leveraging their 16GB RAM tier to ensure snappy, reliable medical processing. We also faced the challenge of data diversity. Medical reports come in many formats (handwritten prescriptions vs. digital lab results). We had to refine our OCR extraction logic to handle various layouts and edge cases like multi-page PDFs. Accomplishments that we're proud of Medical-Grade OCR: High-precision text extraction from messy mobile photos using PaddleOCR. Multi-language Support: Full healthcare clarity in English, Arabic (RTL), and French. Resource Optimization: Successfully deployed a memory-intensive AI engine on free-tier cloud infrastructure. Expert AI Reasoning: Precise medical summaries and medication explanations . Premium Full-Stack Build: A production-ready platform with history, chat, and a hospital-grade UI. What we learned Building MedLens AI was a masterclass in: MLOps: Learning how to containerize and optimize heavy computer vision libraries for production. Ethics in AI: Deeply considering the importance of medical disclaimers and the fine line between "explaining" and "diagnosing." User-Centric Design: Learning that in healthcare tech, "minimalism" isn't just an aesthetic—it's a way to provide calm during a user's moment of need. What's next for MedLens Ai We want to expand MedLens to support even more languages and integrate with wearable health data. Ultimately, we see MedLens AI as a companion tool that empowers patients to have more informed, confident conversations with their actual doctors. <div