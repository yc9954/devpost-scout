---
slug: "gametogether"
url: "https://devpost.com/software/gametogether"
title: "GameTogether"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 272
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
---

# GameTogether

> An app that allows any web based game to be played together as a multiplayer game in a group video call.

[Devpost](https://devpost.com/software/gametogether) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**substrate** [[video_visual]]

**stack** node.js, react, webrtc

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for gametogether

## Body

Once i choose a game i'm taken to a 'Game room' I've shared the link with Sunny who is able to join and now we can play together. Game selection screen Inspiration I really wanted to be able to play simple online games with my dad, but also share our video feeds with each other at the same time. I couldn't find a way to do this simply. With this app i can just share a link with my dad and we can hangout in a video call and play games together. What it does It loads html5 canvas based games in an iframe and streams them using webRTC, as well as streaming a video feed, keyboard stroked and mouse position and clicks, allowing everyone in the call to see each other and play games together How I built it Built using reactjs on the front-end and nodejs on the backend. Challenges I ran into Handling more than two people on the call at one time is challenging. Trying to keep bandwidth usage to a minimum is also challenging. Accomplishments that I'm proud of I'm proud of potentially breathing new life into many online web games. I'm proud of the fact that by just sharing a link and play games and hangout with people at the same time. What I learned Learned a lot about webRTC which i hadn't had much direct interaction with before, it's a very cool technolgoy! What's next for GameTogether Polish and allow for different rooms to be created. Add more games, and work on making a room with more than two people in it more robust. <div