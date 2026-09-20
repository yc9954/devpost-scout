---
slug: "ai-math-tutor-8ihuok"
url: "https://devpost.com/software/ai-math-tutor-8ihuok"
title: "AI Math Tutor"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 465
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
---

# AI Math Tutor

> AI + symbolic-math platform delivering step-by-step solutions, interactive lessons, and personalized instruction across algebra, calculus, linear algebra, and AI/ML—turning confusion into mastery now!

[Devpost](https://devpost.com/software/ai-math-tutor-8ihuok) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]

**stack** ai/ml, dockers, fastapi, flutter-(mobile), go, grpc, jwt, kubernetes, llm-go, matplotlib, numpy, openai, python, pytorch/tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai math tutor

## Body

Welcome to AI Math Tutor Inspiration My motivation for AI Math Tutor is personal: it began while mentoring my high-schooler through algebra, geometry, and early calculus. Seeing the gap between “almost there” and true understanding pushed me to build a tutor that explains why, not just what. With two decades of Java/Spring and secure, scalable systems, I’m bringing that rigor to an educational app that students can leverage as an always-available coach—delivering step-by-step solutions, intuitive visuals, and clear guidance. The goal is to help more kids—at home, in classrooms, and in community programs—gain confidence, master fundamentals, and grow their curiosity. Even strong students get stuck between “steps” and lose confidence. I wanted a tutor that pairs symbolic math (deterministic, correct) with natural-language explanations (clear, human) and wraps it in a developer-grade platform: observable, secure, and ready to scale. What it does • Step-by-step solver: Symbolic solutions with explanations, not just final answers. • Interactive checks: Auto-generated quizzes with targeted hints and “why” feedback. • Visual intuition: Plots for functions, gradients, vectors, eigen-geometry. • Personalized paths: Tracks progress, adapts difficulty and topics. • Realtime sessions: Collaborative walkthroughs for coach/learner. How we built it • Spec-driven from day one: Requirements, design, and task breakdowns guided the build; 13 phases and 40+ tasks. • Microservices architecture: o Python math engine (SymPy, NumPy) for deterministic solving & plots. o Go API gateway for concurrency, sessions, and WebSocket realtime. o React frontend for a clean, responsive UI. • Production disciplines: JWT auth & RBAC, health checks/monitoring, caching, Docker/K8s deployment. • LLM integration: AI explanations layered on top of exact symbolic steps. Challenges we ran into • Marrying LLMs with math rigor: Keeping explanations helpful without drifting from exact steps. • State & sessions at scale: Reliable realtime collaboration with robust session management. • Rendering math cleanly: Consistent LaTeX/plot output across devices. • Security first: Roles, tokens, and safe sandboxing for user-generated math/code. Accomplishments that we're proud of • Comprehensive health/observability wired throughout services. • End-to-end auth (JWT, sessions, RBAC) that feels seamless to learners. • Realtime WebSocket collaboration stable under load. • A capable symbolic engine that explains steps clearly and visually. What we learned • A spec-to-code approach accelerates complex builds and reduces rework. • Separation of concerns (Go for I/O & sessions, Python for math) keeps performance predictable. • Great pedagogy is a feature: Explanations, pacing, and visuals are as critical as algorithms. What's next for AI Math Tutor • Mobile & handwriting/voice input (OCR/STT) for natural problem entry. • Teacher/parent dashboards with mastery insights and interventions. • Spaced-repetition & mastery learning for long-term retention. • Deeper AI/ML math tracks: optimization, eigen/spectral methods, backprop intuition labs. • Privacy & compliance by design (data minimization, export/delete, audit trails). • Open source roadmap: modularize core components for community reuse. <div