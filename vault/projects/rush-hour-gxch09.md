---
slug: "rush-hour-gxch09"
url: "https://devpost.com/software/rush-hour-gxch09"
title: "Rush Hour"
hackathon: "Snap AR Lensathon 2022"
organization: "Snap Inc."
winner: true
words: 696
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/transportation"
  - "substrate/video_visual"
---

# Rush Hour

> Your daily commute in AR! Room-scale Arcade Game in Snapchat.

[Devpost](https://devpost.com/software/rush-hour-gxch09) · hackathon [[Snap AR Lensathon 2022]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[transportation]]
**substrate** [[video_visual]]

**stack** ar, javascript, lens, lens-studio, snap

## How they structured the write-up

- rush hour
- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned and what’s next
- software
- resources

## Body

Rush Hour Snapchat Lens Rush Hour is a Room-Scale AR Arcade Game, that’s fast, fun and full of animations that react to the room around you. It entices players to quickly dip and dive around the room, but still strategize their next quick move. The better you get; the longer you play; the more you score! Inspiration Rush Hour is inspired by the dreaded daily commute. For myself, remote work has changed how much time I spend on the road, but I definitely don’t miss fighting traffic or guzzling gas. Whether you still have to hit the pavement, or just walk to your desk in the next room, I hope this game helps you stand up, get out of your chair, and provides a small stretch break for that best score. What it does Rush Hour begins on the Selfie Camera by introducing the main elements of the game: The Flying Car, Monster, Gas Can, and Asteroids. Highly dynamic animations are driven by physics based motion and react to both user input and surrounding physical environment. When users switch to the Back Camera, a World Mesh scene creates a play area and VR-style guardians. Snapchatters can move about the room for a true room-scale experience. Users shoot as many Asteroids as they can, while they still have fuel. When users shoot the Monster, it spits out a Gas Can which can be collected for additional playtime. When fuel runs out, the game ends with a scoreboard that also displays your best score, and the opportunity to replay. How I built it Snap Lens Studio provides extensive gaming features along with many integrated AR Camera API Libraries. The built-in physics engine and frame-based logic allows for precise control to initiate animations, or transition between physics bodies and graphed transforms, for an extremely dynamic experience. World Mesh features allow for a highly-tuned play area, with a guardian that dynamically scales based on the user distance from the play area center. This allows for both physics and screen space normals that make elements appear to interact with your physical room. There are several Physics World Settings with Physics Bodies that are synchronized to SceneObjects. Transforms are coordinated to a customized physics world origin, and occasionally LERP to static transforms when needed. Dynamic Force and Torque are applied, with many different Collision Detections that trigger interactions. Custom Materials and Depth Texture VFX provide a rich experience that fills the entire room. This is further enhanced with Depth Materials and Post techniques, that casts a galaxy onto the walls with a mystic glow. The final touch is a completely custom Music Track and sci-fi SFX. Challenges I ran into This lens heavily uses the Physics API. Snap is the only Social AR platform to provide this level of physics integration. It truly allows us to make a native-like gaming experience. Controlling transforms and animations was one of the most difficult tasks. Following are a few Physics API feature requests that may have helped ease development: Ability to dynamically change the World Origin of the physics World setting. This would allow devs to move the play area around while keeping a localized origin. The workaround currently in place requires that there is a separate physics SceneObject at the root of the scene, that then synchronizes on frame update to another parent, with its own local transform. This same issue arises for physics games that are anchored to Marker Tech. Option for individual collision groups. This would assist with having only certain bodies colliding with each other. Built-in functions that apply force or rotation in relative ways to other objects. For example, attraction forces or face towards torques. What I learned and what’s next I learned a ton on this project and it continues to enhance my knowledge of Lens Studio physics-based techniques. I’m excited to continue building on this room-scale AR architecture, as there are many opportunities to continue using several of the techniques related to World Mesh, Depth, and Physics. I also hope to port this lens into Spectacles as well as include multiplayer through the Connected Lens API. Software Snap Lens Studio v4.22.1 Resources Snapcode: https://lens.snapchat.com/63feb65436a3477496f254dfff9074d4 Demo Video: https://youtu.be/8ZLi0l0inhs <div