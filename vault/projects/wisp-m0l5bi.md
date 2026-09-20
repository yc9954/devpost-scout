---
slug: "wisp-m0l5bi"
url: "https://devpost.com/software/wisp-m0l5bi"
title: "Wisp"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 273
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Wisp

> Turn your public wallet into a private bank.

[Devpost](https://devpost.com/software/wisp-m0l5bi) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[structural_withholding]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** circom, graphql, nextjs, solidity, thegraph, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for wisp

## Body

DApp main page One time payment request modal. Requestor specifies the token and amount One time payment page. Sender pays the token amount specified by requestor Permanent payment page. Sender can manually input the token and amount Portfolio page Ethereum Mainnet portfolio page Polygon Mainnet portfolio page Transaction page Inspiration Currently as a payer, in order to send a recipient money on EVM-compatible blockchains, he or she needs to know the address of the recipient. However, a recipient may feel uncomfortable sharing his or her wallet address with the payer because: it allows the payer to make a connection between the recipient’s wallet and the identity of that recipient it exposes all of the recipient's financial history to the payer (ex. number of tokens, amount of each token, transaction histories of each token, NFTs, and to whom and where money is being sent or received) What it does Wisp is the first decentralized bank protocol which allows anyone to: Receive payments without revealing their wallet addresses Send payments straight from their Wisp wallet Download account statements for official reporting Passively re-invest money right from their wallet (under development) How we built it DApp frontend is built using Next.js and TypeScript DApp utilizes SNARK zero-knowledge proofs and asymmetric cryptography to keep your assets secure and private ZK circuits are built using circom language and solidity verifies are exported via snarkjs Smart contract wallet allows automatic funds reinvestment What's next for Wisp Re-invest funds in the smart contract using Aave or own lending protocol for APY gains Turn the app into a full-featured wallet Allow private NFT transfers Wisp SDK for private payment integrations <div