---
slug: "sector_07"
url: "https://devpost.com/software/sector_07"
title: "SECTOR_07"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 451
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/sensor_telemetry"
---

# SECTOR_07

> Imagine being trapped inside a dying computer from 1988. The sky is black, the road is glowing, and the only thing standing between the system and a total crash is you and your pixel gun.

[Devpost](https://devpost.com/software/sector_07) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[sensor_telemetry]]

**stack** blender, javascript, lens-studio

## How they structured the write-up

- the story
- what inspired me
- how i built it
- challenges i faced
- future vision

## Body

SECTOR_07 The Story Imagine being trapped inside a dying computer from the 80s. The sky is black, the road is glowing, and the only thing standing between the system and a total crash is you and your pixel gun. You are the System Cleaner, the final line of defense in a collapsing simulation. As the sector attempts a critical reboot, corrupted data vans, rush the bridge to deliver a fatal payload. With your pixel gun in hand, you must protect the core. Every van that leaks past you disrupts the system's progress. If the reboot hits 0%, the simulation dissolves into static forever. What Inspired Me My journey into 3D initially didn't start with the "Blender Donut." Instead, I was attracted by the neon world of Ducky3D's 80s-inspired loop animations. I wanted to take that style and blend it with the high-stakes of The Matrix. I moved away from the points and focused on "System Stability" making it into a battle for survival where everything you see is made of fragile code. How I Built It This project was developed at Tommy ( thisistommy.com ). 3D Modelling (Blender): I used Blender to model the entire "universe". To ensure the experience was optimised for mobile AR, I focused on chunky, geometric shapes. Lens Studio & Logic: I used javascript to handle all the core game logics: global "Reboot Percentage", collision detection, enemy spawning and reset functionality. Accessibility via Joystick: For better precision, I implemented a joystick-controlled aiming system rather than gyro so the game can be played in any environment. Asset Optimisation: Since lenses must perform across a wide range of mobile devices, I opted for a limited, high-contrast palette (Blue, Pink, Green, and Black). This turned technical polygon limits into a deliberate stylistic choice. Additionally, I utilised custom shaders instead of heavy animated textures to reduce project size and loading time. The Character (Bitmoji + Mixamo): To create a more personalized experience and better integrate into the Snapchat ecosystem, I've used the Bitmoji character and animated it using Mixamo. Challenges I Faced Mobile Performance: Keeping a high frame rate with a character controller, multiple vans, and particle effects required mesh-joining in Blender and careful texture management. The "Feel" of the Shotgun: Without physical feedback, making a screen-tap feel heavy was difficult. I solved this by adding a custom particle system to provide instant visual feedback. Future Vision This project is just the beginning. In the future, I plan to evolve this experience into a story-driven series of mini-games, where players navigate deeper into the system to clear different types of hardware corruption and restore the digital world one sector at a time. [SYSTEM STATUS: READY FOR REBOOT] [DEVELOPED @ TOMMY] <div