---
slug: "friktion-bma7v8"
url: "https://devpost.com/software/friktion-bma7v8"
title: "Friktion"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 494
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
---

# Friktion

> First Structured Products Protocol on Solana

[Devpost](https://devpost.com/software/friktion-bma7v8) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]

**stack** anchor, javascript, python, react, rust, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- learnings and accomplishmnets
- what's next for friktion

## Body

Inspiration DeFi across chains lacks a robust risk or portfolio management solution, which we believe the next generation of users will certainly require in order to onboard into the ecosystem. As a team that has worked across various quant research and trading roles, we are excited to develop a solution for this, leveraging our backgrounds and the growing derivatives markets on Solana. What it does Friktion introduces an Automated Portfolio Manager (APM) into the DeFi ecosystem, offering both active and passive strategies. The APM provides a set of profit opportunities for a User with or without existing portfolio, finding ways to maximize return on while providing volatility protection and yields in turbulent markets. Volts, our native investment products allow anyone to access to products built with principal protection, yield generation, and volatility in mind. Our v1 is built on top of PsyOptions' devnet! How we built it Our v1 is built on top of PsyOptions, the leading Solana options protocol on Mainnet, which is built on the Serum Orderbook. Challenges we ran into Technical: Anchor, Serum not dev friendly Computational limits inside of a single instruction maximum 1 serum order to a permissioned market byte size limits on context buffer for an instruction max ~38 accounts. need accounts for CPI calls as well, so they can add up quickly. obscure program errors from the solana VM. Common in blockchain development, but there's some particularly nasty ones Matching client-side to on-chain values. Really tricky and can lead to frustrating errors seed generation (must match exactly or receive obscure error) CPI-specific seeds as well, since need to know what seeds that call expects very useful to understand the intent of an instruction, as authority can be inferred Serum integration permissioned markets brand new, on-chain trading extremely verbose requiring unexpected accounts for a placeorder instruction. e.g OpenOrders, wrapped sol balance. Writing hyper accurate code withdrawal u64 multiplication & overflow Market: Searching for a meaningfully liquid options market showed us how nascent Solana is in terms of utilizing it's inherent advantages. This led to the design of the Volt Smart Router, which creates a way to optimize for price (as a function of size and market impact) into every on-chain options exchange (CLOB/OMM) as well as provided the inspiration for designing our off-chain market maker integration. DAOs are fairly risk insensitive to the assets they own, largely given the stage of development on Solana, meaning a key part of the Friktion's offering should address the need for DAO risk and treasury management Learnings and accomplishmnets Getting familiar with Anchor and using it to translate our trading logic into deployable code on DevNet which trades on PsyOptions through Serum's orderbook; CPIs and PDAs Market and trading logic: Building the most computationally efficient What's next for Friktion Opening up a public DevNet for our active Volts shortly Roll out first three volts on Mainnet by the end of the year! Partnering with DAOs to bring Volts to their protocols <div