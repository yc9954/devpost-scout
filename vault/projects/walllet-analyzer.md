---
slug: "walllet-analyzer"
url: "https://devpost.com/software/walllet-analyzer"
title: "Walllet Analyzer"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 308
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Walllet Analyzer

> Identify trending tokens and top holders of near-protocols, analyze transaction activity, and quickly use interactive AI to inform your trading strategy. This works with the Bitte.AI plugin.

[Devpost](https://devpost.com/software/walllet-analyzer) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[document_pdf]] [[financial_record]] [[sensor_telemetry]]

**stack** bitte.ai, nextjs, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for walllet analyzer

## Body

Inspiration The rise in DeFi and blockchain-based trading inspired us to create Wallet Analyzer, a tool aimed at filling the gap in comprehensive wallet and token analytics on the NEAR blockchain. By incorporating AI insights, we make real-time analysis and data-driven decision-making accessible to traders seeking a competitive edge. What it does Wallet Analyzer is designed to scan wallets and provide detailed metrics to help traders monitor and analyze trading activity on the NEAR blockchain. Key functionalities include: Trending Tokens Analysis: Lists top trending tokens based on trading volume and recent spikes. Top Wallet Holders: Identifies top holders of trending tokens, providing insights into significant wallet activity. Usage toptoken: “What’s top trending tokens?” - Retrieves a list of the top trending tokens. search: “Give me the info about sweat” - Provides specific information about a given token. topholders: “Analyze top holders for sweat” - Analyzes and displays the top holders of a specific token. activity: “Analyze account activity for hodl-lockup.sweat” - Provides insights into an account’s activity and historical data. get-txn: “Give me txinfo about 3CT2mXeRDREv78qYoGvZoJGUB8iGU6rPKu5tctc9CsMf” - Retrieves detailed information for a specified transaction. How we built it Data Collection: Used NEAR block’s APIs and DEXscreener to gather real-time wallet and token data. AI Integration: Implemented Bitte.AI for pattern recognition and predictive analysis. Deployment: ㅍercel Challenges we ran into There were several blockers for building with bitte.ai because of lack of documents. Accomplishments that we're proud of We talked to the community and successfully deployed it on bitte.ai. What we learned AI in Trading Tools: Learned the importance of balancing statistical rigor and real-time processing for predictive analysis. What's next for Walllet Analyzer Multi-Chain Compatibility: Expanding support to popular chains like Ethereum and Solana. Enhanced Predictive Models: Implementing machine learning to improve token trend predictions. Portfolio Management Integration: Adding tools for tracking and managing portfolios across blockchains. <div