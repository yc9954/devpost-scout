---
slug: "water-slide"
url: "https://devpost.com/software/water-slide"
title: "Water Slide"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 335
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/education"
  - "substrate/code_repository"
---

# Water Slide

> Slide the tiles around until all of them are filled with water!

[Devpost](https://devpost.com/software/water-slide) · hackathon [[Flutter Puzzle Hack]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[education]]
**substrate** [[code_repository]]

**stack** flutter, rive, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for water slide

## Body

Inspiration I got the inspiration for the project from one of my first coding projects! Back in high school I built a tunnel game where the user had to rotate pipes to make them connect. This is similar but with sliding. I've come a long way since then! What it does Water Slide's objective is to slide the tiles around until all of them are in some way connected to the water source. The water source is the cross pipe. How we built it For the animation I used Rive. Each tile has a fill and unfill animation that gets toggled on and off using the Rive Controller. I used 2 layers for the water - a lighter shade that goes in one direction and a darker shade that goes in the other. For the puzzle logic I implemented a depth first search graph traversal algorithm (never thought I'd use it IRL). I also added extra attributes to the tiles to determine what kind of pipe it is. Lastly, I deployed the project using Vercel Challenges we ran into One of the main challenges was animating the water so it looks fluid. It took a lot of trial and error until I finally got something I was happy with. Another challenge was the code. I went off the existing source code provided in the resources so I spent some time figuring out where everything was and what I would need to change. Accomplishments that we're proud of Building a working game that's actually fun to play. I shared it with friends and family and they all seem to enjoy it. What we learned I learned that water is NOT easy to animate. And in general animation is very difficult. Thanks to Rive it made my job a little easier. Overall it was a very fun and rewarding experience. What's next for Water Slide I really want to add more levels in the future as well as a leaderboard (which was requested by a few) <div