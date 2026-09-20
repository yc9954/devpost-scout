---
slug: "map-slide-puzzle"
url: "https://devpost.com/software/map-slide-puzzle"
title: "Map Slide Puzzle"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 343
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Map Slide Puzzle

> Create a map of the island with a treasure. Pure Flutter animations and unique handcrafted vector arts on each tile. Touch/mouse/keyboard support. Works on all platforms that Flutter offers.

[Devpost](https://devpost.com/software/map-slide-puzzle) · hackathon [[Flutter Puzzle Hack]]

## Facets

**substrate** [[geospatial]] [[video_visual]]

**stack** dart, flutter

## How they structured the write-up

- inspiration
- what it does
- how i've built it
- challenges i've ran into
- accomplishments that i am proud of
- what i've learned
- what's next for map slide puzzle

## Body

GIF macOS iOS & Android Linux Windows 11 Web Inspiration My children inspired me , they wanted me to take part in this competition at the expense of the time I don't spend with them. Their favorite book is "Treasure Island". Of course, they've already finished this game a million times during testing. What it does The goal is to put the tiles together to form a path to the treasure island. Each tile has unique animation created entirely in Flutter . There are no raster images in the app at all . The tiles have a reduced color saturation until the player puts them all together or when the mouse hovers over them. Once the island is complete, they start playing with all colors and the user will find a treasure chest . How I've built it The application is based on a sample project provided by VGV. State Management is BLoC , the application is covered by almost 100 percent tests. Animations are also controlled via Streams . Vector backgrounds are made in Affinity Designer and exported as SVG, optimized with SVGO . Challenges I've ran into I have encountered problems with SVG rendering on browsers other than Chrome and especially on mobile devices, so there I force rendering via SKIA . Also, audio on desktop platforms was not easy to implement. Accomplishments that I am proud of I think the app has done a good job of animating the foregrounds, which are made entirely from the Flutter widgets. I have a lot of experience with Rive and of course, it will be much easier to create such animations there, but it would affect the performance on the web a lot. So the result is pixel-perfect animations with maximum FPS . What I've learned I learned a lot about the animations and widgets that Flutter provides and how to create non-trivial objects and their animations with it . What's next for Map Slide Puzzle In the future, I would like to add a unique sound effect to each tile . <div