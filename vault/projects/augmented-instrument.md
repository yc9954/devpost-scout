---
slug: "augmented-instrument"
url: "https://devpost.com/software/augmented-instrument"
title: "World Ensemble"
hackathon: "Google’s Immersive Geospatial Challenge"
organization: "Google"
winner: true
words: 302
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/geospatial"
---

# World Ensemble

> Tap buildings to place instruments in the AR world. Tap the sky to switch the audio and visual effects. Walk around to change the beat.

[Devpost](https://devpost.com/software/augmented-instrument) · hackathon [[Google-s Immersive Geospatial Challenge]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[geospatial]]

**stack** geospatial, photorealistic-3d-tiles, streetscape-geometry, unity

## How they structured the write-up

- what it does
- how we built it
- about sound
- challenges we encountered
- what's next for world ensemble

## Body

GIF Photorealistic 3D Tiles to AR GIF Visual Effects Unity Editor Simulator What it does "World Ensemble" is an audio-visual app that positions sound objects in 3D, creating an immersive audio-visual experience. How we built it To spatially locate the sound, we utilized Streetscape geometry to define building shapes and determine the sky area on the screen. We also incorporated Photorealistic 3D Tiles to achieve seamless transitions between the virtual aerial view and the AR view. We had some difficulty when attempting to match the GPS coordinates in the 3D Tiles with the geospatial pose in ARCore. About sound We developed specific musical rules tailored for the AR experience. The sounds are placed in a 3D environment, and their panning and volume automatically adjust as you move around. We implemented a dynamic rule that shifts the 16-step sequencer by one step every 2 meters, which alters the beat as you progress. Although the in-app sequencer quantizes notes 16th-note, there is a distance-based delay based on the speed of sound. A sound located 340 meters away arrives with a one-second delay. Challenges we encountered Quick iterations played a crucial role in developing this audio-visual effect app. We needed to fine-tune numerous parameters while working in the Unity Editor, rather than the built app. Consequently, we created an AR recording/replaying system to simulate the Geospatial AR within the Unity Editor, allowing us to make adjustments in an environment nearly identical to the actual app. What's next for World Ensemble Initially, our idea was to enable AR music playing by connecting a Bluetooth MIDI Controller to control music playback and visual effects. However, due to technical difficulties, we shifted our focus to interactions involving tapping on the screen. After taking a short break, we plan to implement the functionality to connect the MIDI Controller. <div