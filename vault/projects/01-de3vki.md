---
slug: "01-de3vki"
url: "https://devpost.com/software/01-de3vki"
title: "01"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 463
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# 01

> 01 is a fully decentralized, cross-collateralized, and cross-margined derivatives protocol, offering the first implementation of everlasting options on Solana.

[Devpost](https://devpost.com/software/01-de3vki) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**domain** [[developer_tools]]

**stack** anchor, react, rust, solana, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned
- what's next for 01
- join us

## Body

the power of centralized exchanges, decentralized Inspiration When thinking about what can be uniquely built on Solana, that leverages its full scalability and potential, it was clear that we had to build everlastings and decentralized derivatives. From a tech side, protocols on other chains must sacrifice part of their design due to on-chain limitations either through the use of a centralized orderbook (such as dYdX), or through the use of vAMMs to go around the orderbook computational limits. After working closely with the Serum team, it was clear to us that derivatives could finally be fully decentralized on Solana. And thanks to Pyth's high fidelity price feed oracles, this means that every infrastructure component of the stack is entirely decentralized. From a product side, it was clear to us that Solana’s throughput and Serum's matching engine makes the perfect combination to experiment with novel financial instruments. We’ve been excited about the potential of everlastings, since the paper was first published, and are excited to have the opportunity and community support to push it into reality. What it does A fully decentralized derivatives protocol and the first to offer on-chain orderbook-based everlasting options. Everlasting options are options that never expire (similar perpetual futures). They use an elegant funding formula of mark - payout to mimic a basket of options that constantly roll-over. 10x leverage across markets Cross-collateral up to 50 pairs Cross-margin across 100 markets How we built it We started venturing into Solana by first building out a fully working LMSR-based binary options market on devnet, in 1 week. This gave us the knowledge and learnings to move on to what is currently 01. We were also fortunate enough to have chatted with the Serum team, with who we are working closely today. Anchor and the dev discord communities have also been constant game changers when it comes to debugging. And alas, a few *caffeinated all-nighters later, and here we are. What we learned The community is key. We wouldn't be here without them. The feedback we get through discord, and the gm trains is what keeps us going. This is why we believe in the decentralized future, because the community clearly cares and contributes actively. What's next for 01 From a product side, there are many innovative ideas we are incredibly excited to experiment with once the core primitives are built, such as composable derivatives. We’re also already talking with a few protocols to potentially integrate with and compose with. From a community side, the goal is to become fully decentralized. Shortly after our mainnet launch, we want to formalize our governance model. We’re already seeing many members being actively involved in some of the design decisions we are making, and we can’t wait to formalize it. Join us @01_protocol discord.gg/01protocol <div