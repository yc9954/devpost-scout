---
slug: "ai-desktop-companion-glitch"
url: "https://devpost.com/software/ai-desktop-companion-glitch"
title: "AI Desktop Companion (Glitch)"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 743
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# AI Desktop Companion (Glitch)

> Meet Glitch: The JARVIS you dreamed of. A multimodal agent that doesn't just chat—it acts. Sees your screen, automates your OS. #AgenticAI

[Devpost](https://devpost.com/software/ai-desktop-companion-glitch) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]] [[researcher]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css3, electron, elevenlabs, gemini, github, google, html5, javascript, npm, nut.js, pixijs, playwright, three.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for glitch

## Body

Searched for info on google on demand.... Summarized the info and saved on notepad.... Created nextjs project structure to pour life to your ideas... Agent mode to excecute complex tasks... All important tools included from voice mode, agent mode, vision mode to settings where you can customise the characters and voice! Interactive and playful characters!! Not just another chatting bot, this does the real stuffs!! Interactive playful Characters which you can customise too on settings... AI Desktop Companion — Glitch Download here Check out our landing page! Github Repo Download PPT A living, breathing AI that shares your desktop. Not a tab. Not a chatbot. A companion!! Inspiration (Just kidding, don't try that!!) We grew up dreaming of companions like JARVIS — agents that don’t just listen, but act. Somewhere along the way, assistants got stuck in browser tabs. We wanted to break the Fourth Wall of the Operating System . Glitch was born from a simple idea: What if an AI actually shared your workspace? An AI that: Lives on your desktop Sees what you see Acts when needed Feels alive We fused the nostalgia of desktop pets (Clippy, Tamagotchi) with the power of Google Gemini Multimodal Live , creating an AI that isn’t just helpful — it’s present. What it does Glitch is a fully multimodal, autonomous desktop agent. ✨ Core Capabilities 🖥️ Lives on Your Screen A transparent, always-on-top overlay that blends into your OS. Drag Glitch anywhere. Watch him chase his cat. He reacts to your work with a new, sleek Floating Action Button (FAB) UI. 👁️ Multimodal Vision Glitch can see your screen in real-time: “What is this error?” “Review this UI” “Does this outfit look good?” 🧠 Autonomous Agent Mode Powered by nut-js , Glitch can: Control mouse & keyboard Open apps like Notepad effortlessly Execute multi-step workflows 🎙️ Real-time Voice & Personality No external keys needed. Powered entirely by Gemini Live. Dynamic Voices: Switch personas instantly (Glitch, Puck, Charon, Kore, Fenrir). Humor Mode: Glitch is witty, slightly chaotic, breaks the fourth wall, and makes tech jokes. 🧑‍💻 Developer Accelerator Just say: > “Create a Next.js crypto dashboard” Glitch will: Scaffold the project Generate boilerplate Open VS Code Bring your idea to life 📝 Smart Notes Glitch has intelligent note-taking capabilities: > "Write Best bitcoin data API's for Developer in Notepad" Glitch will generate the recipe internally, open Notepad, and magically paste it — no Google searches required unless you ask for them. 🎨 Image Generation (Bonus Power) Glitch can also generate images on demand — perfect for design inspiration, concepts, or quick visuals — seamlessly integrated into your workflow. How we built it Glitch is powered by a Hybrid Agent Architecture : 🧩 Core Framework — Electron Enables a frameless, transparent, click-through desktop overlay. 🧠 The Brain & Voice — Google Gemini Multimodal Live API Handles: Natural conversation & Reasoning Vision analysis (Screen context) Native Audio Streaming (Low latency voice, no 3rd party TTS required) 🤖 The Body — Nut.js Grants OS-level automation: Mouse control & Keyboard bridge Clipboard integration (for instant typing) Application workflows 🎮 The Soul (UI) — PixiJS & React/Tailwind PixiJS : Renders pixel-art characters and physics. React : Powers the new Settings Wizard and FAB controls. Challenges we ran into The Click-Through Paradox Characters needed to be clickable — empty space needed to be transparent. We dynamically toggle Electron’s setIgnoreMouseEvents in milliseconds. Smart Context Switching Teaching the AI when to "type" versus when to "speak". We built a specialized bridge that allows Glitch to paste long texts instantly into Notepad rather than painfully typing character-by-character. Safety in Automation OS control is powerful — and dangerous. We built: A global STOP protocol Verified visual context before acting Accomplishments we’re proud of Seamless OS-level overlay that feels native . Removing complex dependencies (ElevenLabs) to make it pure Gemini-powered. A character with personality , not just intelligence (Sarcastic, Funny, or Professional). A companion that feels present, playful, and productive. What we learned Multimodal is the Future Giving AI sight changes everything. Personality Drives Adoption Users engage more when AI feels alive, makes jokes, and has a unique voice. Simplicity Wins Consolidating voice and reasoning into one model drastically reduced latency. What’s next for Glitch 🧠 Long-Term Memory Vector databases (Pinecone) to remember projects across weeks. 🧩 Skill Ecosystem Developer-written plugins: Spotify control, Git commits, CI helpers. 👥 Multi-Agent Teams Multiple on-screen characters collaborating: Designer Developer Researcher Glitch isn’t just an assistant. He’s a presence. <div