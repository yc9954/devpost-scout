---
slug: "insuredisruption"
url: "https://devpost.com/software/insuredisruption"
title: "Disruptive Insurance"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 714
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/geospatial"
---

# Disruptive Insurance

> Volcano insurance hybrid smart contract. No other insurance business on Earth offers volcano eruption insurance.

[Devpost](https://devpost.com/software/insuredisruption) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[finance_payments]]
**substrate** [[geospatial]]

**stack** bootstrap, chainlink, filecoin, hardhat, ipfs, javascript, metamask, react, solidity, web3.js

## How they structured the write-up

- volcano insurance 🌋
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for disruptive insurance

## Body

Volcano Insurance 🌋 Inspiration Did you know that volcanoes cause $1 billion dollars in property damage every year? It is also estimated that 41,000 homes have been destroyed from volcanic eruptions. Generally, volcano insurance is not covered. If it is covered, you have to "Trust" the insurance company will hold up your claim. Disruptive Insurance upholds "Truth" and fairness with volcano insurance on a hybrid smart contract. What it does The contract owner sends ETH to the insurance contract. Anyone with a Metamask wallet can buy an insurance policy which is then tied to their address, defined by their coordinates and the date they purchased the policy. One ETH sent to the contract is then locked for the policy’s duration [1 year] to be paid out in the event a claim needs to be made. If a volcano erupts within 1 coordinate point from the policy holder’s location before the expiration of the contract, the holder can then claim the ETH that was initially locked to their policy as their insurance payout. However, if the policy expires without a relevant volcano eruption, the contract owner can claim the ETH that was locked to the policy. Owners can remove ETH they added to the contract if a policy isn’t tied to it as a savings account. Owners can even claim ETH from self destruct attacks! How we built it Our insurance product is implemented on Ethereum’s EVM smart contract platform with Solidity, Hardhat and Rinkeby testnet supporting contract development and deployment. The frontend, where users can interact with the contract, is built using ReactJS and Web3 and is served using Fleek IPFS and GitHub pages. Challenges we ran into Integrating React and Metamask together for accessing smart contract functions presented some difficulty. We first discovered that the layout for setting up Web3 is different from jquery and vanilla javascript. After reading some documentation, we were able to enable Web3 in the browser. The Ethereum request format was virtually the same with setting parameters such as: from,to,data and value [Metamask calculates gas price and limit for us]. Spurious Dragon contract file size limit warnings were an issue. We reduced contract file size by importing libraries for converting values and combining "require" logic with AND masking multiple values at once. During testing, we had to figure out how to do Unit tests with oracle API values and other external functions [Owner and Buyer were isolated]. We used mock functions to emulate expected oracle API values and set other values external to the current test. Accomplishments that we're proud of Creating a smart contract which connects to real world API data which solves a problem in the insurance industry. Collaborating as an international team who met online to build a fullstack decentralized application powered by smart contracts! What we learned Hardhat Integration and Unit testing is important before production Fullstack Web 3.0 fundamentals Teammates can discover details and explain new concepts which can improve a project. What's next for Disruptive Insurance Currently, policy prices are static which doesn’t account for risks of eruption based on the buyer’s location. We need to create a calculation to vary the price and payout of the policy. Also, adding different policy terms is more in line with insurance industry standards and buyer expectations. Our team would like to explore the idea of an idea of NFTs as proof of ownership in the context of our insurance policy. For the sake of this hackathon, we decided to go with mappings which we are all more familiar with. However, if we could issue a fully onchain NFT with policy data in the metadata signed by the contract owner, the ownership of that policy could be validated by the presence of that NFT in the wallet of the sender. This has the potential to reduce contract bloat and improves sovereignty of the policy holder. We also had the thought that automating policy payouts to the buyer in the event of volcanic eruption or expired policy claims of locked ETH to the contract owner would make a more complete product. To do that, the contract will need to stay updated on volcanic eruptions as well as perform some comparisons against the locations of current policies. Chainlink Keepers and possibly The Graph could help with this. <div