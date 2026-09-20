---
slug: "notehacks-bsjdoi"
url: "https://devpost.com/software/notehacks-bsjdoi"
title: "NoteHacks"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 258
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# NoteHacks

> Automate your notes so that you can focus on listening :)

[Devpost](https://devpost.com/software/notehacks-bsjdoi) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[video_visual]]

**stack** convex, groq, openai, opencv

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for notehacks

## Body

Taking notes in real time! Convex dashboard Inspiration Ever found yourself struggling to keep up during a lecture, caught between listening to the professor while scrambling to scribble down notes? It’s all too common to miss key points while juggling the demands of note-taking – that’s why we made a tool designed to do the hard work for you! What it does With a simple click, you can start recording of your lecture, and NoteHacks will start generating clear, summarized notes in real time. The summary conciseness parameter can be fine tuned depending on how you want your notes written, and will take note of when it looks like you've been distracted so that you can have all those details you would have missed. These notes are stored for future review, where you can directly ask AI about the content without having to provide background details. How we built it Backend + database using Convex Frontend using Next.js Image, speech, and text models by Groq Challenges we ran into Chunking audio to stream and process it in real-time Summarizing a good portion of the text, without it being weirdly chopped off and losing context Merge conflicts T-T Windows can't open 2 cameras simultaneously Accomplishments that we're proud of Real-time speech processing that displays on the UI Gesture recognition What we learned Real-time streaming audio and video Convex & Groq APIs Image recognition What's next for NoteHacks Support capturing images and adding them to the notes Allow for text editing within the app (text formatting, adding/removing text, highlighting) <div