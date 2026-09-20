---
slug: "community-chats"
url: "https://devpost.com/software/community-chats"
title: "Community Chats"
hackathon: "Reddit Mod Tools and Migrated Apps Hackathon"
organization: "reddit"
winner: true
words: 610
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/transportation"
  - "substrate/video_visual"
---

# Community Chats

> Reviving Chat Channels with Devvit App , With Better Moderation tools than native Chat Channels , A Chat space where Subreddit's Automod and Reddit native filters apply directly.

[Devpost](https://devpost.com/software/community-chats) · hackathon [[Reddit Mod Tools and Migrated Apps Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[transportation]]
**substrate** [[video_visual]]

**stack** devvit, react, typescript

## How they structured the write-up

- important disclaimer
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for community chats

## Body

Important Disclaimer This project began as a non-functional, pre-hackathon concept. It was completely revived during the event after a moderator from the r/RCB community reached out with interest. Over the course of the hackathon, every line of code was written entirely from scratch, transforming the initial idea into a fully operational application with all necessary features implemented. Inspiration When Reddit sunsetted its public chat channels, communities lost their primary hubs for real-time interaction. Legacy chat spaces often suffered from chaotic environments and lacked the robust moderation tools required for active management. To bridge this gap, Community Chats was built on the Reddit Devvit platform. The application delivers a seamless, instant messaging experience equipped with powerful, native moderation tools. By leveraging AutoMod and native Reddit filters, the app automates safety compliance, allowing moderators to maintain an engaging community space with minimal manual overhead. What it does This application embeds an inline Webview directly into a Reddit post, creating an instant-load chat space. Users can participate immediately from their feeds or expand the view to access advanced features like swipe-to-reply and enhanced UI performance. How we built it Backend & API: Reddit Devvit Platform, TypeScriptReal-Time Infrastructure: Devvit Real-Time Capabilities (for instantaneous data syncing) Frontend: Responsive Webview (optimized for fluid inline layout and swipe actions) Challenges we ran into Developing an application of this scale introduced unique technical hurdles, primarily regarding platform compliance and real-time moderation. Devvit requires every chat message to be reportable. To solve this, the architecture saves each chat message as a native Reddit comment within a pinned thread. This design choice enables AutoMod and native Reddit filters to evaluate and instantly delete policy-violating messages. Beyond compliance, the focus was equipping moderators with tools to manage high-traffic events. The application introduces comprehensive controls, including chat slow-down modes (15s to 60s), instant room lockdowns, and a global toggle to disable image attachments. Finally, user experience was enhanced by rendering native subreddit user flairs and emoji reactions directly inside the instant-load chat space Accomplishments that we're proud of We are incredibly proud to see the application scale from an initial concept to a vital piece of community infrastructure. The app has proven its reliability by successfully powering live, high-traffic events, most notably during high-intensity sports events like the RCB & SRH cricket matches. Beyond large-scale sports entertainment, the application has been adopted by diverse subreddits such as r/bihar and r/real_teenindia. In these spaces, it serves as a secure, real-time hub that successfully brings thousands of community members together under an automated, safe, and engaging chat environment. What we learned Building this application taught me the critical importance of meticulous, detail-oriented design when engineering for real-time social spaces. In a public live chat, unpredictable situations are the norm; you must design for every possible edge case to prevent system abuse. Through direct collaboration with community teams, we uncovered the deep stress and operational bottlenecks caused by legacy chat channels that lacked proper controls. This experience taught us that user-facing features are only half the battle. True product success relies on robust backend automation that empowers moderators to confidently step away, knowing the system will handle compliance seamlessly in their absence. What's next for Community Chats Our future roadmap focuses on enhancing user expression while drastically tightening real-time safety controls. On the engagement front, we plan to roll out full support for animated user flairs to give chat spaces more personality. To protect communities, we are developing an automated, in-app anti-harassment filter [1]. Additionally, we will streamline administrative workflows by introducing direct, one-click user banning from the chat interface, alongside a native peer-to-peer reporting system to help community members self-regulate the space effectively. <div