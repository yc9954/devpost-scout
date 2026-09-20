---
slug: "augmental-puzzles-7e3baq"
url: "https://devpost.com/software/augmental-puzzles-7e3baq"
title: "Augmental Puzzles"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 870
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
---

# Augmental Puzzles

> Classic pen-and-paper puzzles reimagined for XR — with native Logitech MX Ink support, spatial OCR handwriting input, and a freeform scratch pad for thinking in ink the way humans naturally do.

[Devpost](https://devpost.com/software/augmental-puzzles-7e3baq) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]]

**stack** aws-lambda, c++, epic-online-services, gdscript, godot

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for augmental puzzles

## Body

Inspiration While adding Logitech MX Ink support to the Godot Engine, we were inspired to draw and play these classic games right in the air. This sparked a quest to find our favorite logic puzzles in XR, only to realize the perfect pen-based experience was still waiting to be created. Classic newspaper puzzles: Sudoku, Nonograms, Minesweeper. Familiar to everyone, hundreds of millions of people solve them daily, thinking in ink. Scribbling out possible solutions and penciling in ideas before committing. This space is completely underserved in the XR marketplace. We're stepping in to bring these familiar puzzles into mixed reality, expand them into magical spatial variants only possible in XR, and fully support the precision hardware that first inspired us. What it does Augmental Puzzles is a collection of logic puzzles in XR designed to be comfortable and relaxing. We launched into Early Access on Meta Quest and Steam with Classic Sudoku, and we're bringing Nonograms, Minesweeper and more puzzle models monthly. Supporting full competitive and collaborative multiplayer before our 1.0 launch. Starting traditional and expanding to exciting new Spatial Variants only possible in the magic of virtual worlds with true 6 dof input. All while maintaining single controller play, comfort and a focus on the puzzles. What's in the box right now: Play across a full range of Sudoku sizes from simple 6x6 to massive 16x16 puzzles Handset puzzles, always by humans. Aided by a Puzzle Engine we have built to validate and provide human style hints to players. Our puzzle engine scales out to any constraint based puzzle. Daily challenges, scoring and leaderboards Smart pencil marks with optional auto-clear Infinite undo and shareable replays Passthrough everywhere or calming immersive environments Intelligent help: number highlighting, rules validation, optional solution checker Cloud saves across devices What MX Ink integration brings: Native pen controls : purpose-built one-handed stylus UX, not a controller remap Scratch pad : a freeform ink layer on every puzzle for working out candidates and thinking in ink, the way you'd scribble on newspaper margins Spatial OCR : our symbol sets are tiny and puzzle specific so we can build a lightweight on-device model that turns handwritten strokes into puzzle inputs and commands. How we built it The project is built on a custom branch of the Godot Engine, specifically specialized for our spatial puzzle mechanics. We actually shipped the original Logitech MX Ink support into the engine ourselves, and we plan to share our custom engine advancements back to the MIT-licensed core so the wider development community can benefit. Under the hood, our generic constraint-based puzzle engine is built in portable C++ as a Godot Extension to guarantee fast, efficient inference. The architecture is split into two parts: we utilize a larger toolset version for our development pipeline, while a smaller, highly optimized hint runtime ships directly within the title. While our original custom OCR model has experienced some code rot, we know exactly how to fix it. If accepted into later rounds, we are fully confident in reviving it to get fast, on-device handwriting inference running smoothly again. Challenges we ran into Puzzle solving and comfort first, we designed everything around a SINGLE controller input limited to the Mx Ink button set. Which presented some unique challenges. Working in Ink feels great but you need the speed of button driven classic input so mixing those two modes and switching is a unique challenge we think we have solved. We looked at full OCR but the on device and less than perfect model was frustrating hence why we limited it to puzzle symbols being OCR and keep the scratch notes in stroke space Rendering a lot of strokes at a decent resolution means bitmaps are too heavy for VRAM so we use an implicit stroke engine to render Accomplishments that we're proud of We're live. Classic Sudoku shipped into Early Access on multiple platforms with more coming, and monthly updates lined up. This isn't a concept, it's a product on store shelves. Our comfort first design with mixed reality means we are seeing well above industry average session times on Quest. The scratch pad concept feels great, can’t wait to bring it back. Our constraint solver helps us hand-set puzzles we can be confident in and that are pleasant to play. It also provides better human hints; we are still working on surfacing their full quality in the UX, but the hint system is already a great teacher. Daily challenges and puzzle packs being handset feels so much better than generated puzzles. What we learned MR passthrough has crossed the threshold where people genuinely want their headset on for casual computing. Relaxing puzzles are a perfect fit for that. The stylus audience is massively underserved. Most MX Ink titles are creative or productivity tools — entertainment is wide open Clean, neutral design wins. Low friction beats flashy themes for this genre. Open the app, solve a puzzle, breathe. What's next for Augmental Puzzles Nonograms (Picture Crosswords) and Minesweeper Spatial puzzle variants — 3D Nonograms, Skyscraper with real depth Multi-platform expansion to all platforms. No headset left behind. Multiplayer modes, both collaborative and competitive Social Progress and Levelling up to give more sense of community and progression <div