---
slug: "acai-gup0bm"
url: "https://devpost.com/software/acai-gup0bm"
title: "Acai"
hackathon: "Bitcoin 2025 Official Hackathon"
organization: "Bitcoin++"
winner: true
words: 437
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# Acai

> the first RBF-resistant WASM smart contract on Bitcoin L1

[Devpost](https://devpost.com/software/acai-gup0bm) · hackathon [[Bitcoin 2025 Official Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** alkanes, fartane.com, metashrew, oyl-sdk, rust, rust-bitcoin, shield, wasm

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for acai

## Body

Inspiration The Acai contract was inspired by a recurring issue in Bitcoin-based minting systems — frontrunning and RBF (Replace-by-Fee) attacks, especially in open public mempools. Existing solutions often require fully private infrastructure or custom transaction types. I wanted to explore a new design space: can we discourage public mempools economically instead of technically forbidding them? The project also builds on the vision of making Bitcoin's L1 more programmable via WASM smart contracts — particularly in the Alkanes ecosystem. What it does Acai is a RBF-resistant smart contract for minting tokens on Bitcoin L1 using Alkanes WASM. It introduces two key protections: Economic discouragement of public mempool use: Minting through a public mempool has only a 14–20% chance of success, while using Rebar Shield ensures 100%. Coinbase miner tag validation: The contract parses the coinbase transaction's scriptSig to ensure the block was mined by a Rebar partner. It also includes creator enforcement logic : minting is only valid if a portion of the output is paid to the contract creator — ensuring economic alignment and sustainability. How we built it The project was built as a modification of the open-source free-mint WASM smart contract provided by Alkanes. The changes included: Extending validation logic to parse the scriptSig of the coinbase input Implementing a list of approved miner tags Adding a rule that checks for required output to the creator’s address Deploying and testing the logic via the fartane.com interface The tooling used included Rust, the Alkanes SDK, and test deployments via Rebar-connected mining pools. Challenges we ran into Lack of standardization in coinbase scriptSig : Miner tags are arbitrary, variable, and often obfuscated. Testing against real blocks: Verifying miner tags against actual Rebar-partnered blocks required manual inspection and iteration. Accomplishments that we're proud of First fully functioning MEV-resistant WASM smart contract on Bitcoin L1 Successfully processed over 317 mint transactions through Rebar Shield On-chain enforcement of creator compensation without breaking standard Bitcoin rules Proof-of-concept that a contract can reshape mempool dynamics What we learned Bitcoin’s coinbase structure can be leveraged for protocol logic without soft forks or consensus changes WASM on Bitcoin via Alkanes opens the door to a whole new class of programmable interactions Economic alignment (e.g., incentivizing use of Rebar) can be more powerful than hard restrictions What's next for Acai Generalizing the validation pattern for other sensitive operations beyond minting — including auctions, lending triggers, and fair token distributions Proposing a standard format for miner tags in coinbase scriptSig to simplify future contract validations Optimizing for fuel cost and expanding developer tooling Potentially integrating with other dApps on Alkanes that need trust-minimized transaction ordering <div