---
slug: "drawphone-draw-describe-draw-describe"
url: "https://devpost.com/software/drawphone-draw-describe-draw-describe"
title: "DRAWPHONE - Draw→Describe→Draw→Describe..."
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 752
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
---

# DRAWPHONE - Draw→Describe→Draw→Describe...

> “Telephone” meets “Pictionary” A chaotic drawing-and-description party game where each player only sees the previous turn turning simple prompts into wildly funny misinterpretations.

[Devpost](https://devpost.com/software/drawphone-draw-describe-draw-describe) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]

**stack** devvit, express.js, react-18, redis, typescript

## How they structured the write-up

- 🧠 inspiration
- 🎮 what it does
- 🏗️ how we built it
- ⚙️ challenges we ran into
- 🏆 accomplishments we’re proud of
- 💡 what we learned
- 🔮 what’s next for drawphone
- ❤️ acknowledgments

## Body

splash screen view chain result prompt selection for first player first turn turn ready screen draw screen 1 draw screen 2 describe screen 1 describe screen 2 already played screen waiting lock screen 🎨 DRAWPHONE — The Game of Creative Chaos 🧠 Inspiration The idea for DRAWPHONE came from wanting to capture the joy of miscommunication — that hilarious moment when a simple message turns absurd as it passes from person to person. We asked ourselves: What if “Telephone” met “Pictionary”? What if the comedy of misunderstanding could be turned into a multiplayer art experience? We wanted to create something that wasn’t about who can draw best — but who can interpret the worst . By blending art, humor, and community collaboration, DRAWPHONE celebrates imperfection and imagination equally. At its heart, the game proves that the funniest art happens when context disappears . 🎮 What It Does DRAWPHONE is a turn-based, collaborative drawing and description game that transforms simple prompts into chaotic masterpieces. Players alternate between drawing what they read and describing what they see — without ever seeing the original prompt. Each turn warps the message a little further until the final reveal becomes an explosion of laughter. ✨ Core Features Telephone-style gameplay — players only see the previous turn, not the full story Three modes — Short (5 turns), Medium (10 turns), Unlimited (6 hours) Professional HTML5 Canvas tools — smooth, responsive, and mobile-ready Smart validation system — detects blank drawings and low-effort inputs Immersive notebook aesthetic — doodle-style UI with 3D sticky notes and coffee stains Native Reddit integration — play directly inside Reddit posts, no extra setup What begins as “A ninja watering plants” might end as “Alien with sword fighting in space.” The results are as unpredictable as they are hilarious. 🏗️ How We Built It Frontend (React 18 + TypeScript) Built using React 18 with modern hooks and strict TypeScript typing HTML5 Canvas for smooth, anti-aliased drawing with full touch support Tailwind CSS + custom Patrick Hand font for a handwritten doodle aesthetic Real-time timers, undo/redo history, and blank-canvas validation logic Responsive and mobile-optimized design for Reddit’s WebView Backend (Express.js + Redis + Devvit APIs) Express.js API managing game state, turn order, and validation Redis used for real-time synchronization and lightning-fast persistence Devvit SDK handles Reddit authentication, post creation, and notifications Automatic timeout system (3-minute turns) and fair-play enforcement (1 turn per user) Architecture Overview React (Frontend) → Express.js (Backend API) → Redis (Game State Persistence) → Devvit (Reddit Integration Layer) ⚙️ Challenges We Ran Into Real-time State Synchronization Coordinating game states across multiple players and posts required precise Redis management and polling. We built a 10-second auto-refresh loop with minimal data transfer and smooth transitions. Blank Canvas Detection To ensure quality contributions, we developed a base64 pixel comparison system that detects empty or near-empty drawings — preventing troll submissions. Reddit WebView Limitations Optimizing the drawing experience within Reddit’s mobile webview meant rethinking touch handling, timers, and state retention after reloads. Fair Play System Preventing players from taking multiple turns per game was tricky due to asynchronous turn claiming. We solved it with Redis locks and turn ownership tracking . 🏆 Accomplishments We’re Proud Of Designed a complete, multiplayer creative game that runs entirely within Reddit posts Created an immersive notebook-style UI that feels handcrafted and playful Engineered a real-time validation and sync system ensuring fair and smooth gameplay Most importantly — we made a game that consistently makes people laugh out loud 💡 What We Learned Designing for Reddit’s ecosystem taught us how to leverage community-driven engagement loops — comments, follows, and sharing — as gameplay mechanics. WebView development revealed the challenges of embedded games, especially around event handling and performance tuning. Redis-based multiplayer design taught us the power of lightweight, fast persistence for turn-based interactions. Humor as a mechanic — we learned that the best user retention isn’t points or XP… it’s laughter. 😄 🔮 What’s Next for DRAWPHONE Team Chains — groups compete to see whose chain stays most faithful to the original prompt AI Chaos Mode — GPT generates “wild” mid-chain twists based on prior turns Replayable Highlights — GIF-style playback of the full chain evolution Seasonal Events — themed prompts for holidays, fandoms, and memes Community Prompt Packs — players submit and vote on new prompt ideas ❤️ Acknowledgments Huge thanks to: Reddit Devvit Team for providing the amazing platform that makes in-post experiences possible Everyone who tested DRAWPHONE — your hilarious drawings and descriptions made this project truly unforgettable <div