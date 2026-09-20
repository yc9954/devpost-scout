---
slug: "world-creation-light-interaction-audio-and-level-design"
url: "https://devpost.com/software/world-creation-light-interaction-audio-and-level-design"
title: "Tutorial - Light, Interaction, Audio and Level Design"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 481
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "user/educator_student"
---

# Tutorial - Light, Interaction, Audio and Level Design

> Details lighting techniques, collider setup for interaction, and audio integration and level design fundamentals.

[Devpost](https://devpost.com/software/world-creation-light-interaction-audio-and-level-design) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**mechanism** [[simulation_digital_twin]]
**user** [[educator_student]]

**stack** github

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tutorial - light, interaction, audio and level design

## Body

Inspiration I wanted to bring together the four questions new Horizon Worlds creators ask most—lighting setups, collider/trigger-based interaction, adding audio, and a basic level-design flow—into one short, practical walkthrough. To do that, I show Environment / Dynamic / Static Light usage, Collider & Trigger Zone behavior, Sound / Sound Recorder settings, and the Worlds Desktop Editor tools step-by-step in a single example. What it does Lighting: Accesses light components from Build > Gizmos, explains Environment _ (sky, fog, exposure, VOIP) _, and walks through Dynamic/Static Light parameters with hands-on examples. Also covers Gen-AI Skybox and Custom Skybox imports. Interaction: Shows how to add Colliders and Trigger Zones, and how to separate behaviors with Collidable and Collision Layers. Audio: Tunes Sound components _ (Volume, Pitch, Global, Min/Max Distance, etc.) _, records with Sound Recorder, and fires sounds via trigger events. Code Samples: Includes DynamicLightController, TriggerLightController, and TriggerSoundController scripts. Level Design 101: Uses Q-W-E-R transforms, Pivot/Transform, Snap tools, view modes, simulation, and builds a Halloween Graveyard from blockout to polish. How we built it I used Meta Horizon World's desktop editor to learn. Then I went through everything and presented it as a tutorial in a way that was as simple, clear, and detailed as possible. Challenges we ran into Performance vs. Dynamic Lights: Too many dynamic lights hurt framerate in VR. We used dynamic lights only for critical moments and static lights for general fill, auditing with Overdraw/Collision views. Trigger Accuracy: Oversized trigger zones caused unintended events. We switched to smaller, purpose-built zones and clarified “Selectable in Screen Mode” where relevant. Audio Balancing: Overlapping loops and hot levels created noise. We layered music/ambience/SFX with distance falloff to keep the mix clean. Collision Setup: Incorrect Collidable or Collision Layer choices led to unwanted interactions. We separated layers clearly and adjusted object scales in Attributes. Accomplishments that we're proud of Three ready-to-use scripts: DynamicLightController, TriggerLightController, TriggerSoundController _ (drop-in, copy-paste friendly) _. End-to-end example flow: From skybox to lighting, colliders/triggers, audio, and testing in the Halloween Graveyard scene. Clear control panels: The most important Environment/Light/Sound variables are summarized and explained in one place. What we learned “Key light + contrast” drives readability; warm/cool tones quickly shape mood. Triggers guide players: flipping lights, opening doors, and firing music reinforce flow. Layered audio _ (music/ambience/SFX) _ with distance-based rolloff greatly improves VR comfort. Editor fundamentals _ (QWER, Snap, Pivot/Transform, View Modes) _ are crucial for fast iteration and tidy scenes. What's next for Tutorial - Light, Interaction, Audio and Level Design Add an Optimization 101 appendix: dynamic/static light budgets, quick health checks with Overdraw/Collision views, and object/simplified-collider counts. Ship prefab packs: Environment/light rigs, trigger–audio–light combos, and example settings _ (packaged versions of the current scripts) _. Advanced interactions: moving platforms, door locks, checkpoints, and sequenced audio/light choreography _ (Audio Complete/CodeBlockEvents) _. VOIP & accessibility notes: deeper Environment VOIP scenarios and comfort options such as adjustable volume/captions. <div