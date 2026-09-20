---
slug: "leafari-pokemon-go-for-plants"
url: "https://devpost.com/software/leafari-pokemon-go-for-plants"
title: "Leafari - Pokemon Go for Plants"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 453
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Leafari - Pokemon Go for Plants

> Leafari turns any stroll into an AR-powered quest to spot, snap and master wild plants, earning badges and building a living field guide that grows with every adventure.

[Devpost](https://devpost.com/software/leafari-pokemon-go-for-plants) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[climate_energy]] [[finance_payments]]
**user** [[general_public]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]]

**stack** bolt.new, convex, cursor, expo.io, gemini, openai, openrouter, react-native, revenue-cat

## How they structured the write-up

- 🌱 inspiration
- 🛠️ how we built it
- 🚀 what we learned
- ⚔️ challenges faced
- 🌍 impact & next steps

## Body

🌱 Inspiration My four kids and I dreamed up Leafari to help people reconnect with nature through AI. We believe that the more you know your local ecology, the more you’ll care for it. We didn’t just want another plant-ID tool - we wanted an adventure that lures kids (and grown-ups) off the couch, out the door, and into the wild. Picture Pokémon GO ’s exploration energy blended with Duolingo ’s bite-sized learning loops, but focused on botany and ecology. 🛠️ How We Built It Layer Tech Why It Fit Mobile React Native + Expo Fast cross-platform shipping in a weekend-friendly toolchain Backend Convex.dev Live data sync & serverless functions without ops overhead AI • Google Gemini → plant facts • GPT-4o → image ID + badge art Best-of-breed models for vision, language, and image generation Payments (coming soon) RevenueCat Drop-in paywalls + cross-store receipts Development window: 6 days total (two long weekends). Dad coded; kids served as product managers and QA testers, brainstorming quests, ranks, and UI tweaks. Bolt.new made it possible by getting the entire app scaffolded and the foundation set in one day. 🚀 What We Learned Kid-driven PM is gold. Their curiosity surfaced delightful features adults overlook. AI is a creative teammate. Prompt engineering can turn models into badge artists and field-guide authors. Scope is everything. A tight, badge-driven MVP beats a sprawling feature list when time is scarce. ⚔️ Challenges Faced Dynamic Badge Generation The big dragon. Crafting prompts that yield consistent, on-brand badge art took many iterations. We ended up building a mini workflow that: Feeds plant traits into GPT-4o → gets back a PNG. Post-processes in JS to remove background. Stores the final PNG in Convex and on device for instant in-app rendering. This means the amount of plant badges is vast, as the users will be generating them. Future user that discover an plant that already has a badge will load the existing badge and plant information. The users are making our badges and plant library for us! Time Crunch With two weeks left in the hackathon - and real life happening - every hour mattered. Continuous delivery via Expo’s OTA updates saved us countless App Store review cycles. 🌍 Impact & Next Steps Leafari already turns a neighborhood walk into a wild plant quest - capture, identify, collect, repeat. Next we’ll: Launch reinforcement games and quizzes to reinforce the learning of the plants they already discovered Add multiplayer “expeditions” so friends can team-up to map local biodiversity. Integrate seasonal challenges Partner with organizations for special events around invasive and endangered species Our hope: a new generation of citizen naturalists who learn, and fall in love with, the living world right outside their door. <div