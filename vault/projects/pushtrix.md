---
slug: "pushtrix"
url: "https://devpost.com/software/pushtrix"
title: "Pushtrix"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 207
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Pushtrix

> A fast paced number puzzle. Starts easy and gets tougher with time. Big emphasis on fun, nice sound and gfx.

[Devpost](https://devpost.com/software/pushtrix) · hackathon [[Flutter Puzzle Hack]]

## Facets


**stack** dart, firebase, flutter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pushtrix

## Body

Inspiration Inspired by my favourite game of all times: Rez. Combines puzzle solving with funky graphics and music. What it does It's a series of sliding puzzles with gradually increasing difficulty curve. Puzzles get bigger and shuffle count increases. Can you make it into the leaderboard? How we built it Flutter: some implicit animations, but mostly hand animated using CustomPainter. Firebase realtime db for online highscores. Challenges we ran into Hardest thing was tweaking performance for the start screen. Oh and drawing the transparent cubes involved SW backface culling, which was kind of a challenge since my vector maths was a bit rusty ;) Accomplishments that we're proud of I think the whole package turned out to be a fun game. What we learned Learned a lot about animations in Flutter and also how to do a game, since using a declarative framework like Flutter for gamedev which usually has a more imperative approach involving a game loop proved to be quite a challenge. What's next for Pushtrix Features: Add new scenes. Fixes: The mobile builds have sound issues which need to be fixed. Windows build didn't work because of a Visual Studio 22 regression. Waiting for a fix from MS. Eventually release in app stores. <div