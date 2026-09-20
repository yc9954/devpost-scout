---
slug: "opto"
url: "https://devpost.com/software/opto"
title: "Opto"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 584
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Opto

> Opto is a decentralized option exchange of derivites products e.g. gas averages, Eth blob price, Equities, Metals, etc... User can either write or buy option, they can even publish custom options.

[Devpost](https://devpost.com/software/opto) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** hardhat, nextjs, solidity, tailwind, thegraph

## How they structured the write-up

- how it works
- chainlink stack usage
- main challenges

## Body

Gas&Blob options - Explore Equities options - Explore Commodities options - Explore Custom options - Write Blob gas option - Write Equities (Apple) option - Buy Options Written by your wallet Options bought by your wallet Opto: A Decentralized Option Exchange Opto is a decentralized option exchange of derivative products. In particular, Opto supports European put and call options. Users can: buy an existing option write a new one using one of the Opto built-in options publish custom options trade their options since options are represented by ERC721 tokens Opto supports different built-in options with different data sources: average mainnet blob fees, from subgraph and public RPC average gas fees for multiple EVM chains, from subgraph and public RPC Equities, from Chainlink Price feed Commodities, from Chainlink Price feed When writing a new option (or publishing a new one), users can choose: expiration date and buy deadline strike price in $ premium price in $ put or call n. of units available to be bought optional stop loss in $ for each unit How It Works Writer writes a new option Buyer buys the option paying the option premium price to the writer When the option expiration date is reached a Chainlink automation (custom logic) Upkeep triggers a Chainlink Function call The Function makes an https call to the option price data source (Price Feed or subgraph/RPC) Depending if the option is a put or call and confronting the resulting price with the strike price the option could have to pay buyers or not Buyers, if won, can claim their option cash settlement difference Chainlink Stack Usage Opto is completely built on the Chainlink stack: Automation: custom logic upkeep to trigger when one or more active options reached the expiration date deadline Functions: the Automation triggers a Functions call to make an https call to the option data source and return the price result Price Feed: called by our Functions to retrieve equities and commodities prices Main Challenges The main challenge was writing an efficient checkUpkeep for the Automation service. The custom checkUpkeep needed to iterate on all the active options with expiration date reached and return the option id. Iterate on a potentially large array is not sustainable at certain gas tresholds, as chainlink DON's can process checkUpkeep offchain up to a maximum of 10M gas. That is a major iussue that we faced during Constellation too and we didn't like the approach to have several upkeeps to check subarrays as suggested in an article about this iusse from chainlink. We wanted to keep 1 single upkeep to do the work. In order to make this sustainable with a very, very large array we elaborated a time-based checkUpkeep system that checks subarrays in a given time-frame. So we can cycle less entries, but eventually have all subarrays being periodically checked, if a subarray gets depleted it is discarded from future checks. We were not aware of how other teams dealt/are dealing with this question mark, but more in general we believe many developers at a point will face the same iussue as we did. So one of our goal in the contract was to sort this out and hopefully be useful as a reference for future Automation devs. We faced other every-day challenges. Like hitting max contract size, facing small typos in js when integrating functions (like missing a ";"), being unlucky to have functions revert cause 30 link werent enough according to the estimation, that kept us wondering for extra hours <div