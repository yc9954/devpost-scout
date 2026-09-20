---
slug: "medqtrack"
url: "https://devpost.com/software/medqtrack"
title: "MedQTrack"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 618
team_size: 0
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MedQTrack

> Healthcare Operations, Done Right

[Devpost](https://devpost.com/software/medqtrack) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[civic_government]] [[health_clinical]] [[supply_logistics]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]
  <sub>weak: document_pdf</sub>

**stack** css, firebase, github, groq, gtts, javascript, llama, multer, natural-language-processing, node.js, ocr, pdf-parser, react, tesseract

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for medqtrack

## Body

Inspiration Hospitals still rely heavily on manual registers, Excel sheets, and disconnected systems. Patients wait for hours in OPD queues without updates. Staff manually track bed availability, causing delays in admissions. Pharmacy teams struggle with stock tracking and expiry management. We were inspired to build a unified, intelligent hospital management platform that connects all departments in real time — eliminating delays, confusion, and inefficiencies. What it does Smart OPD Queue Management: Automatically generates and allocates patient tokens Predicts waiting time dynamically based on live queue length Updates patient position in real time Allows doctors to call the next patient through a dashboard Synchronizes instantly across all devices SMART Digital Bed Management System: Maintains a live visual map of hospital beds Tracks status: occupied, available, under cleaning Updates instantly when admissions or discharges occur Prevents admission delays caused by manual tracking Also tracks which bed has all equipments like oxygen supply , vital monitor , infusion pumps etc (A Bed is is marked available ONLY if its well EQUIPED.)(ADDED) Intelligent Inventory Monitoring: Tracks stock levels in real time Generates automatic low-stock alerts Flags medicines nearing expiry Maintains department-wise inventory visibility AI-Generated Medical Summary(ADDED) Aggregates patient history and previous reports Generates a structured summary before consultation Reduces manual review time for doctors Whatsapp-Based Appointment Booking Patients can book appointments by simply sending “Hi” Collects essential details (name, age, gender, etc.) Automatically assigns a token Enables real-time token tracking Doctor-Initiated Voice Triage(ADDED) Doctors can start voice triage directly from the dashboard AI Generates both audio and text summaries , and this summary sent to patient's Whatsapp number. Ensures accessibility for blind and deaf patients Improves communication without requiring manual interaction Voice Triage & Accessibility (WCAG 2.1 Compliant) (ADDED) Blind patients can book appointments through voice-based triage Global hotkey (e.g., Spacebar / Alt+V) instantly activates the microphone Fully navigable using voice + keyboard only Designed to meet WCAG 2.1 accessibility standards How I built it TypeScript for scalable and maintainable development Firebase Authentication for secure user access Firebase Firestore for real-time cloud database Whatsapp Cloud API for booking through whatsapp , and sending audio / text summaries to whatsapp. Voice Triage Booking is Implemented using Web Speech API (browser-based speech-to-text) AI Audio + Text Summary Generation :Patient data Sent to an LLM API with a structured prompt: Python with gTTS (Google Text-To-Speech) for converting medical summaries into audio messages for visually impaired patients. Whisper (v3): High-accuracy Speech-to-Text for voice triage. Tesseract.js: OCR for extracting text from medical report images. Challenges I ran into Implementing accurate wait-time prediction logic Managing role-based access for doctors, staff, and administrators Speech Recognition Accuracy: Background noise and accents caused incorrect inputs(Solved by Adding confirmation steps (“Did you say X?”)) WhatsApp API Integration Complexity:Webhook setup, message templates, and approvals were tricky Accessibility Edge Cases: Ensuring full keyboard navigation across all flows , Making sure audio + text outputs are always available What I learned Designing real-time distributed systems using Firebase Firestore and event listeners Creating modular frontend architecture for independent yet connected modules (OPD, beds, inventory) Implementing wait-time prediction logic based on dynamic queue data Designing alert systems using threshold-based triggers (low stock, expiry tracking) Text summarization using Tesseract Raw AI output can be inconsistent, so I learned to use prompt structuring + formatting. THE BIGGEST CHALLENGE WASN’T BUILDING FEATURES — IT WAS MAKING EVERY FEATURE WORK SEAMLESSLY FOR EVERY KIND OF USER, INCLUDING THOSE WHO CAN’T SEE OR HEAR. What's next for MedQTrack Improve AI accuracy for medical summaries Make a floor based plan for bed tracking. Explore government partnerships for large-scale deployment Help hospitals forecast:Patient load , Bed demand , Medicine consumption Expand voice triage to Hindi + regional languages for wider accessibility in India <div