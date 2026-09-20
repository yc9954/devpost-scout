---
slug: "sentinelai-lk2w1c"
url: "https://devpost.com/software/sentinelai-lk2w1c"
title: "SentinelAI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 285
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/security_privacy"
---

# SentinelAI

> AI-Powered Threat Detection at Machine Speed

[Devpost](https://devpost.com/software/sentinelai-lk2w1c) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[security_privacy]]
  <sub>weak: finance_payments, transportation</sub>
  <sub>weak: researcher</sub>
  <sub>weak: geospatial</sub>

**stack** css, cybersecurity, fastapi, groq, mitre, next.js, python, recharts, scikit-learn, tailwind, typescript

## Body

## Inspiration Security analysts can't keep up with thousands of network events per second. We built an AI co-pilot that detects threats, classifies them, and tells you what to do about it. ## What it does SentinelAI analyzes network traffic and catches the bad stuff: Detects anomalies using machine learning Classifies threats (DDoS, brute force, malware, data exfiltration, port scans) Scores risk so you know what to fix first Maps attacks to MITRE ATT&CK framework Suggests specific remediation steps Visualizes attacker → target connections in real-time ## How we built it Frontend : Next.js + TypeScript + Tailwind + Recharts Backend : Python FastAPI + scikit-learn ML : Isolation Forest (anomaly detection) + Random Forest (threat classification) Data : 1,000+ synthetic network logs with realistic attack patterns We trained two models, built an enrichment pipeline that adds risk scores and MITRE techniques, then wrapped it in a dashboard that doesn't suck. ## Challenges scikit-learn version conflicts between training and deployment Making ML inference fast enough for 100+ events per page load Balancing risk score formulas to be actually useful Building a professional UI on a hackathon deadline ## Accomplishments ✅ Real trained ML models (not fake demos) ✅ MITRE ATT&CK integration like production security tools ✅ Network topology visualization that's actually cool ✅ Production-quality dashboard with glassmorphism and smooth animations ## What we learned ML deployment ≠ ML training. Versioning, caching, and performance matter. Cybersecurity domain knowledge runs deep (MITRE, threat taxonomies, kill chains). Real-time visualization is way harder than it looks. ## What's next Connect to real network logs (Zeek, Suricata) instead of synthetic data Automated response via firewall/SIEM APIs Deep learning models for sequential attack patterns SaaS platform for actual SOC teams <div