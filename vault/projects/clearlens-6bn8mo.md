---
slug: "clearlens-6bn8mo"
url: "https://devpost.com/software/clearlens-6bn8mo"
title: "ClearLens"
hackathon: "Mind the Product presents World Product Day: Everyone Ships Now"
organization: "Mind the Product"
winner: true
words: 477
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# ClearLens

> Your contacts cost too much and you're wearing them too long. ClearLens fixes both.

[Devpost](https://devpost.com/software/clearlens-6bn8mo) · hackathon [[Mind the Product presents World Product Day- Everyone Ships Now]]

## Facets

  <sub>weak: retail_commerce</sub>
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** antigravity, dart, flutter, node.js, python, supabase, vercel

## How they structured the write-up

- built solo, with ai as a core part of the workflow.

## Body

hero page catalog app novus novus dashboard Inspiration I wear contact lenses myself. Two things annoyed me constantly: forgetting how long I'd had a pair in, and realising mid-checkout that I was probably overpaying without knowing it. I looked for an app that solved both: something that tracked wear time and compared prices across retailers. Nothing existed. So I built it. What it does ClearLens is a two-part product for contact lens wearers. The website (clearlensapp.com & clearlens.ie) scrapes live prices from the majority of optical retailers in Ireland and the UK. You search your lens brand, apply filters, and instantly see where to buy cheapest without manual tab-switching. The mobile app tracks your lenses. You log when you put a pair in, and the app counts down based on your lens type (daily, monthly, extended wear). It notifies you before the safe wear limit. It also tracks your stock and sends a low-stock alert two weeks before you run out with a direct link to the cheapest current price for your brand. No subscription. No in-app purchases. Monetisation is purely affiliate, commission on orders placed through links on the site. Lentiamo is already integrated; more retailers are in the pipeline. How I built it Built solo, with AI as a core part of the workflow. Google Gemini coding agent — architecture decisions and code generation throughout Python — custom scrapers for retailer price data TypeScript — frontend website Dart / Flutter — mobile app Supabase (PostgreSQL) — database and backend Vercel — site hosting and deployment Novus.ai — user analytics and session tracking Awin, Commission Junction, Partnerize — affiliate networks Challenges I ran into Scraping real retail sites at scale is messier than it looks. Every site has a different structure, anti-scraping behaviour varies, and keeping price data fresh and accurate is an ongoing engineering problem is not a one-time setup. Getting up-to-date data from a dozen different retailers without breaking every time they update their frontend was the hardest technical part of this build. On the app side: implementing background tasks and local notifications correctly in Flutter required going deeper into platform-specific behaviour than I expected. What I learned Shipping forces decisions that planning never does. I had this idea for a while, but the hackathon deadline made me commit to an architecture, cut features that weren't ready, and actually deploy. The biggest lesson: a working product with three features beats a perfect product that doesn't exist yet. I also learned that real user behaviour (via Novus ) looks nothing like what you assume during development. What's next for ClearLens App Store and Google Play release Expand price coverage to more UK retailers Activate additional affiliate partnerships (applications pending with several major retailers) Build the price monitoring / alert feature based on first user feedback Grow the audience - Instagram content is already live <div