---
slug: "frenzy-xou70e"
url: "https://devpost.com/software/frenzy-xou70e"
title: "Party Kingdom"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 770
team_size: 10
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Party Kingdom

> Welcome to the Party Kingdom! Hop into the gameplay area with friends to see who can win the most frenzy points and wear the crown. Play through a large array of minigames or hang out in the Inn!

[Devpost](https://devpost.com/software/frenzy-xou70e) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

  <sub>weak: sensor_fusion</sub>

**stack** asana, blender, discord, horizon, photoshop, substance, typescript

## Body

So, what inspired us to build Party Kingdom? Since the days of the World Hop in Horizon Worlds, our team has seen the potential of minigames as fun, snackable content for friends to enjoy on the platform. We were inspired by Mario Party minigames that are fast and exciting, and we removed the wait time between them so the party keeps going! We decided that by tweaking this feature, we could create a frenzy of excitement in the gameplay area while allowing players to freely jump in and out of the gameplay space if they want to hang out with friends in the beautiful inn environment. We crafted this game to be fun and accessible on a mobile platform and are so excited to publish it for the community of players on Horizon to enjoy! The magical Inn is open to all and serves only potions, just watch out for the dragon fire and dodge the spells! We built this world using some of our favorite features of the Horizon Worlds Editor. We built Party Kingdom with the Desktop Editor and, using the testing features to test in mobile, were able to considerably expedite our development process. We specifically leveraged sublevel loading to offer players a large variety of minigame options while keeping the capacity of the world lower and the stability of the world performant. To give life to the world, we made use of many assets in the library including VFXs, props, and audio. We also used custom UI to create a dynamic HUD for players and crafted an NPC to watch over the Inn and bring it to life. With any quick turnaround project, there were challenges along the way. Especially in creating a game based on a large amount of minigame content, capacity was a known issue every day. Using the sublevel system, we found that we could keep each game in its own spawnable sublevel and remove that capacity limit. In each short pregame timer while the environment changes, we despawn and spawn in the new game that has been randomly selected. To ensure the games stay consistent and we do not need to change code in every world, the core loop of the game and any non minigame specific code is set in place in the main world itself. Although we overcame this challenge, being unable to bring the world to life through Unity Asset Bundles and PopcornFX meant we needed to get creative with the asset library available to us. The limitation of the tools as well as the limited time meant that we needed to cut features that we would otherwise have liked to have including a store. We are so proud of our team for their amazing accomplishments on this project. First and foremost, we are proud of the accessibility of the game. The whole development process has been catered to the idea that a player can just jump right into the game with no knowledge and is able to participate without instructions or limitations. The game also plays nonstop, so players can hop in whenever they want. This concept capitalizes on friends joining each other mid game and being able to jump right into the action with them, further encouraging social interaction inside Horizon. Additionally, we believe the game caters to a wide target audience. This beautiful Inn was carefully designed from the ground up to ensure there was a place for every player to feel comfortable and engaged. Between the gameplay area and the spectating area that surrounds it, the layout allows players to stay close to the action regardless of where they roam to, while also not forcing them into the game if they need to step away or simply want to watch. Providing players with the ability to choose their level of engagement within the world was a huge accomplishment for this project. After the judging is complete, we have more plans for this world! One MHCP feature we are really excited about is the Turbo data we can collect. We want to better understand what games players are participating in and create more minigames of those styles. Additionally, we want to reward players for playing these games by providing custom wearables and other assets for purchase in a shop – the intended use of Frenzy Points! Furthermore, granting custom ranks and progression, unlocking a VIP limited area, and increasing the overall magical fanfare (using audio, VFX, and animations) will help keep players engaged for a longer term and keep Party Inn a well known place for players to return and meet up inside of Horizon. <div