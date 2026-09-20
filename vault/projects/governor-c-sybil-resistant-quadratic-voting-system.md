---
slug: "governor-c-sybil-resistant-quadratic-voting-system"
url: "https://devpost.com/software/governor-c-sybil-resistant-quadratic-voting-system"
title: "Governor C: Sybil-Resistant Quadratic Voting System"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 517
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Governor C: Sybil-Resistant Quadratic Voting System

> Fair election is important for DAO. However, the most developed system, Quadratic Voting, is exposed to the sybil attack. We develops Governor C which is sybil resistant QV based on Chainlink-VRF.

[Devpost](https://devpost.com/software/governor-c-sybil-resistant-quadratic-voting-system) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[civic_government]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** bootstrap, chainlink, javascript, metamask, polygon, python, react, recoil, solidity, truffle, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned
- challenges we ran into
- what's next for governor c: sybil-resistant quadratic voting system

## Body

Overview of Governor-C system Service Example Inspiration Recently, DAO emerged as the innovative organization system for the healthy community governance. This is the new governance system for the Web3 ecosystem. DAO services like Snapshot and Tally help more people to build decentralized community. The key for building successful DAO is making fair governance system, and improved voting system can help it. Quadratic voting method which make cost of purchasing tickets increases exponentially has emerged to compensate for the weakness of 'one dollar one vote' and 'one person one vote'. However, this method is also exposed to the risk of Sybil attack. Team DAppO would like to suggest improved voting system smart contract 'Governor C'. It is a fully decentralized sybil resistant quadratic voting system based on Chainlink VRF. We are going to release this smart contract as a scalable open source for the further DAO ecosystem activation. What it does The goal of this project is activate the whole decentralized DAO ecosystem. For doing it, we create and built three novel things: Probabilistic Quadratic Voting Smart contract Governor C that embodies PQV Example of service using Governor C How we built it Probabilistic Quadratic Voting Junmo Lee, Sanghyeon Park, and Soo-Mook Moon. "Secure Voting System with Sybil Attack Resistance using Probabilistic Quadratic Voting and Trusted Execution Environment." KIISE Transactions on Computing Practices 27.8 (2021): 382-387. Make it always a loss to do sybil attack by applying probabilitic element on quadratic voting. In PQV, splitting voting power makes the expected value of voting power lower that executing 1 voting power. QV and PQV shows high similarity through simulation. Also PQV's sybil resistance has been proved. Governor Charlie To implement the probability factor of PQV without compromising decentralized manner, we use Chainlink-VRF. The contract receives random number every time user cast a vote and this will make contract more decentralized and cost-efficient. It follows Compound governance module standard. Therefore current DAOs using compound module based on Governor Bravo can easily apply our new solution which is developed under the same standard. Example of DAO Service A demonstration of the bundle of Governor C contracts. We use Polygon (MATIC) to enhance scalability of application by using blockchain with lower fees and higher speed. What we learned How to use Chainlink VRF Necessary technical stack to build scalable blockchain service Concept of Polygon (MATIC) Blockchain Challenges we ran into But we overcame them! Calculating complex fractional number operation with some restriction such as integer only in Solidity Calling a random function efficiently and frequently to calculate probability Developing UI/UX with complex contents with many states effectively Distinguishing/processing state when request and response are not atomic like random value request. What's next for Governor C: Sybil-Resistant Quadratic Voting System Upgrade Governor C to the next level We improved compound governance module Governor Bravo through PQV and Chainlink VRF. Going to study other methods to improve governance system. Expend the usage of PQV to other areas We developed a service applied Governor C on governance system. We wants to use PQV in several other fields like quadratic funding/ranking and quadratic attention payment. <div