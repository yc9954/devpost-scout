---
slug: "the-digital-exorcist"
url: "https://devpost.com/software/the-digital-exorcist"
title: "The Digital Exorcist"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 598
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/document_pdf"
---

# The Digital Exorcist

> Turn boring file cleanup into a supernatural hunt. Play it as a game — or use it as a tool.

[Devpost](https://devpost.com/software/the-digital-exorcist) · hackathon [[Kiroween]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[accessibility]] [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[document_pdf]]

**stack** electron, fast-check, framer-motion, google-fonts, kiro, node.js, react-18, tailwind-css, testing-library, typescript, vercel, vite, vitest, zustand

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges
- accomplishments
- what we learned
- what's next

## Body

Inspiration The Digital Exorcist was inspired by a problem every developer and computer user knows well: a cluttered file system. Over time, systems become filled with forgotten downloads, duplicate files, and large files that quietly consume storage. Most file management tools reduce this process to technical lists and delete buttons, making cleanup feel boring, mechanical, and easy to ignore. The goal was to reimagine file management as an experience instead of a chore. By representing files as digital entities — ghosts for abandoned files, demons for large files, and zombies for duplicates — the cleanup process becomes more intuitive, narrative-driven, and engaging. The metaphor helps users understand why certain files matter, instead of treating cleanup as a blind delete operation. What it does The Digital Exorcist is a conceptual file management experience that turns system cleanup into an interactive, game-like flow. The project supports three distinct modes of interaction: Interactive Mode Users explore simulated file entities, inspect their properties, and decide how to deal with them through structured interactions and turn-based encounters. Swift Tool Mode A fast, minimal flow designed for users who want efficiency and clear decisions without narrative guidance. Story Mode A fully guided experience using simulated data only , allowing users to understand the system and mechanics without touching real files. The web demo runs entirely on simulated data to ensure safe public access and judging. How it was built The project is designed as a hybrid system. The core concept is intended for an Electron-based desktop application capable of interacting with the file system. For Kiroween, a separate web demo was built using Vite and React, operating exclusively on simulated data to ensure safety and public accessibility. The architecture is split into: a logic layer responsible for entity simulation, state management, and interaction flow a React-based frontend that renders the user interface and game experience a clear separation between conceptual mechanics and any real file system access Development followed a spec-driven workflow using Kiro . Requirements were defined first, translated into structured tasks, and refined through steering documents to maintain consistency across design, mechanics, and tone. Challenges One major challenge was balancing atmosphere with usability. Early iterations leaned too heavily on visual effects, which reduced clarity. This required careful refinement of pacing, contrast, and animation timing. Another challenge was designing turn-based interactions that felt meaningful without becoming complex or frustrating. Managing state transitions — such as player actions, entity responses, and outcome resolution — required careful structuring to avoid edge cases. Maintaining strict separation between simulation and real-world effects was also a key design constraint, especially for the public demo. Accomplishments Designing a cohesive concept that reframes file management as an experience Implementing a turn-based interaction system tied to file-inspired mechanics Creating a safe, fully simulated web demo suitable for public use Maintaining thematic consistency across visuals, logic, and UX Delivering a complete, structured project within a four-day timeframe What we learned This project reinforced how much context and presentation influence trust and engagement. Even when no real files are touched, framing decisions as understandable and intentional interactions makes users feel more confident and involved. From a development perspective, working with clear specifications and structured tasks — guided by Kiro — made it possible to move fast without losing coherence or control. What's next Future ideas include expanding entity types, refining interaction depth, and exploring intelligent classification systems that could one day support real-world file management — without sacrificing safety or clarity. The foundation is designed to scale conceptually, even as the mechanics evolve. But then again, who knows what the future holds... <div