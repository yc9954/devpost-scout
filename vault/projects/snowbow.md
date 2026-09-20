---
slug: "snowbow"
url: "https://devpost.com/software/snowbow"
title: "Snowbow"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 591
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Snowbow

> On-Chain Snowball, For Higher Yields in Volatile Market Environments

[Devpost](https://devpost.com/software/snowbow) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

  <sub>weak: revocation_withdrawal, simulation_digital_twin</sub>

**stack** chainlink, foundry, nextjs, openzepplin, react, solady, solidity, thegraph, thirdweb, typescript

## Body

Hom Page Select Product Buy bullish snowball Check portfolio Inspiration The inspiration behind our project stems from the success of snowball structures in the traditional financial world. Snowball products have been highly popular among financial institutions, with BNP Paribas issuing the first recorded snowball structure product in the United States in 2003. These structures gained popularity due to their attractive features and high yields. Furthermore, some cryptocurrency exchanges (CEXs) have introduced snowball products in the crypto space. In the DeFi ecosystem, there is a clear market opportunity for on-chain snowball products. Therefore, we were inspired to design and create a secure and high-yield on-chain snowball product for DeFi users. Learnings Throughout the development of our project, we have gained significant insights and learnings. Firstly, we learned about the design of snowball products, their underlying mechanisms, and the principles behind the generation of returns through the hedging strategy. We also delved into the challenges and considerations of implementing snowball products in a decentralized environment. Additionally, we learned how to leverage ChainLink's Automation and Price Oracle to obtain accurate price data from various sources. This allowed us to effectively monitor and assess the status of the snowball product. Overall, we are proud to have deepened our understanding of snowball products and successfully implemented them in the DeFi world with a focus on security and openness. How we built it Our project is built on the foundation of three essential smart contract modules: price data retrieval and product status determination, strategy contract for user deposits and withdrawals, and automated hedging contract for generating returns. Additionally, we designed a user-friendly and intuitive UI targeting DeFi investors. To ensure the reliability and robustness of our project. We utilize Solidity and Foundry for writing, testing, and deploying contracts. We employ Chainlink Data Stream to obtain accurate asset prices to correctly alter the knock-in and knock-out states of our snowball products. Chainlink Automation is used to ensure the timely execution of observing and hedging the underlying asset prices. We use The Graph to monitor on-chain events and provide interfaces to the frontend. For creating user interfaces, we use React, Typescript, and ThirdWeb. Challenges The main technical challenge lies in thoroughly considering all the various scenarios of the product. Since the actual asset's product price does not change too rapidly in the short term, to conveniently simulate the various states of the snowball product, we manually mock data on the blockchain for testing purposes, which has taken up a considerable amount of our time. Before the production product launch, it is necessary to conduct multiple backtests using historical blockchain data, which will again be a substantial amount of work. Accomplishments that we're proud of We made a fully on chain and decentralized snowball finance product where not only the purchase and settlement are conducted on-chain, but also the price checks and risk hedging are carried out on the chain. What's next for Snowbow Our project exists in the form of a simple demo. However, there are several areas that require further development and refinement. Firstly, we aim to explore how to integrate a series of incentives to achieve a successful cold start for the product. Additionally, we envision the possibility of constructing different variations of snowball products, such as step-down snowballs and out-of-the-money (OTM) snowballs. Furthermore, we anticipate challenges in evaluating the performance of our theoretical hedging strategy in real market conditions. We view the hackathon as the first milestone in the journey of our project, and we are excited to embark on building a more ambitious future. <div