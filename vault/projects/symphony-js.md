---
slug: "symphony-js"
url: "https://devpost.com/software/symphony-js"
title: "Symphony.js"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 666
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
---

# Symphony.js

> Symphony.js: Stop looking for bugs, start listening to them! An AI-powered editor that turns your code into real-time generative music.

[Devpost](https://devpost.com/software/symphony-js) · hackathon [[Kiroween]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** kiro, monacoeditor, react, tone.js, typescript, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for symphony.js

## Body

Stating intro splash screen animation Home screen Discordant code & music Intense code & music Harmonious code & music Inspiration Coding is a silent, visual task. We hunt for bugs by staring at text, looking for a tiny misplaced character. The "Frankenstein" category inspired us: What if we stitched together a logical, precise code editor with a creative, generative music engine? We wanted to give developers a new sense. To let them stop looking for bugs... and start listening for them. What it does Symphony.js is an interactive web app that analyzes your code (JavaScript, TypeScript, & Python) as you type and translates its quality into real-time generative music. It features three distinct musical "moods": 🎼 HARMONIOUS: Clean, simple, and well-documented code plays pleasant, major-key music. 🎸 DISCORDANT: Syntax errors and bugs instantly trigger jarring, chaotic, minor-key sounds. ⚡ INTENSE: Complex code (like recursion or deep loops) raises the music's tempo and energy to warn you. It also features a "Play Commit" button to generate a 15-second musical "song" that represents your entire file, and a beautiful animated splash screen to set the audio-visual mood. How we built it Symphony.js was built using Kiro's Spec-Driven Development (SDD) methodology. This was our core strategy. Spec & Steering (The "Brain"): We first authored a Kiro steering file: /.kiro/steering/symphony_vibe.md. This spec is the "brain" of our app. It defines the rules for analyzing code and, most importantly, steers the AI to only respond with a valid JSON object (e.g., { "mood": "HARMONIOUS", "key": "Cmajor" }). Vibe Coding (The "Body"): We then used Kiro to "vibe code" and generate the core logic of our src/services/CodeAnalyzer.ts. This code was generated based on the strict rules from our steering file. Frontend (The "UI"): We built the frontend in React and TypeScript , using the Monaco Editor (the engine behind VS Code) for a familiar editing experience. Audio (The "Soul"): We used Tone.js to create the audio engine. The JSON from the Kiro-generated CodeAnalyzer is fed directly into Tone.js to change the instruments, key, and tempo in real-time. Challenges we ran into Our biggest challenge was a conceptual one: we first thought Kiro was a runtime SDK (kiro-sdk). We were stuck when we found it didn't exist. We then had an "Aha!" moment when we realized Kiro is a development partner meant to generate code, not be called by it. Shifting from a "runtime-call" mindset to a "spec-driven generation" mindset was our biggest hurdle and our biggest breakthrough. Another challenge was music theory: making "DISCORDANT" sound genuinely jarring and "INTENSE" feel energetic, not just loud. This required fine-tuning Tone.js synthesizers. Accomplishments that we're proud of We are incredibly proud of the "Aha!" moment when you first hear a bug . The instant, visceral change from HARMONIOUS music to a jarring DISCORDANT sound is powerful and validates our entire "Frankenstein" concept. We're also proud of the final polish. The animated splash screen, the responsive UI, the "Code Health" panel, and the real-time audio visualizer all came together to make Symphony.js feel less like a prototype and more like a finished product . What we learned We learned the true power of Spec-Driven Development . By defining our AI's output (the JSON structure) first , we saved countless hours of debugging. It forced us to build the "brain" before the "body," guaranteeing they would fit together. We also learned that a "Frankenstein" project isn't just about mashing two things together—it's about the "chimera" creating an unexpectedly powerful new value, which for us, is a new form of debugging and accessibility. What's next for Symphony.js Symphony.js is just the beginning. This concept is too powerful to stay just a web app. The clear next step is a VS Code Extension to bring this audio-feedback loop directly into a developer's native workflow. We also plan to build a "Pro" version with user accounts, custom instrument packs (like '80s Synth' or 'Lofi Beats'), and the ability to export your code's "song" as a MIDI or .WAV file. <div