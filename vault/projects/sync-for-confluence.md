---
slug: "sync-for-confluence"
url: "https://devpost.com/software/sync-for-confluence"
title: "Sync for Confluence"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 902
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "domain/media_journalism"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Sync for Confluence

> Write and maintain your content in Confluence. Sync it to Zendesk so your knowledge base always stays up to date.

[Devpost](https://devpost.com/software/sync-for-confluence) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**mechanism** [[provenance_signing]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[housing_homeless]] [[media_journalism]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** forge, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sync for confluence

## Body

Getting started screen Global configuration Space settings Sync mode Keep your Knowledge Base in the fast lane: Automatically sync Confluence documentation to Zendesk. Inspiration The idea was born from a real-world pit stop. A customer asked if our existing product, Released, could publish to Zendesk. We didn't have a native integration, so we suggested a workaround: "Publish to Confluence, then sync to Zendesk." We assumed there were plenty of apps on the Marketplace to handle that second leg of the journey. To our surprise, we couldn't find a solution that met the standard of speed and precision we expected. I decided to "vibe code" a Proof of Concept using NextJS. However, I quickly hit a wall: building a multi-tenant, secure, distribution-ready infrastructure is a massive undertaking... like trying to build an F1 car from scratch when you just want to race. That’s when I turned to Atlassian Forge. Forge already handles the infrastructure, security, and auth, allowing me to focus purely on the logic. As a Product Manager who hasn't written code in years, I saw this as the perfect challenge to test the limits of Rovo Dev and see if an AI-assisted workflow could help me build a production-ready app in record time. What it does Sync for Confluence eliminates the friction between internal documentation (Confluence) and customer-facing support (Zendesk). It acts as the bridge that keeps your external knowledge base perfectly aligned with your internal source of truth. Key Features: Granular Control: Administrators can connect a Zendesk account and map specific Confluence Spaces (or subsections of spaces) to specific Sections in the Zendesk Knowledge Base. Automatic Synchronization: Once configured, the app works like a finely tuned engine. Triggers capture events (Page Created, Updated, Archived, or Deleted) and immediately reflect those changes in Zendesk. Manual Override: A "Sync Now" button allows Space Admins to manually push changes if needed. Rich Content & Media: It doesn't just sync text; it handles images securely, uploading and natively embedding them into Zendesk so they are visible to external customers without permission errors. Audit Logging: A transparency log tracks exactly which pages were synced and when. How we built it We built this app on the Atlassian Forge platform to leverage its serverless infrastructure and security. The AI Co-Pilot (Rovo Dev):' This project was heavily accelerated by Rovo Dev. Since I am a rusty coder, I used Rovo to scaffold the initial project structure, generate the React UI components, and handle the boilerplate for Forge triggers. Agent Configuration: We utilized the Forge MCP (Model Context Protocol) to help the agent understand the project context and deployment process. Iterative Coding: I used Rovo to write the sync logic, specifically asking it to refactor large functions into smaller, reusable components to avoid technical debt. The Tech Stack: Forge Custom UI: For the configuration screens and logs. Forge Triggers: To listen for Confluence events (avi:confluence:page:created, etc.). Zendesk API: For pushing content and managing article hierarchy. Challenges we ran into Every race has its sharp turns, and we hit a few: Zendesk OAuth Limitations: We initially attempted a standard OAuth flow. However, Zendesk's architecture does not support dynamic callback URLs easily, which conflicted with Forge's environment. We had to pivot our authentication strategy to ensure a secure connection without breaking the user experience. AI Hallucinations & Permissions: While Rovo Dev was powerful, it sometimes struggled with the nuances of the Forge Permission scopes. Specifically, it got confused about retrieving attachments "AsApp" during asynchronous event triggers. It initially claimed it wasn't possible! The 20/80 Rule: The last 20% take 80% of the time. Rovo Dev is excellent at logic, but AI agents still struggle with high-end UI/UX polish. Building custom animations and a "non-generic" look required me to step in and manually refine the frontend code to meet our design standards. Integration testing: Establishing integration tests for Forge is inherently challenging. Introducing an additional service while maintaining state across all components is tricky to say the least. Accomplishments that we're proud of Speed to Ship: Going from zero to a fully functional, multi-tenant app in just two weeks is our biggest win. Breaking the "PM" Barrier: Proving that a Product Manager who hasn't coded in years can use Rovo Dev + Forge to build a legitimate, deployable software product. Solving the Image Problem: Successfully solving the technical challenge of securely extracting images from internal Confluence storage and re-uploading them to Zendesk so they render correctly for public users. What we learned Rovo Dev as an Accelerator, not a Magic Wand: Rovo speed up development immensely, but it requires a "Lead Developer" mindset. You must give it specific instructions on structure (DRY principles) or it will generate messy code. Documentation is King: When the AI struggled with specific API parameters, feeding it the raw documentation immediately fixed the issue. It reinforced that AI is only as good as the context you give it. The Pareto Principle is Real: I had a working prototype in 2 days. The remaining 12 days were spent on the details. Error handling, edge cases, and UI polish. What's next for Sync for Confluence We are treating this as a launchpad, not a finish line. Public Launch: Releasing the "Standard" edition of Sync for Confluence to the Atlassian Marketplace. Multi-Platform Expansion: We designed the codebase with a modular "destination" architecture. Next up is building connectors for Intercom and Freshdesk, as our customers have already requested these. <div