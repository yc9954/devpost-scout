---
slug: "sideline"
url: "https://devpost.com/software/sideline"
title: "Sideline"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 587
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/code_repository"
---

# Sideline

> Sideline turns watching into experiencing. With real-time updates, interactive challenges, and friendly rivalries that make every play matter, you’re not just watching the game… you’re part of it.

[Devpost](https://devpost.com/software/sideline) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[code_repository]]

**stack** expo.io, express.js, firebase, firestore, node.js, openai, react-native, sportradar, typescript, ws

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sideline

## Body

This shows the live game room with the microbets This is the pop-up when a microbet is announced This shows the user profile This shows the awards a user can redeem This shows the list of teams a user is a part of This shows the live game a user can select in a team This is the interface for betting in private teams This is the team leaderboard Inspiration Community is a huge aspect of sports, and we noticed that while fans can watch together, the sports-watching experience is often passive. We created Sideline to augment that experience and hone in on the community aspect of sports. We spoke to people who were heavily into sports betting and realized that there is a lot of potential for microbets, specifically, and wanted to make each play meaningful. From there, we also realized the gap in connecting not just fans, but the broader community. As a team with different levels of knowledge when it comes to sports, we realized how important it is to bridge that gap. What it does Sideline is a second-screen experience for live sports that allows users to participate in community micro bets. Micro bets are sponsored by companies, and the more accurate community votes mean more donations. Sideline also lets friends create custom bets and leaderboards, turning game-day into a community challenge that blends competition, charity, and fun. Sideline is made to help beginners understand the game better with its AI chatbot, strengthen sports watching communities, and turn betting into social good. How we built it We built a custom WebSocket wrapper over the NFL Sportradar API to simulate live game events. For the microbets, we used GPT-powered retrieval models to create engaging microbet prompts. Firebase handled authentication, real-time state sync, and user leaderboards. Finally, our UI featured a responsive UI to display bets, track coins, and show group leaderboards for users. Challenges we ran into Some libraries and frameworks were incompatible or would cause rare issues that set us back on time. Towards the end, our ChatGPT API token got invalidated due to an early accidental commit, so we had to create our own. We have never made a web socket before, so we had to overcome a steep learning curve, especially with connecting without localhost. Accomplishments that we're proud of We successfully combined live sports data, AI-generated bets, and social features into a single, cohesive experience. We had a lot of features in mind when we started out, and were worried we were spreading ourselves too thin. In the end, it all came together well and doesn’t feel too cluttered or inconsistent. Additionally, we are proud of our UI, which uses many animations and gradients that bring components into focus. What we learned We greatly improved our API and backend management skills with this project. Since we’ve never made a web socket before, we researched how to set up the connection and send data in chunks. Also, since we worked as a team on GitHub, managing merge conflicts and ensuring proper documentation of errors was crucial so that mistakes wouldn’t reappear on others’ devices. What's next for Sideline Sideline sees itself as the future mode of advertisement. Rather than ads funding corporations, the proceeds are given back to people in need. This way, our community is helped, companies gain presence, and even users are able to gain rewards. We wish to progress as a non-profit based on promoting this cycle while also building a platform that our users genuinely enjoy. <div