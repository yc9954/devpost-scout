---
slug: "go-home-you-re-drunk-nawgm0"
url: "https://devpost.com/software/go-home-you-re-drunk-nawgm0"
title: "Thunderstroke"
hackathon: "HackZurich 2021"
organization: "HackZurich"
winner: true
words: 243
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
---

# Thunderstroke

> Capture a real-time video from your device and jam with your friends wherever they may be. Did we mention you'll be playing air guitar and the instruments alike? Zero lag guaranteed.

[Devpost](https://devpost.com/software/go-home-you-re-drunk-nawgm0) · hackathon [[HackZurich 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]]

**stack** c#, jitsi, mediapipe, midi.js, python, rtpmidi, tensorflow, udp, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rage against the goat

## Body

Just jamming Inspiration We dream of jamming with our friends. Musicians, tone-deaf - anyone! We do not want to compromise when it comes to lag. We want real-time audio and real-time visuals! What it does It captures user gestures from the cam and lets you play various "air" instruments. At the same time, the body landmarks are sent to the immersive 3D environment. How we built it We use Python and various libraries to capture the cam's video, find body posture hand landmarks with AI, recognize gestures based on the instrument and submit the smallest package possible over to the music and video server. We do not transmit audio waves but rather MIDI messages. These are transferred over the RTP-MIDI protocol. So everyone gets the signal, and it is also run through the server's synthesizer for later playback. We used Unity for the 3D world. The body landmarks are transmitted by UDP at about 30 frames per second on the CPU. Challenges we ran into WiFi can be a huge bottleneck for the speed, even if the throughput is good. Getting everything to work at once is not for the faint of heart. Accomplishments that we're proud of amazing teamwork task alignments running prototype the triangle What we learned MIDI messages are more asynchronous in their nature than it first meets the eye. What's next for Rage Against the Goat Make the solution easily deployable and jam with our friends of course. <div