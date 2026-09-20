---
slug: "path-25fs8o"
url: "https://devpost.com/software/path-25fs8o"
title: "HAVEN"
hackathon: "RevenueCat Shipyard: Creator Contest "
organization: "RevenueCat"
winner: true
words: 773
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "substrate/geospatial"
---

# HAVEN

> FIND HOME ON THE ROAD.

[Devpost](https://devpost.com/software/path-25fs8o) · hackathon [[RevenueCat Shipyard- Creator Contest]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[transportation]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** nativewind, revenuecat, stack:-react-native-/-expo-sdk-52, supabase-(postgresql-+-realtime-+-storage-+-edge-functions), zustand

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for haven

## Body

Haven — Project Story Inspiration I've been nomadic for nine months. Before that, I'd travel for months between jobs — in sedans, vans, overlanding rigs, with friends, family, and solo. I've had incredible experiences, but the honest truth is that a lot of the time you are by yourself, and that can be incredibly hard. I find myself constantly craving community and connection, which is one of the hardest things to meaningfully do on the road. The app is named Haven after someone I met by chance in a Walmart parking lot while traveling. We ended up hiking out of the parking lot to a cliff to watch the sunset, then spent a week on the road together — one of those rare connections that only happens when paths cross unexpectedly. Haven exists to make those moments intentional instead of accidental. What It Does Haven is a utility-first mobile app for van lifers and digital nomads — a central hub for managing your travels and building community on the road. The core feature: you plan your route, other community members plan theirs, and Haven shows you where and when your paths will cross. It's not "who's near me right now" — it's "who's going to be where I'm going." From there, community members can create activities — campfire hangouts, group hikes, surf sessions — with host-approved RSVPs and auto-created group chats. They can also post feelers, low-friction broadcasts that say "I'm going to be in Joshua Tree next week, who's around?" and let people reach out directly. Between crossing paths, activities, and feelers, there's always a way to turn proximity into connection. Free users get solo utility tools (interactive map, spot saving, trip planning). Community features unlock via invite codes or membership application, keeping the space curated and safe. Two RevenueCat subscription tiers add pro map overlays ($2.99/mo) and a full Hinge-style dating experience ($9.99/mo) with prompts tailored to van life and matching that prioritizes people on your upcoming path. 31 screens. Real-time messaging. Dating. Trip planning. Spot management. Invite codes. Community moderation. One app. How I Built It Five days. One person. Claude Code Opus 4.6 with three sessions running constantly 4-6 hours a day. Stack: React Native / Expo SDK 52, Supabase (PostgreSQL + Realtime + Storage + Edge Functions), RevenueCat, NativeWind, Zustand. No team, no designer, no backend engineer — just me orchestrating agents and making product decisions as fast as I could. Challenges I Ran Into Prioritization was the real challenge. Every hour mattered across five days, and deciding what to build next, what to cut, and what was "good enough" required constant judgment. Managing three parallel agents meant nonstop context-switching — reviewing one agent's output while prompting another and debugging a third. Claude Code's inconsistency was another factor. Some sessions it's a genius, some sessions it makes baffling decisions. Learning when to trust the output became a skill in itself. Finally — selling it. I know what I built and why it matters. But translating a deeply personal product vision into a compelling demo video for people who've never slept in a van is a completely different skill than building the product. Accomplishments That I'm Proud Of The crossing paths algorithm — finding overlapping travel nodes within 50 miles, computing match scores from shared interests, and surfacing it all in clean, actionable cards. It's the heart of the app. The two-axis access model (community tier × subscription level) that lets free users get real value while keeping premium features and community curation in balance. 31 screens with real-time messaging, dating, and RevenueCat integration — one person, five days. What I Learned AI-assisted development is real but it's not autopilot. The product spec was the most important artifact — when Claude had a detailed spec & made a plan to implement it, output quality jumped. Breaking it down into phases was also critical, each phase would review the previous and integrate the requested features and architecture. Managing multiple agents is its own emerging skill: knowing which tasks parallelize cleanly, how to sequence dependencies, and when to slow down and consolidate. What's Next for Haven It's a solid MVP. Core flows work, data model is sound, feature set is comprehensive. Not ready to scale today — needs push notifications, performance work, Android, and moderation tooling. There are lots of items on the roadmap, including a dedicated builder marketplace. Regardless of the hackathon outcome, if nobody else builds something better for this community, I'm launching it. The van life community deserves a purpose-built tool, not another generic social app with a camping filter who sells out with ads or paywalls. <div