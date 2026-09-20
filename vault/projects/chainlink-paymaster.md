---
slug: "chainlink-paymaster"
url: "https://devpost.com/software/chainlink-paymaster"
title: "Chainlink Paymaster"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 448
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
---

# Chainlink Paymaster

> Connecting zkSync Native Account Abstraction with Chainlink Price Feeds

[Devpost](https://devpost.com/software/chainlink-paymaster) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** chainlink, ethers, solidity, vue, zksync

## How they structured the write-up

- erc20chainlinkpaymaster
- what it does
- problem being solved
- how i built it
- accomplishments that i'm proud of
- what's next for chainlink paymaster

## Body

ERC20ChainlinkPaymaster This smart contract is a zkSync Paymaster for connecting the innovation of zkSync Native Account Abstraction with the ease and security of Chainlink Price Feeds . What it does This Paymaster allows users to pay their gas fees using ERC20 tokens of their choice. It leverages zkSync’s native implementation of account abstraction and Chainlink’s price feeds on the zkSync era Sepolia testnet to convert gas fees in ETH to different ERC20 tokens such as LINK and USDC. Problem Being Solved Traditional blockchain models require users to pay gas fees in the network's native cryptocurrency, such as ETH on Ethereum. This creates several issues: User Inconvenience : Users need to manage multiple cryptocurrencies. If they primarily use ERC20 tokens like USDC or LINK, they must also hold ETH for gas fees, complicating the user experience. Barrier to Entry : New users may find it confusing and discouraging to understand why they need a different token (ETH) for transaction fees, which can hinder adoption. Liquidity Issues : Users may not always have ETH available, requiring them to acquire it, often incurring additional fees and dealing with price volatility. Allowing gas fee payments in ERC20 tokens addresses these problems by: Enhanced User Experience : Users can pay fees with the same tokens they transact with, reducing the need to manage multiple cryptocurrencies. Lower Barrier to Entry : Simplifying fee payments encourages new users to engage with blockchain applications. Improved Liquidity Management : Users maintain liquidity in their preferred tokens without needing to convert to ETH. Using Chainlink’s Price Feeds ensures accurate and reliable price data for converting gas fees, enhancing the reliability and fairness of the process. This solution makes blockchain technology more accessible and user-friendly, benefiting both users and developers. How I built it The ERC20ChainlinkPaymaster.sol contract is written in Solidity and deployed using the Atlas IDE. A simple Greeter contract and Vue.js front-end application are used to demonstrate this Paymaster. The Chainlink Data Feeds are used both off-chain and on-chain to determine how many ERC20 tokens are required. Accomplishments that I'm proud of As it was my first time working on a zkSync paymaster, there was a lot to learn and I faced several challenges implementing the Chainlink Data Feed into it. In the end, it was a great learning experience and has gotten me hooked to zkSync and Chainlink blockchain development. I will be shifting some of my dApp projects onto zkSync and experiment more with its Native Account Abstraction technology. What's next for Chainlink Paymaster This Paymaster can be easily implemented into all sorts of different dApps to bring a better user experience. I'd like to expand and add support to other tokens as well. <div