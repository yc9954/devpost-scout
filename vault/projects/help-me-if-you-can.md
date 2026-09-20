---
slug: "help-me-if-you-can"
url: "https://devpost.com/software/help-me-if-you-can"
title: "Help Me If You Can"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 360
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Help Me If You Can

> A task & reward hub with AI-powered candidate matching and XRPL payments

[Devpost](https://devpost.com/software/help-me-if-you-can) · hackathon [[Hack the North 2025]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** flask, gemini, mongodb, python, react, ripple, rlusd

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for help me if you can

## Body

Inspiration While working on my thesis, I sometimes needed feedback on my code in programming languages I wasn’t fully comfortable with. Having someone quickly review and validate my work would save me a lot of time and frustration. That pain point inspired me to build a platform where anyone can post a task, get expert help, and be confident in the quality of the result. At the same time, I wanted to experiment with RLUSD, a new and not yet widely adopted stablecoin on XRPL. Integrating it into real task flows felt like the perfect opportunity to explore its potential and push its adoption in practical use cases. What it does Help Me If You Can is a decentralized task and reward hub with three core parts: 1. Tasks & Rewards – Users create tasks, fund them with RLUSD or XRP, and assign solvers. Payments are held in escrow (native XRPL) or custodial holds (RLUSD) until work is approved. 2. AI Candidate Ranking – Gemini AI ranks applicants based on their skills and solved history, giving task creators clear recommendations. 3. AI Task Review Assistance – AI checks submissions (length, originality, relevance) and can suggest rework before final approval. How we built it Frontend: React Backend: Flask + MongoDB, with JWT authentication, wallet management, and XRPL/RLUSD payment integration. Payments: Rippled / XRPL testnet escrow for XRP, and custodial logic for RLUSD. AI: Gemini API for ranking candidates and reviewing solutions; Challenges we ran into Handling XRPL escrow transactions correctly (preventing tecNO_PERMISSION and ensuring funds are released only with valid conditions). Integrating Gemini AI for ranking candidates in a way that feels useful and not arbitrary. Also i tried to implement voice AI here, but unfortunately was not managed to do this. Frontend also was kind of a problem, because it is a lot of different elements. Accomplishments that we're proud of Seamless XRPL testnet integration, successfully funding wallets and paying out in both RLUSD and XRP. What we learned How to use AI and implement RLUSD payments in everyday life. What's next for Help Me If You Can Add voice AI, do better design, add more features from rippled <div