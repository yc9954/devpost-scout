---
slug: "jeffrey-the-dinosaur-s-dinotastic-blockchain-adventure"
url: "https://devpost.com/software/jeffrey-the-dinosaur-s-dinotastic-blockchain-adventure"
title: "Jeffrey The Dinosaur's Dinotastic Blockchain Adventure"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 465
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
---

# Jeffrey The Dinosaur's Dinotastic Blockchain Adventure

> Introducing people to blockchain through a timeless classic

[Devpost](https://devpost.com/software/jeffrey-the-dinosaur-s-dinotastic-blockchain-adventure) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
  <sub>weak: web_dom</sub>

**stack** blender, css, html, ipfs, javascript, near

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Inspiration We wanted to dip our toes into the world of blockchain, and then we heard about this hackathon. After reading through the sponsor challenges, we realized that Brave's Dino challenge seemed like a good place for beginners to start - we didn't have to spend any time wondering what we were going to do; only how we were going to do it. What it does Jeffrey the Dinosaur's DInotastic Blockcahin Adventure allows users to log in with NEAR and equip skin NFTs from their wallets. The mechanics of the game are largely the same as the original (although our cacti are a little taller). How we built it We started with a base of the open-source T Rex Runner repo provided in Brave's challenge description. From there, we implemented a new spritesheet in blender and updated the hitboxes accordingly. Afterwards, we integrated NEAR login and the ability to see dino NFTs in-game using their Javascript API. We used IPFS to store our skin NFTs. Challenges we ran into There were a few big components/ideas we either couldn't figure out in time or just didn't get to: (1) DINO coins. We successfully minted $DINO by deploying a FT contract to testnet, but were unable to figure out a secure way to reward players with $DINO in time for the project submission. (2) NFT marketplace. Currently, any skin NFTs a player has must be manually given to them; there is no mechanism for players to see and purchase new skins (3) Blockchain Data Stream. One of the features we were excited to implement was replacing the ground that the Dino runs on with a stream of data from NEAR's blockchain (preferably from a user's own account or from our primary smart contract), so that the Dino could literally "run on blockchain." Unfortunately, we ran out of time. Accomplishments that we're proud of We heard about this project on the later side (beginning of February) and, being students, couldn't really do much until after our midterms. This left us about a week to do the project. We're proud of the fact that we went from never having touched blockchain code to (1) deploying our own smart contract (albeit from a template) and (2) tying it in to our game on the frontend. We're also proud of the skins we produced for use in the game (especially Jeffrey's voxel style). What we learned The primary lesson we learned from this was about the structure/organization of blockchain applications. Coming from traditional Web2 technology, reading the NEAR docs felt a bit like drinking from a firehose, but it was worth it. Overall, we feel that now that we've done the project, the next time we have a blockchain project we'll be able to get off the ground must faster. <div