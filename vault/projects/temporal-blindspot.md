---
slug: "temporal-blindspot"
url: "https://devpost.com/software/temporal-blindspot"
title: "Temporal Blindspot"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 339
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/financial_record"
---

# Temporal Blindspot

> Paste any AI response. We extract every factual claim, score how outdated it probably is, and show you exactly which facts time has made unreliable. Before you act on them.

[Devpost](https://devpost.com/software/temporal-blindspot) · hackathon [[Frostbyte Hackathon]]

## Facets

**substrate** [[financial_record]]

**stack** fastapi, groq, next.js, playfair-display, python, sentence-transformers, tavily-api

## How they structured the write-up

- what is this
- how it works
- what i learned
- what's not finished

## Body

landing_page demonstration claim_analysis What is this AI models have a training cutoff. Everything they know is frozen at a point in time. But when you read an AI-generated response, there's no warning label on which facts are probably still accurate and which ones time has quietly invalidated. So I built a tool that audits AI responses claim by claim. Paste any AI-generated text and it breaks the response into individual factual statements, classifies each one by domain, retrieves current web evidence, and scores staleness using a decay-weighted similarity model. The key idea: not all facts age at the same rate. A claim about Bitcoin's market cap is likely wrong within weeks. A claim about the speed of light is never wrong. The scoring model accounts for this via a velocity config that assigns each domain a decay rate. High-velocity domain plus low evidence similarity equals stale. Low-velocity domain plus low evidence similarity might just be obscure, not outdated. How it works Claim extraction via Groq (Llama-3) breaks the input into atomic factual statements Each claim gets classified into one of 9 domains (AI/ML, crypto, politics, medicine, finance, technology, science, geography, history) Tavily retrieves 3 current web sources per claim TF-IDF cosine similarity scores each claim against the retrieved evidence snippets Final staleness score combines similarity with domain velocity What I learned Claim extraction is harder than it looks. LLMs tend to merge related facts into one claim or split a single fact into three. Getting clean, atomic claims required a lot of prompt iteration. The velocity scores are hand-tuned. I'd want real data on how fast different domains actually change if I were building this properly. What's not finished The training cutoff selector in the UI doesn't affect scoring yet. It's wired up in the frontend but the backend ignores it. The idea was to shift the velocity penalty curve based on the model's cutoff date so a GPT-4 claim about "recent AI developments" gets penalized more than the same claim from a model with a later cutoff. <div