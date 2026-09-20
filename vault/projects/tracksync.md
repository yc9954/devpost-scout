---
slug: "tracksync"
url: "https://devpost.com/software/tracksync"
title: "Tracksync"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 533
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Tracksync

> The github for music.

[Devpost](https://devpost.com/software/tracksync) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[web_dom]]

**stack** fastapi, ffmpeg, gitpython, javascript, lmms(open-source-c++), postgresql, python, react, supabase, tailwind-css, wavesurfer.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tracksync

## Body

Landing page All projects view Repo overview Conflict resolution (1) Conflict resolution (2) Issues Board Inspiration Most of our team are familiar with creating music, and we often work on co-producing tracks with friends. When using conventional collaboration methods, we found that the current ways of remotely collaborating on tracks were slow, inefficient and ultimately lacked version control. This created the inspiration for a software that would allow users to seamlessly collaborate and easily share track versions without the constant hassle of re-downloading and re-uploading songs. Additionally, the ability to easily refer to past song versions was needed, especially when working across multiple or large projects. What it does At its very core, tracksync is essentially the git for music co-production. Currently, remote co-production relies on constantly downloading and uploading files, where there is a severe lack of version control and convenience. Our solution, tracksync solves these issues with a track-level version control system where producers can push changes with commit messages, pull the latest version of a project, review collaborator changes via side-by-side audio waveforms, work on a project concurrently and resolve conflicts by listening to different versions before deciding which to keep. Our team made the decision to remove command line git arguments and replace them with buttons that automate the process. We did this to lessen the barrier to entry and create an easy to use software with a clearcut user interface. How we built it After coming up with the idea, we went through a long process of planning a detailed PRD where we specified the core features of our software, the tech stack and how we would actually implement it. We also included website pages, the flow of our website and what open-source music editing software we could use. Once we finished planning, we worked on actual implementation. We set up FastAPI, GitPython and Supabase to actually enable pushing and pulling. We then built the react frontend so the core demo flow worked in the browser. Finally, we modified LMMS to call our backend. Challenges we ran into Our biggest challenge was figuring out how we would actually apply git commands to audio files given that git is a text based diffing system. We also had to figure out how to alter LMMS and link it to our backend. Accomplishments that we're proud of We are proud that our group came together, and ultimately got our project working! After long hours of focused planning, difficult implementation and debugging, our project correctly emulates git's features and functions but for audio files. We also thought that removing the complex command line commands was a good idea to cater to the technological needs of our target audience. What we learned We learned a lot about how git actually works and how to handle binary file versioning. We got a lot of exposure to using Wavesurfer.js, FFmpeg, FastAPI and Supabase. We also had fun modifying LMMS to fit in with our backend. What's next for Tracksync In the near future, we plan to add user authentication, support for more DAWs beyond LMMS and real-time notifications for pushes. This is actually something we plan to use when making music with our friends! <div