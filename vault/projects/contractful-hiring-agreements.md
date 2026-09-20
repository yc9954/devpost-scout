---
slug: "contractful-hiring-agreements"
url: "https://devpost.com/software/contractful-hiring-agreements"
title: "contractful | Decentralized Hiring"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1049
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/regulation_legal_text"
---

# contractful | Decentralized Hiring

> contractful provides peer-2-peer, safe and secure Hiring Agreements for everyone to use.

[Devpost](https://devpost.com/software/contractful-hiring-agreements) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[finance_payments]] [[immigration_refugee]] [[labor_employment]] [[supply_logistics]]
**user** [[small_business]]
**substrate** [[code_repository]] [[regulation_legal_text]]
  <sub>weak: video_visual</sub>

**stack** chainlink, chainlink-automation, ethers.js, hardhat, ipfs, material-ui, nextjs, polygon, react, solidity, typescript, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for contractful hiring agreements
- image credits

## Body

contractful Langing Page. Hiring Agreement on the client side 1/2. Hiring Agreement on the client side 2/2. Waiting for the freelancer or service provider to consent to the Agreement. Consented Hiring Agreement. 🙌️ News: For early MVP access, click here to participate in our survey from Nov to Dec 2022 . Inspiration ✨ There are multiple sources of inspiration for building out the contractful Hiring Agreements. Predominantly, the idea came from our own need to create a fair, safe and secure contracting environment when getting hired for a freelance job or when providing product development services to the crypto industry. Also - from own experience - we can tell, that the whole process around Hiring involves huge loads of paper work for the contractor and the contractee alike. This work is not geared towards productivity, and widely profits from standardization and automation that can be provided by Smart Contract infrastructures. What it does The contractful protocol lets everyone create peer-2-peer, safe and secure Hiring Agreements. Freelancers, service providers and also permanent employees can use contractful together with their clients or employers to manifest their collaboration terms on-chain. The Agreement is built on top of an underlying agile collaboration process. It assumes contractor (freelancer) and contractee (client) to exchange information on a regular basis ("Conversation over Documentation"). The budgets is escrowed by the Smart Contract along a sprint cycle (e.g. 2 weeks). In case of a successful review, the contractor is paid in a timely manner. In case of a dispute, the Agreement ensures a fair way of splitting the funds based on the hours the contractor already worked on the project. This enables DAOs, crypto companies and startups to seamlessly hire staff for their projects on a global, borderless scale. 👉 For freelancers and service providers in the crypto industry, the contractful Hiring Agreement lets you: Getting hired for an agile project by your client in a way that is fair, safe and transparent. In this process the underlying Smart Contract will escrow the budget for a 2 weeks sprint cycle. Payments are automated and dispensed on sprint review of each sprint and are guarded by the Polygon blockchain and Chainlink Automation. 👉 Benefits for clients: Automated payments: Easy and secure on-chain payment processing. Standardized and blockchain governed Hiring Agreements save hours of paper work. Access to a global hiring market. Full budget control: The Agreement ensures clean budget planning that matches your product development roadmap. The following diagram describes the process of the protocol in-depth: For a detailed description, please visit the README of the protocol's GitHub page . How we built it Architecture wise, we split the application into (1) a protocol , and (2) the contractful frontend to interface with the protocol. The protocol is based on the Polygon EVM and complemented by Chainlink Automation to realize scheduled payouts according to the definitions of the Smart Contract. The frontend is realized as a React / Next JS application that uses Material UI for great UX. The actual description of the Hiring Agreement is stored on IPFS. To keep the description disclosed, the payload stored is encrypted using AES. If you want to learn more about the technical implementation and technological choices we have made (like why we use the Polygon blockchain and Chainlink Automation), please visit the protocol's GitHub page . Challenges we ran into There had been several technical challenges, we ran into. From storing data to IPFS, to configuring and authenticating the Chainlink Automation so that it is enabled to transfer real world funds to the rightful recipients, the implementation approaches needed to be sorted out. But the most challenging part was related to finalizing the concept. Getting the use case right with all details of underlying real-world process that works for the client as well as for the service provider (e.g. freelancer) and is also logical, consequent and comprehensible from their perspective, was the most challenging part. Accomplishments that we're proud of In general, we are proud of the UX, the final integration of all decentralized components, as well as we are proud of the Smart Contract implementation that is now an open-source public good and can be used as well as further extended by everyone. 💪 But we are in particular proud of having created a self-contained product that is ready to being used by everyone out there in the industry. Foremost, the solution now can be used by ourselves 😝 What we learned React and managing concurrent frontend state. Integrate the frontend with the Wallet and the Smart Contract in particular. Use Chainlink Automation with challenging schedule requirements. Store and retrieve data to and from IPFS. Managing the Hackathon project around three different time zones. What's next for contractful Hiring Agreements 💡 The future potential is huge and comes from different angles. Core functionality of the Hiring Agreement Support a broad range of coins (e.g. ERC-20) for financial arrangements in the Agreements. Support VAT and other tax regulations for business interactions between parties from different countries. Add a time sheet functionality, and base the payment due to the service provider, on hours recorded. Provide a specific Agreement for permanent employees. Challenge the assumptions made in the contractful beta regarding a fair split of the budget in case of a cancellation of the Agreement (from the perspective of a client as well as from the freelancer or service provider). Align payouts with custom target for software development (e.g. git commits & successfully tested deployments). Introduce a DAO to the protocol for dealing with disputes. Support weekly or even daily payouts. Evolve the protocol to support the extension of Agreements beyond the predefined engagement period. Services around the protocol Capital efficiency: Generate interest through low-risk yield generating third party protocols (e.g. lending ERC-20 based stablecoins) while the funds are waiting to be dispensed. Provide tax reports for download. Handle even income tax settlements automatically. Integrate or refer contractful users to crypto banking platform (like juno.finance). Integrate contractful with recruiting markets or decentralized reputation systems. Technical improvements Make the contract more Gas efficient (e.g. by being more selective about on- vs. off-chain data). Use ZK technology to make the terms of the Agreement (e.g. sprint budget based on the hourly rate) private to the collaborating parties only. Image Credits fatmawatilauda70555 on vecteezy.com . <div