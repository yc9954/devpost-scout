---
slug: "darwin-w6fez0"
url: "https://devpost.com/software/darwin-w6fez0"
title: "darwin."
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 492
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# darwin.

> evolve coding agents through pvp and reinforcement on web3.

[Devpost](https://devpost.com/software/darwin-w6fez0) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[voice_speech]]
**domain** [[civic_government]] [[developer_tools]]
**substrate** [[financial_record]] [[transcript_audio]] [[video_visual]]

**stack** claude, claude-code, elevenlabs, gemini-cli, google-cloud, letta, livekit, react, sui, three.js, vercel, vite, webgl

## How they structured the write-up

- inspiration
- what it does
- the flow:
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

landing page ui/ux & workflows artifact: shaded ball artifact: cal hacks landing page whiteboard :D Inspiration midjourney lets you generate 4 images and pick the best one, but code agents give you one output and force you into prompt hell if you don't like it. we can't stop agents mid-execution when they go the wrong direction, so we asked: what if ai coding worked like image diffusion with competitive selection instead of iterative prompting? What It Does darwin runs 4 ai agents that compete to build your ui with wildly different styles while a commentator analyzes their approaches in real-time. after each round you pick the winner and agents evolve their strategies - some copy the winner completely, some iterate on their approach, some synthesize patterns, converging toward your taste through competitive selection instead of prompt engineering. agents have their own sui wallet addresses, tip directly with SUI to those you like the agents: speedrunner: fast execution, minimal style bloom: animation-heavy, maximalist solver: logic-driven, structured loader: data-focused, pragmatic commentator: live sports-style narration via send_message_to_agent_async orchestrator: task splitting and validation the flow: orchestrator splits into subtasks 4 agents code simultaneously with distinct approaches commentator queries agent memory and narrates live users watch with audio-reactive 3d visualizations vote on-chain (gasless via sui sponsored transactions) losers read winner's memory and rewrite their own persona blocks how we built it letta cloud - true cross-agent communication via send_message_to_agent_async, agents literally rewrite their own context blocks through tool calling, orchestrator uses run_code to validate execution livekit, elevenlabs tts → pcm → audiosource → localaudiotrack published to room, multi-spectator synchronized experience, data channels for transcripts audio-reactive webgl, livekit mediastream → web audio api analysernode → three.js shaders pulse with voice frequencies (shuriken, sphere, cube, rings) sui blockchain, fully serverless gasless voting via vercel edge functions sponsoring all transactions, users vote completely free, custom move contract with dual entry points (free voting + tipping), ~400ms finality, transparent leaderboard at 0xe649...0c55 claude code - multi-file refactoring, webgl debugging, livekit audio pipeline architecture Challenges We Ran Into livekit audio synchronization with elevenlabs tts buffer management true cross-agent memory reading while maintaining context sui transaction sponsoring securely in serverless functions webgl shader performance with multiple orbs designing meaningful agent learning without overfitting Accomplishments That We're Proud Of true multi-agent system where agents actually query each other's memory zero-cost user experience with on-chain voting each agent has distinct voice personality via elevenlabs self-evolving agents that rewrite their own memory blocks real-time spectator experience with synced audio/video What We Learned letta's persistent memory enables genuinely stateful ai agents that communicate livekit's room model makes multiplayer ai experiences straightforward sui's fast finality enables blockchain voting that feels instant voice-reactive visualizations create visceral connection to ai personalities sponsored transactions completely abstract blockchain complexity What's Next tournament mode with multi-round elimination custom agent training with unique personas agent marketplace as nfts with evolved memory blocks live streaming integration to twitch/youtube voice commands via vapi during battles <div