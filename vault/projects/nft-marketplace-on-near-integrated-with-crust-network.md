---
slug: "nft-marketplace-on-near-integrated-with-crust-network"
url: "https://devpost.com/software/nft-marketplace-on-near-integrated-with-crust-network"
title: "Picasarts.io - NFT Marketplace on Near"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 869
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Picasarts.io - NFT Marketplace on Near

> NFT marketplace on NEAR to mint, buy, sell and auction for NFTs, integrated with IPFS on Crust Network

[Devpost](https://devpost.com/software/nft-marketplace-on-near-integrated-with-crust-network) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[developer_tools]] [[retail_commerce]]
**substrate** [[structured_db]] [[web_dom]]

**stack** crustipfs, diadata, mongodb, mui, near-api-js, next.js, react.js, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for picasarts.io - nft marketplace on near

## Body

Create & Mint an NFT page Buy Now an NFT Make auction for an NFT All collection listing page All NFTs listing page Integrate with Crust Network IPFS Inspiration We got inspired by the growing market of NFT Market, distributed storage, and blockchain technology in 2021. We believe in the Near ecosystem & mechanisms, which are relatively fresh when in comparison with other platforms. So we decided to create an NFT marketplace in the Near platform and take the Crust Challenge to integrate IPFS. What it does Minting NFT on Near Sell NFTs on the marketplace Transfer NFT between Wallets Bidding Option: Making it possible to both purchase items and bid on them. Participants have an opportunity to see information about the current status of their bids Allows NFT holders to sell NFT Marketplace for the price (NEAR), and receive royalties for NFT Set up royalty fees Customize profiles How we built it We are a team having lots of experience in the eCommerce market. So we felt very confident when approaching this new project related to Marketplace Business. We felt lost finding someplace to start our first project. We tried to create some ideas with the Polkadot, BSC, Ethereum ecosystem, but dozens of DApps on the market with the same pictures. Finally, we found NEAR Metabuild Hackathon to start our project! We learn about Blockchain, the ecosystem, and the Rust language using Near and crust's Wiki resources. Then search for available examples and compare whether the instructions align with expectations and meet required standards. We also take advantage of our accumulated programming knowledge to accelerate the development of the APP and refer to available NFT marketplaces such as opensea, paras.io... We use the following technologies to build dApps: The frontend uses: React 17, NextJS 11 and MUI (a react component library using google material design standards) Rust Smart Contracts according to NEP-171. standard Database stores application information using MongoDB atlas Use Crust IPFS gateway to upload the file of the NFT token. Use the Crust Pining service to distribute files to the nodes of the Crust Network Use DIADATA endpoint with Datasource Coinmarketcap to get the price of Near Token in USD. Use near-api-js to perform frontend actions. Challenges we ran into We are new to the field of NFTs and many of the terms were not immediately clear to us, so it took time to study the topic of the NFT marketplace, IPFS,... We currently have a full-time job and therefore had to work at night to finish the hackathon Code examples are quite simple and buggy We are confused with many smart contract standards like NEP 777, NEP 20, ERC 20, ERC 1155... For more than 1 month, we had to learn about Blockchain from little knowledge, then had to learn new programming languages, different APIs and how to be usable. Integrate Crust Network Solution into the NFT marketplace built on the Near Protocol Blockchain, while the documentation and code examples on the internet do not work. When developing a package to simplify the process of uploading files to crust IPFS gateway + pining service through a single function. When integrating the sample code on the wiki, there are bugs and no specific instructions for react. Implemented NFT marketplace according to NEP - 171 standard, using Rust to write smart contracts, there are quite a few repositories on near-example for instructions but inconsistent, and got errors when deploying Marketplace smart contracts to near-sdk 4.0. 0. The error occurs when using near-api-js (v 0.41.0) to call the view function of the smart contract, the function cannot be found while using near-cli the function can still be called. We had to use 2 different versions of near-sdk for NFT and Market contracts. Accomplishments that we're proud of Complete basic NFT Marketplace functions in 1 month Completed all challenges from Crust to build a simple NodeJS package to optimize using Crust Network (check the link) Integrate with Diadata Oracle to convert the price of Near to USD We were able to build a team and workflow Implement smart contract with NEP-171 standard for NFT token and Marketplace Integrate with Google Analytics to implement the number of view token feature What we learned This was our first experience in creating a web-3 application; we have learned so many Build an NFT Marketplace and significant features Connect Near Wallet with a website Deploy a smart contract and the concept of it on Near Blockchain How NEP-171 token standard implemented and the technical aspects it responds to How IPFS network works and what it means for IPFS with NFT What's next for Picasarts.io - NFT Marketplace on Near There are many things we consider when starting out a Blockchain Project It is just a starting point of our Journey, we will keep going to build up this project along with the growth of the NEAR platform Right now, there are some product ideas we can think about: Go live on NEAR mainnet Optimize the Web Frontend page to look more artistic NFT LaunchPad More functions regarding NFT Marketplace Mentors or supports from Near to grow our project In the future, we want to seek funds to call out artists and users <div