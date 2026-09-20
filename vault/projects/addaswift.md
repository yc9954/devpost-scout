---
slug: "addaswift"
url: "https://devpost.com/software/addaswift"
title: "AddaSwift"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 234
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# AddaSwift

> Smarter clicks that make every action faster, across every site

[Devpost](https://devpost.com/software/addaswift) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[media_journalism]]
**substrate** [[geospatial]] [[web_dom]]

**stack** c#, chrome, javascript, webmcp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Inspiration We spend most of our working hours in the browser - Gmail, GitHub, Notion, Figma. The Actions Ring is great for desktop apps, but every time we switched to the browser, it failed to impress. Same generic shortcuts, no awareness of context. We wanted the ring to follow us into the web. What it does AddaSwift makes the Actions Ring context-aware for websites. On Gmail, the ring shows Archive, Snooze, Compose. On GitHub - Merge PR, Request Review. On Notion - New Page, Search. It also surfaces bookmarks and quick-launch links. Everything configures through Logitech Options+. How we built it An Actions SDK plugin built on PluginDynamicCommand that updates the ring at runtime based on the active browser tab. A bridge layer - a desktop app paired with a Chrome extension - communicates browser context to the plugin. We reach websites through three stacking layers: native keyboard shortcuts, DOM element targeting, and WebMCP integration. Challenges we ran into The web has no universal API for "what can I do here." Mapping the static ring to dynamic web content while keeping it responsive was the central design challenge. Accomplishments that we're proud of Contextual ring updates that feel immediate as you switch tabs. What we learned PluginDynamicCommand is more flexible than it first appears. The gap between what users can do on a page and what's programmatically accessible is exactly why WebMCP matters. <div