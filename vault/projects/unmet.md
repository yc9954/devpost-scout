---
slug: "unmet"
url: "https://devpost.com/software/unmet"
title: "Unmet"
hackathon: "DevNetwork [API + Cloud + AI] Hackathon 2026"
organization: "DevNetwork"
winner: true
words: 808
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Unmet

> Reviews in, ranked gaps out. Built on nine SerpApi engines: what app users are begging for, what's breaking for the businesses on your street, and whether Google's AI answer cites you.

[Devpost](https://devpost.com/software/unmet) · hackathon [[DevNetwork -API - Cloud - AI- Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[accessibility]] [[finance_payments]] [[labor_employment]]
**user** [[general_public]] [[legal_professional]]
**substrate** [[geospatial]] [[structured_db]]

**stack** claude, cloudflare, convex, gemini, leaflet.js, openrouter, react, serpapi, typescript, vite

## How they structured the write-up

- the problem i actually have
- what unmet does
- the demo, and what it found
- where serpapi does the real work
- how it's built
- what i learned
- what's next

## Body

The problem I actually have I ship iOS apps for a living — fourteen on the store — and I own a restaurant. Both jobs have the same blind spot: the answer to what should I fix next is sitting in other people's reviews, and nobody reads them, because reading them means ten tabs and a sore thumb. Keyword tools tell you what people search. Nothing tells you what people hate about what they found. What Unmet does Two doors, one engine. Build — type an App Store category. Unmet finds the apps ranking for it, reads hundreds of their reviews across two sorts, clusters the complaints and feature requests, and ranks the gaps by mentions × pain × log₂(breadth) — so a complaint shared across six apps outranks one loud app's bug. Every gap carries the users' own words, centred on the sentence that matched. Pulse — name a kind of business and a place. Every morning Unmet reads this week's reviews across Google Maps, Yelp and TripAdvisor for the places like yours, ranks what's going wrong, tells you whether it's already hitting you , checks whether Google's AI answer cites you and which sources it leaned on, prescribes actions from a playbook with the evidence attached, drafts replies (checked by three rules, never auto-sent), and — next Monday — uses the same engines to measure whether what you did moved the number. The demo, and what it found "You" is Stiles Switch BBQ, half a mile up North Lamar from SerpApi's office. Six rivals including Franklin. 491 real reviews on three platforms. The category's number-one gap is dry, tough or bland meat — 80 mentions, all seven places, all three platforms. Stiles is hit on it, on value, and on cleanliness — the three actions on its morning card. And when you ask Google "is stiles switch bbq worth it" , its AI answer says it "rarely ranks as the absolute top brisket in Austin", citing Reddit, Yelp and TripAdvisor. The same finding from two directions — and the morning card turns it into three things to do today. Where SerpApi does the real work Nine engines, every one load-bearing: apple_app_store , apple_reviews , google_maps , google_maps_reviews , yelp , yelp_reviews , tripadvisor , tripadvisor_reviews , google → google_ai_overview , plus google_trends and google_autocomplete for demand. Apple publishes no complaint API; Google's AI answer has no API at all. There is no other data source in the project. Every response is cached in Convex and replayed on identical calls; the cost of every run is on screen, and the quota badge is SerpApi's own account counter, never estimated. Judge accounts are capped at 30 live searches a day and fall back to replay past the cap. One paying customer is roughly 330 SerpApi searches a month, every month — this is a habit product, not a one-shot tool. How it's built Convex holds the database, the cache, the scheduler (one action per business at 05:00 local) and the tables the cockpit subscribes to — the "data streaming in" screen is a live subscription on the calls table, not polling. Convex Auth with roles. OpenRouter for the model (Sonnet 5, Gemini Flash fallback, local template last), called only for words: reply drafts, the morning headline, an optional re-label flagged and compared. The model never writes a score. Every number comes from a regex taxonomy and one deterministic formula, and every experiment verdict is a fixed rule on Monday's read. The frontend is a Vite/React cockpit on Cloudflare Workers; the street map draws SerpApi's own coordinates on a keyless basemap. What I learned A category's own vocabulary looks exactly like a complaint. In a habit tracker, "add a habit" read as a feature request and "tracking habits" read as a privacy violation. In Austin barbecue, "dry rub" is praise, "cold beer" is praise, and "waited two hours and it was worth it" is five stars. None of this was visible in the tests I wrote first; all of it appeared the moment real reviews hit the taxonomy. Every one of those is a regression test now — which is the argument for building on a live search API instead of a curated dataset. Also: Google shows no AI answer for local-intent queries ("best barbecue austin" gets the map pack) and does for informational ones ("is X worth it", "X vs Y"). Both states are real, and Pulse tracks both. What's next Cloudflare Durable Objects as per-business actors with their own alarms; the public gap-index pages; Google Play alongside the App Store; OpenTable where the place is on it. Disclosures: built new during the submission window. Pre-existing: the App Store fixtures were pulled by an earlier Python prototype of the same idea, written this week and kept in the repo as the reference implementation. Solo build, AI-assisted development. <div