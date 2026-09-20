---
slug: "totalled"
url: "https://devpost.com/software/totalled"
title: "Totalled"
hackathon: "The Reddit Daily Games Hackathon"
organization: "reddit"
winner: true
words: 573
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/geospatial"
---

# Totalled

> Drag numbers to form expressions and hit the targets!

[Devpost](https://devpost.com/software/totalled) · hackathon [[The Reddit Daily Games Hackathon]]

## Facets

**substrate** [[geospatial]]

**stack** react, tailwind

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what's next for totalled

## Body

Splash screen The game in full screen mode Game end state Leaderboard Inspiration I'm a big fan of the Linkedin games. Zip is my favourite. A takeaway that I've come to understand from these daily linkedin games was how quick and satisfying it needs to be to keep people coming back daily. Here are a few learnings from Zip that went on to define my game - The game should have simple mechanics and intuitive to understand Playing the game should be satisfactory and give the user a sense of achievement Users should be able to complete the game in less than 20 seconds The final screen should be rewarding to keep the user coming back What it does Totalled is a fast-paced math puzzle game where players drag through a 3×3 grid of numbers to create mathematical expressions. Each game presents three target numbers that players must find by connecting adjacent cells, with operators (+, -, ×) between them automatically applied left-to-right. The game tracks completion time down to centiseconds, encouraging players to beat their personal best. The timer doesn't start until the player starts dragging, so the ones who plan the paths are rewarded for their efforts. Players can request hints at the cost of a 10-second penalty, adding a strategic element to the speedrun challenge. How I built it Totalled is built with React and TypeScript for type-safe component architecture, styled with Tailwind CSS for a clean, minimal aesthetic. I used Framer Motion to create smooth drag interactions and satisfying animations when targets are found. The game features a custom drag-and-drop system that works seamlessly across both desktop (mouse) and mobile (touch) devices. The path visualization uses SVG rendering with Manhattan-style routing and rounded corners for a polished feel. Vite powers the development environment for fast iteration and optimized production builds. Challenges I ran into Thre was 2 big problems with the game - Information overload With the game involving 9 numbers and expressions, major work had to be done on the UI to make the game look un-cluttered and intuitive. I stuck to a 3x3 grid: simple while still offering multiple patterns of expressions Displayed the operators between the grid in a dark background color to make it look de-cluttered. Positioned the clock, targets, current path and the gameplay grid in order Players get frustrated when stuck The initial version of the game was too hard for many players, since they had to calculate large expressions mentally. To mitigate this, I added- A block where the current expression is calculated dynamically and shown to the player A limit on the number of multiply operations, limited digits to 0-5. A hint system that shows the starting point and the path. What's next for Totalled Game variants Experimenting with grid size (4x4) Addition of walls/no go zones where the user cannot drag Addition of a mystery target with a clue to figure out what the target could be "Largest number" mode, where users can try collecting the largest number ever "Infinity mode" where users can collect all possible combination of numbers Leaderboard & engagement A way to reward flawless execution in scoring (not try multiple paths) Experiment with a target based scoring system where users are timed for each target Global leaderboard across all daily games User flairs for regular players, highlighting average time Comment system where users can share a snapshot of their path to victory (like a heatmap) <div