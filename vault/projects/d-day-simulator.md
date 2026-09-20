---
slug: "d-day-simulator"
url: "https://devpost.com/software/d-day-simulator"
title: "D-Day Simulator"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 625
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/immigration_refugee"
  - "substrate/video_visual"
---

# D-Day Simulator

> Survive the largest amphibious assault in human history and GET OFF THE BEACH. The fate of Europe is on your shoulders, soldier.

[Devpost](https://devpost.com/software/d-day-simulator) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[immigration_refugee]]
**substrate** [[video_visual]]

**stack** horizon

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for d-day simulator

## Body

Cinematic cutscene sets the mood when the player enters the world. An AI NPC instructs the user on what to do next. The player must avoid threats, such as. bomber planes, machine guns, and mines while trying to to reach the end of the beach. Historically accurate props set the scene and enhance the role playing element. High score boards encourage competition. VFX overlays add mood and immersion to the environment (in this screenshot, you see the rain overlay) Inspiration We were inspired by the success of Titanic Simulator on HorizonWorlds, and wanted to create a culturally significant, action-packed survival simulator that rewarded multiplayer co-operation and used unique mobile-native design for a peak experience. Our goal was to take the immersion associated with VR and bring it to mobile through smart camera usage and Noesis overlays. What it does The player arrives at the beaches of Normandy via landing craft and must clear 1000 meters of sand guarded by machine guns, mines, barbed wire, an airforce and much more. Players work together to identify high risk areas and avoid them, while moving strategically to avoid the threats that sweep across the beach in systematic patterns. How we built it We designed the game as a multiplayer experience where every player progresses independently using their own skill and strategy, yet cooperation is always optionally available. Players can see where others are on the beach, how far they’ve advanced, and where/how they died. This lets them learn from others mistakes, coordinate movements if they choose to, or simply compete for the furthest run. So the experience can feel fully solo or highly cooperative depending on the player’s preference. Instead of relying on VFX gizmo, we supplemented and enhanced all effects (rain, explosions, smoke, blood splatter, bullet impacts, etc.) with image-sequence overlays in Noesis Studio, delivering far richer visual effects. We used gen AI NPCs for an onboarding experience that was memorable and unique each time. The user experience is optimized for mobile with custom mobile icons marking controls , and other mobile-only features such as haptics support the feel that this is a native mobile experience. Challenges we ran into One major issue came from our animated overlay system: many intense effects (explosions, rain, etc.) were built as short 4–5 second sequences of high-resolution images. The combined texture size was too large for Horizon Worlds’ strict memory limits, causing long loading times or failed loads entirely. We solved it by aggressively compressing the images, reducing color depth where the eye wouldn’t notice, cutting unnecessary frames, and implementing a system that only keeps the currently needed sequences in memory. Also creating Noesis GUI overlays that perfectly cover the entire screen on both mobile and web was tricky. Some devices left visible borders, breaking immersion for effects like heavy rain or flashing explosions. We fixed this by adding a full-screen viewbox and carefully adjusting the render settings in Noesis. Accomplishments that we're proud of We're very proud of using Noesis almost like a VFX tool in addition to as a UI tool. We really wanted to push the limits of what was possible with it. We're also proud of how effectively our onboarding sequence sets the mood, through the animations, cutscene-like camera movements, and NPC usage. What we learned Noesis was the big one! We learned how to use it from scratch and how to use it as a VFX tool in addition to a UI tool. What's next for D-Day Simulator We want to focus on developing an uprade system that allows the player to level up in rank and use their playtime to purchase improvements, such as bolt cutters that allow them to cut through barbed wire, gas masks that help them evade toxic threats, etc. <div