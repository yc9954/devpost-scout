---
slug: "your-first-perpetual-nft-exchange-fixel"
url: "https://devpost.com/software/your-first-perpetual-nft-exchange-fixel"
title: "Fixel"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 826
team_size: 6
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
---

# Fixel

> Perpetual NFT Exchange on Polygon

[Devpost](https://devpost.com/software/your-first-perpetual-nft-exchange-fixel) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]

**stack** angular.js, hardhat, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fixel

## Body

The First Perpetual NFT Exchange Fixel on Polygon Trade CryptoPunk, BAYC, Doodle, and other top NFT collections with up to 20x leverage Share your NFT Position Card like UniswapV3 Provide Liquidity with up to 10x leverage Inspiration The lack of liquidity in the NFT market limit participants from trading NFTs at the desired size, timing and price. Such liquidity issue occurs due to NFTs’ innate attributes of non-fungibility and indivisibility. There are countless ongoing attempts to tackle such liquidity issue, with representative examples including NFTX which tokenizes NFTs into divisible ERC20 tokens. Nonetheless, NFTX has not been able to solve the liquidity component, thus remaining at a daily total volume of under 100 ETH. Fixel introduces for the first time three groundbreaking concepts to the NFT market which are (1) Synthetic NFT Exchange; (2) PvP AMM; and (3) Synthetically Leveraged LP to become the First Perpetual NFT Exchange. What it does Our Perpetual NFT Exchange, Fixel, provides (1) perpetual NFT trades for NFT traders; and (2) leveraged LP for Liquidity Providers. (1) Perpetual NFT Trades You can trade the average price of an entire NFT collection in the form of perpetual futures with up to 20x leverage. NFT traders can open a long or short position at a desired size, with low fees and without moving the price at all. 0.1% Trading Fee (2.5% at OpenSea) Zero Slippage Leverage up to 20x (2) Provide Liquidity with up to 10x Leverage Liquidity Providers can provide liquidity to become the counterparty of traders while earning trading fees. Liquidity Providers can make up to a 10x leveraged LP position to maximize fee profit. Earn 70% of Fee Distribution Liquidity Providing with up to 20x Leverage How we built it [PvP AMM] We implemented a PvP AMM structure that hedges the default risk of the LP pool, deriving from taking excessively on PnL of traders and from shortages of fund during initial stage of liquidity providing. PvP AMM, proposed by GMX, is a new concept that adds a new feature for traders to participate as liquidity providers on top of currency conversion layer. With the certain level of scale of economic is achieved as much as in derivatives and gambling markets, it is an ideal LP pool model that guarantees profit generating for protocols. [SLLP: Synthetically Leverage Liquidity Providing] We created an idea that allows liquidity providers to 10x leverage by borrowing from a virtual liquidity pool of a protocol based on PvP AMM structure. This model improves liquidity provider’s capital efficiency at an extreme level. Synthetix : Requires to deposit 400% of the actual liquidity in the pool GMX : Requires to deposit 100% of the actual liquidity Fixel : Available to provide 1,000% of actual liquidity provided. Synthetix : GMX : Fixel = 1/4x : 1x : 10x = 1 : 4: 40 [NFT collection index oracle from NFTBank] We Receive data feed of NFT Collection from NFT Bank and update it on-chain to provide index price for perpetual NFT Market. Challenges we ran into [Protocol Stability] There is always a possibility of default risk for synthetic protocols with low liquidity. In address the issue, we implemented 1) PvP AMM structure by GMX 2) Created Synthetically Leveraged Liquidity Providing model to formulate a large liquidity pool using limited capitals. [NFT Projects Have Longer Price Cycle] Compared to ERC20 tokens, NFT collections show longer price cycle durations. This makes NFT collections’ future prices relatively easier to predict. This poses a possibility of LP pool liquidity drainage. To address this issue, Fixel implements valuation models on NFT collections quoted in USD instead of ETH. This way, the price volatility of ETH based NFT collections in turn include the price volatility of ETH. Accomplishments that we're proud of Here is what we have accomplished. Implementing Synthetically Leveraged Liquidity Providing, we made it possible to access margin tradings without gathering any liquidity. With this format, LPs are now able to gain 10x profits by taking on 10x more of PnL of traders; protocols are now able to create even larger liquidity pools and capable of taking on larger amount of PnL while using limited fund sources. Specifically, PvP AMM + SLLP combination transforms PvP AMM’s non-linearly profitable structure into a semi-linearly profitable structure. With such implementations, we expect various synthetic protocols to form even larger liquidity pools for more stability. What we learned While implementing the PositionManager contract, the trading component of the protocol, we had to deal with values that changed in real time. Rather than directly handling the status necessary for implementation by applying dynamic programming, we learned how to minimize the amount of association by storing only essential factors. What's next for Fixel [Decentralized Data Feed] The current data feed is provided through the NFT Bank API and is centralized. The protocol plans to secure decentralization of the data feed through collaboration with API3. [NFT Option Modeling] We will provide derivative products that use NFT as underlying asset. <div