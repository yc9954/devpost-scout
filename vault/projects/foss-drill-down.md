---
slug: "foss-drill-down"
url: "https://devpost.com/software/foss-drill-down"
title: "FOSS Drill Down"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 292
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/security_privacy"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# FOSS Drill Down

> Search, analyze, and monitor libs/packages, OCI images, and git repositories

[Devpost](https://devpost.com/software/foss-drill-down) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[security_privacy]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what i learned
- what's next for foss drill down

## Body

Inspiration It is actually inspired by repology site but with a wider scope. What it does Search, analyze, and monitor libraries (from package registry), OCI images , and git repositories. How we built it I actually have been bookmarking several API docs from various registries on my phone. So it just a matter of cherry-picking and of translating it to a postman collection. Challenges we ran into I give up on using Visualizing responses 😫 (more specifically on visualizing the dependencies graph) It also crashes a lot. Especially when I edit some fields like environment variables and request parameters. Accomplishments that we're proud of Naming the API collection using emojis and non-renderable Unicode to manually sort it 🤣 What I learned Postman workspace is handy for managing and prototyping API but the scripting APIs are really lacking since you can't use ES and/or Commonjs Module. Also, the folder, request, and example don't operate the same way as the file system. For example, you can't create a symbolic link to a folder or a request. If you bit creative, you can also use the monitoring API to watch if a package or version has been yanked, updated, or reported for vulnerabilities. What's next for Foss Drill Down Implement them as pure PWA (no backend and/or server-side code) If you need more detail (or want to collaborate), feel free to contact me. After this hackathon, I plan to move the development to github and not maintain this workspace anymore. Sorry that I don't have enough interest to fully document this workspace. Feel free to make a PR or just fork it 😣 (if you have a cool logo to be used for this project, feel free to comment it in the workspace 😄) <div