---
slug: "defund"
url: "https://devpost.com/software/defund"
title: "DeFund"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 507
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
---

# DeFund

> DeFund (DEcentralized FUNDraiser) is a platform for organizing fundraisers for all types of causes.

[Devpost](https://devpost.com/software/defund) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]

**stack** chainlink, ethereum, filecoin, moralis, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for defund

## Body

Inspiration We're already starting to see first signs of global economic downturn and there are fears of a global recession. As a result we'll see more people falling in financial trouble. However, we've seen tremendous generosity from people donating to all kinds of causes on platforms like GoFundMe or giving micro loans on Kiva.org. Blockchain technology is still often associated with vanity, gambling and "get rich quick" schemes, but we strongly believe it has a huge potential to make positive social impact. What it does Anyone can use DeFund to create a fundraiser - either accepting singular donations from others, or allowing donors to set up recurring payments. How we built it The core of the platform is a factory smart contract responsible for coordinating all fundraisers, donations and recurring payments. The system was build with modularity in mind, supporting more than one type of fundraiser. Every fundraiser is a separate instance of a smart contract, independent of the factory (coordinator). Recurring payments are triggered by Chainlink Keepers. The web3 frontend uses Moralis for interacting with the smart contracts, as well as Web3.Storage to store fundraiser updates and media on Filecoin/IPFS. Challenges we ran into We had so many ideas for cool features we had really hard time choosing which ones to implement as part of the MVP. Many had to be shelved due to time constraints. Accomplishments that we're proud of The platform is fully functional and we really hope it'll be a good demonstration of positive social impact this technology can make. What we learned None of us are experienced blockchain/web3 developers, so it was a learning experience for sure. But in the end we've learned that thanks to a rich ecosystem of tools and services, building web3 dApps is not as hard as it may seem :) What's next for DeFund We have a ton of ideas for further development and features. Just to list a few: Micro loans similar to Kiva.org (which we love!) BrightID "proof of humanity" integration to minimize potential for fraud and highlight fundraisers run by real people in need. NFT reward pool - donated NFTs distributed randomly in raffles among highest ranking donors. The more you donate to verified fundraisers - the higher chance of winning! Reputation system for users - used by microloans, for which there will be no collateral. Kiva shows people tend to pay back despite no collateral, but loan takers there are vetted by local NGOs. We need a trust minimized system for that! Auto-donations - if you don't want to browse all open fundraisers, you can set how much you want to donate from your wallet and an algorithm will auto-donate based on donations of other (reputable) users of the system. Accept donations in multiple different coins / tokens - use Chainlink price feeds to recalculate value. Manage DeFund factory via a DAO Potential commercial aspect - recurring payments (like Patreon) for content creators, open source library maintainers etc. DeFund will never charge commission on fundraisers, but could charge it for commercial payments. <div