---
slug: "farm-inc"
url: "https://devpost.com/software/farm-inc"
title: "Farm Inc."
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown - Reloaded"
organization: "Meta"
winner: true
words: 525
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "substrate/video_visual"
---

# Farm Inc.

> Farm Inc is an incremental farming tycoon featuring top down overviews, interactive menus and an instantly rewarding gameplay loop, all taking place in a beautiful valley.

[Devpost](https://devpost.com/software/farm-inc) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown - Reloaded]]

## Facets

**domain** [[agriculture_food]]
**substrate** [[video_visual]]

**stack** biome, typescript

## How they structured the write-up

- our inspiration
- interactivity
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for farm inc

## Body

Main Logo Wide shot looking at all the tycoons Mobile scenic lookout Mobile seed planting overview Our Inspiration We've always loved a mobile game called Egg Inc, it's an incremental chicken farming game on mobile with an overview camera. We wanted to make something similar, while including more interactivity - such as being able to run around in the world and interact with others - as a core part of our gameplay loop. Farming should be a social experience! Interactivity For this game we wanted to have different ways players could interact with the world, whether that be through the overview camera, or in-world to immerse yourself. In Farm Inc, you take on a farm of your own, with a barn, silo and farm plot. You start with a small handful of wheat seeds, from which you progress and grow your farm to have more buildings such as greenhouses and water towers. Some crops even spawn with special modifiers like "Huge" or "Seedy"! How we built it We were immediately interested in the focused UI and overlay modes of Custom UI's, which is what we centered the gameplay design around. We needed to ensure all UIs worked seamlessly with 4 players, with rigorous testing on gameplay mechanics and carefully balancing performance with animation. Challenges we ran into Server performance was always a big issue for us. A lot of the visual effects we strived for were significantly harder to implement due to the constraints of the binding update limits or other RPCs. The performance tips on the CPU and TypeScript optimization and best practices page helped significantly, but we'd love some additional bandwidth or client-side updating capabilities where possible to make things more reactive. Accomplishments that we're proud of We're super proud of the overview system, being able to tap to plant crops from a camera and then find yourself immersed in the environment from the ground really brings the experience together. We love being able to watch your farm grow as you progress and see new buildings and decorations pop up at your friends bases as well! We're also proud of the incredible environment, making you feel like you're there in that beautiful golden hour valley. What we learned I feel that we both have learnt a lot from this project. We came in with a fresh perspective after getting the privilege to learn from the creator academy and in just one month we've made an incredible game that is really quite fun! What's next for Farm Inc The main thing we want to do is continue to expand on the current tycoon and it's framework, adding more content like crop types, more modifiers, more ways to interact and a lot more tiers to the barn. Additionally we plan to add leaderboard rewards, like crowns that the top 3 weekly players can redeem and wear in game. Last there are further performance optimizations we hope to make. We spent the last few days of the project making sure Farm Inc is as performant as it could be as the project grew and plan to optimize the UI to better handle larger data sets. <div