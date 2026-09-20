---
slug: "blob-clash-arena"
url: "https://devpost.com/software/blob-clash-arena"
title: "Blob Clash Arena"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 749
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/structural_withholding"
  - "substrate/video_visual"
---

# Blob Clash Arena

> Never seen before: A new and unique multiplayer experience, reimagined from the world-famous proven popular browser/mobile game "Agar.io", bringing the popular social cell-eating fun to Horizon!

[Devpost](https://devpost.com/software/blob-clash-arena) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**mechanism** [[on_device_local]] [[structural_withholding]]
**substrate** [[video_visual]]

**stack** meta, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blob clash arena

## Body

THIS is the definition of innovation: When the competition theme “Mobile Innovation” dropped, I asked myself: What’s the boldest thing I could bring to Horizon? Many successful mobile games on smartphones are 2D, yet Meta Horizon is a 3D platform where almost every world follows the same 3D blueprint. So I set out to flip the script. The result is a fully 2D multiplayer game that pushes the boundaries of what Horizon can be! Something that, as far as I can tell, no creator has ever pulled off before. Yes, there are 2D games and worlds, but they’re entirely single-player (Card games, Pet Care, Candy Crush-style puzzles, Poker) with no real interaction between users. We combine all the new features: Noesis UI, Tap-To-Move, and so on. So come on and step into Horizon’s first-ever multiplayer 2D game Inspiration Inspired by the proven game concept of the well-known popular beloved Orb/ball browser game with millions of players. Still, I was suprised to not finding this game on Meta Horizon. Most likely because the game is 2D only which is something you almost never find on Meta Horizon (only in the very recent times). There is one world called "Agario" but it's a completely different game concept. Let me know and comment here below if you have EVER found a Meta Horizon World with a similair "UI/2D only" concept as this one. ESPECIALLY Multiplayer: seeing and interacting with other players in a 2D form. Yes I have seen and played 2D only Horizon Worlds like Poker or Candy Crush but these are Single player games, While I am still relatively new to Horizon, I am very confident that this has never existed on the platform before. This here is the definition of pushing the boundaries of what is possible on Mobile Meta Horizon. Using an already proved concept is a great way as shown when looking back at the winners of the last hackathons and their most played worls. What it does Eat smaller blobs (cells/circles), avoid bigger ones and try to become the biggest of them all! Move around using simple one-touch movement (tap-to-move). How we built it You probably ask yourself how did I build it? It's true that with default Custom UI this would be very hard to do. So did I leverage the new Neosis UI? Even with that you would come to a limit/bounds. The truth is that I completely thought out of the box and used every trick out of the book and combined multiple features to create this, which I would basically call an illusion. I remember "Robo Recall" from the UE4 Devs who faked realistic dynamic shadows by placing the exact same object into the ground but just pitch black. It wasn't a true black shadow but to the player/viewer: In the end we got the impossible: movable dynamic shadows. Challenges we ran into OH boy... where do I even begin? First of all creating a Multiplayer game in a 2D style where there are no player avatars visible or moving around but only circles/orbs WAS HARD Detecting when one Orb/Circle (Player) touches other Orbs/Circles (Food or Players), Collision in general. Because normally collision is squared (boxes) but here the player is round!! and flat! Scaling the Orb visually was easy but Scaling the Collision Detection was another hassle Then all the Server-Client Logic, that a lot of code is running locally on the player but they have to communicate with other players and the server. In this process I also identified a bug(?) or feature that any changes to an attached entity are not visible server-wide and only to that local player (yes, Network Broadcast doesnt do it!) Creating Bots/NPCs that move around like real players, probably one of the biggest which, just like art, can never be finished/final as its just so heavy making a bot that goes to the next level to eat, avoiding bigger players/bots on the way or near and just acting human. Accomplishments that we're proud of I am so proud to bringing a beloved game to this platform and had a lot of fun playing myself. What we learned 2D in Meta Horizon :) What's next for Blob Clash Arena I am working on monetization: allowing players to buy a "skin"/image/design for your blob (round circle shape). This would be a very cool way to personalize. Other than that there is not much else to add as anything else would disrupt this fun game concept <div