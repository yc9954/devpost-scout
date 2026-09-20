---
slug: "project-to-name"
url: "https://devpost.com/software/project-to-name"
title: "HashClaim - Gotta Claim Them All"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 538
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# HashClaim - Gotta Claim Them All

> HashClaim simplifies the management and claiming process for loyalty tokens. By using smart contracts, it allows users to claim their available rewards, view tokens in their wallet and swap tokens.

[Devpost](https://devpost.com/software/project-to-name) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]] [[geospatial]]

**stack** confluence, figma, fleek, hash-connect, hash-pack, hedera-js-sdk, hedera-mirror-node-rest-api, hedera-smart-contract, jira, material-ui, node.js, react, solc, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hashclaim - gotta claim them all

## Body

Inspiration The “loyalty rewards” ecosystem can be a frustrating process - You accumulate points in a variety of apps but you can’t always do much with them because your balance is too low or you’re no longer interested in the products/services the app offers. As a result, you end up with a bunch of loyalty rewards you don’t use, and this inspired the idea for HashClaim. What it does When a company wants to develop a loyalty program and they create a token, HashClaim will allow the company to create a reward in the smart contract instead of rewarding it directly to their users and handling the transfers. This reward can be assigned to a Hedera Account ID and the user will have the ability to open HashClaim deployed on fleek, connect to HashConnect, then claim and/or swap their rewards. The users account will be associated with the loyalty token and then the tokens will be sent. A user will also be able to set up their account ID to auto-claim any loyalty tokens in the future. How we built it We established a project roadmap in confluence and then created the project requirements in Jira. We built the admin scripts and the smart contract first using solidity and solc compiler, then built the dApp using React and Typescript, integrated HashPack wallet, and deployed it with Fleek. Simultaneously, we used Figma to map out the UI design. Challenges we ran into HashPack is not currently returning the transaction result responses as this functionality is not currently available. As a result, the wallet connection is delayed by several seconds as we are pulling transactions from the mirror node instead of directly from HashPack. We spoke to the HashPack dev team and they advised that this feature is estimated to be released soon. With Hedera, we had issues figuring out how the Hedera smart contract would act as the treasury for tokens created by another account. Also, the allowance of transfers is currently empty and isn’t reflecting on the account information although there are fields. Accomplishments that we're proud of We’re proud of… Developing our first dApp with HashPack, deploying on Fleek and using Hedera Smart Contracts. The alternative solutions we found for the challenges we faced. For example, for the transaction response issue we experienced with HashPack, we found the Hedera Rest APIs that could return the transaction results. Finding a UI designer to join the team to create an eye-catching design. What we learned We learned… To find an alternate way to decode results and get token details based on transaction results. How to use HashPack and Discord. About the Hedera SDKs and how to call the smart contract on Hedera. The difference between fungible and non-fungible tokens for our implementation What's next for HashClaim - Gotta Claim Them All We are excited to continue developing features for HashClaim such as the ability to claim NFTs, swap HBars and other currencies and add additional wallet options too. Our goal is to go live in Mainnet in Q4 2022 where we will also implement the donate to Ukraine feature. Also, we plan to apply for grants with the HBAR foundation in the following grant categories: DeFi Exchange Metaverse <div