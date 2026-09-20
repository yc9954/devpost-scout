---
slug: "starkyield-shuttle"
url: "https://devpost.com/software/starkyield-shuttle"
title: "StarkYield Shuttle"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 850
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# StarkYield Shuttle

> The simplest way for Bitcoiners to earn DeFi yield on Starknet — one click, one button, one flow.

[Devpost](https://devpost.com/software/starkyield-shuttle) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**domain** [[agriculture_food]] [[developer_tools]]
**substrate** [[financial_record]]

**stack** atomiq, cairo, express.js, node.js, starknet-js, starknetkit, tailwind, typescript, vesu, xverse

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for starkyield shuttle

## Body

Inspiration Most BTC sits idle; moving it to DeFi is a multi‑step, high‑friction process. Stark Yield Shuttle is a “one‑click” "one flow" app that accepts native BTC (L1 or Lightning), bridges to Starknet, and deploys into a yield protocol automatically. The DeFi landscape is fragmented.Most BTC sits idle; moving it to DeFi is a multi‑step, high‑friction process. While Layer 2 solutions like Starknet offer incredible scalability with fees that are a fraction of Ethereum's, accessing them remains a significant barrier for the average user. The process is complex and capital-intensive with issues like:- Multi-Step Complexity : Users must bridge assets (a scary process for many), then swap for the right tokens, then navigate unfamiliar Starknet dApps, and finally manage their positions. Prohibitive Gas Costs : The initial bridging and setup on Ethereum can cost $50-$100,most of the swaps tools are also fragmented in different sites and with different wallets, making small-scale yield farming uneconomical. Strategy Diligence : Identifying and auditing safe, high-yield opportunities on a new chain is time-consuming and risky. This complexity creates a paradox: the very technology designed to make DeFi accessible (L2s) is itself inaccessible for passive capital. What it does Stark Yield Shuttle is a decentralized finance (DeFi) 'highway' that seamlessly connects the Bitcoin & other L1/L2 evm tokens & LSTs with the Starknet Layer 2 ecosystem, specifically for yield farming. Instead of dealing with complex and expensive bridges, users can easily connect their BTC and starknet wallets using Xverse and deposit assets like BTC/wBTC and stablecoins with a single click and swaps with Atomiq. The protocol automatically deploys them into the highest-yielding opportunities on Starknet using Vesu. It's a one-stop-shop for passive yield, supercharged by Starknet's low fees and high speed We abstract away the entire technical process, offering users a familiar, simple, and efficient experience: One-Click Deposit: Users deposit ETH or USDC on Ethereum. That's it. Automated Shuttle & Strategy : Our smart contracts handle the rest: Secure Bridging : Assets are trustlessly bridged to Starknet via underlying bridge protocols. Optimal Yield Allocation : Capital is automatically deployed into a curated basket of the highest-yielding strategies on leading Starknet protocols (like lending markets and DEXs). Auto-Compounding : Yields are automatically harvested and reinvested to maximize compound returns. Starknet-Benefitted : All complex transactions (swaps, deposits, compounding) occur on Starknet, leveraging its low fees and high throughput, making the strategy efficient even for small depositors. How we built it Wallet Management: Users connect their wallets using Xverse and Starknet wallets (argent & Bravoos) with easy on-boarding for users which is a need Deposit: Users deposit BTC, ETH, Stark tokens or stablecoins on both Starknet & Bitcoin with bridge intents and wallet signings. Shuttle & Compound: Our protocol securely bridges assets to Starknet through Atomiq with reverse bridging Earn: Users earn compounded yield in the native asset, all while benefiting from Starknet's ultra-low transaction fees.The tokens are automatically allocated to top-tier, audited lending protocols and AMMs through Vesu. Stop bridging manually. Start earning passively. The future of cross-chain yield is here. Challenges we ran into Solving a Real Pain Point: It directly addresses the user experience and cost barriers of cross-chain DeFi in two different chains at once where as we are used to do projects independently. Clearing Value Prop: "Deposit on BTC, earn yield on Starknet" is an easy-to-understand narrative in an abstracted UI. Timely & Cheap transaction fees: As Starknet grows, the need for easy onboarding tools like this will explode trusting them and learning on how to leverage the tools into one was not a walk in the park but we pulled it off Creating a Scalable Business Model: The protocol could eventually earn a performance fee on the yield generated, creating a sustainable revenue model. Accomplishments that we're proud of For the User (The Passive Earner): Simplicity: Users having No need to understand bridging or navigate Starknet dApps. Accessibility: Being to dramatically lowers the capital barrier to entry for Starknet yield. Efficiency: Ensuring Automated compounding maximizes returns without manual effort. Cost-Effective: Being able to Leverage low L2 fees for all active management. For the Starknet Ecosystem (The Growth Engine): Liquidity Magnet: To manage an one flow that attracts significant, passive TVL from Bitcoin directly into Starknet DeFi primitives. User Onboarding: Serving as a primary onboarding ramp, bringing new users into the ecosystem who would otherwise be deterred by complexity. Protocol Partnerships: Creating a symbiotic relationships with leading Starknet dApps by directing a steady stream of capital their way through the use of the APIs , SDKs & Pools What we learned Stark Yield Shuttle as an essential piece of infrastructure, not just another DeFi app. What's next for StarkYield Shuttle Stark Yield Shuttle aims to become the default savings account for the Starknet & Bitcoin ecosystem. We are not just a bridge; we are a yield aggregation layer and a capital router. Our long-term vision is to create a suite of automated, risk-managed vaults that cater to various risk appetites, making sophisticated DeFi strategies accessible to everyone. In essence, we are building the foundational layer for passive capital in the StarkBTC economy <div