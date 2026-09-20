---
slug: "flutter-rush-puzzle"
url: "https://devpost.com/software/flutter-rush-puzzle"
title: "Flutter Rush Puzzle"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 408
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
---

# Flutter Rush Puzzle

> Play a new daily rush puzzle game every day

[Devpost](https://devpost.com/software/flutter-rush-puzzle) · hackathon [[Flutter Puzzle Hack]]

## Facets

**domain** [[transportation]]

**stack** android, codemagic, flutter, ios, macos, windows, zflutter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

landing_page puzzle_page_3d puzzle_page_2d victory_page Inspiration As kids, we loved puzzles, all kinds of puzzles. Our favourite one was Rush Hour , a slide puzzle that consisted of displacing cars to let a jammed vehicle drive through the exit. This was our inspiration. Our goal was to bring our favourite puzzle to Flutter; and we wanted this to be in three dimensions, just as how we played it. What it does Our puzzle allows the player to play a daily Rush Hour game. They can drag and slide vehicles, which are projected to appear in three dimensions, in a 6x6 board. The board can be rotated to change the perspective and it can also be toggled to appear in two dimensions. The player must move vehicles to free the ambulance. Whilst the user is playing the number of moved vehicles and time are tracked. Once completed, the puzzle animates and shows the player's score. They can share this with their friends, showing the sequence of vehicles they've moved (with matching vehicle emojis 🚕!). https://flutter-rush.web.app/ (#1) 10: 🚕🚌🚛🚛🚓🚌🚗🚌🚛🚐 How we built it The game is entirely built with Flutter! Our secret sauce is ZFlutter , which allowed us to bring a three-dimension illusion to our two-dimensional Flutter world! Challenges we ran into One of the biggest breakthroughs the project went through was optimisation. More specifically, optimising ZFlutter code to avoid junk. The library has a variety of simple vector arithmetic and render objects and was too slow for our needs. Moving to 4-dimension transformation matrixes allowed us to reach 60 fps. And we are talking about almost 6000 widgets built simultaneously inside a 200 depth tree! Accomplishments that we're proud of We're proud of finishing the game altogether! Being able to experience our favourite childhood puzzle in Flutter was a satisfying experience. The fact that our game can be played in iOs, Android, Web and Windows blow our minds! We're also glad that this project motivated us to improve the open-source package, ZFlutter and we will also be soon contributing with new open-source libraries to support the ecosystem. For example, we will be releasing a new library for building text components. What we learned Bringing a three-dimensional interface to flutter was not an easy task. We learnt throughout the process how to tackle the issues we faced with perspectives, drawing three-dimensional widgets and more! This project allowed us to dive into exploring the possibilities of three dimensions in Flutter. <div