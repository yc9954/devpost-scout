---
slug: "stratify-ai"
url: "https://devpost.com/software/stratify-ai"
title: "Stratify Ai"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 943
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# Stratify Ai

> Turn economic indicators into crypto insights. Local AI analyzes FRED data, news, market trends → probability forecasts with AI narratives. 100% free, zero cloud costs. Built with Ollama.

[Devpost](https://devpost.com/software/stratify-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[finance_payments]] [[labor_employment]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[transcript_audio]]

**stack** axios, coingecko, fastapi, fredapi, jwt, newsapi, ollama, pydantic, python, react, reportlab, sqlalchemy, sqlite, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stratify ai

## Body

Detailed dashboard of the crypto coin Details of Global factors that affects the currency Pdf dowmload and summary data Ai- Analysis About the coin based on affecting factors Inspiration Stratify AI was inspired by a fundamental gap I observed in the cryptocurrency ecosystem. Most platforms focus heavily on technical indicators price charts, RSI, MACD, and short term momentum signals but they rarely connect crypto markets to the broader macroeconomic environment. However, real financial markets are deeply influenced by central bank policies, inflation data, geopolitical tensions, and regulatory shifts. For example, when the Federal Reserve adjusts interest rates, liquidity conditions change across global markets, and risk assets including cryptocurrencies respond accordingly. Yet popular crypto data platforms like CoinGecko and CoinMarketCap primarily display price and volume data without quantifying macroeconomic impact. I was motivated to build a system that bridges this gap one that not only tracks crypto prices but also interprets how macro forces probabilistically influence digital assets across different time horizons. What it does Stratify AI analyzes how macroeconomic forces influence a cryptocurrency by calculating a probability score across short term, medium term, and long term horizons. Instead of providing a simple up or down prediction, the system evaluates multiple normalized influence factors including volatility sensitivity, liquidity depth, regulatory exposure, interest rate impact, and geopolitical risk, and combines them with recent market momentum. Each influence factor is assigned a weight based on its relative importance. The final probability is calculated by applying a sigmoid transformation to the sum of each influence factor score multiplied by its corresponding weight, plus the time horizon momentum adjustment. In simple mathematical terms, the probability equals the sigmoid function of the weighted influence factor scores plus the momentum adjustment. The sigmoid function ensures that the output always remains between 0 and 1. This structured approach allows the platform to generate a probabilistic directional outlook instead of a rigid price prediction, helping users understand expected bias within a macroeconomic context. How we built it I built Stratify AI as a full stack intelligent system combining macroeconomic data, cryptocurrency market statistics, and AI driven explanations. On the backend, I used FastAPI (Python) to orchestrate data from multiple sources, including Federal Reserve Economic Data for macro indicators such as the Fed Funds Rate and CPI inflation, and CoinGecko for real time cryptocurrency metrics. I implemented JWT based authentication with bcrypt hashing to ensure secure access. The scoring engine was modularized into separate services for macro data processing, sentiment normalization, and probability computation, ensuring maintainability and scalability. On the frontend, I developed a modern interface using React 18 with Vite, incorporating glassmorphism UI elements and animated SVG probability gauges to visually communicate risk and opportunity. For the AI explanation layer, I integrated Ollama with a locally hosted LLM (llama3.1:8b), allowing the system to generate narrative explanations for each probability score without relying on expensive cloud APIs. This decision significantly reduced operational costs while maintaining privacy and control over the inference process. Finally, I implemented PDF report generation to produce professional summaries containing macro context, probability breakdowns, and AI generated insights, making the platform suitable for academic, research, and portfolio applications. Challenges we ran into One of the biggest challenges was converting abstract macroeconomic concepts into measurable computational signals. Variables such as geopolitical risk and regulatory exposure are inherently qualitative, requiring proxy metrics like sentiment analysis and weighted jurisdiction scoring. Designing a fair weighting mechanism for the multi-factor model required iterative experimentation to prevent overfitting to short-term momentum. Another significant challenge was multi-horizon alignment. Short-term market momentum often contradicts long-term macro trends, so we had to design a system that differentiates between immediate reactions and structural adoption dynamics. Additionally, optimizing local LLM inference for consistent and context-aware narrative generation required careful prompt engineering and system resource management. Accomplishments that we're proud of We are particularly proud of achieving zero cloud AI costs while maintaining full AI explainability through local inference. The integration of macroeconomic indicators with crypto probability modeling is rarely implemented in retail accessible platforms. The system not only calculates probabilities but also provides transparent breakdowns of influence factors and generates professional downloadable PDF reports suitable for research and portfolio reviews. Most importantly, Stratify AI moves beyond price tracking and delivers contextual intelligence. What we learned Building Stratify AI taught us that financial markets operate on probabilities, not certainties. We learned how deeply interconnected macroeconomics and digital assets are, and how to translate economic theory into computational models. From a technical perspective, we gained experience in full-stack architecture design, API orchestration, AI integration, secure authentication, and probabilistic modeling. The project reinforced the importance of transparency in AI systems and demonstrated that cost-efficient innovation is possible with thoughtful infrastructure choices. What's next for Stratify Ai The next phase of Stratify AI focuses on improving data depth, predictive calibration, and institutional readiness. With external funding or strategic support, we plan to integrate premium financial data providers and enterprise grade news intelligence APIs to enhance macro sentiment accuracy. Currently, the system relies on open source and limited access news sources, which restrict coverage breadth and historical depth. By upgrading to high quality financial news feeds with richer metadata, real time policy transcripts, and structured economic commentary, we can significantly improve geopolitical and regulatory risk modeling. This would allow the scoring engine to operate on more comprehensive datasets, reducing noise and increasing predictive reliability. Additionally, we aim to introduce dynamic weight optimization through machine learning backtesting, expand macro indicators to include global central banks and employment data, and implement portfolio level scenario simulations. With proper funding, Stratify AI can evolve from a powerful prototype into a highly accurate, institution-ready macro intelligence platform for digital assets. <div