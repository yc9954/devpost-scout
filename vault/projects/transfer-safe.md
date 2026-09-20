---
slug: "transfer-safe"
url: "https://devpost.com/software/transfer-safe"
title: "Transfer Safe"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 601
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Transfer Safe

> TransferSafe brings safe peer-to-peer two-step transfers to the Polygon network.

[Devpost](https://devpost.com/software/transfer-safe) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]]

**stack** alchemyapi, amplify, ethers, github, hardhat, next.js, react, solidity, wagmi

## How they structured the write-up

- inspiration
- how i built it
- sponsor tools used
- what i learned
- what's next for transfer safe

## Body

Invoice creation on mobile devices Payments on mobile devices Desktop invoice creation step Desktop invoice creation Desktop wallet connect Desktop invoice view Desktop invoices list Inspiration A year ago, I was looking for an apartment and found a really perfect one — nice looking, well located, and at an affordable price. However, I was asked to pay a small deposit in advance to secure my willingness and keep these apartments for myself. I know, that already sounds like scum, but I was so in love with these apartments that I paid it. And, obviously, the landlord disappeared right after receiving my money. So that's how I came up with the idea of TransferSafe — the app with secure two-step transfers. The first step is a deposit, which TransferSafe holds for two weeks, and the second is a confirmation made after you complete your deal with a seller. How I built it Frontend and backend The TransferSafe's frontend and backend are built on top of the Next.JS React framework, using the following technologies: Next.JS for frontend app, API routes, and server-side rendering Ethers.io for integration with polygon network and wagmi to use ethers as webhooks Material UI as a design framework Smartcontract The smart contract is built on Solidity using the following tools: Solidity as a contract programming language Hardhat for testing and deploying Chainlink for verifying exchange rates during transfer Alchemy as a provider for connecting to the Polygon network and receiving transaction webhooks Runtime and CI/CD Our web app is powered by AWS Amplify . We use it extensively to deploy our app and monitor it. Sponsor tools used AWS Thanks to AWS Amplify , we have our Next.JS app deployed in an entirely serverless environment (yet with serverside rendering, API, etc...). The app runtime is split into two different environments — production and alpha and is being deployed automatically using repository triggers. Chain.link Chainlink is used a lot in the TransferSafe web app and contract. We use it to display invoice amounts in different currencies in our web app and to check the transfer amount against the one that the invoice creator specified in US dollars. Sequence wallet You can use Sequence wallet with TransferSafe to create invoices and pay them (check out the demo video) Since the Sequence wallet is not yet supported by wagmi and RainbowKit , I had to create a few connectors to make it work, and now they are open-sourced and available as npm packages: sequence-connector-wagmi — sequence wallet wagmi connector sequence-rainbowkit-wallet — Sequence RainbowKit wallet connector What I learned Since this is my first blockchain project, I've learned a lot :-) The main Take-aways are: Writing smart contracts using the Solidity and Hardhat stack (check out our smart contract repo ) Auto testing smart contracts using Mocha and Hard Hat test nodes (check out our test reports ) Distributing smart contracts as npm packages (check out our Github Action which builds and deploys TransferSafe router smart contract ABIs) Using ethers and wagmi hooks to build modern web3 powered dApps (checkout our web app ) Working with wallets (check out the wagmi connector and the RanbowKit connector I've made for Sequence wallet) Deploying Next.JS apps with server-side rendering to amplify (nothing to show there, but trust me — it's super easy) What's next for Transfer Safe The next step for TransferSafe is public release on a production Polygon network, which requires about 3-4 weeks of development, testing, and fixing bugs. After the public launch, our main task will be to test the product in real market conditions, assessing product-market-fit and customer acquisition cost. <div