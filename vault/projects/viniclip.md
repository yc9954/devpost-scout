---
slug: "viniclip"
url: "https://devpost.com/software/viniclip"
title: "ViniClip"
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
---

# ViniClip

> An opinionated, automatic video editor that cuts out pauses and errors on the fly. Just press record, ready or not, because you literally cannot make a mistake.

[Devpost](https://devpost.com/software/viniclip) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]]

**stack** ffmpeg, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for viniclip

## Body

Inspiration Ever fumble through a video recording, pause awkwardly, or restart mid-sentence? Typical video editing means recording everything, then spending hours re-recording or cutting out mistakes - but what if your video could edit itself while you recorded? What it does ViniClip is an opinionated, automatic video editor that cuts out pauses and errors on the fly. Record yourself directly in your browser, and ViniClip removes awkward pauses, repeated takes, or any mistake you wish to get rid of instantly. The final product is a video that's ready to post immediately, you can even command the video to be upload to Instagram reels instantly. How we built it Frontend: Vite + React + TypeScript, capturing video with MediaRecorder and audio via an AudioWorklet. Backend: FastAPI with WebSocket communication Speech audio to text: Moonshine Media processing: ffmpeg to trim video/audio streams and segment stitching OpenAI Responses API: function calling to return video pieces to cut and to trigger posting to instagram reels. Challenges we ran into Programmatic video editing: Automatic video editing posed an initial challenge since few well maintained, user friendly ffmpeg interfaces were available. Attempts to interpolate frames between takes presented a trade off between model execution time vs visual realism. Ultimately the decision was made to stick with traditional video edits as processing was near instant, and familiar to users. Agentic AI with custom tools: Although it was simple enough to provide an AI agent with custom built tools, the challenge came with engineering prompts in such a way that the LLM would consistently choose the appropriate tool. Giving the LLM enough context to understand where to make video cuts was an interesting challenge Accomplishments that we're proud of This project enables real-time video editing during active recording sessions. By leveraging asynchronous event queues and frame buffers, we achieve simultaneous processing and editing while the browser streams frames to the server, eliminating traditional post-recording bottlenecks and getting almost instantly edited video. What we learned Multi-threading and event queues ffmpeg Websockets What's next for ViniClip Remove stutters, add subtitles, upload to multiple platforms, allow commands for overlays on the video for visual editing <div