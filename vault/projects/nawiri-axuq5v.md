---
slug: "nawiri-axuq5v"
url: "https://devpost.com/software/nawiri-axuq5v"
title: "NAWIRI"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 556
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# NAWIRI

> In West Africa, families miss aid they're legally entitled to , not because it doesn't exist, but because the system is too hard to navigate. NAWIRI fixes that.

[Devpost](https://devpost.com/software/nawiri-axuq5v) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[accessibility]] [[agriculture_food]] [[civic_government]] [[finance_payments]]
  <sub>weak: labor_employment</sub>
**user** [[frontline_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** google-gemini-api-(gemini-flash-lite-latest), google-translate-(via-cloudflare-worker), leaflet.js, next.js, node.js, openstreetmap, vercel

## How they structured the write-up

- inspiration
- what it does
- why ai and not a search engine or form
- how we built it
- challenges
- what we learned

## Body

Inspiration "People often miss help not because it does not exist, but because the system is too hard to navigate." — USAII Brief 4. In Benin, our home country, we have seen families give up on healthcare, cash transfers, or microcredit they were legally entitled to , not from lack of need, but from lack of guidance. A mother does not know that her cesarean is free. A farmer does not know that ARCH covers him. A grandmother does not know Plan Sésame exists. The information is public. The gap is interpretation. What it does NAWIRI is a conversational AI assistant for West Africa. You describe your situation in plain words — in English, French, Fɔngbe, Wolof, or Twi — and NAWIRI asks one question at a time to identify which of the 25 documented social protection programs you may qualify for. It then returns: the program name, the exact documents to bring, the steps to take, and the official contact to call. Why AI and not a search engine or form A static form cannot interpret a free-text message that mixes health signals, financial signals, and family signals at once. A search engine returns documents , not a personalized action plan. Eligibility for these programs depends on dozens of intersecting variables: age, enrollment in a national registry, household size, income, disability status. Only a language model can hold the full combinatorics and ask the right next question. Critically, NAWIRI does not automate a decision , it interprets and orients. The final eligibility validation always stays with a human agent. This distinction matters for trust and for accuracy. How we built it Four components: Program database — 25 programs across Benin, Senegal, Ghana. Each entry contains eligibility criteria in plain language, required documents (including how to obtain foundational ID documents), step-by-step procedure, and official contact. All data is verified from primary government sources, dated to 2026. Conversational engine — Google Gemini gemini-flash-lite-latest via streaming SSE. A structured system prompt injects only the relevant country's data (auto-detected from conversation context, saving ~49% of prompt size). The model is instructed to ask exactly one follow-up question per turn. Language pipeline — Input in Fɔngbe, Wolof, or Twi is translated to English via a (Google Translate , processed by Gemini in English, then translated back. The AI history is always stored in English, keeping the model's reasoning clean. Institutions map — Leaflet + OpenStreetMap with 10 key institutions across 3 countries. The AI can emit a [[MAP:id|label]] token that renders as a button in the UI and flies the map to the institution. Challenges The hardest challenge was data accuracy. Programs in West Africa are frequently renamed, reorganized, or have corrections that are not reflected online. Key corrections we found and applied: ANACMU became SEN-CSU in Senegal (Decree 2024-832, March 2024); RAMU was operationally replaced by ARCH/ANPS in Benin; dialysis is free in Senegal but NOT in Benin — a critical distinction we tested explicitly in our 25-scenario test suite. Balancing depth (accurate, nuanced) versus accessibility (one question at a time, no jargon) was the other core tension we resolved through prompt engineering. What we learned That the most important work is not building the AI ; it is building the data. The AI is only as useful as the accuracy of the program information it draws from. <div