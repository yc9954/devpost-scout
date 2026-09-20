---
slug: "lumina-ai-self-heal-runtime"
url: "https://devpost.com/software/lumina-ai-self-heal-runtime"
title: "PulsePay"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 542
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/general_public"
  - "user/patient_family"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# PulsePay

> Your body is your wallet. PulsePay uses Amazon Nova AI for face, fingerprint & voice-powered payments — enabling phone-less transactions for 400M+ unbanked Indians.

[Devpost](https://devpost.com/software/lumina-ai-self-heal-runtime) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[structural_withholding]]
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[retail_commerce]]
**user** [[general_public]] [[patient_family]] [[small_business]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** amazon-nova-2-lite, amazon-nova-2-sonic, amazon-nova-multimodal-embeddings, audio, aws-bedrock, express.js, fastapi, next.js-16, node.js, postgresql, python, tailwind-css, typescript, web

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pulsepay

## Body

Merchant POS with Nova risk scoring + voice output Amazon Nova 3-model architecture breakdown Landing page Distress Mode with SOS SMS + GPS alert Inspiration India has over 400 million unbanked citizens who can't access digital payments because they don't own a smartphone. Even for smartphone users, emergencies happen — your phone dies, gets stolen, or you simply forgot it. We asked: what if your body was your wallet? That question led to PulsePay. What it does PulsePay is a biometric micro-wallet that lets users pay using only their face, fingerprint, and voice — no phone required. Adaptive Authentication — Amazon Nova 2 Lite dynamically scores transaction risk and decides whether a face scan alone is enough, or if fingerprint verification is also needed Zero-Knowledge Biometrics — Face images are never stored. Amazon Nova Multimodal Embeddings converts facial features into mathematical vectors, which are then SHA3-256 hashed Voice-Confirmed Payments — Amazon Nova 2 Sonic provides real-time spoken confirmations so merchants know the payment went through Distress Mode — Scan your pinky finger instead of your index finger to silently trigger an SOS alert with GPS coordinates to your family 72-Hour Auto-Expiry — Wallets self-destruct after 72 hours with automatic refunds Family Wallet Delegation — Add family members with their own biometrics and spending caps UPI & Crypto Wallet Connect — Link existing UPI handles or crypto wallets for funding How we built it Frontend : Next.js 16 + TypeScript + Tailwind CSS as a PWA with glassmorphism UI Backend : Node.js + Express integrating three Amazon Nova models via AWS Bedrock SDK CV Service : Python FastAPI handling biometric processing with Nova Multimodal Embeddings Database : PostgreSQL for wallet state, transactions, and family delegation Amazon Nova Integration: Nova Multimodal Embeddings — Generates high-dimensional face vectors for zero-knowledge biometric matching Nova 2 Lite — Agentic security layer analyzing transaction context to dynamically set authentication requirements Nova 2 Sonic — Bidirectional streaming voice AI generating natural merchant confirmations in real-time Challenges we ran into Bidirectional streaming with Nova 2 Sonic required deep research into the AWS SDK's InvokeModelWithBidirectionalStreamCommand and NodeHttp2Handler — the event protocol was complex to implement correctly Balancing security with usability — the AI risk engine needed to be smart enough to not annoy users on small purchases while catching suspicious transactions Camera-based fingerprint scanning in a browser was unreliable, so we engineered a touch-based fingerprint solution with visual progress feedback Accomplishments that we're proud of Built a complete biometric payment system that works without a phone Integrated three different Amazon Nova models across three hackathon categories (Multimodal, Agentic, Voice) The Distress Mode feature could genuinely save lives in real-world emergencies Achieved zero-knowledge biometric storage — no raw biometric data is ever persisted What we learned Amazon Nova's multimodal capabilities can replace traditional specialized ML models for biometric embedding Nova 2 Lite effectively acts as an autonomous security agent when given the right context Building accessibility-first (no phone, no literacy required) forces better design decisions for everyone What's next for PulsePay Integration with India's UIDAI Aadhaar system for real identity verification Hardware biometric sensor support for enterprise merchant terminals Expanding Nova 2 Sonic to support Hindi, Tamil, and other regional languages Pilot program with rural merchants in partnership with local banks <div