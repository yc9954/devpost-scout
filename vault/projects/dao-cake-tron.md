---
slug: "dao-cake-tron"
url: "https://devpost.com/software/dao-cake-tron"
title: "DAO Cake"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 1172
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# DAO Cake

> Making founder contributions easy. Bringing DAO tech to communities & startups.

[Devpost](https://devpost.com/software/dao-cake-tron) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**domain** [[civic_government]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** solidity, typescript

## How they structured the write-up

- incentivise & pay dao members with ease!
- what it does
- architecture
- team
- deliverables
- roadmap
- business model
- what's next for dao cake - tron

## Body

Incentivise & pay DAO members with ease! At amaDAO.io we've been working with DAOs to better understand their needs. The inspiration for DAO Cake came from those discovery interviews with DAOs over the last 10 months. What we found is that for every tokenized DAO there were at least 10 more that were not. We found web3 communities with tokenisation in their roadmap still needed the tools of DAOs: proposals, voting, payments, equity share tracking on chain, yet without their own token. More so, as many of these projects were early and decisions still to be made; they needed tools to be easy to use, easy to get started and without complex configuration or dev resources. From our interviews; consistently we heard that the founding process was full of excitement and energy, everyone involved wanted the same things. However, if there was one thing that caused fiction it was the arguments over contributions which impacted that founding energy. DAO Cake sets out to solve that issue. For the TRON hackathon we’ve focused on the requirements prior to the token generation event. This is often the most troublesome; in the absence of a DAO’s own token there needs to be a mechanism for trust. What it does DAO Cake solves the problem every multi founder team experiences: measuring and rewarding contributions. The typical (imperfect) approach for startups is to split equity equally between each member of the founding team, with the expectation each is bringing equal value. This is not a solution for DAOs as the entire founding community are the ‘founders’. Even if still at the infancy this could be ten or more people committing time and effort in varying degrees to form the DAO. TRON provides an efficient on-chain ledger and runs the most widely used and readable industry standard smart contract language (Solidity). DAO Cake stores transactions on the TRON Blockchain and its' Smart Contract code runs in the TVM (Tron Virtual Machine). The contributions are transactions which claim an amount similar to IOUs (I Owe yoU). In our case, there is no ‘I’ so we term these DOU (DAO Owes You) or ‘Dough’. This makes the DApp easy to use and suitable for startups and communities that do not know if they are going to ultimately generate a token, they may simply have a founding event where all the contributions (DOUs) are tallied and the equity share split accordingly to each contributor. We’ll call this event ‘Baking’. Beyond the hackathon we’ll add features that will allow various forms of Token generation methods for the Bake: Airdrops, NFT Badges etc for contributors. DAO Cake brings to TRON a powerful tool to serve the thousands of new web3 communities and startups. Beyond DAO Cake, our team at amaDAO.io have been working on a suite of products to serve DAOs in facets relating to the future of work. Architecture We’ve kept the model simple yet sufficiently complex and considered for this application. You could say we did not want to “over cook it” (Cake pun intended). We believe the best smart contracts are simple and easy to read so that anyone (technical or not) can understand what is happening. We also wanted to keep this DApp open for anyone to use. With more time we can assess market needs and adjust the implementation where needed (see: roadmap) Smart Contract features TRON TVM Solidity - Secure, type-safe and readable Event emitting - For integration with GraphQL (tracing / audit capable) Simple extensible model based on: Proposal -> transaction lifecycle through voting which can be easily adapted to various types of work associated with an organisation. Inbuilt consensus rules and the ability to update though a proposal and voting. External ID fields to assist integration with external databases. On-chain data maintained to only the critical elements and references necessary for on chain actions. Blob storage ID (for immutable IPFS or BTFS storage) to encode references to large data PDF for invoices, proposal docs etc Deployed to Shasta TestNet: https://shasta.tronscan.org/#/contract/TCPsXZWsTzSGFxAqtbcBG3eFTcJvcDNjet/code DApp front end The original idea was to develop a Smart Contract only and integrate into other tools we've already developed and make it available for 3rd party and community integration. The Smart Contract alone is a powerful product and useful for our immediate application. However, the rest of the team has become interested in the product and see potential for both a stand alone Native Mobile app and ReactJ dashboard. We're now working on the MVP dApp in React / NextJS. Team At amaDAO, we’re a team of 5 engineers covering skill-sets from blockchain, front-end dedicated Mobile Native and ReactJS. Over the course of the last 8 months we’ve evaluated and built products on 5 different blockchains in search of the right fit for our backend. Our core team has worked together in the future-of-work industry for over 6 years. We’ve all been heads down on building out the core platform. As the solution architect, I personally experimented with TRON in my spare time. Deliverables With the limited resources (me) and time available I’ve focused purely on the smart contract. We’ve commenced the front-end in React but have not had time to integrate. We will continue to work on this over the coming weeks to bring the full benefit of the DAO Cake vision to a stand alone DApp. Roadmap Implement Smart Contracts on TRON TVM (DONE) dApp services layer connected to contract on Shasta Testnet (DONE) Complete front-end of DApp MVP (50% DONE) Implement ‘Bake’ action for pay out (from escrow) to wallets to member slices Customer testing of DApp. Feedback on UX, any limitations? Review incentives / disincentives for application in larger DAO communities Generate Internal $DOU token with tokenomics to incentivise participation in voting/proposals (TRC20 Asset Tokens) Provide alternative Bake actions for token issuance (TRC20) or NFT (TRC-721) achievement badges. Launch dApp on Mainnet Build iOS and Android native apps. Launch dApp with chosen business model (Token, SaaS, Service fee?) Assess other applications: eg: measuring open source GitHub contributions. Business model DAO Cakes’ target audience is both web3 startup and DAO founders. We’ll publish the product to Product Hunt, Indie hackers, Reddit and through founder niche campaigns. We’ll generate users through campaigns we’ve planned for amaDAO which include a web3 jobs marketplace and an on-chain CV; the target audience is the same. Revenue will mostly come through amaDAO products and add ons. We’ve had little time for gauging reaction, however potential business models for DAO Cake include the following: Monthly SaaS fee per seat or per organization (includes support) A small percent eg: 5% of $DOU on a TGE Percentage fee on block signing events. What's next for DAO Cake - TRON There are currently approx 4,800 indexed and tokenized DAOs. We’re targeting the 40k+ DAOs who are essentially startups or web3 communities that have not yet tokenized or formalised their structure. We’re excited by the potential to simplifying fledgling ‘DAO’ operations and payments. But also excited by the potential to bring thousands more daily transactions to the TRON blockchain. <div