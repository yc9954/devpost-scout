---
slug: "startupos"
url: "https://devpost.com/software/startupos"
title: "startupOS"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 614
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/small_business"
---

# startupOS

> Scale your business with faster authentic hiring and real outbound, not ai

[Devpost](https://devpost.com/software/startupos) · hackathon [[LA Hacks 2026]]

## Facets

**domain** [[finance_payments]] [[labor_employment]]
**user** [[small_business]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for startupos

## Body

page1 2 3 4 5 6 Inspiration Many of my friends are entrepreneurs. The ones who move fastest are good at finding reliable pockets of labor, keeping costs low, and constantly managing projects without adding too much overhead. That inspired startupOS: an AI-first operating system for small businesses to create work, find verified workers, and coordinate teams that can form quickly and securely. What it does startupOS helps small businesses create and manage jobs, campaigns, projects, and chat channels from one workspace. On the org side, users can create jobs and campaigns manually or through an AI agent. They can also manage projects, invite teammates, chat in channels, and generate basic video/ad campaign packages. On the mini app side, World-verified users can onboard, upload resume/profile fields, browse jobs, auto-apply through a browser agent, complete campaign tasks, and message organizations. The core loop is: Org creates work -> AI/form turns it into a job, campaign, or project -> verified users see it in the mini app -> users apply, complete tasks, or chat with the org How we built it We built startupOS as a full-stack monorepo. The backend uses Express, TypeScript, Prisma, PostgreSQL, and Supabase object storage. The org frontend and mini app are both built with React and TypeScript. We integrated World/MiniKit for verified mini app login, Browserbase/Stagehand for job auto-apply flows, OpenAI for agent/object creation, and ElevenLabs for narration in the video campaign workflow. The AI chat can create structured jobs, campaigns, and projects, then return a button linking directly to the editable object. Challenges we ran into The hardest part was connecting two identity systems: org users on the web app and World-verified users on the mini app. It was also challenging to make AI output become real product state instead of just text. The agent needed to create validated jobs, campaigns, projects, links, statuses, and editable cards. We also ran into production migration issues, browser-agent reliability problems on real job boards, and the design challenge of making both the org dashboard and mobile mini app feel polished. Accomplishments that we're proud of I’m proud that we built a real loop, not just separate screens. An org can create a job or campaign from AI chat, open the generated object, publish it, and have it appear in the mini app. We also built project-based chat channels, persistent messaging, World-user onboarding, resume/profile storage, campaign task flows, and the start of a video-to-campaign workflow. The strongest pieces are: hiring for World-verified users project-based teams and chat fast campaign and job creation through forms or AI What we learned We learned that the best use case is not generic “AI productivity.” It is helping small businesses create real work and coordinate real people. We also learned that agents become much more useful when they have structured tools. A chat agent that can create a job, publish a campaign, or update a project is far more valuable than a chatbot that only answers. The mini app also needs to lead with money-making opportunities. Jobs, campaigns, tasks, and payouts are much easier for users to understand than abstract productivity features. What's next for startupOS Next, I want to expand the agent layer with many more tool calls through systems like Composio. I also want to deepen the World-worker marketplace: service listings, job applications, campaign proof, secure org messaging, and Worldchain-compatible payments. On the org side, projects should become full control rooms with assets, links, chat, tasks, campaign state, generated video packages, and agent-readable context. Long term, startupOS should let a business owner describe what they need, have agents structure the work, hire verified people to execute it, and manage the whole project from one workspace. <div