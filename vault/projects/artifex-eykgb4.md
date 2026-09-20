---
slug: "artifex-eykgb4"
url: "https://devpost.com/software/artifex-eykgb4"
title: "Artifex"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 631
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Artifex

> AI Repair Assistant

[Devpost](https://devpost.com/software/artifex-eykgb4) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[frontline_worker]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]
  <sub>weak: sensor_telemetry</sub>

**stack** auth0, css3, gemini, gsap, lucide-react, next.js, pexels, react, tailwind, typescript, vercel

## How they structured the write-up

- 🎯 the problem
- 💡 our solution
- ✨ key features
- 🚀 tech stack
- 🎥 demo video
- 🏆 why artifex wins
- 📊 impact metrics
- 🛠️ local setup
- 👥 team
- 🔗 links

## Body

Landing Page Home Page Search result Login / SignUp using Auth0 🔧 Artifex | AI-Powered Field Repair Assistant Transform a single damage photo into professional repair documentation in 30 seconds 🎯 The Problem Field technicians, repair shops, and students in Gombe face critical challenges: No access to up-to-date repair manuals for modern devices Inconsistent documentation leads to repair mistakes and wasted parts High training costs prevent new technicians from entering the field Language barriers with English-only manufacturer guides 60% of e-waste in Nigeria comes from devices deemed "unrepairable" 💡 Our Solution Artifex democratizes repair expertise by turning any damage photo into instant, professional repair guides powered by Google Gemini 2.5 Pro. How It Works Authenticate – Secure Auth0 login for authorized users Upload Photo – Snap or upload device damage image (up to 4MB) Get Expert Guide – Receive step-by-step instructions with visual references in 30 seconds ✨ Key Features 🤖 Google Gemini 2.5 Pro Integration Multimodal vision analysis detects device type, damage severity, and repair complexity Structured JSON output generates consistent repair documentation Safety-first approach provides hazard warnings specific to detected damage Context-aware instructions adapt to damage patterns and device types 📸 Intelligent Visual References Pexels API integration fetches contextual repair images Shows relevant tools, components, and techniques based on device type High-quality imagery improves comprehension for visual learners 🔐 Enterprise-Grade Security Auth0 authentication protects proprietary repair knowledge Session management for repair shop team workflows Secure API routes prevent unauthorized access 📋 Comprehensive Repair Guides Each guide includes: ⚠️ Safety warnings and hazard callouts 🛠️ Required tools and materials lists 📸 Contextual repair images 📝 Step-by-step instructions ⏱️ Time estimates and difficulty ratings 🎨 Field-Optimized Design Mobile-first responsive works on any device Auto-scroll navigation keeps focus on current step High contrast interface for outdoor visibility Minimal text design for quick scanning 🚀 Tech Stack Frontend Next.js 16 – App Router with Turbopack for optimal performance Tailwind CSS v4 – Custom inline theme for modern styling lucide-react – Clean, consistent iconography Backend & AI Google Generative AI SDK – Gemini 2.5 Pro with vision capabilities Pexels API – Contextual repair image search Vercel Serverless Functions – Scalable API routes Security & Performance Auth0 SPA SDK – Production-ready authentication Vercel Deployment – Global edge network for fast load times Vercel Speed Insights – Real-time performance monitoring 🎥 Demo Video Watch Artifex in action: DEMO Key Moments: 0:00 – Problem overview 0:30 – Live damage photo upload 1:00 – AI-generated repair guide 1:45 – Technical architecture 2:30 – Community impact 🏆 Why Artifex Wins ✅ Gemini API Mastery Advanced multimodal capabilities (image + text analysis) Structured output parsing for reliable documentation Real-world application of vision AI ✅ Community Impact Empowers 500+ GSU Computer Science students Supports 20+ local repair shops in Gombe Reduces e-waste through accessible repair knowledge ✅ Technical Excellence Production-ready with secure authentication Performance-optimized for mobile networks Clean, maintainable codebase ✅ Innovation First AI repair assistant designed for African field technicians Novel combination: Vision AI + contextual image search + safety analysis Solves real problem with scalable solution 📊 Impact Metrics ⚡ 30-second turnaround vs 2+ hours manual documentation 🎓 500+ students gain repair resources 🔧 20+ repair shops can standardize workflows 🌍 Reduces e-waste by making repairs accessible 🛠️ Local Setup # Clone repository git clone https://github.com/saviour2/Artifex cd artifex-repair-assistant # Install dependencies npm install # Configure environment variables cp .env.example .env.local # Add Auth0, Gemini, and Pexels credentials # Run development server npm run dev Required Environment Variables # Auth0 NEXT_PUBLIC_AUTH0_DOMAIN=your-domain.auth0.com NEXT_PUBLIC_AUTH0_CLIENT_ID=your-client-id NEXT_PUBLIC_AUTH0_REDIRECT_URI=http://localhost:3000 # Google Gemini GEMINI_API_KEY=your-gemini-api-key # Pexels PEXELS_API_KEY=your-pexels-api-key 👥 Team Saikat Das – Full-Stack Development & AI Integration Subarna Maity – UI/UX Design & Full-Stack Soumyadeep Dey – Backend Architecture & API Integration 🔗 Links 🌐 Live Demo: ArtifexRepairs 💻 GitHub: Repo Link 📧 Contact: Team Artifex <div