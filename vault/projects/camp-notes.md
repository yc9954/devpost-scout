---
slug: "camp-notes"
url: "https://devpost.com/software/camp-notes"
title: "Camp Notes"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 728
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Camp Notes

> Remember the best campsites, avoid the worst ones, and share experiences.

[Devpost](https://devpost.com/software/camp-notes) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** claude, firebase, onesignal, posthog, revenuecat, swift, swift-log, swiftui

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for camp notes

## Body

Inspiration Camp Notes was born from a simple need: my wife and I started camping this year and wanted a way to collaboratively track which campsites were worth revisiting and which ones to avoid. We needed shared notes that would help us properly evaluate each site for future trips. What started as a personal solution quickly evolved into an app that could help the entire camping community make better decisions about where to spend their outdoor adventures. What it does Camp Notes is a comprehensive camping experience tracker that allows users to: Record detailed visit information for individual campsites including ratings, photos, notes, and attendees Crowdsource campground data where users contribute to a community database of campgrounds and sites Rate experiences using a 1-5 star system that aggregates into site and campground ratings Plan future trips by browsing community-added campgrounds and their amenities Share camping experiences through upcoming collaboration features The app focuses on site-level tracking rather than just campground-level, recognizing that individual sites within the same campground can have vastly different experiences. How I built it I built Camp Notes as a native iOS app using: Swift/SwiftUI for the frontend, creating a clean, intuitive interface Firebase as the backend (Firestore + Authentication + Storage) for real-time data sync and user management Modular Swift Package architecture with separate packages for core functionality, authentication, settings, and more Community-driven data model where campgrounds and sites are public, but visit records remain private by default The app follows iOS design principles with proper light/dark mode support and uses a nature-inspired green color palette (#4a7c59) that reflects the outdoor theme. Challenges I ran into Several technical and product challenges emerged during development: Firebase authentication timing issues - tokens weren't clearing quickly enough between sign-out/sign-in attempts, requiring delay workarounds that felt like code smells but resolved the problem Balancing design ambitions with shipping deadlines - learning to prioritize core functionality over perfect UI to get feedback faster Empty data set problem - since data is crowdsourced, new users face sparse campground listings, potentially making the app feel less useful before they realize they can contribute App Store approval hurdles - facing rejections due to authentication issues during Apple's review, responsive design problems across device sizes, and complications around subscription management Accomplishments that I'm proud of Actually launching 🎉 - Unlike many side projects that fizzle out due to over-ambitious scope, I successfully shipped a focused, working app Early traction - Within the first week of launch, a user subscribed to the premium tier, validating the value proposition Technical achievements - Successfully implemented complex SwiftUI animations like the progressive gradient on the My Visits view User-driven iteration - Quickly pivoted based on TestFlight feedback to add onboarding and make account creation optional initially What I learned Effective AI collaboration - Learned how to prompt Claude Code effectively by setting clear goals, using "plan" mode for architecture decisions, then allowing implementation while maintaining active oversight through frequent commits Knowing AI's limitations - Recognized when to handle complex, pattern-specific code manually rather than relying on AI, especially with custom types and established architectural patterns Shipping philosophy - Embraced the principle that feedback only comes after launch. Early TestFlight feedback about easing users into account creation was invaluable and led to immediate UX improvements Scope management - Successfully limited features to enable launch, planning collaboration and advanced features as post-v1 iterations What's next for Camp Notes Core Features Visit Collaboration - The original inspiration: real-time sharing of visit records with camping partners for joint evaluation Gamification system - User rewards (coins) based on app engagement to improve retention Advanced filtering and sorting - Help users find campgrounds that match their specific needs and preferences Data Strategy API integration - Populate the database with existing campground APIs to solve the empty data set problem and provide immediate value to new users Community growth - Focus on content that encourages organic user-generated campground data Growth & Expansion Content marketing - Develop blog content and video tutorials to drive organic discovery Measurable goals - Target 10+ visits recorded per month by next year as a concrete success metric Platform expansion - Android version to capture the broader camping community once iOS version reaches sustainable growth Camp Notes represents the evolution from a personal need to a community-driven platform that helps outdoor enthusiasts make the most of their camping adventures. <div