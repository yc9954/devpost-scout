---
slug: "aya-ai-em1aq5"
url: "https://devpost.com/software/aya-ai-em1aq5"
title: "Aya AI"
hackathon: "Prometheus July AI Challenge"
organization: "Prometheus"
winner: true
words: 574
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Aya AI

> A neuro-inclusive AI academic tutor with Generative UI to streamline Master's applications and reduce student burnout

[Devpost](https://devpost.com/software/aya-ai-em1aq5) · hackathon [[Prometheus July AI Challenge]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[accessibility]] [[education]] [[mental_health]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]]

**stack** accessibility, adhd, artificial-intelligence, education, framer-motion, generative-ui, llm, neurodiversity, next.js, react, tailwindcss, typescript, ui-ux

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for aya ai

## Body

Inspiration Applying to global Master's programs is an overwhelming and isolating process. I conducted a UX research survey with 87 students and found that the majority experienced severe anxiety due to information overload, complex grant requirements, and language barriers. Furthermore, feedback from 6 neurodivergent students like me (ADHD) highlighted that traditional productivity tools worsen executive dysfunction during high-stress periods. Aya AI was created to replace rigid checklists with an empathetic, proactive AI agent that adapts to a student's cognitive and emotional state What it does 1) Micro-Generative UI: Instead of wall-of-text answers, Aya generates interactive UI widgets directly inside the chat, such as live scholarship comparison matrices (MEXT, Fulbright, Chevening, GKS) and budget adjustment sliders 2) Academic Language Tutor: Evaluates writing drafts, estimates exam performance, and upgrades vocabulary to C1/C2 standards 3)Anti-Burnout Smart Roadmap: Breaks down complex admission steps into a manageable, RPG-style skill tree 4)Neuro-Inclusive Design: Features a Spoon Theory energy slider to adjust task intensity based on daily energy levels, Dyslexia-friendly fonts, Bionic reading, and RSD-Safe (Rejection Sensitive Dysphoria) gentle feedback modes 5) Dev X-Ray Console: Displays real-time system logs, intent parsing, and payload tracking under the hood for technical transparency How I built it 1) Frontend & UI: Built with Next.js (App Router), React, TypeScript, and Tailwind CSS 2)Generative UI Engine: Developed a custom state machine that detects intent triggers in user queries and dynamically renders custom React widgets inside the message stream 3) Accessibility & Motion: Utilized Framer Motion for smooth transitions, paired with modular CSS controls for sensory adjustment (bionic reading, font overrides, low-stimulation themes). 4) Designed directly around quantitative and qualitative feedback from 87 student survey participants Challenges I ran into 1) Ensuring dynamic widgets (tables, sliders) render reliably within a chat stream without causing layout shifts or re-render loops 2) Displaying complex academic data (stipends, tuition coverage, home-country return rules) while keeping the visual hierarchy simple and stress-free 3) Structuring system prompts to deliver objective academic critiques without triggering rejection sensitivity or anxiety in users Accomplishments that I am proud of 1) Grounded the entire product architecture in real user research from 87 respondents rather than assumptions 2)Successfully implemented a working Micro-Generative UI pattern that replaces generic text responses with interactive functional components 3)Created an accessibility-first platform that directly addresses executive dysfunction and student burnout What I learned Through building this project, I learned that interactive UI components within AI chats significantly improve information retention compared to standard text blocks. I also realized that designing specifically for neurodivergent edge cases , such as executive dysfunction and high anxiety, ultimately results in a much cleaner and more intuitive user experience for everyone. On a technical level, I gained valuable experience in implementing effective state management patterns to route LLM intent into structured UI updates within Next.js What's next for Aya AI Looking ahead, I plan to integrate direct LLM API streaming with native function calling to enable real-time dynamic widget generation. I also aim to expand the global scholarship database to cover additional regional grants and university programs. To make task management smoother, I will add two-way Google Calendar and ICS file export integrations for automated scheduling. Additionally, I intend to conduct broader focus group testing with neurodivergent student organizations. Finally, as I prepare for my Master's studies in Autumn 2027, I plan to use this academic journey to deepen my expertise in HCI and AI, using Aya AI as a long-term research and development project :) <div