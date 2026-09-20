---
slug: "nftdocket"
url: "https://devpost.com/software/nftdocket"
title: "NFTDocket"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1058
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "user/general_public"
---

# NFTDocket

> NFTDocket is a Decentralised Warranty Issue platform that can be used by sellers to dispatch their warranties to buyers via an NFT built using Polygon.

[Devpost](https://devpost.com/software/nftdocket) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[finance_payments]]
**user** [[general_public]]

**stack** etherium, gelato, ipfs, polygon, react, solidity, tailwind, vercel, web3.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nftdocket

## Body

Inspiration The usual practice of warranty being issued in the physical form leads to loss of warranty card due to various reasons like misplacement, theft etc. There must be a better way of issuing and keeping track of issued warranty cards so that the consumer can get proper service and protection for their purchase. The major problems that we focussed to work on in the project are: Use of SoulBound NFT Proof of Ownership Automating Expiry of the Warranty Ability to show Product details and Warranty till expiry date GUI platform to interact with the contract What it does Using our platform a seller can issue warranties using NFTs for products which can later be verified by the Customer. The buyer can also resell it till the expiry date of the warranty. As the platform can also work as a plugin. It can easily be implemented in any marketplace application and used seamlessly without the need to code a single line of code. The issue warranty and resell warranties features of our application can also be made automated with which just a single click will issue the warranty without the need to add details manually if it is implemented in the marketplace an application. As we are using Soulbound NFTs in the application this can also be used to issue on-chain certificates that are issued uniquely such as Degrees, Tickets, Citizenship and much more. Also, as there is no need for prior knowledge of Blockchain it can easily be implemented by any non- crypto native seamlessly. How we built it SoulBound NFTs are basically NFTs that are bound to a particular private wallet i.e. ‘Soul’. This makes them non-transferrable making it very difficult for an NFT Theft to take place. We achieved the above by including the Customer’s wallet address or the ’ Soul Wallet’ as the public key of the owner in the NFT itself so the Soul is intangible and remains secure in the NFT. In simpler words, the Warranty NFT has a part of its data storing the owner of itself and mints in the blockchain. We included the Keccak256 hash of the Product’s Serial Id and the Owner ID in the NFT minted it. Then we send this to the pending warranties list of the owner who then needs to claim this. The verification is done by re-hashing using the Keccak256 hash and comparing it against the hash present in the NFT. On successful claim of the warranty, the warranty is minted in the chain and added to the active list of the owner and can be used to prove ownership till the expiry date. After the Warranty is added to the Active Warranties of the Buyer, the buyer can transfer ownership as well in the case of Resell of the Product the Current Owner needs to put in the New Owners Wallet Address after which it is issued using the same hashing method as Soul and then the new owner needs to prove ownership in a similar process as the previous owner. Once a warranty is activated by an owner in their dashboard the warranty also shows the history of all it's the previous owner who helps in keeping track of the ownership of the product and sales as well. The automation of the Expiry of the NFT was handled using Gelato Ops. Once the NFT reaches it’s expiry the NFTResolver written on Gelato Ops calls the burn function itself to burn the NFT and only the previous data is kept as a record but the NFT can no more be used as a warranty. We treated each warranty as a different page with the details mentioned in the NFT itself which is then rendered into the Frontend of our application. For making the GUI we used React for the frontend and Web3.js for the integration of the frontend to the smart contract. Challenges we ran into The buyer has to put in the details manually on the platform now. This limitation can easily be overcome by implementing a marketplace for the customer to shop for and the seller to post products on. Loyalty Programs could not be added due to Time Constraints but can be implemented as we convert this plugin into a full-fledged application. As the minting of NFTs takes a considerable amount of time waiting period for a contract to execute it makes the overall program slow as in other DApp as well. Accomplishments that we're proud of Solved the issues of having a physical form of warranty cards which can easily be lost or damaged. Created a simple user interface for easing the life of sellers who can keep track of issued warranty cards and check their authenticity of it. Providing a better and transparent mode of customer service for the buyers after their purchase for the duration of the authentic warranty period. Provided a safe method for the issue of warranty and keeping its data safe from any malicious changes for one's personal benefit. What we learned Learnt new technologies during the making of the project during this hackathon and implemented it into the project as per the requirement. Collaborated in a team to make the project using the strength of each other and learnt various new things quickly during the process. - What's next for NFTDocket We can implement this in a Mobile Application to further increase the accessibility and use cases multi-folds. As we are using Soulbound NFTs in the application this can also be used to issue certificates that are issued uniquely such as Degrees, Tickets, Citizenship and much more. We can implement a Gamification in this platform in which every issued warranty NFT transfers some credits to the Seller which can later be redeemed on the same platform using different schemes. These credits can also be used as gas fees for issuing NFT Warranties by the sellers which will promote more and more businesses to implement the NFT Warranty system in their systems. We can implement a marketplace to make the process truly one click. We can use the history tracking functionality to keep a track of sales which can be used in products like cars that frequently change hands. As the marketplace is implemented we can also add the functionality of sending the NFT on the buyer’s mobile phone as a notification. <div