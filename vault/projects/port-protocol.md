---
slug: "port-protocol"
url: "https://devpost.com/software/port-protocol"
title: "Port Protocol: Creator Economy"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 436
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Port Protocol: Creator Economy

> Use content with fair creative attribution and compensation by assembling datasets on-chain.

[Devpost](https://devpost.com/software/port-protocol) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[agriculture_food]]
**substrate** [[code_repository]] [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** alchemyapi, figma, hardhat, ipfs, metamask, moralis, openzepplin, pinata, polygon, react, truffle

## How they structured the write-up

- problem
- solution
- how we built it
- accomplishments that we're proud of
- what's next for port protocol

## Body

GIF View all items on chain in a feed and explore the transaction details with the "expand item" view Problem Current methods of harvesting data for machine learning models is exploitive to creators, because there is no way to compensate them for their work. To quote this tweet , "People’s source code and art is feed into these machines then turned into a paid service without these original creators even agreeing to this let alone getting compensated." We want to empower good actors to fairly compensate creators when they use their works. Think...the person who made your project's boilerplate, the creator of viral social content, or collaborators on a case study. Solution Port Protocol assembles content datasets on-chain so that they can be used with fair creative attribution and compensation. Content is minted into the PortContent NFT, which holds a link (stored either in a web3 decentralized service or from an existing web2 repository) to any file type of content (images, gifs, source code, music). The minter is either a 1) the creator or 2) a curator, represented by the originalCreator boolean in the NFT metadata. Once the content is on-chain, then anyone can mint a PortLicense NFT of that content to fairly use it. In this way, correct usage is trustlessly provable: if the creation was used online, and the license NFT is in the users wallet, then it was fairly compensated for its use. The inverse is also possible to prove: the user is not fairly compensating the creator if they do not have the license in their wallet. How we built it We wrote 3 smart contracts in Solidity ( Port.sol , PortContent.sol , and PortLicense.sol ) to handle the NFTs for the content, licensing, and distribution of royalties. The contracts were developed using helpful documentation from Polygon and Truffle/Infura. Additionally, we also created a full stack dapp (affectionately referred to as "Porthole") to view and browse the content created using the Port Protocol, and also to mint new content and new licenses. The Dapp was written in React and powered by the Alchemy APIs, Metamask login, and IPFS/Pinata. See additional implementation details in our Github README . Accomplishments that we're proud of As this was the first time I ever deployed a Solidity contract, I'm proud of how they turned out! What's next for Port Protocol Next is remixability: Once we have content on-chain, then we can empower creators to remix each others content and have the rewards and attribution automatically tracked and split in smart contracts. Continue to define the creative history of content. Build towards a more collaborative internet! <div