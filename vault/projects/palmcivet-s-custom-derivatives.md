---
slug: "palmcivet-s-custom-derivatives"
url: "https://devpost.com/software/palmcivet-s-custom-derivatives"
title: "Palmcivet's Custom Derivatives"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 526
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
---

# Palmcivet's Custom Derivatives

> Deploy custom derivative contracts to any chain, speculating on any underlying asset, with any collateral asset.

[Devpost](https://devpost.com/software/palmcivet-s-custom-derivatives) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**user** [[developer]]

**stack** arbitrum, automation, avalanche, ccip, chainlink, data-feeds, data-streams, foundry, next.js, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for palmcivet's custom derivatives

## Body

Inspiration Derivatives agreements have long been a popular investment vehicle and potential usecase for smart contracts. New Chainlink products such as CCIP and Data Streams enable us to build next generation implementations of these agreements, allowing users to take full control of their own derivatives by specifying all of the relevant parameters. What it does This project allows users to deploy custom derivatives contracts to their chain of choice, speculating on their asset of choice, with any collateral asset. The deploying user will also specify the amount of the collateral asset, the settlement time, the strike price and their long or short position. Anyone can participate as a counterparty by depositing the same amount of collateral and taking the opposite position. When a new derivative contract is deployed, it is automatically registered with Chainlink Automation which is used to facilitate the settling of the contract, comparing the strike price to the actual price of the underlying asset and paying out the total collateral (minus 2% developer fee) to the party with the winning position. The contract can be cancelled if both parties agree and the settlement time has not been reached, allowing them to each withdraw their full collateral. If one party deposits but the other doesn't, the depositing party can withdraw their full collateral when the settlement time has been reached. How we built it The project was built using Foundry, and features two versions - V1 for Data Feeds and V2 for Data Streams. A Derivative Factory contract is used to deploy the custom derivative contracts. The factory contract registers the deployed custom contracts with Chainlink Automation. CCIP is used in V1, allowing users to deploy to their chain of choice with a Factory Sender contract that sends instructions to a Factory Receiver contract on the chain of choice. Challenges we ran into Originally I intended to build the contract with CCIP and Data Streams. At first I was under the impression Data Streams test usage was restricted so I built V1 with Data Feeds in its place. When I found out Data Streams was available for general access on testnet and built the version with that, I realised that the only chain Data Streams was available on was not a CCIP compatible chain. That's why there are two versions. Accomplishments that we're proud of I'm extremely proud of having built a project that deploys custom contracts across chains with CCIP and registers them with Automation all in one Tx. What we learned During the development of this project I learned how to programmatically register contracts with Chainlink Automation directly from a smart contract and how to use Chainlink Data Streams to retrieve the price of an asset and use it in my contract. I also learned how to use Chainlink Log Trigger Automation, but ended up using Custom Logic Automation which I felt was better suited for this particular usecase as I needed the automation based on a certain time being met. What's next for Palmcivet's Custom Derivatives The next thing I want to do with this project is integrate CCIP with the Data Streams version as soon as that is available. <div