---
slug: "azurance"
url: "https://devpost.com/software/azurance"
title: "Azurance"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 499
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/document_pdf"
---

# Azurance

> A decentralized insurance platform for everyone.

[Devpost](https://devpost.com/software/azurance) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[document_pdf]]

**stack** ccip, chainlink, datafeed, foundry, functions, github, graphql, next, solidity, subgraph, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for azurance

## Body

Azurance Products Liquidity Claim Inspiration The traditional insurance system faces several challenges, including limited liquidity providers (banks and insurance sellers), cumbersome claiming processes, and low flexibility in benefit conditions. Azurance addresses these limitations by offering an open, instant-claim, and highly flexible system for insurance. Liquidity can come from anyone seeking investment. The insurance conditions cover many cases, both on-chain and off-chain data, thanks to Chainlink. Once an insurance contract is eligible for a claim, buyers can immediately claim their benefits without needing further documents and proofs. This platform revolutionizes the insurance industry, benefiting users in both risk management and investment gains. The system simplifies launching global-scale insurance programs from day one. What it does The platform enables anyone to create an insurance contract with customizable conditions. Once deployed, anyone can provide liquidity to the contract, hoping to earn a yield upon maturity. Insurance can be bought by those looking to hedge against various conditions, such as global pandemics, price crashes, or DeFi platform hacking. The platform tracks insurance buying and selling through ERC-20 tokens, Buyer tokens, and Seller tokens. This allows users to swap their insurance statuses on secondary markets, adjusting their risk and return profiles. Both buyers and sellers engage with an insurance contract by depositing their assets. There are three possible outcomes for a contract: Claimable - if the predefined risk condition occurs during the contract period, buyers can claim their benefits. Matured - if the contract expires without any risk event, sellers can claim their benefits. Terminated - in case of issues with the contract, everyone can reclaim their deposit. How we built it The web frontend is developed using Next.JS, ethers.js, WAGMI, and Graph client. The smart contract is written in Solidity using Foundry, with openzeppelin for standard contracts. Chainlink contracts, including Data Feed, Functions, and CCIP, are integrated. The Graph is utilized to index insurance contracts, eliminating the need for backend services as it handles complex queries. Challenges we ran into As beginners, Chainlink's products were initially complex, leading to numerous errors. Eventually, we managed to get them working. Developing a mathematical model for risk and return that is equitable for all stakeholders was challenging but eventually accomplished. Integrating Polygon ID was difficult for us to execute. Debugging the subgraph was time-consuming due to its complexity. However, it is essential for user-friendly dapps. Accomplishments that we're proud of We successfully integrated three Chainlink services and plan to integrate more in the future. We developed a fair mathematical model for justifying the risk and return of all stakeholders. What we learned We gained significant knowledge in using Chainlink, Polygon ID, and The Graph. We discovered the enjoyable aspects of mathematics, especially in DeFi products. We improved our team collaboration and optimization skills. What's next for Azurance We aim to ensure the security of the developed contract before its mainnet launch and seek smart contract audit support. Enhancements in user experience are planned. We intend to secure grants and prepare for mainnet launch when ready. <div