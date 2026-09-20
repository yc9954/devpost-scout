---
slug: "marketmind-b6cy2q"
url: "https://devpost.com/software/marketmind-b6cy2q"
title: "MarketMind"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 463
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "substrate/sensor_telemetry"
---

# MarketMind

> Real-time stock market visualization application with AI-powered agent analysis.

[Devpost](https://devpost.com/software/marketmind-b6cy2q) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[disaster_emergency]] [[finance_payments]]
**substrate** [[sensor_telemetry]]

**stack** elasticagentbuilder, elasticsearch, lava, next.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for marketmind

## Body

Home View Stock View Inspiration Modern (novice) traders are flooded with fragmented, fast-moving information (price action, fundamentals, news/sentiment, and options/volatility) and lack a single, interpretable surface that converts these streams into trustworthy, real-time signals. Making fast, data-driven trading decisions becomes guesswork rather than insight. We wanted to bring order to that chaos by giving traders a clear and interpretable view of market energy in one place. What it does MarketMind turns raw market data into simple, real-time visual signals. Six agents, each built with Elastic Agent Builder, analyze a different layer of the market: price movement, company fundamentals, news sentiment, volatility, etc. Their combined outputs appear as glowing pulses around each stock, showing whether momentum is building, risk is rising, or sentiment is shifting. How we built it We built 6 agents connected to Elasticsearch, each reading from multiple indices and returning standardized JSON results. Every agent computes its own metrics, scoring, and reasoning before sending its output back to the MarketMind client. The frontend was built with React 19 and Next.js 16, using TypeScript, SVG physics-based visuals, and Chart.js for live candlestick charts. Yahoo Finance provided real-time data, while the app’s animation engine created the smooth pulsing and orbiting interactions that make the experience feel alive. Challenges we ran into ESQL was powerful but strict, and small syntax differences broke queries. Aligning timestamps across datasets and keeping data fresh without overwhelming performance required multiple iterations. The hardest part was keeping every agent’s logic explainable while still running fast enough for real-time feedback. Accomplishments that we're proud of We successfully integrated real trading analysis techniques inside a fully explainable multi-agent system. The Oracle Network computes Technical Analysis indicators such as RSI, Bollinger Bands, and MACD to assess short-term price momentum. The Arbitrage Hunter applies Fundamental Analysis metrics including P/E Ratio and Beta to detect valuation imbalances. The Volatility Prophet uses Portfolio Optimization with Risk-Adjusted Allocation concepts like Modern Portfolio Theory and the Black-Litterman Model to contextualize volatility regimes. Bringing all of these together in one live system that is both interpretable and reactive is a major achievement. What we learned We learned that modularity and explainability are essential for both trust and performance. By designing each agent as an independent analytical node with clear responsibilities, we reduced complexity while improving interpretability. We also discovered how visual design can make complex market models not only accessible but intuitive, helping users “see” patterns they might otherwise miss. What's next for MarketMind Our next goal is to use realtime data sources to injest into Elasticsearch. This will provide better data to the agents which will result in better responses. We also aim to implement a user chat interface. This user agent will communicate with the Elastic agents using the A2A protocol to provide a response. <div