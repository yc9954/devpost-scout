---
slug: "graph-goose-your-teamwork-graph-mapped-to-the-real-world"
url: "https://devpost.com/software/graph-goose-your-teamwork-graph-mapped-to-the-real-world"
title: "Graph Goose — Your Teamwork Graph mapped to the real world!"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 439
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Graph Goose — Your Teamwork Graph mapped to the real world!

> Turns your Teamwork Graph 🌐 into interactive 3D models from industry-standard OBJ files — built for automotive, manufacturing, and any workflow with real-world parts. 🛠️ Bring your entities to life!

[Devpost](https://devpost.com/software/graph-goose-your-teamwork-graph-mapped-to-the-real-world) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**substrate** [[geospatial]] [[web_dom]]

**stack** forge, typescript

## How they structured the write-up

- inspiration
- what it does
- challenges i ran into
- accomplishments that i’m proud of
- what’s next for graph goose
- important notes

## Body

Allows sophisticated reporting via dashboard gadgets. Highlights the relevant nodes in your current Jira context! Supports industry standard formats! Inspiration In manufacturing and automotive industries, teams work with complex systems made of many components. While Jira tracks tasks and assets well within the Teamwork Graph, there’s no native way to visualize these tasks in real-world 3D models . Graph Goose solves this. It connects Jira entities to interactive 3D models, letting teams instantly see which parts of a machine, car, or system are affected by a task. Most importantly, the app: Supports industry-standard OBJ files ✅ Visualizes complex workflows across multiple Forge modules 🔌 Runs entirely on Atlassian Forge, thanks to the new Forge Object Store 🛡️ What it does Graph Goose maps your teamwork graph entities 🌐 directly to interactive 3D models. When a Jira task involves multiple systems, the app highlights relevant model parts dynamically. A 3D editor lets administrators map nodes of 3D models to different queries A filter view integrates with Rovo after (JQL) filter generation to visualize the results of work item queries Work items affecting multiple components highlight the corresponding parts in the work item view A dashboard gadget with flexible filter configurations allows dynamic color mapping for reporting Challenges I ran into Rendering 3D models efficiently with three.js was tricky. There is not much space for complicated view control elements so it should behave naturally just by offering 'navigate on double-click'. The app runs entirely on Atlassian, but during the Object Store EAP it needs to allowlist the storage host currently used internally by Atlassian. permissions: external: fetch: client: - 'https://tdp-os.services.atlassian.com' This can and will be removed before the production release. ☑️ Accomplishments that I’m proud of Connecting the libraries to the Forge Object Store was a tricky task. It works by using signed urls that are passed down from the Forge backend. What’s next for Graph Goose Support for AQL is already in progress Upcoming Teamwork Graph APIs will allow support for more object types I’m happy to provide more feedback on the Object Store EAP and plan to publish Graph Goose to production as soon as the Object Store leaves EAP towards public preview! Thanks for reading! 🦢 Cheers, Julian Important Notes Right now the app is only fully functional in the Forge preview environment , because the Forge Object Store EAP does not allow uploading or downloading files in production yet. The app also needs to allowlist an Atlassian host for the time being, since it relies on the EAP. This is a temporary limitation and can be removed once the Object Store is ready for production: https://tdp-os.services.atlassian.com/ <div