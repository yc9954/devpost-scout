---
slug: "tutorial-programmatic-fx-management"
url: "https://devpost.com/software/tutorial-programmatic-fx-management"
title: "Tutorial: Programmatic FX Management"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 313
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Tutorial: Programmatic FX Management

> A tutorial focused on performance and maintainability in Horizon Worlds It details a pattern for programmatically managing all SFX and PFX in your world, reducing complexity, maintenance and capacity

[Devpost](https://devpost.com/software/tutorial-programmatic-fx-management) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**mechanism** [[on_device_local]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** markdown

## How they structured the write-up

- inspiration
- what it does
- what went well
- challenges we ran into

## Body

Inspiration When revisiting my first world to tidy it up, I noticed I was well over the world capacity, and a significant amount of this was coming from FX, despite there being almost none playing 99% of the time. This was because every turret, enemy and trap in my world was sitting there with all of the entities they MIGHT need at runtime. I also found that a decision like "I prefer this new sound for a turret being deactivated" meant I had to go and change every turret variation asset and then propagate these updates out into my world. What it does My goal to solve all of this, was to have zero SFX of PFX on ANY of my assets. Hence, the programmatic FX manager was born. All FX used in the world get defined programmatically in a single script, and are assigned a string name. This manager entity then handles spawning these entities at startup, and any other script can just request a required FX, by name, at runtime. What went well This pattern has worked out fantastically for me personally, and is now the first script I bring into any new world. So I'm hopeful that someone else will find a similar benefit from it. Challenges we ran into As the pattern relies on a static map of spawned runtime entities, the RequestFX function can not be called from locally controlled scripts. We can also not use this same pattern on a locally controlled FX Manager, as a locally controlled script can not spawn entities. My workaround personally, has involved a modification of this pattern, where the FX required by local scripts are added as child entities of a LocalFXManager, which references them through properties. This keeps the format for requesting FX consistent on both client and server, but felt too complex to touch on in this tutorial. <div