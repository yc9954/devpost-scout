---
slug: "shopii"
url: "https://devpost.com/software/shopii"
title: "Shopii"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 621
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/legal_professional"
  - "user/researcher"
---

# Shopii

> Your AI shopping assistant that finds honest product recommendations from real people, not paid reviews.

[Devpost](https://devpost.com/software/shopii) · hackathon [[NexHacks]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[developer]] [[legal_professional]] [[researcher]]

**stack** chatgpt, claude, digitalocean, node.js, postgresql, prisma, react, redis, tavily, typescript, wispr-flow

## How they structured the write-up

- inspiration
- what we built
- how we built it
- challenges we faced
- what we learned

## Body

Mechanical Keyboards Wireless Headphones Shopii Research Inspiration We've all been there: you need to buy a new product, so you search online and get bombarded with sponsored results, suspicious 5-star reviews, and "Top 10" listicles that are clearly paid placements. The modern shopping experience is broken. The real answers are buried in Reddit threads, YouTube comments, and forum discussions where actual users share their honest experiences. But who has hours to dig through all of that? That's what inspired Shopii — an AI-powered shopping assistant that does the research for you, surfacing genuine recommendations from real people instead of paid reviews. What We Built Shopii is a browser extension that acts as your personal shopping researcher. Ask it something like "I need good wireless headphones under $300" and it: Searches across Reddit, YouTube, expert reviews, and forums in real-time Extracts actual product recommendations with real user quotes and sentiment Presents curated suggestions with honest pros/cons and confidence scores Learns your preferences over time through an adaptive recommendation system The extension includes a chat interface for conversational product research, a "For You" tab with personalized suggestions, and the ability to save favorites. How We Built It Backend (API): Node.js with Fastify for a fast, lightweight server deployed on a Digital Ocean Droplet Prisma ORM with SQLite (dev) / PostgreSQL (production) + Redis server managed by Digital Ocean OpenAI GPT-4o-mini for natural language understanding and research synthesis Tavily API for web search across Reddit, forums, and review sites Firecrawl for extracting prices from JavaScript-rendered pages Supabase for authentication and real-time data sync Frontend (Extension): React 18 with WXT (Web Extension Toolkit) for cross-browser support Zustand for lightweight state management Tailwind CSS for rapid UI development Chrome Side Panel API for a non-intrusive shopping companion Key Technical Achievement: Our adaptive recommendation algorithm weights behavioral signals (50%) over stated preferences (25%), context (15%), and ratings (10%). This means the system gets smarter as you use it — it learns what you actually like based on what you click, save, and dismiss, not just what you say you want. Challenges We Faced Real-time research is slow — Searching multiple sources and synthesizing results takes time. We implemented streaming responses so users see results as they come in, and added caching for common queries. Price extraction is hard — Many retail sites load prices via JavaScript. We built a 2-tier fallback system: Tavily for static content, Firecrawl for dynamic pages. Cold start problem — New users have no behavioral data. We solved this with an onboarding flow that captures initial preferences, then gradually transitions to behavior-based recommendations as they interact more. Balancing personalization with discovery — If we only show what users have liked before, they'll never discover new products. Our algorithm intentionally includes "exploration" suggestions outside the user's stated preferences. Privacy vs. personalization — We wanted powerful personalization without being creepy. Solution: all behavioral data is stored locally until the user signs up, and users can view/clear their interaction history anytime. What We Learned Trust is everything in product recommendations. Showing sources and confidence scores matters more than flashy UI. Behavior > Stated preferences — What users do tells you more than what they say. Our "actions speak louder than words" approach to recommendations proved effective. Developer experience matters — We built a full mock/dev mode that requires zero API keys or external services, making onboarding new contributors painless. Browser extensions have unique constraints — Working within the Chrome Side Panel API and managing state across contexts taught us a lot about extension architecture. This story hits the key points hackathon judges look for: clear problem, creative solution, technical depth, honest challenges, and lessons learned. Feel free to adjust the tone or add personal anecdotes! <div