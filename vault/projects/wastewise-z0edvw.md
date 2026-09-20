---
slug: "wastewise-z0edvw"
url: "https://devpost.com/software/wastewise-z0edvw"
title: "WasteWise"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 424
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/supply_logistics"
---

# WasteWise

> Know if you'll actually use it- before you buy it

[Devpost](https://devpost.com/software/wastewise-z0edvw) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[supply_logistics]]

**stack** ai, aiv, code, css, gemini, generator, tailwind

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of:
- what i learnt
- what's next for wastewise

## Body

WasteWise Inspiration Most sustainability apps tell people what they should do, but very few help them understand their own behavior. I noticed that a lot of waste isn’t intentional — it comes from impulse buying, over-optimism, and forgetting past patterns. WasteWise was inspired by a simple question: “What if you knew you wouldn’t use something — before you bought it?” The goal was to shift sustainability from guilt-driven choices to self-awareness and smarter decisions. What it does WasteWise predicts the probability that a product will become unused waste for a specific user before they purchase it. Users enter (or auto-detect) a product they’re considering buying, and WasteWise: Analyzes their past purchase behavior Compares similar items and usage patterns Outputs a personalized waste-risk score Explains why the risk is high or low Suggests gentle alternatives like delaying, borrowing, or buying second-hand Over time, the app learns from real outcomes and becomes more accurate. How I built it WasteWise is built as a personalized, explainable AI system: Frontend: Clean, minimal UI focused on clarity and calm decision-making Backend: API that processes user inputs and generates predictions Machine Learning: Behavioral features (category usage rate, price sensitivity, impulse patterns) A lightweight, explainable model (logistic regression / random forest) Outputs probability scores instead of binary decisions Feedback Loop: Users log what actually happened to purchases The model retrains and improves over time The system is intentionally privacy-first and designed to work without external integrations for the MVP. Challenges I ran into Cold start problem: Predicting waste with limited user history required careful feature design and reasonable defaults Explainability: It was important that predictions didn’t feel like a “black box” Tone & UX: Avoiding shame or judgment while still influencing behavior was a design challenge Scoping: Keeping the AI powerful but realistic for an MVP required discipline Accomplishments that I'm proud of: Built an AI system that feels personal, not generic Designed a sustainability tool that focuses on behavioral insight, not restriction Balanced technical depth with clear, human-centered UX Created an idea that is both ethically responsible and practically useful What I learnt Behavioral data can be more powerful than large datasets Explainable AI builds far more trust than complex models Sustainability solutions work best when they empower, not pressure Designing how feedback is delivered matters as much as the prediction itself What's next for WasteWise Browser extension for real-time purchase checks Smarter item similarity detection Carbon-impact estimates alongside waste probability Optional anonymized insights for cities and sustainability research Expanding into B2B tools for conscious retail and ESG reporting <div