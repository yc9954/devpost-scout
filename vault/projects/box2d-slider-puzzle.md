---
slug: "box2d-slider-puzzle"
url: "https://devpost.com/software/box2d-slider-puzzle"
title: "Box2D Slider Puzzle"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 344
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Box2D Slider Puzzle

> This puzzle uses Box2D physics. The goal is to fill up the containers with the particles, to be able to see the containers' numbers. Then do the normal Slide Puzzle.

[Devpost](https://devpost.com/software/box2d-slider-puzzle) · hackathon [[Flutter Puzzle Hack]]

## Facets

**substrate** [[video_visual]]

**stack** box2d, dart, flutter

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for box2d slider puzzle

## Body

Use physics to solve the puzzle Modify the world physics with Geek Tools Create more particles, at the cost of a time penalty Inspiration I wanted to do something creative and fun, as well as something that would be challenging. I've been meaning to delve into Box2D, as it is an area that the Flutter community can use more plug-and-play packages. This was a demo for me to see how possible it is, and whether I would like to create such a package. What it does Obviously, a puzzle slider :) But to be able to SEE the numbers, you first need to fill the containers with particles that fall from the sky. These particles react to physics (gravity and collisions). So managing the particles may prove to be a greater challenge than the sliding puzzle ;) How I built it I go into more detail on Github and at some point, I'll expand the Box2D knowledge I learned into a package/video/article. Challenges we ran into I was mindful of performance from the start. I initially did all of my development targeted towards macOS, as I wanted hot reload during development. I was pleasantly surprised that the performance on Chrome was decent! ... on a M1 Pro... some devices will struggle for sure. I also ran into this: https://bugs.chromium.org/p/skia/issues/detail?id=11275 After spending a chunk of time cleverly optimizing the way I scale and resize images, which worked on macOS, but then couldn't work on web. I also had to tweak my initial game idea slightly, to make it actually fun and playable. Accomplishments that we're proud of That it works :) What we learned Box2D. Also had fun looking at VGVs code, but my heart lies with Riverpod. What's next for Box2D Slider Puzzle I want to create a Box2D Flutter package that makes it easier to do debug painting (representing what is happening in a Box2D world) for Flutter. As well as then showcase how you can use these physics with actually Flutter widgets. Think the counter app, but with gravity and collisions! <div