---
slug: "intear-oracle"
url: "https://devpost.com/software/intear-oracle"
title: "Intear Oracle"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 375
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Intear Oracle

> Fully permissionless and decentralized oracle marketplace

[Devpost](https://devpost.com/software/intear-oracle) · hackathon [[-REDACTED- Hackathon]]

## Facets

**domain** [[developer_tools]] [[scientific_research]]
**substrate** [[financial_record]] [[web_dom]]

**stack** inindexer, near-sdk-rs, rust

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what we learned
- what's next for intear oracle

## Body

Inspiration ShillGPT was my biggest inspiration for this. I knew that yielded execution is going to be released soon, and the moment it was released on testnet, I made this oracle, it wasn't even in docs, I just used the PR that added it to the sdk to play around with it, but disregarded as something that no one needs. But now I see an increased demand in such oracles, so decided to revive this project What it does It's a decentralized and permission oracle marketplace that allows anyone to register "oracles" or use someone else's oracles. Oracle operators run indexers that look for transactions that request data and submit the data, so that the caller receives the result within the same transaction, like a normal promise. And as a marketplace, it has fees, users have fee balances, can deposit to per-producer fee balances, and producers can issue fee refunds, or a full refund is issued if the data was not delivered. Can be useful for on-chain AI dapps or dapps that use chain abstraction and need to get back the execution result, balances, or just anything from any data source. How I built it I used Intear's indexing stack to help write indexers, and recently migrated them to the new near-api-rs crate to send responses back to the chain. Challenges I ran into There were lots of challenges: Unstable SDK which was not compatible with FT implementations, which delayed the implementation of fungible token fees. And it's still not implemented! But you can use NEAR which is enough for most oracles OpenAI's seed parameter only works with short responses, and because of lack of reproducibility, an oracle that uses Reclaim Protocol to verify OpenAI responses has very limited use It's too expensive to submit large amounts of data, but https://github.com/near/nearcore/pull/12192 will fix this when it lands on mainnet Accomplishments that we're proud of 3 oracles are already running on mainnet dev-unaudited-v0.oracle.intear.near and more on the way! What we learned Using cutting edge tech is fun What's next for Intear Oracle FT fees More oracles: IPFS upload / download, arweave, get data from an arbitrary url, code execution sandbox Decentralized permissionless cross-chain oracles that use light clients Hopefully an audit and a real launch <div