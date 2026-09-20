---
slug: "musiclink-motivational-companion-app"
url: "https://devpost.com/software/musiclink-motivational-companion-app"
title: "MusicLink - Motivational Companion App"
hackathon: "PANDA Hacks 2025"
organization: "PANDA Organization"
winner: true
words: 747
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
---

# MusicLink - Motivational Companion App

> MusicLink: Connect with some of my favourite anime companions through music-themed matching app alike web, designed to motivate students at Panda Hacks 2025. A tribute to my 推し ♡

[Devpost](https://devpost.com/software/musiclink-motivational-companion-app) · hackathon [[PANDA Hacks 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** html, react

## How they structured the write-up

- inspiration
- what it does
- how it's built / technical details
- 🛠️ tech stack
- 🧠 what i learned
- 🔮 team
- 🔮 future improvements

## Body

🎵 MusicLink - Motivational Companion App MusicLink is a front-end web application built in React for the Panda Hacks 2025 hackathon. It's designed to help students stay motivated by connecting them with encouraging "companions" through the shared language of music. Inspiration I was inspired by the engaging mechanics of modern social apps but wanted to create a more positive and productive experience. MusicLink was born from the idea of combining a love for music with the need for daily motivation. Instead of seeking dates, users connect with companions who encourage them through AI-powered chat and shared musical tastes, helping to combat procrastination and build positive habits. What it Does MusicLink is a web app where users discover and connect with motivational companions. The core user journey is: Discover & Sync: Users browse character profiles and "sync" with them using a simple button interface. Collect Music: Syncing with a companion instantly adds their top songs to the user's personal playlist, accessible in the app's music player. Vibe Check & Chat: After syncing, the user sends a first message to unlock a persistent chat. The companions, powered by a keyword-based dialogue system, offer encouragement and motivation. Customize: The entire app experience can be personalized with four distinct visual themes and full English/Japanese language support. All preferences and progress are saved locally. How It's Built / Technical Details MusicLink is a front-end web application built in React, designed to be a complete and polished prototype for the Panda Hacks 2025 hackathon. Component-Based Architecture: Built with React and functional components, leveraging useState and useEffect hooks for state management. Gamified Discovery: Tinder-style swipe interface (re-imagined with buttons) to discover and "sync" with new companions. Dynamic Theming Engine: Four hand-crafted themes (Minimal Light/Dark, Y2K Light/Dark) powered by CSS Variables for instant, seamless switching. Full Internationalization (I18N): The ability to switch between English and Japanese across the entire UI and all character content. State Persistence: User data (connections, chats, preferences, etc.) is saved to localStorage , ensuring a consistent experience across sessions. Data Hydration: Includes logic to safely update outdated localStorage data structures to new ones, preventing errors for returning users. Fully Responsive: A fluid desktop layout that transforms into a mobile-friendly experience with slide-out menus and a bottom navigation bar. Polished UI/UX: Complete with custom components, smooth animations, and Feather Icons for a clean look. 🛠️ Tech Stack Framework: React 18 Language: JSX (JavaScript), HTML5, CSS3 Tooling: Babel (in-browser transpilation for this prototype) Icons: Feather Icons Persistence: Browser localStorage API 🧠 What I Learned Building MusicLink was a fantastic learning experience, particularly in these areas: Complex State Management: Juggling multiple, interconnected pieces of state (e.g., how adding a connection affects the discover queue and the journal simultaneously) was a great challenge. It reinforced the importance of a single source of truth and careful state design. Robust Theming: Implementing the theme switcher taught me the power and flexibility of CSS Custom Properties (Variables). It's a much cleaner and more scalable approach than managing multiple CSS files or using classes for every property. Defensive Programming: Writing the rehydrateItems function was a key insight. It forced me to think not just about the current state of the app, but how to gracefully handle data from past versions of the app to prevent breaking changes for users. Responsive Design Logic: Thinking through how to transform a 3-column desktop layout into a functional mobile view with a bottom bar and sliding sidebars was a great exercise in CSS, media queries, and React state for controlling UI visibility. 🔮 Team ╮ೃ⁀➷Me 🔮 Future Improvements While I'm proud of this hackathon submission, there are many ways it could be scaled into a full production application: ** Real Backend & Database:** Replace localStorage with a service like Firebase or Supabase to allow for user accounts, real-time chat, and data persistence across devices. (My long term goal.) ** Integrate Music APIs:** Connect to the Spotify or YouTube Music API to allow for actual song playback and to fetch real, dynamic playlists for characters. ** Smarter AI Chat:** Move from keyword-based responses to a real Large Language Model (LLM) via an API (like the ai API) for more natural, varied, and intelligent conversations. ** Refactor to a Build System:** Migrate from the in-browser Babel setup to a proper build tool like Vite or Create React App for code splitting, optimization, and a better developer experience. ** Onboarding Flow:** Add a simple tutorial or a "How-To" modal that appears automatically for first-time users. <div