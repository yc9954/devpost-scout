---
slug: "bluekai-bluesky-on-a-flip-phone"
url: "https://devpost.com/software/bluekai-bluesky-on-a-flip-phone"
title: "BlueKai - BlueSky on a flip phone!"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 929
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# BlueKai - BlueSky on a flip phone!

> Retro hardware, future protocol. A BlueSky client for KaiOS feature phones - connecting the next billion users to decentralized social media.

[Devpost](https://devpost.com/software/bluekai-bluesky-on-a-flip-phone) · hackathon [[Kiroween]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[labor_employment]]
**substrate** [[document_pdf]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** babel, css, gecko, html, javascript, kaios, kiro, preact, webpack

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bluekai - bluesky on a flip phone!

## Body

BlueKai brings modern social networking to flip phones thanks to Kiro Featuring an initial set of translations for English, Spanish, French, Portuguese, Arabic, Hindi, Swahili, and Indonesian Inspiration The next billion mobile users aren't getting smartphones. They're getting $20 flip phones running KaiOS . KaiOS powers over 200 million devices worldwide, but modern social networks like BlueSky aren't building for the platform's constraints: 256MB RAM, Gecko 48 (Firefox from 2016, the foundation of KaiOS launched in 2017), D-pad navigation only , and limited bandwidth where every kilobyte matters. I wanted to prove that "dead" technology like KaiOS 2.5 flip phones could run modern web applications, and that AI-assisted development could make building for niche platforms feasible for small teams. What it does BlueKai is a fully functional BlueSky client for KaiOS 2.5 flip phones. Users can: Authenticate with their BlueSky credentials View their timeline with rich media content Create posts and replies Like and repost content Read threads Edit their own profile View notifications The app is optimized for D-pad navigation with context-aware softkeys, includes a data saver mode for users on limited plans, works offline with cached content, and supports 8 languages including right-to-left text for Arabic. The entire bundle is under 75KB gzipped , making it practical for users with slow 2G connections. How we built it I used Kiro 's spec-driven development workflow to structure the entire application. The process had three phases: Requirements : I worked with Kiro to create user stories with EARS-format acceptance criteria (like "WHEN the user logs in THEN the system SHALL authenticate using BlueSky ATP protocol "). This forced me to think through edge cases upfront, including offline behavior, session expiration, and KaiOS-specific constraints. Design : Kiro researched the BlueSky AT Protocol API and Gecko 48 limitations , then generated a comprehensive architecture document with component hierarchies and data models. This became the shared reference for all implementation work. Tasks : The design was broken into 25 discrete implementation steps with sub-tasks. Each task referenced specific requirements, so I always knew why I was building something. Kiro executed tasks one at a time, and I could review progress incrementally. For quick iterations and bug fixes, I used vibe coding, describing behaviors in natural language like "The cursor can start on top of the action bar and prevent scrolling" to get immediate fixes. The hybrid approach worked perfectly: specs for foundational features, vibe coding for refinements. Technical stack: Preact for the UI framework (minimal bundle size), Webpack 5 with Babel for building and optimizing, and aggressive transpilation to ES5 for Gecko 48 compatibility. Challenges we ran into Gecko 48 compatibility was the biggest challenge. No Fetch API meant wrapping XMLHttpRequest in Promises. No async/await meant careful Promise chaining. Limited ES6 support required extensive polyfills and Babel transpilation to ES5. The 200KB bundle budget was brutal, requiring aggressive tree-shaking, code splitting, and careful dependency selection. We ultimately achieved 73KB gzipped. D-pad navigation needed a custom focus management system since standard web navigation patterns don't work with KaiOS keypad input . Virtual scrolling was essential for performance on low-memory devices to prevent crashes when rendering long timelines. Building a production-ready internationalization system for 8 languages including RTL support was far more complex than expected, requiring careful consideration of text direction, layout reversals, and memory-conscious language loading. Accomplishments that we're proud of The internationalization system stands out. Kiro didn't just create the code structure - it generated actual translations for 8 languages (English, Spanish, French, Portuguese, Arabic, Hindi, Swahili, Indonesian), handled right-to-left text direction for Arabic, implemented memory-conscious loading for feature phones, and built graceful fallbacks. We achieved a 73KB bundle (well under our 200KB target) while including a full-featured social media client with offline support, timeline rendering, posting capabilities, and profile management. The D-pad navigation system works smoothly with circular navigation, proper focus management, and context-aware softkey actions that adapt based on the current screen. The offline support with intelligent caching means users can read their timeline even without connectivity - critical for areas with intermittent 2G/3G coverage. The data saver mode respects users on prepaid plans by making image loading optional, helping them preserve their limited data allowances. What we learned Describing behaviors in natural language is more effective than asking for specific code patterns when working with AI. Kiro understood intent and generated contextually appropriate solutions. Specs shine for complex features with many moving parts, providing context that persists across sessions. Authentication, state management, and i18n all benefited from the structured approach. AI excels at handling platform-specific constraints when given proper context, like understanding both Gecko 48 limitations and KaiOS user needs simultaneously. Incremental review (one task at a time) prevents massive code dumps and keeps development manageable. I could verify each piece worked before moving forward. Most importantly, AI-assisted development makes it feasible for small teams to build for platforms that otherwise have steep learning curves and due to technical limitations have lots of edge cases and potential paper cuts to consider. What's next for BlueKai - BlueSky on a flip phone! Future features I would like to add: Direct messages support Search functionality for users and posts Custom feeds beyond the default timeline Media upload support (photos/videos) Quote posts and advanced threading Technical improvements: Service Workers for enhanced offline support WebSocket support for real-time updates KaiOS 3.0 and eventually 4.0 versions to take advantage of new features as these phones make their way out of North America BlueKai proves that modern web applications can run on "dead" technology, bringing decentralized social networking to the next billion mobile users. <div