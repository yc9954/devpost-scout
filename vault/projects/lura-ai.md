---
slug: "lura-ai"
url: "https://devpost.com/software/lura-ai"
title: "lura-ai"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 463
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# lura-ai

> Smart AI app for tracking income, expenses, and savings with real-time financial advice

[Devpost](https://devpost.com/software/lura-ai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[educator_student]] [[small_business]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** ai, chart.js, css3, express.js, groq, html5, javascript, jwt, mongodb, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lura-ai

## Body

Inspiration Managing personal finances is one of the most common struggles for students, freelancers, and young professionals. Most people don’t fail because they don’t earn enough, but because they lack visibility and structure in how they spend and save money. We were inspired to build Lura AI to make budgeting feel simple, intelligent, and interactive — like having a personal financial advisor available 24/7. What it does Lura AI is a smart budgeting assistant that helps users track income, expenses, savings, investments, and financial goals in one unified platform. It provides: Real-time financial dashboards and analytics AI-powered financial advice using Groq Budget health scoring system Interactive Kanban-style financial planning AI terminal for instant financial queries Visual charts for spending and savings analysis It turns raw financial data into actionable insights. How we built it We built Lura AI using a full-stack JavaScript architecture: Frontend: Bootstrap 5 + Vanilla JavaScript + Chart.js Backend: Node.js + Express (ES Modules) Database: MongoDB with Mongoose AI Integration: Groq SDK using llama-3.1-8b-instant The system is structured into clean layers: Controllers for handling requests Services for business logic and AI processing Models for data structure REST APIs for communication between frontend and backend We also implemented a single-page application (SPA) design to ensure smooth user experience without page reloads. Challenges we ran into One of the biggest challenges was designing a system that combines real-time financial analytics with AI-generated insights without making the system slow or expensive. We also faced challenges in: Structuring AI prompts to generate consistent and useful financial advice Designing a clean and intuitive UI for complex financial data Synchronizing frontend state with backend MongoDB data Ensuring the application remains responsive while handling multiple AI requests Accomplishments that we're proud of We are especially proud of: Building a fully functional AI-powered financial assistant from scratch Creating a multi-interface system (Dashboard, Analytics, Terminal, Kanban, AI Chat) Implementing a budget health scoring system that visually reflects financial status Successfully integrating Groq AI for real-time financial reasoning Designing a production-ready full-stack architecture suitable for scaling What we learned This project helped us strengthen our skills in: Full-stack JavaScript development API design and system architecture Working with AI models in real-world applications MongoDB data modeling and optimization UX design for data-heavy applications We also learned how important it is to balance technical complexity with user experience. What's next for lura-ai In the future, we plan to expand Lura AI into a complete personal finance ecosystem by adding: Secure authentication system (JWT + OAuth) Mobile application version Predictive AI for future spending behavior Bank account integration PDF financial reports and export system Smart alerts for overspending and savings goals Deployment to cloud with real-time scaling Our long-term vision is to make Lura AI a personal AI financial companion for everyone. <div