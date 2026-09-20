---
slug: "tradegist"
url: "https://devpost.com/software/tradegist"
title: "Tradegist"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 711
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/supply_logistics"
---

# Tradegist

> Advanced trading (trader) behaviour analysis

[Devpost](https://devpost.com/software/tradegist) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[supply_logistics]]
  <sub>weak: structured_db</sub>

**stack** data, langchai, llm, ml, openai, python, react, typescript

## Body

Tradegist NO SOUND IN THE VIDEO FOR SOME TECHNICAL ERROR. PLEASE READ BELOW! Inspiration There’s no shortage of trading bots that predict the market, tell you how to trade or simple journaling platforms. They are focused on the market. But almost none of them answer from a trader's perspective.: why do traders behave the way they do? What triggers overconfidence after a win, or revenge trading after a loss? What hidden tendencies shape their decisions, and ultimately their success or failure? Trading is as much about psychology as it is about numbers. Many traders know what strategies to follow, but still fall into emotional traps like revenge trading, overtrading, or inconsistent risk-taking. The inspiration behind Tradegist was to build a system that doesn’t just track P&L, but actively analyzes behavioral tendencies through a mix of heuristics, machine learning, and AI — giving traders a mirror into their decision-making. What it Does Tradegist ingests raw trade history and reconstructs round trips. It then runs the trades through a multi-layered behavioral analytics pipeline : Heuristics catch obvious signals (e.g., too many trades in a day, rapid re-entry after a loss). Logistic Regression statistically scores tendencies like overtrading or loss-chasing, based on features such as trade frequency, size escalation, and recovery attempts. LLaMA classifier provides sequence-level analysis, interpreting runs of trades as behavioral narratives to detect advanced patterns like loss spirals or tilt escalation. RAG-powered AI coaching (Claude + OpenAI) pulls in trade history, behavior scores, and past insights to generate personalized reflections, making the tool feel like a coach rather than just a dashboard. How I Built It Backend (Python + FastAPI) : Handles ingestion, feature engineering, and analysis. Uploaded CSVs are normalized, deduplicated, and processed into round trips. Behavioral Pipeline : Heuristics Layer : Rule-based checks for clear triggers (revenge trades, overtrading, averaging down). Logistic Regression : A probabilistic model that weighs features and outputs confidence scores for each behavior. LLaMA : A lightweight model to classify sequences of trades, capturing context and progression of trader psychology. Database (Supabase/Postgres) : Stores both raw trades and derived behavioral signals in a schema designed for clean relational integrity and easy extension. Frontend (React) : Surfaces insights, summaries, and context-aware reflections in an interactive UI. AI Coaching Layer : Uses embeddings and RAG to retrieve relevant trades and scores, then generates grounded feedback via Claude and OpenAI APIs. Advanced Behavioral Analysis Going deeper than just rule flags, we combined models to detect subtle trader psychology: Loss Escalation Spirals : Identifying when traders double down multiple times after losses. Premature Profit Taking : Spotting consistent exits too early compared to risk setup. Ticker Bias : Highlighting when traders are disciplined on one symbol but force trades on another. Discipline Recovery : Tracking whether traders resist the urge to re-enter after losses. By layering heuristics, statistical models, and LLMs, we created a system that not only detects bias but explains it in context — turning analytics into self-awareness. Challenges Designing a schema that could support both raw trades and behavioral scores. Avoiding duplicate ingestion when syncing CSVs into Supabase. Tuning the AI coach to sound reflective and context-aware instead of generic. Balancing scope in a hackathon: deciding what to prioritize versus what to leave for future work. Accomplishments Proud Of Built a full ingestion → analysis → AI coaching pipeline within hackathon time. Detected and surfaced complex behavioral biases like revenge trading and tilt. Integrated AI into the feedback loop, making the product feel like a personalized coach. Designed a modular backend + schema that can easily scale to real-world broker data. What We Learned Behavioral data often reveals more than raw P&L in predicting long-term success. Schema design and indexing early saves massive pain later when layering analytics. AI prompts and grounding are key to producing useful, trader-aware coaching. Hackathon projects work best when you build end-to-end flow , not just isolated optimizations. What’s Next for Tradegist Broker API integrations for live trade ingestion. Richer behavioral tags (volatility-adjusted risk, session-level mood tracking). Deeper AI coach memory across multiple trading sessions. Mobile app support for in-the-moment coaching. 👉 Tradegist turns raw trades into behavioral insights — blending rules, ML, and AI into a coach that helps traders see not just what they did, but why . <div