---
slug: "tango-q37d4z"
url: "https://devpost.com/software/tango-q37d4z"
title: "Tango"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 471
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/labor_employment"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Tango

> Siri if it actually worked on your Mac.

[Devpost](https://devpost.com/software/tango-q37d4z) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[labor_employment]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** agent, ai, gemini, groq, openai, python, voice

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tango

## Body

Explains code blocks in seconds Meme your friends in seconds Tango can generate CSVs from website data Recommend events from larger list Tango - Siri if it actually worked Inspiration How many times have you copy pasted something just to put it through an LLM and regurgitate it's answer back where you were? Tango started out as a bridge for clipboard copy and pasting, but grew into so much more. We want a world where you get all the benefits of LLMs without interrupting your workflow. From searching the web to rephrasing and reformatting, or meme generation. Just speak your request and Tango's got your back. What it does Tango is a lively agent that monitors your clipboard and acts on voice commands to increase your productivity. It's like Siri if it actually worked. Your friend sent you a picture you know would make the perfect meme? Take a screenshot and get Tango to add the caption for you. Perfectly timed humour, every time. Want a bit of guidance for the new tech project you're starting? Wondering "What is the Pandas equivalent in Rust," or "how can I implement a live camera in Python?". No need to pause and prompt. Tango will keep you coding. Want a concrete list of whats on in Goose Games? CMD-A (or Ctrl for those linux fiends out there) and get Tango to make it a CSV. No hassle. Trying to avoid using "engineered", "improved", or the dreaded "spearheaded" a fifth time on your resume? Simply copy any word, ask Tango for a synonym, and paste. No more needless and distracting tab switching, thesaurus searching, or chatGPT prompting. Tango is here to enhance how you use your computer. Remove redundant switching, and keep yourself in focus. As the saying goes, it takes two to Tango. How we built it We used Python to build a MacOS-native application with deep integration into the operation system's clipboard and notifications API. We run low-energy Voice Activity Detection (VAD) and hotword/wakeword detection to trigger Tango on user request and route requests through fast LLM providers to manage your clipboard. We used Graphite to collaborate on this project and work asynchronously. Challenges we ran into Voice Activity Detection was hard but we found WebRTC has solid open-source implementations Managing complexity with speed - slow responses are never an option Steering the LLM towards desired output Accomplishments that we're proud of The breadth of tasks that Tango can do How much it feels like what we always wished Siri would be It's fast The tweaking for detecting the wake word and sentence end to ensure speed The fact we want to use it ourselves What we learned Guardrails add exponential latency LLM agents can be really fun when done right What's next for Tango Faster memory, faster searching, and MCP support <div