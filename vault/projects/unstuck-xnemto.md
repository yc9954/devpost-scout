---
slug: "unstuck-xnemto"
url: "https://devpost.com/software/unstuck-xnemto"
title: "unstuck."
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 510
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# unstuck.

> get your users back on track!

[Devpost](https://devpost.com/software/unstuck-xnemto) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
  <sub>weak: voice_speech</sub>
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** 11labs, cloudflare, fal, gemini, github, hono, lovable, react, supabase, typescript, vite, whisper

## How they structured the write-up

- unstuck: get your users back on track.
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for unstuck

## Body

unstuck in gmail unstack in airbnb unstuck developer dashboard unstuck highlighting an element with the ghost cursor our target users Unstuck: Get your users back on track. unstuck is a 3-line npm package that becomes your website's customer support browser-use agent Inspiration Have you ever received a call from your grandma asking about how to do something on the internet? Have you spent hours trying to explain to your friends how to get to different parts of a website? Have you created extremely simple "intuitive" product flows, only to be disappointed by your users’ confusion? We built Unstuck for moments like these. Inspired by our grandma’s struggles and the universal challenges of navigating websites, we created an AI copilot that seamlessly integrates into any site. Unstuck guides users through complex interfaces using a ghost cursor, voice explanations, and proactive learning. It's an accessibility tool that can be plugged into any website to improve user delight for all - on desktop and mobile! What It Does Unstuck is a drop-in solution that adds a voice and chat interface to your web-app, enhanced by an AI agent that visualizes navigation cues and provides real-time voice guidance. It learns your site’s structure and offers intuitive support for navigation tasks. Developers can use an admin dashboard to see analytics, API management, and domain control, letting them focus on building while we help users get unstuck—effortlessly and empathetically. So, while developers tab, tab, tab away on their IDE, customers can tab, tab, tab, away on websites! How We Built It Using React for the frontend, an agentic LLM built with Gemini for intelligent guidance, and ElevenLabs with an ASR model (through fal) for natural voice interactions, Unstuck wraps websites in a context provider. The dashboard currently helps users create api keys and whitelist domains. We employed lightweight canvas code for visual cues, and with DOM hacking, agentic context handling and smart prompt design, started to see emergent behaviour. Obtaining production websites to try npm packages is hard. So, we created our own - an airbnb clone with Lovable (it's not an exact replica, why overfit). We were able to integrate into the clone site with only a few lines of code, and expect to be publishing our npm package. Challenges We Ran Into Ensuring the ghost cursor and bounding boxes work across dynamic websites, powering the AI agent to run on any website without any prior knowledge of it, and tracking user behavior were key hurdles. Accomplishments That We're Proud Of Creating a user-friendly tool that bridges the digital divide for non-tech-savvy users, delivering a seamless developer experience with one-line integration, and designing an intuitive dashboard for actionable insights. What We Learned We deepened our understanding of AI agent-driven user assistance, website DOM manipulation, and real-time voice synthesis. Agents are genuinely hard to create, but through this process, we learned the best way to build agents end-to-end. What's Next for Unstuck Publishing the npm package, making the workflows easier to record and generate through the admin dashboard, and updating analytics to better reflect usage. <div