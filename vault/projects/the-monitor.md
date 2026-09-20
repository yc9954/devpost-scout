---
slug: "the-monitor"
url: "https://devpost.com/software/the-monitor"
title: "The Monitor"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 765
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# The Monitor

> The Monitor keeps an eye on your address to check if you receive staking rewards. Deposit some ETH, set your order, and it will automatically swap a "mirror" amount of your rewards for DAI.

[Devpost](https://devpost.com/software/the-monitor) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** brownie, chainlink, chainlink-keepers, chainlink-price-feeds, covalent, ethereum, ethers.js, fleek, keepers, moralis, next.js, solidity, web3uikit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the monitor

## Body

The Monitor - User Interface The Monitor - Logo Inspiration The idea from The Monitor comes from the fact that in some countries, staking rewards are taxed as income as soon as they are received, even if not cashed out. We therefore created The Monitor to protect stakers from the volatility of the market and make sure the taxman gets his dues. What it does The Monitor keeps an eye on your address to check if you receive any staking rewards. Deposit some ETH or other main network token, set your order, and The Monitor will automatically swap a "mirror" amount of the staking rewards you receive for DAI (more tokens coming soon). This way, you can sleep easy knowing that a portion of your staking rewards stays tucked away in a stable coin, that you can withdraw from our contract whenever you want! Pretty neat isn't it? The Monitor also keeps an history of the swaps it performs on your behalf, to help with your bookkeeping and, God forbid, tax records. How we built it Inspired by Patrick Collins's 16 hours solidity course, we used Brownie to develop the smart contract, and tried to write as much tests as possible. We also made use of Chainlink's Keepers and Price Feeds for our main feature. We implemented the swaps that The Monitor performs on behalf of our users using Uniswap V2's SwapExactEthForTokens function . Finally, we use the ABDK64x64 math library for the most challenging divisions we had to make in our contract. For the front-end, we used Next.js and tailwindcss . For the Web3 elements, we made use of Moralis react hooks , Web3UIKit , and Covalent to fetch our users' swap history. The front-end gets deployed automatically on IPFS using GitHub CI through Fleek . Challenges we ran into This was our first real Web3 project, and we had a lot to figure out to ensure that everything works properly (in particular, the call to Uniswap V2's swap function). Some of the maths in the contract, and in particular the fact that fractions do not really exist in solidity, were quite challenging, and allowed us to discover libraries such as ABDK64x64. Finally, we learnt a lot about gas optimisation when trying to perfom most of the costly operations in memory instead of using storage variables. We still have two non-breaking pending issues ( here and here ) with our tests and use of ABDK64x64 Math library that we haven't managed to figure out yet: any help is appreciated! Accomplishments that we're proud of We're very proud of having managed to create a functional dapp that, once audited, could eventually be deployed on a live network and provide some utility to the community. We are also proud of our front-end, which we think looks quite good and responsive, and of our history feature, which makes use of a decentralised infrastructure such as Covalent. Overall, we think that our dapp is actually quite decentralised, as it functions without a centralised back-end: All the important logic is in the contract, and even our front-end is deployed on IPFS, a decentralised infrastructure. Ade and myself didn't know each other, and met for the first time on Discord at the beginning of the Hackathon. We are very proud of how fruitful and productive our collaboration has been, despite both of us having full-time jobs. What we learned As mentioned earlier, this was our first real Web3 project, and it allowed us to discover and overcome the challenges that come with developing decentralised applications. I personally learnt that I love developing for Web3, and I look forward to keeping working on The Monitor in the future, hopefully with Ade, and on other projects (I have a few ideas in the pipeline that I would love to implement). What's next for The Monitor Eventually, and when Chainlink is ready on that network, we would like to deploy The Monitor on Moonbeam, which is our target network. Before this happens however, we would like to change the way The Monitor detects staking rewards transactions: Ideally, we would like to listen to staking reward distribution events using a technology such as Subquery , removing the need to check balance changes on our users' addresses. Another feature we would like to add is an "accumulation" function, which would trigger a swap only when a user has accumulated a certain amount of staking rewards. Finally, we would like to allow our users to set up swaps to more tokens than DAI, and add the possibilities to swap rewards for LINK or other tokens. <div