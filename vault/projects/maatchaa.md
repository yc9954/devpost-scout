---
slug: "maatchaa"
url: "https://devpost.com/software/maatchaa"
title: "Maatchaa"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 322
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Maatchaa

> Match your content to the right sponsors with Maatchaa

[Devpost](https://devpost.com/software/maatchaa) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[structured_db]] [[video_visual]]

**stack** blacksheep, cohere, gemini, nano-banana, nextjs, pinecone, python, shopify, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for maatchaa

## Body

Company Sponsorship Approval Dashboard Product showcase Tech Stack Inspiration We love short-form content. Short-form content creators love sponsors. Sponsors love to advertise their products to new groups. The solution? Maatchaa. What it does Maatchaa automatically matches Shopify products with trending YouTube Shorts. Businesses can browse potential creator partnerships, tinder style. Once creators confirm deals, Maatchaa adds the sponsored content for them, automatically generating neat product sets for sponsors. How we built it Backend: Python, Shopify API, YouTube API, vector database for embeddings (text + image). Frontend: Next.js, scrollable “Tinder-style” dashboard for businesses to browse reels and creators. AI & Embeddings: Multi-modal embeddings for videos (Cohere) using Pinecone Gemini for automatic product selection and video analysis Nano Banana (newly released) for AI-generated visuals - product sets, thumbnails, and social-ready imagery that match content style and brand identity Automation: Video analysis → convert video to text + thumbnail Query vector DB → return top matching products Onboard business → push Shopify products to DB → generate product set Creator confirmation → auto-update video description via YouTube Studio API Challenges we ran into Automation of brand deal links while respecting creator control. Matching algorithm balancing engagement, niche, and brand safety. UI design for a scrollable, aesthetic dashboard with multiple product categories. Accomplishments that we're proud of Functional prototype connecting Shopify products to YouTube Shorts using AI. Real-time matching algorithm that categorizes content by viral performance and engagement. AI-generated visual product sets that look professional and compelling. Dashboard that allows both businesses and creators to confirm partnerships seamlessly. What we learned How to integrate multiple APIs (Shopify + YouTube + Gemini/Cohere). How to use vector databases for semantic product matching. Using new image-gen tech like Nano Banana. What's next for Maatchaa Expand to other platforms: Instagram, TikTok, and other platforms. Improve matching AI to include stylistic and aesthetic considerations. Integrate automated reporting and performance analytics for creators and businesses. Monetization options for businesses and creators. <div