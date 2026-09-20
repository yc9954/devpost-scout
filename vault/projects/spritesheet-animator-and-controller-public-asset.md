---
slug: "spritesheet-animator-and-controller-public-asset"
url: "https://devpost.com/software/spritesheet-animator-and-controller-public-asset"
title: "Spritesheet Animator and Controller Public Asset"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 306
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/video_visual"
---

# Spritesheet Animator and Controller Public Asset

> This configurable sprite sheet animator can work with just one image! The asset shows how three sprite sheets controlled by the Player and objects can be used for a 2D mobile game!

[Devpost](https://devpost.com/software/spritesheet-animator-and-controller-public-asset) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[video_visual]]

**stack** customui, horizondesktopeditor, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spritesheet animator and controller public asset

## Body

Inspiration I'd been interested in 2d animation in Horizon since I saw an animation done by swapping textures, however, it also turns out that swapping textures can create a cascade of issues. I set out to make a more efficient animation display by reimagining an old idea: Sprite Sheet Animation! What it does Using a mask to isolate a single image of a sprite sheet on a Custom UI and then moving the sprite sheet position to change the displayed image, I was able to create single image animations! The player controls our central monster and can attack the pig and plant monster. How we built it A SpriteAnimation script holds the animation breakdown of each character and their actions. By splitting the sprite animation into its corresponding rows and columns and labeling each row with its associated action, we can call specific animations. Linking the sprites XY position to the player's XZ position, we're able to interpolate the sprite's screen position and simulate player control. Challenges we ran into Masking a CUI was not intuitive. Creating a reusable method of defining spritesheet animations was difficult. Making a player controller for a Custom UI took some creativity. Accomplishments that we're proud of It's 2D animated sprites, a Player controller with movement reactive animations, a custom input attack, and NPC interaction in Horizon! Cmon! That's pretty unique! And I'm pretty sure it works with multiplayer, which means, my default development workflow is inherently multiplayer compatible at this point. It also auto randomizes the update cycles per CUI to ease the update loads. What we learned How to make sprite sheet animations! What's next for Spritesheet Animator and Controller Public Asset I think there's some pretty fun ways this could work its way into Horizon Worlds. I'm going to keep them to myself for the time being. <div