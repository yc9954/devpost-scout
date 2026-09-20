---
slug: "chaos-vectors"
url: "https://devpost.com/software/chaos-vectors"
title: "Chaos Vectors"
hackathon: "Pygames"
organization: "Microsoft"
winner: true
words: 211
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# Chaos Vectors

> Destroy all invading Vectors.

[Devpost](https://devpost.com/software/chaos-vectors) · hackathon [[Pygames]]

## Facets


**stack** pygame, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chaos vectors

## Body

Inspiration The game is heavily based upon GridWars - a highliy addicting game from more than a decade ago. What it does Random enemies appear on a grid. Evade or destroy the enemies. Grab power ups to increase chances of survival. How we built it Everything element of the game rendered using vectors. The player ship, enemies, the background, particle effects, and even the text on the screen are drawn using basic pygame.draw.line. The gameplay stays mostly loyal to GridWars - using some of its original algorithms and spawn rates. Challenges we ran into The basic drawing module of pygame does not have the common methods of a drawing library such as translate, rotate, scale, save and restore state. I had to implement one with a minimal matrix-vector library. With hundreds of elements on the screen, the performance of the game begins to suffer - even with the basic line rendering. The number of elements on the screen has been capped to maintain performance. Accomplishments that we're proud of Being a novice at python, What we learned Coding in Python. Creating a game with pygame is fun and surprisingly easy. What's next for Chaos Vectors Improve the graphics and the performance of the game. Add more elements to the game. <div