---
slug: "money-council"
url: "https://devpost.com/software/money-council"
title: "Money Council"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 818
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Money Council

> Money Council gives students and young professionals instant, AI-powered financial plans. Build your profile and get clear advice to save, pay off debt, and invest smarter.

[Devpost](https://devpost.com/software/money-council) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[education]] [[finance_payments]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]]

**stack** expo.io, express.js, firebase, gemini, groq, mongodb, node.js, react, remotion, tailwindcss

## How they structured the write-up

- about the project
- what you can do
- what inspired us
- how we built it
- challenges we faced
- what we learned
- what's next for us

## Body

Landing Page Sign In / Sign Up Page Profile Page Voice Input to fill profile quicker Dashboard Page Command Centre Page Transactions Page Goals Calendar Page Time Machine Page (in next 10 years) Split (Make groups and split expenses) Group in Split Page WhatsApp linking docs Page WhatsApp bot that adds transaction Stock Picks Page Investment Scout Page Budget Agent Page Savings Agent Page Debt Crusher Page Stealth Mode (all financial numbers blurred) About the project Money Council is a fintech platform that turns your real income, expenses, goals, and risk tolerance into a clear monthly plan you can actually follow. It is built for students and young professionals who want guidance that feels human, specific, and doable. We also tried our best to make adding transactions feel effortless, because tracking only works if it is easy. You can connect your profile to WhatsApp, and you can also use our mobile app that works offline and includes Split. What you can do Main Dashboard: A quick snapshot of where your money is going and what to do next. It is the fastest way to understand your month at a glance. Command Center: Your control room for key signals and actions across the platform. It helps you stay focused on the next best move. Council Synthesis: Summarizes all the insights and advice into a 30 second video. It is designed to be updated if anything is changed, so it always reflects your current situation. Finance Tools Transactions: Log and review spending with minimal friction. The goal is to make tracking feel lightweight, not like homework. Goal Plans: Turn goals into a timeline and monthly targets. It keeps long term goals connected to small weekly actions. Time Machine: Compare future scenarios so decisions feel less scary. It makes tradeoffs visible before you commit. Split: Track shared expenses with friends or groups in one place. It is designed to reduce awkwardness and missed payments. WhatsApp: Link your profile via WhatsApp and interact in a familiar chat flow. It is our fastest path from “I should track” to “I tracked.” Invest Stock Picks: Curated stock ideas based on the product’s investing experience. It is meant to be beginner friendly and confidence building. Investment Scout: A dedicated investing agent to help you explore options that match your risk tolerance. It keeps the guidance personalized rather than generic. Agents Budget Agent: Helps you build a realistic spending plan without guilt or jargon. It focuses on what is sustainable. Savings Agent: Helps you set savings targets and make them achievable. It turns “save more” into a concrete habit. Debt Manager: Helps you prioritize and plan repayments. It aims to reduce interest drag and mental load. Account and controls Profile: Update the details that power your recommendations. Better inputs lead to better plans. Toggle Theme: Switch light and dark mode for comfort. It is a small touch that makes daily use nicer. Stealth Mode: A privacy friendly view for using the app in public. It enables you to use the platform without displaying sensitive financial information on the screen. Log out: End your session safely. It is there for shared devices and peace of mind. What inspired us Seeing peers stress about money while feeling too embarrassed to ask for help Realizing that “good advice” often fails because it is not personalized to someone’s constraints Wanting to make the first step feel easy: start with your profile and get a plan How we built it Frontend: React + Vite for a fast, modern dashboard and onboarding flow. Backend: Node.js + Express for API routes and orchestration. Data: MongoDB with Mongoose models for students, profiles, transactions, and goals. Auth: Firebase authentication to keep sign-in smooth. UX: Tailwind CSS for a clean, responsive UI. We focused on making the system feel like a real workflow. Capture the profile, track transactions, generate guidance, and then synthesize it into a single plan. Challenges we faced Designing the profile input flow to be comprehensive yet not overwhelming. We had to iterate on the questions and how they were presented to get the right balance. Working with a new library (Remotion) for the video generation. It took some time to understand how to structure the components and manage the state for dynamic content. What we learned A great product is often just a great sequence: collect the right inputs, compute the right signals, and present a small set of high-confidence actions. Personal finance is less about perfect math and more about behavior, clarity, and consistency. Multi-perspective guidance is powerful, but the real value is in the synthesis and prioritization. What's next for us Adding the ability to connect bank accounts for automatic transaction tracking. This will reduce friction and make the insights more accurate. Use messaging queues and workers to handle all the LLM calls asynchronously. This will improve performance and allow us to scale better as we add more features. <div