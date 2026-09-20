---
slug: "pulseearth-r3js08"
url: "https://devpost.com/software/pulseearth-r3js08"
title: "PulseEarth"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 579
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# PulseEarth

> PulseEarth is a real-time AI economic intelligence platform that turns global data, trade flows, and breaking news into actionable insights through an interactive 3D globe.

[Devpost](https://devpost.com/software/pulseearth-r3js08) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]] [[finance_payments]] [[labor_employment]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** ai, amazon-web-services, anthropic, api, bank, bbc, business, claude, css, docker, dynamodb, functions, github, google

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for pulseearth

## Body

PulseEarth 🌍 Inspiration Economic intelligence is scattered across dozens of websites, reports, databases, and news platforms. Understanding a country's economic health often requires switching between World Bank datasets, financial news sources, trade reports, and investment research tools. We wanted to create a single platform where anyone—from investors and founders to students, researchers, and policymakers—could instantly understand the world's economies through an intuitive visual experience. This led to a simple question: What if the entire world's economic intelligence could be explored through a living, interactive globe? That idea became PulseEarth. What It Does PulseEarth is an AI-powered global economic intelligence platform that transforms complex economic data into an interactive 3D experience. Users can: Explore countries on a real-time 3D globe View GDP, GDP growth, inflation, unemployment, trade, and innovation metrics Monitor real-time economic news Generate AI-powered executive briefings Generate AI investment reports Compare countries side-by-side Visualize trade routes and global economic relationships Explore economic heatmaps Analyze investment opportunities through intelligence layers Discover major global economic hubs through the City Network Listen to AI-generated economic briefings through the AI Anchor Instead of reading dozens of reports, users can understand a country's economic landscape in seconds. How We Built It Frontend Next.js React TypeScript Three.js react-globe.gl Tailwind CSS Backend Next.js Serverless API Routes Vercel Deployment Platform AI Layer Anthropic Claude for AI Briefings AI Investment Reports AI News Anchor Scripts Executive Summaries Data Sources World Bank Open Data IMF Economic Indicators Google News RSS Reuters Business BBC Business Country-specific economic news sources Cloud Infrastructure PulseEarth uses Amazon DynamoDB as its AWS database. DynamoDB stores global city intelligence, economic hub information, and supporting analytics that power the City Network and intelligence layers throughout the platform. The application is deployed globally using Vercel. Challenges We Ran Into Data Aggregation Economic data comes from multiple sources and countries publish indicators at different frequencies. We had to normalize and combine data into a consistent format. Real-Time News Quality Many news feeds contain duplicate, irrelevant, or outdated content. We built ranking and filtering logic to prioritize recent and relevant economic developments. AI Reliability AI-generated reports and briefings needed to remain accurate and grounded in real economic data. We implemented structured prompts, validation logic, and fallback mechanisms. Interactive Globe Performance Rendering a globe with multiple intelligence layers—including heatmaps, trade routes, city networks, and investment signals—required significant optimization to maintain smooth performance. Accomplishments We're Proud Of Built a fully deployed production application Successfully integrated AWS DynamoDB into a real-world use case Created a responsive and interactive 3D economic globe Combined AI, economic intelligence, visualization, and real-time news into a single platform Developed AI-powered executive briefings and investment reports Built a scalable serverless architecture using AWS and Vercel What We Learned Building PulseEarth taught us how challenging it is to combine real-time data pipelines, AI systems, cloud infrastructure, and immersive visualizations into a unified user experience. We gained valuable experience with: AWS DynamoDB Vercel serverless architecture AI application design Economic data processing News aggregation systems Interactive data visualization Production deployment workflows Most importantly, we learned that presenting complex information effectively can be just as important as collecting the information itself. What's Next for PulseEarth Our long-term vision is to evolve PulseEarth into a comprehensive economic intelligence platform. Future plans include: Historical economic timelines Predictive economic forecasting AI-generated country outlooks Personalized watchlists and alerts Institutional-grade analytics Portfolio tracking Multi-language support Enterprise and research subscriptions PulseEarth is our step toward making global economic intelligence more accessible, visual, and actionable for everyone. <div