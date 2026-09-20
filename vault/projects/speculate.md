---
slug: "speculate"
url: "https://devpost.com/software/speculate"
title: "Speculate"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 566
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Speculate

> Tokenized Options. Options that are represented as ERC-721 tokens on the binance smart chain.

[Devpost](https://devpost.com/software/speculate) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets


**stack** bsc, chainlink, foundry, ipfs, moralis, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- the exchange
- the option factory
- technologies used
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for speculate

## Body

Inspiration I have for a long time felt that the representations of derivatives on blockchains are worse than what they could be. There is no reason why derivatives such as call options should not follow a similar standard such ERC-721 or ERC-20, and this is a project where I tried to represent options as ERC-721s. What we love in defi in general is interoperability and composability, and this is a approach to making options more interoperable and composable. What it does It's a platform/exchange where users can both be market makers (by writing and selling the options) and takers by buying options. It's not only limited to cryptocurrencies, it works just aswell with equities and fiat. Everything that's necessary to make this work is chainlink price feeds and basic math. The caveat is that the collateral needs to be in cryptocurrency, it can of course not be in say, apple stock. Every option that gets created gets a corresponding NFT that is traded freely. If you sell your NFT, you also sell your right to exercise the option. So the NFT isn't just connected to the option, it is the actual option. How we built it The "backend" is basically divided into 2 parts, the exchange (SpeculateExchange.sol) and the option factory (OptionFactory.sol). There is also a minimalistic node server running that just index some events that are emitted from the exchange contract. The frontend is a next.js app. The Exchange Inspired by the LooksRare NFT marketplace. Major differences are that their marketplace have a off-chain matching system while I do everything on-chain and that I allow users to place limit orders (by utilizing chainlink price feeds). The exchange currently only accepts trading in the wrapped native token, which in my case is WBNB. It's however easy to add more currencies, and it would probably be optimal. The Option Factory Where the options are created. When a option is created a corresponding NFT gets minted, and when a option gets exercised the same NFT gets burned. Every NFT is stored "on" IPFS and pinned by infura. The Option Factory also keeps track of the collateral and thereby the health factor for a options seller. It doesn't yet but it should also handle liquidations when it's implemented. Technologies used chainlink price feeds binance smart chain ipfs for nft storage moralis web3 API for nft information Challenges we ran into designing the options protocol viewing the NFTs on other marketplaces (some accept SVGs, some don't) Accomplishments that we're proud of The limit orders utilizing chainlink price feeds are pretty nice. I also think the general idea of making derivatives more composable and interoperable is great. Also think the frontend looks at least somewhat decent. What we learned Designing a options protocol is hard, especially when you just learned what options are. There are definitely holes in my design, lol. How collateralized does a option need to be? Good question. Wrote a super simple formula for calculating the minimum collateral which is just the inherent value if the underlying asset goes up 25%. (applies to you if you sell a call). What's next for Speculate Will probably look into how I could implement put options first, and then the whole scheme around liquidations. Going to automatically exercise options at expiry with chainlink keepers. After that, I want to try looking into other derivatives as well, and maybe prediction markets. <div