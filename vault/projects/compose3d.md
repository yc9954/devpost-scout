---
slug: "compose3d"
url: "https://devpost.com/software/compose3d"
title: "Compose3D"
hackathon: "FIBO Hackathon"
organization: "Bria"
winner: true
words: 684
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Compose3D

> From 3D composition to AI-generated visuals.

[Devpost](https://devpost.com/software/compose3d) · hackathon [[FIBO Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** bria-api, next, react, react-three, three.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for compose3d

## Body

Inspiration Traditional 3D tools have a steep learning curve, and text descriptions alone often fall short. I wanted to bridge that gap with something intuitive: a tool where you compose a scene visually, and the app understands what you're building well enough to generate an actual image from it. What it does Compose3D is a web-based 3D scene composer that lets you build scenes visually and turn them into AI-generated images. You add objects, position them in 3D space, tweak their appearance, lighting, and camera angles, and the app generates a structured description of your scene. That description gets sent to the Fibo API, which creates a rendered image based on your composition. Core Features: Intuitive Object Placement : Drag and drop objects directly into the 3D viewport with real-time positioning Human & Non-Human Objects : Add people with customizable poses, clothing, and appearances, or use furniture, shapes, and environmental elements Custom Object Meanings : Not limited to predefined objects. Label any shape with a custom meaning (turn a cube into a "futuristic data core" or a "mysterious glowing artifact") and describe it however you want Advanced Appearance Controls : Customize colors, textures, materials, clothing, and other visual properties for each object Camera Control System : Orbit, pan, and zoom controls with preset camera views (front, side, top, isometric) or manual positioning Dynamic Lighting : Adjust scene lighting with controls for intensity, color, and lighting type to set the mood Scene Templates & Backgrounds : Start with predefined templates or customize your own background settings Real-Time Properties Panel : Select any object and fine-tune its position, rotation, scale, and appearance with precision Object Management : Duplicate, delete, and organize objects with an intuitive sidebar Structured JSON Export : Export your entire scene as structured data for use in other workflows or AI systems One-Click Image Generation : Convert your composed scene into a high-quality AI-generated image via integrated Fibo API The tool is flexible enough for quick mockups, creative brainstorming, storyboarding, or detailed visual planning. How I built it I built Compose3D with Next.js and React for the frontend, Three.js for the 3D viewport, and Zustand for state management. The scene composition logic is modular, with each object, camera setting, and lighting parameter translated into structured JSON that the Fibo API understands. The backend is a Next.js API route that validates scene data, sends it to Fibo, and polls for the generated image. Challenges I ran into Getting the scene-to-prompt translation right was harder than expected. 3D scenes have a lot of nuance (spatial relationships, lighting context, object semantics) and I needed to capture that in a way the API could interpret accurately. Making the UI feel natural was another challenge... 3D editing can be clunky, so I focused on smooth interactions and clear visual feedback. Handling edge cases like custom object labels required the system to be flexible enough to adapt based on context. Accomplishments that I'm proud of I'm proud of how accessible Compose3D feels. You don't need to know 3D modeling or prompt engineering you just build what you see in your head, and the app does the translation. The custom object labeling feature turned out better than I hoped, opening up creative possibilities I hadn't fully anticipated. I'm also happy with the modularity of the codebase, making it easy to add new features without getting messy. What I learned I learned a lot about structured prompting and how AI interprets spatial and visual data. It's not just about listing objects, it's about relationships, context, and hierarchy. I also got better at building reactive UIs that handle complex state without feeling sluggish, and integrating external APIs in a way that's resilient to failures. What's next for Compose3D I want to add animation timelines and collaborative editing. Better preset libraries (more objects, poses, materials) would make the tool even more versatile. I'm also exploring ways to let users refine generated images iteratively, tweaking the scene and regenerating until it's exactly right. Long-term, I'd love to see Compose3D used for storyboarding, game design prototyping, and creative workflows where visual communication is key. <div