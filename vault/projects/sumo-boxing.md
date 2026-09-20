---
slug: "sumo-boxing"
url: "https://devpost.com/software/sumo-boxing"
title: "Final Throwdown"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 696
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "substrate/geospatial"
---

# Final Throwdown

> Become the bot and throwdown your friends in our high-energy, hilarious, colocated Mixed Reality game. Perfect for releasing tension at your next family gathering or for resolving workplace disputes.

[Devpost](https://devpost.com/software/sumo-boxing) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[on_device_local]] [[simulation_digital_twin]]
**domain** [[developer_tools]]
**substrate** [[geospatial]]

**stack** c#, interactionapi, mruk, netcodeforgameobjects, presenceplatform, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we solved
- accomplishments
- what we learned
- what’s next

## Body

Final Throwdown — A New Mixed Reality Minigame for Game Night UPDATED BUILD: All non-competition content has been removed from the submission build other than the game setup and scores scenes. Final Throwdown is completely new. Inspiration Final Throwdown was built within Game Night , our 1-4 player, co-located multiplayer Mixed Reality party game. Our mission is to showcase what makes MR magical in a family-friendly, deeply social and intuitive-for-all experience. Final Throwdown was inspired by the punch mechanic, which one of the most fun things you can do with hand tracking. We took this a step further with finger tracking to enable players to punch, slap and finger gun their way to victory. Boxing is a popular genre on Quest, we wanted to show how MR and face-to-face colocated play offers the best social experience while remaining safe. What It Does Players embody playful robot avatars whose fists map 1:1 to their real-world hand movements. The goal is simply to punch all adversaries (other players and the boss) off the arena to score points. Bonus rings positioned around the arena reward precision knockouts. For new players, it’s a chaotic, hilarious competitive free-for-all. For advanced players, it’s a mastery challenge of aiming punches to maximize points. In co-op, everyone works together to punch the boss off the platform first, earning group-wide bonuses. Rounds are short, high-intensity, and physics-driven, encouraging players to squeeze in as many knockouts as possible before time runs out. How We Built It Final Throwdown was built inside our existing Game Night infrastructure, using Unity and the Meta Presence Platform SDK for hand-tracking, physics, and co-located multiplayer support. We ran a public playtest at a local library to gather non-XR players feedback and launched a beta to our Fantail Games Discord community for expert testing and iterative feedback. Challenges We Solved 1. Core Gameplay We wanted to support single player and co-op gameplay in addition to versus to suit every social group. Our early attempts confused players, they didn't understand scoring and wanted to be able to move their avatar. We toyed with movement but adding an extra mechanic complicates gameplay and makes it less intuitive. The central boss's behavior was redesigned to attack from the sides, keeping all players within reach and removing the need for locomotion. This resulted in faster play allowing us to remove the respawn as a “ghost” feature we’d added to prevent players from having too much downtime after knockout. We reinforced scoring communication through clearer textures, effects, animations, and sound cues. 2. Responsiveness As your actual hands are mapped to the player it must feel responsive with zero network latency. The full physics simulation is run locally on each headset rather than via the host. Hits are replicated over the network, with periodic sync checks to keep all clients aligned without disrupting responsiveness. We added a robotic feel to the finger mapping so that players can punch, slap or perform gestures greatly increasing immersion and comedy. 3. Safety Players are guided into safe, evenly spaced positions during setup; moving during gameplay triggers a warning. The arena automatically scales and positions itself according to available space. This allows for gigantic showdowns! 4. Accessibility Arena height adapts to the shortest player (lowest headset), enabling seated play. Arm reach is normalized so every player, adult or child, has equal in-game range keeping it fair. Accomplishments Playtesters consistently tell us Final Throwdown is their favorite Game Night minigame yet. Sessions often end with participants laughing, breathless, and eager for a rematch. Stretching before play is recommended! What We Learned We continue to learn that MR is not a gimmick, and that face-to-face play offers the best social gameplay available. Playtesting proved critical: rather than adding complexity (locomotion), we identified why players felt the need to move and redesigned the experience to solve the root problem. What’s Next Further balancing and effects polishing Ambisonic music and improved SFX Co-op and competitive achievements with cosmetic hat rewards New NPC challengers Fan-requested features: blocking, attack variants, uppercuts, more customization Online multiplayer support It’s the final countdown for December 16 when we throwdown the Final Showdown as a free addition to Game Night . <div