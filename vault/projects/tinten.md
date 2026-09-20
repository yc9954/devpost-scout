---
slug: "tinten"
url: "https://devpost.com/software/tinten"
title: "TinTen"
hackathon: "Reddit’s Games with a Hook Hackathon"
organization: "reddit"
winner: true
words: 380
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# TinTen

> Tap and hold rhythm game built with devvit!

[Devpost](https://devpost.com/software/tinten) · hackathon [[Reddit-s Games with a Hook Hackathon]]

## Facets


**stack** canvas, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tinten

## Body

Inspiration I wanted to make a UGC rhythm game on reddit that can be played inline in the feed, and requires only a single tap to play. Users can create custom sprites/art, via an integrated drawing tool, using a consistent art style. They can even create animated sprites, and share them with the community, giving full creative control over how your level looks. My intention is for creators to create their own visual experience in their level, almost like taking the player on a rollercoaster ride. They can decide which sprites go where, when the background changes, how the player moves. What it does Users upload music (I am working on generating some preset songs for the game also, to lower the creation entry barrier), and then the game auto detects the beat, and lets them record nodes to generate the level layout. They may also create/draw custom sprites for their levels for decoration, and arrange nodes and node transitions however they like for their level structure. Gameplay involves tapping when your avatar passes over a beat node. Your timing impacts your score %. There are 2 modes, safe mode and hard mode. Safe mode is designed for more casual players, and allows mistakes without killing you - but limits your score potential. Hard mode allows for full points but each time you miss a marker you have to restart. On level completion you're assigned a score based on your performance, and it goes into the leaderboard! How we built it React, canvas Challenges we ran into Finding a way to make it visually engaging. I spent a lot of time on helping users 'feel' the music via visuals, effects, transitions. Accomplishments that we're proud of Publishing a UGC game! What we learned Lower creation barrier to entry as much as possible, and provide users the tools so that they don't need to be incredibly creative to make something good, but ensure the super creative users can express their skills still. What's next for TinTen I'd like to visit ways to increase the skill ceiling/level of the gameplay. for example orbs that you have to actually tap on directly instead of the 'tap anywhere' approach. As well as a small sample library of premade tracks for creators to use <div