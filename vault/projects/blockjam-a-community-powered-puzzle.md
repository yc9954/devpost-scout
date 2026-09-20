---
slug: "blockjam-a-community-powered-puzzle"
url: "https://devpost.com/software/blockjam-a-community-powered-puzzle"
title: "BlockJam - A Community-Powered Puzzle"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 489
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/immigration_refugee"
  - "substrate/structured_db"
---

# BlockJam - A Community-Powered Puzzle

> Slide & Solve, Build & Share!

[Devpost](https://devpost.com/software/blockjam-a-community-powered-puzzle) · hackathon [[Fun and Games with Devvit Web]]

## Facets

**domain** [[immigration_refugee]]
**substrate** [[structured_db]]

**stack** devvit, javascript, phaser.js, redis, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- what's next

## Body

BlockJam - Make Or Break Out! BlockJam: A Community-Powered Puzzle Game Inspiration It's a running cliche on some reddit communities that Tetris is a cure to PTSD. Personally I have always found block puzzles to be comforting and soothing, especially without constant ad interruptions and upsells, so I wanted to build something like that for Reddit. This led to the idea of BlockJam, a block puzzle game which I think really belongs on Reddit: you come for the entertainment of the game, but you stay because you find an outlet for your own creativity and community in the accompanying Puzzle Builder. To bring this to life, I took on learning both Phaser 3 and Devvit, building the entire project from the ground up for this hackathon. What It Does BlockJam is a grid-based block puzzle game with a simple goal: clear the board. Players are presented with a grid full of colored blocks and must strategically slide each shape off the board through a matching colored "exit" on the border. (Another name I considered: "Exit Strategy".) It's a game of spatial reasoning and quick thinking, as blocks can block each other and timers can run out, and grids can be different for every game, requiring players to figure out the optimal order of removal. What makes BlockJam a real community experience is the Puzzle Builder that accompanies the game. This tool allows users to design, test, and finalize their own unique puzzles and have others play it. The builder is a multi-stage application that includes: Interactive Grid Construction Outlet and Shape Placement Live Collision and Rule Validation Automatic Difficulty Analysis This aspect of the game is designed to empower the Blockjam community to generate new, clever, enjoyable puzzles and doing their best to create games that aren't just a simple matter of swiping but rather strategizing. Although timed games are planned for the near future, for now users can take as long as they need to solve a puzzle, although it pays to solve it fast! The leaderboard of every post shows the players who solved the puzzle fastest, in order, and how many total players attempted the puzzle. All the data is handled by reddit's redis database. How I Built It The game and the builder are built using Phaser 3 and integrated into the Reddit ecosystem with Devvit Web . I did my best to focus on an enjoyable UI, and learned a lot about game graphics in the process. Devvit of course is its own special learning experience. IYKYK! What's Next So many things I still need to do to make this the game I envision: Harder blocks with constraints like single axis movement, locked blocks, timed blocks, interlocked blocks. User-chosen color schemes, grid sizes. Timed games and multi-player matches. User-powered awards; special flairs and acknowledgements for really good puzzlemakers. Thank you for checking out BlockJam! No video for now, just go and play it! <div