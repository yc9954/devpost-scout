---
slug: "a-vckqad"
url: "https://devpost.com/software/a-vckqad"
title: "Pindex"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 331
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
---

# Pindex

> Agentic Index funds for Polymarket. You bet on anything, Pindex bets on everything.

[Devpost](https://devpost.com/software/a-vckqad) · hackathon [[NexHacks]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]

**stack** arize-phoenix, framer-motion, hono, nextjs, openai, polymarket, react, tailwind, typescript, wxt

## How they structured the write-up

- 🧐 inspiration
- 🤯 what it does
- 👷‍♂️ how we built it

## Body

Technical Diagram Arize Phoenix Script Tracing Arize Phoenix Dashboard 🧐 Inspiration They say bet on anything... why not bet on everything? Strategically, of course. Think traditional investing. People usually put most of their money into index funds like the S&P 500. Why not bring index funds to Polymarket? That's exactly what Pindex does. It's a chrome extension to optimize investments. 🤯 What it does Pindex lets anyone create agentic index funds that automatically diversify risk across related prediction markets. 💭 How it works: First you choose a bet Let's say you want to bet YES on "Lebron James will win the NBA Finals." Our AI finds related markets The agent searches Polymarket for markets that could affect your bet's outcome, such as: "LeBron will score 25+ points per game" "Lakers will make the playoffs" "Lakers will not get knocked out by the Nuggets" Our AI logic layer labels relationships Each related market is tagged with how it connects to your original bet: IMPLIES - If this happens, your bet is more likely to win CONTRADICTS - This would hurt your bet's chances CORRELATED - These tend to move together PARTITION_OF - These outcomes split up all the possibilities (must sum to 100%) SUBEVENT - Your bet is a specific case of this broader event CONDITIONED_ON - This must happen first for your bet to be possible Diversify your position Instead of putting all your money on the Finals bet, spread it across related markets. For example: 60% on LeBron winning Finals 25% on LeBron scoring 25+ PPG 10% on Lakers making playoffs 5% on Lakers not getting injured This way, even if LeBron's team doesn't win the championship, you might still profit from his individual performance or the team making playoffs. Small wins > complete losses, let's make some big money 🤑🤑🤑 👷‍♂️ How we built it Frontend: WXT for chrome extension React Tailwind CSS Framer Motion TypeScript Backend: Hono TypeScript Polymarket API OpenAI API Arize Phoenix (observability layer) Docker <div