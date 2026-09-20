---
slug: "betvex-ai-agent"
url: "https://devpost.com/software/betvex-ai-agent"
title: "betVEX AI Agent"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 484
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# betVEX AI Agent

> In a world where you can't find the link to betVEX, interact with the betVEX ecosystem via a chat assistant. Bet on the next CSGO game. Who has the 4th most winnings? Copy the most successful bet.

[Devpost](https://devpost.com/software/betvex-ai-agent) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**substrate** [[financial_record]] [[web_dom]]

**stack** bitte, typescript

## How they structured the write-up

- problems statement:
- solution:
- what we built:
- going forward:
- scope

## Body

We are building betVEX. Which is a community-powered esports betting platform, While you can interact with it via the website I also wanted to whip up an AI agent to interact with the betVEX ecosystem. Problems statement: It is difficult to carry out niche tasks quickly. All user interfaces are fragmented. Solution: AI Agents! One can define some arbitrary task specific they want to carry out and the agent can call multiple functions to get you to that endpoint. We can plug our agent into the universal interface that NEAR AI and Bitte Protocol are creating to make our application more discoverable and increase the number of users. What we built: We built an AI agent with Bitte (chose Bitte over NEAR AI because I think it offers a more intuitive framework that makes it easy to get something up pretty quickly). We defined a lot of functions that allow you to do some pretty interesting complex prompts: "Make a dollar bet on the next match Shopify Rebellion play" "For every bet where I made over $10 add up the winnings and send them to charity.testnet" "Make a bet of two and a half dollars on the last game that the person at the top of the leaderboard bet on" "Send the person on the bottom of the leaderboard 100 VEX Rewards because I feel sorry for them" "Claim all bets over $5" "Tell me how much I've won betting on teams that start with the letter W" List of basic actions. Ask for basic information about betVEX. Show account balance, USDC, VEX, and staked VEX. Send USDC and VEX to users (register the receiver in the token account via a relayer if not already registered). Swap between USDC and VEX, you can swap by an input amount or by an output amount (register them in the output token account via a relayer if not already registered). Stake and Unstake VEX. Fetch the leaderboard of bettors by winnings or number of wins. Bet on matches. View matches by different filters. View bets by different filters. Claim a user's bets. Abstracted nomenclature, displays in terms of $ instead of USDC, use owen instead of owen.users.betvex.testnet Going forward: I didn't get as much done here as I wanted to. Next, I am going to: Implement the chat component into our website. Be able to pass either a wallet or social login signer into the chat component, if social login then transactions will be sent via relayer. Abstract the interface so it doesn't give details of gas amount or talk about transactions, also remove the part where it's calling tools. Be able to interact with the agent via speech, and it speaks back to you. Be able to make completely non-custodial bets by replying to a twitter post of a market Scope The agent was only added in this hackathon, everything else was pre-existing (contract, indexer) <div