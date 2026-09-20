---
slug: "skillme"
url: "https://devpost.com/software/skillme"
title: "SkillMe"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 435
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# SkillMe

> Learn literally ANY SKILL by getting daily challenges, tailored to you current skill level.

[Devpost](https://devpost.com/software/skillme) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**domain** [[developer_tools]]

**stack** openai, revenuecat, swift, swiftdata, swiftui, thecomposablearchitecture

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for skillme

## Body

Inspiration I’ve always wanted to learn cooking techniques that Michelin-starred chefs use, but that knowledge is scattered, hard to find, and usually means endless research or trial and error. When I asked ChatGPT to help me, I realized AI can break down skills into key techniques and step-by-step exercises. That was the spark for SkillMe : if plain ChatGPT can create a learning plan, how powerful would it be to wrap it in an app that keeps you motivated and on track? What it does SkillMe helps you learn any skill with a structured, AI-powered learning journey. Skill Creation Flow - Set a goal and answer assessment questions to define your starting level. Personalized Path - AI creates a tailored routine with daily challenges, difficulty levels, and pacing. Daily Challenges - Clear instructions, things to watch out for, and expected outcomes. Progress Tracking - Mark off challenges and see your growth over time. Motivation Tools - Notifications, Lock Screen widgets, and Home Screen widgets that deep link straight to your challenge of the day. Flexible Pacing - Designed for one challenge a day, but you can skip or double up whenever you like. How we built it Platform: iOS (iPhone only for now). Tech: Built with SwiftUI and integrated with the RevenueCat SDK for subscriptions. RevenueCat Integration: All access validation and purchases are handled through RC, not StoreKit directly. Custom Paywall: AI generates motivational marketing copy tailored to each user’s chosen goal. Example copy: Cooking → “Don’t lose your progress on becoming the next Gordon Ramsay.” Handstand → “You’re one daily challenge away from turning the world upside down.” Spanish → “Fluency isn’t built in a day, but miss today and you’ll slow down.” Challenges we ran into Designing a flow that feels structured but still flexible. Making daily challenges adapt to each skill and starting level. Building a paywall that feels personal and motivating rather than generic. Accomplishments that we're proud of Shipped a fully working iOS app integrated with RevenueCat. Created an AI-powered learning system that feels motivating and approachable. Built a playful, dynamic paywall that adapts to each user’s goals. What we learned How to combine LLMs with traditional iOS development workflows. The importance of quick iteration to keep learning paths motivating. That small design details (widgets, AI-tailored copy) can make a huge impact on user engagement. What's next for SkillMe Expanding to iPad and Android. Adding smarter tracking so challenges adapt as users improve. Integration a tighter Feedback loop so that the path can be adjusted on the fly whenever the user feedbacks that it's too easy or too difficult. <div