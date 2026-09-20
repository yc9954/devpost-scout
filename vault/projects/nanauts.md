---
slug: "nanauts"
url: "https://devpost.com/software/nanauts"
title: "The Nanauts"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 500
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# The Nanauts

> Connect with AI explorers from a distant galaxy in mixed reality as they survey our world using hands, voice, scene understanding and Llama 3.3

[Devpost](https://devpost.com/software/nanauts) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]] [[legal_professional]]
**substrate** [[geospatial]] [[video_visual]]

**stack** handtracking, hittest, iwsdk, llama3.3, passthroughcameraaccess, webaudioapi, webxr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nanauts

## Body

Modem, Blit and Baud: The Nanauts Inspiration My game was inspired by Walt Disney’s example of trying to harness the latest in emerging technology to create characters and stories with real heart. Therefore my goal lately has been to incorporate AI services for unique gameplay. What it does As earth’s goodwill ambassador to The Nanaunts, you help three cute little robot explorers understand our culture and way of life by exploring your environment in mixed reality, answering their questions, and aiding in their quest for understanding, with the Professor guiding your experience. How we built it from a base Immersive Web SDK project for its many common XR components used Immersive Web Emulator for rapid iteration in the browser used Meta Quest scene understanding to dynamically construct a navmesh for the robot agents to navigate according to crowd sim, flocking and game rules used Passthrough Camera Access to generate custom environment maps Gave the player the ability to speak directly to the characters, using a serverless Meta Llama 3.3 endpoint hosted on AWS, which can judge the intent and emotional sentiment of speech given certain game conditions Two interaction modes using either controllers or hand tracking with natural microgestures. Used the WebXR Hit Test API to get real depth to open portals on tracked surfaces. Navigation-driven procedural animations to impart character, weight and life to each unique bots, using classic animation techniques like stretch & squash, leading with the eyes, and follow-through The UI and robots also have exclusively procedural Web Audio API “voices” which can be imputed with emotion (like “sad,” “inquisitive,” “mad”) with basic musical input I also voiced the narrator, and created an anime-style viseme UV scroll player to mouth any audio narration I fed in. Challenges we ran into I attempted to leverage SAM 3 and SAM-3D-Objects AI models (released mid-November) to recognize and react to more objects in the real-world ( https://www.linkedin.com/feed/update/urn:li:activity:7399101129554419712/ ) but camera intrinsics on Quest browser are still experimental, and I ran into challenges with accuracy, and on a short timescale, I ultimately pivoted the concept to rely on core Quest technology + the more reliably and widely-available Llama. Accomplishments that we're proud of I completed all technical and creative work on my own in only three weeks, starting November 21. I’m proud of not only have having that design and creative intuition, but being an engineer who can see it through. What we learned I learned more about how to develop and design AI services for innovative gameplay versus solely production efficiencies. What's next for Nanauts I’d love to win the contest and have a good reason to keep investing in the technology and title, as I see tremendous possibilities for work and play in interacting with increasingly-intelligent virtual beings in your real-world environment as new AR glasses and computer vision solutions become available in coming years. I could see this becoming a virtual pet title, like a "mixed reality Tamagotchi," encouraging replayability. I want to design for that future. <div