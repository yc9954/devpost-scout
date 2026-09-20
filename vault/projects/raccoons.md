---
slug: "raccoons"
url: "https://devpost.com/software/raccoons"
title: "Crossbow Castle"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 890
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Crossbow Castle

> A crossbow-based FPS, where you clear your way through rooms of traps and turrets.

[Devpost](https://devpost.com/software/raccoons) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for crossbow castle

## Body

Starting off nice and easy I'm sure there's nothing dangerous behind this door... Things can get steamy in the boiler room Uh oh... Who puts turrets at the end of a bridge?! Lava = hot Inspiration With Crossbow Castle, I was looking to replicate the feeling of first person shooters from the 90s such as Doom and Quake. I am aiming for simple to pick up controls, while still allowing a decent depth of mastery as the game progresses, and arcade-like gameplay to support short mobile gaming sessions. What it does The game is split into a number of "Rooms" that the player can progress through. Once a room is entered and "activated", the doors will lock, and a number of traps and turrets will active. It is then up to the players to shoot enough of the targets that appear to defeat the room and progress onwards. After each room there will be some rewards (XP + gold) and time to rest (health potions) before the next challenge! The world currently contains a brief but comprehensive tutorial, followed by two "wings": The Boiler Room and The Ramparts . How we built it The logic is all built in typescript and the desktop Horizon Worlds editor. The artwork is provided by ChatGPT, mapped onto simple 3D geometry in Blender. Challenges we ran into Early on, my plan had been to constrain the player to a flat plane (such as O.G. Doom) however without the ability to control the pitch speed or override the camera rotation, this was unachievable. This led to the game being considerably harder to play than I had intended, and I really had to dial up the auto-aim. (Using an invisible projectile launcher to detect valid targets every 0.2s) Luckily, part way through the 'Jam, the ability to set the players root rotation was released, and this has the happy little side effect of zero'ing out the First-Person pitch, meaning I was eventually able to achieve the controls I ha initially wanted! (After needing to go through and move all the targets back onto the plane!!) A further issue I had, was due to my decision to use a HUD-based weapon ( for maximum Doom vibes, and to challenge myself to make something that felt "different" ) This means that I hide the 3D mesh of the crossbow for the local player. However, as I am unable to also hide my OWN avatar , I have to leave the "pose" of the crossbow as default. I would rather have it set to something like "pistol" so that other players look more natural, however this led to seeing your own hand in front of the screen. Accomplishments that we're proud of I am very pleased with the overall look and feel of the world, as it is very close to the initial concept I had in my mind. I had been looking to create a world that felt cohesive and well polished despite my own limited artistic abilities, and also gameplay that felt somewhat distinct and unique within the horizon ecosystem. What we learned While my initial decision to build bespoke levels and challenges for the players was based around the traditional premium PC shooter, this has ended up being rather time consuming for relatively little payoff. If I had instead focused on something more programmatic, potentially something wave-based within a static arena... this might have given me a bit more longevity in the content, and saved me time spent trying to design interesting and varied levels. What's next for Crossbow Castle While I was focussing on the gameplay loop for this Jam, I only partially addressed the concept of long term progression. The foundations are IN, for earning XP, Currency, levelling up, but I still need to implement the rest of these systems. For the XP/Levels, this will most likely be something like some simple talent points, so that the player can improve over time, while also allowing them some agency on how they wish to specialise. For currency sinks, I have imagined adding some level of "gear" that can be purchased to improved your players stats such as Health / damage / speed. I also think I will move away from the bespoke hand crafted levels, towards a wave based, horde-mode type thing. This will hopefully increase replayability, and allow me to better scale to different numbers of players, making the world a more viable destination for social visits. I intend to insert variety between sessions with some rogue-like elements, such as choices of power-ups that let you customise your load-out and abilities for that session. Helpfully this again increases replicability, and should add some interesting interplay if players team up and get to specialise in complimentary ways. Once the loop is more scalable, the next focus will be on increasing retention, most likely through some mix of daily login rewards, and lucrative daily tasks. By moving the majority of rewards into these time gated sources, we can reward the play style we want of short sessions, over multiple visits over multiple days. This can be further enforced through in-game live-ops events, such as double XP weekends, or certain game modes that are only available on a schedule. Thereby encouraging players to schedule their visits to the same time, increasing the chance of playing together. <div