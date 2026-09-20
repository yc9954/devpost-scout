---
slug: "vibe-director"
url: "https://devpost.com/software/vibe-director"
title: "Stu3dio"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 241
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/video_visual"
---

# Stu3dio

> Make a film by talking to 3D workers in the studio

[Devpost](https://devpost.com/software/vibe-director) · hackathon [[Hack the North 2025]]

## Facets

**domain** [[labor_employment]]
**substrate** [[video_visual]]
  <sub>weak: geospatial</sub>

**stack** fastify, nextjs, react, supabase

## How they structured the write-up

- what it does
- how we built it

## Body

Character artist inside our 3D studio Scene editing 3D map to navigate around the studio Character editing Script Writer! Time line creation before video generation Director! What it does Make an AI movie by talking to others in the 3D studio. First, chat with an Director to brainstorm ideas, build characters, and outline scenes. Secondly, collaborate with an Scriptwriter to flesh out dialogue, actions, and narrative details. Next, meet the Character Artist, where you can tweak style, clothes (ANYTHING YOU WANT) by simply scribbling on the character’s image for instant AI edits. Lastly, view a timeline of all the scenes and their frames, you could edit the scene images directly using scribbling tools and getting instant responses from our image gen AI. Finally ... generate the video ... VoiLa! Your very own AI movie is built! How we built it Projects & Nodes – Each film is a project with a tree of nodes (logline, characters, objects, scenes, final film). Editing a parent marks descendants as stale so they regenerate with fresh context. Only required context is passed when generating each node. Generation Jobs – Every AI action (LLM plot, character sheet, image, video, final stitch) is a generation, queued as a job in Redis. Workers pick jobs, call providers (LLM, image, video), and store results and artifacts. Artifacts – JSON descriptors, images, frame stills, scene clips, and the stitched film are all stored as downloadable artifacts in blob storage. <div