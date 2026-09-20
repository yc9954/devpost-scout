---
slug: "confidfit"
url: "https://devpost.com/software/confidfit"
title: "ConfidFit"
hackathon: "YouCam API Skin AI & Apparel VTO Hackathon "
organization: "Perfect Corp"
winner: true
words: 430
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/legal_professional"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ConfidFit

> ConfidFit adds YouCam generative apparel try-on to Shopify. Shoppers preview looks from a photo; merchants run a real product with metering, analytics, and honest labels.

[Devpost](https://devpost.com/software/confidfit) · hackathon [[YouCam API Skin AI - Apparel VTO Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[labor_employment]] [[retail_commerce]] [[transportation]]
**user** [[legal_professional]] [[small_business]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** fly.io, node.js, postgresql, prisma, react, shopify, typescript, youcam

## How they structured the write-up

- what this is
- why we built it
- how it works (youcam + shopify)
- what we learned
- challenges
- live proof

## Body

What this is ConfidFit is a Shopify app for fashion brands. Shoppers open Try on on a product page, upload a photo, and get a generative apparel preview from Perfect Corp's YouCam Apparel VTO API (cloth-v3). Merchants enable products in admin, pay SaaS plus metered successful try-ons, and see usage and purchase-confidence analytics when there is enough traffic. The preview always carries an Honest Label: visual preview only. It is not a fit guarantee. Why we built it Online fashion still makes people guess how a garment will look on them. That guess is bad for shoppers and expensive for brands. We wanted try-on that is good enough to help a buying decision, honest about limits, and real enough to run as a paid product on Shopify, not a one-page demo that calls an API once. How it works (YouCam + Shopify) Shopper path: Theme App Block on the PDP, consent, photo upload, then an async YouCam task. ConfidFit polls through a completion worker and shows the result in the storefront modal. Server path: browser talks to Shopify App Proxy, then ConfidFit, then YouCam. API keys never go to the browser. Category map for cloth-v3: tops and outerwear to upper_body, dresses to full_body, bottoms to lower_body, shoes to shoes. Intimate and swim stay blocked on purpose. Merchant path: go-live checklist, product enablement, trial and paid plans, soft usage warnings, hard caps, fair-use limits so one shopper cannot burn the budget, and cohort analytics that refuse fake lift when sample sizes are too small. What we learned A thin wrapper around one YouCam call is not enough for retail. Most of the work is entitlement, billing honesty, webhooks, abuse controls, retention scrub, and production ops (Fly web + worker). Pose detection also rejects synthetic test squares. Real person photos matter for dogfood. We also learned that product language has to stay careful. No "perfect fit," no invented conversion percentages. Judges and merchants both notice when the copy overclaims. Challenges Shopify App Proxy auth, long YouCam tasks without hanging the storefront, billing planes (live vs test) that must not confuse production shops, and multi-category garment refs that still look right on cloth-v3. Worker health and migrate-on-boot race conditions showed up under real deploy load and had to be hardened in production. Live proof Marketing: https://confidfit.com Shopify App Store: https://apps.shopify.com/confidfit Source code for judging is a private product snapshot (not open source): https://github.com/Argolinhas/ConfidFit-youcam-judging Read access is shared with the hackathon organizers as required by Devpost. Built for the YouCam API Skin AI & Apparel VTO Hackathon under the Apparel Virtual Try-On track. <div