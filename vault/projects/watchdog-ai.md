---
slug: "watchdog-ai"
url: "https://devpost.com/software/watchdog-ai"
title: "WatchDog AI"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 739
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# WatchDog AI

> Anti-Rug AI agent for memecoins by frontrunning + sandwich attacks. Longer version: - Memecoin risk evaluator - Auto trade bot - Stops hard and soft rug by removing financial incentives

[Devpost](https://devpost.com/software/watchdog-ai) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** python, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- technicals
- potential future steps
- closing/what can watchdog potentially do

## Body

Simulated DEX builts Built trader side profile Simulated mempool to listen to Example of AI agent risk assessment Another example Trader executing auto trade Agent detecting malicious trade to frontrun Agent operating autotrade against "type 1" attack against liquidity removal Inspiration Crypto AI - especially AI agents - has been a hot topic within the industry with many players trying to identify new ways to incorporate AI agents into their builds. However, it seems that the most promising fits are still within that of memecoins - another hot topic this cycle. Memecoins are fun. But rugs are not. Yet, it seems like there is no way to stop rugs from happening since it is financially advantageous to do so... or is there? ps another inspiration is the web3 track "prompt" to use AI agents + AVS to do something crazy So why is this crazy. Because this essentially is a way for a person to do good, make money and stop memecoin rugs at the same time. You get to make money of the rugger (be it hard rug - liquidity removal or soft rug - sell offs). In this project, we align fun, profitability and security. What it does WatchDog AI in its essence is a memecoin anti-rugger, solving the problem by removing the financial incentives. The AI agent is designed to sit on top of a potential AVS, obtaining information from 1) DEX to analyse the riskiness and the possibility of rugs, 2) mempools for transactions and 3) operates as an MEV trading bot. 1) Memecoin evaluator The AI agent itself possesses the ability to evaluate the potential of future rugs based on past transactions and other data about the memecoin. It provides an evaluation on a risk scale. If the memecoin is deemed to be "risky" WatchDog AI would start listening to the mempool for potential malicious rugs. 2) Mempool listener WatchDog taps into the mempools of coins to identify suspicious transactions in real time. It could be able to detect rug attempts and react instantly by sacrificing gas fees to frontrun the rug attempt. 3) MEV attack Autotrader Identifying the rug attempt (for instance a large sell off), the agent could decide to frontrun the transaction with a large short and buy back after the the rug attempt has taken place. (Or even worse, find a way to obtain a flash loan to create a further leverage on the trade. ) This would greatly reduce the monetary gains of rugger. Else if the rugger attempts to remove liquidity, the bot could remove liquidity ahead of the rugger such that there are insufficient liquidity for the rugger to remove resulting in their loss before adding liquidity back into the pool. Technicals To implement this project the following were developped, A simulated DEX, A risk evaluating AI agent A mempool listener A frontrunning + sandwich attack trading bot. The latter few kind of combines to become a simulated AVS/can be easily moved on top of an AVS. The following demo will be conducted on a simulated DEX (since repeatedly rug testing a real dex would probably not be wise). As such, the technicals of the price mechanisms and all (simple) transaction modes were built out from scratch together with the associated mempool (bootstrap version). The AI agent is able to analyse the coin based on robust data and autonomously make trading decisions to profit and stop rugs. This part is the more fun part and probably the part that really steps out of current boundaries. For the functional demo refer to the media attached. Potential Future Steps This project framework can be deployed in an on-chain environment to become a fully verifiable trustless AI. A potential framework could be DEX -> dexscreener, AI agent -> WatchDog, AVS -> Eigen AVS, transactions -> Flashbots Closing/What can WatchDog potentially Do WatchDog AI is a real-time, trust-minimized DeFi security solution that uses AI agents detect malicious transactions. It directly addresses the 40%+ of crypto scams that come from rug pulls and malicious contract actions by preemptively intercepting them in the mempool. By leveraging frontrun and sandwich attacks, it proactively rescues user funds instead of merely labeling risky tokens. Unlike profit-driven MEV bots, WatchDog AI focuses on protecting users and recovering stolen funds, thereby establishing a new standard for real-time, trust-minimized security and greatly reducing rug pulls and malicious contract scams in DeFi—making rug pulls a thing of the past. <div