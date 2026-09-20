---
slug: "slide-for-four"
url: "https://devpost.com/software/slide-for-four"
title: "Slide for Four"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 721
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Slide for Four

> A one vs. one Slide Puzzle (inspired by Tic Tac Toe and 4 Wins)

[Devpost](https://devpost.com/software/slide-for-four) · hackathon [[Flutter Puzzle Hack]]

## Facets

**mechanism** [[realtime_stream]]

**stack** docker, flutter, node.js, rive, websockets

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for slide for four

## Body

Main Menu Single Player Multiplayer Options Multiplayer Inspiration Inspirations for Slide for Four are Slide Puzzles as well as the games Tic Tac Toe and 4 Wins. Additionally, I like to play more competitive games that need some thinking (e.g., chess), and I thought mixing the before-named games could provide an experience like that. What it does You can choose between playing against an Ai (Singleplayer) or another player (Multiplayer) inside the game. When started, the player sees a field with four X and four O, depending on its Token. Then, the player has to move them in the right spots to bring 4 in a line for winning. Possible winning constellations are four in a row, four in a column, or four in a diagonal. The main idea is to play it in multiplayer with your friends. The Singleplayer is to learn the game because the AI is not the smartest yet. How I built it Before starting to build the project, I first created a paper prototype. That prototype consisted of 16 square-formed sheets of paper. Four of them had O, and another four had X. I then played the prototype with some people. Because I had fun playing, I decided to build it out as my submission. From there, I first thought about the different actions a player can do and implemented a WebSocket backend that listened for exactly these actions. Inside the WebSocket, a Controller script also performed these actions in a server-side game instance. After each action, the server sends a message to the clients with the new status of the game. After I had a rough working backend, I started building out a rough Flutter frontend that connected to the WebSocket and listened for the server's messages. Based on these messages, I rebuilt the UI to show the game's current status. Now that I had a working front- and backend, I refined both. Challenges I ran into I encountered multiple challenges along the way: I worked with WebSockets without socket.io for the first time, meaning that I had to implement message handling and rooms on my own It was really hard to work with WebSockets inside of Flutter. For me, it was hard in the beginning, and I had to try multiple different methods. In the end, I created a helper class that holds the servers state and notifies listeners if something changes I implemented and created Animations for the first time. I used Rive for that, but I had huge problems with the rive package inside of Flutter because simple things like starting and stopping an animation weren't clear to me The AI is not as smart as I hoped for. I have tried multiple different Algorithms that I thought of myself but didn't get it to work as well as I wanted it to. Performance of the web app. The main.dart.js file is 1.8MB big, which is too much for initial load time. Sadly, I do not know how to make it more performant, and I will look at that in the future. Accomplishments that I am proud of I am proud of the following things: The game's visuals That you can play together with friends The WebSocket implementation inside of Flutter (because it was really complicated for me) That you can use it in a Browser on your PC or your phone and play together The way I implemented the AI (basically another player that sends events to the server → reuse of logic) What I learned In this hackathon, I learned some general things for my life. First, being persistent in solving a complicated problem is key for a working solution. Second, it is important to validate an idea with something small and easy to create (for me, the paper prototype) if possible. Lastly, planning before building can save a lot of time, but it isn't as fun^^. On the technical side, I learned more about Flutter, NodeJs, and especially how to connect these two with WebSockets! What's next for Slide for Four The next steps for Slide for Four will include creating different game rules (easy, medium, hard) and improving the AI. I think implementing a Pathfinding Algorithm for the AI will solve some issues. Additionally, I will also try to improve the initial load time of the application. <div