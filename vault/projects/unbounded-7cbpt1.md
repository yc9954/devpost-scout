---
slug: "unbounded-7cbpt1"
url: "https://devpost.com/software/unbounded-7cbpt1"
title: "Unbounded"
hackathon: "Hack the North 2019"
winner: true
words: 520
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Unbounded

> A Non-Euclidean VR Portal Puzzle Game

[Devpost](https://devpost.com/software/unbounded-7cbpt1) · hackathon [[Hack the North 2019]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** c#, graphics, oculus, vr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for unbounded

## Body

Demo of how to fit more than one room within a VR space Demo of how non-euclidean space affects how the world is perceived A "render-concept" of how a non-euclidean world would appear. Inspiration Our inspiration came from the fact that we want to make maximal use of physical play space. Unlike most VR games where the virtual play space feels limited by physical space, we designed our game so that players experience a much larger virtual world through non-Euclidean magics. Ultimately, our goal is to ensure the experience for the player will seem as if there are a near infinite amount of virtual space for them to play. (Tricking their minds :D) What it does The main selling point of our game is our "seamless portals", where you will be able to see into the portal and view what is on the other side. And obviously walk into it as if you were just walking into another room in your current environment. (We had to run a breadth first search to determine which portals gets rendered first) You will definitely have your mind blown (at least very confused) when playing our game. We believe that unexpected, surprising events are what brings excitement and fun into our game. How We built it We built this project on the Unity + Oculus platform. Challenges we ran into Rendering portals, and portals in portals. This required heavy use of depth buffers, stencil buffers and multiple render passes from multiple viewpoints using multiple cameras to achieve the desired effect. One of the reasons why this is difficult because the stencil buffer value you compare with and write must be the same, which makes it very hard to force the portals to render only in their region. We had to work around this issue with bitwise stencil operations. Another challenge was the teleportation of the player when the player enters a portal. It was very difficult to get the teleportation appear near perfect. We actually build multiple customized levels for the game, however, due to problems with depth buffer and rendering order, we had to abandon all of the designed levels. Accomplishments that we're proud of We are proud that we were able to create one of the first non-Euclidean VR games in existence. Experiencing the portals in the game is truly a uniquely mind-blowing experience. What we learned There are two important things that we learned. Firstly, we think we could’ve organized the way we worked on the project better. We basically started two Unity projects and had to merge them when we finish both sides. However, like we said before, integrating the rendering graphics into our designed game levels was not only time consuming but also extremely tedious and difficult. Secondly, of course was the technical aspect of our game. Being all 2nd year students, we have limited graphics knowledge. However, with the help of the internet we were able to pull many graphics tricks off within 36 hours. For this we are very proud. What's next for Unbounded Automatic terrain generation Recursive portal rendering (allowing for infinite tunnels) Multiplayer capabilities <div