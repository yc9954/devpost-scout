---
slug: "elsewhere-studio"
url: "https://devpost.com/software/elsewhere-studio"
title: "elsewhere3Dsketch"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 350
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# elsewhere3Dsketch

> A mixed reality sketch to 3D model generated studio, powered by MX INK

[Devpost](https://devpost.com/software/elsewhere-studio) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**domain** [[developer_tools]]

**stack** gemini, llama, meta-quest, mx-ink-sdk, three.js, type-script, webxr

## How they structured the write-up

- inspiration
- what it does
- preliminary stack
- what we learned
- what's next for elsewhere studio

## Body

Inspiration 3D modeling has a brutal learning curve. Every tool — Blender, ZBrush, SolidWorks — requires you to learn its way of thinking before you can make anything. But everyone knows how to draw. I wanted to see what happens when you skip the modeling interface entirely and just let people sketch what they want, then let a vision model handle the translation to actual geometry. What it does You sketch with the MX Ink in mixed reality. It only has to be a simple sketch, a stick figure, a blobby shape, whatever gets the idea across. That sketch gets sent to a vision model which interprets it and generates a 3D model via Three.js. The 3D-model is right there in front of you, and now, you just keep drawing on it! Sketch a hat on the head, add an extra limb, scribble some detail on the torso. The vision model receives the existing model plus your new strokes, understands the spatial relationship, and regenerates with your additions properly integrated. You're iteratively building up a 3D model through a back-and-forth conversation in sketches. Preliminary stack WebXR + Three.js for in-headset rendering, MX Ink SDK for stylus input and stroke capture, vision model API (Gemini, Llama) for sketch interpretation. The pipeline takes the vision model's structured output and translates it into Three.js geometry programmatically. What we learned MX INK's pressure sensitivity and full spatial tracking give the vision model meaningfully more signal than a flat 2D sketch would — you get stroke depth, drawing angle, pressure variation. That's a richer input for the AI to work with when figuring out what you meant. I'm very interested in exploring how much of a difference this makes with asset quality. What's next for Elsewhere Studio Build it. The core risk is the vision model interpretation loop, so that's first — get sketch capture → vision API → Three.js generation working end to end, then layer on iterative refinement. After that: export support (GLTF, OBJ) so models aren't trapped in the headset, and collaborative sessions where multiple people sketch on the same model. <div