---
slug: "compile-crops"
url: "https://devpost.com/software/compile-crops"
title: "Compile Crops"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 605
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Compile Crops

> An edutainment farming simulator with codeable drones! Made with Meta Spatial SDK

[Devpost](https://devpost.com/software/compile-crops) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]]

**stack** android-studio, blender, figma, meta-spatial-sdk, spatial-sdk

## Body

Interface - Lock In Doomscrolling while Coding Shop Interface Coding Blocks Introduction Compile Crops is a mixed-reality edutainment farming simulator built with Meta’s Spatial SDK. Place your plot on your desk or floor, deploy drones, and write code that control how your drones plant, water, and harvest. As you expand your farm, you learn programming fundamentals like loops, conditions, sequencing, and automation through direct spatial feedback. We learned that the key advantage of using the Spatial SDK is that developers with Kotlin experience can quickly code 3d objects, along with traditional 2d UI very quickly. Inspiration New learners often struggle with how abstract coding feels. Tutorials and browser-based edutainment apps are helpful, but they rely on flat screens and offer little sense of physical cause and effect. We wanted to explore how meta-learning and gamification could feel alive inside a spatial environment. How we Built Compile Crops Compile Crops was created by Gulzar, a full-stack developer with experience in mobile apps, and Grace, a product designer and XR prototyper. Gulzar built the core farming systems, drone logic, code-block interpreter, and UI interactions using kotlin and the Spatial SDK’s Entity Component System. Special efforts went into building a custom AST to visualise code execution in realtime. We made use of custom shaders provided by the spatial sdk to enhance visuals Grace designed the experience flow, created all 3D assets, and implemented object placement, farm layout, and the styling within the Spatial Editor. Our workflow combined Kotlin programming knowledge (for logic, ECS, and UI) with Meta’s Spatial Editor (for placement, surfaces, and MR composition). More on Development (Gulzar) 2D stuff: I mostly used Jetpack Compose to design the level screen, objective dialog, and shop panels. To position elements visually next to each other, I used a parent transform component. A WebView panel was also used to emulate the compiler, along with a bridge that enabled communication between the Kotlin and JavaScript layers. I also implemented a custom AST tree to highlight lines of code during execution. 3D stuff: Custom button presses used the ValueAnimator class to perform animations. For the drone entity, a drone system was written to smoothly transition between different action states (harvesting, watering, seeding, etc.). Each action has various listeners that trigger other systems. For example, when the main drone finishes harvesting crops, it triggers callbacks so that the helper (the orange drone) can pick them up. For the wavy effect in wheat, a custom vertex shader was used. I also implemented a dual-grid tile map system that uses only six tiles in the tileset. Challenges On the Developer Side (Gulzar): Custom shaders took time to work with since they use GLSL, which I’m not very familiar with. The dual-grid tile map also took time to implement. Positioning entities relative to each other was tricky at first—I had to figure out the TransformParent component. After that, it became much simpler. On the Designer Side (Grace): Working with the Spatial Editor was tough because importing custom assets wasn’t predictable. Editing, testing, and rebuilding assets through Android Studio was also a big shift from Unity or Blender-first workflows. But, I did appreciate the fast build times compared to Unity! What’s Next We’re just getting started with Compile Crops. Our next steps include: Compete in multiplayer with your friends by building the most optimized drone for your farm. Add better rewards and a more robust progression system. Add improved levels that incorporate interesting algorithms such as nearest-neighbour and greedy approaches. With additional support or funding, we believe we can launch a publicly playable version in summer of 2026, bringing spatial coding education closer to users everywhere. <div