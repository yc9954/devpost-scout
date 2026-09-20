---
slug: "scribe-vjp3sb"
url: "https://devpost.com/software/scribe-vjp3sb"
title: "scribe"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 735
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# scribe

> a collaborative nft writing experiment. a example for bringing producer, data, consumer flow to NFTs

[Devpost](https://devpost.com/software/scribe-vjp3sb) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[general_public]]
**substrate** [[geospatial]] [[structured_db]]

**stack** avalanche, chainlink, evm, go, javascript, postgresql, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scribe

## Body

Inspiration The motivation was to create an nft project with words/writing being the focus. The original idea was to create a generative haiku nft project. This idea seem to not focus on new chainlink integrations or interopability mechanics. The idea was then broken down into a more atomic being of nfts that represent a single word with a system that continually produces words. The Infinite monkey theorem was a big source of inspiration. Project like "the n project", "loot", and "colors" generality of application is a hope for how communities may choose to build on top of Scribe. What it does Scribe is a simple use case of what a collection of producer, data, consumer nft interfaces may be. In terms of scribe project, producers are chimps, data are words, and consumers are scrolls. Chimps produce words, words can be aggregated into scrolls, and scrolls represent some aggregation of defined meaning by the owners of those involved. Technically, scribe uses chainlink vrf numbers captured in nft metadata as input to an off chain computation to produce a new random word. This word is then stored in the that nfts metadata where it can be minted into a new word nft. These word nfts can propose to be part of a scroll. Scroll owners can accept or reject words that have been proposed to the scroll. How we built it An extremely important aspect of the structure between the producer, data, and consumer pieces is modularity. We only want producer and data to have a tight coupling because there is an implicit relationship between the token ids that map where the data was produced from. Consumers and data should be able to interact purely on if they inherit the interface, and each keep track of the token id and contract address. This allows for a modular system of interoperable pieces to be allow data nfts to be aggregated into any consumer nft of their choice. Challenges we ran into By far the biggest obstacle was to figure out a gas efficient solution of how to continually produce data and store on chain to enable a practical mint price of an a chimp nft. Next, would have to be gas efficiencies for multi-royalties stake holder solution. We simply ran out of time and along with getting a laptop stolen with unpushed in the last leg of the hackathon. The distribution of royalties to a dynamic set of distribtees was much harder than we thought, and we were not able to produce a solution we were happy with during this time. Accomplishments that we're proud of We have the base chainlink contract functionality operational. We can produce 150 words for roughly 1 $AVAX thus per chimp the cost of about 0.005 avax a day. This means for an entire year of and assume optimal gas conditions the price per chimp to produce words for an entire year costs 1.825 $AVAX. That is huge news for the practicality of continuously minting projects like this on avalanche. We are very proud of the development operations work we needed to get an avalanche fuji node running, run our own postgresql database, and chainlink node operations deployment automation scripts we developed along the way. What we learned We learned a lot about running a chainlink node, solidity coding, and working in blockchain environments. The majority of the work was around deploying the VRF coordinator contracts, setting up a chainlink node to process these random requests, and building an api for our database of words to work with chainlink external adapters for requests. Once these pieces were in place it was mainly learning the ins and out solidity. We needed to be very gas efficient so we spent time learning low level solidity memory management. Hardhat was a big component for query blockchain data for deploying, running tasks, and simple testing. Our external adapter takes advantage of ethers to work with on-chain data. The project was a good learning experience for DevOps work in blockchain environments and gas efficient smart contracts. What's next for scribe The major next steps for Scribe is to build out the Scroll functionality to impose an ordering on words and have a off-chain representation of the aggregation of words. From there, the royalty structure to enable multi-royalties right accruing structure will be built. We have a fleshed roadmap in our documentation, please see there for more details. <div