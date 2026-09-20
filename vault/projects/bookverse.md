---
slug: "bookverse"
url: "https://devpost.com/software/bookverse"
title: "Bookverse"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 973
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/security_privacy"
---

# Bookverse

> Bookverse empowers book authors by providing community of digital readers a marketplace for NFT books (Think of Bookverse as NFT Books marketplace where users can Mint, Sell and Buy NFT Books)

[Devpost](https://devpost.com/software/bookverse) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[civic_government]] [[developer_tools]] [[security_privacy]]

**stack** cosmos-sdk, golang, ipfs, nextjs, react, starport

## How they structured the write-up

- inspiration
- the problem bookverse solves
- what you can do on bookverse
- how we built it
- challenges we ran into
- what does the bookverse mean to me and how is it different from existing ideas?

## Body

Mint a Book NFT (1) Mint a Book NFT (2) Sell a Book NFT (1) Buy a Book NFT (1) Book Collection(1) Author's Dashboard Sell a Book NFT (2) Buy a Book NFT (2) Book Collection(2) Inspiration Non-fungible tokens (NFTs) and Cryptocurrencies have experienced a surge in interest on another level recently, and several celebrities, high profile people such as Jack Dorsey, Elon Musk and many more have shown a very keen interest toward them, some of the good artist and digital creators also have sold their digital artworks, music and other digital collectibles on different different NFT marketplaces as NFTs. For example a Canadian artist has sold a “virtual home” which was his own creation for nearly half a million dollars in March, 2021. Music, digital art, AI generated art and digital collectibles are already selling on NFT marketplaces and have already become a hot and cream market in the Crypto world, selling something such as books, especially Sci-Fi books, works of fiction or any other bestselling self help book, on these NFT marketplaces has yet to be done and requires a good architecture based platform Hence born the idea for “Bookverse” - an end to end platform which can serve as marketplace for readers where authors can put their books as Non-fungible tokens (NFTs) . The problem Bookverse solves When we buy an ebook on any online platform for example on Amazon, or any other similar service our ownership over that commodity is very different from a physical book that we can keep with ourselves as long as we want. Yes, we bought an ebook on these online services, but we only and only have it for as long as Amazon or that other service is around and agrees to keep providing it as a service. If Amazon or that other service crumbled tomorrow or discontinues its services due to any reason, that book would disappear with the rest of its platform but we had purchased it Right?! We have the ownership, here comes the breach if we put it in very simple sentences we don't have any moral or physical contract with amazon to provide its services and even if amazon wants to continue providing its services and our government bans amazon from their end then who should we address? . From this horizon, Non-fungible tokens (NFTs) have many more things in common with print books — it’s our possession, ownership, period. It won’t disappear at the whims of an outside party or government or organization. In fact, with NFTs, we don’t just own a copy of a book, we own a specific copy within a series of copies. Think first edition, second edition, and so forth of the book for which NFTs have been created. Also, the final cut after the sell from a ebook from other platform such as amazon or other similar platform that reaches Book Author is not much as compared to their efforts, Hence we need some out of the BOX solution for this problem and hence something such as Bookverse will be great idea to introduce in this space. What you can do on Bookverse Bookverse is world’s very first marketplace where anyone can : Authors can Mint their Books as NFTs Authors can Sell their Books as NFTs to the readers by fixed-price Readers can Buy Books as NFT from different different Authors directly by paying a fixed-price. Readers, Authors both can Transfer the NFT books (on-chain/cross-chain thanks to Cosmos IBC) directly to a friend or someone who is interested in P2P transfer. Bookverse leverages the power of IPFS to store token metadata and the power of Cosmos IBC to be able to transfer ownership of NFT Book on cross-chains (The Cross-chains part is not included in the demo because it is just DEV Done) How we built it I have used Cosmos SDK , which is the world’s most popular framework for building application-specific blockchains. The basic codes, like different modules, messages, types with CRUD operations, Inter Blockchain Communication packets tor transfer ownership of NFT Books on cross-chains, all this code was scaffolded using Starport . Since Starport and the Cosmos SDK modules are written in the Go programming language, hence I have got a grasp of Golang during this Hackathon. It was a very fun experience working on these Technologies and building my own business logic for Bookverse, And for the Frontend part I was working on ReactJs and NextJs for a while hence got a good grasp over it so it was not a big task for me to create a better UI and UX with these Technologies. Besides all these great technologies of Cosmos Ecosystem, I have used IPFS to store metadata of each Book NFT, the specific service that I have used is called nft.storage which is built specifically for storing off-chain NFT data. Data is stored decentralized on IPFS, and is referenced using content-addressed IPFS URIs. Challenges we ran into Cosmos Interchain Blockchain Communication Protocol’s Packet Relay was a bit complicated for me and took a lot of time to figure out how can I Broadcast the Heavy Data Payload to another chain, hence the The packet relay in Cosmos IBC took me much time. Sometimes the packets could not broadcast to another chain when payload data is larger than data in examples. Hence cross-chain Transfer of NFT book is Dev Done and will be updated in Demo. What does the Bookverse mean to me and how is it different from existing ideas? Bookverse to me is my own Startup Idea that I am planning to BUIDL also, the purpose of my startup bookverse is not just to provide the fancy services or hype up the NFT craze but is actually to solve a genuine problem that the Book Author and reader community is facing nowadays. <div