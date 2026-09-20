---
slug: "meltdown-nft-candle-auctions"
url: "https://devpost.com/software/meltdown-nft-candle-auctions"
title: "Meltdown"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 449
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Meltdown

> Meltdown is a candle-auction platform for NFTs on Ethereum. It's unique finalisation mechanism means higher revenues for sellers, whilst being more fair and decentralised for buyers.

[Devpost](https://devpost.com/software/meltdown-nft-candle-auctions) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[web_dom]]

**stack** chainlink, dapptools, ethereum, moralis, react, solidity, vercel, web3js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- challenges we faced
- what we learned
- what's next for meltdown | nft candle auctions

## Body

Homepage Auction creation Auction bidding page Inspiration In March 2021, Beeple auctioned off Everydays as a NFT at Christie's auction house. The artwork was sold for a record-breaking $69.3 million. However, shortly after the auction was finished, billionaire Justin Sun claimed he had bid $79 million in the final seconds of the auction, but the website glitched and the bid did not go through. This glitch might have cost Beeple $10 million . NFTs will represent all kinds of digital property in the future, so we need fair and decentralised ways of buying and selling them. Yet, current on-chain solutions are vulnerable to front-running and shill bidding. Meltdown is our solution to on-chain auctions, made possible by Chainlink's innovations in smart contract technology. What it does Meltdown is a decentralised NFT candle-auction platform. NFT owners can list their auction for sale, and buyers can trustlessly bid on them. Candle-auctions are similar to regular auctions, but nobody knows when the auction will end . The auctions will be randomly finalised in the closing period by Chainlink VRF and Keepers . This keeps the platform as fair and decentralised as possible. This has a number of advantages: Auction "sniping" is impossible Efficient as it finalised in a finite amount of time Non-cryptographic (not a commit/reveal scheme) approach, meaning smart contracts can also bid on the auctions How we built it Smart contracts were developed with dapp.tools . Definitely check it out if you are a Ethereum developer! Front-end was built with React and Moralis . Moralis is truly the ultimate Web3 development platform. It allowed us to integrate NFTs seamlessly and the contract syncing is nearly instant and super easy to use. You can view more about how it works at the contract GitHub page Accomplishments that we're proud of Super proud to have met each other in the Chainlink Discord and produce a working product, as well as teach each other about our specialisations to improve our React and Solidity skills :) Challenges we faced Living on the opposite side of the globe required good communication. Managing the scope of the project was also a challenge - determining which features should be prioritised. What we learned Heaps about Dapp development and Chainlink products. The importance of planning and deadlines to ship on time :D What's next for Meltdown | NFT Candle Auctions We think candle-auctions should be used more widely given how easy it is to produce verifiable fair outcomes with the blockchain and Chainlink. We will continue to improve our smart contracts, hopefully turning them into useful NFT and DeFi primitives for the ecosystem to use. We'd love to help teams integrate candle-auctions into their products and platforms. <div