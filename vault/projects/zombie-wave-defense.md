---
slug: "zombie-wave-defense"
url: "https://devpost.com/software/zombie-wave-defense"
title: "Zombie Wave Defense"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 1036
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "substrate/geospatial"
---

# Zombie Wave Defense

> Survive the endless horde, reap the rewards!

[Devpost](https://devpost.com/software/zombie-wave-defense) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**mechanism** [[provenance_signing]]
**substrate** [[geospatial]]

**stack** typescript

## How they structured the write-up

- tl;dr
- inspiration
- zombie wave defense & progression system
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zombie wave defense

## Body

Wave system - new enemies, boss battles, and wave scaling! Weapon system - new weapons, an in-game currency, and an in-game shop! Upgrade system - players earn power ups after each wave! Persistent progression - players can level up, choose classes, and unlock daily rewards! Zombie Wave Defense - Thumbnail TL;DR We built Zombie Wave Defense , an easy-to-play, hard-to-master wave defense game: defeat wave after wave of zombies, survive as long as you can, and earn the highest score! Over the course of the competition, we've added tons of new features to flesh out our progression system. These features are paying off. Our player base has since grown from a few hundred to over 15,000, players have spent over 3000 hours (across headset and mobile) in the game, and, at any given moment, dozens of players are defending against the endless horde. Check us out, and have fun! Inspiration Boxhead and classic Flash games; we love when game loops are simple and game content is deep. Left 4 Dead 2 for zombie-related inspiration. Zombie Wave Defense & Progression System In Zombie Wave Defense, you fight wave after wave of zombies. Your goal is to stay alive as long as you can, earn the highest score, and get to the highest wave! For the competition, we've upgraded nearly every aspect of the game, building a progression system that encourages players to stick around long term. Before When we first started, we had A single, melee only zombie A revolver as the only weapon Higher waves simply included more zombies After Since then, we've Improved the wave system by adding new enemies, boss battles at milestone waves, and wave scaling mechanics that make the game more challenging as you progress. New enemies include the red devil (a projectile firing zombie capable of ranged attacks), the speedster (a melee zombie with incredible movement speed but fragile health), the bloater (an explosive, area-of-effect zombie that detonates near players), and the tank (a high-health, high-damage melee zombie that takes teamwork to defeat). Boss battles include the Zombie Prince , a charger zombie that sprints across the map, leaving chaos in his wake, and the Zombie King , a ranged zombie that fires dozens of projectiles at rapid speed. Bosses spawn at milestone waves (e.g. wave 30) to change the flow of the game, challenging players to play together and signifying progress. Each wave, we adjust enemy strength stats, enemy types, and enemy quantities. Wave scaling makes the game progressively more difficult as players get more powerful, encouraging them to switch up their tactics over time. Improved the weapon system by adding new weapons, coins as in-game currency, and a weapon shop . New weapons include the grenade (an explosive, area-of-effect, throwable), katana (a melee, area-of-effect slice and dicer that can also block projectiles), sniper rifle (a super high damage, but high cooldown weapon), and assault rifle (a high rate-of-fire weapon that's essential for clearing larger waves). Players collect coins as they play the game and can spend them on weapons in the shop. Added an upgrade system that lets players power up with unique abilities after defeating each wave. Upgrades are randomly assigned and add an element of randomness, making each playthrough unique. Introduced persistent, cross-session progression with leveling, a class system, and a rewards system . Killing zombies earns EXP, and EXP lets players level up. The higher your level, the more . Players can select from soldier (higher health and able to spawn grenades), scout (lower health but faster movement and a double jump), medic (team heal), or samurai (increased melee damage). Classes respond to the leveling system and get more powerful as you play. Every day, players can log in to earn keys. Keys open chests at the reward station, and chests can award coins, give EXP, and unlock legendary power ups. How we built it We use native Horizon World gizmos and shapes everywhere, composing them with animations to bring entities to life. We're trying to push Horizon Worlds -- the platform -- to its limits. We want to build a quality game entirely inside the Worlds engine and editor. That's what gives the game its signature style and feel. In mobile, UI also means everything. We've built (and endlessly tweaked) custom UI components to communicate our progression system, game state, and player achievements. Technically speaking, our toolkit is: TypeScript, the world editor, and a lot of work. Challenges we ran into Asset spawning limits. It's an infinite game, so we spawn and despawn a ton of entities -- at least, we used to. A while ago, we hit nasty performance issues and eventually a hard limit on asset spawning (at wave 22). To fix it, we implemented a caching layer (object pool) which avoids constant spawning; instead, we recycle through entities that already exist. Gameplay Balance. Here's an example: you made the AK-47 fire a little faster. Well now the first 10 waves are way too easy. Ok, well let's scale back the enemies. Uh-oh, now it's harder to collect coins, and the AK-47 is harder to buy. And on and on it goes. Balance is tricky for us because small changes in one area can drastically affect how the game feels overall. There's no easy fix here; we play test often and make tweaks constantly. Accomplishments that we're proud of Our players. Our players are the most impressive part of the game. The leaderboards for highest wave reached, highest scores, most kills, etc. are changing all the time -- and we're not even close to the top anymore! We're proud that we've made something other people resonate with. Fun in 20 seconds. We've taken this tagline to heart. We work hard to keep the game simple, easy-to-play, and with a lot to discover as you spend more time playing. What we learned Don't overcomplicate things, build features that you enjoy, and the fastest way to kill the wave 30 boss is to double-up on solider, pre-nade the spawn point, and unleash damage-maxed AK-47s. What's next for Zombie Wave Defense More enemies, more weapons, and more maps! Just to name a few. Our priority is whatever we think will make the game more fun. <div