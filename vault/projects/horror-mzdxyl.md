---
slug: "horror-mzdxyl"
url: "https://devpost.com/software/horror-mzdxyl"
title: "The House of Jeff"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 741
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/educator_student"
  - "substrate/geospatial"
---

# The House of Jeff

> Survive the delusional hospitality of an AI-powered killer who reacts to your voice and actions in this immersive horror survival.

[Devpost](https://devpost.com/software/horror-mzdxyl) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[educator_student]]
**substrate** [[geospatial]]
  <sub>weak: video_visual</sub>

**stack** genai, horizon, llm, meta, navmesh, typescript

## How they structured the write-up

- what it does
- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the house of jeff

## Body

Promotional artwork for the game Game mechanics are explained in the spawn room Entry hall with the exit door Hide from Jeff or run as soon as he notices you. A special chase music will start when he’s after you Find hidden keys to escape the house World Broadcast camera: Watch Jeff live as he hunts down other players Top-down view Jeff spots the player as he discovers a key We included AI video in the trailer to give a distinctive look WorldID: 808103559063266 What it does The House of Jeff is an immersive psychological horror survival game where players find themselves as "guests" (captives) in the mansion of a delusional host named Jeff. The objective is deceptively simple: locate hidden keys to unlock the front door and escape. However, Jeff is constantly roaming the halls. He is polite, obsessive, and lethal. The game leverages advanced stealth mechanics, real-time audio reactivity, and a complex AI antagonist to create a suffocatingly tense atmosphere where every footstep counts. Inspiration We were inspired by psychological horror tropes, specifically the concept of the "unreliable narrator" and the "polite villain." Instead of a mindless monster, we wanted to subvert expectations with an antagonist who speaks to you elegantly, claims to love you, and views your escape attempts not as survival, but as rude insults to his hospitality. How we built it We developed a sophisticated custom AI state machine for Jeff that governs his Patrol, Search, and Chase behaviors with high fidelity. AI Logic: Jeff navigates using a NavMesh with randomized patrol points to ensure unpredictability. We implemented a rigorous Line-of-Sight system : Jeff doesn't just magically know your location; he must visually confirm you before initiating a chase. If you break his line of sight, the AI switches to a "Search" state, meticulously investigating the last location you were seen. Audio Reactivity & LLM Integration: We utilized LLM NPCs to revolutionize immersion. Players can speak directly to the killer via their microphone, and the game logic processes this input. By leveraging NpcConversation.setDynamicContext and addEventPerception , we feed real-time game state data to the AI. Jeff dynamically perceives and reacts to specific player actions—such as sniffing around corners, rattling the locked front door, or picking up his keys. The LLM then generates unique, context-aware dialogue that is polite yet terrifying, creating an "uncanny valley" personality impossible to achieve with static scripting. GenAI Assets: The visual model for Jeff was conceptualized and generated using GenAI tools to achieve his distinct look. Challenges we ran into One significant technical hurdle was the AI navigation; Jeff would occasionally get stuck on complex NavMesh corners or geometry. To solve this, we implemented a custom "stuck-agent detection routine" that periodically checks if the agent's velocity is zero while in a moving state. If detected, the script smoothly resets his position to the nearest valid NavMesh point, ensuring the gameplay loop remains unbroken. Accomplishments that we're proud of We believe we have created one of the most interactive and technically advanced horror NPCs on the platform. Memorable NPC Behavior: Jeff is fully context-aware. His reactions are dynamic rather than canned—he will scold you for "rudeness" if you try the locked door, or become visibly agitated and possessive if you touch his keys, making him feel like a living entity. Best Potential World Broadcast Implementation: We built a custom "Spectator Cam" system. Even without playing, users can watch a live feed that intelligently tracks the killer as he hunts down players. This provides a cinematic "slasher movie" perspective for the audience, transforming the game into a watchable event. New User Onboarding Experience: We replaced traditional tutorials with narrative cues. Jeff’s generated dialogue provides subconscious hints (e.g., complaining about guests trying to leave), guiding players to find keys without breaking immersion. Microphone Interaction: We are particularly proud of the voice input integration. Players can plead with Jeff or taunt him, and the LLM processes these sentiments to generate appropriate, terrifying responses in real-time. What we learned We gained significant expertise in Prompt Engineering and State Management for LLM NPCs. We learned how to bridge the gap between hard-coded game events (triggers) and fluid AI conversation to create a cohesive narrative experience. What's next for The House of Jeff We plan to expand the manor with a fully realized basement level and implement new "punishment" mechanics if Jeff catches you. We also aim to add branching escape routes and multiple exits to increase replayability. <div