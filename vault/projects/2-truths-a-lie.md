---
slug: "2-truths-a-lie"
url: "https://devpost.com/software/2-truths-a-lie"
title: "2Truths-1Lie: A Kiro-Powered Social Video Game"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 513
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
---

# 2Truths-1Lie: A Kiro-Powered Social Video Game

> An engaging mobile social game where players record and guess lies, brought from idea to production-ready open beta release in weeks using Kiro’s spec-driven development.

[Devpost](https://devpost.com/software/2-truths-a-lie) · hackathon [[Code with Kiro Hackathon]]

## Facets

**domain** [[transportation]]
  <sub>weak: financial_record</sub>

**stack** amazon-web-services, javascript, kiro, python, railway, typescript

## Body

GIF Challenge Guessing GIF Challenge Creation GIF Kiro's Spec-Driven Automated Workflow System Architecture: A scalable, production-ready system with a React Native app and a FastAPI backend. App icon & google play link Project Story: 2 Truths & a Lie Our Inspiration At its core, 2 Truths & a Lie was inspired by the timeless social game where players share authentic stories to challenge and connect with friends. We wanted to capture that magic in a modern, digital experience, creating a platform where a global community could interact through the simple joy of storytelling, laughter, and a little bit of deception. Our app lets users record three short video statements—two truths and one lie—which the community then watches and votes on to guess the lie. How We Built It: A Partnership with Kiro Our goal was to build a production-grade application, not just a prototype. To achieve this, we fully embraced Kiro’s AI-powered, spec-driven development workflow from day one. Instead of writing boilerplate, we invested our time in creating detailed specifications for each core feature in our /.kiro/specs/ directory. We treated our specs as the single source of truth, empowering Kiro to translate architectural decisions directly into production-ready code. Kiro automatically generated over 70% of our foundational code , including the entire secure FastAPI backend with JWT authentication and the complex React Native video recording UI . This partnership accelerated our development velocity by an estimated 3x, allowing us to focus on what truly matters: the user experience. Challenges We Faced Building a media-rich social app comes with significant technical hurdles. Our main challenges included: Orchestrating multi-segment video capture to ensure flawless, "no-bleed" playback transitions. Engineering a robust, server-side video merging pipeline with FFmpeg that could scale. Ensuring production-grade stability and security across the full stack, from the mobile app to the deployed Railway backend and ensuring resilient uploads and smooth playback despite varying network conditions. We navigated these challenges by pairing Kiro's automated code generation with rigorous human oversight and a comprehensive test suite. Key Accomplishments & Learnings We are incredibly proud to have delivered a fully operational, scalable, and polished mobile social game ready for its Open Beta launch . Our key accomplishments include: A secure FastAPI backend, architected and generated through Kiro specs. A responsive, cross-platform mobile app with a 90% pass rate across over 240 tests . Successful deployment to a production environment on Railway. What We Learned: Our biggest takeaway was the power of a specification-first mindset. We learned firsthand that by investing time in detailed requirements upfront, an AI partner like Kiro can dramatically accelerate delivery without compromising quality or security. This project proved that speed and stability are not mutually exclusive in modern development. What’s Next for 2 Truths & a Lie We're excited about the future of the project and plan to continue our AI-driven collaboration. Our roadmap includes: Enhancing content moderation with AI-driven detection tools. Introducing personalization features and smart recommendations. Rolling out monetization through RevenueCat-powered subscriptions. Expanding platform parity with full iOS support. Built with passion, powered by Kiro, deployed to production. 🚀 <div