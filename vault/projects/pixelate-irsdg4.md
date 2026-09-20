---
slug: "pixelate-irsdg4"
url: "https://devpost.com/software/pixelate-irsdg4"
title: "pixelATE"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 903
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/security_privacy"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# pixelATE

> Reality is overrated. Pixel it instead.

[Devpost](https://devpost.com/software/pixelate-irsdg4) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[security_privacy]]
**substrate** [[geospatial]] [[video_visual]]

**stack** camera, django, gemini, godot, google, google-cloud, google-generative-ai, google-storage, insomnia, livestream, numpy, pillow, python, requests

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pixelate

## Body

Rohil with a cape! Gatik on a motorcycle! Inspiration Rohil and Gatik wanted to reimagine the creative process in games. What if your in-game avatar was literally you, stylized through generative AI? With tools like Nitrode accelerating Godot-based development and large multimodal models now at our fingertips, we saw an opportunity to create an immersive, personalized experience that bridges art, AI, and interactivity. What it does pixelATE lets players capture themselves using their in-game camera and transform that image into a stylized, playable character, all on the fly. Players can regenerate appearances, add fantasy elements (like a cape or even riding a dragon!), or completely remix their look with a single keypress. We developed 2 key functionalities. Press G to snapshot yourself and become part of the world. Press C to customize with AI-driven options. It’s playable, dynamic, and deeply personal. How we built it We used Nitrode, a Godot wrapper optimized for AI-native gameplay, as our foundation to rapidly iterate on the game mechanics and world design. From there, we built an end-to-end pipeline that moves a single user interaction (pressing G) through a complex flow involving visual capture, latent diffusion, and dynamic asset reinjection. When the player hits G, the in-game camera captures a raw RGB screenshot of their avatar. This image is encoded client-side using image.encode_png_to_buffer() and sent over HTTPS to a Django-based backend. The backend routes the image through a Python FastAPI inference microservice. We utilized OpenCV and Pillow for preprocessing tasks such as resizing, denoising, and contour extraction. A latent diffusion pipeline powered by a pretrained custom Stable Diffusion model. This was fine-tuned on fantasy character datasets using LoRA embeddings, which generate the stylized output. Simultaneously, image embeddings are passed to Google Gemini’s multimodal endpoint to enrich prompt injection and improve stylistic coherence between facial structure and fantasy augmentations. Once the diffusion model returns the generated image (1024x1024 resolution), it is base64-encoded and transmitted back to the client. On the client side, we decode and reformat it as a .png texture using a custom module for performance. The texture is converted into a dynamic Godot sprite sheet, then compiled into a .tres asset in real time, allowing it to be seamlessly injected into the Nitrode player scene without requiring engine restarts. Customization options are layered with prompt modifiers and vector-based overlays. For instance, saying “add a cape” activates a modifier module that chains a second-stage prompt to the latent diffusion pipeline, mixing it with object segmentation to add accessories precisely. Challenges we ran into Integrating a real-time backend with Nitrode required several custom solutions. We developed our own asset injection scripts to dynamically update the game state as new data came in. Working with Gemini’s API introduced challenges such as rate and payload size limits, which meant we had to carefully compress and resize images while maintaining visual quality. Converting raw base64 image data into usable Godot assets also presented edge cases, requiring robust decoding logic and fallback caching to ensure reliability. One of the most complex aspects was coordinating the timing to make sure that the AI-generated assets could load mid-session without disrupting the flow of gameplay took significant fine-tuning. Accomplishments that we're proud of One thing we are really proud of is building a fully dynamic character transformation system that lets players customize AI-generated characters in real time. With no restarts, no reloads. It was a complex challenge that involved live integration with Google Gemini through a backend we built from scratch, all while keeping the experience smooth and responsive. We layered in customization so players could keep iterating on their characters mid-game, and it all runs on Nitrode, which made it possible to pull off this kind of real-time AI interaction. Seeing it come together and actually work in a live setting here at Cal Hacks was incredibly rewarding. What we learned One big takeaway for us was that AI has the potential to enable truly personalized gameplay experiences. This is only possible if you can get the latency and asset pipeline under control. We learned that combining tools like Nitrode and Godot with external services can be incredibly powerful, but real-time processing between them requires careful, precise engineering to keep things smooth. Working with multimodal AI like Gemini was also eye-opening; it’s great for transforming images, but it takes smart prompting and thoughtful image handling to get consistent results. Looking ahead, we’re excited about adding voice interaction. This could make the creative process feel even more natural, especially when paired with AI agents. What's next for pixelATE Next up for pixelATE, we’re aiming to make the experience even more fun and intuitive. We’re integrating voice-powered customization so players can just say things like “give me a flaming sword” or “make me look like a space pirate” and see it happen in real time. We’re also going to be working on a multiplayer mode, so you and your friends can play as personalized avatars together. On the tech side, we’re excited to bring in Groq’s inference to power batch generation with virtually zero lag. We’re planning to launch on Itch.io soon, complete with curated customization packs to help players get started. And to top it off, we hope to be opening up a modding API so the community can create their own transformation prompts and build on what we’ve started. We’re just getting going, and there’s a lot more we can’t wait to build! <div