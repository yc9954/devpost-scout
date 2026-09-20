---
slug: "thediggerman"
url: "https://devpost.com/software/thediggerman"
title: "TheDiggerMan"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 858
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# TheDiggerMan

> Addictive incremental mining game with global leaderboards for competitive community play and maximum user retention. Click, dig, automate, compete.

[Devpost](https://devpost.com/software/thediggerman) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]] [[video_visual]]

**stack** devvit, kiro, react, reddit, redis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for thediggerman

## Body

Inspiration Games like Egg.inc, MakeitRain and Cookie clicker were inspiration. These have extreme difficult progression and a whole bunch of achievements. It makes the user to stay in the app for long time. User screen retention was my goal. I wanted to bring the addictive nature of incremental games to Reddit's platform, where the social aspect of leaderboards and community competition could amplify the engagement. The key was balancing the satisfying click-reward loop with meaningful progression milestones that would keep players invested for weeks, not just minutes. What it does TheDiggerMan is a fully-featured incremental mining game with over 200+ users and exceptional user retention. Players click to mine through 10 unique biomes from surface dirt to ancient bedrock, discovering 30+ different ore types with varying rarity and value. The game features a comprehensive automation system with 8 tiers of auto-diggers that mine passively, a global leaderboard system tracking money, depth, and achievements, and 25+ achievements that create multiple progression paths. Community play features include global goals where all players work together toward shared challenges, and a live activity feed showing real-time player achievements. Real-time competition motivates players to stay on top while the idle mechanics ensure progress continues even when away. How we built it Built with Kiro IDE and Reddit's Devvit platform to capture user clicks and create an engaging mining experience. The technical stack includes: React 19 and TypeScript for the frontend with modern hooks and concurrent features Redis for persistent storage, leaderboards, and real-time data synchronization Express.js serverless backend on Devvit platform with RESTful API endpoints Performance optimizations including particle limits and mobile detection Community features including global goal tracking and real-time activity streams The game features exponential progression curves with 30+ ore types across 10 unique biomes, 8 tiers of automated miners, a sophisticated achievement system, and community-wide challenges that bring all players together toward shared objectives . Challenges we ran into Auto clickers - This is a challenge in all clicker games which can't be completely overcome, requiring careful game balance and progression tuning to maintain fairness. Assets - It was difficult to find assets, sprite images, and other character images for the app. User data and leaderboard management - Implementing scalable Redis data structures for real-time competition while preventing data corruption and ensuring fair play across hundreds of concurrent users. Community synchronization - Managing global goals and activity feeds across hundreds of concurrent players while maintaining real-time updates and data consistency. Performance at scale - Managing 60 FPS depth counters and particle effects while maintaining smooth gameplay across desktop and mobile devices. React stale closures - High-frequency updates caused callbacks to capture outdated state, solved with ref patterns to always access fresh game state. Cross-platform optimization - Balancing rich visual effects for desktop users while ensuring smooth performance on mobile devices with automatic capability detection. Accomplishments that we're proud of Getting over 200+ active users and people actually competing in the leaderboard! A whole bunch of users have reached some of the highest depths of the game (beyond 10,000+ feet), which takes hours of dedicated play to achieve. This verifies that the user retention for the game is exceptionally high and players are genuinely engaged with the progression system. We successfully implemented a zero data loss system with cloud-synced saves, created real-time global competition that updates live, built community features that bring players together toward shared goals , and built a comprehensive admin tooling suite for database inspection and analytics. The game scales to support millions of players with O(log N) leaderboard operations, and we've maintained consistent 60 FPS performance even during intense clicking sessions. Most importantly, we've created a true community experience where individual actions contribute to collective achievements. What we learned Having a clicker game with rich features, engaging visuals, and meaningful achievements will keep people hooked in the game. The combination of individual progression and competitive leaderboards creates a powerful retention loop that keeps players coming back. Exponential progression curves are crucial for maintaining long-term engagement - each upgrade must feel significant while maintaining challenge. Social competition amplifies the addictive nature of incremental games when players can see their ranking against others. Community collaboration adds another layer of engagement when players feel their individual actions contribute to something bigger. Performance optimization is critical for mobile users who represent a significant portion of Reddit's audience. Most importantly, community-driven mechanics like leaderboards and shared goals transform solo experiences into social competitions that drive sustained engagement. What's next for TheDiggerMan Enhanced visuals with custom sprite artwork, animated backgrounds, and particle effect improvements. Expanded mission system with daily challenges, weekly tournaments, and special events with limited-time rewards. Advanced community features including guild mechanics for team-based competition, collaborative building projects where players construct shared mining facilities, and donation systems where players can contribute resources to community pools. Global donation mechanics where the community works together toward massive shared goals like "Mine 1 billion total blocks" for server-wide bonuses. We're also exploring prestige systems that reset progress for permanent multipliers, rare ore events that spawn globally for limited time periods, and social features including player profiles, friend systems, and direct challenges between users. <div