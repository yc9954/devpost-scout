---
slug: "shadowguard-l6yv7p"
url: "https://devpost.com/software/shadowguard-l6yv7p"
title: "ShadowGuard"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 555
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "domain/transportation"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
---

# ShadowGuard

> ShadowGuard is a network-layer AI firewall that detects and redacts sensitive patient data in real time, before it ever leaves a hospital network.

[Devpost](https://devpost.com/software/shadowguard-l6yv7p) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[structural_withholding]]
**domain** [[health_clinical]] [[legal_justice]] [[transportation]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[regulation_legal_text]]
  <sub>weak: web_dom</sub>

**stack** css, d3.js, html, javascript, mitmproxy, node.js, openai, python, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shadowguard

## Body

Inspiration Healthcare is rapidly adopting AI tools, cloud platforms, and smart medical devices. While this improves efficiency and patient outcomes, it also introduces a serious compliance risk: sensitive patient data can leave the hospital network in seconds. A simple AI prompt containing a name, diagnosis, or SSN can unintentionally create a HIPAA violation. We were inspired by a core question: What if hospital networks could defend themselves automatically? Instead of relying on post-incident audits and manual reviews, we wanted to build a system that enforces privacy in real time, at the network layer , before sensitive data ever leaves the building. That vision became ShadowGuard . What it does ShadowGuard is a real-time AI-powered PII firewall for hospitals. It sits inline as a Layer 7 proxy between internal devices and the internet. ShadowGuard: Intercepts outgoing HTTP/HTTPS traffic Reconstructs payloads (JSON, form data, AI prompts) Detects Protected Health Information (PHI/PII) Redacts or tokenizes sensitive data in transit Alerts administrators for high-risk incidents Instead of blocking workflows, ShadowGuard intelligently modifies packets before forwarding them, ensuring compliance without disrupting clinical operations. How we built it We designed ShadowGuard as a modular network-layer system. 1️⃣ Packet Interception We implemented a proxy-based Man-in-the-Middle architecture to route outbound traffic through ShadowGuard for inspection. 2️⃣ Payload Reconstruction We parse and reconstruct application-layer content from packets to analyze real data rather than raw bytes. 3️⃣ Hybrid PII Detection We combined: Regex-based pattern detection (SSNs, phone numbers, MRNs) Named Entity Recognition (NER) LLM-based contextual classification 4️⃣ Inline Redaction Engine Instead of blocking traffic, we dynamically rewrite payloads: Before John Doe | SSN: 123-45-6789 | Diagnosis: Cardiac Arrest After [REDACTED] | SSN: XXX-XX-XXXX | Diagnosis: [REDACTED] 5️⃣ Real-Time Alerting High-severity events trigger logging, alerts, and escalation workflows. Challenges we ran into 🔐 HTTPS Decryption Intercepting HTTPS traffic requires certificate injection and careful trust-chain handling, especially sensitive in medical environments. We used the MITMProxy to handle this. ⚡ Latency vs Accuracy LLMs provide contextual detection but introduce delay. We engineered a layered system where fast deterministic checks run first, and AI scoring is applied selectively. 🎯 False Positives Over-redaction can break workflows. We prioritized precision and designed conservative thresholds to maintain usability. ⚖️ Compliance Considerations Modifying packets inline raises auditing and legal questions. We ensured every action is logged and traceable for compliance review. Accomplishments that we're proud of Successfully implemented real-time packet interception and rewriting Built a hybrid AI + deterministic PII detection engine Reduced latency through layered scoring Designed a system that preserves workflow instead of blocking traffic Created a proactive privacy enforcement model rather than reactive logging Most importantly, we demonstrated that network-layer AI governance is possible in real time. What we learned Security is most powerful when implemented at the network layer. AI systems must include deterministic fallbacks for reliability. Compliance solutions must balance protection with usability. Real-world healthcare systems require transparency and auditability. We also learned that privacy enforcement should not rely solely on user behavior, it should be architected into the system itself. What's next for ShadowGuard Optimizing detection models for lower latency Training lightweight on-device classifiers for IoT medical devices Integrating automated voice-based incident response Building adaptive policy learning for hospital-specific compliance rules Exploring zero-trust deployment architectures Our long-term vision is to make ShadowGuard the foundation for AI-native compliance infrastructure in healthcare. 🛡️ ShadowGuard Privacy. Enforced in Transit. <div