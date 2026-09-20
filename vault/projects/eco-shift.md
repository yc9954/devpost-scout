---
slug: "eco-shift"
url: "https://devpost.com/software/eco-shift"
title: "EcoShift"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 729
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/financial_record"
---

# EcoShift

> EcoShift provides crypto wallets with ethical rules built in. EcoShift wallets bring together communities with shared values by incentivising community-aligned transactions.

[Devpost](https://devpost.com/software/eco-shift) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[civic_government]] [[climate_energy]] [[disaster_emergency]] [[finance_payments]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** brownie, chainlink, polygon, python, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for eco shift

## Body

Inspiration Until now we have looked at money as ‘value-neutral’. A bitcoin doesn’t care if it is donated to an orphanage, or if it is used to fund terrorism. In short a bitcoin lacks ethics and values, as has all money in the history of civilisation. We challenge this idea by providing wallets that have ethical rules built in. These types of wallets can bring together communities with shared values and incentivise collective action. Each user signals their values in a way that is automatically backed by tangible contributions to the community. For this hackathon we applied this idea to the problem of climate change. Climate change is already impacting all of our lives, around the globe. We are seeing more extreme weather patterns, raging wildfires, rising sea levels are all effects of climate change that have become much too real over the past year. We believe that ethical wallets can be a major part of the fight against climate catastrophe. What it does We created EcoShift, EcoShift allows users to mint an EcoWallet, which is an NFT that functions as a crypto wallet. EcoWallets reward transactions that benefit the environment and reduce the impact of transactions that hurt it. EcoWallet users are each assigned a rank (1-5, 1 being lowest). Different ranks correspond to different levels of contribution. You move up the ranks by spending money in the EcoWallet community and spending money with climate-conscious addresses, which are “whitelist” addresses as voted by the community. EcoWallets incentivise the use of money in a way that aligns with the community’s values by requiring anyone sending money to non-whitelist accounts to also donate to climate change charities and organisations How we built it We wrote the EcoShift smart contract in Solidity and used Chainlink oracles to update the community whitelist according to external data. We used brownie for testing and deploying the contracts. To store the NFT media associated to each wallet, we used nft.storage . Similar to the Ethereum Name Service, an EcoWallet is identified by a human-readable name like "mywallet.eco", and its numeric ID is obtained from the namehash. The smart contract was deployed to the Polygon Mumbai Testnet and can be found at the address 0xDF2D882C2130bb1421eE419F75eb051e7057888e. Challenges we ran into It was a challenge to come up with an idea that uses NFTs in a novel and innovative way that achieves our idea of community and social action. It was the first smart contract many of our team members had developed. Figuring how to create the smart contracts and the necessary functions for our idea to work took some time. Eventually, we were able to get a working product that can execute our idea of having a wallet that encourages positive communities and social movements. We quickly realised how difficult it is to design incentives for end users. We had to find a way to reward the actions of those who are willing to take part in a social movement. With these rewards, we can continue to gather support for the community from individuals to create a larger collective action for a social cause. What we learned We learnt how to build smart contracts and take into account how their incentives will impact user behaviour. We also learnt how to test smart contracts and make use of oracles. What's next for Eco Shift In the future, we envision EcoShift having a significant impact on public policy. EcoShift could offer a new non-political, economic means whereby citizens could shape and improve the character and public policies of their societies. A nation’s political leaders might think twice before investing in products that harm the environment if it knew that a significant portion of the nation’s liquid assets were held in EcoWallets. Here are some of the improvements we will be making: Better UI Scope for more communities A voting mechanism that allows EcoWallet holders to vote on who is on the whitelist. This is likely to be a DAO A payment system that is integrated into mobile operating systems. This is so that people can use eco wallets just like they would a credit card Brainstorming around how we can make EcoShift make a bigger difference right now More incentives for people to keep money in the EcoShift ecosystem. The more money in the system the more powerful the community becomes and is able to affect positive change. <div