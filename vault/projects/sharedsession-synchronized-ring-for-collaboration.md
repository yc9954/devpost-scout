---
slug: "sharedsession-synchronized-ring-for-collaboration"
url: "https://devpost.com/software/sharedsession-synchronized-ring-for-collaboration"
title: "SharedSession: Synchronized Ring for Collaboration"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 841
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# SharedSession: Synchronized Ring for Collaboration

> Turn your Logitech MX device into a shared, permission-scoped control surface for real-time remote collaboration.

[Devpost](https://devpost.com/software/sharedsession-synchronized-ring-for-collaboration) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** css3, html5, javascript, logitech-actions-sdk, node.js, typescript, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for sharedsession: synchronized ring for collaboration
- built with

## Body

Inspiration Remote collaboration is broken in one specific way: navigation control. Every day, millions of remote workers sit on video calls saying "can you scroll up?", "go back to that slide", "zoom into that corner." Whether it's a code review, a design walkthrough, or a client presentation — the reviewer has zero control over what they're looking at. They're passengers, not participants. Screen sharing solved visibility. But navigation? That's still completely broken. We looked at Logitech's MX hardware — the precision ring, the tactile buttons, the Actions SDK — and realized this is the perfect physical interface to finally solve it. Not with software-only hacks, but with a real, tactile collaboration layer that no one has built before. What it does SharedSession is a Logitech Actions SDK plugin concept that lets two remote collaborators share specific, non-destructive device controls over a secure session. Here's the idea: One person hosts a session from their Logitech device and gets a session code The other person joins as a reviewer using that code from their own device The reviewer's ring and buttons are now mapped to safe actions on the host's machine — scrolling, zooming, navigating between sections, highlighting elements An on-screen overlay shows both users what the reviewer is doing in real-time The core innovation is the permission system. When a host creates a session, they choose what the reviewer can do: Permission Level Allowed Actions Use Case VIEW Scroll, pan, zoom Reading code together NAVIGATE Jump between sections, switch pages Reviewing a document PRESENT Control slides, spotlight cursor Co-presenting CONTROL_MEDIA Volume, play/pause, scene switch Stream moderation Destructive actions like edit, undo, and delete are never available to the reviewer — by design, not by accident. The plugin simply won't send those commands. How we built it We've designed the architecture and built a working proof-of-concept that demonstrates the core interaction model: Plugin Layer: Designed around the Logitech Actions SDK for Node.js, using CommandActions for button presses and AdjustmentActions for ring rotations. The SDK integration points are mapped out and ready for real hardware. Sync Layer: A WebSocket-based sync server handles session creation, joining, permission validation, and real-time event relay between host and reviewer. Permission Engine: A role-based permission system that scopes actions by category (VIEW, NAVIGATE, PRESENT, CONTROL_MEDIA) rather than individual actions — making it intuitive for both users. Web Dashboard: A browser-based prototype that simulates the full host-reviewer flow, including session creation, code sharing, virtual ring controls, and a live action feed — so we can demonstrate the concept without requiring two physical Logitech devices. We intentionally built the architecture so the simulator layer can be swapped for real hardware input with zero code changes. The Actions SDK integration is a clean interface swap, not a rewrite. Challenges we ran into The hardest design problem was the permission system. We needed to find the balance between giving the reviewer enough control to be genuinely useful, while making it impossible to cause damage. Scoping permissions to action categories (VIEW, NAVIGATE, PRESENT) instead of individual actions was the breakthrough — it's intuitive for the host to grant and natural for the reviewer to understand. We also had to think carefully about the real-time sync model. Actions need to feel instant — any perceptible lag between the reviewer rotating their ring and the host's screen scrolling would break the experience. WebSocket with minimal payload serialization was the right call. Accomplishments we're proud of We're proud that the concept is simple enough to explain in one sentence ("your Logitech ring controls my screen, safely") but architecturally deep enough to scale to real enterprise use cases. The permission system is genuinely novel — no existing collaboration tool scopes physical device control this way. We're also proud of the proof-of-concept dashboard. It demonstrates the full session flow — create, join, control, observe — in a browser, making the idea tangible and testable without requiring hardware. What we learned The biggest insight: the best collaboration tools don't give everyone equal power — they give everyone the right power for their role. SharedSession works as a concept because it respects ownership while enabling participation. That principle guided every design decision. We also learned that Logitech's Actions SDK is genuinely well-suited for this kind of multi-device interaction model. The separation of CommandActions and AdjustmentActions maps perfectly to the host/reviewer paradigm. What's next for SharedSession: Synchronized Ring for Collaboration Our roadmap to take this from concept to product: Full Logitech hardware integration — connect the proof-of-concept to real MX Creative Console and MX Master4 devices via the Actions SDK Multi-participant sessions — expand beyond 2 users to support team reviews and classroom settings Per-application permission profiles — different defaults for VS Code vs Figma vs PowerPoint Haptic feedback — the reviewer's device vibrates when their action is received on the host side Video conferencing integration — embed session controls directly into Zoom, Teams, and Meet Enterprise features — team management, session analytics, and admin-controlled permission policies Built With Logitech Actions SDK (Node.js) TypeScript WebSocket (ws library) Node.js HTML/CSS/JS (dashboard prototype) <div