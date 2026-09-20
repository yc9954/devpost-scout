---
slug: "privify-wl1khb"
url: "https://devpost.com/software/privify-wl1khb"
title: "Privify"
hackathon: "TikTok TechJam 2025"
organization: "TikTok"
winner: true
words: 459
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
---

# Privify

> Your real-time privacy coach - flagging sensitive comments, encrypting every step, and building safer habits powered by fully homomorphic encryption and on-device AI.

[Devpost](https://devpost.com/software/privify-wl1khb) · hackathon [[TikTok TechJam 2025]]

## Facets

**mechanism** [[on_device_local]] [[privacy_tech]] [[realtime_stream]] [[structural_withholding]]
**domain** [[finance_payments]]

**stack** huggingface, lynx, python, react-lynx, scikit-learn

## How they structured the write-up

- 🌟 inspiration
- 🎯 our goal
- ⚡ what it does
- 🛠️ solution overview
- 💻 tech stack
- 📚 what we learned
- 🚀 what’s next

## Body

🌟 Inspiration Everyday comments expose far more than we think . Casual phrases can triangulate where you live, your daily routines, or who you are - even without geotags. Data brokers and AI systems can piece together small signals into a complete picture of identity . What’s missing: a default-on, usable layer of defense that teaches safer commenting habits in real time. Privify was inspired by the idea of a Grammarly-style privacy coach - a system that warns you before you post and helps you build healthier online behavior over time. 🎯 Our Goal We aim to protect users at two levels: Flag risky comments before they’re posted - especially those revealing location, routines, contact info, or identity clues. Keep evaluation secure - even TikTok’s servers (or any host platform) cannot read the original comment or the risk evaluation result. Teach for the future - provide concise, on-device reasoning and long-term insights so users naturally form safer patterns online. ⚡ What It Does 🔒 1. Privacy Guard (Inline Comment Analyzer) Runs before a comment is posted. Text is encrypted client-side . TikTok’s servers process the ciphertext via FHE-enabled classifiers. Returns encrypted results → decrypted locally . User sees real-time alerts : e.g. “This reveals your location” . Concise reasoning powered by TinyLlama (1.1B) - fast, on-device, Grammarly-style hints. 📊 2. Privacy Dashboard Aggregates encrypted results across a user’s comment history. Shows trends, distributions, and high-risk patterns without ever exposing raw text. Generates targeted recommendations via Phi-3 (3.8B) - a long-context on-device model. Helps users understand and improve their “privacy health” over time. 🛠️ Solution Overview 1. All-round encryption Comments are encrypted client-side. No raw data leaves the device. 2. FHE-enabled inference (Full Homomorphic Encryption) Server models (compiled with Concrete-ML) operate directly on ciphertext. Classifiers detect PII categories like geolocation, contacts, routines. Risk scores calculated directly on ciphertext. 3. On-device SLM reasoning TinyLlama: quick inline explanations highlighting 'reasoning' and 'suggestion' for flagged comment. Phi-3: deeper, long-form insights for privacy dashboard. 4. Privacy Health Dashboard Aggregates only encrypted or post-decryption labels. Users see trendlines, risk segments, and actionable suggestions - all computed client-side. 💻 Tech Stack Frontend: Lynx (Mobile), React (Web) Backend ML: scikit-learn + Python Encryption: Concrete-ML (FHE) On-device SLMs: HuggingFace (TinyLlama, Phi-3) 📚 What We Learned FHE in practice: Concrete-ML makes encrypted inference feasible, but demands thoughtful feature design for latency + accuracy. SLM trade-offs: Tiny models can deliver transparent, low-latency rationales ; larger edge models like Phi-3 shine for extended insights and coaching. Prompt tuning matters: Careful instruction design improves clarity and conciseness of feedback. 🚀 What’s Next Expanded PII taxonomy & multilingual support : detecting nuanced identity/location cues across languages. Deeper coaching : long-context Phi-3 sessions for habit formation, goal tracking, and private multi-device sync . <div