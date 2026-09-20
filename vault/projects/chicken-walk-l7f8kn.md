---
slug: "chicken-walk-l7f8kn"
url: "https://devpost.com/software/chicken-walk-l7f8kn"
title: "Chicken Walk"
hackathon: "Meta Horizon Creator Competition: Short Loop Mobile Worlds"
organization: "Meta"
winner: true
words: 647
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Chicken Walk

> Why did the chicken cross the road? To dominate chaos! Dodge traffic, build bridges, and team up to survive wild crossings in this hilarious mobile & VR road-crossing adventure. 🐔🚗

[Devpost](https://devpost.com/software/chicken-walk-l7f8kn) · hackathon [[Meta Horizon Creator Competition- Short Loop Mobile Worlds]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[transportation]]
**substrate** [[geospatial]] [[video_visual]]

**stack** adobe-substance-painter, blender, horizon, horizonworlds, meta, meta-horizon-desktop-editor, metahorizon, procreate, quest, quest3, questpro, typescript, typescript-camera-api, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chicken walk

## Body

Inspiration The idea for Chicken Walk was inspired by the timeless joke, “Why did the chicken cross the road?” with a playful nod to the classic arcade game Frogger. But we wanted more than just a punchline. We reimagined it as a fun, chaotic, hilarious adventure filled with speeding cars, honking trucks, and outrageous obstacles. By blending humor, action, and strategy, we created a game that turns the chaos of road crossings into a fast-paced, laugh-out-loud experience, complete with daring solo challenges and team-based antics like building bridges or stopping traffic. Players will find Egg-straordinary levels. What it does Chicken Walk is a hilarious mobile and VR game where you, as a daring chicken, must navigate chaotic roads filled with speeding cars and wild obstacles. Dodge danger, collect XP, and tackle increasingly hectic challenges. Play solo or team up with friends to unlock shortcuts, slow traffic, and cross the chaos in style! How we built it The game was built with Blender, Adobe Substance Painter, Procreate, Meta Horizon Desktop Editor, and 100% Typescript code. The use of Typescript with the Camera API was essential for this project. We were excited to take advantage of the Camera API and make the game more dynamic by changing the camera distance with every game level. Typescript is also driving the Mobile UI in this game. Mobile players are exposed to a robust UI which uses chicken icons for remaining lives, as well as several chicken and egg icons for in-game messages. Eagle-eyed players will notice that the mobile UI changes depending on the chicken that the player picked. VR players use a more subtle, unobtrusive HUD, and important game notifications are sent via popups. Our team consisted of: Metacrafters (project lead, art, 3d modeling, texturing) voytek.lorenc (Typescript, sound design, character rigging and animation) RandomGamesUniverse (game concept, concept for level design, testing) Challenges we ran into The main challenge in Chicken Walk was to learn how to bifurcate mechanics based on the player’s device type and how to utilize the Typescript Camera API to bring variety to how the chicken characters appear on the screen. Another challenge had to do with efficiently spawning assets across many game levels. To address this, many level elements such as trees, flowers, eggs and even mountains are reused and spawned when the player arrives at the new level. Instead of hiding this technique, we opted to lean into it and present players with fun animations of the world being build right in front of them. Accomplishments that we're proud of It was fun making a Horizon game where the player assumes a form of an animated pixelated chicken. It took a while to get this right. We experimented with various chicken sizes, creative ways to hide the real player avatar legs, and avatar speed. We experimented with character rigging and animating the movement of chicken feet and head. At the end we feel that we managed to create a game where playing as a pixelated chick feels quite organic. What we learned Learning the Typescript Camera API was very rewarding. We are looking forward to making more Mobile/VR experiences in Horizon Worlds. We feel much more comfortable building experiences with bifurcated mechanics that appeal to both Mobile and VR players. What's next for Chicken Walk We have many plans for the future of this game. First of all, we’ll be testing difficulty levels to find the best challenge/fun balance in order to increase time spent and retention. Later we’ll be working on themed and seasonal Levels (whimsical environments like space highways with UFOs or jungle paths with stampeding animals instead of cars and Festive Holidays levels). We’ll make unique Traffic Patterns, Power-Ups (Protective Eggshell: Absorb one hit from a vehicle, etc). Eventually we’d love to release a Build-a-Road Mode where players can design their own chaotic road maps and share them with the friends. <div