---
slug: "dripped-personal-stylist"
url: "https://devpost.com/software/dripped-personal-stylist"
title: "Dripped"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 931
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Dripped

> The answer to "What to Wear?" is here. With Dripped, upload your pieces, get daily outfit recommendations, curate new outfits - never waste hours each morning in front of your closet.

[Devpost](https://devpost.com/software/dripped-personal-stylist) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[developer_tools]] [[labor_employment]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** bun, cloudflare, coderabbit, revenuecat, swiftui

## How they structured the write-up

- inspiration
- what it does
- how i solo-built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for dripped

## Body

Inspiration I am a bad dresser, and I always waste time every day trying to pick an outfit, checking if the color combination matches and what accessory to tag the outfit along with, to solve the color combo problem, I'd ask ChatGPT if it's good and if shirt A would go with shirt B. Sometimes, I would be very under dressed for an meeting due to putting up an outfit at the last minute, and I couldn't wait for minutes for ChatGPT to finish loading or upload each piece to it every time. So to solve all this and more, I built Dripped! What it does Add pieces : Normal : Point and Shoot Split : Add 2 pieces at the same time by laying them up and down. Extract : Click a selfie and uses AI to extract the pieces that your wearing as a product image. Recommendations : Up to 5 Daily Outfit recommendations per day in sync with your calendar so if you have a meeting at 10, and a concert at 9 the outfits are already pre planned Closet Tagging : Each piece in your closet is analyzed and intelligently tagged with brand, material, occasions, colors, fit and more. OOTD Track : Marking your Outfit as OOTD enables Dripped to never repeat outfits. Try On : Virtually Try On outfits before actually wearing them to see how the outfit looks on you Drippy : AI stylist to curate outfit per your taste. Retire : A place for our long gone favorite pieces to rest and be in memory. How I solo-built it As the solo builder I took upon the backend and iOS dev myself going all in, with some help from Cursor, Claude and the live saver Code Rabbit . iOS: SwiftUI UIKit Metal Backend: Bun Cloudflare Workers and R2 Typescript Postgres Quadrant for Vector Database Reviewer: CodeRabbit Challenges I ran into Since this was my first ever full-fledget iOS app, I wanted to ship as many features as possible with the initial version. This meant faster building and vibe coding where any iterative additions would mean dismantling the entire codebase as somewhere something broke. As a solo builder, I didn't have any help in reviewing my code and as it was partially vibe coded, stuff that mostly worked would later on break. This was until I tried CodeRabbit and it was a savior in reviewing my code and finding issues before going to prod. This was such a huge relief for me, as I know the code that I am shipping out were bug free. Next challenge was with virtual try on, where the user image and the generated image varied a lot and would sometimes be racially inaccurate causing frustration among initial testers. This was solved when google launched their image gen model NanoBanana. The biggest of all right now is to market the app. As I am someone with zero taste in fashion or clothing, I am still figuring out the best medium and format to market the app and to find the niche user group. Well, who said marketing was easy! Accomplishments that I am proud of Releasing to the App Store : This is a huge win to me, as this project started of as a way to beat my procrastination and to actually build something that solves my problems Users Subscribe : I got my first ever subscriber!!! . This felt like a validation to my idea. Xcode on the GO! : Using CodeRabbit I came up with a custom workflow which includes Github app, Claude and Xcode Cloud to build features on my iPhone and have CodeRabbit verify it and then ship a preview build to Testflight. Since CodeRabbit lints and has context-aware analysis, I trigger the cloud build only when CodeRabbit gives an all clear, this way I can code on a beach without a Mac! More on this: Medium What I learned Stick to core features for MVP, never add too many features before launch. Launch early to test, get feedback and iterate on it. Get a team mate or a co founder. This is something I regret not doing, as a fresh set of mind working on the problem would open new doors and get better output twice as fast. Choose your stack wisely after due diligence. I initially decided to go with a third party vector database, and integrated it completely within my app. But after initial testing the outfit generation speeds were terrible and the vector db was a huge bottleneck, which I had to completely remove and rebuild. What's next for Dripped Marketing and finding my audience. The current feature set is very impressive, but lacks user retention due to lack of marketing, the next two months would be to launch TikToks and Instagram reels finding the target audience and focus heavily on App Store Optimization using tools like Astro. Social Closet , an Instagram for closets, where you can view your friend's closet, see what their OOTD and style outfits for them. Mac & iPad App Support Trial Room - Select clothing images from any website, pair them with items from your existing wardrobe, and virtually try on the complete look to see what works before you buy. Drip Check - This was initially planned using Elevenlabs agent but couldn't build in time. Basically you'd video call with AI and it acts as a friend critiquing or stylizing your outfit; giving suggestions from your closet. Lots more to come, but for now go ahead and get Dripped and Get Dripped ! <div