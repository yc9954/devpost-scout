---
slug: "hexploration"
url: "https://devpost.com/software/hexploration"
title: "Hexploration"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 444
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/general_public"
---

# Hexploration

> A true on chain multi-player exploration game, attached to an unreal frontend. Utilizing Chainlink VRF and Keepers to seed and progress game state.

[Devpost](https://devpost.com/software/hexploration) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**user** [[general_public]]

**stack** c++, chainlink, githhub, javascript, keepers, solidity, unreal-engine, vrf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hexploration

## Body

Inspiration We wanted to connect a blockchain backend to an Unreal frontend for the best of both worlds. We wanted the decentralization, multiplayer scaling potential of the blockchain, plus the amazing graphical capabilities of Unreal Engine. Blockchain processed games are going to play a huge role in fair gaming of the future, but how do we reconcile the pace and cost of blockchain with the speed of modern computer gaming? What it does Hexploration is a multiplayer exploration game that can be played on chain, regardless of the frontend. We found the pace of a board game is about where the sweet spot of blockchain game processing currently stands so with this project we really leaned into the board game experience. You play as part of a team working together to extract artifacts from an uncharted land. Explore, dig, and battle as a team to make it off the planet alive! How we built it We used solidity for coding the game logic, a custom command line interface for testing, Unreal Engine for the UI, and some javascript / C++ magic in the middle. We turned back to an earlier version of Unreal in order to be able to output our project to html5, which allows us to make use of some browser features such as connecting to metamask. We connect with Chainlink VRF to obtain randomness for dice rolls, card draws, and other environmental effects. Challenges we ran into Connecting a web3 wallet through Unreal was difficult, but we found a couple paths to accomplish this. Contract limitations as far as size and density of functions is always a challenge with game design. We are always trying to find the minimum amount of information to store and transact, as updates can come with a substantial cost if not properly optimized. Accomplishments that we're proud of We were actually able to connect the blockchain backend with the unreal frontend and send information both ways. While this is mostly a tech demo at this point, we are excited to continue building this out until we have a fully playable game we can release to the public. What we learned How to connect a blockchain processed game to an incredibly powerful frontend. We learned that even a small slice of a mid-sized game such as this, can be quite a bit to build, in these relatively uncharted waters. What's next for Hexploration Finishing the game! We want to keep building out the graphics, optimize the game logic, and expand out to fill the game that we’ve designed. This is only the beginning of our journey and we hope you’ll all come along for the ride. <div