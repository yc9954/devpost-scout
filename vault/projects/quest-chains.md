---
slug: "quest-chains"
url: "https://devpost.com/software/quest-chains"
title: "Quest Chains"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 500
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# Quest Chains

> We are building a gamified learning / web3 onboarding platform which through questing structures rewards users upon completion.

[Devpost](https://devpost.com/software/quest-chains) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]]
**substrate** [[video_visual]]

**stack** chakraui, filecoin, ipfs, nextjs, thegraph, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for quest chains

## Body

Inspiration We recognised that DAOs don't have a standardised approach to onboarding, so we wanted to build a platform to provide a way to gamify the onboarding process with a set of quests that award the quester with an NFT. While building it we realised we could make the whole app much more flexible by not targeting only DAOs and their onboarding, but providing a system that enables creation of any kind of quest chain. Basically a fully decentralised web3 version of course platform, which also provides functionality to create courses. What it does The platform enables both creation and completion of quest chains, which is a gamified equivalent of courses. Quest chains consist out of quests, which can be completed by submitting a proof of completion. Upon getting all of the submissions approved the user becomes eligible to mint a soulbound NFT which serves as a certificate of competence. The quester profiles show a gallery of acquired NFTs and any pending actions. During the quest chain creation process you can make a 2D or 3D design or upload a custom image for the NFT the questers will be able to mint after completing all of its quests. Quest chain owners are able to set up roles of the chain, which have cascading permissions. Admins can create and edit quest chains and quests. Editors can create, edit quests, disable and enable them. Reviewers can accept or reject submitted proof of quest completion. By creating this fully decentralised system we hope to empower quest givers and questers of web3 mainly to bring a unified & fun structure to DAO onboarding & generally provide a flexible system to create any kind of a set of tasks. On top of building a platform we want to also offer its functionality through an SDK for seamless integration in any dApp on any network. How we built it We have used Next.js and Typescript + ChakraUI for blazing fast development. From sponsors we used IPFS because it offers a really convenient way to store any kind of data, so we were able to define the whole structure of the questing system along with roles and permissions through it. We queried the data with The Graph because it also provides a very convenient solution for querying more complex structures from the blockchain. Also none of the IPFS hashes are stored on the blockchain but only emitted in the events and these events are picked up by our subgraph and destructured into the graphql schema for easy querying. Challenges we ran into Upgradability of contracts, which will be implemented soon. Figuring out roles system. Accomplishments that we're proud of Implementing the 3D NFT creator component! What we learned That we can be very happy for having an amazing team. What's next for Quest Chains Creating a DAO through Yeeter. Enabling an SDK so any dapp will be able to make use of our system on their platform without having to navigate to ours. Expanding the team. <div