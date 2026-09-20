---
slug: "flynn-web2-to-web3-integration-tools"
url: "https://devpost.com/software/flynn-web2-to-web3-integration-tools"
title: "Flynn, Web2 to Web3 Gamefi integration tools"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 647
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/financial_record"
---

# Flynn, Web2 to Web3 Gamefi integration tools

> With Flynn tools, you can easily integrate your game or product into the Web3 world using familiar technologies and practices from the Web2 world. Create Web3 applications using a familiar stack!

[Devpost](https://devpost.com/software/flynn-web2-to-web3-integration-tools) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** cron, express.js, ipfs, mongodb, node.js, nuxt.js, pinata, solidity, trongrid, tronweb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flynn, web2 to web3 gamefi integration tools

## Body

Sign in/ Sign up page Interface Api Docs Bridge between Web3.0 and Web2.0 for assets Try it out links: https://flynn.ambersoft.llc/authorization - client side https://api-flynn.ambersoft.llc/api-docs/ - API docs Inspiration The idea came from creating our products and interacting with Web2 companies, that are interested in the world of Web3 but have no expertise or understanding to move their products to new heights. We had the idea, what if we will create a product that can make the process of moving to Web3 simple and clear? What it does We can divide Flynn tools into the following services: TRC20 Manager Allows you to create, transfer, mint, and burn tokens (an analog of hard/soft currency from the gaming industry) TRC721 Manager Allows you to create, transfer, mint, and burn NFT-721 (an analog of unique in-game items, TRC721 is also suitable for the implementation of randomly generated items.) TRC1155 Manager Allows you to create, transfer, mint, and burn NFT-1155 (an analog of in-game items, and also suitable for the implementation, for example, AWP Dragon Lore in NFT-form) TRC20 Bridge It’s the main trick, that makes the process of moving to Web3 easier. TRC20 Bridge allows you to implement and remove tokens from the game to the blockchain and back. NFT721/1155 Bridge NFT Bridge is the tool that allows you to implement and remove NFT 721 and 1155 standards from the game and back. How we built it We have been forming this idea for a long time and implementing it in our projects. When we discovered the hackathon, we decided to challenge ourselves and create the MVP product in a week. We shaped a team of IT and Web3 professionals to create a platform demonstrating to you that developing Web3 projects is rather simple. It will also allow you not to stuff your head with the complexities and challenges of blockchain technologies! Challenges we ran into One of the main difficulties was the question: How to provide a set of tools, that would meet all the possible requirements. We don’t intend to create a new almanac on thousands of lines of documentation but strive to give all basic advantages and abstractions from the world of blockchain. And then we shaped the concept of Managers and Bridges tools. The one allows controlling the main abstractions of the blockchain as simply as in the CMS, and the other allows players/users to blockchain their assets, or vice versa to bring their assets from the blockchain into the product. The second challenge was to create a program, which could organize the conducting transactions on the blockchain backend. Operations such as input/output of valuable resources should be atomic and reliable. To do this, the concept of a fault-tolerant transaction service was implemented in a blockchain with detailed logging of information. We call it Wallet Service. At the MVP stage, we don’t release this tool trying to avoid complicating the implementation ideology. Also, one of the main problems with working with TRC721 is getting the user’s “inventory”, because the standard does not provide the methods to get all tokens that the user has. We create the tool to solve this problem. It indexes transactions on tracker tokens so that all NFTs are displayed later. (method/v1/erc721/inventory). Accomplishments that we're proud of As a result, we created a lightweight service for asset interaction from the blockchain world as simple as working with CMS. What we learned Blockchain should be understood and should not frighten developers. What's next for Flynn, Web2 to Web3 Gamefi integration tools For increasing the transaction bandwidth we will create multi-wallet support for one account. Regardless of the current network load and RPC points, Wallet Service will be released to ensure fault tolerance and high stability Ability to integrate private RPC points for interaction with blockchain for more flexible infrastructure management. NFT marketplace constructor Also you can read more at by reading our presentation: https://drive.google.com/file/d/16p5-UbI2SdFX276qVHDl72sMi4u_sQqf/view?usp=sharing <div