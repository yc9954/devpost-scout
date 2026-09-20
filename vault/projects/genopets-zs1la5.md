---
slug: "genopets-zs1la5"
url: "https://devpost.com/software/genopets-zs1la5"
title: "Genopets"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 667
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# Genopets

> Genopets is the world's first Move-to-Earn NFT game that incentivizes players to stay active and earn for free.

[Devpost](https://devpost.com/software/genopets-zs1la5) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]]
**substrate** [[code_repository]]
  <sub>weak: geospatial</sub>

**stack** react, solana, three.js, typescript, unity, web3, webgl

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for genopets

## Body

Genopets - The World's First Move-to-Earn NFT Game The Genoverse map Selecting a destination The step challenge Augment system Inspiration The idea for Genopets was born from our prior work in digital health exploring ways to use a health data marketplace to provide passive income to individuals as an incentive to stay active. While the infrastructure and industry for that concept was too early, we remained steadfast in the vision for passive income for health and pivoted to the Play-to-Earn gaming model earlier this year. We’ve been blessed with narrative tailwinds and growth in this industry and are excited to keep innovating and growing with the community. With Genopets, not only do we hope to financially incentivize players to stay fit, we can encourage them to do so and have fun while doing it. What it does Genopets is a Free-to-Play, Move-to-Earn NFT game on Solana that makes it fun and profitable to live an active lifestyle. Genopets combines user's step data from their mobile device and wearables with blockchain Play-to-Earn economics so players can earn crypto for taking action in real life as they explore the Genoverse evolving and battling their Genopet. How we built it We built this on top of Metaplex’s codebase - specifically the Token Metadata Program allows us to create mutable NFTs and update them at minimal cost. In the future, we intend to partner with Stardust to make this process even more seamless. The front-end is built using Unity and will be deployed to mobile. On the backend we have a simple REST API that performs simple operations such as minting NFTs and mutating them. For the minting process we currently use React / Next.js on the web and THREE.js for the graphics. Challenges we ran into The main challenge we faced was getting the API of the metadata program correct when it was released before the Anchor framework and had no IDL to use. Then we realized that the metaplex repo had JS bindings for all the metaplex programs and that made things a lot easier. The second challenge was to get the augment body parts to be dynamic, which we ended up using a simple unity function to achieve for now but will move to an attachment system later. Accomplishments that we're proud of One thing we are most proud of is that over the course of this hackathon, our community has grown significantly. Today we have more than 55k members on our Discord server and 28k followers on Twitter. This has helped validate the direction we’re headed and motivated our team to keep pushing to build throughout the competition. What we learned Keeping logic and state completely separate may be hard to reason about at first, but becomes super elegant as you become familiar with it. For one, we basically don’t need to touch rust as most of the logic we need to utilize are already deployed on-chain. This allows us to use Javascript bindings very heavily to achieve what we need to do. On the game and economics design side, one of the main things we learned from our deep research into Play-to-Earn games is that the problem with the primary net inflow of cash into your economy coming from new players joining your game is that it too closely ties the stability of your economy to continued user growth. The point at which user growth stalls, the entire game economy could collapse. That is why we designed Genopets to be a crafting and evolution game where the net inflow of cash to the economy comes from players’ active use and enjoyment of the game. What's next for Genopets Following the listing of Genopet Egg NFTs on FTX.us earlier this week, our Genesis Genopets NFT Mint drop is expected mid November, followed by a release of a private beta of the full game by the end of the year. Follow us on Twitter and join our Discord community for the latest updates. Twitter: https://twitter.com/genopets Discord: https://discord.gg/genopets <div