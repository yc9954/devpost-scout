---
slug: "solanalysis-nft-flex"
url: "https://devpost.com/software/solanalysis-nft-flex"
title: "Solanalysis: NFT FLEX"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 411
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "substrate/financial_record"
---

# Solanalysis: NFT FLEX

> Solanalysis gives a bird's eye view of the NFT ecosystem, and using NFT FLEX, users can now see the estimated fair value of their own NFT's and showcase their NFT's to the community.

[Devpost](https://devpost.com/software/solanalysis-nft-flex) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**domain** [[transportation]]
**substrate** [[financial_record]]

**stack** docker, gcp, genesysgo, graphql, postgresql, python, react, sklearn, spanner, tensorflow, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for solanalysis: nft flex

## Body

Inspiration The first Solana mint we ever got exposed to was the @DegenApeAcademy drop and after mint, like everyone else, we were left with more questions than answers. Is this maid outfit valuable (probably not)? What is this crayon-eating ape worth? While exchanges & arweave were troubleshooting for high traffic, we built our first model to value the Apes of the Degenerate Ape Academy. What it does Simply connect your wallet or search a wallet address / .sol name on https://solanalysis.com/nft-flex to view the total estimated value of NFT's in any wallet. While other projects in Solana and other Layer 1 Ecosystems typically display collection floor price, we felt it important to account for rarities & nuance within collections to protect, guide, and empower the community. How we built it We started by parsing on-chain transaction data across multiple marketplaces to display information on our homepage. From there, we gather mintIds of top collections ourselves where possible (otherwise from the project leaders). To create the valuations from the transaction data, we use multiple methods of machine learning & statistical analysis, ranging from neural networks to regression models. If there’s insufficient transaction data for a collection, we don’t display an estimate and default to collection floor price. Challenges we ran into Every exchange has its own methodology of structuring transactions, and the features of the exchanges (as well as the number of them) are changing over time. Similarly, the valuation ranges of NFT's and their attributes also are non-stationary over time. Finally, not all projects follow the same standards when creating their NFT's for a particular collection. Accomplishments that we're proud of Alan, Adriano, and Bryan worked on this hackathon project with us while balancing a full-time job, and Johnny was in the process of leaving his job at Amazon when we began. We worked so well together and believe in a cohesive vision to the point that we will all be working on Solanalysis full-time moving forward. What we learned There are so many great products that need to be developed to serve our burgeoning ecosystem. Together, we can achieve ~moonshot~ goals in short periods of time. What's next for Solanalysis: NFT FLEX We plan on layering in social elements so that you can follow trades, mints & more of your friends and other members of the broader community! We'll also continue to improve UI/UX, add support for collections, create better models, and integrate the experience with the broader community! <div