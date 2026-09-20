---
slug: "sympsense-observability-first-health-ai"
url: "https://devpost.com/software/sympsense-observability-first-health-ai"
title: "SympSense: Safe & Observable Health AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 729
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/media_journalism"
  - "domain/mental_health"
  - "user/clinician"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/web_dom"
---

# SympSense: Safe & Observable Health AI

> A transparency-first AI health assistant that transforms symptom checking into structured, explainable, and calm decision support.

[Devpost](https://devpost.com/software/sympsense-observability-first-health-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[developer_tools]] [[education]] [[health_clinical]] [[media_journalism]] [[mental_health]]
**user** [[clinician]] [[educator_student]] [[researcher]]
**substrate** [[web_dom]]

**stack** datadog, datalog, google-cloud-run, google-gemini-api, html, html5, tailwind-css, typescript, vercel, vite, web-speech-api

## How they structured the write-up

- 🌌 inspiration
- 🚀 what it does
- 🔥 what makes sympsense different
- 🏗️ how we built it
- 🔄 finale round improvements
- ⚙️ challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what’s next for sympsense
- real world impact

## Body

🌌 Inspiration During exam seasons and high-stress academic periods, students often experience physical discomfort but struggle to understand whether their symptoms are temporary, stress-related, or require medical attention. Existing health tools typically fall into two extremes: Overly complex platforms filled with medical jargon Generic AI chatbots that provide answers without clarity or accountability We initially set out to build a calm, student-first symptom awareness tool . However, during development, we identified a deeper issue: Most AI systems in healthcare operate as black boxes — users receive outputs, but have no visibility into how or why those outputs are generated. This led us to rethink the system itself. 👉 SympSense evolved into a transparency-first health AI assistant focused on clarity, safety, and trust. 🚀 What it does SympSense is a non-diagnostic AI health assistant that helps users: 🧠 Describe symptoms naturally using text or voice 💬 Receive clear, structured, easy-to-understand explanations ⚠️ Understand whether symptoms can be monitored or require attention 🚨 Get guidance for potentially serious conditions 🌍 Access multilingual support for improved accessibility 🔥 What makes SympSense different Most AI health tools optimize for generating answers. SympSense is designed to optimize for understanding, safety, and user trust . 🧠 Structured AI Understanding Instead of long, unstructured responses, outputs are organized into: Clear explanation Severity level (Low / Moderate / High) Confidence indicator Recommended next steps 👉 This reduces cognitive overload and helps users make clearer decisions. 🕒 Symptom Timeline & Pattern Awareness Tracks symptoms over time Identifies recurring patterns Enables continuous health awareness 👉 Moves beyond one-time queries to longitudinal understanding 📊 Observability Layer (Core System Thinking) SympSense introduces an observability layer that monitors: Response latency System behavior Safety-related signals 👉 This shifts the AI from a black-box responder → a monitored system This serves as a foundation for deeper reliability and safety evaluation. 🛡️ Safety & Transparency Layer Detection of potentially high-risk symptoms Escalation guidance for critical scenarios “Why this response?” explanation panel Clear non-diagnostic boundaries 👉 Designed to inform responsibly without creating panic or misinformation 🧘 Calm, Human-Centered UX Minimal, soft interface designed to reduce anxiety Emotion-aware tone and microcopy Accessible and inclusive interaction design 👉 Focused on supporting users during uncertainty ⚠️ Important: SympSense does not provide medical diagnoses. It supports awareness and encourages consultation with healthcare professionals. 🏗️ How we built it Frontend TypeScript, HTML, Tailwind CSS Component-based architecture Mobile-first, responsive design AI & Backend Google Gemini API for natural language understanding Lightweight backend for secure AI interaction Structured response formatting layer Observability System Datadog integration for: Request/response logging Latency tracking System behavior monitoring 🔄 Finale Round Improvements To align with the refinement-focused finale round, we prioritized depth and system design : 🔄 Refactored into a more scalable architecture 🧠 Introduced structured AI outputs (severity, confidence, actions) 🕒 Added symptom timeline and pattern tracking 📊 Integrated observability monitoring 🚨 Strengthened safety and escalation handling 🎨 Improved UI/UX for clarity and calm interaction 🌍 Enhanced multilingual accessibility 👉 The system evolved from a basic chatbot into a more structured and responsible AI experience ⚙️ Challenges we ran into Designing AI responses that inform without increasing anxiety Maintaining non-diagnostic boundaries while remaining useful Defining meaningful observability beyond simple logging Balancing system monitoring with user privacy Avoiding over-engineering while preserving usability 🏆 Accomplishments that we're proud of Built a production-style AI system , not just a prototype Introduced structured outputs for better user understanding Integrated observability into an LLM workflow Designed a calm and accessible experience for sensitive use cases Balanced intelligence, safety, and usability effectively 📚 What we learned AI systems in healthcare must be understandable, not just accurate User trust depends on both UX design and system transparency Responsible AI requires system-level thinking, not just model integration Observability enables proactive trust, not just debugging 🔮 What’s next for SympSense Advanced confidence calibration and reliability scoring Hallucination awareness and response validation Long-term personalized health insights Clinician-facing dashboards for oversight Real World Impact SympSense addresses a global challenge in digital healthcare: • Lack of trust in AI-driven medical tools • Over-reliance on black-box systems • Anxiety caused by unclear or overwhelming outputs By introducing explainability, structured outputs, and observability, SympSense improves: • User understanding and confidence • Responsible AI adoption in healthcare • Early awareness and better decision-making This makes it not just a tool, but a foundation for safer AI systems in real-world healthcare environments. <div