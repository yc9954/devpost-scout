---
slug: "alpha_omega-6tu9jo"
url: "https://devpost.com/software/alpha_omega-6tu9jo"
title: "Roamly — AI Travel Planner"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 767
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Roamly — AI Travel Planner

> Plan any trip in seconds with AI. Roamly uses Amazon Nova Lite on Bedrock to generate day-by-day itineraries, smart packing lists, budget breakdowns, and real-time travel chat — all in one app.

[Devpost](https://devpost.com/software/alpha_omega-6tu9jo) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[structured_db]] [[web_dom]]

**stack** amazon, bedrock, boto3, css3, fastapi, html5, javascript, jwt, lite, nova, python, react, rest, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for roamly — ai travel planner

## Body

Inspiration Every time I've planned a trip, I've ended up drowning in browser tabs — one for flights, another for hotels, a blog for itinerary ideas, a spreadsheet for budget, and a Reddit thread for packing advice. None of these tools talk to each other, and the whole process can easily eat 10+ hours for a single week-long trip. I wanted to build something that felt like having a well-travelled friend on speed dial — someone who could take your destination and dates and just handle it . When Amazon Nova launched on Bedrock, the model's speed and reasoning quality made that vision actually achievable in a hackathon window. What it does Roamly is an AI-powered travel planning app that turns a few inputs into a complete trip plan in under 30 seconds. It has four core features: AI Itinerary Generator — enter your destination, dates, budget level, and interests, and Nova produces a detailed day-by-day plan with timings, venue suggestions, cost estimates, and insider tips. Smart Packing List — context-aware checklists tailored to your destination, season, cultural norms, and planned activities (hiking gear for Patagonia, modest clothing for Kyoto temples). Budget Estimator — itemised cost breakdowns across accommodation, food, transport, activities, and miscellaneous — with money-saving tips for each category. AI Concierge Chat — a multi-turn conversational assistant that answers any travel question in real time, with full awareness of your trip context. How we built it The stack is deliberately lean so the AI does the heavy lifting: Backend — FastAPI (Python) exposes four endpoints that call Amazon Bedrock's Converse API using amazon.nova-lite-v1:0 . Streaming responses are served via Server-Sent Events so users see output token-by-token. Frontend — React + Vite SPA with five feature pages. Each page renders Nova's structured JSON output — interactive packing checkboxes, animated budget bars, and live streaming chat bubbles. AI — All intelligence runs through a single call_nova() / call_nova_stream() helper wrapping the Bedrock SDK. Prompts are engineered to return strict JSON schemas so the UI can parse and render them reliably. Auth — JWT-based authentication with saved trips stored per user. Challenges we ran into Consistent structured output from a streaming LLM — Getting Nova to return valid, parseable JSON every time, especially mid-stream, required significant prompt iteration. The final approach defines the exact output schema in the system prompt and post-processes the stream to extract the JSON block even if Nova adds surrounding prose. Streaming JSON to the frontend — Streaming works beautifully for free-form text, but the itinerary endpoint streams structured JSON. We buffer tokens on the client and only render once a complete JSON object is detected, giving a smooth progressive reveal. Making it feel instant — Nova Lite is fast, but first-token latency still matters. Showing a skeleton UI immediately and surfacing the first streamed tokens within ~1 second was key to keeping the experience feeling snappy. Accomplishments that we're proud of A full working app — all four AI features functional end-to-end — built and polished within the hackathon window. Real-time streaming that makes AI responses feel alive rather than a static wall of text appearing all at once. A prompt engineering approach that reliably produces structured, UI-ready JSON from a generative model without any post-processing LLM calls. A UI that genuinely looks and feels like a product, not a prototype. What we learned Streaming changes everything. The perceived wait time drops dramatically when users see tokens appear immediately — even if total generation time is the same. Prompt structure drives output quality. Explicit field names, example formats, and firm schema instructions in the system prompt are more reliable than asking the model to "return JSON." React context + hooks make stateful AI apps clean. Managing multi-turn conversation history across page navigations was elegantly solved with a global AppContext — no external state library needed. Amazon Nova Lite punches above its weight. For structured reasoning tasks like itinerary generation, the quality-to-latency ratio is excellent for a real-time user-facing product. What's next for Roamly — AI Travel Planner Live data integrations — plug in real flight prices, hotel availability, and weather forecasts so estimates are based on actual data, not AI approximations. Collaborative trip planning — share a trip with friends and let multiple users contribute to the same itinerary in real time. Mobile app — a React Native port so Roamly is available offline and can send day-of activity reminders. Voice mode — use Nova's multimodal capabilities to let users plan trips entirely through conversation, hands-free. Post-trip memory — let Nova learn from past trips to make future recommendations progressively more personalised. <div