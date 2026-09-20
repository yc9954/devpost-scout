---
slug: "editor-decide-with-clarity"
url: "https://devpost.com/software/editor-decide-with-clarity"
title: "Editor: Decide with Clarity"
hackathon: "RevenueCat Shipyard: Creator Contest "
organization: "RevenueCat"
winner: true
words: 668
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# Editor: Decide with Clarity

> Most AI tools encourage endless chat. Editor is a structured thinking system that helps you cut through options, make decisions, and move on.

[Devpost](https://devpost.com/software/editor-decide-with-clarity) · hackathon [[RevenueCat Shipyard- Creator Contest]]

## Facets

**mechanism** [[deterministic_policy]]
**substrate** [[code_repository]] [[document_pdf]]

**stack** docker, fastapi, gemini-api, google-gemini-api, openai-api, python, revenuecat, swift, swiftui

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges
- accomplishments
- lessons learned
- what's next for editor: decide with clarity

## Body

Inspiration Most AI tools today optimize for conversation. They invite you to keep talking, refining, and expanding, often without a clear end. While that’s powerful, it creates a new problem: indecision . Editor was inspired by a common frustration for builders and creators: more ideas and longer chats weren't the bottleneck. Decision-making was. The goal was an AI tool that behaves less like a conversational partner and more like an editor: something that challenges, reframes, and helps you conclude. The guiding question became: What if an AI was designed to end conversations, not prolong them? What it does Editor is a structured thinking system for making decisions. Instead of free-form chat, users start a session by choosing a thinking mode (review an idea, get unstuck, make a decision, prioritize, trade-offs). The AI guides them through a focused, constrained flow designed to clarify the problem, surface trade-offs, and reach a conclusion. Every session is designed to end . When clarity is reached, Unlimited users can turn the outcome into durable artifacts such as: decision briefs goals milestones roadmaps definitions Artifacts can be exported directly to Notion , keeping decisions connected to your workspace and workflows. Sessions are for doing. The Library is for keeping. This separation is intentional and central to the product. How it was built Editor is a native iOS app built with SwiftUI , designed from the ground up with a custom navigation and state system. Key architectural decisions include: A router-driven state machine as the single source of truth for onboarding, mode selection, sessions, and paywalls. Guided input flows instead of chat, to enforce structure and reduce cognitive load. Tiered memory by design: Free sessions are stateless; Unlimited sessions can reference a lightweight user context extracted from prior sessions. A clean information architecture where active sessions and stored outcomes live in separate spaces. On the AI side, Editor uses persona-driven system prompts and thinking modes , not a generic assistant. Each mode is constrained by rules, outputs, and stopping conditions to ensure clarity over verbosity. For monetization, RevenueCat powers a single Unlimited subscription and keeps paywalls context-aware (only shown at clear boundaries like locked modes or session limits). For integrations, Notion provides artifact export via OAuth 2.0, allowing users to send decisions and plans directly to their workspace without leaving the app. Visually, the UI uses a mostly monochrome design with a disciplined single accent color , reserved only for primary actions and system boundaries. Challenges The hardest challenge wasn't technical. It was restraint . Avoiding “just add chat” moments. Preventing accidental feature creep. Designing flows that feel helpful without feeling verbose. Making paywalls feel intentional, not punitive. Ensuring navigation and memory felt trustworthy (and never implied hidden context). Another major challenge was aligning UX philosophy with implementation : making sure that the router, views, and state machine all reflected the same mental model: clarity, endings, and intent. Accomplishments Designing an AI experience that is not a chat , and fully committing to that constraint. A clear, opinionated information architecture: sessions vs library. A navigation system that reinforces thinking as a process , not a feed. Strong visual discipline. No decorative AI vibes, no personality theater. A product that can be explained in one sentence and experienced intuitively in seconds. Lessons learned Constraints make AI products better, not worse. Ending is a feature. Users trust systems more when memory is explicit and controllable. UX philosophy must be enforced in code, not just in Figma. Differentiation doesn't come from more features. It comes from saying "no" clearly. What's next for Editor: Decide with Clarity Next steps include: Expanding thinking modes while keeping strict constraints. Refining artifacts into reusable, composable decision documents. Improving review and reflection flows for past decisions. Exploring collaboration and sharing without turning sessions into chats. Expanding integrations (Notion is just the start). Continuing to refine the balance between power and simplicity. Editor is an experiment in building AI tools that don't just generate content. They help people decide and move on . <div