---
slug: "troves-fi-ai"
url: "https://devpost.com/software/troves-fi-ai"
title: "Troves.fi AI"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 292
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Troves.fi AI

> LLM Powered chatbot for Troves.fi that runs on telegram and whatsapp

[Devpost](https://devpost.com/software/troves-fi-ai) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[researcher]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** node.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for troves.fi ai

## Body

Inspiration DeFi can feel overwhelming; diving into vault contracts, figuring out yields, or picking a strategy often seems like trying to crack a secret code. We wanted to simplify on-chain financial literacy, so we built an AI that anyone can chat with to get the lowdown on how Troves operates behind the scenes. That's why we created Troves.fi AI, a friendly Telegram assistant that guides users through the Troves ecosystem, helps them grasp yield strategies, and lets them check out contract data all in natural language What it does Troves.fi AI is a read-only, LLM-powered Telegram bot built for the Troves.fi ecosystem. It allows users to: Chat naturally to learn about Troves, vaults, and how yield strategies work. Fetch real-time contract data like TVL, APY, or vault composition. Explain strategies in plain language (e.g., “What does Trove ETH Vault do?”). Stay updated on the latest Troves vaults, metrics, and yield stats — all via Telegram. It’s like having a DeFi analyst + Troves documentation assistant in your chat. How we built it We built it using the Telegram Bot API with Node.js and TypeScript, connected it to a Claude MCP trained on Troves.fi documentation and contract data, and used Starknet.js to read on-chain vault information. All responses are cached for speed, and the bot is strictly read-only with no wallet or transaction access. Challenges we ran into Teaching the LLM how to interpret Troves contract functions correctly Accomplishments that we're proud of Built the first AI knowledge bot fully dedicated to Troves.fi on Starknet. What we learned How to turn DeFi smart contracts into human-readable explanations What's next for Troves.fi AI Add voice-based DeFi explanations (“Explain Troves ETH Vault in 30 seconds”). Implement ability to invest in yield strategies via telegram <div