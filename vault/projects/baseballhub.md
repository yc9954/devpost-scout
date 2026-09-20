---
slug: "baseballhub"
url: "https://devpost.com/software/baseballhub"
title: "BaseballHub"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 935
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# BaseballHub

> Built with Bolt.new, Baseball Hub went from idea to App Store in a week—an AI-powered app that helps youth coaches manage teams, lineups, and schedules fast

[Devpost](https://devpost.com/software/baseballhub) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[supply_logistics]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** expo.io, netlify, react, react-native, supabase, tailwind

## How they structured the write-up

- 🧢 inspiration
- ⚾ what it does
- 🛠️ how we built it
- 🚧 challenges we overcame
- 🏆 accomplishments we’re proud of
- 📚 what we learned
- 🚀 what’s next
- ⚡ how bolt.new supercharged development
- 🎯 final thoughts

## Body

🧢 Inspiration As a youth baseball coach with four kids, I’ve experienced firsthand the overwhelming logistics of running a team. Managing schedules, creating lineups, and coordinating with parents often pulled me away from what truly matters—coaching and connecting with the kids. Baseball Hub was born out of this challenge: to simplify the admin work so coaches can focus on the game and the players. ⚾ What It Does Baseball Hub is a comprehensive, cross-platform team management app tailored for youth baseball coaches. It streamlines time-consuming tasks with features like: 🧍 Player Management – Track player skills, positions, and preferences. 📆 Game & Practice Scheduling – Create events with automatic calendar integration. 🧾 Lineup Builder – Manage batting orders and field positions. 📲 Availability Tracking – Let families mark player attendance ahead of games. 🍎 Snack Sign-Up – Organize volunteers for post-game snacks. 🌐 Public Team Pages – Share team schedules and info with families. 🤖 AI Lineup Generator (Pro Feature) – Generate optimized lineups based on player data, coach preferences, and league rules using AI. 🛠️ How We Built It Frontend: Built with React Native using Expo , allowing us to deploy to iOS, Android, and Web from a single codebase . This approach powered not just the mobile app, but also our landing page and public team pages , ensuring consistent experience and faster iteration. Expo Router is used for screen navigation and API route definitions. About 90% of the application was built with AI-generated code , with only ~10% needing manual implementation and tweaks. Backend & Infrastructure: Supabase provides authentication, real-time syncing, and a PostgreSQL database. A Supabase Edge Function securely handles our AI lineup generation , integrating with OpenAI. A Netlify Function powers iCalendar subscription links for syncing team events. RevenueCat manages all in-app purchases and subscriptions , including Pro features. App Store Launch: This was my first iOS app submitted to the App Store . Thanks to Expo , the build and submission process was seamless. Apple’s review feedback came in under one business day, and after a few quick fixes, the app was approved and successfully published . I used theapplaunchpad.com to quickly create high-quality App Store screenshots. 🚧 Challenges We Overcame Cross-Platform UI Consistency: Ensuring a clean and responsive interface across all devices. Real-Time Data Sync: Efficiently synchronizing availability, schedules, and lineups across users. AI Prompt Handling: Structuring complex prompts and parsing outputs into usable, rule-based game data. UX for All Tech Levels: Designing intuitive workflows for coaches with varying tech backgrounds. Performance: Maintaining speed and responsiveness as datasets grow. 🏆 Accomplishments We’re Proud Of This is my first-ever iOS app published to the App Store , with a smooth submission experience via Expo. Thanks to Bolt.new , I was able to go from idea to App Store approval in about one week —a huge win for rapid development. Built a full-featured, cross-platform app from a single codebase with minimal hand-coded logic (~10%) . Successfully integrated Supabase, Netlify Functions, and RevenueCat for a modern, scalable backend. Created a polished AI-powered lineup generator that adds real value to coaches. Shipped a clean and user-friendly app that even non-technical coaches can use with ease. Launched a public-facing web experience using the same React Native codebase. 📚 What We Learned Expo makes publishing to the App Store surprisingly smooth. The end-to-end flow, including building, submitting, and responding to Apple’s feedback, was intuitive—even as a first-timer. AI-generated code is incredibly productive. About 90% of the app was generated, drastically reducing development time and letting us focus on what matters most. A single React Native codebase can power both mobile and web—including landing pages and public team views —with careful component design and platform-specific tweaks. Supabase Edge Functions are a great way to securely run advanced server logic, especially for AI workflows. iCalendar support via Netlify Functions provided an easy yet powerful feature for families. Building a great UX means testing early, iterating often, and simplifying wherever possible. The Expo + Supabase + RevenueCat + Bolt.new stack is ideal for fast, scalable, real-world app development. 🚀 What’s Next AI Practice Planner: Automatically suggest drills and practice formats based on team needs. In-App Messaging: Communication tools for coaches, parents, and players. Player Stats & Reports: Track progress, attendance, and performance over time. Support for Other Sports: Easily adapt Baseball Hub to soccer, basketball, and beyond. Coach Community Tools: Template sharing, lineup strategies, and best practice guides. ⚡ How Bolt.new Supercharged Development Bolt.new dramatically accelerated development through intelligent AI code generation and smart suggestions—all while keeping us in full control of the code. 🧠 AI-Assisted Coding Bolt.new enabled us to generate React Native components, Supabase queries, and backend logic from natural-language prompts. It handled everything from form validation to API integration. 🛠️ Code-First with Guidance Unlike low-code tools, Bolt.new doesn’t hide your code—it enhances it. We worked directly with the codebase while receiving smart refactors and fixes from the AI assistant. ⚙️ Prebuilt Integrations We hit the ground running thanks to Bolt.new’s built-in support for Supabase and Expo. We spent less time on setup and more time building real features. 🔄 Rapid Prototyping Bolt.new made it easy to test and iterate on ideas quickly—essential for staying agile during a hackathon sprint. 🎯 Final Thoughts Baseball Hub solves a real problem for real coaches. Built in record time using powerful modern tools, it’s already making game day easier for teams—and it's just getting started. Thanks to Bolt.new , Netlify , RevenueCat , and Supabase , we were able to go from idea to App Store in just days—with production-level polish and performance. Let’s play ball. ⚾ <div