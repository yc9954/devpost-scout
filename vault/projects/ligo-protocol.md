---
slug: "ligo-protocol"
url: "https://devpost.com/software/ligo-protocol"
title: "Ligo Protocol"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 395
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/housing_homeless"
  - "domain/transportation"
---

# Ligo Protocol

> A protocol for car sharing agreements.

[Devpost](https://devpost.com/software/ligo-protocol) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[housing_homeless]] [[transportation]]

**stack** chainlink, docker, filecoin, ipfs, moralis, node.js, postgresql, react.js, shell, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ligo protocol

## Body

Architecture Inspiration Blockchain is the future for integration among trustless parties working together. Similarly, the car rental industry is one of such businesses that involve multiple parties working together. The Ligo protocol is aimed to build a decentralized car sharing infrastructure that can bring decentralization and transparency to solve existing car sharing problems like disputes among renters and the owner. What it does The Ligo Protocol introduces infrastructure and solutions for the decentralized car sharing system for transparent car rental agreements with the help of vehicle information like odometer, latitude and longitude, etc. How we built it The solution consists of following parts: 1) Ligo Node. The backend of Ligo contains authorization and external adapter(EA) for the Smartcar API. Auth token management is done using Moralis for storage. 2) Chainlink Node. The Chainlink Node acts as bridge between EA and the Ligo Smart Contracts. The Chainlink Node has Jobs to get API data. 3) Ligo Smart Contracts Ligo Smart Contracts have rental agreements for vehicle owner and renters with the data from EA through Chainlink Node. 4) Ligo Client App. The UI is built on React.js. The client uses Web3.storage to store vehicle information on IPFS and Filecoin for others to view. Challenges we ran into 1) Chainlink uses Operator.sol for multi-variable responses 2) When we declare the jobid as bytes32, smart contract automatically converts JobID to real bytes data because program sees that it is a string. and the real bytes32 is 0x363…(JobID). Accomplishments that we're proud of During the hackathon we: Created the backend with External Adapter for Smartcar API authorization Tested, deployed and implemented the smart contracts Developed UI Created the scripts to configure the CL nodes, jobs, and EA What we learned How to run and manage the CL node. How to manage the jobs. How to manage an external adapter. How to integrate API in smart contract How to test and deploy smart contract How to store data on Filecoin using Web3.storage How to use Moralis user management and storage How to use the SmartCar API What's next for Ligo Protocol Our initial goal was to create rental agreement and solve one of the common disputes. So our further steps will be: Investigate how to handle more complex agreements Investigate how to store as much agreement data off-chain as possible to lower cost and preserve privacy Many security improvements <div