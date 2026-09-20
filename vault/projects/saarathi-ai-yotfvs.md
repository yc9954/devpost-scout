---
slug: "saarathi-ai-yotfvs"
url: "https://devpost.com/software/saarathi-ai-yotfvs"
title: "SAARATHI AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 759
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/education"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# SAARATHI AI

> India has hundreds of welfare schemes, yet millions miss out — SAARTHI bridges this gap by turning awareness into real access, guiding citizens from discovery to application with AI and CSC support.

[Devpost](https://devpost.com/software/saarathi-ai-yotfvs) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[agriculture_food]] [[civic_government]] [[education]]
**user** [[educator_student]] [[frontline_worker]] [[general_public]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** ai, fastapi, ivr, natural-language-processing, next.js, python, rest, tailwind-css, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we’re proud of
- what we learned
- what’s next
- vision

## Body

Citizen chat — natural language input with AI profile extraction SAARTHI landing page — quick entry to citizen discovery and CSC operator portal Document readiness — detected documents and missing document guidance Scheme recommendations — ranked eligible schemes with match scores,scheme details — eligibility rationale, required documents each scheme card's options available for user to choose CSC operator login — secure access for operators CSC operator dashboard — manage assistance requests and follow-ups Inspiration We noticed something simple but serious — India has hundreds of government welfare schemes, but many people around us had no idea which ones they could actually use. Even when they knew about a scheme, they were confused about eligibility, documents, or where to even start. In rural areas, this problem is even bigger because of language barriers and limited digital access. We realized the issue isn’t the lack of schemes — it’s the gap between information and actual access. That’s what pushed us to build SAARTHI. What it does SAARTHI is an AI-based system that helps people figure out which government schemes they can apply for, just by describing their situation in simple language. For example: “I am a farmer from Karnataka with low income” Based on this, SAARTHI: Understands the user’s background Finds relevant schemes Explains why they are eligible Shows required documents Guides them on how to apply If the user is not fully eligible, it also suggests what’s missing. The goal is not just to show schemes, but to actually help people move forward. Accessibility focus We tried to design SAARTHI keeping real users in mind: Web interface (simple and clean) Voice support (planned) IVR system so people can use it without internet Option to connect with a CSC operator for help So instead of just information, the user gets a full path: from understanding → to action How we built it How we built it SAARTHI is built around a simple idea — let users describe their situation naturally, and let the system handle the complexity behind the scenes. AI understanding layer At the core, we use AI/NLP to convert free-text input into structured data. When a user says something like: “I am a farmer from Karnataka with low income” The system extracts key details such as: Location Occupation Income level Category (farmer, student, etc.) This is then converted into a structured user profile. Scheme matching & eligibility Once the profile is created: It is matched against schemes stored in our dataset ( schemes.json ) Rule-based logic is applied to check eligibility The system determines: Which schemes the user qualifies for Which conditions are satisfied What is missing (if not eligible) Explanation engine Instead of just listing schemes, SAARTHI explains: Why the user is eligible What documents are required What steps they should take next This makes the output clear and actionable. System flow The overall flow of the system works like this: User Input → AI Understanding → Structured Profile Profile → Scheme Matching → Eligibility Check Results → Explanation → Next Steps Scalability The system is dataset-driven, which means: New schemes can be added easily The platform can scale without changing core logic We also integrated APIs to support: Assistance requests CSC operator workflows Challenges we ran into One of the biggest challenges was handling user input. People don’t speak in structured formats, so converting free text into usable data took effort. Another challenge was explaining eligibility clearly. It’s easy to match schemes, but harder to explain why someone qualifies. We also had to think beyond just the app — how this would work for someone without internet, which led us to the IVR idea. What we’re proud of We built a working prototype that actually completes the full flow The system doesn’t just recommend — it explains We included a path for real-world help (CSC operators) The design is simple enough for non-technical users The system can grow easily by expanding the dataset What we learned We learned that solving real problems is very different from building demo features. Clarity matters more than complexity. Also, technology alone isn’t enough — combining it with human support makes the solution more practical. What’s next We want to make SAARTHI more usable in real conditions: Add support for multiple languages Improve voice interaction Expand the scheme database Make eligibility explanations clearer Add better tools for operators Vision We want SAARTHI to become something simple but powerful: A tool where any person can understand and access the benefits they deserve without confusion or dependency. Even if they don’t have internet. <div