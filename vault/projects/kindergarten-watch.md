---
slug: "kindergarten-watch"
url: "https://devpost.com/software/kindergarten-watch"
title: "Seamless"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 502
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Seamless

> From screen to closet SEAMLESSLY

[Devpost](https://devpost.com/software/kindergarten-watch) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[finance_payments]] [[retail_commerce]]
**user** [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[video_visual]]

**stack** python

## How they structured the write-up

- inspiration shouldn’t be hard to buy
- what is seamless?
- how it works
- why smart contracts?
- engineering challenges and wins
- personalization
- why this matters
- built with
- what’s next
- final thought

## Body

Seamless — Turn Inspiration Into Instant Purchase Inspiration shouldn’t be hard to buy Every time you watch a movie, scroll TikTok, or binge a show, you see outfits that make you think: “I want that.” But then the moment passes. The scene is gone. The creator isn’t credited. The brand gets exposure but no attribution. And you’re left Googling “black jacket actor episode 3” until you give up. That’s billions of dollars in lost intent. So we built Seamless . What is Seamless? Seamless is a real-time AI shopping assistant that turns anything you watch into a shoppable experience. When you see something you like on screen, you press a button. Seamless instantly: Identifies every clothing item on screen using AI vision Finds the exact product online Lets you buy it in one click Automatically pays the creator who inspired you No affiliate links. No promo codes. No “link in bio.” Just discovery to purchase to commission in one flow. How It Works 1. Real-Time Vision Intelligence We use OverShoot to analyze live video and describe every clothing item visible on screen. 2. Product Matching OverShoot’s natural-language output is passed to Serpur, which matches each item to real products on the Google Store. 3. Trustless Affiliate Commissions We use Kairo AI to generate and validate smart contracts that automatically handle creator commissions. Before any purchase goes through: The buyer commits the product cost The store commits the commission Funds are locked in escrow Only then does the transaction execute. No fraud. No chargebacks. No broken affiliate links. Why Smart Contracts? Today’s influencer marketing is messy: Brands delay payments Creators chase invoices Affiliate links break Attribution is unreliable Seamless replaces all of that with programmable trust. If a creator inspires a purchase, they get paid automatically. Engineering Challenges and Wins Screen Streaming OverShoot only supports camera and video file input, not live screens. We built a workaround using an OBS virtual camera, turning the user’s screen into a real-time camera feed. Item Persistence OverShoot would re-detect the same items repeatedly, creating duplicate results. We solved this by appending: DON’T LOOK FOR THIS: {previous_results} to the prompt, preventing duplicate detection and enabling persistent item tracking. Personalization Users can customize their profile, including style, budget, and preferences. This directly influences product matching and ranking, making Seamless smarter the more you use it. Why This Matters Seamless creates an entirely new advertising channel: Every movie becomes a storefront Every TikTok becomes a shopping mall Every stream becomes a runway Brands get attribution. Creators get paid. Consumers get instant access. Built With OverShoot API for real-time vision-to-language inference Serpur for product matching on the Google Store Kairo AI API for smart contract generation and validation OBS Virtual Camera for live screen streaming Blockchain escrow for trustless affiliate commissions What’s Next Mobile app Creator dashboards Real brand partnerships On-chain settlement Cross-device support Final Thought The future of shopping is not search. It is inspiration. Seamless turns “Where did they get that?” into “It’s already in your cart.” <div