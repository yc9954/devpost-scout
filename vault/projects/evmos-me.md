---
slug: "evmos-me"
url: "https://devpost.com/software/evmos-me"
title: "Evmos.me"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 499
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
---

# Evmos.me

> Evmos.me is a wallet that allows the user to interact with the evmos blockchain using Metamask and Keplr. It supports the interaction with intrarelayer module, ERC20s, ibc-vouchers and cosmos coins.

[Devpost](https://devpost.com/software/evmos-me) · hackathon [[Cosmos HackAtom VI]]

## Facets

**substrate** [[financial_record]]

**stack** github, google-cloud, node.js, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for evmos.me

## Body

Landing page Wallet Cosmos ERC20s Send Coins ERC20 functions Delegators Intrarelayer Converters Intrarelayer Proposals Wallet Utils Inspiration The evmos blockchain has the problem that it supports ethereum and cosmos transactions. For the community this implies that they need to use both Metamask and Keplr wallets to interact with the blockchain. What it does The evmos.me wallet allows the user to sign up with Metamask or Keplr to start interacting with the blockchain. The main features are: sending cosmos, ibc-vouchers and ERC20 coins allowing the interaction with the newly created intrarelayer module (create proposals and convert coins) creating ERC20 contracts (Metamask only) minting of ERC20 tokens (Metamask only) transferring of ERC20 tokens (Metamask only) requesting ERC20 tokens balance converting ​ethereum (0x...) and evmos (evmos1...) addresses delegating and un-delegating aphotons ​ How we built it The project was built as a client - server application. The frontend was built using React and Nextjs , it's hosted on github pages and just request to the backend api. The backend was built using python ( fastapi ). To support the cosmos messages on evmos, a python library was developed. This library is also open source evmosgrpc . Challenges we ran into The main challenge was figuring it out how to interact with the grpc endpoint. After creating the python library that was very easy to deal with. The other challenge was how to sign cosmos transactions using Metamask and determinate the Keplr wallet limits when interacting with ERC20 tokens . The last challenge was dealing with the fees on each transaction because creating a contract is very expensive but sending a token is pretty cheap. Accomplishments that we're proud of The project started as a way to see how could I interact with the blockchain and allow me to send transactions without using the cli . At the end of the HackAtom it ended being a wallet that can be used for the main tasks that a normal user would need. Creating an ERC20 with just 2 inputs was really fun and enables more users to interact with the incentivized testnet and earn some coins. What we learned Interacting with cosmos blockchains is easier than expected once you understand how the GRPC works and it can lead to the development of very interesting apps. What's next for Evmos.me TODOs list from the FAQ: List all the intrarelayer coins without the need to remember the complete assigned name. Display the correct value for the intrarelayer coins because the GRPC response list the balances, for example, as PHOTON, but it should be displayed as BALANCE/DECIMALS PHOTONS. List all the current active proposals and allow the user to vote using his wallet. List all the validator and simplify the delegate photons process. Read the ERC20 registered tokens from the gov proposals instead of manually adding the contract addresses. Add a display cosmos message info option for each message before signing it with Metamask. (This information is already displayed on Keplr when sending the same transaction) <div