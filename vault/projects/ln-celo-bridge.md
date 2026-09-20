---
slug: "ln-celo-bridge"
url: "https://devpost.com/software/ln-celo-bridge"
title: "LN - CELO Bridge"
hackathon: "Celo's Make Crypto Mobile Hackathon"
organization: "Celo"
winner: true
words: 387
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# LN - CELO Bridge

> LN-CELO Bridge connects Celo and Bitcoin on Lightning Network to onboard millions within seconds in a trustless way with submarine swaps.

[Devpost](https://devpost.com/software/ln-celo-bridge) · hackathon [[Celo-s Make Crypto Mobile Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[general_public]]
**substrate** [[code_repository]] [[financial_record]]

**stack** celo, lightning-network, node.js, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ln - celo bridge

## Body

Inspiration Every new blockchain have the standard chicken/egg problem consumer apps have. Onboarding people to the network to experience them is hard. People can use KYC exchanges or custodial bridges. We have a better way. What it does LN - CELO Bridge allows users to swap their Bitcoin to CELO within seconds in a completely trustless way. It utilizes submarine swaps and it requires no accounts. The swap is atomic, the swap operator locks funds into a contract on CELO and the user can only claim the CELO if they pay a Lightning invoice to reveal the preimage of the LN invoice. Both LN to CELO and CELO to LN swaps are supported and user interacts with the contract with a user-friendly frontend. How we built it We forked the boltz open-source codebase, which operates this submarine swap exchange between Bitcoin and other EVM chains and adapted it to work with CELO. Challenges we ran into Even though there are similarities, there were still some challenges specific to CELO. We also introduced several new data sources to aggregate and properly serve CELO/Bitcoin conversion rate. Currently user needs to have an injected web3 provider (metamask) or wallet connect compatible mobile wallet. Ideally in the future we'd like to integrate with a wallet and offer these swaps directly on user's device with even faster UX. Accomplishments that we're proud of Swap works and overall provides a very nice UX to complete swaps! Of course it can be improved with new wallet providers or even an additional feature to onboard accounts with zero initial CELO. Currently the user needs to have a small amount of CELO to call the claim contract call. We really believe this bridge provides great interoperability to CELO, improves liquidity and ties it to the strongest network with its millions of onboarded users. What we learned CELO is very easy to work with and get started, many tools are available to build with and documentation is straight-forward. What's next for LN - CELO Bridge We hope to continue working on this after the hackathon and bring it to mainnet. We also want to think about new and innovative ways to ensure liquidity on both LN and CELO is consistent and able to meet demand. These are all very exciting challenges we look forward to tackle, <div