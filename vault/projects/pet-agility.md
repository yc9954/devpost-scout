---
slug: "pet-agility"
url: "https://devpost.com/software/pet-agility"
title: "Pet Agility"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 429
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
---

# Pet Agility

> Pick a cute pet and guide it round the obsticle course in the quickest time.

[Devpost](https://devpost.com/software/pet-agility) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**mechanism** [[deterministic_policy]]
  <sub>weak: video_visual</sub>

**stack** blender, metaai, photoshopcs5

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pet agility

## Body

jump through rings guide your pet over a seasaw get ur cute pet to the finish line logo hero image This is my first solo meta horizon world. I attended the bootcamp in NY and watched to submit somthing to this contest. Inspiration At first i wanted to make a pokemon clone but limited my scope when i had a simple pet following and it was fun and then thought of those pet agility courses and thought it was achievable in this scope. What it does Pick a pet and guide it through a course in the fastest time. It has a pet that animates and follows you around. This is customizable to different pets and sizes of pets. There are a few obstickle assets to reuse in remixes too like rings, slalum posts, tunnels saesaw , planks and boxes. I think this is a good starting point to make pet agility courses based on this. We have a simple checkpoint and time system too. Also has s simple script to scale down the grass tufts when the pet walks over them. How we built it I built the pet parts and world assets in blender to keep them optomised then set up empties in horizon to attach them to so we could animat them through code. I had a long chat with the meta code ai tool and slowly built up the animations and simple state machine. Challenges we ran into I was initially gonna add some fetch and pokeball catching type mechanics but the horizon throw mechanic is a but fiddly and inconsistent. Plus when i throw a ball at the pet it breaks the physics and crashes the editor so i ignored that for now. Accomplishments that we're proud of I'm really happy with how the modular code based animation and simple follow script works to bring the pet alive. What we learned I learned a few quirks of the engine like u cant hide an object but have its children visible so had to use placer objects and make others track to them rather than be children at times. What's next for Pet Agility I wanna add proper scoreboards but thought it was unease to expose potentially backend codes in a remixable world. I also wanna add more courses and some pet training stuff to make your pet more or less obedient. Also dono how to make multiple people have multiple pets in the world yet , that would be nice. I see people using and expanding on the pet asset in their worlds. <div