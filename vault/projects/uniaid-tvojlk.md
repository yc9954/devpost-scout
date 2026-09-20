---
slug: "uniaid-tvojlk"
url: "https://devpost.com/software/uniaid-tvojlk"
title: "UniAid"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 522
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/housing_homeless"
  - "domain/immigration_refugee"
  - "user/educator_student"
  - "substrate/structured_db"
---

# UniAid

> Real student insights for better University choices

[Devpost](https://devpost.com/software/uniaid-tvojlk) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[measured_ablation]] [[retrieval_grounding]]
**domain** [[education]] [[housing_homeless]] [[immigration_refugee]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** elasticsearch, figma, llm, ml, python, react, vm

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for uniaid

## Body

Inspiration Every member of our team has faced countless issues while starting their journey at a new University. Our parents have spent many sleepless nights worrying about their child's welfare; it's hard to find all the resources you need in one place. This inspired us to create UniAid, with the aim of helping students and parents across the globe. What it does Ever felt anxious while choosing a new university? Do your parents have thousands of questions that you don’t know how to answer? Have you ever wished for a reliable and streamlined source of information and guidance? UniAid is a one-stop solution for all these questions. How we built it Frontend: React (Vite), deployed on Netlify, with a simple UI for search, profiles, and auth. Backend: FastAPI (Python) for auth, user/mentor data, and the recommendation API, hosted on a cloud VM (EC2/GCP). Database: PostgreSQL for users, mentors, mentees, and sessions. ML recommendations: We use sentence embeddings (e.g. sentence-transformers) and learning-to-rank (LTR), so recommendations match free-text requests (university, field, visa, housing, languages). The model is trained on mentor profiles and optional interaction data. Deployment: Frontend on Netlify, Backend + ML on a single VM, with clear separation so we can scale or move services later. Challenges we ran into ML in production: Fitting the ML stack (e.g. PyTorch/sentence-transformers) into limited memory and disk; we switched to CPU-only builds and tuned dependencies so it runs on a small VM. Deployment: Deciding between one server (Backend + ML together) vs separate services; we went with one VM for the hackathon and documented how to split later. Recommendation quality: Making the model respect multiple constraints (university, field, visa, languages); we combined semantic search with requirement matching and LTR so results stay relevant and interpretable. Accomplishments that we're proud of End-to-end product: From sign-up and mentor search to ML-powered recommendations and profile browsing, all working in production. Smart matching: Recommendations that understand natural language (“I need visa and housing help, CS, Mandarin”) instead of rigid filters. Real deployment: Frontend on Netlify, Backend + ML on a cloud VM, with auth, DB, and API wired together and callable from the app. Inclusive design: Built for both students and parents, with support for multiple languages and types of help (visa, housing, culture, career). What we learned How to design and deploy an ML-backed API (embeddings + LTR) in a resource-constrained environment. Trade-offs between monolithic vs microservice deployment for a hackathon (speed vs scalability). Importance of CPU-only and smaller dependencies when running ML on free or low-cost cloud VMs. How to keep recommendations explainable by combining semantic similarity with explicit requirement checks (e.g. visa, language). What's next for UniAid Booking and sessions: Let users book 1:1 sessions with mentors and track them in the app. More universities and regions: Expand mentor and university coverage so more students and parents can find local support. Parent-specific flows: Dashboards and content tailored to parents (e.g. safety, costs, keeping in touch). Stronger ML: Richer training data, A/B tests on recommendation quality, and optional personalization based on past interactions. Mobile and accessibility: Responsive/mobile-first UI and better accessibility so the platform works for everyone. <div