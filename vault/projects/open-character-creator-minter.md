---
slug: "open-character-creator-minter"
url: "https://devpost.com/software/open-character-creator-minter"
title: "IC Avatar Creator"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 737
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
---

# IC Avatar Creator

> The IC Avatar Creator allows users to create and manage avatars for the open metaverse. The project includes GLB avatars that are minted to the Internet Computer using the DIP721v2 token standard.

[Devpost](https://devpost.com/software/open-character-creator-minter) · hackathon [[Supernova]]

## Facets

**substrate** [[code_repository]]

**stack** internet-computer, motoko, node.js, react, react-three-fiber, rust, three.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ic avatar creator

## Body

Inspiration The aim of this project is to provide newcomers to the open metaverse with a way to express their identity through a 3D avatar that they can own and use on a wide variety of platforms. Hosted entirely on-chain via IC, users are able to create their avatars as NFTs and secure or trade them using a crypto wallet and decentralized identity. Users can view their avatar from the same canister the assets are stored in, and even inspect it interactively in Plug wallet. This provides a unique and powerful solution for users who wish to have greater control over and connection to their online identity. What it does The IC Avatar Creator is a project that enables users to mint their own Avatars for the metaverse and store them fully on-chain. The project is 100% on-chain and leverages the power of the canister architecture to provide a seamless experience for users. The project consists of the following features: Front-end hosted directly on a canister This allows for a fast and responsive user experience that is directly integrated with the canister architecture. Plug & DAB integrations This allows users to easily mint their Avatars as DIP721v2 NFTs. GLB Avatars minted as DIP721v2 NFTs This allows for a high degree of interoperability for users when minting their Avatars. Assets stored in asset canister This ensures that all user data is stored securely on-chain. How we built it This project was a team effort, with all members collaborating inside the Outpost. The smart contracts used by the program are written in Rust and Motoko, and hosted on the Internet Computer. We used React and TypeScript for the front-end, which is also hosted on the Internet Computer. We used the DIP721v2 canister for the NFT, as well as a Motoko-based storage canister for receiving and storing the static assets. We used Psychedelic Plug and DAB functions for handling the core actor/agent based logic. The NFT canister was registered to the DAB registry for full functionality when using Plug and DAB. Challenges we ran into 1) Chunking large assets into a storage or assets canister prior to running the mint function. 2) Creating and designing good-looking 3D models and assets for the project. Accomplishments that we're proud of We are proud to have accomplished the following: DIP721v2 integration and minting functions working from the UI Canister asset storage working for storing assets fully on-chain Interoperable 3D NFTs using the GLB model standard What we learned We learned that the Internet Computer has some limitations that will require further development to solve. Delivering large static files from a canister was not well documented, and required digging deep into other open-source projects to figure out how they were solving certain aspects of the batching and chunking of files. Through our work together, we were able to identify these limitations and develop strategies to overcome them. This experience has taught us the value of collaboration in problem-solving and we will carry this lesson forward into future endeavors. What's next for IC Avatar Creator The IC Avatar Creator has seen great progress so far, and we plan to continue growing it. It will aim to become the base repository used by the Outpost for minting open-metaverse avatars on the IC. This will allow us to apply for grant work around the IC Avatar Creator and have multiple projects use it. The code will become open source, so anyone will be able to contribute. We are really excited to offer engine integrations and enable communities to have their own avatar sets. Right now, 3D tools are just too complicated for most users, but the default avatars that come with any engine rarely represent them. Most communities have a few strong creators, but they aren’t able to make custom assets for everyone. Avatar creators like this simplify the number of options and meet both users and creators where they are. We foresee a shift from high-value, exclusive random generations to much less expensive and inclusive sets that offer customization, and we hope that future NFT projects will fork this one and build toward the open metaverse with it. From our Supernova hackathon, we packaged a standalone avatar creator React component, as well as a Plug wallet provider for making interacting with the IC less complicated. Both of these projects are now available on npm – we’ve added links to these packages in the links section <div