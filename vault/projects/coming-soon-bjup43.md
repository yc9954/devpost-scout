---
slug: "coming-soon-bjup43"
url: "https://devpost.com/software/coming-soon-bjup43"
title: "Star Chasers: Mini Games Mayhem (Elevated)"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 900
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Star Chasers: Mini Games Mayhem (Elevated)

> 10 Worlds in 1! Grab the most stars across random levels: dungeons, icebergs, space, lava, Big Boss Kitty, & more! Mobile players: Share meme-able pics & rank up to earn custom emojis & dance moves!

[Devpost](https://devpost.com/software/coming-soon-bjup43) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** blender, cameraapi, custom, horizon, meta, photoshop, typescript, ui, worlds

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for star chasers?

## Body

Star Chasers: Mini Games Mayhem Inspiration I love high-energy mobile multiplayer party games in fun settings. When I learned about the World streaming capabilities in the Desktop Editor, I knew I could create an experience that’s effectively 10 mini games in one, each game its own unique World. A unifying game objective (collect stars!) streamlines onboarding. Players can join the fun anytime – no need to wait for a lobby to fill – and players are never eliminated, either­ – the fun is nonstop! To elevate Star Chasers: Mini Games Mayhem, once again I was inspired by some of my favorite mobile games and experiences. Progression and self-expression are at the core of many successful games, so I combined both in a system that lets mobile players collect stars to rank up. At each new rank, they earn progressively more fun and hilarious emojis and dance moves they can use to bring their own personality and fun to every game. And people love to share fun experiences, so I also created some epic meme-worthy moments. What it does Gameplay basics: Starchasers: Mini Games Mayhem is a party game for up to 10 players, though solo gameplay is an option. When they start the game, a loading screen shows players which random level (World) they’ll play in Round 1; they return to this loading screen for Rounds 2 and 3. For each round, a separate and unique World is streamed in a quick and seamless transition — no doors, menus, or portals. Each level is a custom game with unique mechanics, design, landscape, and obstacles, but for all levels, the simple objective is the same: collect as many stars as you can in 90 seconds. The number of available stars adjusts for the number of players to improve fair play. The first round is always an obby/runner, the second round is always a maze, and the third round always features the Boss Kitty, a giant robot cat with a smile and an attitude. Players can join the game anytime and find the fun right away. After 3 rounds, players see their final scores and the top 3 winners triumphantly displayed in the trophy area. Here’s how I elevated the game progression: For mobile players, I introduced a new ranking system with unique rewards to encourage progress. A revamped custom UI shows current rank and progression toward the next rank. When the player collects enough stars to rank up, they see an animation, color change, and pop-up. A pop-up also tells the player they’ve unlocked a new reward – either an emoji they can display (including custom emojis of the Big Boss Kitty), or a fun dance move. There are 8 ranks and 8 rewards, with increasingly more stars required to rank up. When they enter the world, a NUX display invites players to check out all 10 levels. We added 3 new levels: an underwater obstacle course, a mall maze, and an amazing Lava Boss challenge. New scripting ensures you never play the same level in consecutive games, encouraging repeat play and progression. Here’s how I elevated the shareable moments: Players can share funny new memes of themselves performing dance moves with a beautiful vista of the World behind them. These custom dances are available only in these “victory meme” moments. After each game, a custom animated camera scene unveils the revamped trophy area with winners’ names on their trophies, plus a panel highlighting player stats, rank, and progress. New custom emojis and dance moves allow a range of self-expression and let players create fun and shareable moments. Other enhancements in the revamped Star Chasers: NUX instructions and popups help onboard new players Custom UI and other in-world graphics were optimized Three new levels were added How we built it I used the amazing tools available in the Worlds Desktop Editor, including custom model and animation imports, World streaming, custom UI, nav mesh, Gen AI skyboxes, Camera API, asset pooling, and of course TypeScript. Documentation and tutorials were extremely helpful resources as well. For the game assets, I used Blender 3D and Photoshop, optimizing models and textures for efficient gameplay. Challenges we ran into Adding so many new, mobile-focused features required a lot of troubleshooting, debugging, and patience to ensure a smooth and optimized experience. I had quite a learning curve with asset pooling, advanced custom UI, and the camera API, but I’m pleased with the results. Accomplishments that we're proud of Star Chasers: Mini Games Mayhem was already my most ambitious world, and I feel I took it to the next level with these enhancements for game progression and shareability. I love seeing players doing the new dances and sharing the new emojis and meme moments, knowing the effort they put in to earn these rewards. What we learned As always, I was reminded that careful planning and managing “scope creep” are critical to success on an ambitious project with a hard deadline, as is rigorous playtesting. This challenge really helped me level up my TypeScript and game design abilities as I incorporated all these new features. What's next for Star Chasers? I have several new levels planned, with great new shareable moments. I’d also like to augment the game progression with even more fun rewards. And I may add a store to purchase durable and consumable items – the Big Boss Kitty would look great on a t-shirt. <div