---
slug: "endow"
url: "https://devpost.com/software/endow"
title: "Endow"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 477
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/financial_record"
---

# Endow

> Is a DeFi proof of donation investment product (nfts) targeted towards HODLERS who want to share their investment rewards from yield farming with community selected (DAO voting) charitable campaigns

[Devpost](https://devpost.com/software/endow) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[civic_government]]
**substrate** [[financial_record]]

**stack** aave, alchemyapi, aragon, chainlink, ipfs, javascript, moralis, node.js, polygon, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- smart contracts
- challenges we ran into
- what we learned
- what's next for endow

## Body

Inspiration our inspiration for this project are the many crypto investors who are HODLERS - our project gives the opportunity for these Hodlers to share yield opportunies by investing in low risk lending protocols and allocating rewards owned to socially beneficial campaigns as donations What it does investors can invest their crypto holdings in Endow investors investments are invested in a lending product (currently DAI - more to be added later) investors are issued Endow governance tokens for their investment - in future we will also issue share tokens to provide liquidity these investments are invested in AAVE via Endow's governance DAO (Aragon) Campaigner can post a socially beneficial campaign for donations on Endow - when they post their campaign they are issued with an NFT Investors vote via the DAO as to which Campaigns are eligible for donations from earnings on the investment pool During predesignated voting periods - investors can use their governance tokens to selectively allocate their rewards for donation to the eligible campaigns in the donors pool At the end of each voting period the investors rewards and donations are recalculated - the investor receives a Proof of Donation ERC 1155 NFT issued by each campaign they have donated to, as an official receipt for their donations How we built it hardhat chainlink starter solidity smart contracts react UI IPFS Aragon Dao Aave Moralis Alchemy Polygon Chainlink Keepers ERC1155 @openzeppelin Smart Contracts To facilitate our application several smart contracts were developed - as follows ITokenManager.sol - manages governance token issuance and burning with the Aragon Smart Contract IVoting.sol - manages voting for elegible campaigns and for selecting for each investor supported campaigns CampaignLauncher.sol - manages the workflow for a campaigner to submit, obtain approval and donations for each campaign - this contract also manages the issuance of NFTS for campaigns as well as NFTS for proof of donation by calling the EndowTokenManager.sol contract CampaignVotingManager.sol - manages the submission of campaigns for voting CampaignDonationKeeper.sol - A keeper is used to get the donation votes for each campaign CampaignReviewKeeper.sol - A keeper that manages the approval vote for any newly submitted campaigns AAVEDAIDDonorsPool.sol - A contract for managing investors investments into the investment/donation pool IDonor.sol - interface to track donations EndowTokenManager.sol - a contract that managers the issuance of NFTs for each campaigns and NFTs for Proof of donation Challenges we ran into time we all have full time jobs ## Accomplishments that we're proud of how we were able to integrate modular components ie chainlink, openzepplin, aragon dao, aave into an easy to use investment protocol issuing nfts to represent each campaign and erc1155 Proof of Donation tokens What we learned DAO protocols, Aave, NFTS, IPFS What's next for Endow further development including share tokens, security review deployment of UI to IPFS additional investment protocols add KYC/AML and identity validation to campaign owners <div