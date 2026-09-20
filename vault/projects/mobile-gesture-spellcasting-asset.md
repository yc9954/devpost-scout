---
slug: "mobile-gesture-spellcasting-asset"
url: "https://devpost.com/software/mobile-gesture-spellcasting-asset"
title: "Mobile Gesture Spellcasting Asset"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 495
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "substrate/geospatial"
---

# Mobile Gesture Spellcasting Asset

> Allow users to cast spells in your world! The four swipe directions can be mapped to different elements, and YOU can define spells made up from sequences of those elements!

[Devpost](https://devpost.com/software/mobile-gesture-spellcasting-asset) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**domain** [[transportation]]
**substrate** [[geospatial]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what's next for mobile gesture spellcasting asset

## Body

Inspiration This system is largely inspired by the game Magicka, an amazing game where you play as a wizard who casts spells out of sequences of elements. What it does A spellbook button is placed on the HUD. Tapping this will open focused interaction mode, where a diagram appears shows a mapping of direction to element. Each swipe will add an element to the current "spell" (displayed in the middle of the screen) Once the required number of elements is achieved (default 3), the system will check if a valid spell has been cast. If so, it will print the name of the spell, and send a network event to the server for gameplay logic to action the spell. If not, a message will be displayed informing the user. How we built it Having recently wrestled with making interactions and systems that played nicely on both VR and mobile simultaneously, I wanted to try building something purely for mobile. With the recent release of the gesture API, this seemed like a great starting point. A map is included at the top of the script where a creator can add/remove/tweak the valid spell list. The icons for the elements are prop vars, and therefore easy to swap out to better fit the theme of the creator's world. Accomplishments that we're proud of Overall the system feels pretty much how I imagined it when I set out. I think the scope for what could be done with such a system is pretty large! Adventure: For combat, pells could easily be mapped to different projectile emitters, that could be launched with the corresponding successful spell cast. Clues about which spell to cast to open a locked door could be hidden around the environment. Maybe you could define a spell which enables visibility/collision on select objects in the world for a limited time. Obby: Mapping spells to different movement abilities could add a lot of depth to an Obby. Imagine needing to cast "feather fall" to float to that distant island. Maybe you need to cast "low gravity" to make the next few jumps. What if you had a "mega jump" ability for making those really high ledges. Avoid getting crushed by the stompas by a quick cast of "fleet foot" before dashing down the corridoor! What's next for Mobile Gesture Spellcasting Asset Ways the asset could be extended/improved: A UI element could be added when in focused mode, either showing a subset of spells that players should always know, or maybe showing the last few "discovered"/cast spells. While it goes against my initial goal of focusing on mobile... it wouldn't be too big a leap to add VR support, based on waving a hand in the directions of the elements while holding a trigger, for example. The system currently only supports four elements, for the four swipe directions, but it would be possible to also support e.g. tap and pinch as elements / modifiers on the spells. <div