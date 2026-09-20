---
slug: "tutorai-8moeq6"
url: "https://devpost.com/software/tutorai-8moeq6"
title: "tutorAI"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 599
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# tutorAI

> Personalized AI tutor that generates animation and real time chat to help you learn

[Devpost](https://devpost.com/software/tutorai-8moeq6) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[education]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** express.js, javascript, python

## How they structured the write-up

- problem statement
- solution -> tutorai
- market & target demographic research
- business model
- traction
- risk mitigation & mvp
- one-pager summary

## Body

TutorAI Github: https://github.com/dan-the-man639/tutorAI Linkedin: https://www.linkedin.com/in/danny-yang639/ Video Demo: https://youtu.be/NehwRFE2Res?si=GcNgIAa7dGwLDg2R Problem Statement Core issue : Online learning platforms still push identical videos to every learner, while private tutoring is costly and scarce. What’s broken / not working Static videos cannot adapt to a learner’s pace or address individual gaps. Massive-open courses average completion rates below 10 %. Private STEM tutors cost US $60–150 per hour, pricing many families out. Why this persists Existing platforms were built for broadcast rather than conversation. Real-time visual explanations once required skilled humans; only recent AI + GPU advances make automation viable. Solution -> TutorAI What it is : A voice-first AI tutor that listens, explains with live animations, and obeys playback commands spoken by the learner. How we solve the problem GPT-4o reasons through any math or STEM prompt. A cloud engine renders bespoke 10-second animations (e.g., Riemann sums collapsing into an integral). ElevenLabs voices the explanation; a lip-synced avatar boosts engagement. A JSON command layer obeys natural speech like “rewind,” “slow to half-speed,” or “highlight step three.” Use-case snapshots AP-Calculus student: “Show how Riemann sums become an integral.” Linear-algebra freshman: “Visualise eigenvectors of this 2×2 matrix.” Data-analyst up-skiller uploads a PDF and receives a spoken walkthrough of each formula. Market & Target Demographic Research Total Addressable Market (TAM) : Global e-learning plus private tutoring ≈ US $485 B (2025). Serviceable Available Market (SAM) : English-language, online STEM learners ≈ US $95 B. Serviceable Obtainable Market (SOM) : Capturing 0.12 % over three years ≈ US $115 M in annual recurring revenue. Ideal early customers : North-American high-school and college STEM learners, self-taught programmers, and tutoring centers seeking scalable help. Business Model How we make money Freemium with a US $15 / month TutorAI Pro tier. B2B SaaS: US $5 per seat per month for schools and tutoring centers. API licensing for publishers embedding TutorAI explanations. Revenue mechanics Subscriptions create predictable ARR. Volume licenses yield low-churn institutional revenue. White-label API earns per-lesson transaction fees. Extra details Gross margin exceeds 80 % after GPU and token costs (~ US $0.06 per full lesson). Planned partnerships with cloud-GPU vendors and curriculum publishers. Traction Alpha prototype live: typed prompt → custom animation; voice layer specification complete. Fifty closed-beta learners averaging 12 minutes daily use. Two tutoring-center chains have signed letters of intent for pilot seats. Roadmap Q3 2025: launch web MVP with full voice and video-control commands. Q4 2025: reach 1 000 paying users and five pilot schools; raise US $1.5 M seed round. 2026: release AR-glasses demo and add multilingual support. Risk Mitigation & MVP Technical cost risk – mitigated with caching and shorter default animations. Pedagogical accuracy – human educator review loop plus user feedback buttons. LLM hallucinations – guard-rail prompts and post-processing validators. Adoption friction – demo requires no login; voice UI lowers the barrier. MVP definition – web app featuring mic input, GPT-generated text, live animations, ElevenLabs voice, and six voice commands (play, pause, rewind, slow_down, speed_up, highlight_step) delivered in under 25 seconds end-to-end. One-Pager Summary TutorAI is the affordable AI-powered STEM tutor that fuses GPT-4o reasoning, real-time animations, and natural voice interaction. Learners simply speak; TutorAI explains, visualises, and obeys commands like “rewind to step three.” Targeting a slice of the US $485 B e-learning and tutoring market, TutorAI starts with a freemium model, institutional licenses, and API sales, aiming for US $115 M ARR within three years. Alpha prototype is live with 50 active testers and tutoring-center LOIs. Next milestone: Q3 2025 MVP with complete voice control. TutorAI delivers 3Blue1Brown-level clarity with Jarvis-style interactivity—at less than 10 % of human-tutor cost. <div