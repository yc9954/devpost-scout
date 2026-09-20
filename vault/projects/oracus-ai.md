---
slug: "oracus-ai"
url: "https://devpost.com/software/oracus-ai"
title: "Oracus AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 890
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/measured_ablation"
  - "mechanism/multi_agent"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# Oracus AI

> AI-powered focus group that predicts how your target market will react to any business decision, before you spend a dollar. 100s of personas, 14 market metrics, strategic playbook, under 2 minutes.

[Devpost](https://devpost.com/software/oracus-ai) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[measured_ablation]] [[multi_agent]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[health_clinical]] [[scientific_research]]
**substrate** [[document_pdf]] [[sensor_telemetry]]

**stack** amazon-nova, amazon-web-services, fastapi, python, react, scikit-learn, tailwind, typescript, vercel, vite, zustand

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for oracus ai

## Body

Inspiration Product decisions fail all the time. Companies spend months on focus groups and A/B tests that cost thousands, and most startups just skip that entirely and launch on gut feeling. I kept asking myself: what if you could simulate your entire target market's reaction to a decision before actually making it? Not a survey. Not a poll. A full simulated focus group with realistic personas who actually reason about your product based on their income, habits, and preferences. That's what Oracus AI is. What it does You type in any company name. Oracus auto-detects the company's products, pricing, audience, and competitors from public web data using Amazon Nova's web search grounding. Then it generates 100 diverse AI personas modeled on real-world demographic distributions for that company's market. You describe a change you want to test ("raise the subscription price to $13.99" or "launch a freemium tier"), and Oracus simulates each persona's individual reaction with sentiment scores, behavioral predictions, reasoning, and willingness to pay. After simulation, it computes 14 hard mathematical market indicators (NPS, churn risk, polarization index, loyalty paradox rate, income-sentiment correlation, and more), clusters dominant themes using K-Means on Amazon Titan Embeddings, fetches the company's real-world baseline metrics for comparison, and generates a profit-optimized strategic playbook. If the verdict is "Pivot," it suggests a revised strategy you can re-simulate with one click. That iterative loop is the core of the product. How I built it Six specialized AI agents, all running on Amazon Nova 2 Lite via Bedrock. The Population Architect generates persona archetypes from real demographics. The Simulation Engine runs 100 parallel Bedrock calls (one per persona) using forced tool use for structured JSON output. The analytics layer is a hybrid: all 14 market metrics are computed deterministically in Python with pandas and numpy (the LLM never does math), and theme discovery uses unsupervised K-Means clustering on Titan Embeddings. The Diagnostic Report agent synthesizes the hard numbers and clustered voices into an executive assessment. The Baseline Intelligence agent web-searches for real financial data. The Strategic Advisor compares simulated outcomes against the real baseline and produces the final playbook. Frontend is React + TypeScript + Vite + Tailwind with Zustand for state management and Recharts for data visualization. Backend is FastAPI deployed as serverless functions on Vercel. Each pipeline stage is its own API endpoint so no single call exceeds Vercel's timeout limits, and the frontend orchestrates the full flow with progressive loading states. Challenges I ran into Nova 2 Lite sometimes ignores forced tool use and returns raw markdown instead of the structured JSON I need. I had to build aggressive fallback parsers with regex extraction for every single agent call, plus retry loops with exponential backoff. Rate limiting was a real problem when firing 100 parallel persona simulations. I built an async token bucket rate limiter to stay within Bedrock's throughput limits without killing performance. LLM sentiment hallucination was another big one. Some personas would return sentiment scores on a 1-10 scale instead of the -1.0 to 1.0 range I specified. I added a normalization layer in the metrics pipeline that detects and squishes out-of-range scores automatically. The hardest challenge was debiasing. Without careful prompt engineering, every persona had a strong opinion about every change. Real markets have large neutral/indifferent populations. I had to explicitly permit indifference in the simulation prompt and separate archetype generation from scenario awareness so the population isn't over-indexed on the thing being tested. Accomplishments that I'm proud of I validated Oracus against Netflix's 2023 password-sharing crackdown, a well-documented real decision with known outcomes. Oracus correctly predicted the polarized reaction structure: solo subscribers would be indifferent while sharing households would react strongly negative. It also correctly identified that the financially important segments would be unaffected. That's the exact insight that justified Netflix's decision to proceed. The "hard math first, LLM interpretation second" architecture is something I'm really proud of. The LLM never calculates a single percentage. All 14 market indicators are computed deterministically, and the LLM only interprets pre-computed metrics. This makes the system mathematically reproducible, which is rare for an AI-heavy product. The whole pipeline runs 100 personas in about 2 minutes for under $0.10 on AWS. That cost efficiency is what makes the iterative simulation loop practical. What I learned Multi-agent architectures need way more error handling than you'd expect. When you have six agents in a pipeline and any one of them can return malformed output, you need fallback parsing, retries, and validation at every single boundary. I also learned that the most effective way to use LLMs in analytics is to NOT let them do the analytics. Compute everything you can deterministically, then hand the LLM a package of pre-computed facts and ask it to interpret. The outputs are dramatically more trustworthy. Prompt engineering for persona simulation is its own discipline. Small wording changes in the system prompt (like adding "you are allowed to feel indifferent") completely change the distribution of outputs across 100 personas. What's next for Oracus AI Historical simulation tracking so you can see how predictions evolve across multiple runs. Integration with real analytics platforms to validate Oracus predictions against actual post-launch data. Custom persona templates for specific industries. PDF export for shareable executive summaries. And the big one: competitive scenario testing, where you simulate how a competitor's customers would react to YOUR moves. <div