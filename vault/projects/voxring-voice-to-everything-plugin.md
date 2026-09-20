---
slug: "voxring-voice-to-everything-plugin"
url: "https://devpost.com/software/voxring-voice-to-everything-plugin"
title: "VoxRing - Voice-to-Everything Plugin"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 445
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# VoxRing - Voice-to-Everything Plugin

> Press. Speak. Done. Voice-to-everything for MX Master 4 and MX Creative Console. You already know how to talk. VoxRing just makes your computer listen, and do something about it.

[Devpost](https://devpost.com/software/voxring-voice-to-everything-plugin) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[voice_speech]]
  <sub>weak: developer_tools</sub>
**substrate** [[transcript_audio]] [[web_dom]]

**stack** c#, dotnet, dpapi, html, javascript, logitech-actions-sdk, naudio, piper, vosk, whisper, yaml

## How they structured the write-up

- five boxes a day
- press. speak. done.
- built into the hardware, not onto it
- what actually ships
- where it goes
- one more thing

## Body

Five boxes a day Every day, the same thought goes into five different boxes. A message. An email. A note. A calendar invite. A reply. The keyboard isn't slow. You are, moving between windows, hunting for the right app, breaking your own train of thought to tell the computer where the words should go. Voice tools exist. None of them solve this. Dictation apps transcribe beautifully into the wrong place. Assistants answer questions but can't send a message. Extensions work in one app and nowhere else. Nothing bridges the gap. That's what VoxRing is trying to do. Press. Speak. Done. This is the first version of VoxRing. It's early. But it already does something no other plugin does. The idea is simple: your words land where you meant them to - Slack, email, Notion, Teams, Discord, Calendar, WhatsApp, Telegram, or the clipboard. Nine destinations. One gesture. No window switching. No keyboard. No cloud. The trigger? A button on the side of your MX Master 4. Built into the hardware, not onto it VoxRing isn't a voice app with a keyboard shortcut bolted on. The side button runs push-to-talk with short-tap and long-hold detection on the same button, separated by timing alone. The haptic motor fires seven distinct feedback events so you know the state of your message without looking. The Creative Console becomes a live voice control surface - dB meter, waveform, word count, and a nine-destination grid. What actually ships Thirty-three actions across eight sidebar groups. Offline transcription through Vosk and Whisper - you pick the engine. AI formatting through a provider-agnostic interface, toggleable per action. Voice Assistant with Piper read-back and multi-turn conversation history. Seven haptic events. Live dB, waveform, and word count on the Creative Console. Piper and voice models bundled, no external installer. API keys encrypted at rest with Windows DPAPI. This is a first-version plugin. WhatsApp and Telegram currently work through clipboard-and-URI handoff rather than native APIs. Contact resolution, wake-word, calendar write-back, and macOS support are on the roadmap, not in this build. Nothing is faked. What you see in the demo is what installs on your machine. Where it goes Native integrations for the destinations still on fallback. Contact-aware email dictation. Calendar events that create real events, not URLs. macOS parity. A wake-word so the side button becomes optional and VoxRing moves from a peripheral feature to an ambient one. Voice is the fastest interface you already know how to use. VoxRing is one plugin today. With time, it becomes a category and the side button becomes to voice what the scroll wheel became to browsing. One more thing I also built a guitar tuner. Because I could. <div