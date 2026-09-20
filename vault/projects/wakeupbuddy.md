---
slug: "wakeupbuddy"
url: "https://devpost.com/software/wakeupbuddy"
title: "WakeUpBuddy - Transforming Mornings into Lovey Interactions"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 874
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# WakeUpBuddy - Transforming Mornings into Lovey Interactions

> WakeUpBuddy is the world’s first social alarm app that pairs users with friends or strangers. When the alarm rings, one tap triggers an instant call—wake up together or both lose the streak.

[Devpost](https://devpost.com/software/wakeupbuddy) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]]
  <sub>weak: geospatial</sub>

**stack** convex, expo.io, java, kotlin, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wakeupbuddy

## Body

Authentication Screen Home Dashboard Of WakeUpBuddy Alarm Manager Screen Create new alarm, with different modes (solo, random or friend) Leaderboard to enhance user retention (Gamified Approach) Explore other Buddies and Invite for wakeups User Profile and their Wakeup maps User stats based on their Wake-ups Users Achievements Profile Customization to enhance UI/UX User and friend stats together, Tracks both activities Detailed Stats between you and your buddy Notification Screen Our Monetization strategy, additionally also integrated Google Admob WakeUpBuddy – Wake Up With a Stranger Who Cares Inspiration Waking up early is hard for millions of people who rely on alarms that are all too easy to snooze or ignore. Many students, professionals, and people living alone struggle because mornings feel lonely and there is no real social accountability when the alarm rings. WakeUpBuddy was inspired by the idea that a warm human voice and a simple someone is waiting for me feeling can transform wake-up time into something people actually look forward to. People wake up more effectively when someone else is expecting them. What it does WakeUpBuddy is a social wake-up alarm app that automatically matches you with another user who has set an alarm for the same time, then connects you through a real phone call when either of you wakes up. When one person taps I'm Awake , the app triggers an instant call so both buddies can share a short, uplifting morning conversation, turning a lonely alarm into a moment of human connection and motivation. The app supports features like simple alarm creation, optional anonymity ( voice-only ), streaks, buddy stats, and post-call mood or thank-you interactions to make waking up both effective and emotionally rewarding. Key user experience Set your alarm with a simple, minimal interface. Get matched with a wake-up buddy who chose the same time. When either of you wakes and taps I'm Awake , a real call is triggered for a short, positive morning chat. How we built it WakeUpBuddy is built using React Native with Expo to deliver a smooth, cross-platform mobile experience and polished, calming UI animations suitable for early mornings. The backend runs on Convex , which provides realtime database capabilities and serverless functions that handle instant matching, live updates, and wake-up event flows. For reliability, Android Alarm Manager ensures alarms fire on time even in the background, and the native phone dialer is used to trigger immediate voice calls between matched buddies when I'm Awake is pressed. React Native + Expo for cross-platform UI. Convex for realtime data, matching, and serverless logic. Android Alarm Manager and native dialer for dependable alarms and calls. Challenges we ran into A major challenge was designing a reliable matching and call-trigger system that works in realtime, even when devices are locked or apps are in the background. Ensuring alarms fire consistently across devices and then coordinating the instant call flow through the native dialer required careful integration of realtime queries with alarm and telephony APIs. UX-wise, creating a flow that makes users comfortable talking to a stranger while still feeling safe and optionally anonymous demanded thoughtful interface design, permissions handling, and social safety choices. Balancing reliability, privacy, and comfort was one of the hardest parts of the project. Accomplishments that we're proud of The team successfully implemented a seamless set alarm → get matched → wake up → talk loop where a single tap on I'm Awake leads to an immediate, real human call that feels natural and supportive. The app now offers a minimal, calming interface, engaging matching animations, and post-wake-up stats and streaks that reinforce habit formation without overwhelming the user. Building a monetization-ready product with ad placements, a clear premium plan, and a robust engagement loop around social wake-ups is a key milestone the team is proud of. Seamless alarm-to-call flow using real phone calls. Clean, calming UI optimised for early-morning interactions. Built-in monetization with both ads and premium subscriptions. What we learned The project reinforced how powerful human connection is compared to traditional notifications or purely gamified alarms when it comes to behavior change and waking up consistently. The team learned to design systems where realtime backend logic, native alarms, and telephony must work together reliably, and how small UX details can dramatically affect user trust and comfort in stranger-based interactions. It also highlighted the importance of aligning product, retention mechanics, and monetization early so that a wellness and social app can sustain itself while staying user-centric. Technology plus real human voices can be a stronger alarm than any ringtone. What's next for WakeUpBuddy Next steps include AI-based mood and personality matching to pair users with buddies who can best uplift them during morning calls, as well as group wake-up rooms where 3–5 strangers can wake up together. Planned features also include interest-based matching for students, fitness enthusiasts, and motivation seekers, plus integrations for sleep analysis and smart alarms that adapt to users’ sleep patterns. In the long term, WakeUpBuddy aims to scale globally with localized alarms, optional video wake-ups, and deeper community features that turn waking up into a daily ritual of kindness and social bonding. AI-based mood and interest matching. Group wake-up rooms and community features. Smart alarms with sleep-analysis integrations. Learn more about our App Download Our App <div