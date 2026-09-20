---
slug: "the-accuracy-trap"
url: "https://devpost.com/software/the-accuracy-trap"
title: "The Accuracy Trap"
hackathon: "ZerveHack"
organization: "Zerve AI"
winner: true
words: 376
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/disaster_emergency"
  - "domain/scientific_research"
---

# The Accuracy Trap

> Retail-flooded prediction markets are 10.97× less accurate than sophisticated ones. I proved it across 4,714 markets and built a live detector that flags it in real time.

[Devpost](https://devpost.com/software/the-accuracy-trap) · hackathon [[ZerveHack]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[disaster_emergency]] [[scientific_research]]

**stack** aws-lambda, fastapi, manifold-markets-api, pandas, polymarket-api, python, scipy, streamlit, wikipedia-pageviews-api, zerve

## How they structured the write-up

- what inspired this
- what i found
- how i built it
- challenges
- what i learned

## Body

Real Case Studies: 50% Error vs 0.5% Error, Same Event Live Topic Classifier: GME Retail Flood Detection Polymarket Live Alerts: Real-Money Markets at Risk OLS Regression Proof: It's Composition, Not Attention Real Examples Tab: The Most Compelling Cases From Real Data Calibration Plot: When the Market Says X%, What Actually Happens? The Accuracy Trap: Hero Dashboard What Inspired This Two Manifold markets, same question, same day, will Trump win the 2024 election. One at 50%. One at 99.5%. That shouldn't be possible. I wanted to understand what was causing that gap. What I Found The signal is one number: average bet size. $$\text{avg_bet} = \frac{\text{total volume}}{\text{unique bettors}}$$ Someone putting in 2,000 Mana has probably researched. Someone putting in 20 is betting on vibes. Across 4,714 resolved binary markets from Manifold: Market Type Calibration Error Median Avg Bet Micro-bet (Retail flood) 22.3% 52 Mana Whale-bet (Sophisticated) 2.0% 720 Mana That's a 10.97× accuracy gap : p < 0.001, Cohen's d = 1.256. The obvious objection: viral topics are just harder to predict. I controlled for this with OLS regression. Holding crowd size constant, avg_bet still predicts accuracy at p < 0.001. It's composition, not topic difficulty. How I Built It Full pipeline in a Zerve notebook : fetch, compute, test, reproducible. Live tool is a FastAPI backend on AWS Lambda + Streamlit dashboard : case studies, calibration curves, OLS proof, a market classifier, and live Polymarket alerts scored by social momentum. Validated on real money: 299 Polymarket markets, $116.9M USDC, same pattern holds. Challenges Ruling out the confounder : showing a gap isn't enough, I had to prove it survives controlling for attention. The obvious alternative explanation is that viral topics are just harder to predict, not that the traders are worse. Getting the OLS setup right to cleanly isolate composition from crowd size took several iterations. Live data reliability : Polymarket and Google Trends APIs go down randomly. Built a fallback chain so the app never breaks: Google Trends → Wikipedia Pageviews → neutral score. Without this the live alerts tab would fail silently half the time. What I Learned Calibration error isn't random, it's traceable to a single upstream variable. When avg_bet is low and attention is high, the market is lying to you. <div