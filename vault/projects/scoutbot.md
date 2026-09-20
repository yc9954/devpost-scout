---
slug: "scoutbot"
url: "https://devpost.com/software/scoutbot"
title: "ScoutBot"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1267
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "domain/education"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/web_dom"
---

# ScoutBot

> Opportunty Resource allocation for nigerian students

[Devpost](https://devpost.com/software/scoutbot) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[human_in_the_loop]]
**domain** [[education]]
**user** [[educator_student]] [[patient_family]]
**substrate** [[web_dom]]

**stack** html, javascript, python, scrapy

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scoutbot

## Body

Inspiration Every week, hundreds of scholarships, fellowships, and internships open for Nigerian students on a national and international scale, with only a few being publicized and taken advantage of—and most of them expire unfound. I built ScoutBot because close friends and coworkers of mine have missed brilliant opportunities like the Afara Initiative program, Microsoft internships, and more. Not because they aren't qualified. Because they find out late, days after the deadline, weeks after it's buried in a blog post I either sent or they stumbled on by accident. That was the moment I realized the problem wasn't the opportunities, as we are always told at events, "Africa needs more opportunities," and we do, but the main problem was the distribution network. Nigeria has over 2 million university students. The average student checks 6–8 different websites, social media groups, and WhatsApp forwards to stay updated. By the time an opportunity surfaces in their feed, it's often already crowded or closed. I wanted to build something that wakes up every morning, does the searching for them, uses AI to filter out the noise, and delivers only the real ones—clean, ranked, and directly to their inbox. What it does ScoutBot is an automated opportunity intelligence bot for Nigerian students. It runs every week at 7am Sunday WAT, completely on its own, with no human in the loop. Here's what happens in each run: Scrapes 7+ Google News RSS feeds for scholarships, fellowships, internships, bootcamps, and exchange programs—both Nigeria-specific and international opportunities open to Nigerians Filters by keyword (must look like a real opportunity listing), publication date (dropped if older than 5 days), and year (no 2024 or earlier results) Scores with Gemini AI—each opportunity is sent to Google's Gemini Flash model with the title, category, and description. Gemini returns a relevance score (1–10) and a 2-sentence subscriber-facing blurb. Items scoring below 5 are permanently dropped before they ever touch the sheet Writes to Google Sheets—surviving items land in a clean 6-column sheet: Title | Category | Application Link | Deadline | Date Added | AI Blurb Cleans expired entries—any entry whose deadline has passed or that has been in the sheet for more than 23 days is automatically removed Sends a weekly email digest every Sunday to subscribers—a clean HTML newsletter with the week's opportunities grouped by region (🇳🇬 Nigeria / 🌍 International), colour-coded by category, with deadline indicators and one-click Apply → buttons The result is a fully automated pipeline that turns scattered web noise into a curated, AI-filtered, dead-link-free opportunity feed, delivered every Sunday morning How we built it The architecture is intentionally simple and cheap—the whole system runs on free tiers: Development: Replit free tier Scraping layer — Python + Scrapy Scrapy handles concurrent RSS fetching with rate limiting, retry logic, and duplicate filtering. Each run fetches 7 Google News RSS feeds simultaneously. Items are filtered in the parse_rss callback before they ever reach a pipeline. A separate YouthHubAfrica scraper handles direct HTML for Nigeria-specific listings. AI scoring layer — Google Gemini Flash scoutbot/gemini_scoring.py is the only file in the repo that talks to the Gemini API. Each item is serialized into a prompt asking Gemini to rate relevance (1–10) for Nigerian students and generate a 2-sentence blurb. Items scoring below 5 are dropped via Scrapy's DropItem exception before they reach Google Sheets. Rate limiting is enforced with a 6-second inter-call sleep and a 3-attempt exponential retry on 429 errors. Storage layer — Google Sheets + gspread SheetsPipeline writes survivors to a Google Sheet with two tabs: Nigeria and International. Schema migration is automatic — if the bot detects an old column structure, it clears and resets headers on the next run. cleanup.py runs after every scrape and removes expired rows using header-name column lookup (robust to schema changes). Delivery layer — Gmail SMTP notify.py builds a responsive HTML email using inline styles, assembles the subscriber list from three sources (environment variable, Google Sheet Subscribers tab, Google Form responses), deduplicates and validates every address, records bounces, and sends via Gmail SMTP with graceful per-address error handling. Scheduling — GitHub Actions The entire system runs on a GitHub Actions cron workflow (0 6 * * * = 7 AM WAT). No server, no VPS, no Replit subscription required. The workflow runs as long as the GitHub repo exists — completely free on public repos. Challenges we ran into Cloudflare blocking on GitHub Actions IPs Major opportunity sites (opportunitydesk.org, afterschoolafrica.com) return Cloudflare challenge pages when scraped from GitHub Actions datacenter IPs, even with a real browser user agent. I switched to consuming Google News RSS feeds (which are Google's own infrastructure and unblocked) and emitting items directly from the RSS data instead of following article links. Google News redirect URLs Google News RSS items link to news.google.com/rss/articles/CBMi... redirect URLs that require JavaScript to resolve to the actual source article. Scrapy doesn't execute JavaScript. The fix: emit items directly from RSS metadata (title + description snippet) and use the redirect URL as the application link—it's functional when clicked and takes the reader to the source article via Google's own reader. Gemini rate limiting on the free tier With 15–25 items per run and a 15 RPM free-tier limit, naïve sequential calls cause HTTP 429 errors. I implemented a monotonic-clock rate limiter (6-second minimum gap between calls) plus a retry loop with 60-second waits on 429 responses, so the bot degrades gracefully under rate pressure rather than failing silently. Subscriber email validation Early digests bounced against corporate email servers. I added a proper validation pipeline: format checking with regex, MX record lookup via dnspython, a persistent "Bounced" tab in Google Sheets that blocks resends to known bad addresses, and per-address error handling in the SMTP loop so one bad address doesn't abort the whole send. Keeping it alive without a paid server GitHub Actions free tier gives 2,000 minutes/month for public repos. ScoutBot uses about 5–8 minutes per run × 30 days = 150–240 minutes/month. It will run indefinitely at zero cost on any public GitHub repo with the secrets configured. Accomplishments that we're proud of 500+ subscribers, the full WhatsApp engine , t Telegram channel and most especially the zero-cost infrastructure. As a student from a middle class background in a lower income country. This is the most impressive feat. To build is to live but being unabe to afford to live can be quite a challenge. What we learned Scrapy's async pipeline model—how process_item interacts with defer.inlineCallbacks vs async def, and why the modern approach matters for Scrapy 2.13+ When to leave AI inetgration out: Gemini was the most technically interesting part of the project and the first thing to get cut. The lesson: AI layers add real value when the problem is genuinely ambiguous. When a budget is tight, simplicity is pirotized, then AI adds complexity without proportionate value. However we were able to leverage AI by using reply AI agent to automate authentication and consistent processing. Prompt engineering for scoring — before cutting Gemini, the prompt went through six iterations. The phrase "Score 7+ ONLY if it is explicitly open to Nigerians or Africans broadly" reduced irrelevant high scores by 40%. Building for longevity—every design decision was made with the question, "Will this still run correctly in 6 months when I'm not looking at it? When I cant afford to fix (e.g laptop breaking down, internet connection issues, etc.) That led to auto-migration logic, header-name column lookups, the 23-day cleanup cap, and persistent bounce tracking. What's next for ScoutBot Every week, hundreds of scholarships, fellowships, and internships open for Nigerian students—and most of them expire unfound. <div