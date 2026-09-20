---
slug: "real-estate-derivatives-swap-amm"
url: "https://devpost.com/software/real-estate-derivatives-swap-amm"
title: "RealBlock"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 611
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/housing_homeless"
  - "substrate/financial_record"
---

# RealBlock

> A synthetic asset protocol and market maker for real estate derivatives

[Devpost](https://devpost.com/software/real-estate-derivatives-swap-amm) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[housing_homeless]]
**substrate** [[financial_record]]

**stack** chainlink, filecoin, ipfs, matic, polygon, quicknode, truflation

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for realblock

## Body

Inspiration 💶 Decentralised Finance (DeFi) has already shown use cases for cryptocurrencies, commodities, indices, stocks, and synthetic derivatives that can be represented on-chain as NFTs backed by real off-chain assets or collateralised synthetic tokens that provide exposure to underlying assets without actual ownership. 🔗 Chainlink has been pivotal for these DeFi markets, provisioning price oracles for each of these asset types. This has allowed new products and markets to be quickly launched in areas like lending/borrowing, derivatives, asset management, and more. ⚡ RealBlock is now bringing a new asset class on-chain: real estate derivatives . What it does • In this project we build a primitive that brings high-quality real estate data on-chain using chainlink. • And we create a market for traders who want to buy long exposure to real estate, short real estate or provide liquidity. • Effectively, we are creating an automated market maker (AMM) for real estate derivatives that is 100x more capital efficient than TradFi equivalents. • We also provide off-chain real estate and housing inflation analytics to enable on-chain trading. How we built it We created custom data pipelines connecting real state data from government APIs and data feeds (scraped). We've used Filecoin's IPFS and web3.storage to store, 'persist' and address the real estate data on-chain. This helped us improve transparency and immutability. We've used Chainlink to feed that data in and for price oracles, bringing off-chain house price data on the blockchain. Our swap contract then integrates with Chainlink /USD price feed to provide real-time currency conversion and allow users to swap USDC for tokens of each local region. We've used Truflation's housing inflation data feed to 1) provide users with additional analytics when they trade real estate derivatives on-chain, 2) we also built a token based on Truflation's UK housing data to enable users to directly trade on UK housing appreciation. We are using Quicknode to support core functions of the app and improve user experience e.g. show past transactions and live prices. We've used Polygon as the underlying chain and launched this on the Mumbai Testnet . Challenges we ran into • No GBP / USD data feed on Polygon's testnet. We had to bring our own off-chain FX data to use for currency conversion. • We had to understand on-chain data storage concepts and migrate from AWS to Filecoin. • We run into problems with Quicknode query limit of 10k blocks so all transaction activity has been hardcoded for now, until we find a solution for this. • Chainlink Automation transactions do not show up on Mumbai polygon scanner, making it difficult to verify if the transaction completed successfully - requiring events for tracing purposes • It was a challenge to create the architecture that maintains the peg between the tokens and off-chain housing data, when there is a 2-month delay with the off-chain data. We created an architecture (not yet coded) of perpetual futures market with an AMM to achieve the peg. Accomplishments that we're proud of • We expanded on an previous hackathon creating a big part of the product where users can now trade and provide liquidity What we learned • Speaking to 180 users, among them traders at hedge funds we learned that there is as a need for real estate derivatives trading on-chain. • We learned to use new tools such as Chainlink's keepers, Filecoin's IPFS, Quicknode and new products like Truflation. What's next for RealBlock • Add concentrated liquidity to liquidity pool. • Create a lending protocol using Chainlink's proof of reserves for collaterals and Chainlink's keeper functions for automated liquidations. • Create a DAO to govern the protocol. • Launch on Mainnet 🚀 <div