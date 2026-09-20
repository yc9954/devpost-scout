---
slug: "fireview"
url: "https://devpost.com/software/fireview"
title: "Fireview"
hackathon: "Zero to One Hackathon by Convex Vol 2"
organization: "Convex"
winner: true
words: 482
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Fireview

> Notion for your application data

[Devpost](https://devpost.com/software/fireview) · hackathon [[Zero to One Hackathon by Convex Vol 2]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]] [[government_staff]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** clerk, convex, next, stripe, tailwind, vercel-ai-sdk

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fireview

## Body

Welcome to Fireview Customizable document detail drawers Notion style filters for your application data Generate dashboards or views with natural language Link any collections and subcollections Aggregations on any collection field Inspiration With Fireview we want to solve the shortcomings we faced with Firestore while building previous startups and apps for clients . Every time, we ended up building bespoke admin apps to visualize and manage data inside our database, and struggled to answer the simplest questions about our application data. We stumbled across Convex through Antonio’s Notion tutorial on YouTube, which we used as a way to learn web development and have some building blocks we could use for Fireview. What it does Currently, Fireview enables Firestore (low-code) developers & teams build admin dashboards in minutes instead of days. Users can easily connect their Firebase project and Fireview infers the schema of their no-SQL collections and lets users view it in a Notion-inspired multi-player, intuitive and modular fashion. It’s also possible to create dashboards entirely through natural language, by making use of Fireview’s AI agent which is schema-aware. How we built it Our stack is: Convex (database, functions, secrets) Clerk for auth + organization management Vercel for deploying to staging and prod Stripe for subcriptions Vercel AI SDK for AI features Next JS (App Router) Tailwind CSS To keep track of our progress and what we developed during the hackathon timeline, check our updates page Challenges we ran into Too many to list honestly, but developing with Cursor and getting quick help from the Convex team on Discord was invaluable. Sometimes we just needed guidance but sometimes the Convex team actually pushed fixes in record time to unblock us. Accomplishments that we're proud of Fireview has gone from idea to paying customers in less than 4 months! User testimonial: “Had to build a completely custom set of dashboard pages for a mobile app for user management, app feedback, user reporting, etc. It took several hours of development + testing. I recreated the dashboard in Fireview in literally 2 minutes and it essentially has more functionality because I can easily edit if needed without a deploy and can 1-click edit documents.” What we learned The list is too long: React Next Convex Optimistic updates Zod to Convex Webhooks with http actions Migrations Node vs Convex runtime Database wrappers Function auth wrappers Clerk auth and organization management Vercel AI SDK Agent with tools that interact with Convex directly What's next for Fireview Our vision with Fireview is to do to databases what Notion did to knowledge bases. Our dream would be to see non-technical people building dashboards using natural language, marketers creating social media material directly based on milestones reflected in their application data, founders creating pitch decks as shareable Fireview pages, PMs creating internal reports and presentations based on Fireview’s visual components synced in real time to their Firestore/Hubspot/Stripe data, etc. <div