---
slug: "chainrand-io-provable-random-distribution-computation"
url: "https://devpost.com/software/chainrand-io-provable-random-distribution-computation"
title: "Chainrand.io - Chainlink VRF anywhere without limits"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 455
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "user/researcher"
---

# Chainrand.io - Chainlink VRF anywhere without limits

> Multiple fields suffer from a major problem of RNG manipulation (P-Hacking). With Chainrand, we enable Chainlink VRF to be easily used anywhere to prevent cherry-picking (even in off-chain code).

[Devpost](https://devpost.com/software/chainrand-io-provable-random-distribution-computation) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]] [[researcher]]

**stack** alchemyapi, c++, chainlink, css, filecoin, go-ethereum, golang, javascript, polygon, python, rust, solidity, web3-stoage

## How they structured the write-up

- inspiration
- why it matters
- what it does
- how we built it

## Body

Chainrand Logo Chainrand as a Chainlink VRF service Cross-Industry Problem of Probability Manipulation Chainrand as a VRF hybrid solution How Chainrand works Verifying projects using Chainrand Hackathon deliverables completed Hackathon prizes applied for Chainrand future development roadmap Inspiration Random number generators (RNG) are widely used across multiple fields. However, they lack a verifiable process, making them vulnerable to manipulation and abuse. Multiple fields including academia, investment backtesting, and NFT generative art suffer from this same problem. This results in the loss of funds from failed promises, and in some cases a scam on investors. We were particularly challenged by NFT generative art projects that claimed to be "fair" launch but in reality skewed in favour of the original developers to get more rare NFT art pieces. A similar problem occurs in Casino-like protocols that claim to be "fairly run" but by choice of seed for a random generator, able to skew results in favour of the house. Why it matters With Chainrand, we have now enabled the wider community with a fair and transparent manner for creating probability related projects on the blockchain. This will help encourage people to trust projects and help users verify that indeed the random number generation has not been tampered with. This will also allow for different industries (investment backtesting, academic research of simulations) to adopt Chainlink more readily as with Chainrand it can solve these cross-industry problems of P-hacking and RNG manipulation. What it does Leveraging VRF, we introduce a new service standard to cryptographically generate fair probability distributions used for any probability experiment without cherry-picking. This allows any user without a background in solidity or smart contracts to verifiably generate an unlimited array of random numbers over a chosen probability distribution that can help with their own projects - without cherry-picking. Chainrand uses Chainlink VRF to be the best of both worlds: Efficiency and flexibility of off-chain RNG computations (Compute with common programming languages like Python & JavaScript) Seeded with the verifiable fairness of on-chain Chainlink VRF How we built it We introduce the Chainrand NFT Smart Contract deployed in Polygon's Mumbai Testnet. For ease of adoption, we have provided deterministic cryptographically-secure RNG software development kits (SDKs) in C++, Python, JavaScript. Developers can now do heavy stochastic computations off-chain with the SDKs, and tie their code to Chainrand in an immutable manner, demonstrating that the random numbers are generated in a fair manner. As a demo, we also developed a NFT generative art project that uses Chainrand as a source of verifiable randomness that is seeded by Chainlink VRF. We also created a DAPP frontend at https://chainrand.io for easy interaction with the Chainrand smart contract, so that that anyone can verify the integrity of projects using Chainrand. <div