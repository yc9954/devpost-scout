---
slug: "electroswap-electroneum-dex"
url: "https://devpost.com/software/electroswap-electroneum-dex"
title: "ElectroSwap - Electroneum DEX"
hackathon: "Electroneum Hackathon 2025"
organization: "Electroneum"
winner: true
words: 531
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# ElectroSwap - Electroneum DEX

> The first DEX on the ETN-SC with built-in liquidity locking to protect our users, yield farm to earn passive income, and ETN portfolio view and transaction history. Home of the $BOLT and $DYNO tokens.

[Devpost](https://devpost.com/software/electroswap-electroneum-dex) · hackathon [[Electroneum Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]]
**substrate** [[financial_record]] [[geospatial]]

**stack** ethersjs, mongodb, node.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for electroswap

## Body

Bolt Portal Swap Dialog Portfolio View Token List Token Details Yield Farm NFT Collection List NFT Collection Details NFT Asset Details NFT Bidding NFT Bid Management Inspiration The inspiration behind ElectroSwap was to create a decentralized exchange (DEX) that not only simplifies trading and liquidity provision but also addresses common issues that plague other platforms, such as impermanent loss and rug pulls. We aimed to build a secure, efficient, and user-friendly platform that can serve as a model for future DEXs on other EVM chains. What it does ElectroSwap enables users to trade cryptocurrencies, provide liquidity to earn fees, and engage in yield farming with impressive APYs. Key features include liquidity locking to enhance security, strict listing requirements to ensure only non-malicious token projects are highlighted, real-time transaction updates via our Telegram buy-bot, multi/cross pool routing for optimal trade execution, and user-friendly displays of charts and recent transactions thanks to a custom-built indexer. Additionally, users can now trade NFTs through our newly launched NFT Marketplace, built specifically for this hackathon! How we built it Our team utilized Solidity for smart contract development, integrating the time-tested Uniswap V2 and V3 liquidity protocols while developing groundbreaking custom features like an integrated liquidity locking mechanism and a yield farm to reward liquidity providers. We also built a custom indexer to convert raw blockchain data into accessible formats for an enhanced user experience, alongside a Telegram buy-bot to notify users of buy transactions. For our NFT Marketplace, we leveraged the well-established Seaport v1.5 protocol pioneered by OpenSea, bringing a robust and seamless NFT trading experience to the platform. Challenges we ran into Implementing the liquidity locking and yield farming features securely was challenging, as was optimizing the integration of Uniswap’s protocols on a new blockchain. Developing the custom indexer to handle vast amounts of data efficiently and creating a Telegram bot that provides timely updates also presented significant technical hurdles. Additionally, integrating the NFT Marketplace using the Seaport protocol required careful attention to ensure compatibility and performance on the Electroneum Smart Chain. Accomplishments that we're proud of We are particularly proud of our secure liquidity locking mechanism and the successful integration of our Yield Farm, both of which have been fully audited to ensure user funds remain safe. Our custom indexer aggregates multi-hop/multi-route swap transactions, significantly improving how transaction data and charts are presented, making trading activity more accessible and understandable. The launch of our NFT Marketplace stands as a major achievement, expanding ElectroSwap’s functionality and showcasing our ability to deliver innovative features under tight deadlines. What we learned This project deepened our expertise in blockchain data handling and real-time communication tools in DeFi platforms. We also enhanced our skills in smart contract security, NFT protocol integration, and user interface design, ensuring a seamless and secure user experience across both trading and NFT functionalities. What's next for ElectroSwap With the NFT Marketplace now live, we plan to further enhance its features and usability based on user feedback. Additionally, we’re exploring the possibility of a True Random Number Generator service for new projects on the Electroneum Smart Chain. These future developments aim to broaden our services and solidify ElectroSwap’s position as a comprehensive DeFi platform. <div