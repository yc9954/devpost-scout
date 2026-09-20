---
slug: "slideparty"
url: "https://devpost.com/software/slideparty"
title: "slideparty"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 470
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# slideparty

> A cross-platform sliding puzzle game you can play with friends locally or online.

[Devpost](https://devpost.com/software/slideparty) · hackathon [[Flutter Puzzle Hack]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** dart, flutter, heroku, shelf

## How they structured the write-up

- inspiration
- what it does
- you can try at
- how we built it
- challenges we ran into
- what we learned

## Body

Home screen Single mode Multiple mode Online mode - up to 4 player! Inspiration I want to make a puzzle game that runs on all platforms : Android, iOS, Linux, Windows and MacOS. You can play with your friends regardless of what operating system you are using, you just need to have a room number to be able to play online and compete with your friends or you can directly compete with your friends. locally by various types of controls for different types of screens. What it does Just a casual and fun puzzle game! You can try at Demo gameplay video playlist in my youtube channel. Live at here . How we built it The game has two part: Client: I use flutter to make truly one codebase for across platform. Server: I use shelf to make a web server in dart. Client Slideparty has three game-mode Single mode: Play and try to solve as fast as you can a 3x3, 4x4 or 5x5 puzzle board. Features: Auto solving Multiple ways to control game base on current devices Multiple mode: Play with friends in local, you can play upto 4 players. Features: Responsive layout Multiple ways to control game base on current devices Some sort of skills to prevent or annoying your friends for fun Online mode: Enter a room code and you can play like multiple mode but on different devices. Features: Real-time communication All features in multiple mode Server Slideparty server use websocket for handle real-time interaction between players. Use shelf and shelf_router to making a web server is pretty straight-forward. I seperate how client talking to server with mono-package slideparty_socket base on websocket, basically when client send an event and server handle that event, processing how the playboard changed and send back to client a json decoded. Challenges we ran into Auto-solver is pretty hard, first i'm trying to use A* algorithms to find the best solutions. It works well with 3x3 puzzle ... but with 4x4 the time complexity is so huge and immediately block UI thread so with this approach, impossible to solve 4x4 and 5x5 while keeping the app run smooth. After that I trying to find a pattern of the game then i found that if we solve the first row and first column of a N x N playboard and you remain exact (N - 1) x (N - 1) playboard and you can keep solving until N = 1 you solve the puzzle! This solution isn't return the shortest step to solve but it's run pretty fast and it's can solve any N x N board so i'm accept that is not the best solution but it is the fast enough to run smooth solution. What we learned Have fun with flutter Discover how to use dart for backend <div