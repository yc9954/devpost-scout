---
slug: "meltdown-vaw85t"
url: "https://devpost.com/software/meltdown-vaw85t"
title: "Meltdown"
hackathon: "Pygames"
organization: "Microsoft"
winner: true
words: 429
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Meltdown

> Block-pushing bullet hell

[Devpost](https://devpost.com/software/meltdown-vaw85t) · hackathon [[Pygames]]

## Facets


**stack** box2d, pygame, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for meltdown

## Body

GIF A GIF showing how blocks can be dragged to control radiation. A level featuring lasers. A level featuring a lot of radiation. A level featuring several receptors (crystals) and one barrel. Inspiration For a few months I've been thinking about this concept for a puzzle game where the main mechanic is to move and rotate shapes in a 2D plane. The shapes would collide and push each other, you control a character, and there's some goal you're trying to achieve by moving the shapes around. The idea takes inspiration from stuff like Tetris, Blokus, Rush Hour (sliding block logic puzzle), and the Moving Sofa Problem , but also just everyday life. Until this week though, I wasn't able to come up with a strong enough hook for the game to make it worthwhile to build - but then the idea of deflecting particles hit me, and that seemed cool, so I decided to make it. What it does The object of the game is to deflect radiation particles from barrels and lasers into receptors (crystals) without absorbing too much yourself. You do this by pushing and dragging objects, which the particles bounce off of. The art, music, and sounds are all original and/or were generated during the jam. How we built it The game uses Box2D under the hood for the physics and particle dynamics, which I learned nearly from scratch during the jam. The rendering is pure pygame, with some tricks to make objects look 3D. Challenges we ran into Since the rendering isn't true 3D, there's no per-pixel depth buffer so shapes don't always overlap correctly (sometimes a shape that should be behind another will render in front of it instead). I know why it's happening, but I didn't have time to figure out a better sorting strategy for the shapes. So that's an outstanding bug (or artistic quirk, however you want to frame it~). Accomplishments that we're proud of I started late, so I'm proud I was able to finish so much in just a week while learning a new framework at the same time (Box2D). It was cool to see the art and gameplay come alive in dynamic ways from the physics beneath them. What we learned I learned how to use Box2D, and how to utilize it effectively in an actual game. What's next for Meltdown I still would like to potentially build a larger game that expands on this shape-pushing mechanic, for which Meltdown would be the prototype. But we'll see. I may add more mechanics and levels to Meltdown too. <div