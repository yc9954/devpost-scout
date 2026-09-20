---
slug: "improving-blood-transfusion-supply-chains-with-nfts"
url: "https://devpost.com/software/improving-blood-transfusion-supply-chains-with-nfts"
title: "Improving Blood Transfusion Supply Chains with NFTs"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 399
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/patient_family"
---

# Improving Blood Transfusion Supply Chains with NFTs

> Non-Fungible Tokens (NFTs) that act as Finite State Machines (FSMs) managed by Smart Contracts can break down data siloes and improve patient outcomes in Blood Transfusion Supply Chains.

[Devpost](https://devpost.com/software/improving-blood-transfusion-supply-chains-with-nfts) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[supply_logistics]]
**user** [[educator_student]] [[patient_family]]

**stack** near-api-js, near-cli, near-sdk-rs, react, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for improving blood transfusion supply chains with nfts

## Body

Inspiration I'm on a mission to make humans live longer, healthier lives. I've been pursuing this by building data oriented healthcare startups, and have taken an interest in recent shortages in the blood transfusion supply chain. I've had an idea that NFTs might be cool since hearing about them a few years ago, and seeing this hackathon prompted me to learn about the underlying blockchain technology. What it does This app mints NFTs that store a Finite State Machine (FSM) on-chain managed by a Smart Contract to store data related to units of blood tracking them from donation to transfusion and disposal. Transparency into this data equips healthcare providers to improve the auditability of their supply chain and improve patient outcomes through superior resource management. The specific use case of improved recall functionality has the potential to reduce costs for healthcare providers as well. How we built it The smart contract was built in rust using the near-sdk-rs, while the front end was built using react and material-ui. The near-api-js library provided the link between the two. Challenges we ran into I spent a substantial amount of time doing tutorials on this hackathon. I enjoyed learning about rust, how the blockchain works, the role of smart contracts and NFTs. I ran into some difficulties with the near-api-js library however, I was getting some very exotic errors when attaching gas to contract method calls and ultimately had to refactor the project such that the smart contract paid for all gas fees. Accomplishments that we're proud of I'm very happy to have built something that demonstrates the value of NFTs that goes beyond the hype. This has changed my perspective on the blockchain. What we learned About two weeks ago I was squarely in the "blockchain is a scam" camp, but after taking a deep dive into the excellent utility of smart contracts and NFTs I've reversed course on that belief. I remain skeptical about bitcoin and its progeny however. I am happily humbled and improved by this hackathon. I'm curious to learn more about NEAR in particular. What's next for Improving Blood Transfusion Supply Chains with NFTs I see many other niches this NFT-FSM concept could be applied to. I find the decentralized architecture very useful. The next step will be exploring how to build a compelling value proposition to blood banks for a pilot program around this product. <div