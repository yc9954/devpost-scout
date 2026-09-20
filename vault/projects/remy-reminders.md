---
slug: "remy-reminders"
url: "https://devpost.com/software/remy-reminders"
title: "Remy Reminders"
hackathon: "RevenueCat Shipyard: Creator Contest "
organization: "RevenueCat"
winner: true
words: 482
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/finance_payments"
  - "substrate/structured_db"
---

# Remy Reminders

> iOS & Android Live Synchronizing Reminders. Snooze Reminders Straight From The Notification! No Need to Open the App. Custom Snooze Times With a Few Button Presses.

[Devpost](https://devpost.com/software/remy-reminders) · hackathon [[RevenueCat Shipyard- Creator Contest]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[finance_payments]]
**substrate** [[structured_db]]

**stack** convex, expo.io, kotlin, revenuecat, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for remy reminders

## Body

Remy Inspiration I really like the challenge of Sam's brief because it's a real world example of him using something on one platform that doesn't exist on another. And when I started to get the idea for a system that synchronizes seamlessly between two different operating systems, I knew I had to go with this brief! What it does this app offers a seamless reminder experience with a great user experience, design, and a pretty complex system in the background that does a full offline-first synchronization engine between different devices and different sources of truth. It offers an easy way for the user to snooze reminders straight from the notifications both on iOS and Android. How we built it iOS and Android both have different ways to integrate system UI into the notifications sheet. So I had to build a custom Swift plugin and a custom Kotlin plugin into my expo React Native application in order to make the UI work on both systems. The synchronization engine is mostly built in JavaScript, but the web hooks and online database come from convex. Challenges we ran into Convex itself does not offer offline-first synchronization, so I had to build that myself. Building native Swift and Android extensions in Expo is also never easy because it's pretty difficult to debug. Those were probably the two biggest challenges. Accomplishments that we're proud of I'm pretty proud of the general design, especially the landing page. remy.spreen.co I feel like in a day and age where everything that's built by AI looks the same, I'm always proud of making designs that look high quality and like there was a lot of attention to detail! I'm also proud of integrating a solid monetization into onboarding, which I know is great for maximizing the amount of people that try the free trial. I'm also happy that I was able to integrate a 50% off offer with RevenueCat on iOS and Android to win back users that did not opt for the trial on the first screen! What we learned this is the first time I built an app in Expo on more than one platform. Previously, I would only use Expo for an iOS app and I've never released an Android app before, so this was an exciting learning. What's next for Remy Reminders there is currently an iOS version that's live on the App Store, which is version 1.0.0, but a lot of improvements have been made. So please review the test slide version, not the live iOS version. I'm also still waiting for Google Play to review version 1.0 that is not live yet at the time of writing. The web version does fundamentally work, but the UI is really mobile optimized right now, so it’s not released yet. A desktop web version powered by RC web payments will be the #1 focus of future development! <div