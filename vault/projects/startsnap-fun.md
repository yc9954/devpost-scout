---
slug: "startsnap-fun"
url: "https://devpost.com/software/startsnap-fun"
title: "startsnap.fun"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 1368
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# startsnap.fun

> Startsnap.fun is a platform for the #buildinpublic movement, where vibe coders can showcase their projects, document their journey, and connect with a real, onchain creator economy powered by Algorand

[Devpost](https://devpost.com/software/startsnap-fun) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[labor_employment]]
**user** [[general_public]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** algorand, bolt.new, gemini, netlify, sonner, supabase, tailwind

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for startsnap.fun

## Body

Landing page Send tip in ALGO Projects discovery Inspiration My inspiration comes from the heart of the #buildinpublic movement. As a vibe coders, we live on Twitter, sharing snippets of progress, celebrating small wins, and searching for feedback. But Twitter is a great firehose and a terrible library. Progress is scattered, context is lost, and meaningful support is limited to likes and retweets. I wanted a home. A place designed for the "Vibe Coder" - the builder who believes the story of the build is as important as the final product. A platform that treats the journey as a first-class citizen and empowers creators to connect with a community that genuinely cares about their process. What it does startsnap.fun is a community platform where creators can: Showcase Their Work: Post projects as either "Ideas" or "Live" products, complete with galleries, links, tech stacks, and tags. Document Their Journey: Keep a "Vibe Log" for each project - a Markdown-enabled journal for updates, challenges, and breakthroughs. I even integrated an AI assistant that lets you brain-dump your notes and have them instantly polished into a well-structured entry. Engage with a Real Community: Give and receive detailed, threaded feedback. All platform activity - new projects, user joins, feedback, and support are broadcast to the "Community Pulse," a live feed that makes the platform feel alive. Support Projects They Vibe With: Give and receive support "likes" that help projects trend and climb the popularity ladder. Build a Creator Economy: This is the core of my hackathon entry. I've built the foundational layer of a creator economy using Algorand. Creators enable tipping across all their projects with a single action: connecting their Pera wallet in their user profile. This makes them instantly eligible to receive direct, peer-to-peer tips in ALGO or USDC from any supporter on the platform, turning community appreciation into tangible, real-world support. Example of the project you can support with tips is our own startsnap: https://startsnap.fun/projects/startsnapfun (you will see "TIP CREATOR" button as the owner of the project has wallet address for tips added in their profile). How I built it This project was built from the ground up with Bolt.new for the Bolt.new hackathon with a focus on a modern, robust, and scalable stack: Frontend: React with Vite, initiated in bolt.new from a Figma design. All routing is handled by React Router. UI/Design: I implemented a consistent Neobrutalist design system using Tailwind CSS, building out a library of reusable components to maintain a cohesive look and feel. Backend & Database (The Supabase Workhorse): Supabase was my workhorse for this entire project. I'm using its full suite of features: Auth: For secure user management, including email/password and Twitter OAuth. Storage: For hosting all user-uploaded project screenshots. I'm also using Supabase's image transformation CDN to serve optimized, resized images on the fly. PostgreSQL Database: The single source of truth for all user profiles, projects, vibe logs, and feedback. Row-Level Security (RLS): RLS policies are enforced throughout to ensure users can only modify their own data. Database Functions & Triggers: The Community Pulse is powered by database triggers that log every meaningful action. From a new project to a new tip - into a dedicated activity_log table. Edge Functions: The "AI Magic" button invokes a Deno Edge Function that securely calls the Gemini API to format user content. Blockchain Integration: The creator economy is powered by Algorand. A major focus was creating a seamless, QR-code-based connection that lets users interact directly with their Pera mobile wallet. This allows all transactions to be constructed in the browser and signed securely on the user's own device, maintaining a fully non-custodial experience. Challenges I ran into The Desktop-to-Mobile Wallet UX: My biggest technical challenge wasn't the blockchain itself, but creating a tipping experience that was intuitive for a user on a desktop whose wallet is on their phone. I spent significant time refining the TippingDialog flow to make the QR code connection, currency selection, and transaction signing feel simple. Real-time Activity at Scale: My initial plan was to use WebSockets for the Community Pulse. I quickly realized this introduced significant complexity. I decided to pivot to a smart, polling-based system that provides a near-real-time feel without the infrastructure overhead - a trade-off for an MVP. Knowing When to Stop: The temptation during a hackathon is to just keep adding features. My biggest challenge was calling the scope "frozen" after the tipping feature was implemented. This allowed me to deliver a stable MVP. Accomplishments that I'm proud of The Tipping Feature Just Works. I successfully built a full, end-to-end peer-to-peer payment system on Algorand that is fast, cheap, and has a great user experience. It's the technical and visionary core of my submission. The "AI Magic" Button. Integrating a serverless function to help users write better is a feature I'm really proud of. It lets you brain-dump unstructured thoughts and lets AI do the magic of formatting - a real accelerator for the "Vibe Coder" workflow. A Living MVP with a Unique Identity. I had an absolute blast designing and building the app's Neobrutalist UI. Creating the custom ConfirmationDialog and TippingDialog from scratch to ensure they felt tangible and on-brand was a major highlight. More importantly, startsnap.fun isn't an empty shell. I took the time to seed the platform with projects curated by the VibeScout account, so on day one, it's already a living, breathing product. What I learned The Database is an Active Engine, Not a Passive Store. My approach shifted to pushing key processes directly into the database using Supabase. By leveraging PostgreSQL functions and triggers to automatically manage the activity feed and update support counts, the data layer itself became an active, event-driven part of the application. It’s a more robust and surprisingly fast way to build core social features. Web3 Tooling is Finally 'Just Works' Tier. Going into this, I assumed the blockchain integration would be the most complex part. I was wrong. The Algorand ecosystem, especially the @txnlab/use-wallet-react library, made the whole process incredibly straightforward. The Pera Wallet QR code connection worked out-of-the-box, proving that an intimidating "crypto feature" is now a well-documented integration task. It's all easy in hindsight. A Polished MVP Beats a Rushed one. The best decision I made was to stop adding features and pivot entirely to polishing. A stable, core experience is infinitely more valuable than a sprawling, fragile one. What's next for startsnap.fun With the tipping payment rail in place, the path is clear to build an ecosystem that turns a builder's work into real opportunities. The Talent Hub: A Living Resume. My number one priority is building a dedicated discovery portal for recruiters and collaborators. Instead of a static resume, they will be able to search for Vibe Coders based on the tangible accomplishments they've showcased on startsnap.fun . A Rich, Verifiable Reputation System. The Talent Hub will be powered by a badging system that rewards meaningful actions. We'll award badges for achievements like: "Shipped an Idea to a Live Project," "Top Feedback Provider," or "Serial Snapper." To make these achievements portable, I'll explore minting them as Algorand NFTs, for on-chain verification. Feedback Bounties: The Economic Engine. To accelerate this reputation-building, I will introduce Feedback Bounties. Creators can post an ALGO or USDC bounty to get expert feedback on their projects. My plan is to implement this in two phases: Phase 1 (The MVP): I will first facilitate this with a platform-managed escrow system . Secure Supabase Edge Functions will verify when a creator funds a bounty into a platform wallet and will automatically handle the payout to the feedback provider upon the creator's approval. Phase 2 (The Future): This MVP approach paves the way for a fully decentralized version built on a dedicated Algorand smart contract . This will remove the platform as a trusted intermediary, creating a truly trustless system where the bounty rules are enforced by code. Fulfilling these bounties will be a primary way for users to earn expert-level badges, creating a powerful loop where providing value directly translates to a stronger professional profile. I believe startsnap.fun has the potential to become the definitive home for the next generation of builders: vibe coders. This hackathon was just the beginning. <div