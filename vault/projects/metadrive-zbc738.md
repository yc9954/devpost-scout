---
slug: "metadrive-zbc738"
url: "https://devpost.com/software/metadrive-zbc738"
title: "Metadrive"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 513
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/sensor_telemetry"
---

# Metadrive

> Metadrive is a decentralised platform for uploading and sharing encrypted files. You can think of it as Google Drive for Web3.

[Devpost](https://devpost.com/software/metadrive-zbc738) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

  <sub>weak: revocation_withdrawal</sub>
**substrate** [[sensor_telemetry]]

**stack** filecoin, graphql, ipfs, mantine, polygon, react, solidity, thegraph

## How they structured the write-up

- inspiration
- what it does
- how it works
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for metadrive

## Body

User dashboard Unregistered user Sharing file Inspiration The idea of a platform like Metadrive came to me while I was working on another project of mine called Aegis. I needed a way to upload and store encrypted files in a decentralised way. I also needed the platform to be composable with other dApps, e.g. Aegis would use that platform as a file storage and sharing layer. There were some available options for this, but none of them used IPFS and Polygon as the primitives, rather they built custom solutions which is not something what I was looking for. What it does Metadrive is a decentralised platform for uploading and sharing encrypted files. It rests on top of two successful technologies, IPFS and Polygon, and overcomes the transparent nature of IPFS by providing an encryption layer on top of it using smart contract. You can think of it as Google Drive for Web3. It's also designed with composability in mind, so that other dApps can easily use this as a service and build on top of it. How it works For each registered user, it stores their public encryption key in the smart contract. For each uploaded file, it generates a symmetric key (called file key from now on), and encrypts the file using that key. And for every user the file is shared with (including the owner), the contract stores the encrypted version of file key, encrypted with the respective users' public encryption key. Whenever a user wants to download a file, the frontend gets the encrypted file key for that user, and requests Metamask to decrypt it using their private encryption key. Once the frontend has the plaintext file key for the file, it downloads the encrypted file from IPFS and decrypts it using that file key. The Metadrive smart contract is also an ERC721 NFT contract, and it mints an NFT for each file uploaded to Metadrive. The owner of the NFT is the owner of the file, and transferring the NFT means transferring ownership of the corresponding file. The dApp also uses The Graph as a critical part of its infrastructure. A subgraph indexing the Metadrive smart contract keeps track of each user's profile. Challenges I ran into The primary challenge was getting Metamask's eth_getEncryptionPublicKey and eth_decrypt RPC functions to get working, given it's a lesser used functionality and there's less documentation. These RPC functions are essential for Metadrive to function, but unfortunately only Metamask implements them as of yet, hopefully other wallets will add support for these soon. Another challenge was getting writing custom code for file encryption-decryption. Accomplishments that I'm proud of As far as I've looked, this is the first of its kind dApp, across all blockchains, and I believe this is a crucial piece of infrastructure that Web3 needs. What I learned Learned a lot about encryption! What's next for Metadrive Getting user feedback and making modifications as necessary, and then launching on mainnet. After mainnet launch, work would be focused on making the UX better, both from the frontend and as a composable smart-contract. <div