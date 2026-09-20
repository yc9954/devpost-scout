---
slug: "super-car"
url: "https://devpost.com/software/super-car"
title: "Super Car"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 235
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/simulation_digital_twin"
  - "domain/transportation"
  - "user/frontline_worker"
---

# Super Car

> Enjoy this super vehicle in your world. There is a custom mobile control and a custom vr control for best experience.

[Devpost](https://devpost.com/software/super-car) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**mechanism** [[measured_ablation]] [[simulation_digital_twin]]
**domain** [[transportation]]
**user** [[frontline_worker]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

Inspiration I have tried different vehicles in horizon worlds. I noticed that either they get the VR right or mobile but not both. I decided to make something for both worlds. What it does Super Car is a full customizable vehicle you can just drop in your world and go. You can a custom VR control and also a custom mobile control. You can customize the vehicle engine, mass, brake and lots more. Players can enter the driver seat or even the passenger seat. The game engine sound accurately simulates your speed and when the car changes gears. There are lots more to love about Super Car. How we built it I built the controllers to be separate from the Car. VR control runs better when controller the Car in server side while mobile control runs best on local. Having a separate controller makes it easy to switch ownership of the car for mobile players and maintain ownership in server for VR players. The code is well documented for users that want to change some settings or code. Challenges we ran into The main challenge is controlling the same vehicle from local and server. I have to separate events and functionalities for when each type of player takes control. Accomplishments that we're proud of I like how the car drives like a real world car with engine sounds, brake sounds, reverse and crashes :) <div