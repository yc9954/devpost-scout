---
slug: "handshake-0szjd5"
url: "https://devpost.com/software/handshake-0szjd5"
title: "HandShake"
hackathon: "TRON Grand Hackathon - HackaTRON Season 6"
organization: "TRON DAO"
winner: true
words: 484
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/civic_government"
  - "substrate/financial_record"
---

# HandShake

> More secure and reliable way of token transfers, Ensured by Mutual Consent

[Devpost](https://devpost.com/software/handshake-0szjd5) · hackathon [[TRON Grand Hackathon - HackaTRON Season 6]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[civic_government]]
**substrate** [[financial_record]]

**stack** mongodb, next.js, node.js, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for handshake

## Body

Home page Home page Dashboard Initiating Transaction EIP-712 Signing Approving transaction Inspiration The inspiration behind creating Handshake stemmed from reports of individuals permanently losing funds by sending tokens to incorrect addresses. Analyzing this issue, we asked ourselves why not develop a product that adds an additional layer of security to the ecosystem. Additionally, we recognized that many users are unaware of the details they are approving, as they typically see only the hash in their wallet during transactions. To address this, we decided to implement EIP-712 to enhance clarity and safety. What it does Handshake Protocol makes token transfers especially safe and secure, no matter the size of the transaction. Before any tokens are moved, both the sender and the recipient have a chance to double-check and agree on all the details. This step is like a mutual thumbs-up — it ensures that everyone is on the same page, and it prevents mistakes like sending tokens to the wrong place or to an inactive account. With Handshake, you can relax knowing that every transaction is double-confirmed. It’s perfect for when there’s a lot at stake and you need that extra layer of security. Just a simple and secure way to handle large token transfers without any hassle. How we built it We have leveraged EIP-712 standard, which allows users to see clearly structured data when signing transactions. This clarity ensures that all parties understand exactly what they are agreeing to, enhancing trust and security in decentralized transactions. Challenges we ran into One challenge we faced was during the creation of the smart contract and implementing EIP-712. We were trying to verify the signature, but the address obtained using ECDSA was not from the initiator of the transaction. We were making some errors with the data passing, which took our time, but eventually, we were able to solve those problems. Accomplishments that we're proud of We are proud that we were able to complete all the milestones on time and were able to design the product as we wanted to. The idea that was conceived in our minds and what the end product became were exactly what we desired to create. What we learned We have learned many things from this project, first of all, team collaboration. It is crucial for everyone to be on the same page. On the technical aspects, we got to explore more about smart contracts and the cryptographic foundation of signatures and how they work. What's next for Handshake We will add a feature by which the sender, who is sending the tokens, can send tokens without paying the gas fees with the Handshake protocol, just like we have the permit function for ERC-20 tokens. We also aim to integrate Handshake Protocol with major DeFi platforms, expand the range of supported tokens, and explore additional use cases in commercial transactions and cross-chain operations to enhance its accessibility and utility. <div