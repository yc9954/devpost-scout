---
slug: "xpanse"
url: "https://devpost.com/software/xpanse"
title: "Xpanse"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 381
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "user/educator_student"
---

# Xpanse

> The Yield Optimizer

[Devpost](https://devpost.com/software/xpanse) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[agriculture_food]] [[developer_tools]]
**user** [[educator_student]]

**stack** near, react, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- what's next for xpanse

## Body

Inspiration We are currently two members. Roti: Started the journey into web3 through the NEAR Metabuild Hackathon. It contained several beginner friendly challenges. Coco: He has experience in building dapps on solidity, He has written yield optimization strategies on ethereum. After hours of discussion and research, the team decided to work on Auto-compounding challenge from REF Finance. The challenge was interesting to work on with a lot of future potential. Also being an avid stock trader this seemed most relatable ( because of AMM ). What it does It optmizes the yield for a ref finance farm using auto-compounding strategy. How we built it We used rust and react to build it. Challenges we ran into Working on and implementing Cross-Contract Calls was difficult. Asking questions on Discord server came in handy when we were stuck on a callback issue. We saw a lot of 'Exceeded the Prepaid Gas' Error. To tackle this we had to divide the code into several steps. For example, The complete harvesting process consists of 5 steps i.e. 5 Cron calls. What we learned Learn and Build was our slogan throughout the journey. Not being familiar with NEAR concepts a lot of research was needed. Plan was to spend some time on the NEAR Docs, go through the Excellent tutorials there and then the SDK Docs. For the building Phase, We decided to first work on Harvesting code. The complete harvesting process was divided into several steps: Claiming Rewards from the farm. Withdrawing them to Near wallet. Deposit Back to Ref. Swapping Rewards for Pool Tokens. Adding Liquidity Staking the new seeds into Farms Next we worked on User Deposit and Withdraws Funds Code. Correctly deciding the states for contract was the crucial step here. Next came making a UI for the Contract. Not being familiar with the UI frameworks, this was challenging but with the help of stackoverflow and the official docs this task was also conqured. Accomplishments that we're proud of We wrote our first auto-compounding strategy for yield optmization Made a basic UI for this What's next for Xpanse We will be adding more strategies, the next will be using harvested rewards in some other pool which high APR than the current one. And then we will try to improve and optimize. <div