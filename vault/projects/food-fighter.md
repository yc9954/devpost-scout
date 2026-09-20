---
slug: "food-fighter"
url: "https://devpost.com/software/food-fighter"
title: "Food Fighter"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 669
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Food Fighter

> Food falls from the sky, and eating it makes you grow bigger. Bring your enlarged body to the central finish area to enter the leaderboard. Challenge yourself to become the biggest player!

[Devpost](https://devpost.com/software/food-fighter) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** editor, horizon, meta, typescript, worlds

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for food fighter

## Body

Growing bigger with every bite! Fight back with powerful melee attacks! Reach the FINISH zone when you’re large enough! Reach the FINISH and claim your victory Grow so big that the city looks tiny! Race for food — every second matters! Stay alert — every hit shrinks you! Chaotic multiplayer food battle! Compete for the top of the leaderboard! World ID: 873769362490133 Inspiration I believed that a game where you grow bigger the more you eat is a fun concept anyone can enjoy. But rather than making it just a simple growth game, I wanted to add a competitive PvP element — combining gluttony and combat to create a humorous yet intense experience. My goal was to deliver an immersive gameplay experience where players move around, eat for themselves, and fight for themselves. What it does Food Fighter is a competitive game where players grow larger by eating food. Eat food that drops onto the field to increase your size The bigger you get, the slower you move — a clear risk & reward system Use weapons to attack and hinder other players When you think you're big enough, head to the finish zone in the center to record your score on the leaderboard Intuitive HUD and “How to Play” UI make it easy for newcomers to jump right in The goal is simple: “Who can eat the most?” How we built it Food Fighter is developed using the Meta Horizon Worlds Editor and TypeScript. Implemented interactions based on META Horizon Script Created custom HUD UI (food count display) and How To Play popup UI Built a grabbable weapon system (force hold, collision detection, swing validation) Saved individual player scores using PersistentStorage Implemented accurate hit detection using collision events + swing timing Local UI updates through bindings for player-specific HUD refresh Produced custom image assets and integrated them into the UI While it may seem feature-rich, the overall architecture is optimized with one clear goal — “Fast and intuitive combat.” Challenges we ran into While developing Food Fighter, I encountered and solved the following issues: Understanding the Horizon UI System -Challenges with distinguishing between Local Script and Default Script -Fixed issues where onClick wouldn’t trigger (layer, input mode, hidden state etc.) -Resolved UI updates affecting all players instead of individual ones Duplicate Weapon Collision Detection -OnPlayerCollision was being triggered multiple times per frame -Introduced a Set-based system to ensure only one hit is counted per swing Attach & Grabbable Conflicts -Replaced attachToPlayer with a force hold approach -Applied per-player grip offsets to correct inconsistent weapon grip positions Image Asset Loading -Solved Image source undefined issues -Fixed custom UI failing to render properly Each issue helped deepen my understanding of Horizon’s internal mechanics. Now, I can confidently manage UI, weapon systems, and player data handling within Horizon. Accomplishments that we're proud of The four aspects of Food Fighter that I’m most proud of: A fully custom UI system -HUD, How To Play popup, icons, and close buttons -Easy for new players to understand the game quickly Accurate weapon hit detection -Swing timing, collision detection, and duplicate-hit prevention provide satisfying combat feedback Growth mechanic based on eating -Simple yet highly addictive core gameplay rule Full multiplayer support -Player-specific HUD -Player-specific storage -Competitive elements are cleanly handled What we learned I learned a lot about how to structure games in Horizon for better maintainability and scalability, especially through developing Food Fighter. Key learnings include: How Horizon Worlds’ UI system works Handling clicks through Pressable objects and Input Modes Understanding collision event physics Managing player data using PersistentStorage Updating UI uniquely per player (bindings + player-specific updates) What's next for Food Fighter Moving forward, I plan to add the following features: Additional weapon types (hammer, stick, frying pan, etc.) Ultimate skill system: unleash a powerful attack after eating a certain amount New maps with strategic elements (jump pads, narrow paths, etc.) Enhanced hit feedback with sound effects and impact particles Lobby waiting room and tutorial area Cosmetic customization (skins, colors, different forks) <div