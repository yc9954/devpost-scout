---
slug: "headbanger-60"
url: "https://devpost.com/software/headbanger-60"
title: "Headbanger 60"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 524
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
---

# Headbanger 60

> Fast paced, head swinging according to beats? - nah it's not a metal concert IT'S HEADBANGER 60

[Devpost](https://devpost.com/software/headbanger-60) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** javascript, lens-studio, mixamo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for headbanger 60

## Body

MainMenu Missed Successful Hit Start Game Over Inspiration The game is inspired from 2 missions of GTA San Andreas, wherein you have to dance in particular directions according to direction of scrolling arrows. The difference in my game is instead of keyboard input, we tracked facial movement. What it does Take control of your 3D Bitmoji in this high-speed, head-tracking rhythm challenge. Match the dance steps using real-world head movements to rack up points and trigger epic dance moves. Hit the Beat: Move your head in the target direction to stay in the groove. Chase the Combo: Chain Perfect hits to skyrocket your multiplier and maximize your score. Claim the Throne: Build your legacy and climb the Global Leaderboard to prove you're the ultimate dance-floor quant. 60 Seconds. One Beat. No Misses. How we built it Core Systems & Logic Input Mechanism (Head-Tracking): The game leverages the Face Mesh and Head Transform to track real-time directional movement. By mapping head tilts to the four cardinal directions (Up, Down, Left, Right), the user’s face becomes the primary game controller. Dynamic Arrow Spawner: A randomized spawning system generates directional arrows that travel toward a central hit zone. To maintain difficulty scaling, the spawning frequency and movement speed ramp up linearly over the 60-second duration. Intensity Mapping: The game logic features a specialized "Final Push" phase. During the last 15 seconds, the speed and density reach maximum intensity, challenging the player's reflexes for a high-scoring finish. Bitmoji & Animation Integration Animation State Manager: The player’s 3D Bitmoji serves as the visual anchor. Correct hits trigger specific dance states within the State Manager, ensuring the avatar’s choreography is perfectly synced with the player’s head movements. Feedback Loops: * The Hit Zone: A central timing circle acts as the trigger point. Precision Scoring: Hits registered inside the circle grant points, with "Perfect" timing feeding into a Combo Multiplier for exponential score growth. Persistence & Global Competition Global Leaderboard: Integrated via Snapchat’s Connected Lenses API, allowing for real-time score submission and global rank tracking. Persistent Storage: High scores and max combos are saved locally using the Persistent Storage System, ensuring players can track their personal bests even across different sessions. Challenges we ran into I am a Unity developer and it was my first time using Lens studio. It was challenging to adjust to different interface, scripting and UI. My bitmoji was disappearing quite a lot of times, I imported wrong leaderboard package, facetracking is hardcoded so to test the angles it took time, and obviously repeated testing gave me neck pain :) Accomplishments that we're proud of Being able to finish the game, it was a roller coaster ride, I believe the game is quite catchy and the fact I was able to finish such a catchy game is quite a thing to be proud of . What we learned A good understanding of how lens studio works, Bitmoji and also a few things about mixamo that I wasn't sure about What's next for Headbanger 60 Become a trend; it has got the potential to get there-> catchy, fast paced, feedback, high involvement. Yeah why not go viral? <div