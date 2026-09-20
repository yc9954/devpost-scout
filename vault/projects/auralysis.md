---
slug: "auralysis"
url: "https://devpost.com/software/auralysis"
title: "Auralysis"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 396
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Auralysis

> Auralysis is an AI medical imaging system that diagnoses MRI/X-ray scans, generates reports, explains results with ElevenLabs voice output, and is fully monitored with Datadog.

[Devpost](https://devpost.com/software/auralysis) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[health_clinical]] [[transportation]]
**user** [[clinician]] [[patient_family]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** api-handling, datadog, efficientnetv2b0, elevenlabs, fastapi, flutter, gemini, google, groq, latency-&-error-tracking-railway-?-llm-+-tts-pipeline-deployment-&-environment-variables-render-?-ml-model-inference-hosting-android-/-mobile-app-?-frontend-for-uploading-scans-&-receiving-results-dotenv-?-requests-?-pil-?-numpy-?-preprocessing, llama, llm, metrics, railway

## How they structured the write-up

- 🧠 auralysis
- 💡 inspiration
- ⚙️ what it does
- 🛠️ how i built it
- 🚧 challenges
- 🏆 accomplishments
- 📚 what i learned
- 🔮 what’s next
- ❤️ final thoughts

## Body

Diagnose. Explain. Report 🧠 Auralysis AI-powered medical image diagnosis, reporting, explanation, and doctor-style voice output. 💡 Inspiration Healthcare reports are often slow, unclear, and difficult for patients to understand. MRI and X-ray interpretation requires expert review, which isn’t always instantly available. Auralysis started with a simple question: What if an AI could diagnose medical images and also explain the results clearly in a doctor’s voice? This led to building a system that diagnoses, reports, explains, and speaks medical insights automatically. ⚙️ What It Does Auralysis performs a complete end-to-end medical AI pipeline: Predicts disease class using a TensorFlow model Generates a structured clinical report using Groq LLaMA Simplifies the explanation for patients using Gemini Converts the summary into a doctor-style audio output using ElevenLabs Tracks latency, errors, requests, and confidence using Datadog Pipeline: Diagnose → Report → Explain → Speak 🛠️ How I Built It 🧪 Model Training Dataset: 5400 MRI & X-ray images 6 medical classes Model: EfficientNetV2B0 (TensorFlow/Keras) Validation accuracy: 86.94% ☁️ Render ML Inference API Exported TensorFlow SavedModel Built FastAPI inference service Returns prediction, confidence, and probabilities Deployed on Render as a scalable inference microservice 🧩 Railway Backend (Pipeline Brain) Handles the full pipeline: Groq LLaMA → structured JSON medical report Gemini → simplified patient-friendly summary ElevenLabs → doctor-style MP3 voice report Datadog → live monitoring of every request 📱 Flutter Mobile App Users can: Upload MRI/X-ray images Trigger the pipeline Receive diagnosis + detailed report Listen to a doctor-style spoken explanation 🚧 Challenges Managing flow between Groq → Gemini → ElevenLabs → Render Keeping LLM outputs stable and strictly JSON Reducing latency across cloud services Integrating Datadog metrics Securing API keys across platforms 🏆 Accomplishments Complete real-time medical AI pipeline Dual-LLM architecture for clarity and accuracy Automated voice-based medical reporting Full Datadog observability dashboard A mobile app delivering results in seconds 📚 What I Learned Production-grade ML deployment Multi-service AI orchestration Why observability matters for reliability AI explainability improves patient understanding Voice output greatly improves accessibility 🔮 What’s Next 🚀 Short Term Add more disease classes Improve severity scoring Add multilingual voice support 🏥 Long Term Doctor review portal Steps toward medical compliance CT/ultrasound image support Stronger LLM reasoning and validation ❤️ Final Thoughts Auralysis began as an attempt to make medical AI easier to understand. Now it diagnoses, explains, and speaks medical insights clearly. Clear diagnosis. Clear explanation. Clear voice. <div