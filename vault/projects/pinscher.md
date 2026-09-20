---
slug: "pinscher"
url: "https://devpost.com/software/pinscher"
title: "Pinscher"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 355
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Pinscher

> Working with your computer is pretty tedious and manual, what if it wasn't? Pinscher allows users to seamlessly present and use their computer to do tasks such as go over slides, documents and more!

[Devpost](https://devpost.com/software/pinscher) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[document_pdf]] [[web_dom]]
  <sub>weak: video_visual</sub>

**stack** electron, gemini, javascript, marpcli, opencv, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Overview of features and Gemini AI Features Start presentation, create slide deck, summary and show core features Configuration settings for gesture action, detector and camera Inspiration Working with a computer is a serious of tedious, manual clicks and keystrokes. We wanted to make the digital experience feel more like a superpower. We set out to build Pinscher: a system that turns your natural gestures and voice into a direct bridge to your operating system. What it does Pinscher is an AI-powered OS controller that lets you run your Mac hands-free. Vision Control: Use index-thumb pinches to click and drag, or ring-finger swipes to switch browser tabs. Voice Intent: Natural language processing that doesn't just transcribe, it understands. Say "Summarize this meeting," and Pinscher records, transcribes, and generates a PDF. Gemini Intelligence: A "Presenter Assistant" that generates slide decks (Marp) and speaker notes automatically from your recorded video sessions. Accessibility: Includes dwell-click and sticky-key modes for users with limited mobility. How we built it We built a multi-process architecture to handle real-time data streams: Frontend: A slick Electron dashboard for device configuration and gesture tuning. Backend: A Python core managed by Poetry, utilizing OpenCV for hand tracking and Vosk for offline-capable speech-to-text. Intelligence: Integrated the Gemini 2.0 Flash API to parse complex user intents and perform multi-modal video summarization. OS Link: A custom bridge that translates Python logic into low-level Mac system events for mouse and keyboard control. Challenges we ran into Learning how to set up Electron for the first time Dependency issues regarding Vosk, which can work on certain versions of Python and processors Accomplishments that we're proud of We successfully scrolled through a document and switched apps using nothing but a hand gesture We were able to play Wordle without touching our keyboard Creating a command that records a demo, muxes it, and generates a formatted PDF slide deck in under 60 seconds What we learned Multimodal is difficult to manage Cursor anchors is more feasible since holding up your hand for long can be tiring in real life ## What's next for Pinscher Make it compatible across all other OS systems <div