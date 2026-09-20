---
slug: "dauction"
url: "https://devpost.com/software/dauction"
title: "Dauction"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 386
team_size: 5
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "substrate/geospatial"
---

# Dauction

> Decentralized auction project which uses a sealed bid mechanism to enable an ERC721 asset to be auctioned without each bid being revealed until the end of a given period as specified by the seller

[Devpost](https://devpost.com/software/dauction) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**substrate** [[geospatial]]

**stack** chainlink, ethersjs, ipfs, openzeppelin, pinata, solidity, sveltekit, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dauction

## Body

Dauction - Decentralized Auction Inspiration This project was inspired by a real challenge we faced last year when a member of our team wanted to sell his Macbook Pro laptop. Four friends showed interest in purchasing the laptop as it was still in good condition and its price was far cheaper than the real market value. We realized a problem: no one wanted to be outbid; no one wanted the auction owner to influence the outcome of the auction. Everyone wanted a solution that could trustlessly allow anyone to bid without revealing their respective bid amount, an efficient solution to determine the highest bidder without compromising privacy concerns. What it does Dauction is a decentralized auction project which allows users to auction their assets. Using a sealed bid mechanism, ERC721 tokens otherwise referred to as NFTs can be auctioned, allowing bidders to bid without revealing the value of their bid until the end of a given auction period as specified by the seller. At the elapse of a given auction period, the highest bid would be unveiled, thus allowing the highest bidder to seamlessly purchase the auctioned asset. How we built it We built the dapp by splitting the required tasks into: Design: built using Figma Frontend: built using SvelteKit and Typescript Smart contract development/testing: built using solidity, hardhat Challenges we ran into We had challenges while trying to utilize Zokrates - zk framework - to implement our solution Accomplishments that we're proud of We are proud we were able to solve the problems associated with the privacy of bids and we successfully provided bidders an option to create bids using an array of tokens - LINK, WETH, WBTC and USDT What we learned How to map complex data structures and leverage Chainlink to implement our real-time exchange rate needs in a secure manner What's next for Dauction This solution is a work in progress; we intend to still research further to find more efficient means to reduce user-dependent parameters, implement zero-knowledge and enhance our general UX. While the current solution only focuses on the on-chain aspects, the off-chain aspect is a crucial part we intend to efficiently implement by leveraging relevant technologies such that a given auction item can be tracked, monitored, and proven that its on-chain auction settlement outcomes verifiably satisfy all expectations <div