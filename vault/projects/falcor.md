---
slug: "falcor"
url: "https://devpost.com/software/falcor"
title: "Falcor"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 402
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# Falcor

> A no-loss donation protocol

[Devpost](https://devpost.com/software/falcor) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** chainlink, javascript, polygon, solidity, spheron, vue

## How they structured the write-up

- inspiration
- what it does
- sponsor technologies used
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for falcor

## Body

Inspiration Falcor is inspired by PoolTogether. Basically, Falcor aims to be the "PoolTogether for donations". What it does Falcor is a lossless donation protocol where people can donate to organizations, causes or individuals without loosing their deposited funds. The protocol is permissionless, which means anyone can create donation pools and deposit funds into the pools. The protocol allows the deposit of Stable coins (such as USDC, USDT and DAI) and more options will be added. Returns earned from the pools will be sent to the benefiary of each donation pools every month, automated with Chainlink Keepers. The amount each donation pool beneficiary gets depends on the amount of token deposited into the pool by the protocol users. Donation pool depositors can also withdraw their funds from the donation pools anytime they want. Sponsor Technologies Used Filecoin/IPFS: I used Filecoin/IPFS via web3.storage to store donation pool images and indirectly through Spheron network Spheron Network: The Dapp user interface is hosted on the decentralized network via Spheron ( https://falcor-protocol-azauxm.spheron.app ) Chainlink: I used chainlink keepers to automate the yield distribution to donation pools beneficiary addresses and also used chainlink data feeds. How we built it Falcor is built and deployed to the polygon blockchain(currently Mumbai Testnet). It's smart contracts are written in Solidity It's Frontend is written in Vue Files (Images) are stored on IPFS The frontend is hosted via spheron protocol (which also use IPFS) Challenges we ran into A lot of challenges were encountered during the period of building this project, some are: Choosing the yield source for the POC: Initially 0vix protocol was used as the yield source but due to little developer resources, Aave is used. Integrating Chainlink Keepers: Chainlink keepers does not run the performUpkeep if there is an error and does not provide a way to figure out what went wrong, I have to spend a lot of time working things out. Accomplishments that we're proud of What we learned So many things were learnt during the hackathon, some of them are: How to integrate Chainlink keepers into a smart contract Hosting Dapps on Spheron What's next for Falcor Get a team to work on the protocol with me. Modify the protocol's core to allow integration of more yield sources (such as 0vix, compound etc) Grow a community of individuals and organizations that will initially use the protocol Develop a roadmap of the project Launch on mainnet <div