---
slug: "don-t-kill-the-fish"
url: "https://devpost.com/software/don-t-kill-the-fish"
title: "Don't Kill The Fish"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 559
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
---

# Don't Kill The Fish

> A high-stakes, community-run permadeath fish tank. All of Reddit collaborates to keep fish alive, hit goals, and win rewards. But if all the fish die, all progress is permanently lost

[Devpost](https://devpost.com/software/don-t-kill-the-fish) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]

**stack** pixijs, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges i ran into
- accomplishments that we're proud of
- what's next for don't kill the fish

## Body

Inspiration I was looking for a community game concept that was both fun to play and simple to develop. The idea of a community-run fish tank came to mind, and I realized it would be a perfect fit for a collaborative platform like Reddit. I hope it's fun because it wasn't that simple to develop 😂 What it does It's a high-stakes, community-run permadeath fish tank. The entire Reddit community collaborates to keep a population of virtual fish alive while completes goals that give prizes to decorate the fish tank. But if the community fails and the last fish dies, all progress is permanently lost. The tank resets. The top contributors from each "cycle" are immortalized with a permanent statue , creating a lasting legacy. How we built it My strategy was rapid iteration using AI. I used Kiro to bootstrap the initial game logic, then switched to Cursor for its 'tab' that I'm more used to use and allowed me to work faster and be more precise. Kiro is superior to Cursor in terms of planning a feature and having an agent to develop whats planned but normally it doesn't take the output I want both in terms of architecture and UI and I need to take more time teaking and understanding what was generated. So my approach is to develop small features or small iterations and tweak things till I get what I initially inteded. I was very happy with this workflow using Kiro for bigger tasks and Cursor, especially tab feature to tweak and fixes. Game Engine: I chose PixiJS for its high-performance 2D web rendering, making the tank accessible to anyone with a browser. Community Integration: I connected directly to the Reddit Realtime API to pull in user commands. Game State Logic: The game state is loaded and stored on every user action in Redis. To keep the simulation alive 24/7, even when no one is playing, a scheduled trigger runs every minute to update the tank's health and environment. Challenges I ran into One of my biggest technical hurdle was the Reddit Realtime API . I were expecting a full socket API for bi-directional messaging, but its limitations made true real-time synchronization difficult. This meant the game state could occasionally be slightly out of sync, but we accepted this as part of the chaotic charm. The other major challenge was balancing chaos and order. To prevent trolls from instantly killing the tank, we built a democratic input system where the community must vote on critical actions, turning potential anarchy into structured collaboration. To be honest I'm still working the latter Accomplishments that we're proud of I’am incredibly proud of creating a new genre: the social rogue-like. I've successfully built a game where every single action, taken by anyone on Reddit, has permanent consequences. My biggest accomplishment is the statue' incentive. It’s a powerful hook that solves the "why should I care?" problem. It gives players a real stake in the game—a way to achieve a permanent legacy that survives the permadeath reset, which will keep them coming back. What's next for Don't Kill The Fish Rankings - Adding points so user can track how they are compared with other Special events - Like a predator fish enters the tank and users need to destroy it before it eats the other fishes Improve animations <div