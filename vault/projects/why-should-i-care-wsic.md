---
slug: "why-should-i-care-wsic"
url: "https://devpost.com/software/why-should-i-care-wsic"
title: "Why Should I Care (WSIC)"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 584
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "domain/media_journalism"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Why Should I Care (WSIC)

> WSIC is a modern web application that helps users explore new topics and expand their knowledge through engaging, visually appealing format designed to spark curiosity and encourage learning.

[Devpost](https://devpost.com/software/why-should-i-care-wsic) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[retrieval_grounding]]
**domain** [[labor_employment]] [[media_journalism]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** azure-postgres, convex, exa-api, google-agent-development-kit, google-cloud-run, nextjs, python, qstash, react-markdown, render, serper-api, shadcn, tailwind, tanstack

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for why should i care (wsic)

## Body

Thumbnail Dashboard (Web) Topic page (Web) Explore page (Web) Profile page (Web) Dashboard (Mobile) Inspiration The internet is overflowing with information, but most people struggle to understand why something actually matters . When reading about scientific concepts, historical events, or emerging technologies, the "so what?" is often missing. Why Should I Care (WSIC) was born from my idea of making knowledge more contextual, interactive, and relevant to real life . Instead of just dumping facts, WSIC helps people connect topics with everyday use cases, and real-world impact. What it does Why Should I Care (WSIC) is an innovative ed-tech + social media platform that helps users discover interesting topics. Using advanced multi AI agent architecture and intelligent search, the platform creates comprehensive, interactive learning modules on-demand, making even the most obscure subjects accessible and engaging. It is a learning platform that answers the fundamental question: “Why should I care about this topic?” 🔎 Search System – Combines keyword + semantic vector search for finding relevant topics. ⚙️ Content Pipeline – Multi-agent workflow: research → generate → fact-check → assemble. 🧩 Interactive Modules – Quizzes, flashcards, and real-world relevance sections. 📊 Dashboard – User login (Google OAuth), metrics, and saved topics. 🎨 Frontend & UX – Clean glassmorphism design with responsive Next.js + Tailwind. 🗄 Backend – Powered by Postgres, Convex DB, job queues (QStash), workers (Render), and multi AI agent architecture developed using Google ADK and hosted on Google Cloud Run. How I built it I built WSIC in 3 weeks using a combination of modern tools and Kiro (Amazon’s new AI IDE) to speed up development. 📝 Spec-Driven Development (Kiro) – I used this to outline the initial plan and generate boilerplate code. 🎛 Agent Steering (Kiro) – Helped me maintain UI and coding style consistency. 🔌 MCP Integration (Kiro) – Allowed me to connect to Convex DB for testing. 🪝 Agent Hooks (Kiro) – Generated comprehensive documentation automatically. 🎶 Vibe Mode (Kiro) – My most heavily used feature. I even ran into overages on the Pro plan, but it was worth it because of the code quality powered by Claude 4. 🏗 Stack – Next.js + Tailwind for frontend, Convex + Postgres for databases, QStash for queues, workers on Render, and AI services developed using Google ADK and hosted on Google Cloud Run. Challenges I ran into ⚖️ Balancing AI-generated code quality vs. unnecessary over-generation. ⏱ Building the search page (the core of WSIC) on the last day of the hackathon — it took ~10 iterations with Kiro, but it worked beautifully. 🔌 Integrating multiple services (Postgres, Convex, QStash, Render, Cloud Run) into one smooth pipeline. Accomplishments that I'm proud of 🚀 Building a fully functional MVP in 3 weeks. 🔎 Developing a powerful search + semantic system . 🧠 Designing an end-to-end content pipeline with multi-agent orchestration. 🎨 Delivering a polished frontend with responsive design. ✨ The search page , generated using Kiro, was the most impressive piece. What I learned How AI-assisted development (with tools like Kiro) can drastically accelerate building complex systems. The importance of agent steering to keep AI output aligned with design goals. How multi-agent pipelines can create structured, interactive educational content. The value of integrating multiple services into a unified architecture. What's next for Why Should I Care (WSIC) 🌍 Expand topic coverage and depth. 🤝 Build more collaborative and social features - Rewards, Learning communities, Notes etc. 📈 Smarter content graphs: make the system automatically detect and connect similar content for more contextual learning. <div