---
slug: "dash-slide-puzzle"
url: "https://devpost.com/software/dash-slide-puzzle"
title: "Dash Slide Puzzle"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 436
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
---

# Dash Slide Puzzle

> Prepare to fight Dash in a no-holds-barred Slider Puzzle! Strategically use various skills to turn the tides in your favor.

[Devpost](https://devpost.com/software/dash-slide-puzzle) · hackathon [[Flutter Puzzle Hack]]

## Facets

**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]

**stack** flutter, rive

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dash slide puzzle

## Body

Inspiration I'm a Flutter developer for years now and its embarrassing for me to admit that I have very little experience when it comes to the nitty-gritty parts of the animation in Flutter. I just couldn't find the right opportunity to dive into it. 😅 After hearing about this hackathon, I knew that this was the right moment to get my hands dirty with Flutter animations and see what I can come up with. What it does This is a puzzle game wherein you get to play with a bot in completing a slide puzzle. It's a bit unfair considering that you're playing with a bot who already knows how to solve the puzzle. So, to even the odds you can cast various spells to disable your opponent. How we built it Basically, I just kept a list of all the features I want in the game and created a timeline for each of my tasks which I revise roughly every week depending on where I am now. The first week was spent mostly with experimenting on different game ideas to see what's feasible and what's not. From there, the app essentially evolved into something that I didn't even imagine at the start of my development. 🤣 Challenges we ran into PUZZLE SOLVING ALGORITHM ISOLATE PROBLEM I recently just learned that Isolates don't work on web. This was an issue because I couldn't run the puzzle solving algorithm in the main thread or else I risk freezing the application. I could think of three possible solutions for this issue, which are: Use a Web Worker for the Web Platform. Use Firebase Functions to host the function for solving the puzzle. Use Future.delayed at certain intervals to release the main thread. After considering the time crunch, I decided to go with the 3rd option because its simpler and faster to implement. Accomplishments that we're proud of The speed it takes for the algorithm to solve the puzzle The different animation poses of Dash Using Rive to animate the puzzle tiles and the background The animating stars at the background What we learned The different ways to do animation in Flutter and which techniques are efficient. How simple and easy it is to create animations with Rive! I'll definitely be using this for my projects moving forward. What's next for Dash Slide Puzzle I always wanted to start writing articles about Flutter as a way to share my knowledge and gain exposure in the Flutter community. Sharing how I implemented different features of this slide puzzle game seems to be a perfect opportunity to do just that! <div