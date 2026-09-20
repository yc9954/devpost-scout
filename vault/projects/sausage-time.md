---
slug: "sausage-time"
url: "https://devpost.com/software/sausage-time"
title: "Sausage Run!"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 1277
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Sausage Run!

> A multiplayer team based parkour game where you play either in a team of Sausages trying to get to the plate, or you're in a team of mini-chefs trying to stop them!

[Devpost](https://devpost.com/software/sausage-time) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**substrate** [[video_visual]]

**stack** blender, gimp, metahorizonworldsdesktopeditor, substancepainter, typescript

## How they structured the write-up

- 🌭 sausage run!
- 🌎 meta horizon worlds
- 💡 inspiration
- 🛠️ how i built it
- 🚧 challenges
- 🏆 accomplishments
- 🚀 next steps

## Body

🌭 Sausage Run! Multiplayer team based Parkour mayhem! Play as a Sausage trying to get to your plate, or as chef trying to stop the sausages. Introducing a new multiplayer twist on the regular parkour genre! It's not easy being a Sausage , especially given the perils of a modern day kitchen and the mini-chefs are out in force to try and stop you! If a sausage player reaches the plate, then the sausage team wins If the timer runs out and the chefs have stopped the sausages, then the chef team wins. For this competition I added the following new main features: A Progression System Players are now awarded XP if they are on the winning team and this goes towards a levelling system. A local progress custom UI is shown to the player and XP & levels are represented in the form of building burgers. As the player gains more XP by winning matches, the burger will build up and once it's complete the player eats the burger and is awarded a permanent speed increase. The more burgers they build & eat, the more speed they'll have in the game to gain an advantage. As the levels progress, it takes more and more XP to create a burger, so higher levels take longer to achieve but also gives the player a more competitive edge. A Custom UI Shop I have added a custom shop in the game where the player can purchase, equip and view costumes that they can wear in the matches. This shop was written using local custom UIs and deals with the purchasing of costumes using an in-game currency. As the player can either be assigned as a Sausage, or a mini-chef, there are a set of customs per player type that they can purchase and equip. These are also viewable in the kitchen island lobby as a mirror is used as part of the shop, so the player can equip a costume and view it in the mirror at their leisure. Currently there are four costumes per character type but is very expandable. It could also be tied into the player's XP level, so certain rare costumes can only be available to players at a certain level. Use of the Camera API Previously the game was difficult to play as a chef character because using the kitchen hazards while moving the camera was incredibly tricky. Also, from the default 3rd person view it was hard to see the sausage players and timing your actions to stop them. For the chef characters, I implemented a camera system where, on approaching specific areas the camera would transition to a pre-defined fixed point and focus on a specific aim point. This solved both issues, and the game is far more playable because of it. I also added a button to exit the fixed camera if the player feels they want to revert back to 3rd person during these sections then they have that option. These camera also give a great vantage point for seeing your 'kills' and pulling off moves using the kitchen hazards and great for sharing fun moments in the game. A Kitchen Island (lobby/hang-out area) Previously, there wasn't much of an introduction into the world, or a lobby where players could just hang out in between matches. Therefore I added a kitchen island in the middle where players are spawned when they enter the world. If a match is in progress, they can still hang out in this area and watch the match while it plays out around them. The kitchen island was also a great place to put the player progress UI panels, leaderboards and shop/costume preview area. It also acts as a great area to introduce the world with how-to screens and allow the player to get comfortable with the environment before entering a match. 🌎 Meta Horizon Worlds Created specifically for the Meta Horizon Worlds Mobile competition made for mobile, web & VR - this world was created using the desktop editor and this is my first Horizon World I've made and updated. 💡 Inspiration What inspired you to create this world? What other worlds or media influenced your creative direction? I wanted to make a fun, fast paced team arcade game with a comedy element. It was initially going to be about Fish & Chips, but I felt Sausages would be more fun! I liked the idea of a team based parkour game, where one team is trying to finish the course as fast as possible, while the other is controlling the environment to try and stop them. 🛠️ How I Built It What were the key tools and processes you used to create the world? If this is a team world, who contributed and how did they contribute? The main tool was the Meta Horizon Worlds Desktop Editor. I also made my own assets in blender, substance painter and put together my own toolchain. One particular element visually was that I felt many Horizon Worlds textures are very low-resolution and I came up with techniques to create high resolution PBR surfaces. I created the logic in typescript as well as modelling and texturing the assets involved. 🚧 Challenges What were the biggest difficulties you encountered, and how did you overcome or work around them? It was a steep learning curve, especially using typescript & the process of importing custom assets and textures. I'm largely from a Unity background, so some things were very familiar, while other elements took time to learn and be proficient enough to create the idea. Therefore the biggest challenge was to create the game within the time I had, learning the system, coding the logic, as well as modelling and texturing the environment to a competitive level as a solo dev. Doing the update also allowed me to learn new systems such as dynamic custom UIs, the camera API and more about how local and server scripts are managed. 🏆 Accomplishments Which parts of your world, or your building process, are you most proud of? Initially, admittedly, it was slow going at first and a lot of time was spend learning and understanding the systems and the editor. However, the part I'm most proud of was when there was a turning point. Nearing the end, processes started to click, things got quicker to make and the game started to be fun. I'd say the greatest accomplishment would be creating this game and learning the horizon worlds editor and process within the time I had and extending my knowledge of the editor and scripting. 🚀 Next Steps How are you going to keep improving the world? What would you like to add if you have more time? I think given the limited time I had to make it, that given more time I can really push on the quality of this game and add so much more. More play testing with teams of players and balancing it well - there are some areas of the course which need more gameplay balancing. I'd also like to extend the shop and UI features too. I do feel it's a fun game to play, especially how manic it gets with 8 players, but I feel that many more hazards can be added to this game and potentially more environments & customisation on the characters. Personally, I would like to make progress on this after the competition, along with more play testing and add more features to the world. Adding variations to the parkour course would be great so it's not always the same. Thank you for playing - I hope you enjoyed being a Sausage! <div