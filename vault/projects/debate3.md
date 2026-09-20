---
slug: "debate3"
url: "https://devpost.com/software/debate3"
title: "Debate3.xyz"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 650
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Debate3.xyz

> Decentralized Discussions for DAOs

[Devpost](https://devpost.com/software/debate3) · hackathon [[EthCC Hack 2022]]

## Facets

**substrate** [[document_pdf]] [[financial_record]]

**stack** hardhat, next, react, solidity, tailwind, truffle, typescript, vyper, wagmi

## How they structured the write-up

- inspiration
- pitch & live demo (video)
- what it does
- how we built it
- challenges we ran into :
- security of the protocol :
- accomplishments that we're proud of :
- what we learned
- kleros proof of equilibrium proposal
- what's next for debate3

## Body

Landing page we are multichain ! Forum Creation Accessing a Forum ( must have membership to see the content ) Give membership to an account ( done by the moderator ) Contribute , Discussions More on Discussions Moderators can give badges to users Types of badges Phone view with current stored forums Join a Forum ( if you have the membership ) Inspiration We wanted to solve the problems of low engagement in DAO/community forums and bring decentralization in this field to a completely new level. 🔥 Pitch & Live Demo (Video) https://www.loom.com/share/eceff0a8233d4c47aa2cdbc4f5f8333d What it does In a few words, our protocol lets you create a Forum, which is fully decentralized and privacy-first (Privy and Orbis as storage solutions) as well as completely tokenized . We mint the Forum logo as an NFT, we mint Membership NFTs for access control, moderators can mint award badge NFTs, and the latter are summed up dynamically on-chain into reputation NFTs. We incentivize engagement not only via reward badges but also with an innovative on-chain reputation slashing algorithm that decreased your reputation over time if you don't contribute regularly. We are already live (debate3.xyz) and have working multichain deployments on Cronos, Neon, Celo, Gnosis, and Polygon. Because different communities demand to have their tokens in the ecosystem of their choice. How we built it The stack: Front-End: NextJS, React, Typescript, TailwindCSS (twin.macro), Rainbowkit/Wagmi, Turborepo/pnpm Contracts: Solidity & Vyper (Truffle) Back-End: Privy, Orbis, IPFS Technologies: We are deployed on all chains : Cronos, celo, neon, polygon, gnosis. We have ERC721 for memberships and ERC1155 for badges : all metadata is stored in IPFS Challenges we ran into : -> Building a working multichain environment in a hackathon is not simple, you have to manage a lot of deployments, addresses, inform the user to switch the chain, etc. – This was quite some work. -> As you can not auto-execute transactions on chains nor run native cron-jobs we had to invent an implicit (passive) on-chain recalculation algorithm. Security of the protocol : Our protocol is secured through its smart contract, we give a maximum number of badges that a protocol can award to their contributors. Reputation score decreases along the time goes by, to prevent users getting rewarded after a long time of inactivity. Accomplishments that we're proud of : We are live on all the chains! The UI works and looks slick. We managed to implement cool features that make our protocol safe and scalable and even did it in both: Solidity & Vyper. What we learned We learned that it is hard to implement a fully on chain discussion system because of incentivation, privacy, and security. Also many score mechanisms can be proposed in order to improve the protocol. Kleros Proof of Equilibrium Proposal See our proposal: https://github.com/wottpal/debate3/blob/main/Proposal_Kleros.pdf . – We think our solution offers many nice opportunities to integrate Kleros. What's next for Debate3 We have awesome ideas for future features to integrate : 1) Together with our "Proof of Equilibrium Proposal" some interesting Soulbound-like / Proof of Humanity features could become reality. Because actual contribution in a community (+ rewards) proof your humanity. 2) Contribution/Reputation Leadboard to even incentivize contribution more. 3) Our dynamic reputation NFT should get an on-chain rendered SVG with the actual score inlined. 4) Fund Distribution Support : Moderators can do random airdrops on a Forum , fairly distributed based on reputation score. Owners of protocols can reward contributors without scrutinizing their reputation score 1 by 1. 5) Moderator Governance / Elections 6) Dynamic Reputation Transformations with additional access-gated content: currently our protocol lets users redeem badges of higher levels using other badges, for example 5 bronze badges made into 1 solver badges. we want to improve this feature by using dynamic svgs on our 1155 , when a user reaches a certain number of badges of one type, another badge is minted automatically. 7) Mainnet 🚀 <div