---
slug: "someday-vzdi0f"
url: "https://devpost.com/software/someday-vzdi0f"
title: "SOMEDAY"
hackathon: "Mind the Product presents World Product Day: Everyone Ships Now"
organization: "Mind the Product"
winner: true
words: 1242
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/media_journalism"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# SOMEDAY

> A museum for unfinished work. Dump your abandoned project, get an AI exhibit card, browse by wing, and let others request to continue it via chat.

[Devpost](https://devpost.com/software/someday-vzdi0f) · hackathon [[Mind the Product presents World Product Day- Everyone Ships Now]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[legal_justice]] [[media_journalism]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** better-auth, drizzle-orm, neon-(serverless-postgres), next.js-16-(app-router), openrouter-api, react-19, shadcn/ui, tailwind-css-4, typescript, vercel, vercel-blob, zod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for someday

## Body

landing exhibit novus-integration Inspiration Most of us carry around a graveyard of half-finished work. A side project that stalled after the MVP, a novel stuck at chapter three, a design system that never shipped, a band demo that never got recorded. These things usually end up in a private folder, a dead GitHub repo, or just memory. Deleting them feels wrong. Sharing them on Twitter or LinkedIn feels performative. There's no neutral place to say: this existed, it mattered to me, and here's where it stopped. Someday started from that gap. Not a productivity app telling you to "just finish it." Not a startup pitch deck factory. A museum. A calm, public archive where abandoned creative work gets a proper exhibit card and a chance at a second life. The emotional bet is simple: unfinished work deserves dignity, and sometimes the right stranger is exactly who should pick it back up. We built this for the Mind the Product - World Product Day hackathon. Solo, in roughly 6-10 days. From an idea to execution What it does Someday is a public gallery of unfinished projects. Creators sign up with a real username, submit something they abandoned, and publish it as an exhibit : a structured museum plaque with four fields (what it was, why it stopped, and what it could have been). The museum structure Exhibits live in four wings , each with its own browse page: Products : apps, websites, tools, side businesses, prototypes Art : visual art, music, photography, design Scripts : novels, screenplays, poems, lyrics Everything Else : the catch-all for anything that doesn't fit the above The home page acts as a museum lobby: hero copy, live count of archived projects, entry points into each wing, and a feed of recent exhibits. Submitting an exhibit The submission flow is a 5-step wizard: Choose a wing where this project belongs in the museum Describe what you abandoned with a freeform text dump (minimum 50 characters), plus optional image uploads and external links Generate your exhibit card where AI drafts a museum plaque from your words, or you skip AI and write manually Review and edit so you control the final copy before anything goes public Publish and toggle whether you're open to someone continuing the work AI is deliberately one step in the flow, not the product itself. The curator drafts; the human publishes. Browsing and discovery Each wing page is a paginated gallery with: Text search across exhibit titles and body copy "Open to collaboration" filter to surface only exhibits where the creator wants continuation requests Exhibit cards showing title, excerpt, creator username, wing, and collaboration status Exhibit detail pages read like museum plaques: structured sections, optional image gallery, external links, creator profile link, and a collaboration badge when applicable. Request to Continue If an exhibit is open to collaboration, any signed-in visitor can click "Request to Continue." That creates (or reopens) a conversation thread tied to that specific exhibit and redirects to an in-app chat with the original creator. The thread always carries context: which exhibit it's about, who the other person is. The conversation starts with shared ground instead of a cold DM. Creators manage incoming requests from a Messages inbox. Unread state is tracked per side of each conversation. Profiles and ownership Every user gets a public profile at /u/[username] showing their bio and published exhibits. Creators can edit or unpublish their own exhibits after publishing. Visitors can report exhibits they find inappropriate; admins get a moderation queue to review reports and hide content. What we intentionally left out No likes, streaks, or follower counts. No payments or IP transfer. No file hosting for the actual unfinished codebase (links out if needed). The product is a conversation starter, not a legal handoff platform. We wanted it to feel like walking through a gallery, not scrolling a feed. How we built it Stack Next.js 16 (App Router) with React 19 TypeScript throughout Tailwind CSS 4 + shadcn/ui for a calm, editorial UI Neon (serverless Postgres) as the database Drizzle ORM for schema, migrations, and typed queries Better Auth for email/password auth with public usernames OpenRouter for AI exhibit card generation Vercel Blob for image uploads Zod for validating API payloads, form data, and AI responses Vercel for deployment (live at someday.curr.xyz ) Data model The core entities map cleanly to the product loop: User : email, username, bio, avatar, role (user/admin) Exhibit : wing, title, three plaque fields, collaboration flag, publish status ExhibitMedia : images and links attached to an exhibit Conversation : one per exhibit + requester pair (unique constraint prevents duplicate threads) Message : persisted chat messages with sender and timestamp Report : user-submitted flags on exhibits for admin review Indexes are tuned for the main read paths: browsing by wing + status + recency, fetching messages by conversation, and looking up a user's exhibits. Challenges we ran into AI output reliability. LLMs don't always return valid JSON on the first try. We added response_format: json_object , a strict Zod schema, and a manual fallback path. The generation step is optional by design. Users can skip it entirely. Username-based identity with Better Auth. Email login is standard; public usernames at a stable /u/[username] URL took more wiring. Sign-up requires picking a username, and profiles are a first-class part of the product, not an afterthought. Chat that feels alive on a budget. Polling has edge cases: duplicate messages on merge, scroll position, stale unread counts. Getting incremental fetches and read-state updates right without WebSockets took more iteration than expected. Moderation for a public platform. Once exhibits are public, you need a way to handle bad content. We added user reporting and a basic admin queue rather than building a full moderation system. Accomplishments that we're proud of Shipped the complete product loop : submit, AI draft, edit, publish, browse, request to continue, chat. All working end to end. Four browsable wings with search, pagination, and collaboration filtering AI-assisted submission with a human in the loop . The creator always reviews before publishing. Persistent in-app chat tied to exhibits, with unread tracking and conversation context Public creator profiles with exhibit grids and collaboration badges Image uploads on exhibits via Vercel Blob Edit and unpublish for exhibit owners Admin moderation for reported content Deployed and usable at production URL, not just localhost What we learned AI works best as a single step, not the whole product. Exhibit card generation is a focused, bounded task with a clear schema. That's where LLMs shine. The museum (browsing, profiles, chat, trust) is still a normal web app. Polling is underrated for v1 chat. We spent zero time on WebSocket infra and still shipped a working messaging loop. Good enough is sometimes the right call when you're on a deadline. Schema-first development pays off. Drizzle for the database, Zod at API boundaries, and typed queries meant fewer bugs when wiring auth, exhibits, conversations, and messages across server actions and route handlers. What's next for Someday Voice note submission so people can record instead of type. Real-time chat and notifications when someone requests to continue your exhibit. Better discovery with full-text search and featured exhibits on the lobby page. And more of the museum feel: subtle transitions between wings, clearer community guidelines, faster moderation. The long-term vision stays the same: a quiet public place for unfinished work, and occasionally a bridge between someone who stopped and someone who wants to start. <div