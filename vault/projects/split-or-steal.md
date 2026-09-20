---
slug: "split-or-steal"
url: "https://devpost.com/software/split-or-steal"
title: "SPLIT OR STEAL"
hackathon: "Build with MeDo Hackathon "
organization: "Baidu"
winner: true
words: 1031
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/structured_db"
---

# SPLIT OR STEAL

> A high-stakes multiplayer Prisoner's Dilemma. You have exactly two minutes to convince a stranger, a friend, or a manipulative AI to share the wealth before time runs out.

[Devpost](https://devpost.com/software/split-or-steal) · hackathon [[Build with MeDo Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[developer_tools]]
**substrate** [[structured_db]]

**stack** medo, postgresql, react, supabase, tailwind-css, typescript, vite, websockets

## How they structured the write-up

- 🤖 medo llm as a live game mechanic
- ⚡ smooth realtime multiplayer
- 📱 true mobile-first design
- 🎨 strong visual identity
- 🚀 full product built through medo
- 🤖 ai is more powerful as a collaborator
- ⚡ simplicity creates strong gameplay
- 📱 user experience matters deeply
- 🔗 short-term goals
- 📈 future expansion

## Body

Split Or Steal A Real-Time Psychological Multiplayer Experience Built with MeDo 🚀 Inspiration "Can you trust a complete stranger with your fortune?" That single question became the foundation of Split Or Steal . Inspired by social strategy shows like Golden Balls and the psychology behind trust and betrayal, we wanted to create a multiplayer experience where the real challenge is not combat, grinding, or mechanics — but human decision-making itself . Most online games focus on: fast reflexes, complicated systems, or endless progression. We wanted to build something radically different: ✅ Instant psychological tension ✅ Emotionally unpredictable outcomes ✅ Mechanics simple enough to learn in 10 seconds ✅ Depth created entirely through human behavior At the same time, we challenged ourselves technically: Build the entire product — frontend, backend, AI systems, and deployment — using MeDo's prompt-to-product workflow as a full-stack development partner. 🎮 What It Does Split Or Steal is a realtime browser-based multiplayer social strategy game. Two anonymous players are matched instantly and receive: 💰 A shared prize pool ⏱️ A live 120-second countdown timer 💬 A realtime negotiation chat Both players secretly choose: SPLIT Share the reward fairly. STEAL Attempt to take everything. When the timer ends, both decisions are revealed simultaneously. The result creates moments of: trust, betrayal, bluffing, greed, negotiation, and emotional tension. All resolved in under two minutes directly inside the browser. ⚡ Key Features ⚡ Realtime multiplayer matchmaking 💬 Live negotiation chat 🤖 MeDo LLM-powered AI opponent ⏱️ Countdown pressure system 🛡️ Anti-ragequit & disconnect protection 🏆 Global leaderboard 📱 Mobile-first responsive gameplay 🎨 Western-cartoon inspired UI 🚀 Instant browser play with no installation 🛠️ How We Built It ⚙️ Tech Stack Layer Technology Frontend React + TypeScript + Vite Styling Tailwind CSS Backend Supabase PostgreSQL Realtime Sync Supabase Realtime Serverless Logic Supabase Edge Functions AI Opponent Engine MeDo LLM Plugin AI Workflow MeDo Multi-Turn Chat + Full-Stack Generation 🤖 How We Used MeDo MeDo was not a tool we used occasionally. It became our: AI Co-Architect We used MeDo’s core capabilities throughout the entire project lifecycle. 1️⃣ MeDo LLM Plugin — The AI Opponent Brain The most impressive feature MeDo helped us create was the AI opponent system powered directly through the MeDo LLM Plugin . When no human player is available, our backend invokes the MeDo LLM with: the current prize pool, negotiation chat history, player behavior, and game context. The AI does not choose randomly. It evaluates: trust, deception, risk, bluffing, and negotiation tone to simulate realistic human behavior. Example Prompt You are a player in a high-stakes trust game. Prize pool: $X Opponent said: [chat log] Based on their behavior and tone, decide whether to SPLIT or STEAL. Reason like a real human player. The result is an AI opponent that feels: manipulative, unpredictable, and psychologically engaging. 2️⃣ MeDo Multi-Turn Chat — Full Development Collaboration We used MeDo's multi-turn conversations to architect and refine nearly every system in the game. Example Problem Two players disconnecting could permanently deadlock matches. How do we solve this? MeDo Solution beforeunload recovery handling cleanup systems automatic timeout decisions fallback match resolution Result: ✅ Zero deadlocked matches Example Problem The mobile layout breaks on smaller screens. MeDo Solution horizontal layouts touch-friendly controls safe-area spacing responsive gameplay redesign Result: ✅ Fully playable mobile experience Example Problem Two simultaneous player submissions may overwrite each other. MeDo Solution atomic database writes isolated player state updates collision-safe synchronization Result: ✅ Stable realtime multiplayer synchronization 3️⃣ MeDo Full-Stack Generation — Prompt to Product We began with a single prompt: Build a realtime multiplayer browser game where two anonymous players negotiate and secretly decide to Split or Steal a shared reward. From there, MeDo helped: structure the backend, design the database, build matchmaking logic, generate UI systems, optimize responsiveness, and accelerate deployment. The workflow genuinely became: 💡 Prompt → Prototype → Product → Deployment 🔌 Plugins & API Integrations Integration Purpose MeDo LLM Plugin AI psychological decision engine Supabase Realtime Live multiplayer synchronization Supabase Database API Match records + leaderboard Supabase Edge Functions Serverless backend logic Supabase Presence API Matchmaking + connection tracking 🚧 Challenges We Ran Into 1️⃣ Deadlocked Matches Problem A disconnected player could trap the opponent forever. Solution We implemented: disconnect recovery, timeout systems, and automatic fallback decisions. Result ✅ Zero deadlocked matches 2️⃣ Realtime Synchronization Problem Simultaneous actions could create state conflicts. Solution Atomic isolated database updates. Result ✅ Stable realtime synchronization 3️⃣ Mobile Gameplay Problem Desktop layouts failed on small screens. Solution A complete mobile-first redesign. Result ✅ Smooth cross-platform gameplay 4️⃣ AI Security & Latency Problem Frontend AI requests expose credentials and increase latency. Solution Serverless Edge Function integration. Result ✅ Secure AI workflows with fast responses 🏆 Accomplishments We're Proud Of 🤖 MeDo LLM as a Live Game Mechanic The AI opponent became an active psychological participant instead of a simple scripted bot. ⚡ Smooth Realtime Multiplayer Sub-second synchronization created a seamless competitive experience. 📱 True Mobile-First Design The game was redesigned specifically for touch gameplay. 🎨 Strong Visual Identity Every UI element reinforces the psychological tension of the game. 🚀 Full Product Built Through MeDo From first prompt to deployed product, MeDo accelerated every stage of development. 🧠 What We Learned 🤖 AI Is More Powerful as a Collaborator Using MeDo as: an architecture partner, debugging assistant, design collaborator, and iteration accelerator dramatically improved development speed and quality. ⚡ Simplicity Creates Strong Gameplay The emotional complexity comes entirely from: trust, greed, fear, and human behavior. Not from complicated mechanics. 📱 User Experience Matters Deeply Small UI/UX improvements dramatically improved gameplay quality and accessibility. 🚀 What's Next for Split Or Steal 🔗 Short-Term Goals private friend lobbies voice chat support tournament systems party matchmaking 📈 Future Expansion native mobile apps multi-language support spectator mode cosmetic customization creator integrations 🌍 Long-Term Vision Transform Split Or Steal into: A global social strategy platform where trust, deception, and human psychology become the core gameplay mechanic. 🎯 Final Thought Split Or Steal demonstrates how Simple Prompt, MeDo’s LLM Plugin, multi-turn collaboration, and full-stack generation workflow can transform a raw idea into a polished realtime multiplayer product. The opponent in this game isn't the code. It's human nature. <div