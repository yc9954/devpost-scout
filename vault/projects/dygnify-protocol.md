---
slug: "dygnify-protocol"
url: "https://devpost.com/software/dygnify-protocol"
title: "DygnifyProtocol"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 743
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "user/developer"
  - "user/general_public"
  - "user/small_business"
---

# DygnifyProtocol

> Defi protocol for real world lending - A decentralised credit infrastructure for connecting digital asset investors to investment opportunities (Credit Funds, FinTechs) in real world.

[Devpost](https://devpost.com/software/dygnify-protocol) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[developer_tools]] [[disaster_emergency]] [[finance_payments]]
**user** [[developer]] [[general_public]] [[small_business]]

**stack** alchemyapi, blockpass, figma, ipfs, openzeppelin, polygon, react, solidity, spheron, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dygnifyprotocol

## Body

Dygnify Logo Dygnify proposition on a page Dygnify proposition in a line Inspiration Inspiration for Dygnify comes from our interaction with hundreds of small businesses (“SMB”) who fail to access formal financing and spiral into the debt trap. Our project is a means to enable financial inclusion at scale, enabling SMBs to build a transparent on-chain credit track record so that they can access global pools of capital at affordable cost. We believe that if we’re able to get larger pools of capital to flow to the SMB funding chain (specialized funds, shadow lenders, Fintechs), it will result in enabling better access to credit to SMBs What it does Dygnify is a provider of decentralised credit infrastructure for connecting digital asset (crypto) investors to investment opportunities linked to SMB economic activity. We have implemented a use case of a Credit Fund as a borrower, who in turn is aggregating/lending to small businesses. We believe access to decentralized finance can help solve the financial inclusion problem sustainably by bringing the following benefits: 1. For the borrowers – a. Tapping global digital asset liquidity bringing sustainable lower-cost solution for emerging market borrowers b. Accessing Blockchain based on-chain borrowing, which is fast, secure and creates an immutable credit track record which can open the flood gates to capital * 2. For the investors – * a. Empowering any digital asset holder to become a lender, backing real-world economic activity b. Stable, sustainable yields (10-25%) delinked from crypto volatility We plan to build a progressively decentralised community (DAO) of underwriters, auditors, service providers, asset originators, developers and investors; with an incentive mechanism designed to yield good behaviour, can solve for centralised decisioning across the network We plan to build the protocol as an infrastructure toolkit to serve three purposes: a. Taking away crypto and DeFi complexity for users b. Providing on+off chain reputation & identity management, regulatory compliance c. Enabling Security and Privacy Example – tools for on+off chain credit scoring, Reputation management, whitelisting, compliance, decentralised data storage, dash boards etc. with encryption and security features built-in. How we built it We started with writing end to end customer journey Concretized the user journeys through a Figma prototype Finalized our Web3 tech stack – Polygon emerged as the go-to chain for hosting our Dapp, while leveraging Web3 infra of decentralized file storage (IPFS) and decentralized hosting. We also leveraged OpenZepplin’s battle tested smart contracts to write our own custom upgradable smart contracts on top. Finally, we used Alchemy to host our Dapp on Polygon network Developed Front end using React and react native frameworks like Material UI and tailwind CSS. Smart Contracts are written for Borrower and Investor profile creation, Loan Request/Opportunity pool creation by Borrower, Investor deposit and withdrawal, Borrower drawdown and repayment and Loan request allocation to Underwriter and approval of loan requests by Underwriter. Most importantly, since we are developing a protocol that enables lending to Real World Assets, we have integrated with Blockpass, a global KYC/AML API for Investor and Borrower KYC and AML to ensure compliance. Challenges we ran into Internal Integration testing – multiple scenarios and inter-dependencies took a lot of time and thinking to get right. 3rd party integration testing with providers like Blockpass and Spheron. Worked collaboratively to stitch all integrations that are working well now. Accomplishments that we're proud of We’re glad that we could make the full end to end functionality right from user KYC to investor withdrawal with a simple to use UI/UX. We have also validated the proposition with few borrowers who have expressed their willingness to be our first users. What we learned Its always better to keep making smaller units of functionality and keep integrating it Follow the best practices of s/w writing so that we avoid the common traps While building the product, simultaneously testing the hypothesis with potential users is critical. What's next for DygnifyProtocol Next 30 days - We would like to add functionalities like Gnosis safe multi-sig, automate opportunity allocation to underwriters, build user whitelisting via identity NFTs, do internal security testing by running static analysis and fuzzying + run our project on the public testnet, do bug-bounties Next 60 days - Get the project audited by one of the reputed smart contract auditors Launch it on the Mainnet and start implementing real use cases. Once live, keep adding new functionalities like decentralised reputation management, on and off chain credit scoring, identity management tools, add more wallet support. <div