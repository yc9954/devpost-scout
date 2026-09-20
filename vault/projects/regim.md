---
slug: "regim"
url: "https://devpost.com/software/regim"
title: "Regim"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 415
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/scientific_research"
  - "domain/security_privacy"
---

# Regim

> A Market Microstructure & Optimal Execution Research System

[Devpost](https://devpost.com/software/regim) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[scientific_research]] [[security_privacy]]
  <sub>weak: transportation</sub>
  <sub>weak: web_dom</sub>

**stack** css, fastapi, fredapi, hmmlearn, html, next.js, python, railway, shap, typescript, vercel, yfinance

## How they structured the write-up

- the problem
- what it does
- how i built it
- challenges
- what i learned
- what's next

## Body

landing page about page findings page findings page contact page live regime tab live regime tab live regime tab live regime tab live regime tab backtest tab backtest tab paper vs reality comparision tab intraday simulation statistical sumary paper trading The Problem This system operationalizes a finding from my research paper on the CTMSTOU optimal execution framework: RL agents trained with PPO fail to reliably exploit regime information even when it's explicitly in their state space, sometimes inverting regime sensitivity entirely. Hard-coded regime conditioning bypasses the optimization problem that policy gradient methods can't solve reliably, this dashboard proves it works on real market data. What it does Regim is a quantitative finance research platform that detects market regimes using machine learning and studies whether those signals can improve trade execution. It classifies any of 8 assets into one of four states, crash, bearish, transitional, or bullish, in real time, then tests whether acting on those signals beats standard execution baselines, and rigorously identifies the conditions under which they fail. How I built it The core is a 4-state Gaussian Hidden Markov Model fitted on price-volume features, with BIC covariance selection run across 40 random seeds per asset. The backend extends this with regime-conditional GARCH volatility forecasting, Bayesian changepoint detection via the PELT algorithm, SHAP explainability on HMM posteriors, and FRED macroeconomic attribution. Validation uses three simultaneous hypothesis tests, paired t-test, 1000-iteration permutation test, and binomial test, with Bonferroni correction. The frontend is a 7-tab Next.js dashboard with live regime classification, walk-forward backtesting, cross-asset comparison, intraday simulation, and a full statistics view. Challenges Separating crash from bearish required a volatility-based disambiguation step on top of the HMM return scores, they look similar in return space but require completely different execution. Ensuring zero look-ahead bias in the walk-forward backtest with a one-day signal lag was critical for any result to be credible. Getting SHAP to work on HMM posterior probabilities rather than a standard classifier took a custom KernelExplainer setup. What I learned Knowing when not to use a model is as important as building it. About 23% of trading days fall in low-confidence transition zones where the regime signal has no statistical edge, filtering those out and falling back to TWAP actually lifts overall performance. The model flagging its own uncertainty is itself a useful signal. What's next Companion paper forthcoming on SSRN, Temporal Aggregation Reveals HMM Regime Uncertainty Signals in Optimal Trade Execution, extending the cross-asset analysis to 8 assets and 5 evaluation horizons. <div