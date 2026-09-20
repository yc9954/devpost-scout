---
slug: "pixel-truth"
url: "https://devpost.com/software/pixel-truth"
title: "Pixel Truth"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1093
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/media_journalism"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Pixel Truth

> Play as a detective at the Netropolis Truth Bureau - examine suspicious news posts, interview witnesses, and use your detective tools to expose or verify the truth before the city descends into chaos.

[Devpost](https://devpost.com/software/pixel-truth) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[media_journalism]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** lua, luau, roblox, robloxstudio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pixel truth

## Body

Thumbnail Talk to witnesses Analyze a post - fake or real? Gain City Trust Learn more with Dr. Veritas Inspiration We were inspired by the work of the National Association for Media Literacy Education (NAMLE) and the broader movement around digital literacy education. Today, it has never been easier to create information that looks credible, and never harder to determine what is actually true. Headlines, screenshots, AI-generated quotes, and edited videos all circulate through the same feeds at the same speed, blurring the line between fact and fabrication. Rather than simply talking about misinformation, we wanted people to experience the challenges of navigating it. Our goal was to create an interactive learning environment that encourages curiosity, critical thinking, and media literacy skills in an engaging way. Roblox felt like the right platform because the audiences most affected by online information ecosystems are already spending time in immersive digital spaces like it. That vision became Pixel Truth - an interactive game where players see firsthand how information choices shape a community. In the game, the health of the city is measured by the player's accuracy in identifying fake news. What it does Pixel Truth places players inside a small city where a single visible metric - CITY TRUST, measured from 0 to 100 percent - reflects the community’s collective confidence in information. As players explore the city, they interact with characters like Dr. Veritas and engage in conversations that require evaluating news headlines and social media posts. Choosing accurate, well-verified information raises the trust level, while allowing misinformation to spread gradually lowers it. When trust collapses, the city begins to fall apart - the skyline darkens, buildings ignite, and social stability deteriorates. The experience transforms the abstract concept of “trust in information” into something tangible, allowing players to watch in real time how misinformation erodes communities destabilizes society. How we built it We developed the experience entirely in Roblox Studio using the Luau scripting language. The city environment was built in Workspace from modular building assets, allowing us to quickly iterate on layout and gameplay design. NPCs such as Coach Rivera, John Blackrock, and Dr. Veritas, are implemented as character models equipped with ProximityPrompts that trigger player dialogue interactions. Dialogue systems and trust-scoring mechanics run through server-side scripts housed in ServerScriptService, while shared modules and RemoteEvents in ReplicatedStorage keep communication synchronized between the client and server. The City Trust interface is displayed through a ScreenGui in StarterGui, which listens for trust updates and dynamically animates the progress bar. We organized development across three main areas: world and NPC design, dialogue and game logic, and user interface and player experience, collaborating and integrating our work using Roblox’s Team Create workflow. Challenges we ran into Our biggest challenge was simply getting started - two of the three team members had never opened Roblox Studio before this weekend. Before we could meaningfully build anything, we had to learn the entire development stack. Much of the first several hours were spent helping each other understand the fundamentals. The second challenge was scope. Our original concept included three fully developed narrative cases, each with its own setting, characters, and trust progression. About eight hours in, we realistically assessed what could be accomplished within a 36-hour build window and recognized that the plan was too ambitious. We pivoted to completing one case end-to-end while bringing a second to roughly 80% completion - polished enough for demonstration. Scaling back was difficult in the moment, but it ultimately strengthened the project by allowing us to focus on quality rather than spreading effort across multiple unfinished experiences. The third challenge involved animation. Getting Roblox characters to move naturally proved far more complex than expected. Navigating the animation editor, rigging workflows, AnimationTracks, and humanoid state management required significant iteration, but we persisted and successfully animated the NPCs. Accomplishments that we're proud of We built a city that feels like a real place, not just a flat map with NPCs placed on top. Streets, buildings, a plaza, and natural sightlines all guide players toward the next interaction. For a 36-hour build with two first-time Roblox Studio users, having the world read as coherent and navigable is something we’re really proud of. The UI was another key piece. The City Trust HUD became the main feedback system, and we refined it so it feels constantly present without being intrusive. Color, motion, and placement all help it sit naturally in the player’s attention. As a team, we stayed tightly aligned despite new tools and shifting scope, avoiding fragmented work through constant pairing and integration. We also maintained a consistent tone, aiming for writing that lets players draw their own conclusions instead of being told what to think. Finally, everything in the demo is real and playable - no placeholders or “imagine this works” moments. And through teaching each other everything as we went, we all came out of the weekend able to understand and navigate the full project. What we learned One of our biggest lessons was that immersion comes from both storytelling and environment design working together. On the dialogue side, we learned that pacing and meaningful choices are what make players emotionally invested. The trust system only felt engaging when conversations unfolded naturally and made players feel that their decisions genuinely mattered, encouraging them to keep interacting with the story. At the same time, the game environment played a huge role in maintaining engagement. Interactive elements, clear world layout, and visual guidance like path lines and directional cues helped players intuitively understand what to do next without breaking immersion. By reducing confusion and letting exploration guide progress, players stayed focused on the experience rather than the controls. Ultimately, we learned that players keep playing when they both care about the story and always know how to move forward. What's next for Pixel Truth Smarter NPCs are a next step - right now, conversations are fully scripted dialogue trees. We want to explore an LLM-powered layer so NPCs can respond to what players input in a chatbox, not just pre-written options, bringing the game closer to the kind of dynamic interaction that matches the problem we set out to explore. More scenarios and more city. Creating new cases that target different NAMLE core lessons, expanding into new neighborhoods, and additional characters would make the world feel even more reactive and immersive. Long-term, we want Pixel Truth to be something a teacher or parent could hand a child and say, “play this for twenty minutes.” A small, focused experience that quietly builds media literacy through play. <div