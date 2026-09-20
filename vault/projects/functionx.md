---
slug: "functionx"
url: "https://devpost.com/software/functionx"
title: "Cloudbeam"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 562
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
---

# Cloudbeam

> "Seamless Cloud Computing for Smart Contracts: Unlock Efficiency, pay with diverse tokens"

[Devpost](https://devpost.com/software/functionx) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]

**stack** amazon-web-services, javascript, nextjs, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cloudbeam

## Body

Cloudbeam Dashboard Register Functions with Automation Register Functions without Automation Service Marketplace Edit Registered Function Top up Inspiration Having built previous projects that require a lot of computation and involve usage of external data in smart contracts, we encountered issues with bringing computation on chain, with ease. Also, from our survey conducted of developers, we also noticed that it gets difficult to acquire LINK or other ERC 20 tokens to pay for computation. What it does Cloudbeam provides a seamless and efficient way to manage computations and functions, making it easy to integrate functions into decentralized apps. We make it easy to bring cloud computation to smart contracts by making payments cheap and payable with native tokens and other ERC 20 tokens. With the "pay as you go" feature, balance is billed on fulfillment which means, you pay for only what you want to use. With Cloudbeam, you can securely create API credentials for smart contract calls with our secret encryption tool. In addition to the above use cases as cloud provider for smart contracts, we've integrated other services in our marketplace for developers to chose and add to their smart contracts. How we built it We built Cloudbeam using the following Chainlink Tools: -Chainlink Functions -Chainlink Automation -Chainlink Price feed Using the recently released Chainlink Functions, we try to solve the difficulty in creating encrypted secrets that are to be used in the smart contracts. Stripping down the Chainlink Starter Kit, we designed and built a tool that helps developers securely handle (create, update & delete) environment variables for function calls and an SDK for easy integration into dApps. We built Cloudbeam into three (3) major parts: Platform as a service (UI)_: where you can create, top up and edit functions while also being able to handle, request and view those functions. Service Marketplace : where you can pick and select already built out services to integrate into your smart contract. With our marketplace, you can choose various available services to be connected to your smart contract with ease like Artificial Intelligence (AI), Insurance, Weather, Foreign Exchange etc. Software Development Kit (SDK) : for easy integration into an already existing web2 app or dApps. Cloudbeam consists of 3 major contracts, namely; The Paymaster Contract: handles payment for all functions, manages both automated and manual function calls. Registry Contract: new function calls are register A Client Contract These contracts help manage function calls. Using the Client Contract, you make requests. On request fulfilment, the information in the function request like the Request ID , Function ID , Response and Status , and even Time Stamp is saved on the smart contract. Challenges we ran into Given that Chainlink functions is still relatively new and our entire project is formed around it, we had to find novel ways to interact Accomplishments that we're proud of One of our greatest achievements during this hackathon was being able to actualize our idea and learn new concepts at the same time. What we learned In the process of building cloudbeam, it exposed us to the world of cloud computing and serverless architecture and it's importance in web2 and how you can bring it to web3 using Chainlink. What's next for Cloudbeam Bringing on more developers to expand the features of Cloudbeam Adding more functions services to our service marketplace. Integrating into web2 and web3 dApps <div