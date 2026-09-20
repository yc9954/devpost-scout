---
slug: "near-karts"
url: "https://devpost.com/software/near-karts"
title: "NEAR Karts"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 709
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/educator_student"
  - "substrate/video_visual"
---

# NEAR Karts

> Dynamic NFT Battle Karts on NEAR

[Devpost](https://devpost.com/software/near-karts) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[educator_student]]
**substrate** [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** blender, blockchain, css, html, javascript, near, react, rust, three.js

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges faced
- accomplishments
- what was learned
- what's next for near karts
- sponsor challenges

## Body

Garage Pre Battle Battle NEAR Kart NFT Artwork - NEAR Propulsion Artwork - NEAR Blockchain Transmission Artwork - Bottle of Borsh Artwork - Hold on to your cats Inspiration Wanting to build and battle 3D Battle Karts!! There are many NFT collections based around 2D characters. For my first NFT app I wanted to explore what was possible when generating dynamic 3D NFTs of karts. What it does A system for creating dynamic NFT battle karts. The garage has two areas: equipment and pimping. The creator can view updates to their 3D Kart in real time. When the Kart is just right, it can be minted on NEAR. The image is sent to a server for signing and uploading. The data is then minted on NEAR which verifies the image content is signed. Battle mode is a simple on chain game with text summary. The main purpose of battle mode is to add randomness and suspense to dynamic NFT creation. Equipment has no effect on the result of the battle. It just makes the Karts look cool. Winning battle = 1 level up + chance of winning decals Higher levels = Better equipment Every 5 levels the Kart NFT can be upgraded. How it was built NEAR Contract - Adapted the NEAR NFT tutorials to support verified minting with equipment checks and battle mode Front End - Created with ReactJS, 3D with ThreeJS, and contract interaction with near-api-js Imagery - Karts and 3D in Blender, with images and textures in Inkscape and Gimp Challenges Faced Most challenges involved the limitations of Blockchain. Such as only being able to upgrade code, not data, without recreating a contract. Using logs and indexing to summarise and communicate information. Verifying NFT data submitted from the creator's browser. There were challenges around usability in terms of the user being redirected away from the app and back again when using the wallet. Accomplishments Creating my first major smart contract application. The look and feel of the app. What was learned That you can't borrow a ref that was borrowed as mut or something like that. Aka Rust language! There were a lot of lessons learned around the limitations and conventions of smart contracts. What's next for NEAR Karts Only limited equipment is added in this demo version. More equipment will make the app more engaging. In future, only one Kart with each name will be allowed to be minted. This will enable the main dynamic of the game: The aim is to choose a name that will go perfectly with the kart style you hope to unlock. Names like Fatkart Slim, with acid house styling would be more valuable than more generic combinations. As more decals and equipment will be added over time, this creates an incentive to continue to interact with system. The game is a simple coin-toss type game. More complexity could be added to take account of Kart equipment / strategy while remaining within gas limits. Because the Karts are NFTs, the future uses are limitless. An off chain battle/race game can be created. The promo movie is one example of how the NFTs can be put to other uses. Sponsor Challenges Paras Decentralized App using NFT NEP-171 standard NEAR Karts NFTs are NEP-171 NFTs on the NEAR blockchain. non_fungible_token_core, non_fungible_token_approval and impl_non_fungible_token_enumeration are implemented for the NEAR Kart NFTs. nft_mint is modified to allow minting only when with verified nft data is provided. NEAR Kart NEP-171 Implementation The Graph Integration ⚠ The graph indexer reaches a certain block and then stops indexing so the leaderboard in the application does not stay up to date. This has been reported on Discord The Graph is integrated into the application to provide daily and monthly leaderboards. The NEAR Karts Subgraph also provides: A historical record of the NFT for each kart as they are upgraded Battle details that can be used to replay previous battles Records of minting and upgrading events NEAR Foundation - Calling all Liberal Artists As part of the development of the promo movie , a collection of 4 artworks were created focusing on the efficiency and speed of NEAR blockchain. The artwork is styled as promos / posters for automobile products. The full size renders are located in https://github.com/ben-razor/near-karts/tree/main/artwork/images/game/collection <div