---
slug: "splat-n-treat"
url: "https://devpost.com/software/splat-n-treat"
title: "Splat-n-Treat - WorldNotes"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 1041
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Splat-n-Treat - WorldNotes

> A Notion for AI 3D Spatial Worlds: A spatial CMS powered by client-side AWS + Gaussian splats + Kiro-assisted architecture refactoring.

[Devpost](https://devpost.com/software/splat-n-treat) · hackathon [[Kiroween]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[provenance_signing]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[legal_professional]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, blender, cloudfront, cognito, glb, guassian-splats, javascript, kiro, lamp, liquidmetal, python, raindrops, react, s3

## How they structured the write-up

- 1. rendering core — spark.js + glb integration
- 2. treat engine — the core abstraction
- 3. backend architecture — client-side aws (not zero-backend)
- 4. kiro usage — strongest implementation score section
- 5. architecture split — skeleton crew category

## Body

Splat-n-Treat → WorldNotes A Notion for AI 3D Spatial Worlds: A spatial CMS powered by client-side AWS + Gaussian splats + Kiro-assisted architecture refactoring. 🧠 Inspiration 2026 will be the first year where AI-generated 3D scenes become widespread: Gaussian splats from mobile photogrammetry AI world models capable of generating indoor/outdoor scenes Neural rendering pipelines that output full environments But nothing exists today that lets ordinary users annotate, explain, or build meaning inside these worlds. There is no equivalent of Notion or WordPress for 3D spaces. Our insight: The world can stay static — but the layer of meaning placed inside the world must be dynamic. WorldNotes is that dynamic layer. 🧩 What It Does WorldNotes lets anyone: Load a .spz Gaussian splat world Walk through it (WASD + mouselook) Click to place 3D “Treats” (GLB objects) inside the scene Add messages, notes, metadata Reposition, rotate, edit, delete Press Share , which: serializes the scene as JSON uploads it to S3 using client-side Cognito credentials generates a shareable viewer URL hosted on CloudFront Viewers can: Explore the world Interact with the placed notes No login, no install, no editor UI This is effectively Notion for 3D worlds , built on fully client-side, credentialed AWS access. 🛠 How We Built It (Technical Detail that Wins Points) 1. Rendering Core — Spark.js + GLB integration We built a unified WebGL pipeline that merges: Gaussian splat rendering (Spark.js) GLB treat rendering (THREE-style transforms mapped into Spark coordinate space) Scene graph overlays Technical features implemented: camera calibration panel with live pose export forward-vector math for treat placement raycasting into splat space deterministic placement on uneven surfaces cross-origin GLB loading with correct CORS settings 2. Treat Engine — the core abstraction A minimal but expressive schema: { "world": { "name": "Factory Floor", "splat": "factory-floor.spz" }, "treats": [ { "id": "uuid", "url": "geomarker_animated.glb", "pos": [x, y, z], "rot": [pitch, yaw, roll], "message": "string" } ], "camera": { "pos": [...], "rot": [...] } } Why this matters: Supports arbitrary 3D annotations Stable across worlds, splats, NeRFs, and AI-generated scenes Extensible (scale, custom metadata, typed treat classes) Can be diffed or streamed later (for multiplayer editing) 3. Backend Architecture — Client-Side AWS (NOT zero-backend) AWS S3 hosts: splat files treat-layer JSON GLBs thumbnails public READ for viewer Cognito-authenticated PUT for editor AWS Cognito Identity Pool Client-generated AWS STS credentials. We used: unauthenticated identities IAM roles scoped to exact prefix paths Kiro to debug “resource prohibited” field issues in IAM CloudFront viewer + editor static hosting fast global caching URL parameter routing CORS preflight compatibility Why this wins points: We are not using “no backend”; We are using a real, production-grade distributed backend , powered entirely through client-side AWS SDK — a modern pattern used by Figma, Framer, and other edge-native apps. 4. Kiro Usage — Strongest Implementation Score Section We used Kiro aggressively and meaningfully: Vibe Coding rewrote S3/Cognito integration in minutes generated IAM policies repaired CORS configs scaffolded viewer/editor split Specs defined treat schema abstracted world loader contract defined core module interfaces: addTreat, removeTreat, updateTreat, serializeScene, applyCameraPose Hooks autosave treat UUID generation scene validation batch object cleanup Steering guided architecture refactor into a clean split standardized naming conventions removed accidental complexity MCP synced static assets patched configs live regenerated file trees for two separate repos This demonstrates “above-and-beyond” Kiro usage — not just codegen, but system design, debugging, and refactoring . 5. Architecture Split — Skeleton Crew Category We produced a shared core + two fully separate repos , in under an hour: worldnotes-core Splat loader GLB loader Raycaster Camera calibrator Treat manager Scene serializer URL config parser worldnotes-editor (Repo 1) full edit panel treat placement custom GLB loading message editing reposition/drag mode S3 upload Share modal camera calibration UI worldnotes-viewer (Repo 2) read-only world exploration treat display message interaction no S3 writes lightweight, embeddable viewer This satisfies — explicitly — the Skeleton Crew requirement: One core, two meaningful, distinct applications. 😱 Challenges We Overcame (Technically Explicit) 1. Spark.js WASM fail on Vite We had to remove Vite, switch to: pure ES modules predictable WASM loading paths CloudFront-friendly asset resolution 2. IAM policy misconfiguration Cognito complained: “resource contains prohibited field.” Kiro helped us generate: "Resource": "arn:aws:s3:::worldmatica/splat_n_treat/*" for correct role delegation. 3. S3 CORS failures Fixed: Access-Control-Allow-Origin: * GET, PUT x-amz-acl CloudFront invalidations 4. world-space vs splat-space mismatch Solved by: calibration panel world origin reset consistent meters-per-unit normalization 5. UX complexity inside FPS worlds Resolved by: drag-to-move mode edit modal separation treat highlight feedback toggled cursor states 🏅 Accomplishments We’re Proud Of Built a spatial CMS for the coming tidal wave of AI 3D worlds. Designed a professional-grade client-side AWS backend . Performed a complete architecture split in under 60 minutes with Kiro. Created a standard for 3D annotation layers parallel to WordPress/Notion for 2D. Fully open-source, easy for anyone to self-host on S3. 📚 What We Learned Gaussian splats are stable foundations for mixed-reality UI. Treat layers (GLB overlays + metadata) form a universal spatial data structure. Kiro is exceptionally strong at refactors, debugging cloud configs, and structuring repos. Client-side cloud architectures minimize operational overhead while preserving power. 🚀 What’s Next 1. Multi-user co-editing (CRDT-based spatial deltas) 2. Semantic AI hotspots (“suggest treat placement here”) 3. Plugin treat types (scripts, interactions, metadata) 4. World model importers (AI → splat → editable CMS) 5. Spatial RAG index (embedding queries inside 3D environments) 🎯 Judges’ TL;DR Splat-n-Treat becomes WorldNotes: a spatial CMS for 3D worlds, powered by Gaussian splats, a robust client-side AWS backend, and a Kiro-assisted architecture split into two real applications (editor + viewer). It showcases advanced implementation depth, production thinking, and exceptional use of Kiro. Powered by LiquidMetal AI Raindrop + Vultr Compute This project integrates LiquidMetal AI’s Raindrop platform as the orchestration layer for AI-generated 3D assets, using SmartBuckets for artifact storage, SmartSQL for job and provenance tracking, SmartMemory for reusable intent profiles, and SmartInference for deterministic fabrication planning. Heavy 3D processing (mesh optimization, UV unwrapping, texture baking, and export) is executed on Vultr-hosted compute , allowing raw AI outputs to be converted into game-ready, production-usable assets . Raindrop turns AI 3D from disposable output into an iterable, versioned fabrication pipeline , while Vultr provides the scalable compute needed to make the process fast and repeatable. <div