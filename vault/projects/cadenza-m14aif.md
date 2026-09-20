---
slug: "cadenza-m14aif"
url: "https://devpost.com/software/cadenza-m14aif"
title: "Cadenza!!"
hackathon: "2019 Developer Circles from Facebook Community Challenge"
organization: "Facebook"
winner: true
words: 605
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Cadenza!!

> Hit falling notes on a keyboard to the beat of the music ... in VR ... in a browser

[Devpost](https://devpost.com/software/cadenza-m14aif) · hackathon [[2019 Developer Circles from Facebook Community Challenge]]

## Facets

**domain** [[developer_tools]]
**substrate** [[geospatial]] [[video_visual]]

**stack** aframe, html5, javascript, pixi, three.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for cadenza!!

## Body

It's like guitar hero but with 8 keys, in the browser, and with VR support Inspiration I came across this sick looking rhythm game in Japan and thought it'd be nice if I could play something like that at home. Existing VR rhythm games that tend to involve hitting the notes themselves weren't exactly what I was looking for. What it does Cadenza!! is a WebVR rhythm game where you hit falling notes on a keyboard to the beat of music. On VR devices with hand controllers, the user strikes the keys using mallets. Without a VR device, the game can be played on keyboard or with a touchscreen. How I built it Before the hackathon, I had built a prototype for the game with AFrame/three.js. This involved developing: a beatmap schema, note creation and music synchronization logic in order to play beatmaps, and collision detection logic in order to register/handle key hits. I also made a really basic beatmap making tool using Pixi.js which I used to create the prototype's beatmap. During the hackathon period, I built on top of the prototype game and tool. Features added during hackathon period Game Features Menu system Simple graphics effects Custom environment Support for notes of varying width (used in easy maps) Haptic feedback for VR devices Mallet bounce behaviour when a key is struck from above Keyboard support Touch support Basic score system and persistence of high scores Basic camera adjustments based on client dimensions A name Beatmap Editor Features Support for notes of varying width Keyboard shortcuts for copy/pasting and deleting notes Ability to import beatmaps Ability to zoom in and out Midi to beatmap conversion script Challenges I ran into Hitting the notes was unsatisfying -> added haptics, mallet bounce, and graphics effects -> needed to keep performance in mind for graphics effects -> learn about shaders Did not want to use the prototype environment -> wanted a reflected sky type of thing -> dive deeper into shaders -> eventually find a sun-sky component for aframe -> eventually figure out I can just add a second sky into the scene rather than reflect it with a shader Even with the editor I made, beatmap making was slow and tedious. I also needed to get more music for the game -> midi to beatmap conversion algorithm + find public domain midi files that feature solo instruments Debugging in VR was kind of slow -> added keyboard support Accomplishments that I'm proud of Designed and developed custom shader effects for the first time. Designed and developed a simple menu system that easily supported various input methods. Developed a midi -> beatmap conversion algorithm. What I learned The basics of shader programming. Shaders for realistic looking atmospheres involve some nasty math/physics . Shadertoy eats weak gpus for breakfast. Glitch is useful for experimenting with web technologies/frameworks/libraries. Searching Google Fonts for fonts that support specific sets of characters (left and right arrows in my case) is a pain. Monospaced fonts are good for text-based menu systems. Melody detection is a thing, but as with most machine learning related stuff, all the code for it is in Python. The Mutopia Project is good for finding free midis of classical music LMMS is useful for modifying midi files and converting them to .ogg or .mp3 What's next for Cadenza!! Improvements to the midi -> beatmap conversion algorithm More beatmaps Polishing up and releasing the beatmap tool Ability to load beatmaps from file Ability to save and share replays Ability to load and play midi files without needing to convert to the beatmap format More note types Fancy graphics effects <div