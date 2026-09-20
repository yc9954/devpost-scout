---
slug: "live-privacy-shield"
url: "https://devpost.com/software/live-privacy-shield"
title: "PrivaStream"
hackathon: "TikTok TechJam 2025"
organization: "TikTok"
winner: true
words: 447
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# PrivaStream

> Protecting Privacy in Real Time, One Frame at a Time

[Devpost](https://devpost.com/software/live-privacy-shield) · hackathon [[TikTok TechJam 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[retrieval_grounding]] [[structural_withholding]] [[vision_ocr]] [[voice_speech]]
  <sub>weak: agriculture_food, civic_government, finance_payments, security_privacy, supply_logistics</sub>
**substrate** [[structured_db]] [[transcript_audio]] [[video_visual]]
  <sub>weak: document_pdf, geospatial</sub>

**stack** flask, nextjs, node.js, opencv, python, pytorch, whisper

## Body

Demo (old) Poster Architecture Diagram F1-Confidence Curve Precision-Recall Curve Precision-Confidence Curve Recall-Confidence Curve Inspiration 💡 In the age of live streaming, creators often expose sensitive information by accident—faces of bystanders, license plates, on-screen documents, or even credit card numbers. On TikTok Live especially, streams are fast-paced and unedited. Current privacy solutions work after the damage is done, leaving creators vulnerable in real time. This is the problem we set out to solve. We wanted to build a production-ready, real-time privacy filter for Tiktok livestreams and across other platforms. Key Features ✨ 🎥 Real-time Video PII Blur Face detection with whitelist support License plate detection (97.62% mAP50) Text PII blur (OCR + ML classification) 🎵 Audio PII Detection Faster Whisper speech-to-text processing Silero VAD to filter silence Fine-tuned DeBERTa (96.99% accuracy - SOTA) Real-time mouth blur sync with audio Overall Flow 🔀 How We Built It 🛠️ Datasets: Audio: ~70k samples (Kaggle PII-DD, Mixtral essays, + custom 2k dataset). License plates: Singapore License Plate Dataset (Roboflow, ~9k images). On-screen text: ICDAR2015 incidental scene text benchmark. Whitelist faces: InsightFace crops with ArcFace embeddings. Training: Ensemble of 10 DeBERTa models across 7 groups with weighted voting (Optuna). Aggressive data augmentation (blur, glare, HSV jitter) for license plates. Logistic Regression classifier with TF-IDF n-grams for OCR PII classification. Latency & Scalability ⚡ Video redaction : ~150 ms per frame at 720p30. Audio redaction : ~2–4 s per utterance (Faster-Whisper + DeBERTa ensemble). Scaling : One Azure NC40ads H100 v5 node supports 15–20 concurrent 1080p30 streams with batching + TensorRT. Production-ready : Modular microservices + default-to-blur fail-safes ensure privacy is never bypassed. Accomplishments We're Proud Of🏆 State-of-the-art audio privacy : 96.988% precision, 98.34% classification accuracy, surpassing prior DeBERTaV3 benchmarks. Robust video protection : License plates – Recall 97.16% , Precision 95.01% , mAP\@0.5 97.62% . OCR PII – Recall 98.69% , Precision 97.01% . Whitelist face blur – 98.38% accuracy in distinguishing creator vs. bystanders. Security 🔐 Face data safety : PrivaStream never stores actual faces — it only keeps anonymized embeddings (numerical signatures), making it impossible to reconstruct the original image. Audio safety : Spoken content is processed into token-level transcripts and embeddings for PII tagging; raw audio is never stored . After analysis, transcripts are discarded and only the anonymized, redacted audio continues in the stream. Default-to-blur & mute fail-safes : If a detection fails, video regions are blurred and audio is muted by default to guarantee privacy-first output. What’s Next 🚀 Voice anonymization – pitch shift / bleep for sensitive speech. Adversarial noise injection – make streams resistant to scraping/AI analysis. Fine-grained segmentation masks – cleaner, region-specific redactions. AI Safety HUD – predictive alerts for likely privacy risks. <div