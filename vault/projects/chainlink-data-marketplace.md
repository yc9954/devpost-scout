---
slug: "chainlink-data-marketplace"
url: "https://devpost.com/software/chainlink-data-marketplace"
title: "Chainlink Data Marketplace"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 636
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Chainlink Data Marketplace

> Our project is a decentralized marketplace that aims to connect chainlink node operators with developers/projects seeking access to data on chain.

[Devpost](https://devpost.com/software/chainlink-data-marketplace) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** chainlink, ethersjs, polygon, quicknode, rainbowkit, react, remix, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- smart contracts (polygon [mumbai])
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chainlink data marketplace

## Body

Data Marketplace Github repo: https://github.com/Robert-H-Leonard/data-marketplace Inspiration After setting up a node, one must find users who need off-chain data to earn LINK. Developers who need off-chain data brought on-chain have no place to go to make their request except directly in discord. Node operators have no place to go to monetize their data on-chain. The data marketplace serves to connect the 2 parties to enable a rich on-chain data ecosystem. What it does A marketplace where anyone can request specific data (such as the price of 1kg of gold) they would like on-chain. Chainlink node operators can submit bids detailing the fee required for getting the data, their oracle address and the jobId that can be used to retrieve the requested data. Once node operators submits bids to a specific request, the wallet which created the request can pick which bid to accept. When a bid is accepted this will trigger the conditions for our automation contract to trigger the validation (attempting to fetch data from the node operator) of the oracle address and jobId in the accepted bid. If the node operator returns the correct data the request is set to validated and the oracle address, jobId and fee is displayed for anyone to be able to use. How we built it Solidity smart contracts (Deployed on Mumbai) Chainlink Automation Chainlink node Frontend( Etherjs, Quicknode, Rainbowkit) Smart Contracts (Polygon [Mumbai]) JobRequest.sol : Smart contract that acts as a data store for the app + an oracle client to validate node operator jobs: https://mumbai.polygonscan.com/address/0x4B464136CCBb709E1b238E00e8C40975C6A32e8c Automation.sol : Smart contract used to trigger validation of accepted node operator bids: https://mumbai.polygonscan.com/address/0x7E954307CB634B1885c3b0cFdB0e359f09E7dbF6 https://automation.chain.link/mumbai/79616312988537092179866366291075391444640142700716884656781977912678455043062 Challenges we ran into Smart contract design: It was more challenging than we initially thought to figure out how our automation contract would interact with our data store contract. We eventually figured out that a custom logic automation was what we needed. We attempted to use json validation on chain from the response of a node operators job but weren't able to figure out a good way to do it on-chain. Accomplishments that we're proud of Designing a marketplace to connect node operators with developers who need data on chain : Even though it is a proof of concept we are excited we were able to design and build a marketplace app where the state was managed 100% on chain. Designing a solution to a real need with Chainlink technology : Once we were able to get the automation working we were able to really understand how it can be used as a tool across many different problem domains What we learned Setting up and running a chainlink node Problems / application designs that chainlink automation can be used to solve The difficulties of parsing json on-chain How to build smart contracts that are oracle clients Overall increased knowledge of solidity programming / deployment What's next for Chainlink Data Marketplace The next version of the JobRequest.sol contract isn't a complete oracle client. We want to finish implementing the oracle client so we can programmatically validate jobs submitted in bids by node operators Right now the JobRequest.sol contract validated the responses from node operators on-chain. This is an issue because parsing json on-chain is very expensive and inefficient. We want to implement an external adapter to validate the json responses off-chain. This would allow us to programmatically validate much more complex data from node operators In the app users requesting data can only request single fields in data they want. We want the add the ability to users requesting data to be able to specify multiple fields they want in a json response. In order to incentivize node operators to be good actors we want to build a profile reputation system (similar to something like Upwork) and reward node operators that provide quality data and data avalibility <div