---
slug: "eco-quest-htuvns"
url: "https://devpost.com/software/eco-quest-htuvns"
title: "Eco Quest"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 331
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/climate_energy"
  - "domain/retail_commerce"
  - "substrate/financial_record"
---

# Eco Quest

> EcoQuest is your gamified AI sustainability app. Complete eco-challenges, scan receipts, get smart shopping tips. Grow your digital plant as you reduce your real carbon footprint. Make green fun.

[Devpost](https://devpost.com/software/eco-quest-htuvns) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[climate_energy]] [[retail_commerce]]
**substrate** [[financial_record]]

**stack** climatiq, css, fastapi, gemini, langgraph, next.js, python, supabase, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eco quest

## Body

Inspiration We wanted to make sustainability feel less like a hassle and more like an adventure. Traditional carbon trackers are passive and boring, so we built an AI companion that actively guides you toward eco-friendly choices in real time. What it does EcoQuest is a gamified sustainability app where users grow a digital plant by taking real-world eco-actions. An AI shopping assistant suggests sustainable swaps, a receipt scanner calculates carbon impact, and personalized missions build lasting green habits. Users earn XP, level up their plant companion, and track their actual environmental impact. How we built it Frontend: Next.js with Tailwind CSS for a responsive, modern UI Backend: FastAPI with supabase Agentic AI: LangGraph orchestrates workflows, Gemini 2.5 flash powers the shopping agent, receipt parser, and mission generation Impact Data: Climatiq API provides scientific co2 emission factors for accurate carbon tracking Challenges we ran into Getting the AI shopping agent to generate contextual, helpful suggestions without hallucinating was tricky. We also struggled with different methods of receipt parsing, OCR versus Gemini API call. After testing out both we realized OCR fails to understand a lot of context behind the receipt (missing $ labels, can't understand tables and rows etc). Accomplishments that we're proud of We built a fully functional AI agent system that actually works! The shopping assistant feels genuinely helpful, not gimmicky. Our personalized mission generator adapts to individual lifestyles, so a vegan never gets "eat less meat" advice. The plant growth visualization creates real emotional connection. What we learned AI agents need careful orchestration, LangGraph was essential for complex workflows. We learned that users respond better to positive reinforcement (XP, plant growth) than guilt. Small, specific actions beat vague climate advice. Also, Gemini Vision is surprisingly good at reading messy receipts! What's next for Eco Quest Social features: Friend challenges and leaderboards Carbon offset marketplace: Convert XP into real tree-planting donations Expanded agents: Travel planner, energy monitor, fashion advisor Community goals: Unlock collective achievements when neighborhoods hit sustainability milestones <div