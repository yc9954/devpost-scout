---
slug: "allbridge-stable-bridge"
url: "https://devpost.com/software/allbridge-stable-bridge"
title: "Allbridge Core"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 710
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
---

# Allbridge Core

> Allbridge Core enables users to transfer native stablecoin liquidity between Tron and various EVM/non-EVM chains via decentralized cross-chain messaging protocols with an additional privacy layer.

[Devpost](https://devpost.com/software/allbridge-stable-bridge) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**substrate** [[financial_record]]

**stack** node.js, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for allbridge core

## Body

Inspiration Allbridge officially launched back in July 2021. In our time of working on Allbridge, we have gained valuable experience in providing seamless cross-chain transfers. Since the mainnet launch, our users bridged over $6.2B by transferring assets between 14 supported networks . While the original bridge architecture supported both the native and wrapped types of transfers, the last couple of months clearly demonstrated the shift in the market tendencies toward the provision of native stablecoin transfers . In our latest product, Allbridge Core , we set out to create the ultimate bridge experience , enabling users to bridge stablecoin liquidity between both EVM and non-EVM networks by offering a convenient platform for native stablecoin swaps. Our particular focus on the Tron ecosystem allows us to tap into the largely underutilized market of TRC20 USDT by the existing products on the market. The new bridge architecture encompasses all of our previously acquired experience and focuses on solving the sore points in the cross-chain transfers by providing a simple and intuitive one-click bridge experience , connecting Tron with EVM and non-EVM networks. What it does Allbridge Сore enables users to transfer stablecoins in a fast, cheap, and trustless way by providing a native bridge that connects EVM and non-EVM chains via decentralized cross-chain messaging protocols with an additional privacy layer. In addition, the platform offers farming opportunities to the liquidity providers , who may leverage its advantages to supply single-asset liquidity in exchange for stablecoin rewards. How we built it The development began in mid-June , after the bridge architecture had been finalized. At first, we created an MVP of the new architecture for internal testing. We proceeded with outlining the UI of the Allbridge Core and designing it around the new stablecoin bridge . At the same time, we were working on developing our cross-chain messaging protocol for conducting native stablecoin transfers on Tron . It is our pleasure to showcase the result of our development process by presenting the test transfers between Tron and Ethereum in our demo video . Challenges we ran into One of the main challenges was developing a model enabling the support of the native stablecoin transfers at low slippage and ensuring that networks have sufficient liquidity to process the transactions. A lot of attention has been put into testing the functioning stable curve exchange model , which would balance out the exchange rates based on the size of the liquidity pools and reduce slippage. Moreover, Allbridge Core utilizes single-sided liquidity pools , facilitating cross-chain transfers of native liquidity by incentivizing the liquidity provision of native stablecoins on each chain. Accomplishments that we're proud of While certain messaging protocols are limited in their coverage of networks, we circumvented the issue by creating a flexible bridge architecture , enabling us to use any cross-chain messaging protocol on the market, thereby expanding the list of available chains our bridge may offer. We’ve also built an internal messaging layer , which allows us to complete the transfers of the native stablecoins between Tron and other supported networks. In addition, while most bridges currently require several steps to transfer assets from one network to another, Allbridge Core provides a one-click solution to move your stablecoin assets and offers a possibility to convert part of the transfer amount into the gas token . Lastly, the bridge will offer customized security levels ranging from password-protection to ZK transactions , allowing you to perform anonymous transfers. What we learned We learned more about designing a stable curve exchange and explored various cross-chain messaging protocols on the market. This experience has provided us with an opportunity to join the Tron ecosystem and contribute to its expansion by building a product that will enable more users to access Tron from various EVM and non-EVM networks. What's next for Allbridge Core Throughout the summer, we will work on finalizing the product and integrating more chains and tokens. When the bridge is thoroughly tested and deployed , the ability to upgrade the contracts will be disabled , as well as the admin access to ensure that the bridge remains non-custodial . We aim to release the Allbridge Core to mainnet this autumn and cross the $1,000,000,000 milestone in bridged volume by the end of 2022 . <div