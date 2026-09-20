---
slug: "kodadot-moonsama"
url: "https://devpost.com/software/kodadot-moonsama"
title: "KodaDot: Moonsama"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 565
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# KodaDot: Moonsama

> We feel honoured to implement set of MoonSama contracts running on MoonRiver EVM

[Devpost](https://devpost.com/software/kodadot-moonsama) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[structured_db]]
  <sub>weak: financial_record</sub>

**stack** bounties, evm, graphql, indexer, kodadot, moonriver, nuxt, subsquid, uniquery, vuejs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kodadot evm: moonsama
- working demo links on kodadot: moonsama beta

## Body

Moonsama NFTs showing in KodaDot Holders of Moonsama NFTs in KodaDot History of transactions in Moonsama NFTs in KodaDot Pondsama NFTs in KodaDot Moonsama Minecraft NFTs in KodaDot User searching for Moonsama #337 in collection Inspiration As KodaDot wants to implement various NFT standards across the Polkadot ecosystem, we take this as an opportunity to battle test our thesis with Moonsama NFT contracts, which will help us prepare EVM integration into KodaDot for fully compatible deployment on MoonRiver, Moonbeam and Astar. What it does This submission extends the capability of KodaDot to gain insights from Moonsama contracts running on EVM parachain called MoonRiver in a friendly end-user user experience. You can browse various collections from a set of Moonsama multiverse and see NFT items' properties and their on-chain history activity per item. Per collection, the user can search on top of the collection see collection history, where you can see particular events users choose see top holders and which NFTs each address currently owns flippers which made gains on NFTs (currently experimental) How we built it We used the state-of-art EVM indexer by SubSquid. Using their tech stack, we could properly and correctly index NFTs based on the ERC-721 standard. Moreover, thanks to several smart hacks, we could integrate ERC-1155 NFTs without breaking the whole KodaDot architecture, which saved us a lot of time. Challenges we ran into You're always doing squids super-rough lol - Dima (CEO of SubSquid) We ran into a ton of challenges. First, not all smart contracts used the standard ERC-721 ABI, namely the BLVCK smart contract, written in solidity 0.4.24, used different calls. Second, the library ethers.js used internally unhandled WebSocket that crashed after a couple of minutes. Therefore, the SubSquid indexer suffered the downtimes. Third, the support of ERC-1155 - KodaDot UI was firstly optimized for the non-fungible tokens. Adding support for semi-fungible tokens, where we added a ton of entropy. Trying not to break the original functionality of KodaDot :) Accomplishments that we're proud of We were able to make a friendly, read-only version of the Moonsama-based NFTs in the KodaDot. Thanks to the flexible nature of our codebase and the reusability of components we have in KodaDot. To verify the correctness of the indexed data, we run our database dump against the running graphs provided by Moonsama. Data Exploration of Moonsama What we learned We are familiar with the Substrate codebase and how it behaves. We tried the modern ethers.js as the successor of web3.js. Additionally, we expanded our previous knowledge of Solidity smart contracts. We found out how the EVM data behave in the environment of substrate-based chains. What's next for KodaDot EVM: Moonsama We plan to integrate another series of features into the KodaDot EVM, so people can search NFTs through rarity explorer and, thanks to the marketplace contract, the ability to trade their NFTs, adding the sale amount per item into collection history and ability to gain another insight like historical prices and floor prices per collection. Best of all, everything is made as public good and open source and anyone can leverage KodaDot for their own stuff Working demo links on KodaDot: Moonsama Beta You can explore collections with various insights like collection history, top holders, and more coming along, as integrating EVM into KodaDot is a bit complex issue for our codebase. Enjoy Moonsama NFTs insights https://beta.kodadot.xyz/moonsama/explore?page=1 https://beta.kodadot.xyz/moonsama/collection/0xe4edcaaea73684b310fc206405ee80abcec73ee0?tab=items&page=1 https://beta.kodadot.xyz/moonsama/collection/0xe4edcaaea73684b310fc206405ee80abcec73ee0?tab=history&page=1 https://beta.kodadot.xyz/moonsama/collection/0xe4edcaaea73684b310fc206405ee80abcec73ee0?tab=holders&page=1 https://beta.kodadot.xyz/moonsama/collection/0xb654611f84a8dc429ba3cb4fda9fad236c505a1a?search=%23337 <div