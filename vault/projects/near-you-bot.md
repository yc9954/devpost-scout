---
slug: "near-you-bot"
url: "https://devpost.com/software/near-you-bot"
title: "Near you BOT"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 254
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Near you BOT

> ask about any transaction, NFT, analysis or anything at all!!

[Devpost](https://devpost.com/software/near-you-bot) · hackathon [[-REDACTED- Hackathon]]

## Facets

**substrate** [[financial_record]] [[structured_db]]

**stack** fastly, near, node.js

## How they structured the write-up

- inspiration and what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for near you bot

## Body

Inspiration and what it does the barrier to entry is quite high for new users to blockchain technology. In order to solve that, I created a telegram and discord AI bot the answers users questions about any smart contract, transactions, acounts, NFTs, trend analysis, etc. How we built it We used LLM to parse user's questions and convert it to bigQuery SQL command that is then ran on the near bigQuery public dataset, the result is sent back to the LLM which interprets the table and explains it for the user to understand. Challenges we ran into Initially, it was challenging to get the LLM to produce a correct SQL command that aligns with the user's interest, but we were able to fine tune the system prompt and thankfully, near already has the schema and definitions, so we copied that and inserted it into the system prompt Accomplishments that we're proud of We were able to create bot telegram and discord bots that works wonderfully well!! What's next for Near you BOT Creating a twitter bot Performing transactions directly from telegram and discord via the AI bot. ## Applicable Tracks Near native track: The bot works exclusively with the near blockchain ZettaBlock | AI/Web3 Bounty: As per requirement, we built an AI and web3 bot that converts users question to query, executes it and returns an explained result in english language. Questflow | AI Agents Bounty: The project aligns with the requirement of building an AI agent that performs actions based on intent. <div