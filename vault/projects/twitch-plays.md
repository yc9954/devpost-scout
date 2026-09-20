---
slug: "twitch-plays"
url: "https://devpost.com/software/twitch-plays"
title: "Twitch Plays Tetris"
hackathon: "MLH Local Hack Day (2018)"
winner: true
words: 283
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
---

# Twitch Plays Tetris

> Tetris, controllable directly from Twitch Chat

[Devpost](https://devpost.com/software/twitch-plays) · hackathon [[MLH Local Hack Day -2018-]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
  <sub>weak: web_dom</sub>

**stack** css, html, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for twitch plays tetris

## Body

Inspiration In the past, concepts such as "Twitch Plays Pokémon" have become rather popular, and so I decided to try to make my own version of a "Twitch Plays" game. What it does Players type commands such as "l" and "r" in to chat, and those directly control the game of Tetris shown on the stream. The game is also controllable via the arrow keys and the "c" key, if the game is opened directly in a browser. How I built it An Azure VM runs two scripts, one of which connects to the Twitch Chat via IRC, and the other runs a websocket server. When a valid command is entered into Twitch Chat, it is forwarded on to the websocket server. The websocket server simply broadcasts any message it receives to everything it is connected to. Then, the game (running locally on the user's computer) connects to the websocket server and listens for commands. Otherwise, the game runs as a normal(ish) game of Tetris. Challenges I ran into My university's network blocked the ports required to interface with the IRC server, so I decided to host the IRC script and the websocket server on an Azure VM. Otherwise, there were difficulties trying to make the pieces properly render and collide with obstacles. Accomplishments that I'm proud of I'm proud that I was able to write a functioning game of Tetris in Javascript within the time limit. What I learned Games are fun to play, but difficult to write! What's next for Twitch Plays Tetris It would be possible to expand this system to work with other games, and potentially with ones that already run in a browser (via imitating key presses?) <div