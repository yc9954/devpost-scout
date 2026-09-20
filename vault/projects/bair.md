---
slug: "bair"
url: "https://devpost.com/software/bair"
title: "Bair"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 440
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Bair

> A finance buddy that budgets for you.

[Devpost](https://devpost.com/software/bair) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** flask, groq, nextjs, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bair

## Body

Inspiration Many students and young adults struggle with managing money — not due to lack of discipline, but due to lack of guidance, structure, and clarity. Budgeting apps often track your finances, but rarely coach you. We wanted to build something different: A budgeting companion, not just a dashboard. We envisioned a conversational, AI-powered finance buddy that would help users not only track their budgets but make smart decisions in real time — like a friend who’s good with money, always there when you ask, “Should I buy this?” What it does Bair is a personal budgeting assistant designed to: Analyze a user's income, expenses, and goals Automatically set daily and monthly budgets Use AI to coach users through real-world purchase decisions Track streaks of responsible spending to gamify saving Help users achieve long-term savings goals (e.g., vacation fund) Offer verbal (voice-based) interactions for real-time finance Q&A Recommend budget-friendly food options (meal deals, cheap spots) Example interaction: “Can I buy this $70 concert ticket tonight?” Bair checks your spending, savings, and goals — then gives a thoughtful response with budgeting logic and suggestions. How we built it Frontend: React + Tailwind CSS for a sleek mobile-first UI Backend: Flask (Python) serving API endpoints and OpenAI integration AI Logic: OpenAI GPT-4 used to process structured user data (income, category spending, goals, streaks, etc.) and return natural-language financial advice Challenges we ran into Designing prompts that made the AI feel like a coach, not just a rule-based filter Parsing raw bank statement data reliably via PDF upload and matching it into categories Enforcing real-time budget logic dynamically, without making the app feel rigid Building smooth fallback logic when a user didn’t submit full data (e.g., no budget set yet) Managing user privacy and data securely while offering customization Accomplishments that we're proud of Built a prompt system that can reason through spending decisions like a human coach Developed real-time feedback logic that incorporates user streaks, rollover savings, and long-term goals Integrated voice interaction to make financial coaching more accessible and conversational What we learned Streaks, encouragement, and small wins are psychologically powerful in changing financial behavior Real-time decisions (e.g., “Should I buy this?”) need deep context — which we modeled using structured inputs What's next for Bair Launch a mobile app version of Bair with push notifications and spending alerts Integrate real bank data via Plaid to automate transaction tracking Improve AI feedback with historical trends and monthly summaries Add scheduling for smart reminders (e.g., “Only 4 days left to hit this week’s savings goal!”) Build a deals aggregator to recommend cheap food, gas, or events based on location + budget <div