---
slug: "instameme-oh8m3c"
url: "https://devpost.com/software/instameme-oh8m3c"
title: "InstaMeme"
hackathon: "Arm AI Developer Challenge "
organization: "arm"
winner: true
words: 427
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "substrate/video_visual"
---

# InstaMeme

> InstaMeme is a fully on-device, privacy-first meme creation app powered by Apple Silicon and the MLX framework.

[Devpost](https://devpost.com/software/instameme-oh8m3c) · hackathon [[Arm AI Developer Challenge]]

## Facets

**mechanism** [[on_device_local]]
**substrate** [[video_visual]]

**stack** applevisionframework, arm64, avfoundation, coregraphics, imagerendererapi, ios17, localai, mlx, mlxllm, photosui, quantizedllamamodel, swift, swiftdata, swiftui

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for instameme

## Body

Gallery Camera Capture Inspiration Memes are one of the fastest ways people communicate online — quick, expressive, and sometimes painfully accurate. But creating them usually involves jumping between apps or relying on cloud-based AI tools. I wanted something faster and more personal: an app that could generate memes instantly, without needing the internet. With the rise of on-device AI and the MLX framework, this was the perfect opportunity to prove that creativity can happen locally on ARM64 — fast, private, and fun. What it does InstaMeme lets you take a photo (or pick one) and instantly turn it into a meme — all on-device. The Vision framework identifies what’s in the image and a quantized Llama model running with MLX generates short, meme-style captions. You can remix the text, browse past creations, and export a final, burned-in meme ready to share anywhere. No servers, no uploads, no waiting. 📱⚡ How I built it I built InstaMeme using SwiftUI, SwiftData, and Apple’s Vision framework for object recognition. Caption suggestions come from an MLX-powered LLM running locally on ARM64 using a quantized Llama model. All rendering and image processing — including export with burned-in text — happens on-device through a mix of SwiftUI and Core Graphics. The result is a lean, self-contained system where everything from inference to persistence stays local. Challenges I ran into The biggest challenge was managing image memory while integrating AI inference and exports. Early builds crashed when sharing large camera photos because the share sheet duplicated image buffers. Resizing intelligently and optimizing the rendering pipeline fixed that. Getting MLX and Vision to work smoothly together in a clean SwiftUI architecture also took some iteration. Accomplishments that I'm proud of I’m proud that everything runs locally — no external AI services, no dependencies, and no Internet required. Seeing the first on-device caption appear instantly (and hilariously incorrectly) was a great milestone. Watching the workflow tighten into something fast and intuitive feels like a solid step toward real, production-quality on-device AI creativity tools. 🎉 What I learned On-device AI isn’t just possible — it’s genuinely practical now. Between MLX, Vision, and Apple Silicon, it’s amazing how far inference and generation can go without the cloud. I also learned a lot about structuring SwiftUI apps that balance UI responsiveness, storage, and ML workloads. What's next for InstaMeme Next up: an iMessage extension for inline meme generation, sticker packs, GIF support, and personality modes (wholesome, chaotic, sarcastic corporate, etc.). Longer term, I'd love to explore personalized on-device fine-tuning so captions reflect the user’s humor over time. 😎 <div