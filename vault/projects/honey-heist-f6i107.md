---
slug: "honey-heist-f6i107"
url: "https://devpost.com/software/honey-heist-f6i107"
title: "Honey Heist"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 742
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "substrate/sensor_telemetry"
---

# Honey Heist

> Master the slingshot and survive the expanding bee swarm in this daily challenge adventure

[Devpost](https://devpost.com/software/honey-heist-f6i107) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]]
**substrate** [[sensor_telemetry]]

**stack** javascript, lensstudio, seedrandomlogic, snapcloudstoragemodule

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i am proud of
- what i learned
- what's next for honey heist

## Body

Home screen with the play button and Daily challenge button Ingame scenes showing bees with different behaviors level, level text, a score system, flowers with a bow in the bottom center ingame scenes showing bees with different behaviors ingame scenes showing bees with different behaviors Win screen Lose screen Inspiration "Honey Heist" was inspired by the classic satisfaction of arcade shooters and the "juicy" game design philosophy where every interaction feels responsive and alive. I wanted to create a casual yet progressively challenging experience that fits perfectly into the Snapchat ecosystem: quick to pick up, but with enough depth to keep players coming back every day. The Longform category particularly appealed to me because I wanted to build a game that grows with the player. What it does "Honey Heist" is an infinite arcade shooter where you defend your garden from waves of stealing bees. Core Loop: Use a tactile drag-to-aim slingshot to snipe bees in the order of their number (From bee 1 to the last bee). Shooting the right bee earns you 10 points and when there're no more bees left in the scene, you win. Shooting the wrong bee takes 10 points away from your score and when your score reaches 0, you lose the game. Progression: The game features infinite levels that get progressively harder, introducing new bee types (from slow green bees to fast red bees, erratic swarmers) as you advance. Daily Challenges: Every day, the game generates a unique, seeded challenge level. This is synchronized globally, so every player faces the exact same "random" swarm configuration for that date, perfect for challenging friends. Persistence: Using Cloud Storage, the game remembers your level and high score, so you never lose progress. Aesthetics: The game features a calming background with subtle leaf particle effects and flowers. The bee and bow assets were custom-made using basic geometric shapes (spheres and cylinders) in Lens Studio. How I built it I built this game using Lens Studio , leveraging its powerful scripting capabilities to create a robust game loop. Core Mechanics: I implemented a custom slingshot physics system using vector math for aiming and launching arrows. The "drag-to-shoot" mechanic was refined through multiple iterations to ensure it felt tactile and precise. System Design: I designed a weighted spawn logic driven by mathematical curves to manage difficulty. A seed-based random number generator was written from scratch in JavaScript to ensure the Daily Challenges are deterministically random across all devices based on the date. Persistence: I integrated Snap's Cloud Storage Module to save complex player states (current level, score, daily completion status) reliably. Challenges we ran into Balancing Difficulty: Tuning the bee spawn rates and movement speeds to be challenging but not unfair was tricky. I solved this by implementing a "Hard Bee Quota" system that ensures difficulty scales predictably, preventing sudden difficulty spikes while still keeping high levels intense. Input Refinement: Initially, the slingshot would fire on simple taps, which was frustrating. I had to rewrite the input logic to specifically detect drag gestures vs taps, ensuring that every shot was deliberate. Visual Clarity: With many bees on screen, they would often clump together. I wrote an algorithm to add randomized offset positions to their target flowers, ensuring the swarm looks natural and individual targets remain distinguishable. Accomplishments that I am proud of The "Juice": Simply popping a bee feels satisfying thanks to the custom particle effects, squishy audio cues, and responsive physics. It just feels good to play. The Daily System: Successfully implementing a seeded random generator that works off the calendar date to create unique daily content was a technical highlight. It turns a single game mechanic into endless content. Seamless State: Getting the Cloud Storage to flawlessly save and load progress so players felt like they were in a persistent world, even in a temporary Lens environment. What I learned This project deepened my understanding of state management in Lens Studio and the importance of user feedback (audio cues, particle effects) in making a game feel more interactive. I also learned how to effectively use Cloud Storage to create persistent, long-term gameplay loops in a transient AR environment. What's next for Honey Heist I plan to expand the "Heist" theme by introducing: Boss Battles: Giant Queen Bees that require multi-stage attacks to defeat. More Weapons: Unlockable slingshot ammo (explosive honeycombs, sticky nets). AR Mode: Bringing the garden into the real world for an even more immersive defense experience. <div