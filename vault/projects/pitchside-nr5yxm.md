---
slug: "pitchside-nr5yxm"
url: "https://devpost.com/software/pitchside-nr5yxm"
title: "Pitchside"
hackathon: "United Hacks V7"
organization: "Hack United"
winner: true
words: 455
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/media_journalism"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Pitchside

> The football archive you can walk into.

[Devpost](https://devpost.com/software/pitchside-nr5yxm) · hackathon [[United Hacks V7]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[media_journalism]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** blender, c#, css, glsl, next.js, python, react, statsbomb, three.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for pitchside

## Body

homepage broadcast view fly view tps view tps view stats + commentary leagues how matches demo : my demo video keeps getting blocked by Fifa 💀 - hopefully this video works 😭 live at : pitchside-united.vercel.app github : public github repo Inspiration Football has one of the richest archives of any sport but everything before the streaming era survives as grainy clips, box scores and stories. Luckily, StatsBomb's Open Data stored every pass, foul, shot and stat from around 4,000 real matches, going back to the 1958 World Cup final and using this, I decided to rebuild the broadcast itself from the data and watch Pelé in 1958 or Messi in 2022 like a live game. What it does Pick any of ~3,900 real matches and watch it as a live 3D broadcast. Real players, passes, goals at their real timestamps TV camera + auto-director with slow-mo goal replays; orbit, fly, follow, and first-person POV cameras Era time machine: newsreel grain for 1958, Technicolor for 1970, VHS for the 90s, with era-voiced commentary Real lineups, subs, cards, stoppage-time minutes, penalty shoot-outs How I built it Next.js + React Three Fiber A reconstruction engine compiles the event stream into dense position/heading/action tracks; the renderer is a pure function of tracks × clock, so scrubbing, rewind, and slow-mo come free Event data has no tracking, so we synthesize it: a possession model glues the ball to the carrier's feet, and every player gets a seeded "persona" (reaction lag, pace, wander) so teams move naturally Blender pipeline for retargeted rigs; baked per-match commentary; procedural crowd audio Challenges I ran into No tracking data: early versions had the ball drifting off feet, defenders moving in lockstep, players frozen like statues. We built motion metrics and iterated until they passed Coordinate frames: StatsBomb coords flip by team and period; one wrong sign teleports the ball 60m Dead time: the clock learned to skip VAR checks while keeping broadcast minutes accurate Accomplishments that I'm proud of The 2022 WC final reconstructs perfectly: 3–3, pens 4–2, every goal at its official minute in the browser Motion realism we can measure: ball within ~1m of the carrier, team lockstep down to real levels The 1958 final in newsreel grain feels like recovered footage Animations and 3d environment UX What I learned Physical constraints (speed caps, turn limits, arrive-on-time movement) beat clever interpolation Verify visuals with numbers — screenshots lie, metrics don't The last 10% of "does it feel like football?" is 90% of the work What's next for Pitchside Recognizable players (jersey names, headline-player presets) Tactical overlays: pass networks, xG timelines, formations on the pitch One-click clip export of any goal, any camera, any era More sports as open positional data appears <div