---
slug: "pocket-lands"
url: "https://devpost.com/software/pocket-lands"
title: "Pocket Lands"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 408
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/sensor_telemetry"
---

# Pocket Lands

> Open a diorama the size of your lap to the whole living room floor and shape a voxel world directly with your hands. Or, drop in and immerse yourself fully in the lands waiting to be explored.

[Devpost](https://devpost.com/software/pocket-lands) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[sensor_telemetry]]

**stack** c#, meta-sdk, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pocket lands

## Body

Immersed diorama view Immersed diorama at sunset Passthrough diorama view First person VR view Tabletop MR diorama Inspiration One of my defining "wow" moments in XR was the E3 2015 HoloLens 1 demo showing Minecraft in a holographic diorama. It left a lasting impression on me, and I'm sure on many others in the industry as well. Unfortunately it remained a one off for E3 and never actually saw the light of day. With mixed reality and hand tracking improving significantly since then, I figured it was time to do the concept justice. What it does Pocket Lands is a voxel sandbox with a unique visual style that can be played as a volumetric diorama in passthrough or fully immersed in the world, as well as in first person VR. The diorama mode is designed around hand tracking, though controllers are also supported. How we built it The voxel engine was built over the past year, but only in the month of the hackathon did it really become a full game. All application code and assets except for audio were produced by me, without the use of AI. Challenges we ran into Designing for intent when using hand tracking. For instance, I wanted the catalog to be accessible with both raycasting and directly grabbing blocks from it, while also using pinches to grab and place blocks in the world. This creates a conflict when the catalog is in front of the user, as the raycasts have to take precedence over grabbing the world, considering the entire world is interactable. In this case, I solved this by automatically disabling the raycast if the hand's pinch point is close to blocks in the world, so that no conflict arises and it "just works" for the player. Accomplishments that we're proud of The large diorama size in passthrough running at smooth frame rate, at 90 FPS depending on scene complexity. What we learned Going from tech demo to game as a solo developer in one month is one hell of a crunch! I worked every single day of the hackathon from 6 am to often 9pm or 2 am. What's next for Pocket Lands Pocket Lands releases in early access on December 11th as a creative sandbox. After launch it will first get additional polish such as more blocks and biomes, and for the full release in the second half of 2026 it will feature creative multiplayer with build battles. <div