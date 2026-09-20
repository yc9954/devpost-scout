---
slug: "nomis-n1p0cd"
url: "https://devpost.com/software/nomis-n1p0cd"
title: "Nomis"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 759
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/financial_record"
---

# Nomis

> Nomis is an open-source protocol that helps developers both to build better DeFi producst, and to balance already existing high-TVL protocols.

[Devpost](https://devpost.com/software/nomis-n1p0cd) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**user** [[developer]]
**substrate** [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** .net, asp.net, c#, css, docker, html, javascript

## How they structured the write-up

- inspiration
- what it does
- what we built during the hackathon
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nomis
- team

## Body

Inspiration We build Nomis to crush one of the most significant barriers to entry and adoption of DeFi which are over-collateralized loans. Today mainstream borrowers are either not using DeFi lending due to its unattractiveness as a financial product comparing to bank lending, or taking over-collaterized loans with unfair collaterals and APR. In other words, today's DeFi loans suck: ﹥125% collateral scares away mainstream borrowers from DeFi loans; Collateral liquidation terms are tricky and make it even more unattractive; No personalized terms even if a user has 'good' on-chain history. Over-collateralized lending and lack of customized reputation-based terms are the huge problems that needs to be solved to bring mainstream borrowers to DeFi and get closer to mass adoption. Our long-term vision is to allow one to borrow capital using one’s on-chain reputation as a form of collateral (best cace scenario), or at least provide better terms. What it does Nomis is an open-source protocol that helps DeFi developers both to build better on-chain solutions and use cases, and to balance already existing high-TVL protocols. Every lending/borrowing platform will be able to create extremely customized loan terms for borrowers by using Nomis API. Nomis is designed to be a multi/cross-chain solution and offer the most robust financial snapshot of a potential borrower by hiring hierarchy analysis as a scoring method. Before the Hackathon we had MVP on Ethereum and Solana . Nomis will help Polygon to grow its TVL, MAU (as a result of acquisition of mainstream borrowers), MAD, # of on-chain use cases (as a result of opportunity provided to develop new DeFi solutions on-top of the Nomis open-source protocol). What we built during the Hackathon As far as we aspire to build multi-chain solution and offer the most robust financial snapshot of a potential borrower, we are extremely interested in developing Nomis on top of Polygon. As a result, we have developed MVP for Polygon wallets based on on-chain history which is open source . We also have developed API and its documentation . Our Hackathon roadmap was as the following: Extracted wallet and transaction data from Polygon and constructed initial variables; Aligned the Nomis mathematical model to the variables extracted; Developed credit score and UI for Polygon wallets; Developed API for Polygon and its documentation. How we built it We hired PolygonScan API to get wallet, transaction and NFT-movement data. We constructed variables, based on the data extracted, which can be received via Nomis API. Finally, we hired our mathematical model to develop Nomis (credit) Score based on the constructed variabled. Our solution is based on the .NET 6 platform and the ASP Net Core framework. We used the Docker toolset to build and deploy the solution. To build, run the command below: docker build -f src/Nomis.Web.Client.Polygon/Dockerfile -t nomis-polygon . docker -dp 80:80 nomis-polygon Challenges we ran into Choose and justify the appropriate methods for the model. Build the appropriate mathematical model for credit score calculation based on expert opinions. Accomplishments that we're proud of We are proud that we developed MVP for Polygon during the Hackathon. Moreover, the prototype correctly works based on wallet and transaction data only. We took a step further and developed several product- and business model-related hypotheses during the Hackathon. What we learned How to work with PolygonScan API. Deepen our knowledge about the structure of the Polygon blockchain. What's next for Nomis As mentioned above, our goal is to allow one to borrow capital using one’s on-chain reputation as a form of collateral (best cace scenario), or at least provide better terms. Although, the long-term vision for Nomis goes far beyond credit scoring for DeFi. In the future, other dApps will use Nomis Score as a wallet qualifier for making job offers, adding in whitelists, offering special marketing terms, or just for inviting to a private party, etc. We plan to make Nomis self-sufficient by hiring one of the B2B or Web3 business models and GTMs. Team Fedor - PhD in CS - Solidity & Rust developer - 8 patents’ holder (neural networks) - Ex. custom L1 blockchain solution Alex LinkedIn • Telegram - MSс in Mathematics and Economics - 5-year C-level experience - 15-year experience in neural networks - Ex. GoRecruit — employee scoring SaaS for HR Arty Twitter • LinkedIn • Telegram - MSc in International Business Development - 4-year experience of PM/UI/UX in crypto - Ex. KickCity — web3 event dapp on Ethereum - TON Hackathon Awardee Nick - Degree in CS - .NET developer - Active open source contributor - 4 times blockchain hackathons awardee <div