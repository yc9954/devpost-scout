---
slug: "null-s-flight-pack"
url: "https://devpost.com/software/null-s-flight-pack"
title: "Null's Flight Pack"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 290
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
---

# Null's Flight Pack

> Created an asset for a modular flight system that can be swapped for any vehicle body and it's corresponding vehicle ability including weapons. It can also be used as a ground or water vehicle.

[Devpost](https://devpost.com/software/null-s-flight-pack) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**domain** [[transportation]]

**stack** horizonworlds, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for null's flight pack

## Body

Icon in public asset folder. Inspiration Horizon World has had a lack of vehicle gameplay and I wanted to create an asset that would expand the possibilities of the types of games that can be made. What it does It's a flight (or ground) system that creates the framework for vehicles and their abilities. It's completely modular and can be quickly and easily swapped with other parts for easy prototyping. How we built it It looks simple with 3 basic assets; a controller that is held, a grouped AvatarPose, and lots of scripting. Modifications are done by attaching scripts to the vehicle body and parts and placing them in the group. Events are then sent from the controller. Challenges we ran into The hardest part was making it all run smoothly. And making it work on cross screen.. Lots of code optimization. The assets were also published before the deadline, but the DevPost portion didn't go through. Accomplishments that we're proud of As far as I know, this is the first full flight system apart from my first CodeBlock based racing world which isn't cross screen friendly. What we learned I had to learn about other methods of player input. The code makes use of the PlayerInput code to increase the number of controls. For instance, the player will use "jump" to activate the thrust in cross screen. What's next for Null's Flight Pack I'm hoping that it becomes popular enough that people will ask for other features that I can add in. I'm also hoping someday to get more access to the code that would let me disable player motion and keep people from accidentally running out of the vehicle. (Helps with people that might have stick drift.) <div