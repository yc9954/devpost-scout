---
slug: "drawit-a-mutiplatform-draw-guess-game"
url: "https://devpost.com/software/drawit-a-mutiplatform-draw-guess-game"
title: "DrawIt - A Multiplatform Draw & Guess Game"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 211
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
---

# DrawIt - A Multiplatform Draw & Guess Game

> Real-time Draw & Guess game. Create rooms, invite friends, sketch fast, guess smarter. Crisp design, animations, punchy SFX. Built with Compose Multiplatform for iOS, Android & Desktop too

[Devpost](https://devpost.com/software/drawit-a-mutiplatform-draw-guess-game) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[developer_tools]]

**stack** firebase, kotlin, swift

## How they structured the write-up

- what we built
- how we built it
- weekly blogs | challenges | accomplishments
- what's next for drawit - a mutiplatform draw & guess game

## Body

IOS Android Desktop Multiplatform What we built DrawIt is a Draw & Guess game a popular and well-known party classic. One player sketches while the others guess. It’s fast, fun, and creative! We’ve added the ability to create rooms, invite friends, leaderboard and chats How we built it We used the Compose Canvas APIs to draw and color shapes, and all Compose APIs worked flawlessly across Android, iOS (including Apple Pencil), and desktop (mouse/trackpad). Next, we built a real-time backend state machine to keep the game moving, creating rounds, choosing words, updating the leaderboard, and more. We used Firebase services Firestore, Cloud Functions, Cloud Run and Authentication, and on the client we integrated them via the Firebase GitLive KMP SDK. With the foundations solid, we shifted our focus to the UI, implementing adaptive layouts with a List–Detail pane and WindowSize classes, and testing on desktop, iPad, Android tablets, and foldables to ensure a consistent and reliable experience across devices. Weekly Blogs | Challenges | Accomplishments We published weekly YouTube videos covering the exciting challenges and milestones we achieved over this two-month period. Check out here DrawIt YouTube Playlist What's next for DrawIt - A Mutiplatform Draw & Guess Game Building Real time Audio & Video Chats Improving overall Game Experience <div