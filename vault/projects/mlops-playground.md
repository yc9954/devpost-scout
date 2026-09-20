---
slug: "mlops-playground"
url: "https://devpost.com/software/mlops-playground"
title: "MLOps Playground"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 701
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/document_pdf"
---

# MLOps Playground

> Learn production ML by operating it, not reading about it.

[Devpost](https://devpost.com/software/mlops-playground) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[document_pdf]]

**stack** 14, css, docker, fastapi, framer, groq, next.js, node.js, python, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mlops playground

## Body

DemoImage9 DemoImage10 DemoImage8 DemoImage2 DemoImage4 DemoImage11 DemoImage7 DemoImage3 DemoImage1 DemoImage5 DemoImage6 Inspiration I was preparing for ML engineering interviews and kept bouncing between tabs. One blog post for canary deployments, another for drift detection, a GitHub repo for interview questions, a YouTube video for system design. Nothing tied it together and nothing let me actually practice. I wanted a single place where I could run a simulator, understand the concept behind it, and then answer interview questions on it without leaving the page. That frustration is what started this. What it does MLOps Playground is a learning platform for production machine learning engineering built around three modes. Labs gives you 16 interactive simulators where you inject faults, configure thresholds, and watch automated gates respond in real time. Study Guide covers the concepts behind each simulator at engineering depth, with AI-generated quizzes after every section. Mock Interview has 360 plus questions drawn from real ML system design rounds, and the AI evaluates each answer telling you specifically what you got right, what you missed, and what a follow-up would look like. At the end of any interview session you can export a full preparation guide as a PDF with technical answers, behavioral variants, and STAR-method responses for every question in the module. How we built it The frontend is built with Next.js 14 and TypeScript. Every module follows the same structure: a simulator component, a content file that holds the study guide sections and interview questions, and a simulation hook that manages fault injection and state. That structure made it possible to build 16 modules without things becoming inconsistent. The backend is a FastAPI service that handles real-time simulator state and proxies the Groq API. All AI calls go through a single abstraction layer that tries the user's own key first, falls back to the server key, and then falls back to static content if neither is available. Challenges we ran into The hardest part was the content. Writing study guide sections that were actually useful at senior engineering level, not just technically correct, took much longer than the code. Vague explanations are easy to write. Specific ones with real numbers, real tool names, and production failure modes are not. The second challenge was making AI features fail gracefully. Every feature needed a static fallback that was genuinely useful, not just an error message, because the platform has to work even without an API key configured. Staying disciplined about scope was also harder than expected. There were always more features to add and more modules to build. Accomplishments that we're proud of Getting 16 simulators working consistently across four different engineering domains is something we are proud of. The PDF export feature turned out better than expected. It generates a complete interview preparation guide with AI-written answers, behavioral questions, and STAR responses for every question in a module, and if you answered questions during your session your answers and the AI feedback on them are included alongside the model answers. The three-tier AI fallback also works cleanly in practice. The platform degrades gracefully at every level. What we learned Building the simulators forced a much deeper understanding of the concepts than studying them ever did. You cannot build a PSI drift detector without actually understanding what PSI measures and why the thresholds are where they are. Writing interview questions and their rubrics, and then watching people answer them, sharpened how clearly we could explain these systems ourselves. On the technical side, building a clean abstraction over AI that handles multiple providers and graceful fallbacks taught us a lot about how to make AI-dependent features production-ready rather than fragile. What's next for MLOps Playground The immediate next step is improving the simulators for the monitoring and system design domains to match the depth of the deployment simulators. After that, I want to add a guided mode that walks you through a module in a structured order, lab first, then study guide, then interview, with checkpoints between each. Longer term, the platform could support user accounts so progress and session history persist across devices, and collaborative practice sessions where two people interview each other with AI playing the interviewer role in the background. <div