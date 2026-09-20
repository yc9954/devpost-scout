---
slug: "ghostmanager"
url: "https://devpost.com/software/ghostmanager"
title: "GhostManager"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 309
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "user/government_staff"
  - "user/patient_family"
  - "user/researcher"
---

# GhostManager

> Using agentic AI to reinvent compliance.

[Devpost](https://devpost.com/software/ghostmanager) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[structural_withholding]]
**domain** [[health_clinical]] [[mental_health]] [[security_privacy]]
**user** [[government_staff]] [[patient_family]] [[researcher]]
  <sub>weak: web_dom</sub>

**stack** fastapi, gemini, html, javascript, python, typescript

## How they structured the write-up

- inspiration
- the what
- challenges

## Body

Inspiration Every year, healthcare organizations lose billions to compliance mistakes, not from breaches, but from small human errors. A new hire sends an email with patient data. A researcher shares a file in Slack. Having worked in healthcare startups, clinical research, and AI labs, we’ve felt that fear firsthand: the anxiety of “what if I mess up?” That fear inspired us to build GhostManager, an AI-native compliance officer that proactively prevents mistakes before they happen. The what GhostManager is the “Grammarly for compliance.” It runs a live compliance layer across company communication (i.e. Gmail, Slack, Notion), detecting and correcting potential HIPAA, FDA, and governance violations in real time. It flags risky messages, explains why they’re noncompliant, and even rewrites them to be compliant, all before they’re sent. It also builds a living, searchable knowledge base that captures each organization’s evolving compliance decisions. This dual pronged workflow allows for both security and education for new employees in a way not seen before. We built GhostManager around an agentic hierarchy of specialized AI models, each trained for a specific compliance domain. These agents collaborate to assess risks and suggest fixes. To ensure privacy, we integrated a spaCy-powered data sanitization pipeline that strips all personal or health identifiers before any data touches an AI model. The backend is built in FastAPI, with a responsive JavaScript frontend for real-time feedback and visualization. Challenges The primary challenges included properly synthesizing a backend consisting of an triple-tiered (eight total agents) hierarchy of compliance/knowledge agents with a efficient and streamlined frontend that would first undergo data sterilization. Oftentimes, there were issues with over-sterilization, time sinkage, or confusion between agents before a more explicit hierarchy was coded. In terms of the sterilization, a combination of NLP and spacy allowed for PHI (patient health information) to be protected without a significant amount of compliant information being [REDACTED]. <div