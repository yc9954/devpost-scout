---
slug: "iso-chess"
url: "https://devpost.com/software/iso-chess"
title: "Iso Chess"
hackathon: "The Reddit Daily Games Hackathon"
organization: "reddit"
winner: true
words: 964
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/sensor_telemetry"
---

# Iso Chess

> An isometric chess game with full matches against the computer for all skill levels, plus puzzles from historic games. Fast-loading and lightweight with minimal dependencies

[Devpost](https://devpost.com/software/iso-chess) · hackathon [[The Reddit Daily Games Hackathon]]

## Facets

**domain** [[labor_employment]]
**user** [[developer]]
**substrate** [[sensor_telemetry]]

**stack** canvas, css3, html5, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for iso chess

## Body

Inspiration I’ve been making a lot of games lately and really enjoy the process, especially when I can keep things lightweight. I prefer working with the basics TypeScript and the Canvas API and avoiding heavy dependencies. I've played chess since I was a kid. My grandfather gave me my first chess board, and in a way, this project is me handcrafting a digital one for others to play on. There's also a fun bit of family history with chess. During the 1972 World Championship in Iceland, Bobby Fischer ran into my mom. She claims he asked her out on a date and she turned him down. It’s just a cool story from an iconic era of the game that’s always stuck with me. What it does Iso Chess is a minimalist, isometric chess platform designed to be fast and functional. It gives players two main ways to engage with the game: Daily Puzzles Every day, the app pulls a "checkmate in X" puzzle from a famous historic game. It’s a quick way to test your tactics against positions once faced by the pros. Full Matches vs. AI You can play a complete game against a computer opponent that scales to different skill levels. Persistent Sessions I built it to save unfinished games to local storage automatically. If you have to close your tab or walk away, you can jump right back into your match exactly where you left off. Lightweight Performance Because it’s built with minimal dependencies, the game loads almost instantly and runs smoothly in any modern browser / reddit app Play Anywhere I made sure the game works whether you're on a desktop, a tablet, or a phone. The isometric grid scales to your screen, and the controls feel natural whether you're clicking with a mouse or tapping on a screen. How I built it I wanted to keep the game lightweight and minimal, I avoided big game engines and stuck to TypeScript and the Canvas API. The Engine I wrote the isometric engine and coordinate math from scratch, reusing some logic from my previous projects but tailoring it specifically for a chessboard grid. The AI I integrated the js-chess-engine package to handle the move logic. To keep the UI from freezing while the computer "thinks," I offloaded the engine's computation to a Web Worker. This keeps the animations smooth and the game responsive on another thread. The Puzzles I found a collection of historic games in text format and wrote a custom script to parse and convert them into a JSON format that my game can read. I also set up a cron job to handle rotating the daily puzzle automatically. The Art I created all the assets and sprites myself for this version. I’m not an artist by trade, but it was important to get the initial version finished. I'm definitely open to considering any contributions if someone wants to submit better or different art assets down the road. Challenges I ran into The technical hurdles weren’t necessarily bugs, but rather the architectural decisions that come with an iterative process. Refactoring and Growth I started with most of the logic inside a single Game class. As the project grew, I had to balance the speed of implementing features with the need for clean code. Moving from that "God Class" to a more modular system breaking logic down into controllers and smaller parts that communicate via callbacks took a lot of discipline and constant refactoring. Creating a Shared Engine I decided to build this in a workspace where I could reuse logic from a previous isometric project. The challenge was identifying which parts of the code were truly "generic" and which were specific to Chess. Decoupling that logic so the engine could live at the root and serve two different games simultaneously required a lot of careful planning. Visual Identity Since I’m not an artist, finding a visual style that worked for a isometric grid was a constant back-and-forth. I spent a lot of time iterating on what looked "right" for the board and pieces to ensure the game felt polished. Accomplishments that I'm proud of Smooth Performance I’m really happy with how the Web Worker implementation turned out. The AI can think through complex moves without the UI lagging or the browser freezing. Zero Bloat The game loads almost instantly. I managed to keep the dependencies to an absolute minimum, which was a core goal from the start. Homegrown Engine Building the isometric coordinate system and rendering logic from scratch and then successfully turning it into a reusable engine for other projects is a big win for me. What I learned Power of Refactoring This project reminded me that it’s okay to start with a "messy" single file to get the logic working, as long as you have the discipline to go back and break it down into proper controllers and classes later. Worker Communication Passing complex game states back and forth between the main thread and a Web Worker taught me a lot about data serialization and keeping state in sync across different threads. Asset Management I learned a lot about how to structure a workspace so that a central engine can feed multiple game projects without breaking either of them. What's next for Iso Chess Visual Polish I’m happy to consider any art contributions from others to replace my "programmer art" with something more professional. Future Support It really depends on the reception. If the project gets some traction and people actually use it, I’m happy to keep supporting it and adding new features. Portfolio & Growth If not, I’m still happy with where it is. It was a great way to learn more about engine architecture, and it serves as a solid piece for my portfolio. <div