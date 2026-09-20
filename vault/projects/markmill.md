---
slug: "markmill"
url: "https://devpost.com/software/markmill"
title: "MarkMill"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 556
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/legal_professional"
  - "user/small_business"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MarkMill

> MarkMill is an AI-powered marketing agency in a box: it crawls your site, designs data-backed campaigns, makes posts, and schedules them—launch a pro-level campaign in minutes, no agency needed.

[Devpost](https://devpost.com/software/markmill) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]]
**user** [[legal_professional]] [[small_business]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** amazon-ec2, amazon-web-services, css, django, gemini, html, javascript, nginx, openai, openai-agents-sdk, python, route53, sqlite, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for markmill

## Body

dashboard Ask to create campaings campaign generations from request campaing details view campaing details content section detail post page generated video for a post content review approvals campaing list calendar page asset library personal asset upload company settings also made admin page logo Inspiration While building previous projects, I constantly hit the same wall: marketing . Agencies quoted $10 K+ for a single, modest acquisition campaign and took weeks to deliver. I eventually jury-rigged my own DIY campaigns, but the experience convinced me there had to be a faster, cheaper, automated way. That realization sparked MarkMill an AI-driven, plug-and-play marketing agency you launch with nothing more than your website URL (its pretty cool ;) ). What it does MarkMill orchestrates 10+ specialized AI agents (OpenAI + Google Gemini) to handle the entire campaign lifecycle: Full-stack research – Playwright scraping + LLM analysis extract your brand voice, products, audiences, and competitors. Strategy design – Agents brainstorm and rank multi-channel campaign options, complete with KPIs and rationale. Content production – Copywriters, designers, and a video agent generate posts, graphics, and 8-second promo videos. Scheduling & launch – A calendar view slots content at optimal times; assets are stored and ready for one-click rollout. In short, MarkMill is a marketing team in a box instant, data-driven, and always on. How we built it Backend: Django + Gunicorn + Nginx Agents: OpenAI Agents SDK coordinating >10 GPT-4o agents for research, strategy, copy, design, and optimization Scraping: Playwright & BeautifulSoup for dynamic site crawl and llm processing with pyantic structure and openai-agents-sdk Media: Google Gemini VEO-2 for video generation; image via OpenAI image models Infra: deployed on AWS EC2 behind Route 53 ; custom domain markmill.co registered on GoDaddy CI/CD: GitHub → EC2 ; environment variables via AWS Challenges we ran into Scale & scope: Solo-built in 30 hrs—threading agents, async tasks, and UI without blocking the demo. Video quality: Gemini VEO-3 isn’t public with api yet; VEO-2 lacks music and HD, so generated clips will be better next month when veo3 is released publicly https://gemini.google/overview/video-generation/?hl=en Deployment hurdles: Nginx reverse-proxy rules, SSL, and security groups had to be ironed out at 3 a.m. to get the live domain running smoothly, very difficult for me. Accomplishments that we’re proud of End-to-end functionality: From URL input to finished multi-channel campaign with real copy, images, and video. Live production deploy: Judges and hackers can hit markmill.co right now and generate a campaign. (or www.markmill.co ) Real-world impact: Another SpurHacks team already used MarkMill to draft their own marketing assets during the event! What we learned Deep dive into the new OpenAI Agents SDK —structured outputs, tool calls, progressive hand-offs. Hands-on with Gemini video APIs and their current limitations. Practical lessons in rapid AWS deployment, domain management, and keeping an LLM-heavy stack responsive under tight time limits. What’s next for MarkMill Use our own product: Run MarkMill to market itself and onboard early users. Upgrade media quality: Adopt Gemini VEO-3 (or equivalent) for HD video + audio once released. Team collaboration tools: Multi-user workspaces so marketers and founders can co-review and approve assets in real time and also full analytics cycle, the infra is there. Vision: democratize pro-level marketing so any founder, freelancer, or local shop can launch world-class campaigns—instantly and affordably, to try to make the world a better place with their products! <div