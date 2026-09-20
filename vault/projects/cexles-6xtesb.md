---
slug: "cexles-6xtesb"
url: "https://devpost.com/software/cexles-6xtesb"
title: "Cexles Finance"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 681
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/financial_record"
---

# Cexles Finance

> CEXLES is a fully decentralized EVM-compatible trading platform that provides a wide range of tools, familiar to CEX users, but totally on-chain.

[Devpost](https://devpost.com/software/cexles-6xtesb) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[finance_payments]] [[security_privacy]]
**substrate** [[financial_record]]

**stack** amazon-web-services, chainlink, golang, hardhat, nextjs, quicknode, react, slither, solidity, the-graph, typescript, uniswap, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Main page Order page User balance Inspiration The creation of the project was inspired by many recent events, such as collapses of exchanges, banks, stricter control and sanctions against many user groups. We also see a dramatic lack of such tools in the DeFi world, despite the fact that in centralized finance this area is very well developed. Taking into account the size of liquidity in DeFi, our tool will help thousands of users to manage their assets more accurately and safely, minimize risks and maximize profits. What it does The main idea of our project is to bring to the market the tools for convenient asset management, risk management for every DeFi user without any restrictions, as well as providing the usual tools for CEX users in a fully decentralized manner, without censorship and without giving full control over user funds to third parties. The TradingPlatform smart contract is responsible for validating the conditions and allows Chainlink Automation to execute orders. Chainlink Automation increases the reliability and decentralization of the entire application. Our project provides the following types of orders: Take-profit - Order that is triggered when an asset exceeds a price threshold, initiates profit taking, designed to replace an asset for profit. Stop-Loss - Order that waits for prices to dip below a stop price trigger, designed to swap out of the input asset to prevent losses. DCA(Dollar Cost Averaging) - Order that helps to buy an asset on a regular basis (e.g. every week for one month) and allows you to average the purchase price. Perfect for beginners. Trailing - Order in which the selling price of an asset is automatically adjusted upward as the market price rises, allowing investors to make a profit while allowing for potential further profits. When price falling back, after the target price, the trailing order fixes all remaining assets. How we built it The idea of this project came to us at the beginning of the year and we were thinking how to better implement the order execution part, how to do it in a decentralized and secure way. During the research we came to the conclusion that the automation from Chainlink is the most suitable solution. This technology makes our project fully decentralized and not dependent on any centralized power or vulnerability. Challenges we ran into In the process of creating the project we faced many challenges, many of which were taken into account in the planning and design phase, but during the implementation we had to make important decisions and change the implementation of certain components of our solution. One of the most interesting challenges we faced was a possible problem with execution of a large number of orders in one transaction because all orders may not fit into the gas limit of one automated transaction and also the probability of a transaction failure due to internal problems of one of the orders is growing. We have discovered a great solution and implemented our Load Balancer for Chainlink Automation and an approach for implementing contracts with possible problems of this kind. The idea of the load balancer is that it tracks the workload of the last created keeper and, if necessary, creates a new one, which will take over the new tasks. The most important advantage of this implementation is that keepers distribute the load automatically. Accomplishments that we're proud of We are proud to have implemented such a useful tool that is of benefit to any DeFi user. And also because we have developed an approach and load balancer for Chainlink Automation that will help many projects in the future implement their functionality without limitations. What we learned During the hackathon, we got a more in-depth understanding of the chainlink infrastructure. More than anything, we mastered Chainlink Automation and deeply integrated this service into our infrastructure. Automation allowed us to solve a non-trivial case without spending a lot of resources on reinventing the same functionality over months and years. It gave us the opportunity to dedicate invaluable time to the idea, user interface and functionality of the platform. <div