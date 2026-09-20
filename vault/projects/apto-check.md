---
slug: "apto-check"
url: "https://devpost.com/software/apto-check"
title: "Apto-Check"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 1354
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/general_public"
  - "substrate/financial_record"
---

# Apto-Check

> The first blockchain-backed legit check

[Devpost](https://devpost.com/software/apto-check) · hackathon [[TreeHacks 2023]]

## Facets

**domain** [[health_clinical]] [[retail_commerce]] [[supply_logistics]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** aptos, firebase, firestore, gimp, next.js, next.js-backend:-typescript-+-aptos-api, petra, react, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- features coming soon to apto-check
- apto-check’s growth strategy

## Body

Inspiration The biggest question asked in the resale of any item of value used to be about condition, functionality, and other tangibles. But now, in a world where counterfeits are so hard to spot and brand value reigns supreme, the single most important question has become “is it real?” As unfortunate as it is, with the explosion of e-commerce, counterfeits have become an increasingly prominent concern in the purchase of any item, from consumer electronics to even fields as critical as prescription medication. However, no sector of business has been hit harder by counterfeiting than that of luxury apparel and accessories. The rise of counterfeiting has spawned a $118 billion anti-counterfeiting industry, with advanced QR codes and printing techniques employed to make it more difficult for bad actors to manufacture fakes and third-party validation companies like StockX protecting the resale market from fakes. Ironically, anti-counterfeiting measures have inspired many counterfeiters to also manufacture fake anti-counterfeiting features, including copied QR codes, forged certificates of authenticity, and even fake StockX tags. As a result it is absolutely impossible to say with 100% certainty that anything sold by anybody but the manufacturer itself is real, a plight that has plagued the secondhand market for years. In a survey of several sneakerheads across the nation with varying stakes in the sneaker resale market, the unanimous single largest concern when buying goods, even with seemingly proper documentation, is that the product is counterfeit, and the process of verifying/proving authenticity takes an average of nearly half the time spent on a transaction (over ten minutes!). We seek to provide a solution to this problem by leveraging the immutability of the blockchain, transparent transaction history of digital assets, and the unforgeability of digital signatures to INSTANTLY certify with 100% certainty that a physical asset is real using an NFT. What it does Apto-check is a protocol built on the Aptos blockchain that backs verifiably legitimate physical assets with NFTs. The protocol works as such: When the admin receives the asset’s serial number and substantial evidence that an asset is legitimate (what qualifies as “substantial” is either proof of recent purchase directly from the manufacturer or verification by trusted third parties like StockX or GOAT), the admin mints an NFT for the asset using the admin account’s private key and sends it to the address of the user requesting the NFT. It is important to note that the protocol is structured such that new NFTs can only be minted by ONE ADDRESS, the admin account. This is done deliberately, as it allows for every NFT minted for Apto-check to be traced back to the exact same minting address, making Apto-check NFTs absolutely impossible to counterfeit. Even if a criminal were able to mint an NFT with the exact same picture, serial number, and internal smart contract data, because they don’t have the admin’s private key, the fake NFT would trace back to the criminal’s address, rather than the admin’s, making it painfully obvious that the NFT is fake. Although this is certainly enough to invalidate attempts to counterfeit Apto-check NFTs, Apto-check actually has an additional safeguard in place in that it is impossible to send, receive, or even view NFTs not minted by the admin address, meaning that even if a counterfeit Apto-check NFT were to make it into an Aptos wallet, it would be impossible to use in the Apto-check dApp. Apto-check syncs with a user’s Petra Aptos wallet, and shows a detailed overview of the user’s current Apto-check NFTs on the homepage. Because Apto-check is meant to be used as a tool for the sneaker resale industry, let us consider how the dApp performs in the case of a sneaker sale. The idea is that a sale between buyer Alice and seller Bob will go as follows: Alice takes a look at an Apto-check backed pair of Jordans and decides that she is interested in purchasing it. Alice asks the ultimate question in requesting proof that those Jordans are real. Bob shows Alice the corresponding Apto-check NFT on the homepage of the Apto-check dApp, and demonstrates that the NFT’s serial number field matches the physical serial number on the pair of Jordans. Alice is assured without any doubt that the pair of Jordans are real, and decides to buy the shoes. Bob transfers the corresponding NFT to Alice’s Aptos address through the Apto-check dApp. Upon receiving the pending transfer of the shoes’ NFT in her Aptos wallet, Alice pays Bob for the shoes and accepts the transaction. The NFT is transferred to her wallet, and Alice is now able to prove to anybody that her Jordans are undeniably real. The hope is that in the sneaker resale market, Apto-check NFTs will be used as an undeniable standard of authenticity. How we built it Frontend: React, Typescript, Tailwind, Next.js Backend: Typescript + Aptos API, Firebase Blockchain: Aptos Accounts DB: Firestore Aptos Wallet: Petra Design: GIMP & MS Paint Challenges we ran into Learning how to use the Aptos API to interact with the Aptos blockchain was difficult to pick up, as it was both of our first times ever being exposed to the Aptos blockchain. We encountered some difficulty with using the Aptos incrementer to access an account’s tokens for the frontend, and accidentally became rate-limited. Many thanks to the Aptos team for their incredible support in helping us through the process of building in the Aptos ecosystem, answering any and all questions we had, and for solving the rate-limiting fiasco :) Accomplishments that we're proud of We took a big risk by deciding to take an idea we had planned to implement on another blockchain and building it on Aptos, a blockchain we hadn’t heard of until Treehacks. We are especially proud of how we were still able to leverage some unique aspects of Aptos to implement additional security features (such as preventing non-admin-minted NFTs from appearing in the dApp) to make Apto-check as airtight as possible, and we’ve certainly learned the unique benefits of building of Aptos, especially for a project like ours. In addition, we’re very happy with the user-friendly user experience we’ve created, as we believe that especially with blockchain projects, it is of utmost importance to make it easy enough for a user with no blockchain background at all to use properly. Features Coming Soon to Apto-Check Our intentions from the start were to subsidize all gas fees as to prevent overcomplicating the user experience by requiring all users to have APT in their wallets. The means to implement this feature are soon to come in an upcoming Aptos update. We also intend on vastly simplifying the barriers of entry for blockchain users by utilizing QR codes to communicate public keys, and by removing the necessity of a user to set up their own Petra wallets. We plan to allow users to sign up and sign in with just their email addresses and passwords by setting up wallets for them when they sign up to remove the overcomplication of needing to deal with multiple platforms. Apto-Check’s growth strategy Apto-Check has been segmented for the sneakerhead market first for several reasons, with the most obvious being the importance of proving genuinity quickly and with complete certainty, and with the most important being that the sneakerhead community has a generally bullish outlook on NFTs and has a substantial amount of overlap with the NFT community. We hope to establish Apto-Check as the new golden standard for authenticity in the sneakerhead market, just like how StockX did with their verification tags before they started getting faked, and use this to expand into the very adjacent broader market for luxury apparel. Given Apto-check’s potential to disrupt the $1.7 - 4.5 trillion market for counterfeit goods, the market potential for Apto-check, especially if it becomes integrated in the luxury goods supply chain (e.g. partnering with manufacturers to mint NFTs for all goods produced), is incredible. Furthermore, because it costs fractions of a penny for each transaction, monetization via charging a flat fee for each NFT minted will be infinitely scalable due to the negligible cost of maintaining the Apto-check network. <div