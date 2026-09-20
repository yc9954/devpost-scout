---
slug: "comet-cross-chain-intent-centric-swap"
url: "https://devpost.com/software/comet-cross-chain-intent-centric-swap"
title: "Comet · Cross-chain Intent Centric Swap"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 590
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/security_privacy"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Comet · Cross-chain Intent Centric Swap

> Comet - Revolutionise cross-chain swaps. Decentralised, permissionless, and secure asset exchange across networks with Chainlink CCIP and Polygon LXLY, ensuring atomic transactions.

[Devpost](https://devpost.com/software/comet-cross-chain-intent-centric-swap) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[security_privacy]]
**substrate** [[financial_record]] [[web_dom]]
  <sub>weak: code_repository</sub>

**stack** fondary, node.js, react, solidity, typescript

## How they structured the write-up

- motivation
- current challenges & our solution
- our technical highlight
- how we built it
- challenges we ran into
- outcomes & proud accomplishments
- what we learned
- source code

## Body

Creating a Limit order Limit orders Diagram of the order flow Hint: Enable subtitles (CC) on the YouTube demo to improve your experience! Motivation Our team, through past experiences in learning blockchain, often encountered scenarios where obtaining a specific asset was necessary. While platforms like Cowswap and 1inch offer Swap and Limit Order features, they are limited to assets within the identical blockchain. Thus, we explored the feasibility of enabling seamless cross-chain asset swaps. Current challenges & our solution In our subsequent research, our team discovered three main challenges in cross-chain asset swaps: Asset safety: All bridges involve bringing assets cross-chain, which increases risk for the assets Centralised bridge and safety: Heavily rely on one bridge, which leads to the top hack in history Cross-chain arbitrage: Need to have assets in both networks After studying, our team believes these issues are solvable. Consequently, we decided to build a secure, permissionless cross-chain swapping platform. Our technical highlight Our solution is an Intent-centric swap platform, primarily distinguished by three prominent advantages: Asset safety: We only bridge messages, not assets, which significantly reduces hack vulnerability Decentralised bridge: We use multiple bullet-tested bridges such as Chainlink CCIP and Polygon LXLY to bridge messages only Permissionless taker: Anyone could settle any order in any amount, which dramatically increases the flexibility for cross-chain assets Leveraging CCIP and LXLY, we facilitate seamless cross-chain swaps by bridging messages in an atomic manner. This breakthrough minimises barriers to cross-chain asset swaps within the ecosystem, enhancing overall efficiency. The following diagram indicates the main technical detail in the order flow of our website. How we built it To achieve the desired functionality, we crafted three innovative smart contracts, four interfaces, and numerous functions using the classic Solidity language in Web3 development. These components collectively form the core backend logic of our solution. Regarding the user interface, we started with the front end of the existing open-source platform Cowswap, making numerous enhancements and introducing new interactive elements essential for cross-chain transactions. The result is a visually appealing and user-friendly interface with seamless logic. Challenges we ran into Our journey involves conquering frontend challenges to harmonise assets cross-chain and tackling backend intricacies by leveraging CCIP and LXLY bridges for flawless atomic transactions. These hurdles fuel our pursuit of a sleek and dependable cross-chain swapping experience, promising innovation and user satisfaction at every step. Outcomes & proud accomplishments We've successfully achieved all our set objectives, seamlessly delivering a cross-chain swap with four distinctive and standout features: Safe asset: As only the message got the bridge, not the asset, this would help make the swap less vulnerable to hackers. Safe bridge - As LXLY is the official bridge and CCIP goes through DON, it would be much safer and decentralised than the regular bridges. Partial fillable - Limit orders can be partially filled, which helps to fill orders much quicker. Permissionless and intent swap - Anyone could be a taker to fulfil any amount of assets on-chain with whatever liquidity they have. What we learned While developing this software for the Chainlink Hackathon, our technical journey unveiled vital insights. On the front end, we fine-tuned our proficiency in state loading and promise callback, enhancing the dynamism of user interfaces. Meanwhile, on the backend, our successful implementation of Fondary for scripting laid a robust foundation for seamless software execution. The technical advancements in smart contracts underscored the innate advantages of Chainlink, particularly in securely transferring data for smart contracts and seamlessly integrating real-world inputs into blockchain functionality. Source code Smart contract repo Website repo <div