---
slug: "255labs-xyz-entry"
url: "https://devpost.com/software/255labs-xyz-entry"
title: "SmartPool.near"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 642
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/vision_ocr"
  - "substrate/geospatial"
---

# SmartPool.near

> SmartPool.near democratizes AI investing. Pool your capital, let NEAR-powered AI manage funds, and enjoy quick liquidity. Empower everyone to benefit from a user-owned AI investment revolution.

[Devpost](https://devpost.com/software/255labs-xyz-entry) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[vision_ocr]]
  <sub>weak: revocation_withdrawal</sub>
**substrate** [[geospatial]]

**stack** docker, javascript, near, nearai, nextjs, node.js, postgresql, python, react, rust

## How they structured the write-up

- inspiration
- what it does
- how we built smartpool.near
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smartpool.near

## Body

Smartpools are liquidity pools that are AI managed. They have delayed settlement for withdrawal and deposit as well as a looping agent. The levels of ai agent autonomy. The smartpool abstraction scales with capability level. The four components we built and how they interact. All open source at github.com/255BITS/smartpool.near Our landing page Pool details after it has purchased and sold some of a prediction market position "GPT-5 not announced in 2024?" You can see a full breakdown of the user-owned NEAR AI's reasoning and predictions. It also gives a recommended action. The nearai prediction market assistant can be used outside of smartpools to provide assistance with polymarkets and NEAR AI. Not our product, this is the polymarket prediction market our AI is tracking in the demo. Inspiration The inspiration for SmartPool.near came from our mission at 255labs.xyz, to help people adapt to the AI age. We see AI powered businesses and funds exceeding human capabilities in the future, and we want to help people participate in the enormous value this can create. Traditional businesses and funds: Lack transparency Suffer from lack of liquidity Do not leverage AI at their core We see a future a rapid rise of AI-driven businesses and we want anyone to be able to participate. What it does SmartPool.near lets anyone create or participate in AI-managed investment pools. Our first implementation focuses on prediction markets: Core features: Users can deposit/withdraw from pools using NEAR Each pool mints SP tokens representing ownership share AI analyzes opportunities repeatedly using NEAR.AI Smart contracts handle all token operations and pool management Platform tracks pool performance For example: User deposits NEAR into "Sports Prediction Pool" Smart contract mints corresponding SP tokens AI researches and executes predictions in the market continuously User can withdraw anytime Oracle handles closing positions and distributes earnings Each SmartPool has its own SP token, strategy, and AI agent while sharing the same underlying infrastructure. This creates a framework that can support various AI-driven investment strategies. How We Built SmartPool.near It's at https://github.com/255bits/smartpool.near We built SmartPool.near using: Rust smart contracts on NEAR Next.js frontend with postgres backend Oracle in python NEAR AI agent in python Deployment with terraform, docker, docker-swarm Challenges we ran into Several significant challenges emerged during development: AI Integration Complexity Ensuring reliable AI analysis within time constraints. The prompting specifically took a while to get to a reliable state. Smart Contract Architecture The smart contract deploying another smart contract was difficult to piece together and we initially went down other routes. System Design Figuring out where the cut points are for a complex system like this. Vision Understanding what a liquid ai-agent led business could accomplish now and in the future. Creating 'levels' of ai capability for smartpools helped us to narrow on what could be accomplished for the hackathon. Accomplishments that we're proud of Smart contract factory system for multiple pools Reliable AI prompting for prediction markets Full NEP-141/145 token implementation Scalable architecture for future AI capabilities What We Learned We learned a lot building SmartPool.near, including: Advanced rust smart contract development on NEAR. Our 'controller' smart contracts deploys 'pool' smart contracts. The limits of current AI by asking it to complete complex tasks that crossed systems NEP-141 token implementation, NEP-145 implementation NEARAI intricacies How prediction markets work What's next for SmartPool.near We believe SmartPool.near represents a crucial piece of infrastructure for democratizing AI-powered investments, making the benefits of AI automation accessible to everyone. We think SmartPool.near can be a viable alternative to current top down organizations. Long term, by having AI lead development and liquidity efforts we believe this can change how common infrastructure and services work at a fundamental level. We want to continue building SmartPool.near to prepare for stronger AI agents while adding new forms of pools. We want to deploy to mainnet for when level 1 (expert level) agents are available. <div