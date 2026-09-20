---
slug: "study-flow-ue29iz"
url: "https://devpost.com/software/study-flow-ue29iz"
title: "Study-Flow"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 685
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Study-Flow

> Your intelligent study companion. Track progress, collaborate with peers, and unlock your academic potential with AI-powered insights.

[Devpost](https://devpost.com/software/study-flow-ue29iz) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**user** [[researcher]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** chef, claudecode, convex, heroku, mcp, nextjs, spotify, tweakcn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for study-flow

## Body

Hero Section dashboard study_page_pomodoro_style settings page Groups Discover Page based on interest Group Page with collaboration Inspiration Built StudyMate during mid-semester exams to solve a problem I faced daily – managing study time effectively while juggling academics. The irony? Building a study tool while supposed to be studying. But it taught me more about time management than any productivity app ever could! MentorMind's first advice? "Take breaks more often" – advice I clearly wasn't following while coding at 2 AM. What it does Study-Flow is an AI-powered study management platform featuring: Smart Study Timer : Customizable Pomodoro sessions with automatic tracking and Spotify integration for focus music MentorMind AI Assistant : Multi-agent system (GPT-OSS 120B, Nova Lite, Claude 3.5 Haiku) with RAG architecture for personalized study advice Auth0 Integration : Secure third-party API access via Token Vault (Google Calendar & Spotify live) MCP Tool Support : Automatic external resource fetching – just drop a URL and MentorMind reads it with you Performance Analytics : Visual dashboards tracking study patterns and progress Study Groups : Collaborative workspaces with real-time chat and leaderboards Coin Economy : Gamification system (earn 1 coin/second studying, spend 100 coins/AI query) How we built it Tech Stack: Next.js 14 + TypeScript frontend with Convex real-time database Hybrid auth architecture: Convex Auth for users + Auth0 Token Vault for API tokens Heroku Managed Inference powering multi-agent AI system MCP integration with dynamic tool discovery and SSE parsing Key Innovation: Hybrid auth pattern (undocumented elsewhere) – kept Convex Auth for familiar user login, added Auth0 exclusively for third-party API token management. Zero downtime migration with feature flags. Code Impact: Auth0 Token Vault reduced token management from 120 lines of manual refresh logic to 30 lines of enterprise-grade automation. That's 75% code reduction while upgrading to SOC 2 Type II certified security. Challenges we ran into MCP Integration Complexity : SSE parsing, dynamic tool routing, and understanding Heroku's Agents API took days to crack. The breakthrough came from building a custom SSE parser and provisioning all available tools to the AI. OAuth Understanding : Confused ID tokens, access tokens, and refresh tokens initially. Auth0's docs clarified the differences beautifully. Hybrid Auth Architecture : No documented pattern for combining Convex Auth + Auth0 Token Vault. Designed it from scratch with automatic fallbacks. Balancing Development : Building during exams meant 3-hour sleep nights. Used MentorMind to help me study while building it (meta!). Accomplishments that we're proud of Production-Ready Infrastructure : Heroku-deployed MCP server with 10 working calendar tools, multi-user isolation, rate limiting Hybrid Auth Innovation : Pattern allowing zero-downtime migration between auth systems with feature flag control Spotify Integration Live : Full playback control in study timer with Auth0-secured token management, configurable via settings Collaborative AI Deployed : Shared MentorMind assistants for study groups with full group context and member insights Meta Achievement : Used MentorMind to study for exams while building MentorMind. Got B+ on exam I was supposed to fail! Real Impact : Context-aware AI that checks actual Google Calendar to suggest optimal study times What we learned Don't Reinvent OAuth : Auth0 Token Vault solved token management better than any custom implementation. Just use proven solutions. Hybrid > All-or-Nothing : Keep what works, add what you need. No need to rip out existing auth. Feature Flags Are Magic : Testing Auth0 alongside Convex system gave confidence for safe migration. Good Documentation Matters : Auth0's AI agents docs and Heroku's MCP GitHub examples were excellent. Real Data Testing Reveals Truth : Mock tests are fine, but testing with actual Google Calendar revealed edge cases we'd never find otherwise. What's next for Study-Flow Email/Gmail Integration : Track email-based assignments and deadlines Notion Sync : Import study notes for better AI context Voice Interaction : Hands-free studying for memorization sessions Mobile App : On-the-go study tracking and session management Advanced Spotify Features : Automatic playlist switching based on study intensity and break detection AI-Powered Study Plans : Auto-generated weekly schedules optimized for exam prep Built with: Claude Code (frontend logic), Convex Chef (backend development), TweakCN (theme customization), and Aceternity UI (meteor animations & hover effects) <div