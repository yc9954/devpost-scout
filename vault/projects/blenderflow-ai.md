---
slug: "blenderflow-ai"
url: "https://devpost.com/software/blenderflow-ai"
title: "BlenderFlow AI"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 286
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
---

# BlenderFlow AI

> The first native Logitech plugin for Blender — combining physical dial/key controls with AI-powered 3D model generation, bringing 14M Blender users into the Logitech MX ecosystem.

[Devpost](https://devpost.com/software/blenderflow-ai) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]

**stack** .net, blender, c#, hunyuan3d, hyper3d, logisdk, polyhaven, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next

## Body

Inspiration Blender has over 14 million monthly active users, making it the world's most popular free 3D creation tool. Yet on the Logitech MX Marketplace, there is no native Blender plugin — only basic keyboard shortcut profiles inherited from the old Loupedeck platform, which have known modifier key compatibility issues on macOS. We saw an opportunity to build the first true API-level Blender plugin for the MX Creative Console and MX Master 4, and to push it further with AI-powered 3D generation. What it does BlenderFlow AI transforms the MX Creative Console into a dedicated Blender control surface: Dial — Smooth viewport orbit, zoom, and parameter fine-tuning LCD Keys — One-tap mode switching (Object / Edit / Sculpt) with dynamic icon feedback Roller — Adjust active property values (bevel width, subdivision level, brush size) Actions Ring (MX Master 4) — Instant access to frequently used Blender tools Haptic Feedback — Physical confirmation when operations complete The AI Layer — what sets us apart: Press one button to generate 3D models from text using Hyper3D Rodin / Hunyuan3D AI-powered material application — search and apply textures in one click Smart scene analysis and optimization suggestions Browse AI-generated variants by rotating the dial How we built it Logi Actions SDK (C# / .NET 8) — Plugin core with Commands and Adjustments Blender Python Addon — Receives instructions via WebSocket for real-time bi-directional communication Hyper3D Rodin API / Hunyuan3D — AI 3D model generation PolyHaven Integration — AI-assisted material search and application What's next Prototype development after receiving Logitech hardware (Top 50 phase) Publish to Logitech Marketplace as freemium (basic controls free, AI features as Pro subscription) Expand to support more 3D apps (AutoCAD, Maya, Cinema 4D) ``` <div