---
slug: "sqlsidequest"
url: "https://devpost.com/software/sqlsidequest"
title: "sqlsidequest"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 232
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# sqlsidequest

> Learn SQL by solving crimes, not reading textbooks

[Devpost](https://devpost.com/software/sqlsidequest) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

  <sub>weak: developer_tools</sub>
  <sub>weak: developer</sub>
  <sub>weak: video_visual</sub>

**stack** miro, react, sqlite, typescript

## Body

Inspiration: Growing up, I was obsessed with sci-fi, space operas, post-apocalyptic worlds, and even Lovecraftian horror. I always wanted to become a game developer but never got the opportunity to pursue it. So the idea of combining learning with gaming sparked an idea. I wanted to bring that same immersive magic to learning and practicing code. Think of SQL Side Quest as an interactive novel where you don’t just read the story, you drive it forward by writing real SQL queries to solve mysteries. The idea is to make learning SQL fun and engaging. How We Built It: I built the frontend as a Miro plugin using React and TypeScript, with an in-browser SQLite engine powered by sql.js WebAssembly so players get instant query results with zero server round trips. Challenges I Ran Into: One of the biggest hurdles was working with images on the Miro board ,generated visuals from Gemini came back at unpredictable sizes, which caused latency spikes during gameplay. On top of that, Miro enforces a 2MB limit on uploads, so adding GIFs for animated reveals meant we had to compress and resize everything on the fly to stay under that cap without killing the visual quality. Next up, I want to refine our AI prompts so the mysteries feel more compelling , tighter narratives, more believable suspects, and clues that actually make you want to keep digging. <div