---
slug: "traffic-slide"
url: "https://devpost.com/software/traffic-slide"
title: "Traffic Slide"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 355
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
---

# Traffic Slide

> Take the slide puzzle but make it more dynamic. Escape the police by dodging the traffic and achieve a new highscore.

[Devpost](https://devpost.com/software/traffic-slide) · hackathon [[Flutter Puzzle Hack]]

## Facets

**domain** [[transportation]]

**stack** flame, flutter

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for traffic slide

## Body

The games main menu, with a nice reveal animation when you start your game Traffic is hindering your escape Inspiration A huge inspiration were definetly the endless runner games I sometimes played when I was younger. I wanted to have somethin similar for this project but with a slide puzzle. I also took inspiration from a classic game element, the chase. What it does In Traffic Slide you play a race car, which escapes the police. On the chase there will occur blocked roads, the player has to move the cars to clear the road, but always keep in mind, the police is just around the corner, so you better be fast. How I built it This game is based on the Flutter Flame game engine, to easily implement a parallax background. The board and both cars are also flame components. But as I wanted to build the sliding board with Flutter Widgets, I used a service based architecture to update a positioned widget, which places the board, according to the components position. The overlay is also built with pure Flutter. Challenges I ran into I had a hard time making the game responsive, considering the game is highly dependent on a correct positioning. On every resize the underlying components need to be updated. To not have problems, with resizing while running the game, the game gets automatically paused if there is a resize. I also had a hard time, getting to know the way a vectorgraphic editor works, so that I can create my own assets What I learned As this was my first project, where I needed a responsive layout, I learned many things around how to make your project responsive. I also improved my problem solving skills along the journey, because, let me tell you, there were a lot of problems while developing Traffic Slide. What's next for Traffic Slide There will be a mobile version of this game. I didn't manage to publish this version in time for this hackathon, but there will be a version for mobile, as it is way to easy to publish cross plattform with flutter. <div