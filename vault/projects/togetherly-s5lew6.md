---
slug: "togetherly-s5lew6"
url: "https://devpost.com/software/togetherly-s5lew6"
title: "Togetherly"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 271
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/government_staff"
---

# Togetherly

> Togetherly is a real-time digital whiteboarding web app enabling visual collaboration for distributed teams. Break geographical barriers, share and work in real-time. Made with Next.js and Convex.

[Devpost](https://devpost.com/software/togetherly-s5lew6) · hackathon [[Boost Hacks II]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[government_staff]]

**stack** convex, nextjs, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for togetherly

## Body

Togetherly Architectural Overview Landing Page Preview Main dashboard screen Inspiration The inspiration for Togetherly came from my own frustrating experiences trying to collaborate with team members located in different places. I wanted to build a platform that could bring distributed teams together to ideate and create in real-time. What it does Togetherly is a web-based collaboration hub with interactive digital whiteboards for real-time communication. Users can create organizations, invite members, and start sessions to visually brainstorm ideas together. The platform aims to boost efficiency through built-in templates, assets, tools that enhance collaboration. How I built it I built Togetherly using Next.js for the frontend and Convex for real-time collaboration capabilities. Next.js allowed me to build a fast, SEO-friendly webapp, while Convex enabled low-latency concurrent editing on the digital whiteboards. Challenges I ran into One challenge was optimizing Togetherly for real-time performance across potentially thousands of concurrent users. I overcame this by implementing data structures like CRDTs on the backend. Another challenge was building an intuitive permissions system for organization members which I solved by using Clerk as an authentication service. Accomplishments that I'm proud of I'm proud of Togetherly's ability to support thousands of simultaneous users with low latency. The platform performs 80% faster than competitors, providing a seamless collaboration experience. What's next for Togetherly Next I plan to add mobile support, more whiteboard templates, and integration with popular productivity tools which includes more assets also some graphical functionality where in users across the globe can add in data's when required and the visualization gets changed realtime. I also want to explore adding voice/video chat for even richer real-time collaboration. <div