---
slug: "scratchml-ckxuh2"
url: "https://devpost.com/software/scratchml-ckxuh2"
title: "ScratchML"
hackathon: "Mind the Product presents World Product Day: Everyone Ships Now"
organization: "Mind the Product"
winner: true
words: 768
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/accessibility"
  - "domain/education"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ScratchML

> Scratch, but for AI: kids snap blocks, show examples by webcam or doodle, and watch a real neural network learn to see — live in the browser. No code. No accounts. Nothing uploaded.

[Devpost](https://devpost.com/software/scratchml-ckxuh2) · hackathon [[Mind the Product presents World Product Day- Everyone Ships Now]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[accessibility]] [[education]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** javascript, mobilenet, nextjs, react, tailwind, tensorflow.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scratchml

## Body

Novus.ai Dashboard Novus by Pendo on the live site Landing Page Inspiration Google's Teachable Machine proved the pipeline in 2017: browser-based, no-code, train-on-your-webcam. We asked a different question: what would it take for a seven-year-old to do this alone — and want to come back tomorrow? Three things, we think: no camera required (plenty of kids, parents, and classrooms won't turn one on — so your crayon drawings become the dataset), a pipeline you can see (every step is a named block you snap into place), and joy (a robot coach, sounds, confetti — the moment it learns should feel like magic you made). What it does ScratchML is a studio where kids train a real image classifier with zero code: 🧩 Snap a recipe — Use the Camera (or Use the Sketchpad ) → Teach a Thing ×2+ → Train the Brain → Guess It! ✏️ No camera needed — a crayon sketchpad (7 colors, brush sizes, eraser, undo) makes drawings the training data — the wedge Teachable Machine never shipped 🧠 Train in seconds — MobileNet transfer learning + a trainable head, entirely in the browser 🎉 Guess live — confidence bars, a reactive robot mascot, confetti on the first confident guess 🗑 Curate like a practitioner — inspect and delete individual training examples Honest note: today the blocks form one guided recipe, not arbitrary programs — training wheels that teach the vocabulary of every ML system (input → examples → train → predict). Real composability is the roadmap, below. Privacy is structural: camera frames and drawings never leave the device. There is no backend. How we built it ML : TensorFlow.js + MobileNet v2 (self-hosted weights); hardware WebGL with a WASM-SIMD fallback for machines without it — kids' products get opened on old school laptops Studio : Next.js 16, TypeScript, Tailwind v4, dnd-kit, zustand; custom pointer-events sketchpad with coalesced input Proof : a Playwright suite that draws shapes with the mouse, trains, and asserts the model recognizes a new drawing — run against the live production URL Shipping : Docker on Fly.io; Novus by Pendo measuring from day one; the model pre-loads while visitors read the landing page Tooling : built with Claude Code as the development pair, ElevenLabs for sound, OpenAI image models for art — the human owned every product decision, scope cut, and live-site bug report Challenges we ran into The self-erasing sketchpad — "my drag doesn't register" was a React effect with an unstable dependency repainting the canvas white whenever an unrelated toast dismissed. Two-line fix, found by measuring instead of guessing. The invisible GO block — Tailwind v4 tree-shakes tokens it can't see in class names; our runtime-composed block colors got deleted from the CSS and the most important button rendered white-on-transparent. The 17-second brain — without hardware WebGL, shader compilation took 17s and the CPU fallback froze the page. The WASM backend cut inference ~100×; the e2e suite went from 4.5 minutes to 49 seconds. The model that learned the "wrong" thing — circles drawn in ink, squares in red crayon: it classified a red circle as a square. Not a bug — color really did separate the examples. It's now a coaching moment in the product. A bug only real use found — picking a demo after the model loaded stranded the GO button on "loading brain…" forever. The user's exact flow became a regression test: verified failing on production, then fixed. Accomplishments that we're proud of A stranger can open a URL and train a neural network in about two minutes — on a phone, no account, no camera required The e2e suite tests actual learning , not just UI The privacy claim survives a network-tab audit WCAG AA contrast, focus-trapped dialogs, and keyboard-operable capture — on candy-colored blocks What we learned Name your prior art. Early drafts implied more novelty than we'd earned; "Teachable Machine, rebuilt as a toy" is truer and stronger. Variety is the curriculum. A model learns whatever separates your examples — so teaching kids to vary their drawings isn't a tip, it's the lesson. Perceived performance beats raw performance. Pre-loading during the landing page made the loading screen effectively disappear. What's next for ScratchML One idea: earn the Scratch comparison. Action blocks — "when it sees ⭕ → play a sound." The trained model becomes a sensor kids can program against; the blocks become a language, not a recipe. Fool-my-model links — friends try to draw something that breaks your model. Adversarial thinking, disguised as a game. A second sense — sound classification through the same blocks, proving the vocabulary generalizes. <div