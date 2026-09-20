---
slug: "paws-arena-multiplayer-pvp-play-to-earn"
url: "https://devpost.com/software/paws-arena-multiplayer-pvp-play-to-earn"
title: "Paws Arena - Multiplayer PVP Play to Earn"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 666
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Paws Arena - Multiplayer PVP Play to Earn

> This is the cutest, most fun and competitive turn-based play to earn multiplayer game on the ICP. Players will fight in the arena and earn $PAW Tokens which will be used to buy in-game items.

[Devpost](https://devpost.com/software/paws-arena-multiplayer-pvp-play-to-earn) · hackathon [[Supernova]]

## Facets

**domain** [[developer_tools]]
**substrate** [[geospatial]] [[video_visual]]

**stack** javascript, react, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for paws arena - multiplayer pvp play to earn

## Body

Wallet Connect - NFT Selection Menu Paws Arena - Menu Multiplayer - Lobby Screen During a match Triple Rocket selection Triple Rocket - How to use Life box You Win Screen Architecture 1. For the best experience please use the Google Chrome browser; you can use the Full Screen button beneath the game window. Mobile devices are not supported yet. 2. Please note that for this submission we haven't included the wallet connect function. We wanted to make sure that the Juries will be able to play Paws Arena without the need of owning an ICKitty. This way we avoid any kind of incident that may not allow you to buy an ICKitty from the marketplace, etc. Thank you. Inspiration We first started our project in September of 2021 in the form of an NFT collection, named ICKitties. In order to make it easier for our audience to follow our story, we created a 90 second animated video showcasing the background of each kitty race in a fun and easy to follow way. Now, our NFT collection will find a new home in Paws Arena, our upcoming game. The inspiration for our game came from games created years or even decades ago (like Worms Armageddon or Shellshock Live). The idea of our game is simple, yet very powerful because it's challenging and engaging for the users, making them fight against other players in order to get in the top positions in our Leaderboard and win bi-monthly or monthly prizes. What it does We noticed that no other project on the Internet Computer had a challenging multiplayer feature or any system that would give players a reason to come back and play again. That is why we created Paws Arena to allow users to connect in multiplayer PVP fights and get rewards every time they win a match. How we built it We built our game in Unity. We used React to integrate @dfinity, dab-js and plug-connect (for the wallet connect function), Fleek for CI/CD pipeline (staging environment) and then we used dfx for production environment. Animations are mostly done with the help of spritesheet animations, combined with well-placed linear animations, camera shakes, particles and post processing effects. Our NFT collection (ICKitties) is the central pillar in Paws Arena. Choosing your favorite Kitty from your wallet, you not only choose your skin theme, you will also have access to a specific set of items that will give a nice flavour to your game experience and can even decide your fate in a duel. Challenges we ran into The most challenging parts were: Integrating the wallet connect function, because from the dab-js library we had to specifically implement only the ICKitties canister, without calling all the other NFT canisters; Deploying Paws Arena in a canister We had to host our assets on Amazon S3 because of the 15 Mb limit on the canisters. We learned too late that we can overcome this limitation by using a Motoko/Rust canister that is able to serve bigger files via implementation of http_request method. We will use this method in our future development. Accomplishments that we're proud of We are really happy with the advancements that we have made so far; we have a working first version of PawsArena which can be tested and we can gather feedback from our users, which will allow us to improve it continuously. What we learned It was a journey that allowed us to learn how to create and deploy canisters and how Dfinity Agent interacts with wallets, canisters and NFT tokens. What's next for Paws Arena - Multiplayer PVP Play to Earn After the Supernova Hackathon is over we will only allow ICKitties NFT holders to play Paws Arena. We will gather our community's feedback on our Discord server and continue developing our game. We will implement the missing functions of our game (leaderboards, weapon attachments, new maps, a levelling system, daily challenges), with the working version following to be launched in Q4 2022. <div