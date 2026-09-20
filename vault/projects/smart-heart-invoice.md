---
slug: "smart-heart-invoice"
url: "https://devpost.com/software/smart-heart-invoice"
title: "Smart Heart Invoice"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 352
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Smart Heart Invoice

> Smart heart invoice was a web platform enabling cryptocurrency transactions and integrating blockchain seamlessly into an all-encompassing invoice system.

[Devpost](https://devpost.com/software/smart-heart-invoice) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** nestjs, nextjs, postgresql, radis, solidity, thegraph, typescript, wagmi

## How they structured the write-up

- inspiration
- features
- why do we create solutions
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smart heart invoice
- how to try smart heart invoice

## Body

Flow of Smart Heart Invoice Customer invoice list Claim: cross chain Admin dashboard Customer pay Inspiration Coingecko's recent report highlights a significant trend—global companies are investing around ten billion dollars in Bitcoin for corporate treasuries. Our solution offers multiple transaction channels, providing businesses with diverse options to manage cash flow effectively. Features Blockchain Empowerment Harnessing the potential of blockchain technology to enhance business transactions, seamlessly connecting real-world activities with the blockchain. Effortless Transactions Facilitating sellers in effortlessly generating invoices and conducting transactions through the integrated blockchain system. Data Synchronisation Implementing a robust system for updating diverse transaction data, ensuring synchronisation between on-chain and off-chain activities for a comprehensive overview. Why do we create solutions Difficult Tracking invoice status Difficult transaction Payment Verification limitation of accepting only fiat currency How we built it CCIP - Deployed contract on 3 chains, utilized in the pay and claim process for cross-chain token transfers. Chainlink Function - Integrated with CCIP contract, using Chainlink Function to call our backend api for update status Chainlink automation - Set up custom logic automation triggers to call CCIP smart contract for the claim process. Sub graph - Emit and query transaction (Claim) to show Frontend - connect with backend and smart contract Backend - provide general data such as invoice, customer Challenges we ran into We went through various difficulties with determination and learning. After that, we were able to complete the planned work. Accomplishments that we're proud of Successfully implementing Chainlink products into the invoice system. Increased skills in smart contract development. Building valuable relationships among team members. What we learned Utilizing Chainlink products: CCIP, Automation, and Chainlink Function. Integrating Chainlink products with real-world use cases. The effectiveness of teamwork in a Scrum environment. What's next for Smart Heart Invoice Discuss with AP department: for get more feature We want to apply some of NFT (ERC1155) for represent to success invoice transaction Cornjob: For update over due invoice status Subgraph We will emit and query all of step of invoice process How to try Smart Heart Invoice https://docs.google.com/document/d/1dVpibFabLeNnvwk-BaOqbpIwvU7OxzcIrpJiZTUjdaU/edit?usp=sharing If you want to try all features, Please contact noppawansa29@gmail.com <div