---
slug: "cofre-rwgb37"
url: "https://devpost.com/software/cofre-rwgb37"
title: "Cofre"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 600
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# Cofre

> The safest place in Solana for peer-to-peer NFT swaps.

[Devpost](https://devpost.com/software/cofre-rwgb37) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** anchor, metaplex, react, rust, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cofre

## Body

Landing page My NFTs Start an NFT swap Lock your NFT to initialize swap of Cofre #30 for Cofre #26 NFT locked and swap ready to be shared NFT swap from the counter's party perspective Swap has been successful, now counter party owns Cofre #30 You can also sell your NFTs here NFT swap and sale marketplace Inspiration The name "Cofre" in Portuguese/Spanish: A safe and resistant box to store valuable objects. Air Protocol - An awesome peer-to-peer exchange protocol, which we will bring to Solana land. Existing NFT marketplaces - Solanart, OpenSea, Rarible Degen Ape Academy Discord and the awesome #want-to-trade - Identified the need for a safe place to swap NFTs with other people. What it does Cofre is the first peer-to-peer NFT swap platform. A need I've seen firsthand in many discord groups. This particular use case is just a single proof-of-concept behind the more general idea of a highly configurable escrow program. Under the hood, Cofre allows to safely trade assets with several mechanics and configurations. To avoid having to trust in the other party to fulfill the other end of the deal, and to be able to trade any asset with any asset. It is published as an open-source program, and a wrapper client is generated using Anchor, in order to provide its functionality to any program or dApp needing to safely escrow things. How we built it Solana Program: Rust, Anchor, Vipers. Front End: Using Typescript, React, Chakra UI. Anchor RPC client for the Solana program Metaplex JS SDK to easily access Metaplex Metadata Goki's WalletKit + Saber's use-solana for wallet management Candy Machine RPC client Solana Web3.js A lot of this was built while streaming on the Anchor/Rust Study Group discord. Which was incredibly fun. Challenges we ran into Validating whether an NFT is authentic or not. Which we will work on showing that soon before launching to mainnet. Working on this by myself on nights and weekends, while being a full time CTO of a company and managing a team of engineers. Accomplishments that we're proud of Launching the first NFT peer-to-peer trading platform, to allow people to swap amongst each other without risking their precious NFTs. More importantly: Understanding and building the foundational block of what Cofre will unlock in the future: off-chain to on-chain things (more below) "This is dope! UI is so clean as well. Never imagined I would have so much fun minting devnet NFTs hahaha" "The UI here is lit." What we learned Solana's runtime, programming, and data model. It is so fascinating and will definitely keep building, and contributing things here. Learning Rust and Typescript. It was tough, but so much fun, and definitely worth it. What's next for Cofre As a general rule: Listen to the community to build and polish functionality In the short term: 1) Deploy on Mainnet 2) Add a mechanism for people to submit Counter Offers in order to ease the process of trading 3) Improve search on the Marketplace 4) Support escrowing multiple NFTs, to swap a group of NFTs for another group of NFTs, or trade them for SOL or any SPL token. In the medium/long term: Cofre is meant to be a solid and highly configurable escrow for the whole Solana platform. And by adding multisig release with a dispute resolution network, unlocks a use case I am most excited about, which will tackle a billion-dollar market: to enable off-chain to on-chain trades. So in short terms, this will unlock peer-to-peer trades such as Buying an NFT with a Venmo transaction Selling SOL for a wire transfer <div