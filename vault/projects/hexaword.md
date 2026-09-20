---
slug: "hexaword"
url: "https://devpost.com/software/hexaword"
title: "Hexaword"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 666
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
---

# Hexaword

> A daily word game! Arrange tiles to form words and make the target shape.

[Devpost](https://devpost.com/software/hexaword) · hackathon [[Fun and Games with Devvit Web]]

## Facets


**stack** dnd-kit, express.js, networkx, python, react, redis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hexaword

## Body

Mid way through a game, can you figure out where the last tiles go? GIF Playing Hexaword on mobile How to play Hexaword The stats screen - me coming 5th/8 at my own game was disapointing. Inspiration I was inspired partly by Syllacrostic - I liked the idea of breaking up words into chunks, and the gameplay of combining them. I was also inspired by an old game I tried to make, which involved making chains of words where adjacent words shared a meaning. That idea turned out to be pretty confusing and unfun, but the idea to do it with syllables seemed much better. An example: PI-TY-RES-ULT - all adjacent pairs form words. From there, the idea just got out of hand... I first went to square grids, and finally to hexagonal ones - where all adjacent tiles form words. What it does Hexaword is a daily puzzle game. Every day, you're given 6 tiles and a target shape. The goal is to arrange the tiles to make the target shape, and so that all neighboring tiles also form words when read left to right. How we built it I started off experimenting with different puzzles. I even made some hacky code to generate some simple puzzles which I wrote out on pieces of paper. My girlfriend and I struggled to solve a few sample puzzles like that... Simpler variations with chains of prefixes and suffixes. After I found the hexagonal grid idea and found some puzzles for it, I got cracking on the UI. I tested a few drag and drop libraries for react, before settling on dnd-kit (with some tips from of a kind user discord channel to set it up). The backend was surprisingly straightforward with redis - saving users' fastest solves, etc. Challenges we ran into The first and hardest step was building/finding puzzles, this took a lot of effort. I wanted the puzzles to have a unique shape. These shapes are called Polyhexes - which are simply shapes made out of joined hexagons. Armed with the wikipedia page I generated all Polyhexes with 6 tiles, and narrowed them down to a list of different board shapes I liked. Next I set out to find arrangements of words which filled the grids. I did this by building a directed graph of word pieces, so that e.g. "STOR" points to "RY" because "STORY" is a word. Then I could turn the grid layouts into graphs too. Represent each tile as a node, and nodes share edges if they should form a word. Finally, I could search the Word graph for subgraphs matching the Grid graph. I wrote a multithreaded solver, too, and let it run. The result was 30 million unique puzzle layouts (about 4GB) - which I narrowed down to a set of puzzles for the game, posted daily. I found 183 boards with no overlapping words, which make up Hexagrid's first run of puzzles. One smaller challenge among all of that was simply finding a list of words that seemed 'fair' for the game: no countries/towns, names, or words spelled differently in US or UK english. Names which are also rarely-used 'good' words were annoying, e.g. Josh. These would show up on scrabble dictionaries as well as high on word frequency tables. Accomplishments that we're proud of I'm quite proud of the little animations in the game, I just think they're quite satisfying. That little slide-over -> slide down animation took lots of tweaking to get it just right. I'm also proud of the puzzle generation - that was a significant effort. What we learned I learned a lot about puzzle generation and word stuff. It was also my first 'real' project in react, which I'm now a fan of. I learned dnd-kit too and how to write programs involving drag & drop interactivity. What's next for Hexaword I'd love to get people playing it! I've playtested it with some friends, who like it... Hopefully more people will too! <div