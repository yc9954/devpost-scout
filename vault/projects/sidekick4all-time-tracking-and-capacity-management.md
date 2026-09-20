---
slug: "sidekick4all-time-tracking-and-capacity-management"
url: "https://devpost.com/software/sidekick4all-time-tracking-and-capacity-management"
title: "Sidekick4All Connecting Teams Across Jira and Calendars"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 492
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "user/developer"
---

# Sidekick4All Connecting Teams Across Jira and Calendars

> Sidekick4All aligns teams by connecting Jira and calendars both ways turning planned work into focus time and meetings into Jira effort giving teams clarity and speed 🏎️ across planning and execution.

[Devpost](https://devpost.com/software/sidekick4all-time-tracking-and-capacity-management) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**domain** [[developer_tools]] [[legal_justice]]
**user** [[developer]]

**stack** atlassian-forge, custom-ui, forge-sql, google-calendar-api, jira-cloud, jira-entity-properties, microsoft-graph-api, nodejs-22, oauth-2-0, react, serverless, typescript, vite

## How they structured the write-up

- sidekick4all is now available on the atlassian marketplace
- about the project

## Body

Connect your work or personal Calendars to Jira using Sidekick4All Easy and Secure Setup with support for Microsoft and Google Calendars Get insight about your current workload - directly within Jira Track Time in multiple ways and get insights about where are spending the most of your time GIF Available on the Atlassian Marketplace Sidekick4All is NOW available on the Atlassian Marketplace View on Atlassian Marketplace About the project Inspiration Across marketing, sales, HR, support, and legal teams, we kept seeing the same problem: Work is planned in Jira, but it happens in calendars. Meetings consume time that is never logged, while Jira tasks lack protected focus time. This leads to misalignment, inaccurate reporting, and slow decision-making across teams. We built Sidekick4All Connecting Teams Across Jira and Calendars to reduce this gap and connect the two worlds where work really happens. What it does Sidekick4All connects teams by synchronizing Jira and Google or Microsoft calendars in both directions: Jira issues create calendar focus blocks to protect time for work Calendar meetings are automatically captured as Jira worklogs Planned time and actual effort stay aligned Manual timesheets and follow-ups are no longer required This gives business teams clarity and speed by aligning what is planned with what actually happens. How we built it Sidekick4All is built as a Forge-native Atlassian app designed to feel like a natural extension of Jira rather than an external integration. Key building blocks include: Jira issue events to detect when work should be scheduled Forge UI for configuration and team preferences Secure Forge storage to manage calendar links and synchronization state Event-driven workflows that translate Jira updates into calendar actions and calendar events into Jira worklogs By relying on Forge, we avoided external infrastructure and ensured security, performance, and compliance with Atlassian Cloud best practices. Challenges we faced The main challenge was handling bi-directional synchronization without creating noise or conflicts. Key challenges included: Preventing duplicate calendar events and Jira worklogs Respecting personal and team calendars without being intrusive Balancing automation with user control Designing workflows that work for business teams, not just developers We addressed these challenges through careful event handling, clear ownership rules, and thoughtful defaults. What we learned Building Sidekick4All showed us that productivity problems are rarely caused by missing tools. They are caused by misaligned systems. We learned that: Business teams need automation that works quietly in the background Calendars are a critical but underused source of truth Forge enables powerful, secure, event-driven apps without operational overhead Small reductions in friction can have a large impact on team alignment What's next Sidekick4All is just the beginning. Planned next steps include: Capacity management to help teams understand availability and avoid overload Shareable scheduling links that align Jira work with real calendar availability Rovo agents with multiple actions to proactively schedule focus time and capture work across Jira and calendars Our goal is simple: help teams stay aligned across Jira and calendars, where work really happens. <div