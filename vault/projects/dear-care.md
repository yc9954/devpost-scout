---
slug: "dear-care"
url: "https://devpost.com/software/dear-care"
title: "Dear-Care"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 781
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/patient_family"
  - "substrate/video_visual"
---

# Dear-Care

> AI-powered voice healthcare assistant for rural India. Runs on edge, speaks 7 languages, measures vitals, scans prescriptions, generates clinical notes via Amazon Nova 2 Lite — works offline.

[Devpost](https://devpost.com/software/dear-care) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[health_clinical]] [[labor_employment]]
  <sub>weak: developer_tools, transportation</sub>
**user** [[patient_family]]
  <sub>weak: general_public, government_staff</sub>
**substrate** [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** ai, amazon-nova, arm64, bedrock, cloud-services, dart, dynamodb, flutter, healthcare, iot, lambda, polly, python, s3

## Body

Architecture Diagram Inspiration India's 900,000+ ASHA workers serve as the healthcare backbone for 600 million rural citizens — yet they work with paper forms, no diagnostic tools, and limited connectivity. We asked: what if an AI assistant could sit in their pocket, speak their language, measure vitals, read prescriptions, and make clinical decisions — even without internet? What it does Dear-Care is a voice-activated AI healthcare assistant that runs on the RDK S100 edge device. A health worker says "Hello Kamal" and the assistant guides them through a complete patient encounter: Identifies patients by Aadhaar number (spoken, extracted by Nova 2 Lite) Measures vitals — SpO2, heart rate (MAX30102), temperature (BMP280) via I2C sensors Scans prescriptions — camera capture → Textract OCR → Nova 2 Lite analysis Generates AI clinical notes — Lambda processes encounter data through Nova 2 Lite to produce health summaries, structured clinical notes, and triage reviews Speaks results back to the health worker in 7 languages via Polly Neural TTS Syncs to mobile — the Fit-U Flutter companion app receives verdicts via SNS push and DynamoDB, showing triage decisions and clinical recommendations on the worker's phone Works fully offline — every AWS service has a local fallback; data syncs automatically when connectivity returns How we built it Edge Device: 17 Python modules running on the RDK S100 (ARM64, Ubuntu 22.04, 4GB RAM) handling voice I/O, sensors, camera, encounter management, triage, and AWS integration AI Core: Amazon Nova 2 Lite via Bedrock for all reasoning — intent classification, Aadhaar extraction, prescription analysis, multi-turn health consultation, clinical notes generation, and triage review Voice Pipeline: Amazon Transcribe Streaming (STT) → Nova 2 Lite (reasoning) → Amazon Polly Neural (TTS) with Jabra mic and Bose Bluetooth speaker Cloud Pipeline: S3 encounter upload → Lambda invokes Nova 2 Lite for 3 actions (health summary, clinical notes, triage review) → results stored in DynamoDB → SNS push to mobile Mobile App: Flutter Fit-U app with offline-first SQLite cache, pedometer, geolocation, and REST sync via API Gateway 9 AWS services working together: Bedrock, Polly, Transcribe, Textract, S3, Lambda, DynamoDB, SNS, API Gateway Challenges we ran into RDK S100 camera: The SC230AI outputs RAW10 bitpacked Bayer data — no standard OpenCV capture works. We had to write custom demosaicing, gamma correction, and white-balance pipelines from scratch 4GB RAM constraint: Running PaddleOCR + Nova inference on a device with 4GB RAM required aggressive memory management and lazy loading Offline-first design: Every AWS service needed a working local fallback — pyttsx3 for Polly, SpeechRecognition for Transcribe, PaddleOCR for Textract, CSV/JSON for S3+DynamoDB, rule-based triage for Lambda I2C sensor reliability: MAX30102 pulse oximeter readings are noisy — we implemented averaging windows and outlier rejection to get clinically usable SpO2/HR values Cross-platform sync: Getting the Flutter app, two Lambda functions, API Gateway, DynamoDB, and SNS to work together seamlessly with proper error handling took significant iteration Accomplishments that we're proud of Complete end-to-end working system — from voice input on an edge device to AI clinical notes on a mobile phone, fully functional True offline capability — Dear-Care works in villages with zero connectivity, then auto-syncs when online 7-language support — a single device serves health workers across linguistic regions Nova 2 Lite handles everything — one model powers intent classification, Aadhaar extraction, prescription analysis, health consultation, clinical notes, triage review, and health summaries Real medical sensors — actual SpO2, heart rate, and temperature readings, not simulated data Privacy by design — Aadhaar masking, AES-256 encryption, PIN auth, 30-day auto-retention What we learned Edge AI is viable for healthcare — even a 4GB ARM64 device can orchestrate sophisticated AI workflows when combined with cloud services Amazon Nova 2 Lite is remarkably versatile — it handles medical reasoning, multilingual understanding, and structured data extraction from a single model Offline-first architecture is hard but essential — rural India's connectivity reality demands that every feature works without internet Hardware integration (I2C sensors, MIPI cameras, Bluetooth audio) on ARM64 Linux requires deep system-level debugging that no amount of documentation fully prepares you for What's next for Dear-Care Amazon Nova 2 Sonic integration for real-time voice-to-voice conversations, eliminating the STT→LLM→TTS pipeline latency Multi-modal diagnosis — using Nova's vision capabilities to analyze skin conditions, wound photos, and X-rays directly Regional language expansion — adding Tamil, Telugu, Bengali, Marathi, and Kannada for broader Indian coverage Fleet management dashboard — a web portal for district health officers to monitor all Dear-Care devices, track encounter volumes, and review AI triage decisions ABDM integration — connecting with India's Ayushman Bharat Digital Mission for standardized health records On-device fine-tuned models — distilling Nova's medical reasoning into smaller models that run entirely on the RDK S100 for zero-latency, zero-connectivity diagnosis <div