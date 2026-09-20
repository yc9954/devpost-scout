---
slug: "doclyst"
url: "https://devpost.com/software/doclyst"
title: "Doclyst"
hackathon: "ERNIE AI Developer Challenge"
organization: "Baidu"
winner: true
words: 978
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Doclyst

> Doclyst is a purpose-built medical safety interpreter. It turns complex medical reports into clear, human-readable explanations with safety alerts in under 30 seconds.

[Devpost](https://devpost.com/software/doclyst) · hackathon [[ERNIE AI Developer Challenge]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** ernie, flask, paddleocr, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what is next for doclyst

## Body

Mockup Inspiration Last year, my grandmother received a blood test report. She stared at it for hours, confused by terms like "lymphocytes" and "MCV." She called me in tears, convinced something was terribly wrong. It turned out everything was normal. She just could not understand the report. This happens to millions of people every day. Medical reports are written for doctors, not patients. The result? Panic, confusion, and sometimes dangerous decisions like skipping follow-ups or self-medicating based on misunderstood results. We asked ourselves a simple question: What if anyone, regardless of education or language, could understand their own health? Doclyst was born from that question. What it does Doclyst transforms complex medical reports into clear, human-readable explanations in under 30 seconds. Upload any medical report (blood tests, X-rays, ECGs) as a PDF or image, and Doclyst will: Extract text using advanced OCR technology Analyze each test result and explain what it means in simple language Flag urgent findings with a color-coded safety triage system (Green, Yellow, Red) Provide anti-panic guidance including "What this does NOT mean" and "Questions to ask your doctor" Compare old and new reports to track health changes over time Read results aloud in 5 languages (English, Bengali, Hindi, Chinese, Spanish) Generate a downloadable PDF summary to share with family or doctors Doclyst does not diagnose. It does not prescribe. It simply helps patients understand their own health data so they can have better conversations with their doctors. How we built it We designed Doclyst with a dual-fallback architecture to ensure reliability and showcase sponsor technologies. OCR Pipeline: Primary: PaddleOCR (Baidu) via Gradio for accurate text extraction from medical documents Fallback: OCR.space API for edge cases LLM Pipeline: Primary: ERNIE (Baidu) for medical text analysis and explanation generation Fallback: Groq (Llama 3.3 70B) for high-speed inference when needed Frontend: React with TypeScript for type-safe, responsive UI Custom anti-panic UX design with calming colors and reassuring language Multi-language support with real-time translation Google TTS integration for voice read-aloud feature Backend: Flask REST API deployed on Render Stateless architecture with no data storage for privacy gTTS for server-side text-to-speech generation Key Design Decisions: No user accounts or data storage to protect patient privacy Rule-based urgency flagging combined with LLM explanations for safety Culturally sensitive, non-alarming language across all supported languages Challenges we ran into The "Doctor Language" Problem: Medical terminology is precise but intimidating. Finding the balance between accuracy and accessibility was our biggest challenge. We spent hours crafting prompts that explain without oversimplifying or causing unnecessary alarm. Handling Report Variety: Medical reports come in hundreds of formats. Lab reports from different hospitals, handwritten notes, ECG printouts. We had to build a flexible system that does not rely on rigid parsing but instead lets the LLM understand context. CORS and TTS Integration: Browser-based text-to-speech has inconsistent language support. We pivoted to a backend TTS solution using gTTS, which required building a proxy endpoint to avoid CORS issues while maintaining low latency. Fallback Orchestration: Ensuring seamless failover between PaddleOCR and OCR.space, and between ERNIE and Groq, without user-visible delays required careful error handling and timeout management. Multi-language Voice: Supporting Bengali, Hindi, and Chinese voice output meant dealing with character encoding issues and finding TTS services that actually sound natural in these languages. Accomplishments that we are proud of Real Impact Potential: We built something our own families can use. My grandmother can now upload her reports and hear explanations in Bengali. That alone makes this project meaningful. Safety-First Design: Unlike generic AI chatbots, Doclyst never diagnoses. Every response includes disclaimers, and our triage system errs on the side of caution. Yellow means "ask your doctor," not "you might be fine." Anti-Panic UX: We are proud of the "What this does NOT mean" section. It directly addresses the anxiety patients feel and provides actionable next steps instead of leaving them to spiral. Sponsor Technology Integration: PaddleOCR and ERNIE are not just checkboxes. They are the primary engines powering Doclyst. We built fallbacks for reliability, but the Baidu stack handles the majority of requests. Accessibility: Five languages. Voice read-aloud. PDF export. We wanted Doclyst to work for a 70-year-old in rural Bangladesh and a busy professional in New York. We think we got close. What we learned AI is not magic, but it can be kind: The real power of LLMs is not in replacing doctors. It is in translating expertise into understanding. We learned to use AI as a bridge, not a replacement. UX matters more than features: Early versions had more features but felt clinical and cold. Stripping back to essentials and focusing on emotional design made Doclyst actually usable. Fallbacks are not optional: In healthcare-adjacent applications, reliability is everything. Building redundancy from day one saved us during demos when APIs had hiccups. Prompts are products: We rewrote our ERNIE prompts dozens of times. The difference between a scary explanation and a reassuring one often came down to a single sentence in the prompt. What is next for Doclyst Expanded Report Support: We want to add support for radiology images (X-rays, MRIs) using ERNIE's multimodal capabilities. Not for diagnosis, but for helping patients understand what their doctor is looking at. Doctor Dashboard: A companion tool where doctors can review AI-generated summaries before sharing with patients, adding their own notes and recommendations. Offline Mode: Many users in developing countries have limited internet. We are exploring on-device OCR and cached explanations for common test types. Integration with Health Records: Partnerships with hospitals and labs to automatically generate patient-friendly summaries alongside official reports. More Languages: Arabic, French, Portuguese, and regional Indian languages are on our roadmap. Healthcare should not have a language barrier. Doclyst started as a hackathon project, but the problem it solves is real and urgent. Millions of people receive medical reports they cannot understand every single day. We want to change that, one report at a time. <div