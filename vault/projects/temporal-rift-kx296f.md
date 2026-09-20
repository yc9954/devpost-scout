---
slug: "temporal-rift-kx296f"
url: "https://devpost.com/software/temporal-rift-kx296f"
title: "Temporal Rift"
hackathon: "Hack the North 2020++"
winner: true
words: 691
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Temporal Rift

> Like time travel? In this game you will need to interact with your past and future self to solve the puzzle!

[Devpost](https://devpost.com/software/temporal-rift-kx296f) · hackathon [[Hack the North 2020-]]

## Facets

**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** c++, ubisoftapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that i'm proud of
- what's next for temporal rift
- extra links

## Body

Game Level Design You have 3 lives, and in each life you can see the actions of your past selves! You'll have 20 seconds per life to learn about as much of the level as you can - for a total of 60 seconds! Inspiration As a group of avid puzzle solvers who have a thrilling obsession with smash-like platform games and time-travel movies, we wanted to create a game where it has all the interactive and fun mechanics of super smash bros, but also incorporates sophisticated puzzle components that are simply a blast to solve, and all within the constraints of a 60-second timer. Introducing Temporal Rift, a C++ based puzzle platform game built on the Ubisoft NEST API. Play as an alien exploring a new world, with the power to reverse a limited amount of time and complete the objective. What it does We fully employ the idea of temporal displacement, inspired by movies like Tenet or Groundhog Day - what happens if you could go back in time, but interact with other copies of yourself? We enable players to replay the same segment in time multiple times and then stack them together to orchestrate the completion of the puzzle. Players will need to plan ahead of time to consider how their present actions assist their future goals when being replayed concurrently, or how a future action might allow the present player to reach an objective. To make this even more challenging, we have added built-in enemies that will speed up toward the player when the enemy sees the player, to stop them from finishing their puzzles. Players can shoot bullets in the direction of the cursor to kill enemies or push other copies of the player (sometimes necessary to push the player onto an objective). Last but not least, we have implemented dynamic terrain such that players can open gates or move platforms to reach previously inaccessible places through interacting with the world (buttons/pressure plates, etc.), and different objectives the player should reach to increase the score and beat the level. How we built it Although we have never used Ubisoft’s game engine API, we wanted to challenge ourselves to learn more about game dev and really put our teamwork and technical skills to the test under stress. We added our own components for physics, adding gravity, ground friction, air strafing, and smooth acceleration. (Yes, you can b-hop in this game!) Plus, we implemented mechanics such as ladders, moving platforms, shooting bullets, and recording the player’s movements to replay in the next run, using game entities and components. To improve the user experience, we added different animations for jumping, walking, and standing, as well as grass, rocks, and other foliage on the platforms with different Z-levels to surround the player. Challenges we ran into We ran into multiple issues in the beginning regarding setup across multiple platforms, since within our group, there’s Mac, Linux, and Windows users. However, we quickly resolved this through using a consistent and replicable virtual machine on everyone’s device. Setting up textures and animations took more time than we expected, and managing all the different states of the GameBoard and interactions between entities was challenging. Accomplishments that I'm proud of We are proud that we were able to complete this project within such a short amount of time given that it was our first time using the Ubisoft game engine. Not to mention, the complexity of the in-game mechanics and the many polished UI components were really feats that we are extremely pleased about. What's next for Temporal Rift Our primary next step is to create more levels and figure out a way to implement a tutorial inside the game itself. With that begin said, a few parts of the existing map still need to be tweaked and changed for example optimizing player strafe and movement speeds to make the game feel more responsive. We also didn't have enough time to find the assets for sounds and implement a custom lightning controller into the engine. Extra Links Temporal Rift Intro - https://www.youtube.com/watch?v=yNQ_v63djw8& Winning Run with commentary - https://www.youtube.com/watch?v=eG545QYoYxU Raw Winning Run - https://www.youtube.com/watch?v=klydmUFVRfg <div