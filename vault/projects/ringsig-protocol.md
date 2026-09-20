---
slug: "ringsig-protocol"
url: "https://devpost.com/software/ringsig-protocol"
title: "Ringsig Protocol"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 402
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
  - "substrate/financial_record"
---

# Ringsig Protocol

> A Decentralized, Regulated Solution for Supervised Privacy Transaction

[Devpost](https://devpost.com/software/ringsig-protocol) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[revocation_withdrawal]]
**domain** [[civic_government]]
**substrate** [[financial_record]]

**stack** etherscanapi, hardhat, javascript, python, react, solidity, tencentcloud

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ringsig protocol

## Body

FlowChart RingSig chainlink.ccip front-end chainlink.functions Inspiration Seeking anonymity is not solely the domain of criminals or individuals with things to conceal. When we witness instances like Tornado.cash being banned by multiple governments due to an influx of illicit funds, it is disheartening because technology itself is not inherently malicious. Therefore, we aim to create a privacy computing protocol that combines regulatory compliance with privacy. Simultaneously, we strive to reduce the hardware requirements and costs for users. What it does RingSig Protocol: A privacy transaction protocol where users make deposits using one address and can withdraw funds using another entirely unrelated address, proven through ring signature mechanisms. Supervision Contract: After funds enter the supervision contract, anyone can report a deposit address associated with a blacklist address through Chainlink Functions. If the verification is successful, the reported address will be set as a blacklist address, preventing illicit funds from entering the main protocol. Cost-efficient Withdrawals: To save costs, a relayer on the Polygon chain assists in withdrawals and synchronizes information with the mainnet through Chainlink CCIP. The mainnet protocol then transfers funds to the designated address included in the ring signature proof. How we built it The main body of the RingSig Protocol consists of multiple smart contracts. RingSig Protocol uses ring signature technology to achieve privacy computation through a Python program. We use Chainlink Functions to achieve automated reporting verification in the supervision contract. We place proof verification calculations on Layer 2, where the actual funds exist on Layer 1, using Chainlink CCIP to achieve data synchronization between the two chains. Challenges we ran into Chainlink Functions' HTTP - Maximum queries limit, solved by sending multiple small requests iteratively. Team collaboration can be challenging when there is a 13-hour time difference among some members. But in the end, we successfully completed the project. Accomplishments that we're proud of Chainlink Functions and Chainlink CCIP seamlessly integrate with our project. Our demo runs smoothly and comprehensively. What we learned New Chainlink technology stacks usage. Good spirit of teamwork. Other skills like using AI dubbing and video editing. What's next for Ringsig Protocol Add logic for reporting success rewards and reporting failure penalties to the protocol. Currently, the origin blacklist is manually set by us, but in the future, we plan to obtain blacklist data from a third-party security company and automatically add it to the blacklist pool in the supervision contract. User community governance. <div