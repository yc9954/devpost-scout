---
slug: "decentralized-kameti"
url: "https://devpost.com/software/decentralized-kameti"
title: "Decentralized Kameti"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 392
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Decentralized Kameti

> Leveraging Chainlink Oracle networks crypto verified decent data & Polygon ID for secure identity verification on/off-chain to provide a Decentralized way for millions to protect their life savings!

[Devpost](https://devpost.com/software/decentralized-kameti) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[finance_payments]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** chainlink, hardhat, polygon, polygonid, solidity, vrf

## How they structured the write-up

- inspiration
- accomplishments that we're proud of
- what we learned
- what's next for decentralized kameti

## Body

Inspiration We wanted to build something in the Social Impact category. We interviewd some locals to get a better idea of pain points that "Blockchain tech, Chainlink & Polygon" can solve while being user-friendly. What is (Decentralized) Kameti? We came across a problem thats a very common cause of People losing their life-savings to fraudsters and lack of paperwork & trust, knows as KAMETI's in Asia or more generally ROSCA(Rotating Savings And Credit Association). In simple words, a group of people agree to save collectively and an organizer chooses a person (in a so-called random process writing names on paper pieces and picking one from them) every month who access the whole pool for that month. So, 5 people with 100$ monthly payment means 500$ pool every month. So, everyone gets access to a big amount randomly. There are other types of these kind's of savings that our dapp's code can support with just a little bit changing for each. Problems: We pin-pointed some of the most crucial problems in this process that everyone involved face Trust Issues (more specifically organizer favors people in the selection process) => Solved using Chainlink VRF Identity Issues (in case someone defaults, we don't have their right ID) => Solved using Polygon ID Transaction Records => Solved using IPFS storage & Polygon's native ledger (no one can manipulate or delete) Technologies: Using Chainlink (Eliminate Trust Issues) => Getting a random number from chainlink VRF to select the winner Using PolygonID (Eliminate Identity issues) We can't upload People's ID directly on the chain, thanksfully Polygon ID allows us to issue zk-claims (by getting their ID details off-chain and saving cryptographically) to people that they can later use for authentication on smart contracts & our other services. Using Polygon (Eliminate Transaction Records issue) Uploading all the event data & Transaction details on the Polygon Network. We get an immutable ledger that no one can manipulate or delete like physical ledgers. Accomplishments that we're proud of Haven't slept for 2 days XD, this hackathon revived my underlying reason for programming. To build something cool and helpful to people What we learned Learned some really mind-blowing work people are doing to eliminate trust in third parties and authority. What's next for Decentralized Kameti Want to create a complete working product with other types of saving schemes like installments etc <div