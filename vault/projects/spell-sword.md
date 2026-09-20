---
slug: "spell-sword"
url: "https://devpost.com/software/spell-sword"
title: "Spell Sword"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 846
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/supply_logistics"
---

# Spell Sword

> Wield your words as weapons against waves of monsters. Defeat numerous foes, gather loot, upgrade your gear, and complete daily quests as you push deeper into battle in this turn-based RPG experience.

[Devpost](https://devpost.com/software/spell-sword) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**domain** [[supply_logistics]]
  <sub>weak: security_privacy</sub>
  <sub>weak: video_visual</sub>

**stack** adobe-illustrator, flaticon-license, horizonworldsdesktopeditor, photoshop, premiere, sunoai-license, typescript

## Body

Build words from the available letter tiles Collect and use loot to aid you in battle Immerse yourself into the world of Spell Sword Accept Daily Quests, Climb the Rankings, and replay previous Floors ⚔️Inspiration Wield your words as weapons against waves of monsters. Defeat numerous foes, gather loot, upgrade your gear and complete daily quests as you push deeper into battle in this turn based RPG experience. 📖What it does Spell Sword is a fantasy turn based RPG that blends strategic wordplay with classic combat progression. Players form attacks by crafting words from dynamic letter pools, using vocabulary skill as a core combat mechanic. As they battle waves of monsters they earn loot, upgrade equipment, unlock consumables and progress through daily quests that encourage long term engagement. Designed for both casual players and RPG fans, Spell Sword aims to deliver an accessible but demanding experience that stands as the first chapter of a larger saga. 🛠️How we built it The project began as a full exploration RPG with multiple classes, co-op play and story driven quests. To align with the Mobile Innovation theme I intentionally narrowed the scope to a focused combat scope that is optimized for a comfortable one handed portrait orientation mobile game. The result is a one player experience where the challenge comes from choosing the right word at the right moment rather than learning complex input patterns. Most of the early work went into building the word engine. I developed dictionary utilities, custom rarity tiers and a scoring model for each letter, then curated a 170,000+ word list tuned for modern English, fantasy terms and a few seasonal extras. I merged and cleaned multiple sources, filtered out low quality entries, and created a separate block list of roughly 500 words so public leaderboards stay appropriate for a general audience. 🐉Challenges we ran into On top of this system I designed a combat loop across 99 floors of increasing difficulty. Each floor considers enemy archetypes, player stats, equipment tiers, consumable drop rates and three player mindsets: casual, dedicated and pay-to-win. Balancing those factors produced more than 4,700 data points that shape a curve which starts generous and ramps into a meaningful challenge. The first 10 floors are intentionally forgiving so new players can jump straight into the fun. Deeper in, stronger weapons, armor, and afflictions become available and a simple word choice turns into a tactical tradeoff. Afflictions are a key layer. Bleeding accelerates as the player is hit, poison becomes more dangerous the longer a fight lasts, and curse behaves like poison while making the victim more vulnerable to all damage. These effects interact with rarity weighted weapons and armor plus several consumables. Potions heal and cure afflictions, summoning scrolls let players inject specific letters onto the board, and the Pocket Sand Glass artifact refreshes the entire letter pool. All of these systems are tied back into the balance model so rewards feel intentional rather than random. Progression also depends on collection and replaying previous floors. Duplicate weapons and armor are not wasted inventory, they are materials. Gathering ten copies of an item allows the player to upgrade it through five tiers, increasing base damage, mitigation and affliction strength. This creates long term goals without overwhelming the mobile interface. 🏅Accomplishments that we're proud of To make combat feel like a modern RPG instead of a static puzzle I rebuilt the presentation around the player avatar. An avatar and NPC controller drives animations, visual effects, sound cues and the health bar, while a spline based camera system glides through cinematic angles instead of cutting between fixed shots. The result feels closer to a steady cam following action sequence than a simple 2D panel of letters. Later in development I partnered with Takatado, whose strengths in environment and 2D art complemented my focus on systems and UX. Together we replaced the placeholder arena and wireframe UI with a cohesive visual identity: a damaged stronghold that hints at past battles and a clean, legible interface built for phones. The chibi style monsters, knight and spell tiles carry the tone across both gameplay and branding. 🧠What we learned Under the hood, world persistent variables and JSON configuration files drive almost everything, including word lists, shop inventory, drop tables, starting gear, and equipped avatar item traits. This keeps the experience data driven and easy to tune after launch. Custom leaderboards highlight not only highest levels and damage dealt, but also the best words used in battle giving players recognition for both power and creativity while respecting the filtered word lists. 🌟What's next for Spell Sword In an age dominated by AI generated brain rot and low effort doom scrolling, Spell Sword is my attempt to reward players for skills that rarely get attention on the Meta Horizon platform: vocabulary, planning, and critical thinking. My hope is that this focused combat slice can grow into a broader universe with raid style bosses, additional character classes, co-op play, PvP tournaments and exploration worlds with cognitive skill challenges that all feed into this same word powered combat system. <div