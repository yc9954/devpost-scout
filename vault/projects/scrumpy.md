---
slug: "scrumpy"
url: "https://devpost.com/software/scrumpy"
title: "Scrumpy"
hackathon: "RevenueCat Shipyard: Creator Contest "
organization: "RevenueCat"
winner: true
words: 1216
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Scrumpy

> Recipes from your feed

[Devpost](https://devpost.com/software/scrumpy) · hackathon [[RevenueCat Shipyard- Creator Contest]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[agriculture_food]] [[developer_tools]] [[immigration_refugee]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** ffmpeg, gemini-api, instacart-api, openai-api, python, python-dotenv, render, serper-api, supabase, swift, swiftdata, swiftui, typescript, uikit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for scrumpy

## Body

Inspiration Cooking is my sanctuary; it is how I unwind after work and pursue my creative side. More importantly, it is the bridge to my heritage, allowing me to connect with my immigrant parents as they pass down their intricate, unwritten recipes. However, I realized that the modern cooking experience is fractured. My culinary inspiration lived in a disorganized “recipe graveyard” of saved Instagram Reels, TikToks, and endless Notes app bulleted lists. This fragmentation led to three specific problems I faced every week: The “Single-Use” Waste Buying a full container of an obscure ingredient for just one recipe, leading to food waste. The Grocery Maze Spending hours aimlessly searching for ingredients because my list wasn’t categorized by aisle or store section. The “Saved vs. Cooked” Gap Having hundreds of saved videos but never actually cooking them because I lacked a structured way to turn a 60-second clip into a shopping list. I built Scrumpy to solve my own problem: a “Social-to-Stove” pipeline . I wanted a simple way to liberate recipes from social media, extracting the creator’s info, ingredients, and steps, and instantly transforming them into categorized shopping lists with Instacart integration to ensure I buy only what I need. By leveraging AI to parse these videos, I’ve turned my screen time into mealtime—spending less time in the aisles and more time in the kitchen. What It Does Scrumpy is an AI-powered culinary companion that transforms the way home cooks discover, plan, and shop for meals by bridging the gap between social media inspiration and kitchen execution. The app serves as a centralized hub for managing the entire cooking lifecycle: AI Recipe Extraction Users can share videos from TikTok or Instagram directly to the app. Scrumpy’s backend automatically parses the video to extract ingredients, quantities, cooking steps, and nutritional data. Conversational Cooking An integrated AI chatbot allows users to generate recipes from scratch or discover meals based on ingredients they already have in their pantry. Intelligent Meal Planning The app features an “Auto-Plan Week” function that generates a full seven-day meal schedule based on the user’s dietary restrictions, grocery budget, and saved recipe collection. Streamlined Shopping Scrumpy automatically aggregates ingredients from meal plans into a categorized shopping list. Through a direct Instacart integration , users can convert their digital list into a real-world delivery with a single tap. Ingredient Analytics The app tracks usage patterns to show users their most-frequently used ingredients and categorizes their digital pantry to help reduce food waste. How We Built It Scrumpy is built with a modern, async-first architecture that combines a native iOS experience with a scalable AI-powered backend. The goal was to transform unstructured cooking content into structured, reusable recipes—quickly, reliably, and at scale. Native iOS Frontend The frontend is built entirely in Swift using SwiftUI for a fast, responsive, and highly animated user experience on iOS 17+. SwiftUI powers all primary views, layouts, and animations UIKit is used selectively for advanced tab bar styling, navigation appearance, and the share extension UI SwiftData provides local persistence for recipes, meal plans, chats, and preferences using modern @Model definitions State is managed using @State , @StateObject , @EnvironmentObject , @AppStorage , and Combine Real-time interactions (recipe extraction progress and chat responses) are streamed via Server-Sent Events (SSE) Additional integrations include: Share Extensions + App Groups for one-tap video imports AVFoundation + Speech Framework for voice input and transcription UserNotifications with deep linking for background task completion Intelligent Recipe Extraction Pipeline To reduce latency and cost, Scrumpy uses a tiered AI pipeline: Caption First Video captions and descriptions are analyzed first and often contain full or partial recipes. Audio Transcription (If Needed) If captions are insufficient, audio is transcribed using Whisper. Visual Analysis as a Last Resort Key frames are extracted with OpenCV and analyzed using Gemini 1.5 Flash for OCR and visual cues. The combined context is finalized into a structured recipe using GPT-4o, validated with Pydantic, and stored in PostgreSQL. Smart Caching for Instant Results The first user to import a video triggers full processing (~30 seconds) Once processed, the recipe is stored in the database Subsequent users receive the recipe instantly without reprocessing This approach ensures fast UX while keeping AI and infrastructure costs low. Monetization with RevenueCat Scrumpy uses RevenueCat to manage subscriptions: Free and Pro tiers with usage limits Real-time entitlement syncing across devices Paywall presentation and purchase restoration RevenueCat enables a clean separation between product logic and billing infrastructure. Developer Workflow Development was accelerated using Cursor and Claude Code , enabling rapid iteration on async pipelines, AI prompt design, and Swift/Python integration without sacrificing code quality. Challenges We Ran Into This was my first time building an app from the ground up, so I encountered nearly every challenge that comes with being a first-time developer. Simple bugs that would now take minutes to fix often took entire days to track down. I developed the app alongside a full-time job as an environmental engineer, making time management one of the biggest hurdles. Progress often happened late at night or on weekends. Ironically, building an app focused on recipes introduced constant temptation. While testing, I discovered countless recipes I felt compelled to try, leading to late-night cooking sessions and a frequently monopolized kitchen—much to my roommates’ mixed reactions. Despite these challenges, each obstacle accelerated my learning and pushed me to become more self-sufficient as a developer. Accomplishments We’re Proud Of Starting with no prior app development experience, I successfully designed, built, and shipped a fully functional iOS application from scratch. I am particularly proud of building a resilient recipe extraction workflow that successfully processes videos incumbent apps could not convert into usable, shoppable recipes. A major milestone was creating a seamless end-to-end system that transforms short-form cooking videos into structured, actionable recipes—integrating share extensions, backend processing, real-time feedback, and clean presentation. I am also proud of developing an AI-powered recipe assistant that supports conversational creation, ingredient-based discovery, and real-time streaming responses. Beyond individual features, I am proud of the app’s cohesiveness. Meal planning, shopping automation, analytics, and subscriptions work together to mirror how people actually cook. What We Learned Building this app reinforced that a good idea is only the starting point. Progress required continuous iteration as real-world constraints surfaced. I learned that resilience in system design matters more than ideal inputs. Real cooking videos are messy, inconsistent, and incomplete. Balancing development alongside a full-time role emphasized prioritization—focusing on user value over premature polish. I also learned that user experience and technical architecture are inseparable. Real-time feedback and progress indicators were essential for building trust. Finally, building something personally useful proved to be the strongest motivator throughout development. What’s Next for Scrumpy My goal is to turn Scrumpy into a scalable product with meaningful distribution. If selected as a winner of the Shipyard Creator Contest, I would explore an equity partnership with Eitan Bernath and focus on creator-driven distribution. On the product side, I plan to introduce features such as photo- or video-based fridge scanning for recipe recommendations and significantly expand the default recipe library. From a growth perspective, I plan to join the Instacart affiliate program and introduce revenue sharing for creators, with future expansion to platforms like Amazon. Finally, I plan to launch on Android and add multi-language support to position Scrumpy for international growth. <div