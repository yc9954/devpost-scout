---
slug: "starkflow"
url: "https://devpost.com/software/starkflow"
title: "StarkFlow"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 384
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
---

# StarkFlow

> StarkFlow — Automate Starknet. Visually. Effortlessly with 0 lines of code

[Devpost](https://devpost.com/software/starkflow) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** nextjs, sncast, snfoundry

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for starkflow

## Body

banner landing workflow sample Inspiration We were inspired by how no-code tools like Zapier and Buildspace automate complex workflows off-chain. We wanted to bring that same power to the Starknet ecosystem—where anyone, regardless of coding background, can visually create, deploy, and automate on-chain actions like minting NFTs, deploying tokens, or running AI-generated contracts. What it does StarkFlow is a drag-and-drop automation builder for Starknet. It allows users to create complete on-chain workflows—from deploying and minting contracts to performing swaps or batch payments—without writing a single line of code. Each block represents a Starknet action, and connecting them builds a fully executable flow that can be deployed instantly. How we built it We built the frontend using Next.js and React Flow for the visual builder. The backend is powered by Python and Starknet_py for contract deployment and transaction execution. Scarb and sncast are integrated for on-chain compilation and deployment. We also included AI-powered blocks that can generate Cairo smart contracts dynamically, letting users create custom logic using natural language prompts. Challenges we ran into The main challenge was managing the complexity of Starknet tooling integration, especially with asynchronous deployments and fee estimation. Designing a flexible flow engine that could translate visual nodes into real Starknet transactions also took several iterations. Another challenge was ensuring composability across different contract templates while keeping execution deterministic. Accomplishments that we're proud of We built a working prototype that can visually design and deploy ERC-20 and NFT contracts, execute swaps using Atomiq, and perform batch payments through Chipi Pay. The seamless integration of AI-generated contract logic into the flow was a major milestone, making StarkFlow a powerful tool for both developers and non-developers. What we learned We learned how to orchestrate Starknet tooling in a user-friendly environment and the importance of modular contract design. Integrating AI into smart contract workflows taught us how natural language can accelerate blockchain development. Most importantly, we discovered how automation can simplify complex on-chain processes without compromising transparency or control. What's next for StarkFlow Next, we plan to introduce a flow marketplace where users can share and reuse StarkFlow templates. We’re also adding on-chain scheduling for automated recurring executions, and expanding beyond Starknet to include other L2 networks. Long term, our goal is to make StarkFlow the go-to automation layer for decentralized, AI-driven applications. <div