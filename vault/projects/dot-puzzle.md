---
slug: "dot-puzzle"
url: "https://devpost.com/software/dot-puzzle"
title: "Dot Puzzle"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 285
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Dot Puzzle

> Puzzle that feels like it is alive and reacts towards the user interactions

[Devpost](https://devpost.com/software/dot-puzzle) · hackathon [[Flutter Puzzle Hack]]

## Facets

**substrate** [[video_visual]]

**stack** dart, fluttter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dot puzzle

## Body

Inspiration I wanted to create a puzzle that feels like it is alive and reacts towards the user interactions, sticking out from the classic puzzle. What it does You can start a game and play it with your mouse, keyboard or even with a touch device. Users have a status of the current game. The game can be restarted if you feel like you are stuck. You will see your movements and the amount of tiles we need to put in the correct place. Chance to change between image or numbered puzzle mode How we built it The game is built based on CustomPainters from flutter, almost everything in the screen is being rendered this way. With MouseRegion and Listener the app knows the exact location of the mouse/finger and adding some math to this the board is being updated to reflect the user interaction. And then of course by using CustomPainter this is shown on the screen. Challenges we ran into At the beginning I ran over a performance issue, becouse the app draws over hundred of dots, each one with a position, color and different opacity. Accomplishments that we're proud of This was a really interesting use for my knowledge in flutter, the puzzle was fun and creative. And is also a clear example of the huge potential that flutter brings. What we learned I learned to render other types of views instead of the normal traditional widgets . I also learned to optimize the rendering flow in flutter. What's next for Dot Puzzle There are a lot! I will love to improve the app animations, improve how the status is shown to the user and also how sounds are being handled. <div