---
slug: "neuroscan-ai-shb8ag"
url: "https://devpost.com/software/neuroscan-ai-shb8ag"
title: "NeuroScan AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 445
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# NeuroScan AI

> An AI Powered Brain Tumor Detector for Radiologists

[Devpost](https://devpost.com/software/neuroscan-ai-shb8ag) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[video_visual]]
  <sub>weak: code_repository</sub>

**stack** ai-agent, airtable, automation, css, gemini-api, googlefonts, jupyter, keras, n8n, numpy, opencv, pillow, plotly, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges w##inspiration
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neuroscan ai

## Body

“Secure NeuroScan AI login screen for radiologists, with clean dark UI and demo credentials for controlled hackathon access.” Patient information for Diagnosis report Generation “NeuroScan AI main screen: upload MRI scans, view guidance, and interact with NeuroBot in one focused clinical workspace.” “Result view showing MRI image, tumor probability gauge, clear ‘Tumor Detected’ label, and one-click diagnostic report download.” "Result view Showing that no tumor is detected " this message will be shown when the uploaded image is different than MRI scan “NeuroBot Q&A panel where Radiologists ask neuroscience questions and get clear, structured explanations about brain tumors and the brain.” “NeuroScan AI sidebar explaining the problem, AI-driven solution, workflow steps, and clinical impact for radiologists.” Full Workflow by which the Diagnosis report automatically sent to the Email Address Automated Email of Diagnosis report of Patient through n8n Automation Automated Email of Diagnosis report of Patient through n8n Automation Inspiration What it does How we built it Challenges w##Inspiration Radiologists spend 45min per MRI analyzing brain tumors manually, fatigued after 100+ patients daily. Dangerous delays kill. We built a hospital-ready AI workflow to make detection instantaneous. ​ What it does 1) Detects brain tumors from MRI in 3 seconds (90% acc) . 2) Complete workflow: secure login → patient profiling → CNN analysis → confidence gauge → auto PDF reports → n8n email → Gemini NeuroBot patient education. 45min → 3sec . ​ How we built it 1) Frontend : Streamlit + glassmorphism UI (Poppins Google Font) 2) AI Core : Custom CNN (TensorFlow/Keras, 3-class: No Tumor/Tumor/Unsupported) 3) Visualization : Plotly interactive confidence gauges 4) Automation : n8n workflows (PDF → email) 5) Patient Education : Google Gemini 2.5 Flash NeuroBot 6) Deployment : Streamlit Cloud (100% uptime) Challenges we ran into 1) CNN rejecting poor-quality scans without false positives 2) n8n webhook reliability for clinical-grade automation 3) Balancing medical accuracy with 3-second inference speed Accomplishments that we're proud of 1) 90% accuracy on 1000+ real MRI scans 2) End-to-end production workflow (not just a model) 3) Live MVP : ( https://neuroscann-ai.streamlit.app/ ) 4) Youtube Video :- ( https://youtu.be/wSLeP_obpVo ) 5) Github Repository :-( https://github.com/AjayMudliyar/NeuroScan-AI.git ) 6) Google Gemini integration for patient education (unique) What we learned 1) Clinical workflows > isolated ML models 2) 3-class detection > binary (handles real hospital data) 3) n8n > custom backend for rapid automation 4) Glassmorphism UI increases doctor adoption 5) Transparent confidence scores build radiologist trust What's next for NeuroScan AI 1) Hospital partnerships, radiologist validation 2) Tumor localization, CT/PET support, DICOM integration 3) Global SaaS, multi-language NeuroBot, FDA pathway e ran into Accomplishments that we're proud of What we learned What's next for NeuroScan AI <div