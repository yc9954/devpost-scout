---
slug: "beyondvelvet"
url: "https://devpost.com/software/beyondvelvet"
title: "BeyondVelvet"
hackathon: "The AI Champion Ship "
organization: "LiquidMetalAI"
winner: true
words: 427
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# BeyondVelvet

> See what the world really thinks—beyond the algorithmic bubble.

[Devpost](https://devpost.com/software/beyondvelvet) · hackathon [[The AI Champion Ship]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[accessibility]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** claude, radix, raindrop, react, typescript, vultr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for beyondvelvet

## Body

Inspiration Social media algorithms trap us in "velvet bubbles" where we only see content that confirms our biases. We realized small teams and researchers are flying blind, priced out of enterprise tools and stuck in echo chambers. We built BeyondVelvet to democratize access to unfiltered public opinion, helping users see the raw, diverse reality of human sentiment beyond their curated feeds. What it does BeyondVelvet is a serverless sentiment analysis platform that: Collects Data: Instantly scrapes raw posts from social media (Twitter/X) on any topic. Analyzes Sentiment: Classifies opinions, extracts trending keywords, and identifies user clusters. Visualizes Reality: Displays an objective dashboard of Positive, Neutral, and Negative sentiment distributions. Optimizes Costs: Intelligently caches results to make repeated insights instant and free. How we built it We architected a modern serverless stack using LiquidMetal AI's Raindrop Platform and Vultr infrastructure: Backend: Raindrop (v0.13) + Hono.js handling API logic at the edge. Storage: Vultr Object Storage (Seattle) for frontend hosting; Raindrop SmartBucket and D1 SQL for reports and data. Data Pipeline: Apify actors for scraping, feeding into our analysis engine. Scoring Logic: We calculate a Net Sentiment Score ($NSS$) weighted by engagement, ensuring viral posts impact the score more than unseen ones: $$NSS = \frac{\sum (w_i \cdot s_i)}{\sum w_i}$$ Where $s_i$ is sentiment ($-1, 0, 1$) and weight $w_i = \log(1 + \text{likes} + \text{shares})$. Challenges we ran into The Cost of APIs: Real-time social scraping is expensive. We solved this by implementing a Smart KV Cache with a 24-hour TTL, reducing API calls by over 95% for repeated queries. Unstructured Data: Raw tweets are messy. We had to build robust TypeScript schemas (Zod) to normalize erratic data from the scraper before it hit our database. Accomplishments that we're proud of True Serverless: Successfully deploying a full-stack app on Raindrop with multiple Smart Components working in harmony. Vultr Integration: Achieving high-performance frontend delivery via Vultr Object Storage. Launch-Ready UI: Building a polished, responsive dashboard with PDF exports and dark mode in a single hackathon sprint. What we learned Edge Architecture: How to effectively couple ephemeral serverless functions (Hono) with persistent storage (SmartBucket). The Value of Caching: For "wrapper" apps relying on third-party APIs, aggressive caching isn't just an optimization—it's the only way to make the business model work. What's next for BeyondVelvet Multi-Platform Activation: Turning on the Reddit, TikTok, and YouTube scrapers (architecture is ready, currently disabled for cost). SmartInference: Upgrading from keyword analysis to LiquidMetal SmartInference to detect nuance, sarcasm, and irony using LLMs. Live Streaming: Adding WebSocket support to stream posts onto the dashboard in real-time. <div