---
slug: "guardian-ai-powered-fraud-prevention-for-your-money"
url: "https://devpost.com/software/guardian-ai-powered-fraud-prevention-for-your-money"
title: "Guardian: AI-powered Scam and Fraud Prevention"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 647
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/general_public"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/transcript_audio"
---

# Guardian: AI-powered Scam and Fraud Prevention

> Defend against suspicious charges before they even reach your account, utilizing voice alerts, agentic reasoning, and real-time merchant intelligence.

[Devpost](https://devpost.com/software/guardian-ai-powered-fraud-prevention-for-your-money) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[elder_child_care]] [[finance_payments]] [[retail_commerce]]
**user** [[general_public]] [[small_business]]
**substrate** [[financial_record]] [[transcript_audio]]

**stack** anthropic, brightdata, claude, coderabbit, css3, django, fetch, figma, fish, github, html5, javascript, machine-learning, numpy

## How they structured the write-up

- our inspiration
- how we built it
- challenges we ran into
- accomplishments
- what we learned
- what's next for guardian

## Body

This page demonstrates our risk score analysis, all the factors that come together to give a total risk score. Showcasing the notification center, hovers above the transactions dashboard, transitions/slides in from the right The main transactions dashboard, showcasing one's transactions across all bank accounts. Our Inspiration About 75% of Americans have been victims to some form of financial fraud in their life. Banks let you know when fraudulent activities occur, but only after your money’s already gone. What if we could stop the fraud in its tracks before our wallets get drained. And that’s exactly where Guardian comes in: protecting your hard-earned money from fraud. When we first thought of the idea, we wanted to help the elderly population as they are five times more likely to be targeted by scammers than younger adults. Banks often have difficult and complex ways to try and get a refund, which elderly people could use a helping hand to do. We built something that gives everyone confidence and protection. Guardian is bringing back financial independence to the people. We don’t just prevent fraud, we also provide peace of mind, along with a wallet with a few more green bills at the end of the day! How we built it We created Guardian as a real-time fraud protection solution powered by a modular Python Flask backend and a clean, accessible React frontend. Our risk engine, an unsupervised anomaly detection framework using SHAP, identifies suspicious transactions based on features like abnormal spending amounts, time of charge, foreign transactions, and rate of transactions. We then enhance our risk detection using BrightData's web-scraping, which lets us detect changes in merchant reputation and patterns of consumer complaints. If a transaction looks dangerous, Claude (Anthropic) generates a friendly, easy-to-understand explanation and a recommended action language specifically designed to support seniors who may feel anxious or confused during fraud events. That script is then automatically transformed by Fish Audio into a natural-sounding voice alert that speaks directly to the user. The entire workflow completes in under a second, and helpful automation powered by Fetch.ai handles follow-up tasks like checking for duplicate charges or preparing a dispute kit. Meanwhile, the UI shows the voice transcript, a risk level, and two large buttons keeping users in control while Guardian does the heavy lifting to keep them safe. Challenges we ran into Integrating multiple intelligent systems in real time was NOT easy, especially under hackathon pressure. Authentication and environment handling across several APIs challenged us early on, and we worked hard to optimize latency. Accomplishments We’re incredibly proud that in just one weekend we built a fully working voice-first prototype that: blocks fraud before money is stolen, speaks to the user like a real human guardian automates the stressful parts of post-fraud recovery combines Bright Data, Anthropic, Fish Audio, and Fetch.ai into one smooth agent. What we learned We learned that designing for financial security isn’t just a data problem, it’s an intrinsically human one. During moments of fear, people need clarity, reassurance, transparency, and compassion. We learned how to combine multiple AI systems together operating simultaneously, while handling security and reliability with care. We learned that AI isn’t just a tool for automation, it can become a protector that gives people peace of mind. What's Next for Guardian We plan to run a pilot with a fintech or card-issuing partner, add multi-language voice alerts to support diverse communities, improve personalization to reduce false positives even further, and collaborate with both smart speakers for users who aren’t comfortable with apps, and accessibility experts to deepen our senior-first design. Our goal is simple : Ensure that everyone, especially the elderly, feels safe and confident when they use their money. For us, Guardian has the potential of being more than just a hackathon project. Rather, it's the beginning of a financial safety companion for the people who need protection the most. <div