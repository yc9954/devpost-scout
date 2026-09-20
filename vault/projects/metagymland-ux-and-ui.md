---
slug: "metagymland-ux-and-ui"
url: "https://devpost.com/software/metagymland-ux-and-ui"
title: "MetaGymLand"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 799
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/structured_db"
---

# MetaGymLand

> Smart Fitness and wellness platform for a decentralized world. A virtual gym where you can actually move physically

[Devpost](https://devpost.com/software/metagymland-ux-and-ui) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[labor_employment]]
**substrate** [[structured_db]]

**stack** adobe, ai, blender, chainlink, figma, filecoin, ipfs, javascript, mediapipe, mongodb, moralis, phaser.js, polygon, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for metagymland
- disclaimer

## Body

MetaGymLand MetaGym Canals MetaGymLand MetaGym Runner MetaGymLand Inspiration Our initial inspirations were our own struggles with keeping work/life balance during the pandemic. We have learned that: 577 mln people are affected by back pain globally Over 80% of adults are estimated to experience back pain in their life (mostly desk workers) People are failing to take healthy quick work breaks because they are too hyper-focused on what they are doing (forget) and they are finding standard workout/exercises boring We wanted to find an easy and accessible solution that adds gamification for daily workouts. We decided that including NFTs and tokenization will be another great asset for this project which will boost the incentive aspect for the users 🚀 What it does MetaGymLand is Gamifying Daily Stretches and Workouts You can: [x] Play minigames by moving your body [x] Mint your NFT [x] You will need to enable your webcam for pose detection [x] Enter MetaGymLand virtual gym room [x] Then you can move your body, and your NFT avatar will move with you 🤯 🙂 [x] Play minigames hidden in gym mats [x] You can earn XP points [x] Unlock locked Gym Rooms by completing the minigames in the current room [x] After unlocking all the rooms and gaining at least 10.5 XP you will be eligible for an NFT reward [x] Mint your NFT reward How we built it Tech used: TensorflowJS and Mediapipe deliver all the AI pose detection capabilities moralis.io makes talking to blockchains easier and faster moralis.io is used as a [Bakcand As A Service] tool here, we use moralis objects as our Database Chainlink VRF is used for NFT minting with fair distribution NFT mint price stays the same, then the smart contract based on randomization from Chainlink VRF will decide which NFT you will get Chainlink VRF is used for drawing NFT rewards after completing milestones in the game Polygon is used as the main L1 Blockchain on top of which all the MetaGymLand digital assets are built. GymBuddies NFTs are on Polygon Mumbai Testnet IPFS and filecoin is used for NFT storage by utilizing nft.storage Phaser is our Metaverse game engine React for the frontend Github Pages for deployment And Spheron for deployment We integrated Sequence Wallet connection Challenges we ran into Coming up with a good GameFi concept is not an easy thing How to quickly introduce user to the game rules, such that the onboarding process is frictionless How to encourage users to come back to the platform How to make stretches engaging enough for the user to come back for more Smooth switching between webcams and not breaking the AI model Metaverse is a larger concept How to make Metaverse product Scalable in terms of building it, such that we will not have to introduce new content all the time [new levels, new rooms, new minigames] Accomplishments that we're proud of Successful Integrations of various technologies [AI, NFT, Web, React, Game engine] Introduction of Demo GymBuddy will allow everyone to try MetaGymLand if they are not familiar with Web3 yet Good design More ideas for future development and product improvement Ideas about what to pivot in our product, what we should change what we should stop The fact that we progressed our product during the hackathon from simple POC to early MVP allowed us to think more about the MVP audience and product market fit and many more... What we learned Tons of stuff about UX and UI in Blockchains context Game mechanics strategies related with UX GameFi system design Metaverse is not just about gaming What's next for MetaGymLand We will dig deeper into the MetaGymLand story and prepare a better introduction to what MGL is (animation explaining GymBuddy origins and user's mission etc.) Metaverse in 3D Make the product look more like a wellness tool rather than a game User research to test all product-market fit assumptions so far Introduce a more sophisticated backend rather than using only BAAS tools, currently the majority is happening on the Frontend Improve security and locking system in our Smart Contracts [now its easy to mint NFTs if you know the Smart Contract] Disclaimer MetaGymLand was born in Jan 2022, so before the hackathon. What was achieved during Polygon BUIDL IT : Summer 2022 hackathon 👇 expanding minigames portfolio from 4 to 7 (additional games) expanding the Metaverse size from 1 room to 4 rooms add game lineage mechanics , and user progress from more straightforward levels to more difficult Expand game mechanics (types of body movements that activate the avatar) NFT rewards after achieving milestones in the game (Play And Own) Bug fixes Performance improvements UX/UI improvements Game Design Improvements GameFi/Game rules improvements (Play 2 Own) Add Game Animations (Tweens and Particle Emitters) Gradual migration from JavaScript to TypeScript <div