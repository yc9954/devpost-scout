---
slug: "agent-sfx"
url: "https://devpost.com/software/agent-sfx"
title: "Agent SFX"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 629
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Agent SFX

> Generates Voiceovers & SFX for games instantly. No recording, no manual importing—just click and play.

[Devpost](https://devpost.com/software/agent-sfx) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** elevenlabs, fal, godot, v0, vercel

## How they structured the write-up

- inspiration
- team info
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- compliance
- what's next for agent sfx

## Body

Just add AI Analyze! It will automatically generate your sound bank! Prompts are still editable Supports Dialog as well! Inspiration We are game developers, and we know how challenging game development can be. Sound design often becomes an afterthought due to time and budget constraints. Scouring sound effects and recording voiceovers is time-consuming and expensive , whether you're an indie dev or a AAA studio. We saw an opportunity to save time and costs while making high-quality audio more accessible to all developers. Agent SFX allows game creators to generate professional voiceovers and sound effects instantly , streamlining the entire process. Team Info Arian Allenson Valdez - lead developer/ideation Mikayla Pace - game developer/ideation What it does AgentSFX compromises of a godot plugin and a web app: As a Godot plugin, it automatically generates voiceovers and sound effects with AI. With a single click, it: Analyzes your node structure and a screenshot of your game Thinks of the possible sound bank for your game Creates a Sound Bank for your game that you can integrate Generates lifelike NPC dialogue using Eleven Labs Create background music with FAL This removes the need for external tools and/or manually scouring the internet/sound databases for audio, making sound design effortless. As a web app, it only provides analysis for your screenshot, but we envision a full end to end workflow for audio design (i.e. revisions, finalizations, creating tickets, asking for feedback) We use Next.JS/Vercel for the web app How we built it The godot plugin itself consists of 3 'core' nodes, that the user can even use without the agent: AI_SFX - generates sound effect via prompts using Eleven Labs AI_Dialog - generates high quality voice acting using Eleven Labs AI_BGM - generates BGM using FAL We then have the 4th node AIAnalyzer, which serves as the AI Agent orchestrating the entire show. AI Analyzer: analyzes the node structure and screenshot (via FAL vision models) processes the analysis (via FAL LLM) proceeds to create the core nodes to a SoundsEffect node that the user can use the user can then integrate the node to the game engine Possible improvements are syncing/persisting audio keys, allowing users to make the AI 'reanalyze' things it has not yet seen/considered. For the web app, we use next.js + the same integrations. Challenges we ran into The entire thing actually was pretty smooth development wise - the hardest part of the hackathon was finding the right idea. We even thought of just skipping this one, but after seeing a random action heavy video clip (that only had sound effects), we thought - can we make an AI agent that analyzes a 'silent' game and generate the audio for it? Accomplishments that we're proud of Making essentially two tools (web app and godot plugin) in pretty much only 1 working day was something we are very proud of. The really seamless integration with Godot is something we're proud of as well! There are lots of improvements to be made still but it's already plenty useful! What we learned How to optimize AI workflows for real-time generation. The power of automation in game development. The challenges of AI-driven creative tools and how to refine them. Compliance We acknowledge adherence to hackathon rules and deadlines - heh we even started so late! :P What's next for Agent SFX Customization options for voice styles and sound types. In particular, allowing users to train their own voice through the web app, or through a sound bank in the engine. More tight integration with the game engine Expanding to other game engines beyond Godot Providing an end to end workflow using the web app. (brainstorming, task management, feedback, finalization) 🚀 Agent SFX is just the beginning—our goal is to revolutionize AI-powered game audio! <div