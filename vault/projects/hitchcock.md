---
slug: "hitchcock"
url: "https://devpost.com/software/hitchcock"
title: "lossfunk"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 409
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# lossfunk

> Hitchcock: You call the shots - an AI-based film generator powered by Open Deep Research, Fal and ElevenLabs

[Devpost](https://devpost.com/software/hitchcock) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**substrate** [[code_repository]] [[video_visual]]

**stack** elevenlabs, fal, mahilo, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hitchcock

## Body

hitchcock architecture a shot from a film made on pandas a shot from a film made on humans on mars a shot from a film made on humans on mars Inspiration We love film-making and wanted to explore how good the current systems can be stretched to make films. In the team, we have people with varied tech interests and that pushed us to experiment with things like multi-agent systems, video generation, and more! What it does Given just a prompt, Hitchcock's multi agent system will first research about your input and make sure that the script it writes for your story is accurate in terms of cultural, historical and scientific context. It then details the scenes in your story and identifies the right shots to use for them. A DOP agent, powered by Fal.ai, then translates these scenes into realistic and accurate images and then runs a feedback loop with the Story Board agent to finalize the scenes. A Narrator Agent, powered by Eleven Labs then adds the right audio to the video and syncs it together. How we built it We built the multi-agent architecture using an open-source project called mahilo. For the scene and image generation, we used Fal.ai while the audio was provided by Eleven Labs. The front-end is built in React. Challenges we ran into Making the LLM outputs in the agent consistent with the schema we wanted was a challenge and we used the instructor library for it. There were also challenges with the video size, number of scenes to generate and maintaining consistency across frames. We also spent considerable time speeding up the video generation pipeline, through directly using ffmpeg in our code. Accomplishments that we're proud of Making the multi agent system work reliably Maintaining consistency in the characters in the film Speeding up our whole application Integrating all media-- image, text and audio in a limited timeframe. What we learned Models should be in a different class in Python to avoid circular import hell Never push to main when you have multiple people working. Video generation takes time (still running) What's next for Hitchcock Virtual Writers’ Room: Foster real-time ideation sessions with AI-assisted script suggestions, enabling creative teams to ideate on dialogue. Micro-Cinematics: Faster production of short-form content for platforms like TikTok or Reels, maintaining high production value in condensed formats. Storyboard-to-Screen: Transform initial outlines into animated storyboards, offering directors and producers quick previews before committing to full production. <div