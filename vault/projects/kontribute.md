---
slug: "kontribute"
url: "https://devpost.com/software/kontribute"
title: "Kontribute"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 915
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "user/developer"
---

# Kontribute

> Kontribute brings readers, writers and NFTs together. Write some lore for your NFT collection or support your favourite writer by buying their NFTs - Web 3.0 creative writing with NFTs

[Devpost](https://devpost.com/software/kontribute) · hackathon [[Supernova]]

## Facets

**domain** [[civic_government]] [[developer_tools]] [[media_journalism]]
  <sub>weak: supply_logistics</sub>
**user** [[developer]]

**stack** icp, motoko, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kontribute

## Body

Featured and Recent Stories NFT Marketplace Single Story Text editor for writing a story NFT Launchpad User NFT Inventory Large View of NFT NFT Filtering Kontribute on a Mobile Phone Inspiration Kontribute was inspired by the idea of wanting to give everyone a use case for their NFTs as well as giving creative writers a platform on web 3 to write on and benefit from. We decided to combine both of these ideas to bring NFTs to storytelling. Readers can support their favorite authors by purchasing their NFTs, giving authors an incentive to write good stories and make good NFTs. What it does Kontribute allows readers, writers, and web 3 enthusiasts, to write and read stories, or sell and trade NFTs from their stories all within our dapp. To achieve this we have integrated a creative writing feature, a story section, and an ICP wallet in the dapp - users can directly hold their NFTs and ICP all within Kontribute. Kontribute gives writers a place to share their stories with a community and a way for them to sell NFTs from their stories. Readers may want to support an author's story by purchasing their NFTs. Larger projects with large stories and a large collection of NFTs can also launch stories and NFTs on the dapp via our launchpad. How we built it Kontribute is fully decentralized and built on top of the ICP blockchain from frontend to backend and we take advantage of the many tools that it provides including Internet Identity, DFX, and Motoko. Our frontend is made with React.js and uses lots of modern react techniques such as functional components with hooks, dynamic components, and React-Redux for state management. We have multiple frontend integrations via npm packages that let us call other smart contracts on the ICP blockchain most notably NFT Anvil smart contracts(also written in Motoko) - which power our NFT integration and ICP Wallet. For our UI and design, we use Chakra UI which allows us to build fast and responsive UI's that look nice on desktops and mobile alike. Our backend has two main smart contracts launched by us. One for our initial token offering or ito.mo which powers our NFT launchpad and lets us launch our Bonsai Warrior NFT collection. We also have story.mo which is the smart contract that powers our story section of the dapp which lets us store all user stories on the chain, to be called dynamically to our frontend. All of this makes Kontribute a multi-canister dapp. For a more detailed description of the development of our dapp and our code design decisions, you can read our GitHub README . All of our code is open-sourced and available for the community to look at and/or learn from. Challenges we ran into Building an app on ICP is much different than normal app development and there was a learning curve to figure all the new tools out. We found once we understood the idea of canisters, principals, and how to launch our front-end on-chain - things started to flow. Building out smart contracts in Motoko turned out to be a challenge as there were new concepts for us such as orthogonal persistence and the actor-based model. Accomplishments that we're proud of So far we are very happy with the success we have had thus far. Sold out our Bonsai Warrior NFT collection of 1100 NFTs within 5 hours raising 1500 ICP . 300 monthly users on the dapp already. Almost 2k followers on Twitter and 1k members in our discord. We have projects reaching out to us daily about using our dapp and we have joined multiple community calls and Twitter spaces with ICP journalists. We have also engaged with other dapp developers in the ecosystem and have multiple partnerships with different projects that we work with very closely such as NFT Anvil and Usergeek. What we learned We found ourselves thinking a lot about dapp architecture and how to create dynamic frontend components that interact with our Motoko backend. The async nature of the smart contracts also meant we had to think about how to properly display the information to our front-end and how we can notify the user of what's happening. We have learned and are still learning many new features of Motoko as a smart contract language. Building out this project and growing a community around it turned about to be a new sort of challenge for us as well. We know we have a niche audience that we can attract and we feel we have a product-market fit, So we have had to figure out how to grow an audience and keep them engaged all while we develop our dapp and launch new features. What's next for Kontribute We have about 5 other larger ICP NFT projects wanting to launch on our platform, as-well-as many writers who cant wait to get on board. We have many features lined up for improvements for the stories and marketplace sections of our dapp some of which that are currently being worked on are: Trade history for the marketplace. draft stories. story likes. voting options for interactive stories. We also have plans to add extra use cases for our Bonsai Warrior NFTs including claiming airdrops and using them to access the content. We want to scale the dapp out now as much as possible and try to cater to as many web 2 writers as we can and bring them over to web 3. <div