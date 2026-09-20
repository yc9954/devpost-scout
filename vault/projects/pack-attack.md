---
slug: "pack-attack"
url: "https://devpost.com/software/pack-attack"
title: "Pack Attack"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 734
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/supply_logistics"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Pack Attack

> A chaotic MR party game! The headset player shouts robot orders to friends playing on their phones. They pack 'em, you launch 'em. A high-speed, cross-device test of communication and shooting skills.

[Devpost](https://devpost.com/software/pack-attack) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[supply_logistics]]
**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** adobe, blender, photoshop, substance-painter, ue5, unreal-engine

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pack attack

## Body

Lobby Parcel Drop Zone MR Post office Window with Delivery Drone Companion App for mobile / desktop players Friends packing parcels End Game Results! Leaderboard Inspiration We’ve always been huge fans of couch co-ops and social games, nothing beats the feeling of screaming instructions at your friends, whether you’re in the same room or on a call. We wanted to capture that frantic, high-stakes energy found in games like Overcooked or Keep Talking and Nobody Explodes , where the gameplay is 10% mechanics and 90% pure communication. The specific theme came from watching the absolute chaos of the holiday season. We started wondering: with Christmas delivery times getting tighter and logistics getting crazier, what is actually happening behind the scenes? And more importantly, what will the chaotic, automated warehouse of the future look like? That’s where the idea for Pack Attack was born. What it does Pack Attack is a cooperative party game that encourages players to work as a single unit. It brings people together by removing the friction of traditional multiplayer setups. The core loop is simple but challenging: you have to manage a futuristic delivery line. The MR player checks what the delivery robots need, tells it to their couch-colleagues who have to pack the order and send it away. The parcel will land in the MR drop zone so the player in the headset can pick it up, drop it into the canon and shoot it towards the correct robot. It encourages constant (and often loud) communication between all participants. It’s designed to be chaotic, but when you finally get into a flow state with your team, that shared sense of triumph is unmatched. How we built it We wanted the game to look stylized and with history, so we started by creating all of the models in Blender and texturing them in Substance Painter to give them that vibrant look. The heavy lifting is done by Unreal Engine 5 , which handles the game logic and environment. To ensure a low barrier to entry, we didn't want players to have to download a companion app. Instead, we built a responsive web interface using React . Players simply join the game via a website on their phones, turning their mobile device into a controller instantly: https://pack-attack.app ! Challenges we ran into The biggest hurdle was definitely the "invisible" stuff: networking and UX. Onboarding: We wanted it to be seamless. Ensuring data was sent instantly between the mobile web client and the headset without lag was tricky. Control Feel & Asymmetry: Designing for asymmetric gameplay on the Quest was a unique challenge. We spent a lot of time iterating on how the MR player interacts with the world versus how the mobile players assist them. The Quest controls needed to feel physical and immersive through actually lifting boxes and firing cannons, while remaining intuitive enough to coordinate with teammates on 2D screens. If the MR mechanics fight the player, the game stops being "fun-chaotic" and just becomes frustrating. Accomplishments that we're proud of We are incredibly proud of the accessibility. The fact that the MR player can allow their friends to join a session with ease, and be playing inside the game session within seconds without installing anything is a huge win for us. Seeing the seamless session setup and reliable performance between a high-fidelity engine like UE5 and a standard mobile browser feels like magic every time it works. What we learned Cross-device communication: We learned a massive amount about WebSockets and optimizing data packets to keep latency low between the website and the main MR game. The art of chaos: We learned that chaos needs to be designed. You can't just throw random things at players; you have to give them tools to solve problems, then slowly turn up the heat. What's next for Pack Attack We have a big roadmap ahead! This simple game loop has potential for a lot of exciting directions: Story Mode: We want to add a single-player, story-driven mode to explore the lore of this futuristic delivery company. More Chaos: We plan to implement events, think machinery breaking down, conveyor belts reversing, or power outages that force players to adapt on the fly. Mobile Depth: We want to give the mobile players more specific, tactile tasks on their screens (like rewiring circuits or stamping packages) to make their role feel even more distinct. <div