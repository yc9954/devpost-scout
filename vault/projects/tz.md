---
slug: "tz"
url: "https://devpost.com/software/tz"
title: "Tower Zen"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 641
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/retail_commerce"
  - "substrate/geospatial"
---

# Tower Zen

> Tower Zen is a peaceful multiplayer 2.5D platformer where players climb a mystical tower, light candles, and unlock secrets, featuring soothing visuals and Horizon’s first playable animated character.

[Devpost](https://devpost.com/software/tz) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[retail_commerce]]
**substrate** [[geospatial]]

**stack** audacity, blender, blockade-labs, canva-pro, discord, eleven-labs, gimp, horizon-worlds-desktop-editor, suno-ai, visual-studio

## How they structured the write-up

- 🧠 inspiration
- 💡 what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments we're proud of
- 📚 what we learned
- 🚀 what's next for tower zen

## Body

🧠 Inspiration Sky: Children of the Light Mega Man Donkey Kong Country 💡 What it does Tower Zen is a peaceful multiplayer 2.5D platformer designed for mobile in Horizon Worlds. Players ascend a mystical tower, light candles, and collect shards of light to unlock hidden features on a tranquil island, all while experiencing the first animated character system built for Horizon’s cross-platform ecosystem. 🛠️ How we built it Our two-person team ( Bryan “Not-The-Bake” and Matt “Matthiaos” ) brought 9 years of combined Horizon Worlds experience to the project. Bryan was also a winning team member of the Meta Horizon Worlds Short Loop Mobile Worlds Devpost hackathon. We approached this build with performance, optimization, and platform limitations at the forefront. Built using the desktop editor , with layout and mechanics prototyped in VR Assets modeled and optimized in Blender , textured in GIMP , and UI conceptualized in Canva Pro Code written in Microsoft VS Code , using a fail-early , scalable design with toggleable console logging and test modes Skybox generated with Blockade Labs , refined in GIMP Audio sourced from Suno AI , Eleven Labs , Horizon’s public library , GenAI tools , and mixed in Audacity All VFX sourced from the Horizon Worlds public library Team coordination via Discord We began with a detailed game design doc and prototyped a simple obstacle layout in VR. Since animations weren’t supported for MHCP, we created the first known workaround to give the illusion of replacing the avatar with a fully animated character , while preserving Horizon’s built-in player input system for familiarity. Additional tech features: Per-player mesh visualization , texture swapping , audio , VFX , and dynamic UIs Smooth animations via client scripting and onUpdate subscriptions that auto-disconnect when objects are out of view A low-cost collision map , allowing all meshes to be non-collideable, significantly reducing CPU load for improved performance 🚧 Challenges we ran into ⏳ Time was our biggest challenge. With only 60 days in the competition window, we lost 2 weeks finalizing our team and 1 week for preplanned vacations. We overcame this with a strict production schedule, focused task management, and many long nights (and lots of coffee). 🛠️ Technical hurdles included: A platform bug that broke per-player audio stopping. We reengineered our audio system based on player proximity instead. Texture lighting issues that corrupted visual fidelity. We resolved this using Horizon’s autosave backup feature, though at the cost of several hours of lost work. 🏆 Accomplishments we're proud of We’re especially proud of how two teammates with distinct skillsets came together to deliver a unified, high-performing experience. Key highlights: Multiplayer features like custom nametags and voice chat , enhancing social connection 3D character animation that maintained framerate and responsiveness on mobile A fully failsafe scripting system that never throws runtime errors after first-frame validation Clean hierarchy organization for easy updates and scalability Our proudest accomplishment: creating the first 2.5D animated character platformer built for mobile in Horizon Worlds and also the first of its kind across the entire cross-platform ecosystem, completed in a compressed timeline. 📚 What we learned We learned that Horizon Worlds has very specific limitations, but with clever creativity, many of them can be worked around to achieve ambitious results. This project reinforced that deep platform knowledge, paired with smart problem-solving, can unlock seemingly impossible features. 🚀 What's next for Tower Zen The world was built with expandability and ease of maintenance in mind, allowing future updates without major rework. Planned Features: Player-selectable character models More island unlockables Unlockable character animations (dance, cheer, moonwalk) New towers and expanded movement: wall jumps, ledge grabs, etc. Power-ups to unlock secret areas of the tower Future Goals (with more time): Greater visual detail and polish World streaming to support a library of diverse levels A storefront for customizing player models and textures <div