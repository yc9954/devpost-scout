---
slug: "vioke"
url: "https://devpost.com/software/vioke"
title: "Vioke"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 273
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Vioke

> Karaoke anytime, anywhere.

[Devpost](https://devpost.com/software/vioke) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: web_dom</sub>

**stack** html, javascript, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for vioke

## Body

home screen uploading a song sing! Inspiration We both love karaoke, but there are lots of obstacles: going to a physical karaoke is expensive and inconvenient youtube karaoke videos not always matches your vocal (key) range, and there is also no playback existing karaoke apps have limited songs, not flexible based on your music taste What it does Vioke is a karaoke web-app that supports pitch-changing, on/off vocal switching, and real-time playback, simulating the real karaoke experience. Unlike traditional karaoke machines, Vioke is accesible anytime, anywhere, from your own devices. How we built it Frontend The frontend is built with React, and it handles settings including on/off playback, on/off vocal, and pitch changing. Backend The backend is built in Python. It leverages source separation ML library to extract instrumental tracks. It also uses a pitch-shifting library to adjust the key of a song. Challenges we ran into Playback latency Backend library compatibily conflicts Integration between frontend and backend Lack of GPU / computational power for audio processing Accomplishments that we're proud of We were able to learn and implement audio processing, an area we did not have experience with before. We built a product that can can be used in the future. Scrolling lyrics is epic It works!! What's next for Vioke Caching processed audio to eventually create a data source that we can leverage from to reduce processing time. Train models for source separation in other languages (we found that the pre-built library mostly just supports English vocals). If time and resources allow, we can scale it to a platform where people can share their karaoke playlists and post their covers. <div