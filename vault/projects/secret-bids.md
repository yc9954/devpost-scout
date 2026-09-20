---
slug: "secret-bids"
url: "https://devpost.com/software/secret-bids"
title: "Secret Bids"
hackathon: "Privacy4Web3 Hackathon"
organization: "Oasis Foundation"
winner: true
words: 309
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Secret Bids

> Privacy-preserving auction platform

[Devpost](https://devpost.com/software/secret-bids) · hackathon [[Privacy4Web3 Hackathon]]

## Facets

**domain** [[accessibility]]
**substrate** [[code_repository]] [[structured_db]]

**stack** api, firebase, hardhat, node.js, picocss, solidity, svelte

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for secret bids

## Body

home create auction place a bid claim token What it does Secret Bids is an on-chain privacy-preserving auction platform that allows auctioneers to launch secret auctions to sell their tokens/NFT. Currently, the platform offers 2 types of on-chain auctions Blind auction: (sealed bid auction) is a type of auction where all bidders commit their offers in sealed envelopes, without knowing the bids of the other participants. The highest bid wins the auction. Lottery auction: is a type of auction where the winning bid is determined randomly How we built it Secret Bids includes 3 main parts: 1. Contracts : Leverage Oasis Privacy Layer (OPL) and Sapphire contracts library Utilize Celer's Interchain Messaging <-> Sapphire integration to bridge contracts from Sapphire to other EVM networks 2. API : Sync on-chain data from contracts to the Firebase database Expose API to serve data to client dApp 3. dApp : Using ethers library to interact with Metamask Adopt Svelte framework and picocss to simplify coding Workflow Challenges we ran into Oasis Privacy Layer - Sapphire is awesome, Celer's Interchain Messaging (IM) integration is smoothly working. But the testing on remote messagsing is not easy, I didn't find any examples to guide this. Contract verification is quite inconvenient, it couldn't be verified by hardhat tool. Although, Oasis supported hardhat JSON metadata files to verify, but "Payload Too Large" error always happened when submitting on Oasis explorer. Eventually, I could verify by flattening contracts and submitting verification on Oasis explorer. Accomplishments that we're proud of Successfully launched an MPV version of on-chain privacy-preserving auction platform What we learned Learned more about Oasis architecture, components, Consensus/ParaTime layers as well Explored and deeply understood how Oasis Privacy Layer (OPL) - Sapphire work What's next for Secret Bids Offer more auction types Support more token standards ERC1155, ERC20... Support all networks as Oasis integrated Improve UI/UX <div