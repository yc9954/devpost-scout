---
slug: "metro-police-ai-powered-visual-mystery-game"
url: "https://devpost.com/software/metro-police-ai-powered-visual-mystery-game"
title: "Metro Police: AI-Powered Visual Mystery Game"
hackathon: "FIBO Hackathon"
organization: "Bria"
winner: true
words: 620
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Metro Police: AI-Powered Visual Mystery Game

> In the shadows, the truth always finds a way to shine

[Devpost](https://devpost.com/software/metro-police-ai-powered-visual-mystery-game) · hackathon [[FIBO Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[runtime_tool_creation]]
**substrate** [[geospatial]] [[video_visual]]

**stack** bria, fibo, next.js, openrouter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for metro police: ai-powered visual mystery game

## Body

Inspiration I've always loved detective games and visual novels, but I noticed something: all of them use static, pre-made images. What if a mystery game could generate its visuals dynamically, responding to every player action in real-time? When I discovered BRIA FIBO's structured JSON prompts, I realized this was finally possible. The ability to control camera angles, lighting, and composition through JSON meant I could build an AI "Game Master" that truly sees what the player describes. The film noir genre was a natural fit—its dramatic shadows and moody atmospheres are perfect for showcasing FIBO's precise visual control. Every "examine the evidence" or "look around" command triggers a custom-generated image with the right lens, focus, and mood. This project started as an experiment to see how far we could push AI-driven visual storytelling. Turns out, pretty far. What it does Metro Police is a text-based detective game where every visual is generated in real-time using BRIA FIBO. Players type natural language commands like "examine the coffee cup" or "go to the break room," and an AI Game Master interprets these actions, generates narrative responses, and creates matching visuals through FIBO's structured JSON prompts. The camera angle, lighting, and composition automatically adapt to player intent—macro shots for evidence inspection, wide angles for exploration, portrait framing for conversations How we built it We built Metro Police using Next.js with TypeScript for the frontend, and integrated two AI systems: OpenRouter (DeepSeek) for narrative generation and BRIA FIBO for visual generation. The core innovation is the "action-aware" prompt generator. When a player examines evidence, the LLM constructs a FIBO JSON schema with macro lens settings and shallow depth of field. When exploring a room, it switches to wide-angle parameters. All visuals maintain film noir consistency through shared style tokens. Challenges we ran into Getting consistent visuals across different actions was tricky. Early tests produced images that felt disconnected—different lighting, color palettes, and styles for each scene. We solved this by implementing a visual history system that feeds recent FIBO outputs back into the LLM context, ensuring each new image respects the established aesthetic. Tuning the FIBO parameters (steps, guidance scale) for the right balance of quality and speed also took iteration. Accomplishments that we're proud of The fact that every single visual in the game is dynamically generated—no pre-made assets. Players can investigate objects that weren't even in the original scenario, and FIBO produces coherent, stylistically consistent images for all of them. The action-to-camera mapping system also feels intuitive. We didn't expect the difference between "look around" (50mm, wide) and "examine closely" (100mm macro, shallow DOF) to feel so natural, but it does. What we learned FIBO's structured prompts are incredibly powerful when you embrace them fully. Instead of crafting text prompts, building JSON objects with explicit lighting, composition, and camera parameters gives you precise control that text prompts can't match. We also learned that agentic workflows need guardrails—the LLM sometimes overcomplicates the visual descriptions. Keeping the JSON schema constrained but flexible was key. What's next for Metro Police: AI-Powered Visual Mystery Game More cases, more locations, and voice narration. We want to add audio for dialogue and ambient sounds to make the experience more immersive. We're especially excited about BRIA FIBO's upcoming features. Character consistency is coming soon, which will let us generate the same suspect face across multiple encounters—essential for detective games where you interrogate people repeatedly. If 2:1 panorama support becomes available, we'll definitely integrate it into our lens system. Imagine "look around the crime scene" generating a true wide panoramic view that you can pan through. That would take the immersion to another level. Multiplayer investigations could also be interesting—multiple detectives working the same case, sharing clues in real-time. <div