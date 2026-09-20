---
slug: "ezspeak-30hy1w"
url: "https://devpost.com/software/ezspeak-30hy1w"
title: "EzSpeak"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 573
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# EzSpeak

> Breaking language barriers, one word at a time!

[Devpost](https://devpost.com/software/ezspeak-30hy1w) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]]
**substrate** [[transcript_audio]] [[web_dom]]

**stack** azure, azurecognitiveservices, chrome, chromeextensionapi, css, html, javascript, webaudioapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ezspeak

## Body

logo Pop-Up of EzSpeak Chrome Extension EzSpeak Settings (for dev) Inspiration We built EzSpeak because of how diverse the world we live in truly is! Living in Miami (one of the most diverse places in the WORLD ) - surrounded by a vibrant mix of cultures, ethnicities, and constant language switching - its hard to make that connection with everyone when you are face with language barriers. However, the EzSpeak team took that as challenge to lower the barriers between people who don’t share a native tongue. As globalization and digital interconnectedness accelerate, we believe everyone should have the ability to talk to anyone, anytime, anywhere! What it does EzSpeak listens to the audio from your current browser tab. The audio is sent securely to Microsoft Azure Cognitive Services Speech, which powers: Speech‑to‑text (captions) Translation (your chosen language) Text‑to‑speech (optional AI voice) Results appear in Chrome’s Side Panel so you can read along and, if you want, hear the translated voice. How we built it We built EzSpeak mainly using JavaScript, which handles everything from capturing audio to updating the UI. It uses Chrome’s tabCapture API to grab sound from the active tab, then processes it with the Web Audio API to downsample it into the right format for Azure. JavaScript streams these audio chunks to Azure’s Speech SDK using async functions and listens for the real-time responses. As transcripts, translations, and AI voice data come back, JS updates the Chrome side panel instantly and plays audio if enabled, while also saving user settings like language in chrome.storage. Challenges we ran into A challenge we ran into was determining the right model to use. AI is a new and upcoming tool that is constantly changing, and the topic the project is related to is very fresh. With limited resources and tools to use, it made live translations and the creation of the AI voice very difficult. We scrapped a lot of original planning and had to come up with new solutions with limited time. However, with pure determination and relentless research / problem solving we decided to go with the Azure AI speech resources due to the AI speech solutions it offers Accomplishments that we're proud of We are proud of the whole project, as well as the idea itself. This wasn't just a hackathon project for us, but instead it was a real idea that we had a lot of passion for, even way before we even wrote a single line of code. This project allowed us and others to be able to speak to people to others, who naturally had a tough time speaking to, and break those barriers for the first time. What we learned There were so many new thing learned such as software and new tools. However, for the majority of us this was our first hackathon. So the main thing we learned from this experience was working in a group of new people, as well as working in a time crunch. This squeeze of pressure is what gave us that extra push to go the distance and finish this project. What's next for EzSpeak Better AI voice timing for tighter synchronization with the original speaker. Automatic AI voice selection by analyzing speaker characteristics; optional manual voice selection per session. On-the-fly language detection: auto-switch translation target and AI voice when the spoken language changes, no extension restart needed. Multi-speaker, multi-language meeting support speaker separation, per-listener language output. <div