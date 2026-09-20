---
slug: "grindstone"
url: "https://devpost.com/software/grindstone"
title: "Grindstone"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 244
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Grindstone

> A Mastra AI-Agent powered goal tracker that gamifies your goals.

[Devpost](https://devpost.com/software/grindstone) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

  <sub>weak: developer_tools, labor_employment</sub>
**substrate** [[structured_db]]

**stack** ai-sdk, cloudflare, d1, eventskit, gemini, mastra, nextjs, openai, swift, swiftui, workers

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for grindstone

## Body

Inspiration Other apps were focused on habit tracking (like drinking water), not customizable smart goals. They didn't set real milestones or suggest features, and they weren't fun to use. What it does You can input a rough goal and use the Mastra agent to refine it to an achievable goal with specific start and end dates, and then use Mastra to further refine that into a SMART goal with specific milestones. The agents are aware of your specific schedule and workload (using EventsKit), and take that into account when building each milestone. How we built it We used Next.js with Mastra for the backend and SwiftUI for the frontend, using Cloudflare for hosting and the database, and Gemini and OpenAI for agentic capabilities. Challenges we ran into Figuring out how the agent could search the user's reminders and calendar to determine their workload was extremely tricky. We landed on an approach that synced the user's events to our database and created a tool using the Mastra framework that allowed the agent to fetch events. Accomplishments that we're proud of We were able to build this in 24 hours (late start!) with beautiful hand-drawn illustrations into something that we're proud of. What we learned We learned a lot more about the Mastra framework, but mainly about building quickly. What's next for Grindstone We want to expand if the interest is there and add all of the features we thought of! (stats, trackers, joining others) <div