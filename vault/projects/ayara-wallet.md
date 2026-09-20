---
slug: "ayara-wallet"
url: "https://devpost.com/software/ayara-wallet"
title: "AYARA Wallet"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 464
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "substrate/financial_record"
---

# AYARA Wallet

> Universal-gas wallet, use any L2 dapp without gas bridging.

[Devpost](https://devpost.com/software/ayara-wallet) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**substrate** [[financial_record]]

**stack** accountabstraction, ccip, chromeextension, ethers, hardhat, node.js, react, solidity, typescript, web3auth

## How they structured the write-up

- inspiration
- what it does
- how it works
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ayara wallet

## Body

Universal Gas Token Login Dashboard Inspiration One of the bad experiences we have with crypto is that we have an endless of L2 chains and for every chain we need a native token to interact with dapps. Would it be awesome if we only need LINK in one chain and be able to use it as a gas for all L2 chains? We are fulfilling the dream of LINK as a " universal gas token ". Imagine a world where: One wallet that is on all chains. Use one Gas Tank on all the chains. Never worry about having enough gas on every chain. What it does Ayara Wallet is a smart contract wallet designed to simplify the use of Layer 2 (L2) networks and other blockchain networks. It eliminates the need for users to acquire or bridge native gas tokens. Install Chrome Extension. Creates a new EOA wallet with Google sign-in (web3auth is used as a signer), which becomes the owner of the smart contract wallet. Facilitates the creation of a smart contract wallet account. Allows locking of LINK in the contract, referred to as the "universal gas tank". Utilizes CCIP to create a smart contract wallet account on a different chain and execute a transaction on that chain. Subsequently, continue using the chain and with the gas allowance set by CCIP from the gas tank. How it works Smart Contracts The smart contracts are written in Solidity and tested using Hardhat. The contracts are deployed on Optimism Goerli, Base Goerli and Sepolia testnets. The contracts are using Chainlink's CCIP to send messages across networks to other AyaraController contracts. In one transaction it can: Lock some Link tokens in the wallet Send a message to another network Create a new smart contract wallet on the target network Set an allowance for the user to spend on the target network Execute the smart contract call on the target network AyaraController is deployed with the same address on all networks. This is important for the creation of Ayara Instances on other networks since it will create the same address for the same user across all networks. Optimism Goerli: 0xb7b6d3b50Bb0256eF6eE484fe535d95A6b879176 Base Goerli: 0xb7b6d3b50Bb0256eF6eE484fe535d95A6b879176 Sepolia: 0xb7b6d3b50Bb0256eF6eE484fe535d95A6b879176 Example of a successful cross-chain transaction with wallet creation Inheritance Graph: Challenges we ran into Somehow we can't inject the provider from web3auth, so we can't interact with dApps now. Accomplishments that we're proud of We create a smart contract wallet and use CCIP to send tokens in a second chain. What we learned Learned how to build a wallet on the chrome extension Learned smart contract wallet Learned CCIP What's next for AYARA Wallet Make Ayara wallet can interact with dApps directly. As CCIP becomes more connected, the complexity increases for users, so does the usefulness of Ayara Wallet! <div