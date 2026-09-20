---
slug: "flea-archway-nft-market"
url: "https://devpost.com/software/flea-archway-nft-market"
title: "Flea (Archway NFT Market)"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 420
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Flea (Archway NFT Market)

> Our NFT market on Archway is unique in that we don't need to charge market fees to our users.

[Devpost](https://devpost.com/software/flea-archway-nft-market) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** archway, cosmjs, cosmwasm, keplr, nextjs, react, rust, typescript, vecel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flea (archway nft market)

## Body

You can buy favorite NFTs from Market. You can sell your own NFTs. You can mint your NFT easily. You can convert native token to wrapped CW20 token easily. Inspiration We want to create meaningful applications on Cosmos. There are various Cosmos chains, and little by little, NFT projects and marketplaces are appearing. For the development of the Cosmos ecosystem, We thought that a marketplace where NFTs of various chains can be traded is necessary. The marketplace that everyone will use is one that has low fees and is sustainable. We believe that Archway is the best place to achieve this. What it does This is the NFT marketplace on Archway. You can easily publish NFTs here by filling out the form with your name, image URL, and description, and then clicking a button. If you have CONST, the native token of Archway Testnet, you can easily get Wrapped tokens and use them to buy and sell NFTs. How we built it Using the official Archway CLI, We created and deployed smart contracts for the NFT marketplace, NFT issuance, and Wrappd Token issuance. We used Typescript, React, Next.js, and tailwind to create the frontend, and cosmjs and Keplr to connect Archway's testnet to Dapp. The frontend is exposed to everyone, not just the local environment, by deploying it on Vercel. Challenges we ran into After the maintenance of Archway's testnet, which took place around December 3, a misconfiguration of the RPC node made it impossible to reference queries or execute transactions for several days. However, by reporting to the management team from time to time, the management team was able to identify the cause and resolve the issue. Thank you, management team. Other than that, it was difficult to handle Archway's CLI because the specifications were different from those of other CLIs that handle CosmWasm. We also learned how to build a virtual Ubuntu environment to set up a development environment. Accomplishments that we're proud of We were able to create the beginning of a project that would be meaningful to do on Archway and Cosmos. And the simple fact is that we were able to complete the preparation of the smart contract and the front-end within the time frame. What we learned Handling Complex Contracts Using CW20 and CW721 How to create Dapps using Keplr Collaborate with the developer community What's next for Flea (Archway NFT Market) NFT Collection NFT Auction Floor price reference by collection or attribute NFT Launch Pad Handling of another chain NFT via IBC <div