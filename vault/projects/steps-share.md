---
slug: "steps-share"
url: "https://devpost.com/software/steps-share"
title: "Steps Share"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 350
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Steps Share

> Steps tracker with Social: friend groups, weekly leaderboards/challenges Gamified: streaks & badges KMP: shared UI

[Devpost](https://devpost.com/software/steps-share) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[video_visual]]

**stack** cmp, compose-multiplatform, kmp, kotlin

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for steps share

## Body

Inspiration I noticed friends comparing step counts in a WhatsApp groups screenshots, jokes, and dares flew back and forth. Engagement skyrocketed the moment movement became social, yet everyone still relied on one-player pedometer apps. That disconnect sparked Steps Share : a tracker where accountability is baked in from the first tap. What it does Live Progress Ring updates with every step. Friend Duels overlay your graph against a friend’s in real time. Custom Goals for steps, calories, distance, or minutes. Trend Dashboards (unlocked via RevenueCat Pro) show weekly and monthly deltas with badges: 🟢 ↑, 🔴 ↓. Privacy-First Sync — only friends you invite can see your stats, nothing is posted publicly. How we built it Layer Tech Notes UI / Logic JetBrains Compose Multiplatform One Kotlin codebase → Android & iOS Data Sync Firebase Auth + Firestore 3 sub-collections: users/{uid}/friends , duels , goals Subscriptions RevenueCat Paywall + analytics in < 2 hours Health Data Google Fit (Android), HealthKit (iOS) Bridged via KMP expect/actual Open Source MIT-licensed core engine on GitHub steps-share-oss repo Challenges we ran into HealthKit vs. Google Fit permission timing caused race-conditions on cold launch. Balancing privacy with real-time syncing—solved by listener throttling and Firestore security rules. Time-zone drift in duels; normalized all leaderboard queries to UTC midnight. Accomplishments that we’re proud of 22 % average step increase among 250 closed-beta users after adding just one friend. Shipped the first Pro paywall in under 48 hours, thanks to RevenueCat. Community-led PRs merged from Brazil 🇧🇷, Germany 🇩🇪, and Jordan 🇯🇴 within two weeks of open-sourcing. What we learned Compose MP is production-ready; animation glitches were edge-cases, not blockers. Users value clarity over complexity —a single live ring beat four earlier dashboard mock-ups. Open-sourcing early brings free QA, localization help, and evangelists. What’s next for Steps Share Apple Watch & Wear OS complications for wrist-first logging. Group Challenges —rooms of up to 20 friends with weekly leaderboards. Offline Buffer for hikers: queue up to 24 h of steps before sync. We’re just getting started—join the repo, fork a feature, or simply lace up and duel us! <div