---
slug: "wingnote"
url: "https://devpost.com/software/wingnote"
title: "WingNote"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 843
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/mental_health"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# WingNote

> WingNote – Smart hardware meets AI-powered documentation to listen, structure, and simplify care for nurses and patients.

[Devpost](https://devpost.com/software/wingnote) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]] [[health_clinical]] [[housing_homeless]] [[mental_health]]
**user** [[clinician]] [[patient_family]]
**substrate** [[medical_record]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** arduino-nano, deepgram, gemini, li-po-battery, mistral-ai, next.js, openai, perplexity-api, python, rfid-reader, supabase, typescript, vercel, vercel-v0

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wingnote?

## Body

WingNote device WingNote EHR Inspiration Nurses spend over 4 hours per shift on documentation, leading to burnout, high turnover rates, and reduced patient care time. At the same time, most patients don’t understand their own medical notes, creating a gap in healthcare accessibility. We set out to build WingNote —a fully integrated hardware + AI-powered solution that automates nurse documentation while ensuring patients receive clear, personalized summaries in their preferred language and at their reading level. With a tap of an RFID badge , a nurse can start recording a patient interaction, and AI does the rest—transcribing, analyzing, structuring, and presenting the information in an EHR-ready format , while also generating a patient-friendly summary . What it does WingNote is a smart badge & AI-powered software system that automates clinical documentation for nurses and improves patient understanding. Hardware RFID-based patient identification – Scans patient wristbands to log patient ID. Power efficient audio & video syncing – Captures speech & patient behavior for every interaction throughout the day. Xiao ESP32-S3 smart badge – Microphone, camera, and Wi-Fi enables wireless transmission of real-time data. Custom 3D-printed housing – Encases ESP32, RFID reader, and patient wristbands for hospital use. AI-powered software Speech recognition (Deepgram API) – Converts nurse-patient dialogue into detailed, diatorized text. Vision analysis (Gemini 2.0 Flash) – Identifies helpful details about the patient and room to enhance notes. EHR structuring (Mistral AI) – Transforms raw conversation into Epic-compatible notes. Doctor’s review portal (Next.js/Vercel v0) – Physicians edit & approve AI-generated documentation. Patient summary app (Next.js/Vercel v0) – Provides multilingual, easy-to-read summaries of doctor's notes. Patient Q&A (Perplexity Sonar API & Postgres SQL) – Patients can receive reliable medication answers grounded in their doctor's notes and web data. WingNote fully automates the documentation pipeline, improving workflow efficiency and patient care. How we built it Hardware stack Xiao ESP32-S3 Sense – Microcontroller with Wi-Fi, camera, and microphone. RC522 RFID reader – Used for patient wristband scanning. Arduino Nano (I2C bridge) – Converts SPI to I2C to allow RFID to work over a retractable wire. Custom 3D-printed cases for: Smart badge (ESP32-S3 with mic & camera). RFID reader & Arduino Nano (compact with retractable cable). Patient wristband (RFID tag enclosed for easy scanning). Software stack Deepgram API – Speech-to-text transcription with enhanced medical-grade accuracy and speaker identification. Gemini 2.0 Flash API – Patient behavior tracking. Mistral AI – Converts conversation data into structured EHR notes. Next.js/Vercel v0 – Doctor's portal → EHR-ready notes for review & approval. Patient’s portal → Multilingual, age-adapted health summaries. Perplexity API – Provides LLM responses grounded in web data Supabase - Postgres SQL database and cloud storage for notes and artifacts From hardware to AI-powered documentation, we built WingNote from the ground up. Challenges we ran into RFID integration with ESP32-S3 The RC522 RFID module requires 6 wires , but the retractable cable we used only had 4 wires . Solution: Introduced an Arduino Nano as an I2C bridge , converting: RFID Reader (SPI, 6-wire) → Arduino Nano (SPI to I2C) → ESP32-S3 (4-wire I2C). Dual serial communication on Xiao ESP32-S3 Initially, we tried using two UART ports simultaneously, but the ESP32-S3 couldn’t support dual UART for both the computer and the RFID unit . Solution: Switched RFID communication to I2C and kept UART free for debugging. Power efficient data transmission over Wi-Fi Issue: ESP32-S3 couldn’t stream high-resolution video & audio simultaneously and it takes a lot of battery to do so continuously . Solution: Store audio and video locally on the device while filming. Transfer audio and video between appointments to save on battery and improve quality. Reliably transferring data between the hardware and software remains a significant challenge. Overcoming these challenges led to a fully functional, AI-powered clinical documentation system. Accomplishments that we're proud of Built a complete hardware + AI solution from scratch . Seamless RFID scanning + multimodal AI processing (speech + video). Fully functioning real-time documentation workflow (nurse → AI → doctor → patient). Deployed an AI-powered patient portal that enhances healthcare accessibility. Integrated Deepgram, Gemini 2.0, Perplexity, and Mistral AI to process medical documentation. WingNote is a fully operational, AI-enhanced documentation system that works end-to-end. What we learned Embedded systems development – Learned how to interface ESP32-S3, RFID modules, and I2C communication. AI workflow optimization – Successfully merged audio & vision AI into a seamless pipeline. Real-time AI integration – Implemented low-latency STT + vision analysis with structured data formatting. Hardware design & 3D printing – Designed & printed custom enclosures for smart badges, RFID readers, and wristbands. This project pushed us to solve real-world hardware & AI integration challenges. What's next for WingNote? Direct EHR integration (Epic, Cerner, etc.) Currently, doctors review AI-generated notes in our portal, but future versions will push data directly into EHRs. Real-time transcription for nurse efficiency Currently, transcription happens after the visit, but we plan to add live transcription during conversations . Wider language support Expanding multilingual AI summaries & patient Q&A support for even more languages. WingNote is just getting started—our vision is to make documentation completely seamless. <div