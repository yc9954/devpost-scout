---
slug: "voxel-pnxmlc"
url: "https://devpost.com/software/voxel-pnxmlc"
title: "Voxel"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 496
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Voxel

> Revitalizing education through a headset powered by Augmented Reality and Generative AI.

[Devpost](https://devpost.com/software/voxel-pnxmlc) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** dart, flutter, genai, html, langflow, meshyapi, nix, ruby, shell, swift, watsonai

## How they structured the write-up

- inspiration
- product summary
- technology stack

## Body

LandingPage Scene Detection & Anchor Placement Informative Flashcards Saturn V Diagram Rocket Launch Rocket Launch Pt.2 Inspiration As a team, we wanted this hackathon to be a massive learning experience. We took a leap of faith, challenging ourselves to learn Augmented Reality, mobile app development for the first time using Flutter, and Generative AI workflows in a single weekend. Our goal was to prove that with AI and spatial computing, learning doesn't have to be static; it can be a hands-on, engaging , and infinitely customizable experience. Product Summary Voxel is an immersive Augmented Reality application that brings high-quality, AI-generated, and animated educational models into the real world. The app aims to make education more accessible and engaging by: The AI Model Generator (Personalized Learning): Students or teachers can enter a text prompt (e.g., "a bronze Roman gladiator helmet" or "a plant cell structure") into the app. To ensure security and performance, this request is routed through our custom Dart proxy server, which orchestrates a complex "preview and refine" workflow with the Meshy AI API. Once generated, the app maps the physical environment and anchors the high-fidelity 3D model onto a desk or floor. This allows students to physically walk around and inspect concepts they are learning about in real-time. Saturn V Diagram & Spatial Flashcards: This module acts as an interactive, spatial textbook. Users place the Saturn V rocket into their physical environment, and the app automatically generates hovering 3D "flashcards" for each key component (First Stage, Service Module, Lunar Module, etc.). Using quaternion math, the app continuously calculates the camera's position to ensure these flashcards always "billboard" (rotate to face the user) as they walk around the rocket. Saturn V Rocket Launch Animation: Education shouldn't just be static; it should be an experience. This module allows users to experience the Apollo 11 launch sequence right in their living room. After placing the rocket, a synchronized audio countdown begins, triggering dynamic flame sprites, thrust audio loops, and a mathematically smoothed ascent animation that carries the rocket upwards into a procedurally placed cloud layer. Technology Stack Languages: Dart: Utilized across the entire stack, powering both the mobile frontend and the backend proxy server. Frameworks and Libraries: Flutter: The core UI framework used to build the visually rich, cross-platform mobile application. ar_flutter_plugin_2: Leveraged to handle complex Augmented Reality sessions, bridging ARCore and ARKit. We used this for plane detection, rendering 3D (.glb/.gltf) nodes, and managing the 3D translation math required for spatial UI (billboarding). Shelf: A modular web server framework for Dart, used to build our backend proxy that handles API routing and multi-step polling. IBM Tech Stack Langflow: To orchestrate overall research agent workflow using the LangFlow Canvas Watson AI: For agent prompt refinement and conversation of agent output into JSON format DB2: Storage of image assets after 3D Rendering Platforms: Meshy AI: The generative AI platform powering our text-to-3D engine. We utilize their robust API to execute a two-stage (preview and refine) generation workflow. <div