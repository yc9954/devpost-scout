---
slug: "liddx-payroll"
url: "https://devpost.com/software/liddx-payroll"
title: "liddX Payroll"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 534
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# liddX Payroll

> liddX Payroll we plan to be the Sage payroll of blockchain, making it easy for users to manage employees, payroll and client projects all from a single platform built on Hedera Contract Service.

[Devpost](https://devpost.com/software/liddx-payroll) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** angular.js, circle, hedera, ipfs, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for liddx payroll

## Body

Login Dashboard Inspiration liddX Payroll is inspired by the need for a decentralized payroll and project management application on the blockchain that would enable seamless HR and project management for web3 users and businesses within the community. We seek to become the Sage payroll of the Blockchain space using stablecoins and native crypto for payments to employees and clients as well as making use of IPFS for the storage of business data. What it does liddX Payroll allows for an organizations to create and capture new employees into the payroll system, run payroll. It also allows the organization to manage projects and payments thereof. With liddX employees have access to an easy to use Self-Service Portal to update their personal records, log timesheets and update payment details. Clients of the organisation also have access to a protal where they can capture invoices, track the progress of the project and interact with the organizations team. All this and more on the blockchain using Smart Contracts and IPFS for data storage How we built it Our MVP was built using Angular with Typescript as the frontend framework, the design was put together using Draw.io. We then implemented the smart contracts as the application backend using Solidity and deployed the basic initial contract to Polygon's Mumbai testnet using Hardhat and IPFS for the data storage. We used Chainlink Keepers to run the payroll function. This will allow for the contract to execute the monthly salary payments automatically on the set date. Challenges we ran into When coming up with the dApp concept we quickly realized that this would not be a simple CRUD smart contract and would require some complex data structures within the smart contract to manage the application backend, since we are beginners in Solidity we seeked advice from the community and were advised to build a basic smart concract just as proof-of-concept which we would then improve on after the hackathon. We also ran into issues trying to implement signin with wallet using Moralis, also the issue was not resolved we plan to work on it after the hackathon. Accomplishments that we're proud of This is our first time working with major hackathon with a complex solution, although it was challenging we managed to put together a bacis but functional smart contract as well as deploy to Mumbai and to integrate some sponsor technology. This coupled with a beautiful UI is definetely something we are proud of as an accomplishment. What we learned We learnt the importance of starting small when building up a concept as it can be overwhelming, also, how to leverage the community when help is required. Most of all we are happy to have learnt about smart contracts and how to deploy application on the network. What's next for liddX Payroll Firstly we would like to improve on the overall smart contract and UI to provide full functionality for our proof of concept as well as implementing a contract factory so that each organization deploys their own contract. We also would need to work on the dapp's security and get the smart contract audited. Lastly we would love to actually launch the project on mainnet and get to market. <div