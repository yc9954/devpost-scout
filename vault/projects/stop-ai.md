---
slug: "stop-ai"
url: "https://devpost.com/software/stop-ai"
title: "Stop AI"
hackathon: "Reddit Mod Tools and Migrated Apps Hackathon"
organization: "reddit"
winner: true
words: 1381
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Stop AI

> Stop AI rebuilt on Devvit Web with Stop Bots and Repost Intel apps folded in. AI auto-scan, cross-community repost tracking, BotBouncer routing, mod automation playbooks. Live on 460+ subreddits.

[Devpost](https://devpost.com/software/stop-ai) · hackathon [[Reddit Mod Tools and Migrated Apps Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** devvit-web, hono, node.js, postgresql, react, reddit, redis, supabase, tailwind-css, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments i'm proud of
- what i learned
- what's next for stop ai

## Body

Polished dashboard interface A planned feature after the hackathon Subreddit dropdown featuring difference between premium and non-premium Skeleton UI loading on Dashboard Light theme optimization Skeleton UI loading on Splash screen (Installed subreddit view) Multiple animated surfaces displaying sleek luxury design on the Splash screen Quick Note: You will need to update to the latest version or install the app to a subreddit before you are able to test its features, and primarily the "Command Center" dashboard where the app lives and breathes. Inspiration Mod tooling on Reddit had become fragmented. I had built two separate Devvit apps, Stop Bots and Repost Intel, that were solving related problems with completely separate codebases, separate UIs, and separate install footprints. A moderator who wanted AI detection, bot flagging, and repost matching had to install and learn three different things. That felt wrong. At the same time, the "AI detection" space was full of black-box tools claiming 98% accuracy with no explanation of how they worked. I didn't trust them, and I suspected moderators shouldn't either. I wanted to build something deterministic and explainable, where every flag comes with a reason a mod can actually evaluate. The hackathon was the forcing function to consolidate. I rebuilt Stop AI on Devvit Web by migrating it from Devvit Blocks and absorbed the full toolkits of both sibling apps into one installation, one dashboard, one permission model. What it does Stop AI is a moderation assistant for Reddit communities. When a post or substantial comment goes up, Stop AI runs it through OpenClaw, my in-house deterministic detection framework, and routes high-confidence hits to the mod queue with a plain-language reason. Nothing gets silently removed by default. Mods stay in control. The free tier covers AI auto-scanning (posts and comments), typographic signals like em-dash usage, bot accusation routing via BotBouncer through modmail, and posture presets (Light, Standard, Strict) so each community can set its own sensitivity level. Everything is managed from a shared Command Center dashboard accessible right from each sub's mod menu. Two premium add-ons are available via Reddit Gold. Repost Detection (250 Gold) fingerprints text, titles, URLs, and image bytes to catch cross-sub reposts. Playbooks Automation (150 Gold) is an if/then rule engine: if a post matches a condition, do something from a menu of actions (remove, report, flair, add a mod note, send modmail, escalate to BotBouncer). Both are available as a bundle for 350 Gold. A team panel lets the account owner (Root Admin) manage a roster of collaborators with four permission tiers (Root Admin, Master Admin, Admin, Member), control per-module kill switches, run upgrade broadcasts to 463+ modmail inboxes at once, and review broadcast logs. How I built it The app runs on Devvit Web. The backend is a Hono server hosted inside Devvit's infrastructure. The frontend is Vite, React 19, and Tailwind 4. I styled it as "GameChanger OS," a dark-first design system: #0f1115 backgrounds, Reddit OrangeRed ( #ff4500 ) for urgent actions, gold ( #f5a524 ) for premium surfaces, and Inter as the base typeface, all tokenized in theme.css and mapped through Tailwind's @theme directive. Durable state lives in Supabase (Postgres). Hot caches, queues, and ephemeral per-sub state run on Devvit Redis. Entitlement gates use Reddit Payments. The dashboard is a single Devvit custom post hosted on r/bricksapps, deep-linked from each sub's mod menu via a ?from=<sub> query param so every one of 463 installs shares one source of truth. OpenClaw, my detection framework, has 5 core agents, 12 heuristic library wrappers, 3 Phase-3 repost scaffolds, and 20 registered handlers total. No third-party LLM is in the hot path. That means no per-event API cost, no rate-limit risk, and no content leaving the app's controlled surface. Challenges I ran into The biggest structural bug was a host-fallback problem in the webview. When a mod opened the dashboard via ?from=somesubreddit , the server was falling back to context.subredditName , which always resolved to r/bricksapps (the host sub), not the mod's actual community. Every settings read and write was silently scoped to the wrong sub. Fixing it required a requireModForSelectedSub server-side helper and a per-sub overview hook on the client, touching about 25 files across the app. The second crisis was a trigger-handler crash. When a comment came from a deleted or suspended Reddit account, authorName was undefined. A downstream .toLowerCase() call in my moderator-check helper threw a TypeError. The handler returned HTTP 400. Devvit retried. The result was roughly 1 crash per second on any affected sub. The fix had two parts: null-guards on all mod-check helpers, and a structural change to return HTTP 200 on any inner exception. A bad event can now fail silently and move on instead of amplifying into a retry storm. Third: a code-vs-schema mismatch on repost fingerprints. The live pipeline was reading and writing per-sub slice columns against the cross-sub canonical repost_fingerprints table. PostgREST returned a 42703 (undefined column) error every time. I fixed it by introducing a dedicated repost_fingerprint_slices table. The most operationally surprising thing I hit: the dashboard's JS bundle is served from the r/bricksapps install, not from each sub's own install. I uploaded 9 versions of fixes (v0.0.162 through v0.0.170) over a week, and every one of them sat dormant because I hadn't clicked "Update" on r/bricksapps itself. One click there activated all 9 versions of UI fixes for 470+ installs simultaneously. Accomplishments I'm proud of Stop AI is live on 470+ subreddits, and the architecture scales to more without per-install work on my end. The "return 200 on inner throw" structural change is something I'm genuinely proud of. It's a small pattern change that makes any future single-event bug unable to amplify into a retry storm. I should have done it earlier. OpenClaw's deterministic approach means every flag is explainable. A moderator can look at a report and see exactly which signals fired and why. No black box, no confidence percentage that means nothing in context. The cross-sub repost fingerprinting pipeline, once I got the schema right, works across text, titles, URLs, and image bytes simultaneously. The team panel with four permission tiers means large moderation teams can operate Stop AI without giving everyone root access. The upgrade notifier now lets me broadcast a modmail to all 463 mod teams at once when I ship a meaningful change. What I learned The dashboard-bundle-lives-on-the-host-sub mental model is something every Devvit Web developer needs to internalize early. It's not obvious, and learning it via 9 versions of dormant fixes was an expensive lesson. Now it's the first thing I check before declaring a UI bug fixed. Returning HTTP 200 on any inner exception is the correct default for Devvit trigger handlers. A 400 response tells Devvit to retry. A 200 response lets it move on. If you want visibility into inner failures, log them, but don't let a single malformed event generate hundreds of retries. Context fallbacks are dangerous. Ambient values like context.subredditName feel convenient until they silently resolve to the wrong thing in a shared-host architecture. Explicit validation helpers (the requireModForSelectedSub pattern) are worth the extra boilerplate from the start. Schema work deferred until late is expensive. The repost fingerprints mismatch cost me a live pipeline failure that could have been caught if I had written the migration before the code that depended on it. What's next for Stop AI Repost Detection currently does byte-exact image matching. I want to add perceptual hashing so visually similar images with minor edits are caught too. I'm considering an optional LLM "second opinion" SKU, gated to cases where OpenClaw's signal scores land in an uncertainty band. It would be cost-controlled, opt-in, with hard caps per sub and a Root Admin kill switch. It would never claim authorship-proof, just flag the case for a human. I want to close the feedback loop between moderator outcomes and detection thresholds. Right now, when a mod approves or removes a flagged item, that signal disappears. Wiring it back into threshold tuning over time would make the system smarter for each community. Two infrastructure items are on the list: a "Cleanup-After-Mod-Removal" trigger workaround for the fact that Devvit doesn't expose an onAppRemove event, and an app_version column written back to the database on every install and upgrade trigger so I always know exactly which version is running on which sub. <div