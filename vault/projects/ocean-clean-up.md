---
slug: "ocean-clean-up"
url: "https://devpost.com/software/ocean-clean-up"
title: "Ocean Clean-Up"
hackathon: "Snap AR Lensathon 2022"
organization: "Snap Inc."
winner: true
words: 278
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Ocean Clean-Up

> This is a gamified lens I created as a fun and interactive way to spread awareness of the obvious yet very important fact that plastic does not belong in our oceans.

[Devpost](https://devpost.com/software/ocean-clean-up) · hackathon [[Snap AR Lensathon 2022]]

## Facets


**stack** javascript, lensstudio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into

## Body

Inspiration I live in the beautiful City of Cape Town in South Africa. Due to our country being surrounded by the Indian, Atlantic and the Southern Ocean, South Africa has an exceptionally rich marine diversity. Approximately 15% of the world's fish species is found in the South African waters. One of the biggest threats to this diverse marine life is plastic pollution. Over 8 Million tons of plastic is dumped in the world's oceans every year I created this lens as a fun and interactive way to spread awareness of the obvious yet very important fact that plastic does not belong in our oceans. What it does The lens transforms your world into an underwater experience where you are in a small submarine and your goal is to collect as much plastic as possible before the timer runs out. You can collect plastic by aiming the submarine’s zapper at the plastic and pressing the big red button. How we built it Built in Lens Studio. A depth material is used to create the underwater effect. This lens then uses a world mesh to detect surfaces in the real world and spawn coral and fish in your environment. The button in your submarine glows red when it detects that you are in range to collect a plastic object. This is done using a raycast and colliders attached to the plastic objects. Challenges we ran into Optimizing 3D models and textures. Some bugs where materials on scene objects keep disappearing. Surface tracking not very good on some devices. Had to remove the fog material from the underwater effect due to the above problem. Fog was covering the whole screen <div