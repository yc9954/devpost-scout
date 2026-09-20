---
slug: "the-vigilance-1m807f"
url: "https://devpost.com/software/the-vigilance-1m807f"
title: "The Vigilance"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown - Reloaded"
organization: "Meta"
winner: true
words: 956
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
---

# The Vigilance

> A Lovecraftian Idle Incremental Tap game, set on an expedition aboard the Vigilance. Tap the screen to defeat horrors of the deep, and upgrade your ship to get further each time.

[Devpost](https://devpost.com/software/the-vigilance-1m807f) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown - Reloaded]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[video_visual]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the vigilance

## Body

The vigilance braces for impact... Upgrades are essential to survival There's strange things in the deep... Hire crew to bolster your expedition Face fierce beasties Inspiration The Vigilance is a tap-based incremental idle game, inspired by titles like Tap Titans and Egg Inc., and reimagined inside Meta Horizon Worlds. Set aboard a weathered ship adrift in a Lovecraftian sea, the game blends the compulsive, infinite progression of idle clickers with the immersive presence of Horizon avatars, grounding players in a dark nautical adventure that’s both familiar and unsettling. What it does The core loop: (minute to minute) As your boat encounters monsters from the deep, your Horizon Worlds Avatar stands upon the bow and wards them off, being rewarded with coins in the process. You do this by tapping the screen to damage the monster, however every so often (when the energy bar fills) you will encounter a boss monster, possessing greater health and requires defeating within a time limit. Once the boss is defeated, you advance one Nautical Mile to the next area. Each area will feature tougher monsters, with more challenging boss timers, requiring you to spend your coins on empowering both your avatar and boat. You are able to purchase automated cannons for the boat, which are where the idle element of the game is introduced, allowing you to let the boat churn through non-boss monsters on its own. The Prestige Loop: (inter-session) When you reach the point that you are not able to reliably progress to the next level, you can "Prestige" to reset your expedition, in exchange for relics that can be spent on incredibly powerful permanent boosts to damage and currency, allowing you to reach new distances on your future attempts. Player's choices here allow them to specialise into certain types of damage, as they may prefer to focus on the idle or the active damage sources. The Passive Loop: (inter-day) To further bolster your expedition, you can hire crew for your boat, and train them up. These crew give even further boosts to your damage and currency, making your boat even more powerful the longer you play. The LiveOps Loop: (inter-week) Each week, a new crew member becomes available. As long as you hire them, you keep them forever. Just make sure to train them up as much as possible during their event week! How we built it While the reference games I looked at were entirely 2D, I felt it was important to include the Horizon Worlds Avatar, to tie the identity of the player into the world. To do this, I split my UI into two separate parts. The interactive elements are rendered as usual on a blocking screenspace canvas, while the background and world etc. are rendered on a world-space canvas positioned behind the avatar, aligned with the static camera. Challenges we ran into As idle games are typically "Lean Back" games, often played while also doing something else like watching TV, I felt it was important to support one-hand play, and therefore portrait mode was required. Although I knew portrait support was coming, I did not want to rely on it being released in time, and therefore the canvases are all being rendered in landscape and then rotated at the last stage to fit the portrait screen. Incremental games like this are very well suited to tournaments and leaderboards, however due to not having a 3D space, I was not able to incorporate the leaderboard gizmo into my world in any meaningful way. While I have still hooked up progress to PVars and Leaderboards for consumption by the horizon platform outside of the world, I would have liked to be able to access some kind of leaderboard API to include the information in my own screens Accomplishments that we're proud of With my worlds, I generally always find myself trying to create something very distinct and different from most other experiences on the platform. I am very pleased how this world has turned out in that respect, as I feel the theme shines through very strongly, but I am especially happy with how well the Horizon Worlds Avatar being included fits in, as it really feels like I can still play as MYSELF in this dark eldritch world. In order to get the constant growth and progression that is native to incremental idle games, I needed a solution that would not limit me to the max value of a "number". The game is therefore built on a custom Number object, stored as the mantissa and exponent, allowing the game to scale indefinitely. What we learned I found the talks from Connect especially insightful to help me organise my thoughts and plans around how best to build this entry as more of a "complete game" than just a series of fun ideas and concepts. I made sure to pay attention to gameplay loops, a rewarding sense of progression, and potential for live ops and events in the future. What's next for The Vigilance While the gameplay is intentionally shallow, there is still SOME further depth that could be added, by added real time interactive elements for the players to respond to. Some examples could be: Boat addons that require a tap to activate them: e.g. Giant cannons / Mines, that the player can choose when to deploy for maximum impact before they go on cooldown. Supply drops that appear, and can be claimed in the environment by tapping on them. These could supply currencies or short-term buffs. I am happy to have SOME element of Live Ops in, but feel there is much more that could be added here, in the form of alternate game modes and time limited challenges for players to compete on. <div