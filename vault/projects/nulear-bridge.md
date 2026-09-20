---
slug: "nulear-bridge"
url: "https://devpost.com/software/nulear-bridge"
title: "Nuclear Bridge"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 400
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/security_privacy"
  - "substrate/financial_record"
---

# Nuclear Bridge

> A censorship proof decentralized protocol providing peer-to-peer atomic bridges.

[Devpost](https://devpost.com/software/nulear-bridge) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[security_privacy]]
**substrate** [[financial_record]]

**stack** solidity, tailwind, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nulear bridge

## Body

Inspiration We first had the idea for a peer-to-peer bridge by seeing the multiple recent security breaches on bridges. All bridges today have to rely on an offchain third party to allow both chains to communicate. Those third party can be compromised. What it does Our bridge matches two people wanting to bridge the same asset between two different chains. Each agent has to lock his funds on his chain and after making an on-chain request and accepting the other agent's request, they can withdraw the other agent's funds. Right now, it works with signatures and keccak hashes so it allows bridging ERC-20 token on any EVM-compatible chain. This is the only bridge we know of that need only the two blockchains and nothing else. How we built it We started by defining the steps and the transactions that had to be sent for the bridge to work. Then, we wrote the specifications of the contract and the content of each transaction. We tried to attack the contract in mutliple ways and ended up with the current structure of 6 transactions in total, 3 by each user. We believe it is not possible to reduce this number without adding any third party. We then started implementing a user-friendly front-end and connecting it to the smart contract. Challenges we ran into The hardest part was to design a safe protocol that only allows a user to withdraw funds if the other user has consented to bridge. We had to work with signatures and locking periods to ensure this process is secure. We also had to implemented nonces for each lock and requests to avoid replay attacks. Accomplishments that we're proud of We are proud to have produced a working PoC and the beginning of a user interface. To test, we deployed on Gnosis, Cronos, Celo and Polygon testnets. What we learned We think the main thing we learned while working on Nuclear Bridge is to implement a project quickly and iterate fast. We also strengthened our Solidity skills. What's next for Nulear Bridge We are proud of the idea and we want to continue working on it, but we think we need a significant breakthrough on the user experience side to make it simpler. The main drawback of our implementation is the number of steps, but we think we can make it simple enough to create a seemless bridge experience. <div