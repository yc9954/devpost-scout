---
slug: "way-for-ball"
url: "https://devpost.com/software/way-for-ball"
title: "Way For Ball"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 500
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Way For Ball

> Move the tiles to roll the ball.

[Devpost](https://devpost.com/software/way-for-ball) · hackathon [[Flutter Puzzle Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[web_dom]]

**stack** bloc, flutter, rive

## How they structured the write-up

- introduction
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for way for ball

## Body

Puzzle Screen Start Screen Volume Setting Screen Levels Screen Level Completion Screen Introduction Hey there, We are a team of two, Nehal and Vivek Nehal is a Flutter enthusiast and Developer in Flutter and very active in the Flutter community and events. Vivek is having good experience in JavaScript and Node.js. So we took it as a fun project and we knew we are going to enjoy the upcoming challenges. Inspiration Vivek: Honestly enthusiasm of Nehal inspired me to join this project. Nehal: Honestly Vivek's confidence that we could do this inspired me to start. And we began to build something that was fun and could be played by any age group. And that abides the slide puzzle rules 🙂 What it does Way for ball This engaging puzzle game is really simple, but challenging at the same time. The aim is straightforward – guide your ball through the maze to the exit area. The ball will not roll until you have completed the route. To create the route you must move each individual pattern and solve the puzzle. This is exactly the same as the classic jigsaw sliding games, just digital! Some tiles are movable some are not. One with bolts on them is not movable. The graphics are smooth, and the puzzles become increasingly difficult. This game tests your skill and logic, and is great fun to play! How we built it Flutter was the only choice :D Challenges we ran into To begin with, Vivek had no prior knowledge of Flutter so it was our first challenge. We decided that we are going to make a ball puzzle, writing logic for the ball reaching from one position(circular and linear motion) to another was our second challenge and maintaining the animation of the ball on different screen sizes(after a change in tile sizes) was challenging. Then we encountered resize issues when PNG aspects were not proper, so we pivoted to SVG. Flutter is not very rich in SVG so we had to manually create SVG's by writing code for SVG's as we lacked Designer in our team. Being a JS developer Vivek often found it irritating but managed somehow. We faced challenges to learn Rive, we did some experiments and finally, we were able to put the bird animation. We added some Lottie animation. But if we keep the "Flutter build rendering to HTML " the Lottie animation was not rendering properly so we pivoted to CanvasKit rendering Now in CanvasKit rendering, the refresh rate is different for different devices so we compromised the ball speed. Accomplishments that we're proud of We are proud that we were able to pull it off and convert our idea into a working game even after facing so many constraints. What we learned We learnt a lot about Ball Animation, Using SVG, Lottie, Rive Animation and got to know about a lot of pitfalls in Flutter. What's next for Way For Ball Adding more levels Add hints Add animations Add theme <div