---
slug: "trajaudit"
url: "https://devpost.com/software/trajaudit"
title: "TrajAudit"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 263
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "domain/finance_payments"
---

# TrajAudit

> Detects adversarial conversational agents via behavioral trajectories — not single messages.

[Devpost](https://devpost.com/software/trajaudit) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[accessibility]] [[finance_payments]]

**stack** geminiapi, plotly, python, streamlit

## How they structured the write-up

- what inspired this
- the core insight
- what we built
- results
- what we learned
- challenges

## Body

Benign conversation scores 0.04 — zero false positives Job scam detected at Turn 7 — SUSPICIOUS score 0.70 Crypto scam — SCAM DETECTED at Turn 5, score 0.99. TrajAudit catches it 3 turns before single-turn baseline. What Inspired This I spent 6 months observing real deployed scam bots on Snapchat. Every existing tool failed — not because the tools were bad, but because the adversarial signal genuinely isn't present in early turns. The bots looked completely normal until it was too late. The Core Insight A system that detects only after exploitation begins is not a safety system — it is a logging system. Standard monitors evaluate one message at a time. Adversarial agents distribute their intent across many turns. This gap is Detection Latency — an architectural property, not a calibration failure. What We Built TrajAudit accumulates evidence across the full conversation: $$score(t) = score(t-1) + s \cdot (1 - 0.3c)$$ Four behavioral phases detected in sequence: 🟢 RAPPORT — normal social interaction 🟡 EXTRACTION — curiosity, flattery 🟠 CAPTURE — authority, urgency, redirect 🔴 CONVERSION — payment, wallet, subscription Results Blind Gemini monitor evaluated 13 conversations at two context lengths. Adversarial conversations: NORMAL at turns 1-5, SUSPICIOUS at full trajectory. Zero false positives on benign controls. What We Learned The intervention window problem is real and measurable. Monitor confidence and victim psychological investment both rise as conversation progresses. These curves cross before detection kicks in. Challenges Building a scoring engine that compounds signals without saturating early — the decay factor (0.3c) was critical to preserving trajectory sensitivity across long conversations. <div