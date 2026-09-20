---
slug: "market_pulse"
url: "https://devpost.com/software/market_pulse"
title: "Market_Pulse"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 687
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/regulation_legal_text"
  - "substrate/web_dom"
---

# Market_Pulse

> AI-powered multi-agent financial sentiment platform that transforms real-time market news into actionable sentiment scores, trend insights, and visual analytics.

[Devpost](https://devpost.com/software/market_pulse) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[regulation_legal_text]] [[web_dom]]

**stack** analysis, api, apis, css3, face, fastapi, financial, html5, hugging, natural-language-processing, news, plotly, python, render

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for market_pulse

## Body

Architectural Workflow Dashboard Search History Analysis Result and Visualisations Inspiration Financial markets are heavily influenced by public sentiment. A single headline about inflation, earnings, regulations, or global events can instantly affect investor behavior and stock prices. However, manually tracking financial news across multiple sources and interpreting market sentiment is time-consuming and often subjective. We wanted to build a system that could automatically: collect relevant financial news, understand the emotional tone behind headlines, quantify market sentiment, and visualize it in an intuitive way. This led to the idea of Market Pulse — an AI-powered multi-agent financial sentiment analysis platform that transforms unstructured news into actionable sentiment insights. What it does Market Pulse analyzes financial sentiment for stocks, indices, and assets such as: AAPL, TSLA, RELIANCE, NIFTY, BTC The platform uses a 3-Agent AI workflow : 📰 Agent 1 — News Fetching Agent Fetches top financial headlines related to the selected ticker. 🔍 Agent 2 — Keyword & Sentiment Analysis Agent Extracts important keywords and determines the contextual sentiment behind the headlines. 📊 Agent 3 — Sentiment Scoring Agent Calculates a normalized sentiment score between: $$ -1 \leq S \leq 1 $$ Where: $$S \to 1$$ indicates strong positive sentiment $$S \to 0$$ indicates neutral sentiment $$S \to -1$$ indicates strong negative sentiment The platform then visualizes the analysis using: sentiment gauges, trend charts, headline displays, and categorized market mood indicators. Additional features include: search history tracking, printable reports, screen recording support, theme switching, and a fallback demo mode when APIs fail. How we built it We built Market Pulse using a modular AI-agent architecture. Frontend Streamlit for the interactive dashboard Plotly for charts and visualizations Custom UI styling using HTML/CSS Backend FastAPI for API handling Uvicorn as the ASGI server AI / NLP Pipeline Transformer-based sentiment analysis Keyword extraction workflows Custom scoring logic for sentiment normalization Deployment Deployed on Render The complete system workflow looks like this: User Input ↓ News Fetching Agent ↓ Keyword & Sentiment Agent ↓ Sentiment Scoring Agent ↓ Visualization Dashboard The sentiment score is generated using weighted sentiment aggregation across multiple financial headlines: $$ S = \frac{\sum_{i=1}^{n} w_i \cdot s_i}{\sum_{i=1}^{n} w_i} $$ Where: $$s_i$$ = sentiment polarity of headline (i) $$w_i$$ = importance weight of headline (i) Challenges we ran into One of the biggest challenges was handling inconsistent financial news APIs and rate limits. We also faced: deployment issues on Render, API timeout problems, backend/frontend communication delays, import path conflicts during deployment, and handling cold-start latency on free cloud infrastructure. Another major challenge was designing a sentiment scoring system that remained interpretable while still being responsive to real-time news changes. We also had to implement a fallback demo mode so the application could continue functioning even when APIs failed. Accomplishments that we're proud of We are proud that we successfully built: a fully functional multi-agent AI workflow, real-time financial news analysis, interactive sentiment visualizations, normalized sentiment scoring, and a production-ready deployed platform. We are especially proud of: the modular AI-agent architecture, the clean UI/UX, the fallback demo system, and the explainable sentiment pipeline. The project evolved from a simple sentiment checker into a scalable AI-powered financial analysis platform. What we learned Through this project, we learned: how to design modular AI-agent systems, how to deploy FastAPI + Streamlit applications, how to handle real-world API failures, how cloud deployment differs from local development, and how to build scalable NLP pipelines. We also gained practical experience in: sentiment analysis, asynchronous API workflows, debugging deployment environments, and designing user-friendly financial dashboards. Most importantly, we learned how difficult it is to transform noisy real-world financial data into meaningful insights. What's next for Market_Pulse We plan to expand Market Pulse into a much more advanced financial intelligence platform. Future plans include: real-time stock market streaming, portfolio-based sentiment tracking, AI-generated financial summaries, sentiment-based trading alerts, mobile responsiveness, and advanced forecasting models using LLMs. We also want to integrate: social media sentiment analysis, financial report summarization, and predictive market analytics. Our long-term vision is to build an intelligent financial assistant that helps users understand not just what the market is doing, but why it is behaving that way. <div