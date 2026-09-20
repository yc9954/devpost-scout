---
slug: "saber-punks"
url: "https://devpost.com/software/saber-punks"
title: "Saber Punks"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 808
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
---

# Saber Punks

> Saber Punks is a VR PvP Fighting with projectiles and motion based combos that we are adding Colo AR multiplayer and single player features to. 12 characters and over 150 intuitive combos now w/MR

[Devpost](https://devpost.com/software/saber-punks) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[deterministic_policy]]
  <sub>weak: multi_agent</sub>

**stack** bhaptics, liv, mruk, photon, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for saber punks
- instructions for play

## Body

Colo Multiplayer - Burst shield Slash swarm Colo on a bridge Directional combos Combos trigger unique projectiles Diverse set of weapons and character playstyles 3rd person spectator Aerobic dodging Real world object impacts Ultimate burst with bag collisions/occlusion impacts seen on the left Super move, Samurai Menu Concept Art Key art Inspiration Playing VR rhythm games and envisioning a PvP melee-driven swordfighting combat game where swinging your sword creates a projectile that would land where you would have hit someone standing in front of you. Seeing other games that had passthrough but lacked an interesting combat system inspired us to join the competition. What it does Creates a no-desync combat system with motion at the focus, where skill and speed triumph. Translates melee attacks into projectiles with special properties like spin, stun, and unblockable accessible through our combo system. Now with room-aware colocalized multiplayer passthrough mixed reality and spectator modes. Room scan provides interesting obstacles and cover to the existing combat system. Colocalized multiplayer opens up new realms of social competition for our game. Great for parties where you can pass around the headsets and fight full speed wherever you are without fear of running into walls. This brings a much-needed fun casual component to our competitive PvP combat game. Casual players can enjoy spawning single player bots to fight anywhere and jumping behind couches while slashes pelt the cushions is just so much fun. Spectator mode allows users to record and share content in new ways. Our game is LIV integrated and we know streamers love to insert themselves into the game and this adds a whole new level of content creation that can help accelerate our game visibility. Buttonless Combo give fast action motion-based special attacks that can spin, stun, blow through defenses, and even trigger game-ending super attacks. Precise Angle Defenses blocking can parry on perfectly perpendicular alignments and build up burst shield. Precision blocking prevents overly drawn-out matches. Weapon Variety 24 different weapon types with swords, claws, axes, gunblades and more. Colo AR Room aware combat arenas at home with all the combat tools in the base game Collision surfaces Walls and invisible IK models allow projected decals to provide interactive surfaces for gameplay objects to collide with Demo Reel How we built it Our original gameplay elements were built up over 5 years of careful experimentation and testing. We use Unity with Photon for backbone and the Meta Mixed Reality Utility Kit for colocalized mixed reality passthrough and room aware setup. Challenges we ran into Original Game Getting a global best fit for detecting slashes with colliders and angle calculations, mixing in jabs and blocks can make for a difficult detection space. Colocalization Mixed Reality room materials require deep understanding of render layer ordering for occlusion and collision. Colocalization synchronization can be inconsistent and we could not automate fullly. Players need to confirm that their sync has been established correctly and resync options are still very manual and non-deterministic Accomplishments that we're proud of Adding real-world, fight anywhere experiences to our game is a huge accomplishment Tackling new challenges presented by free motion Leveraging existing IK systems to create invisible player overlays Generating room aware spawns for single player Upgrading multiplayer workflows to accommodate spectator players to watch the action and record content Creating passthrough materials that can take decals so any surface can be projected onto Adding collision to room surfaces. We learned there are interesting combat interactions with obstacles. and will likely bring that up into the main game Our directional combo system which makes dozens of options available without any need for buttons Working with a double platinum rapper for sound track. Studying sword fighting with HEMA, and meeting with a Major League pitcher to learn about curveball physics What we learned Surface meshes and materials for passthrough occlusion and collision had to be created Transparencies are still an issue where background alphas will get overwritten by shaders and create black empty spaces instead of see-through results Balancing pvp when players are restricted by the limitations of the body rather than game animations requires a lot of consideration and adjustment. Making Art and Models for VR has more factors to consider and imposes some additional challenges to find solutions for. What's next for Saber Punks We want to secure funding to finish our character models and environments. Generally, deliver the best experience possible. We want to continue to integrate MR into our project with Improve gameplay adaptation to complex or confined room configurations Incorporate more on surface effects like decals and shaders -Cinematic transition into special attacks Instructions for Play Single Player Launch->Start->Single Player->Versus->Passthrough Checkbox in the bottom right corner of Character Select Multiplayer Colo (2 Quest 3+ Headsets Join on the same network, ~8 feet apart) Launch->Start->Multi Player->Colo Spectator 3rd headset join Colo before end of character select <div