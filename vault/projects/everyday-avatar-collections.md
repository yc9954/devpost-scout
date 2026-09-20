---
slug: "everyday-avatar-collections"
url: "https://devpost.com/software/everyday-avatar-collections"
title: "Everyday Avatar Collections"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1001
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Everyday Avatar Collections

> A dynamic NFT like a paper doll, where you can own and swap all the clothes and accessories, on-chain!

[Devpost](https://devpost.com/software/everyday-avatar-collections) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]]
**substrate** [[financial_record]] [[video_visual]]

**stack** hardhat, moralis, node.js, polygon, solidity, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for everyday avatar collections

## Body

minting page overview of collection Inspiration (Demo dApp) As a newcomer to the crypto space (after the NFT boom last year), I saw lots of really cool project, but was too late to participate in them. The projects were either long minted out or had incredibly high floor prices on the secondary market. I had been out-timed and out-priced from participating. The Everyday Avatar is a profile-picture style, dynamic NFT project, on a mission to be affordable and available to all who wish to participate in this crazy-fun world of crypto! What it does Everyday Avatar is an NFT version of the paper doll toy, and you have access to the entire collection of components to choose from while playing with your Avatar! Just like a real paper doll, you start with a base character and can swap out the accessories and components to your every whim, like the clothes, accessories, hairstyles, etc. Using our dApp you can change or update your Avatar anytime you want, EVEN AFTER YOU MINT! All the components and attributes are stored ON-CHAIN. To make it affordable, the minting price is pegged to the USD! So when Matic prices rise in the next bull market (along with interest by newcomers), our project will remain affordable! Gas costs are also kept low thanks to the Polygon network, for every time you want to change and update your Avatar's look. Our project is one that is built to last, and with no collection upper limit, everyone can own their very own Everyday Avatar! No more high secondary sales, just a fun project anyone can join, regardless of when they learn about us. How we built it The Everyday Avatar project is implemented in three parts: the React Frontend, the Solidity Smart Contracts, and the Webservice Backend. We built our Avatar's smart contract using openzeppelin ERC721 and the EIP-3664 standard by DRepublic Labs to manage the components for each NFT token, and handle updating the attributes on-chain. The USD priced-pegged functionality was built using a chainlink price-feeds oracle. It's called in a public function to update the contract's minting fee. Anyone can call this function, but it's planned to be called once daily by a chainlink keeper. The backend API service was implemented using node.js, and manages the image resources for our Avatars. The individual component images are stored on IPFS, uploaded via Pinata, and then cached locally on the server. We then implemented two endpoints, one to create the image, and the other for smart contract interaction, building and pushing the updated Avatar's CID into the URI. The react frontend was built to display an avatar, along with our component collection, allowing the users to pick-and-choose the components they want to use. We choose chakra as our UI component library, which has helped us to develop faster. We integrated our react-app with Moralis react-moralis for all our smart contract interactions. We also used the Moralis Web3 NFT API to build the Avatar cards, which simplified how to display the images and metadata. Our dApp currently only supports Metamask as the wallet provider, with more planned to help with onboarding. Challenges we ran into In the original iteration of our project, we used a chainlink oracle in order to update the IPFS CID on-chain. The oracle added a significant cost to the upkeep of the dApp, and wasn't in line with our objectives of keeping the project affordable. We still wanted to avoid ERC-712 signatures and the complications to the user experience, so we updated our contract to implement role-based permissions. This allowed us to have our backend interact directly with the smart contract using the URI_UPDATER_ROLE. So when a request to update the IPFS on-chain for an Avatar, it's handled 100% by our updated backend function. Accomplishments that we're proud of I wanted to create a crypto project that anyone can get involved in, regardless of how or when they find us. This means a project that is NOT all about the money, rarity reveals, or the moon for that matter! Let us take a step back from all the charts and graphs (especially now that they are pointing down instead...) and let's just have some fun with NFTs for a change. Here are some of the benefits and improvements over "Traditional" NFT projects we are proud to have included in our project: Everyday Avatar "Traditional" NFT Projects ✔️ Unlimited Collection Limited Collection, limited owners (thanks whales) ♾️ Mintable Forever "Can" mint out quickly (usually by bots) 🧔 Choose how your Avatar looks Randomly assigned at reveal (what if the art sucks?) 🔗 Dynamic on-chain metadata Static metadata and images on IPFS (simple but effective) 😊 Stable and Low mint fee (pegged to USD) High-cost barriers on secondary market (seriously who pays those prices!?!) 💸 Long-term revenue potential (for dev team) Revenue ends when minting ends (and devs are off to the next cash cow...) In reality, the biggest accomplishment is that we built a really cool web3 product and it works! Both Hussain and I are newer to the web3 space, so this was really a project about jumping into the web3 space; no longer being just spectators! What we learned We learned a crap-ton from this Hackathon, between the sessions and actually building Everyday Avatar: ChainlinkClient APIs like Oracles and Price Feeds How awesome Moralis is, and how easy it is to interact with the smart contract. Makes your life so much easier when Moralis is the only SDK you need! How to implement gasless meta-transactions How to build and deploy a backend API and front end server How to use IPFS in the client code AND in our backend server What's next for Everyday Avatar Collections The Everyday Avatar is destined for the Polygon Mainnet, and our next steps include: Working with artists and illustrators to make some outstanding and beautiful Everyday Avatars Revamping our UI's onboarding and educational elements to target a larger market Hardening the backend API to support the Mainnet launch <div