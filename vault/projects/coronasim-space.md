---
slug: "coronasim-space"
url: "https://devpost.com/software/coronasim-space"
title: "coronasim.space"
hackathon: "hack:now"
winner: true
words: 379
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "user/general_public"
  - "substrate/web_dom"
---

# coronasim.space

> A realtime multiplayer simulation of coronavirus

[Devpost](https://devpost.com/software/coronasim-space) · hackathon [[hack-now]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**user** [[general_public]]
**substrate** [[web_dom]]

**stack** cloud-dns, colyseus, google-compute-engine, html5, javascript, node.js, p5.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for coronasim.space

## Body

Inspiration Hi! We're a team of incoming freshman at Stanford University. We figure that social distancing isn't fun. Especially when you need to weave your way through the crowd at Costco every few weeks to buy the food your family needs to survive. How do we balance society's needs with our own? It's clear that many people, from schoolchildren to protestors, simply don't understand how COVID-19 transfers and why we need to take precautions. This realtime/multiplayer game/simulation aims to educate and to demonstrate that we're all in this together. What it does This simulation mimics a world dealing with coronavirus. The goal is to stay alive and keep up your health bar. To keep health up, you have to constantly restock on food (essential items). Due to the various strains of coronavirus in the region, you also have to maintain social distancing from other players/computer-spawned player bots because you are at risk of running into someone carrying the virus (you won't know/see if they have the virus or not). If you spread the virus to others, your health also takes a hit since you are destabilizing your environment. Spread the virus to 5 people and your controls will freeze for 5 seconds. As you age over time you are more likely to die from the virus, a mechanism we modeled after real mortality distributions across different age groups. coronasim.space provides some gamification to make learning about coronavirus, and the importance of social distancing, more engaging. How we built it We ran an Apache web server to serve our frontend content and a game server to handle game state and logic all on Google Compute Engine; to hook up our domain to our static IP address we used Cloud DNS. We also set up a VM responsible for creating the game's player bots. We used a framework called Colyseus for networking, which leverages HTTP/WebSockets for automatic state synchronization between server and client. To draw the game we used p5.js and extrinsic HTML/CSS, and the backend was written in TypeScript. What's next for coronasim.space We plan to make the app more scalable, improve the UI/UX, and keep it up and live for the public to enjoy and learn from. Social distancing saves lives! Stay home and play our game instead. <div