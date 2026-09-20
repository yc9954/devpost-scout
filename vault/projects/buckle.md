---
slug: "buckle"
url: "https://devpost.com/software/buckle"
title: "Buckle"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 890
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/developer"
  - "substrate/financial_record"
---

# Buckle

> Permissionlessly teleport any token to any chains with low fees. A liquidity based bridge. Repo: https://github.com/fabriziogianni7/buckle-app/blob/main/README.md

[Devpost](https://devpost.com/software/buckle) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** ccip, chainlink, next, pricefeed, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how does it work
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for buckle
- evidendces for hackathon and sponsor price 🔍:

## Body

Logo teleport screen stake screen Inspiration Once I had 10 DAI in Mainnet and I needed to bridge to Arbitrum. I didn't want to use a bridge because fess were high and I was scared I would lose my money. My friend Had some DAI in arbitrum and I proposed this deal: I'll send you 10 DAI in Mainnet and you give me 10 DAI on Arbitrum. From this concept aka "atomic swap", I decided to create Buckle. Buckle is a trustless cross chain bridge protocol operating with Chainlink ccip. It's inspired by the model of atomic swaps , but it's much more. It allows to "teleport" tokens to any chain permissionlessly, safely and with the lowest fees on the market. It is different From other bridges because traditional bridges use a burn/mint lock/unlock mechanism that is centralized and expensive. What it does Buckle allow to do mainly 2 things: Allow users to teleport (bridge) any token to any chain with the safety provided by ccip and the lowest fees on the market Allow Liquidity Providers to deposit tokens in the pools and earn fees on every teleport How does it Work click on highlighted words to go to the code Buckle Is a protocol composed essentially by 2 smart contracts: CrossChainPool and PoolFactory . CrossChainPool This is the contract that allow users to teleport tokens and LPs to deposit tokens and earn fees . Each CrossChainPool is deployed and connected in pair with another pool on another chain . the 2 pools can move 1 token from chain A to chain B. When a user want to do a teleport, the pool uses ccip to send a simple message to the other pool. Users deposit tokens supported by the pool in the pool on chain A. This one send a message to the pool on chain B telling to release the tokens to the address of the user. Users will receive the amount they bridged minus fees. Users pay ccip fees in native currency. Each pool has the count of how much tokens are in the pool on the other chain ; this way it's not possible to teleport more than the amount available on the other pool. PoolFactory This contract deploys a pool pair with 1 transaction . It uses a ccip message to do that. The factory will send a message to another factory on another chain, which will deploy a new pool. The factory uses CREATE2 opcode to create the new pool and to compute the address of the pool that will be deployed on chain B ; then, it set it as allowed sender on the pool on chain A. when the message lands on chain B, the receive function set the address of the deployed pool on chain A as allowed sender and actually deploy the pool we computed the address for on chain A 🥳. How I built it I built it with solidity, chainlink ccip and nextjs. I deployed all the contracts on Avalance Fuji-c, Polygon Amoy testnet, Sepolia and Arbitrum Sepolia Challenges I ran into Challenge Solution Always knowing the amount of liquidity in the pool pair each pool is taking the count of how much tokens are in the other pool making sure LPs don't rug-pull users that placed a teleport order I inserted a cooldown period LPs have to submit before redeeming their tokens deploying pools and connect them in just one transaction Using CREATE2 opcode and computeAddress to deploy pool cross chain 🤯 making the teleports, deposit, redeem smooth and cheap fine-tuning the gasLimit used by ccip Accomplishments that I am proud of I'm proud of having completed the project as a solo programmer, from designing it, to smart contracts and frontend I'm proud of having my contracts tested I'm proud about overcoming every problem I encountered I'm proud that buckle is potentially way cheaper of other bridges I'm proud that buckle is an innovative and novel use case for bridging tokens I'm proud recording the building process in live streaming, on my yt channel, in 17 days. They told me: "build in public!" and so I did. I'm proud of using best practices to protect my private keys (even tho they are just from test addresses) What I learned I learnt a lot about smart contract and cross chain liquidity protocols. I understood all the challenges that involve building this kind of projects What's next for Buckle I intend to follow up with the development of buckle. In these days I've been collecting feedback and I started to gain user traction. I deployed a set of pools where user can teleport real test Link. I think the idea is valid and the project is solid. So it is worth to keep going with it. Evidendces For Hackathon and sponsor price 🔍: Chainlink: Ccip usage: using ccip to send messages cross chains, in specific, the protocol send message to make:- teleports, deposit, redeemals and to deploy simultaneusly 2 pools crosschain code: teleport function deposit function redeem function deploys a pool pair with 1 transaction Sponsor price: Polygon I deployed contracts in Polygon Amoy and I'm using them in the frontend. Factory: Polygon Amoy : 0xdbb077ddec08e8b574186098359d30556af6797d Pools: 0x17ecec2ab5977077d4c66f51fa7053b991e97fc4 Sponsor price: Avalanche I deployed contracts in Avalanche Fuji-c and I'm using them in the frontend. Factory: 0x9c0a2c95646e32a764858fa95e30b7bd4d29cac2 Pools: 0x2Edde7A4f7A5d684CcE3c98D25A2F92042ef6C32 <div