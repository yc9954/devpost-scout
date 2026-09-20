---
slug: "building-blocks-63kh15"
url: "https://devpost.com/software/building-blocks-63kh15"
title: "Building Blocks"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 409
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Building Blocks

> Building transparent communities one block at a time.

[Devpost](https://devpost.com/software/building-blocks-63kh15) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** chainlink, ethers, hardhat, hardhat-deploy, next, openzepplin, polygon, solidity, tailwind, typescript, vercel, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for building blocks

## Body

Home page Create society page Deposit into society See service details in society Handle services in society Inspiration In Social blocks and Residential complexes where decisions are usually not made as a community, rather it's more likely that a single party does them and they don't share the documents of the transactions they do on behalf of everyone. That raises the concerns of transparency. That inspired us to build a decentralized multisig payment system to pay for services. What it does Building blocks allows a user to create a multisig on demand that provides a horizontal governance structure, making sure all the information and transactions are persistent and each member has a vote. Users can create a multisig by defining a certain deposit amount in USD The deposit is used later to pay for other service transactions. The creator/owner of the multisig can invite other users Only the owner is allowed to create a new service transaction Other users in the multisig can vote on whether they approve the service or not. We use chainlink datafeeds so the user can define their prices in usd and we convert them to matic inside each contract. How we built it We built this using a monorepo where we can see the contracts and the frontend in the same repo. We used hardhat for local testing and solidity for the contracts, we also used chainlink's datafeeds in order to convert usd to matic. The frontend was built with Nextjs, typsescript, tailwind, wagmi and rainbowkit. As a starting point we used npx create-web3 . Challenges we ran into The datafeed for MATIC/USD requires a Matic input and returns a USD output but in our case we wanted a USD input and a MATIC output, for this what we did was basically get the inverse function, this took a lot of trial and testing We are creating multisigs from a factory so we wanted to be able to get some info of each multisig from the factory, this is something that we hadn't done before, we did this using an interface and that was something new. Trying to implement gasless functions. Accomplishments that we're proud of Creating a multisig factory contract Using chainlink datafeeds for the first time What we learned Chainlink datafeeds How to create a factory contract How to use rainbowkit What's next for Building Blocks Adding more datafeeds (for each multisig can handle more tokens). Deploying to polygon main net. <div