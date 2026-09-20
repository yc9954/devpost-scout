---
slug: "vibecat"
url: "https://devpost.com/software/vibecat"
title: "VibeCat"
hackathon: "Gemini Live Agent Challenge"
organization: "Google"
winner: true
words: 548
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# VibeCat

> Your proactive desktop companion. VibeCat watches your screen via Gemini Live API, suggests actions before you ask, and executes with self-healing navigation. Built with GenAI SDK + ADK on Cloud Run.

[Devpost](https://devpost.com/software/vibecat) · hackathon [[Gemini Live Agent Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]]

**stack** appkit, artifact-registry, avfoundation, chromedp, cloud-build, cloud-logging, cloud-monitoring, cloud-run, cloud-trace, coregraphics, docker, firestore, gemini-live-api, genai-sdk

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vibecat

## Body

Action Execution Pipeline — triple-source grounding (AX/CDP/Vision) with self-healing retry and vision verification. System Architecture — Swift client ↔ Go gateway on Cloud Run ↔ Gemini Live API + ADK orchestrator. The Problem — developers lose flow switching between reactive AI tools that all wait for commands. Meet VibeCat — a proactive companion that connects your code, music, and workflow seamlessly. Inspiration "Every AI tool waits for your command. But what if one didn't?" Solo developers ship alone, debug alone, and celebrate alone. Every AI coding tool today is reactive — it waits for you to type a command. The context switch is the real cost: you break flow to talk to the AI, and lose minutes of mental re-entry time. We wanted to flip this model entirely — an AI that watches your screen, recognizes opportunities, and speaks up first. What it does VibeCat is a native macOS desktop companion that watches your screen, understands your context, and proactively suggests actions before you ask. It follows the core loop: OBSERVE → SUGGEST → WAIT → ACT → FEEDBACK Sees your screen via Gemini Live API's real-time vision Suggests actions in natural voice ("I notice a missing null check — want me to fix it?") Waits for your permission before acting Executes via 5 function calling tools with self-healing navigation Verifies results through vision-based screenshot analysis Three demo scenarios: YouTube Music playback, code enhancement in IDE, and terminal command execution. How we built it macOS Client (Swift 6.2 + AppKit): Native screen capture, microphone input, voice playback, and local action execution with 131 tests across 20 test files. 80+ key codes mapped for full keyboard control. A floating NavigatorOverlay HUD shows grounding source badges (AX/Vision/Hotkey/System) in real-time. Realtime Gateway (Go + GenAI SDK v1.49.0): WebSocket bridge to Gemini Live API. Manages the pendingFC sequential execution queue — each function call completes and verifies before the next begins. Self-healing retries with alternative grounding sources on failure. ADK Orchestrator (Go + ADK v0.6.0): Handles vision verification — captures post-action screenshots, analyzes them with Gemini, and confirms success before proceeding. Runs on Cloud Run alongside the gateway. Challenges we ran into YouTube Music renders controls on <canvas> — invisible to the macOS Accessibility tree. Solved with triple-source grounding: AX → CDP (chromedp) → Vision coordinates. Gemini sometimes hallucinates tool usage without actually calling the function. Fixed by using real voice input instead of programmatic text injection. Sequential multi-step execution required the pendingFC mechanism to prevent race conditions when Gemini batches multiple function calls. Accomplishments that we're proud of VibeCat proactively spoke first 5/5 times during live testing — without being prompted Self-healing pushed YouTube Music success rate from 62% to 94% 18 dev.to blog posts documenting the entire journey Full automated deployment pipeline via infra/deploy.sh What we learned Proactive AI is fundamentally harder than reactive AI — knowing when to speak vs. stay silent Vision verification catches dozens of silent failures that "execute and hope" misses Transparent narration (showing what the AI is doing) is more important than the retry logic itself 5 FC tools was the right constraint — fewer choices = more reliable function calling What's next for VibeCat Multi-monitor support and per-app context awareness Plugin system for community-contributed tool declarations Collaborative mode for team pair programming sessions <div