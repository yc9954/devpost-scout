---
slug: "hall-of-us"
url: "https://devpost.com/software/hall-of-us"
title: "Hall of Us"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 423
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Hall of Us

> Hackathons move fast, and it’s easy for moments to slip away. Hall of Us lets you capture photos, enhance them, and relive them in an immersive Quest 3 museum where every memory becomes an exhibit.

[Devpost](https://devpost.com/software/hall-of-us) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**domain** [[media_journalism]]
  <sub>weak: developer_tools, finance_payments</sub>
**substrate** [[structured_db]] [[video_visual]]

**stack** cedar, langchain, metaxr-sdk, next.js, openai, postgresql, react, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hall of us

## Body

Cheeto Guy with VR Cheeto Guy (shoutout daniel) Inspiration Hackathons fly by. Between coding, meeting sponsors, and collaborating with teammates, the best moments often get lost. We wanted a way to capture those experiences and bring them back to life—not just as photos on a phone, but as immersive, shared exhibits everyone can explore. That’s how Hall of Us was born: a mixed reality museum of memories. What it does Hall of Us is a two-part experience: A web app where users upload photos and videos. AI automatically tags and captions them. A Quest 3 mixed reality app where those memories are transformed into spatially anchored exhibits placed throughout the hackathon venue. This includes near the sponsor booths, judging tables, and working spaces. Visitors can filter memories, explore curated exhibits, and even use natural language prompts to surface specific types of content. How we built it Frontend: React for the web app, with AI-powered tagging/editing features integrated through Cedar. Backend: FastAPI type-safe Pydantic models, and a PostgreSQL database hosted on our own backend server. Storage: Amazon S3 for photos and videos, organized by user and tag. Deployment: Our own VPS with Coolify to support easy deployment. XR App: Unity + Quest 3 to build the immersive museum environment, anchored by predefined spatial tags tied to the AI-generated metadata. Challenges we ran into Designing a clean pipeline for AI tagging and storage while keeping user data secure. Getting Quest 3 spatial anchors to align with real-world areas of the hackathon venue. Bridging three ecosystems—web, backend, and XR—so they all share the same data models and authentication. Balancing technical scope with hackathon time limits. Accomplishments that we're proud of Building a seamless workflow where a photo can move from web upload → AI enhancement → VR museum exhibit. Making the XR experience feel natural, like walking through a curated gallery of memories. Creating an extensible architecture that could easily be reused for conferences, meetups, or other events. What we learned How to tie together mixed reality development with modern web tooling and backend APIs. The importance of aligning AI outputs (tags, captions) with human expectations. Practical lessons in designing for collaboration—our type-safe API setup allowed frontend, backend, and XR to evolve in parallel. What's next for Hall of Us Supporting video exhibits alongside photos. Adding personalization features like “show me only my team’s memories.” Scaling beyond hackathons to conferences, festivals, and even personal events like weddings. Exploring persistent museums that you can revisit after leaving the event, turning shared experiences into lasting immersive archives. <div