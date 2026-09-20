---
slug: "seed-i6xesh"
url: "https://devpost.com/software/seed-i6xesh"
title: "The Dream"
hackathon: "Chroma Awards: AI Film, Music Videos, and Games"
organization: "ElevenLabs"
winner: true
words: 712
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/transportation"
  - "substrate/video_visual"
---

# The Dream

> The Dream is an immersive world with over 12,000 generated 3D models, created by 2 people in 1 month. It explores how artistic agency evolves using AI to augment human intuition, emotion, and meaning.

[Devpost](https://devpost.com/software/seed-i6xesh) · hackathon [[Chroma Awards- AI Film- Music Videos- and Games]]

## Facets

**domain** [[transportation]]
**substrate** [[video_visual]]

**stack** 404-gen, ableton, adobe-creative-suite, blender, elevenlabs, fal, midjourney, openart, unreal-engine

## How they structured the write-up

- 12,000 objects - 2 people - 1 month
- human x ai interactions
- key technologies
- alpha release

## Body

Gameplay Screenshot Gameplay Screenshot Gameplay Screenshot Gameplay Screenshot Gameplay Screenshot The Dream This game ( The Dream ) is a creative exploration into how human agency evolves when the artist becomes a curator more than a traditional asset creator. The goal was to understand how AI can accelerate production without collapsing artistic authorship or flattening creative identity. We began with a set of questions that guided our design choices: Can two people build a world with spatial, narrative, and cinematic depth in one month? What happens when AI imperfections - artifacts, distortions, uncanny moments - are treated as part of an emerging aesthetic vocabulary rather than flaws to remove? Which aspects of worldbuilding should remain human to preserve intention, tone, and narrative coherence? 12,000 objects - 2 people - 1 month To test these ideas, we built an open world that spans four square kilometers (with above and below ground interventions). It is dense with narrative detail and created through a hybrid process of AI-assisted 3D asset generation and human-led storytelling and creative / art direction. More than 12,000 3D objects populate the environment - all stylistically cohesive, generated with 3D AI and refined through a curated pipeline. The enormity of this scale was deliberate: we aimed to show that a tiny (two person) team can reach cinematic density in a fraction of the time (1 month) . The most important learning was that constraints introduced by AI can become strengths when treated as part of the visual language. Accepting artifacts and irregularities created an aesthetic that felt raw and alive, especially in a dark, layered urban setting. Human x AI Interactions The build process followed a tight loop: Generate 2D concepts in Midjourney, OpenArt, and fal. Use those references with 404–GEN to generate 3D splats (and convert them to meshes). Refine outputs with PBR adjustments and targeted artistic passes. Mix and balance generated assets (props, buildings, vehicles) with simple manual surfaces (flat, low information geometry like floors and blank walls). Use ElevenLabs and Ableton to create voices, soundscapes and music, then blend them with human composed audio. Shape narrative through placement, lighting, pacing, and spatial composition in Unreal Engine to build storytelling. This produced a workflow where AI handled variation and volume, and humans shaped intention, emotion, and meaning. Imperfections from the models, which a conventional pipeline would either hide or correct, became part of the world’s texture. They added tension and a slightly surreal quality that reinforced the narrative tone. Key Technologies We relied on a diverse range of AI technologies working together to build this game. Concept art and early 2D visual exploration began with Midjourney, OpenArt, and fal . These tools allowed rapid iteration, letting us refine style and mood before moving anything into a 3D pipeline. The transition from 2D to 3D was handled by 404–GEN, our open-source project for generating gaussian splat based 3D models using a decentralised AI framework . Through a custom (and open-source) Blender integration, images were converted into splats and then into meshes. In Blender, we adjusted materials, rigged models when needed, and applied targeted refinements using Blender-native tooling so the assets could function reliably once placed in the world. This workflow acted as a bridge between fast AI output and fully usable game-ready elements. A link to the github repo for 404–GEN is included with our submission in case the jury is interested in a deeper technical review of the underlying 3D AI and Visual Language Model technology: 404–GEN Github Final assets were exported into Unreal Engine , creating a clean flow from generation to refinement to integration. Audio followed a similar hybrid process: we used ElevenLabs and Ableton for voices, sounds, music and atmospheric layers, mixed and integrated them procedurally in Unreal to support spatial storytelling and create a more immersive experience. Alpha Release What began as an experiment for this competition now grows into the first chapter of a larger world. The project will continue to evolve, and this build represents an alpha version - the foundation for ongoing creative exploration into a additional gameplay mechanics, player choices and branching narratives. A link to a public overview of our project is included with our submission in case the jury is interested in following its evolution: The Dream Overview <div