---
slug: "medical-report-analyzer-healthy-habits-recommender"
url: "https://devpost.com/software/medical-report-analyzer-healthy-habits-recommender"
title: "Medical Report Analyzer & Healthy Habits Recommender"
hackathon: "HP & NVIDIA Developer Challenge"
organization: "HP"
winner: true
words: 382
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Medical Report Analyzer & Healthy Habits Recommender

> This application provides a simple web interface to generate summaries, health suggestions, and food recommendations from medical documents (PDFs or images)

[Devpost](https://devpost.com/software/medical-report-analyzer-healthy-habits-recommender) · hackathon [[HP - NVIDIA Developer Challenge]]

## Facets

**mechanism** [[vision_ocr]]
  <sub>weak: cross_origin_web</sub>
**domain** [[agriculture_food]] [[elder_child_care]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** llama, llm, openai, prompt, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for medical report

## Body

Main Page Suggestions Inspiration Every year during my annual hospital checkups, I receive multiple test reports. Some values are normal, while others need improvement. But after a few days, I tend to forget about them. I wanted a solution that could analyze my reports, remind me of areas to improve, and suggest actionable health habits so I can stay on track year-round. This project was inspired by that need—to have an intelligent assistant that turns my medical data into daily, personalized health advice. What it does Accepts medical documents (PDFs, scans, images) Uses OCR to extract structured medical data Summarizes doctor’s notes and prescriptions using GPT Generates personalized: Health summaries Few health habit suggestions Few food/nutrition suggestions Stores data per user profile and avoids duplicate document processing Recommends habits based on entire user history, not just one report How we built it Backend: Python Frontend: HTML UI OCR: Tesseract for extracting text from images AI Engine: OpenAI GPT/Llama2 local model for summarization and suggestions Model Management: MLflow for model versioning and deployment Platform: Deployed and tested on HP AI Studio The pipeline automatically connects uploaded files → OCR → GPT prompt creation → response processing → user-specific output generation. Challenges we ran into Parsing inconsistent formats across medical reports Handling poor-quality scanned images for OCR Designing prompts that produce medically accurate summaries and suggestions Avoiding redundant processing of the same report multiple times Deployment issues with GitHub and HP AI Studio integration Accomplishments that we're proud of Fully functional end-to-end system: upload → analyze → actionable insights Automatically detects duplicate uploads to save compute and time Personalized health & food suggestions based on real medical context Intuitive and clean interface with minimal setup Packaged model using MLflow for reproducibility What we learned Effective ways to combine OCR + LLMs for real-world document processing How to build self-adaptive prompts for variable medical data Streamlining model lifecycle with MLflow Leveraging HP AI Studio’s deployment stack for app hosting and testing Importance of user-centric design for medical applications What's next for Medical Report Add multi-language support for reports in regional languages Enable continuous habit tracking and notifications via email or mobile app Integrate basic health visualizations (charts/trends) Include more advanced medical models for deeper insights Add voice-based interaction for elderly or visually impaired users <div