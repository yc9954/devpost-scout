---
slug: "tower-tycoon"
url: "https://devpost.com/software/tower-tycoon"
title: "Tower Tycoon"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown - Reloaded"
organization: "Meta"
winner: true
words: 725
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Tower Tycoon

> Tower Tycoon is a multiplayer tycoon that allows players to build their very own skyscraper and customize it to their heart's extent with decorations and also compete with others in shared mini events

[Devpost](https://devpost.com/software/tower-tycoon) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown - Reloaded]]

## Facets

**mechanism** [[simulation_digital_twin]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** adobe-illustrator, horizon, krita, typescript

## How they structured the write-up

- what it does
- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tower tycoon.

## Body

Tower Tycoon Mobile HUD, Player standing at their Tower entrance. They can see how much their Tower is worth and show it off to other Players. The Elevator inside their Tower to travel between floors Elevator Scrollable CUI Playtime Rewards UI Balloon Shooting Minigame Airdrop Minigame What it does Tower Tycoon is a multiplayer tycoon game where players build and expand their own skyscraper, unlocking new floors as they progress. Each floor can be customized with unique decorations, while fun mini-events and social features foster player socialization and community-building , creating a vibrant shared experience. Inspiration It was inspired by modern tycoon games with fast gameplay loops that are popular on several UGC platforms How we built it Our multiplayer tycoon framework stores all buyable items (buttons) in the world as IDs. We use Persistence variables to store which IDs a player has unlocked and use this data to load only those items when they enter the world, keeping the game super performant. We also added a dependency system for tycoon buttons and upgradability so that certain buttons are unlocked only when some specific button is unlocked and so that each individual button provides longer gameplay possibilities with upgrades. We wanted this to be the kind of world you can’t put down — small rewards, short actions, and a clear next step every time. That is also why we made sure that our First Time User Experience (FTUE) tutorial was robust and guided the player through all the main mechanics of buying tycoon buttons, claiming money and participating in events. We’re especially proud of how we used the Camera API for style and interactivity here — the camera actually tells the player what matters. We kept asking: “Are they having fun in the first 20 seconds or are we wasting them?” That’s why the landing zone, signposting, and first interactable are all right in front of the player. The player is also rewarded for playing longer with our Playtime Rewards and Daily Quests systems. Players can spend diamonds earned from Playtime Rewards on the Lucky Wheel to progress faster. We leveraged Meta's GenAI to create an awesome skyline for our cityscape environment that would have taken ages to do manually! We also used GenAI to create the dozens of decoration variations that the player can use to customize their skyscraper! The SFX generation tool helped us to create announcement audios and sound effects for our Airdrop and Balloon Shooting minigames. We can't overstate how helpful these were to reduce our workload and can't wait to use it in our future projects. Challenges we ran into We wanted to add a funny Mayor NPC the player could talk to, however as soon as the NPC was placed in the World, they would cause errors in our Persistence dependent scripts and, since Persistence was so deeply embedded in our Tycoon framework, we decided to not include the NPC. Due to object count limitations, we had to limit the number of player Towers the world could support from 4 to 2 to maintain performance. Accomplishments that we're proud of We had to create a multiplayer tycoon system from scratch, which was challenging, because we had to load objects into the World based on each Player's save data while maintaining performance, but we managed to do it! We believe this is the first multiplayer tycoon on Horizon Worlds built at this scale — a 10-floor player tower, 100+ purchasable tycoon buttons, upgradable buttons, and unique base decorations. The Custom UI was designed to feel native on mobile: big CTAs, progress panels, and context-sensitive buttons, with ScrollViews to allow scrolling with fingers. Our custom base decoration, elevator menu and Daily Quest systems ended up being one of the parts we’re proudest of. We are proud of all of these achievements and truly believe this makes Tower Tycoon the best game in the Simulation->Tycoon genre! What we learned We learned how to use every single one of Meta's GenAI tools What's next for Tower Tycoon. We plan on optimizing the game to support 4 player Towers at the same time without compromising on the player's tower size or customization options, and we already have a solid idea for how to accomplish this! More fun, social minigames! More ways for players to show off their tower and wealth to other players <div