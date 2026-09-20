---
slug: "the-apis"
url: "https://devpost.com/software/the-apis"
title: "Blockchain API"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 661
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/financial_record"
---

# Blockchain API

> The easiest way to connect your app to blockchains. Blockchain API is to the blockchain as Twilio is to telephony, or Stripe is to online banking.

[Devpost](https://devpost.com/software/the-apis) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[financial_record]]

**stack** colocation, docker, ethereum, graphql, node.js, postgresql, postman, react, redis, rust, solana, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the apis

## Body

Launch your own ERC20 token with one API call Inspiration The high yield decentralized finance (DeFi) products have attracted over $26 billion U.S. dollar locked on blockchains. DeFi products are developed by elite engineers with in-depth knowledge in blockchain, cryptography and finance. While these products are mostly open source, the deep learning curve has prevented more developers to build better user experiences that could lead to more mainstream adoption. The APIS project aims to liberate the DeFi access by allowing developers to connect their apps to blockchain with easy RESTful APIs. No blockchain expertise required; no blockchain nodes to run, and no infrastructure to manage. Even the no-code or low-code community can build decentralized apps with the APIS endpoints! What it does The APIS allow developers to perform commonly used blockchain methods with simple API calls. From create wallet to launch your own token , or even performing analytics and queries that are usually slow using web3 and RPC calls can be done in milliseconds with the APIS endpoints. The APIS is built with real world use cases and an open architecture in mind. All developers can further the power of the APIS by contribute to the project on Github. As a tutorial, we have created endpoints to retrieve DeFi lending protocol savings rates, allow users to supply and earn yields and list the assets in wallets. You can build a high yield savings products easily with just these 3 endpoints. How we built it The APIS creators have been building different blockchain apps for 3 plus years. We put together a code base that is connected via a gateway that connects to different blockchain nodes on both main net and test nets. We built an extensible backend service that breaks into several categories, from the native RPC pass-throughs so we can support all native calls, to high level unified API endpoints that allow uniform curl calls to connect to different blockchains. In this hackathon, we are supporting Ethereum and Bitcoin blockchains, while we have also created connections to Solana. We have built part of the frontend UI with GraphQL and React, but we ran out of time so it will be completed later. The server is put together with NodeJS, that connects to an indexed Postgres DB that syncs to blockchain nodes and provide caching for fast queries. Challenges we ran into There are two main challenges we encountered: the more blockchain nodes that we run (current 4 nodes, main net and test net for both Ethereum and Bitcoin), deployment and syncing the nodes require a lot of devops work to maintain the infrastructure. The second challenge is inherited to how blockchain works. To be secure, signing transactions should happen on client-side, and only pass the signed transaction to the API endpoints to be executed on blockchain. However, that'll require more frontend work which we did not have time to finish within the hackathon period. The better solution is to bundle the RESTful APIs with client-side SDKs. Accomplishments that we're proud of We are proud to be one of the first--if not the first--open source and decentralized project that empowers developer to easier blockchain access on a much higher level. We have been told the APIS to blockchain is like Twilio to telephony or Stripe to online banking. What we learned As we talk to more peers about our project, I learned the interest level of being able to connect to DeFi is high. We also realize that there are a big and growing No-Code and Low-Code community that want to have more high-level APIs built so the non-tech entrepreneurs can focus on building user experience and bring the high yield products to masses. What's next for The APIS We want to continue building out more features based on real world use cases. We will work with different entrepreneurs and developers who have solid decentralized app ideas, to provide them with more powerful RESTful APIs and support more blockchains. <div