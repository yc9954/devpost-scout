---
slug: "left-for-loot"
url: "https://devpost.com/software/left-for-loot"
title: "Left for Loot"
hackathon: "Reddit’s Games with a Hook Hackathon"
organization: "reddit"
winner: true
words: 890
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "user/patient_family"
---

# Left for Loot

> Slay hordes, grind loot, rank up from E to SSS — a full survivor ARPG inside a Reddit post.

[Devpost](https://devpost.com/software/left-for-loot) · hackathon [[Reddit-s Games with a Hook Hackathon]]

## Facets

**user** [[patient_family]]
  <sub>weak: educator_student</sub>

**stack** devvit, unity, webgl

## Body

Using the Rift Gate to explore dangerous Rifts and collect valuable loot. Town View Main Gameplay where you defeat monsters and collect loot Inspiration Reddit games felt like they were missing something. There were a lot of AI-slop games— guess this , beat that , and similar concepts. I wanted to build something different. Something fresh. An extraction-style ARPG felt like the perfect fit. If you die inside a rift, you lose everything you picked up. Every run matters. On top of that, there's long-term progression through ranks (E → SSS), daily rotating shops, and a constant sense of grinding toward better gear. It felt like a great match for the hackathon and the kind of game people could come back to every day. What it does You spawn naked. Everything you own was taken from something that tried to kill you. The town is a shared hub where you can see other players walking around, visit the daily rotating shop, or gamble your gold at the forge. Once you're ready, you choose a rift and descend into the underworld. Combat is automatic—you control positioning while your weapons do the fighting. Your loadout defines your build. The Rift is endless, so you can keep exploring, dodging, fighting enemies, and hunting for better loot. Each run lets you carry back up to 5 items , regardless of rank. If you die, you lose everything you picked up during that run. If you successfully make it back to town, the loot is yours to keep. Players, enemies, items, and rifts all share the same rank progression: E, D, C, B, A, S, SS, and SSS . Your rift rank is determined by your current loadout, so you can't skip ahead into content you haven't geared for. There's also a level requirement, meaning getting lucky and finding an SS-tier weapon early doesn't let you jump straight into the endgame—you still have to earn your way there. The game currently features 112 lootable items across 8 ranks: 28 melee weapons 26 cloth pieces 23 helmets 20 armor pieces 8 wands (one per rank) 7 capes That's 112 unique items, with roughly 12–16 items available in each rank. How we built it The game was built in Unity , exported to WebGL , and shipped inside a Devvit webview . Challenges we ran into The biggest challenge was creating all the art in such a short amount of time. I reached out to several artists hoping to collaborate, but after hearing the scope of the project, most of them backed out. So I decided to build everything myself. I invested some of my own money into marketplace assets, then spent the rest of the time animating, integrating, and coding the game on my own. From a programming perspective, the hardest challenge was designing a modular weighted loot system that worked across every rank. Getting the drop probabilities to feel fair while keeping progression balanced took far longer than I expected. UI implementation was another major hurdle. Building without an artist is tough. I really didn't want to rely heavily on AI-generated art, so I ended up combining assets from multiple sources and designing the rest myself. There are still parts of the UI I'm not completely happy with, but I managed to make everything fit together. I also had bigger plans for the hackathon. I wanted to include a player trading system and asynchronous daily world bosses that players could team up to defeat for rare loot. Unfortunately, I fell sick during the final stretch of development and simply ran out of time. Those features are definitely coming in future updates. Another feature I was excited about was a spell system. While melee and ranged combat worked well, I wanted players to unlock powerful spell books that granted unique abilities. The four empty slots on the bottom HUD were reserved for these spells—things like Meteor Rain, Thunder Strike, Frost Nova, and other elemental abilities. Each spell book would have introduced a different playstyle and build variety. Sadly, this was another feature I couldn't finish before the deadline, but it's one of my highest priorities for future updates. Accomplishments that we're proud of I'm especially proud of the FTUE (first-time user experience). The cinematic intro, tutorial flow, boss encounter, and onboarding all came together better than I expected. Honestly, I'm still not sure how I managed to build a game of this size within the hackathon timeline while working a full-time job. There were a lot of late nights and countless iterations, but in the end I just wanted players to have a polished experience that didn't feel like another AI-generated game. What we learned This was my first time building a 2D extraction ARPG and my first time developing with Devvit, so there was a lot to learn. I learned how Devvit handles data, schemas, and state management, and I also spent a lot of time designing and implementing weighted probability systems for loot progression. What's next for Left for Loot Player-to-player loot trading Daily world bosses Leaderboards and competitive ranking Player skins and cosmetics Magic spells and spell books More enemies, bosses, and rift biomes Writing this with just 30 minutes left before the deadline. I used AI to help refine the wording, but the project, design, code, and story are all mine. <div