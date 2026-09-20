---
slug: "ai-cybershield-real-time-scam-fraud-detection-system"
url: "https://devpost.com/software/ai-cybershield-real-time-scam-fraud-detection-system"
title: "AI CyberShield – Real‑Time Scam & Fraud Detection System"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 361
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "substrate/web_dom"
---

# AI CyberShield – Real‑Time Scam & Fraud Detection System

> AI CyberShield protects users in real time by detecting scams, phishing, and malicious links with explainable AI.

[Devpost](https://devpost.com/software/ai-cybershield-real-time-scam-fraud-detection-system) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[realtime_stream]]
**domain** [[finance_payments]] [[security_privacy]] [[supply_logistics]]
**substrate** [[web_dom]]

**stack** chrome-extension-manifest-v3, fastapi, hugging-face-inference-api, javascript, next.js, node.js, npm, python, sqlite, tailwindcss, typescript, urlhaus, uvicorn, virustotal

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what’s next for ai cybershield – real‑time scam & fraud detection system

## Body

AI CyberShield landing page with live demo preview and feature overview. Analyzer dashboard for pasting suspicious messages and running instant scans Scan results dashboard showing scam probability, risk score, and live threat feed status. Explainable AI highlights with confidence band and pattern matches for transparency Detailed URL reputation analysis and model category scores Threat history dashboard with weekly blocked scams, cumulative risk saved, and reports. Inspiration Scams and phishing are no longer limited to emails — they hit users through SMS, social media, crypto wallets, and everyday browsing. We wanted to build something that protects people in real time, not just after they paste a message. That vision led to AI CyberShield: a proactive security system rather than a reactive tool. What it does AI CyberShield analyzes suspicious messages, URLs, and browsing activity to detect scams. It outputs a scam probability, risk score, and explainable reasons, and the browser extension provides real‑time alerts, link highlighting, and optional auto‑block protection. How we built it Frontend: Next.js + Tailwind dashboard Backend: FastAPI with AI scoring + rule detection + threat intel Extension: Chrome Manifest V3 for live scanning AI: Hosted NLP model (Hugging Face) + rules engine Threat feeds: URLhaus + VirusTotal Risk is computed by combining multiple signals: $$ \text{Risk} = 0.4 \cdot \text{AI} + 0.2 \cdot \text{Patterns} + 0.4 \cdot \text{URL/Feeds} $$ Challenges we ran into Free threat feeds often rate‑limit or block requests Making the extension fast without spamming the API Balancing strong detection with privacy‑first storage Turning model signals into clear, user‑friendly explanations Accomplishments that we're proud of Real‑time browser protection with offline fallback Explainable AI highlights and confidence bands Automated threat scoring that feels like a real product Privacy‑first storage and consent flow What we learned Security isn’t just about detection accuracy — it’s about trust, explainability, and UX. We learned how to combine AI, threat intelligence, and browser‑level protection into one cohesive experience. What’s next for AI CyberShield – Real‑Time Scam & Fraud Detection System Add more threat feeds with reliable caching Train a custom model focused on crypto & financial scams Expand to mobile/PWA scanning Build a community reporting network that strengthens detection over time <div