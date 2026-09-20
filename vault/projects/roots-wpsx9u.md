---
slug: "roots-wpsx9u"
url: "https://devpost.com/software/roots-wpsx9u"
title: "Roots"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 898
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/government_staff"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Roots

> Roots is an open-source school management platform designed to replace Madrid’s outdated Raíces system. Roots empowers teachers, parents, and students with a intuitive mobile-friendly experience.

[Devpost](https://devpost.com/software/roots-wpsx9u) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[education]]
**user** [[educator_student]] [[government_staff]] [[researcher]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]]

**stack** clerk, conversationalai, dall-e3, elevenlabs-api, eslint, fastify, framer-motion, git, github, groq, lingo.dev, netlify, ngrok, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for roots
- sponsored challenges

## Body

Login Home Dashboard Student's Schedule Services Progress Interpretation Service Progress Interpretation Agent Extra-Curricular Online Activities powered by ElevenLabs Agents Build Your Own Story and DALL-E Illustration Agent Bulletin Board User Preferences Panel Inspiration Madrid’s public education system depends heavily on Raíces , a legacy platform that’s become synonymous with frustration. Crashes during exam periods, confusing navigation, poor mobile usability, and frequent timeouts have made even routine tasks feel like an odyssey for families and educators alike. After years of patches and millions of euros spent, confidence in the system is eroding. As parents living in Madrid we saw an opportunity not just to fix it—but to rethink it entirely and made it available for free to the community. In many small and/or underfunded schools across Spain, students and families face systemic educational gaps: limited extracurricular options, lack of native-speaking language teachers, and virtually no coaching or mentorship resources for parents. We saw an opportunity not just to modernize an interface, but to radically improve educational equity using AI. What it does Roots is a fully open-source school management platform built to meet the real needs of parents, students, and educators. It provides essential tools such as messaging, academic tracking, attendance, scheduling, and school communications—all in a fast, accessible, mobile-first interface. It’s designed to be intuitive, resilient, and fully compliant with accessibility and data protection standards. Roots combines essential educational services (grades, messages, schedules) with advanced AI-powered tools like: Multilingual support for non-Spanish-speaking families Math and language tutoring in multiple languages Voice-based parent coaching and wellness mentoring Conversational chess coaching with a virtual grandmaster Real-time illustrated storytelling for early childhood development AI-powered translation, illustration, and engagement at scale How we built it Core Architecture Roots is built on a modern full-stack TypeScript architecture using React 19 with Vite for the frontend and Fastify serverless functions for the backend. The application leverages a distributed deployment strategy with Netlify hosting the SPA frontend and Vercel handling the serverless API, providing automatic scaling and global edge distribution. The UI is crafted with Tailwind CSS and Framer Motion for animations, while Clerk handles complete authentication flows and React Router manages client-side navigation. Key Features & Technologies What makes this stack particularly interesting is the hybrid internationalization system using Lingo.dev for AI-powered translations alongside local dictionaries, supporting English-to-Spanish localization. The voice features are powered by ElevenLabs , real-time illustrations by OpenAI DALL·E 3 , and seamless multilingual support by Lingo.dev . The backend uses Fastify with Server-Sent Events (SSE) for live storytelling updates. The platform includes OpenAI integration for educational tutoring services and Socket.IO for real-time communication features. Everything is fully type-safe with TypeScript , localized in English and Spanish, and deployable on Netlify . The entire codebase emphasizes modern tooling including ESLint flat config and optimized Vite bundling with intelligent code splitting. Challenges we ran into Legacy complexity : Mapping the workflows and features of Raíces revealed layers of institutional complexity, often undocumented. UX/UI modernization : Designing a clean, modern interface that also respects the identity guidelines of the Comunidad de Madrid took careful balancing. Localization : Ensuring all user-facing content worked seamlessly in both Spanish and English required setting up a full i18n pipeline. Timeline pressure : Building an MVP that’s production-grade within a tight deadline pushed us to be laser-focused on essentials. Creating real-time experiences like illustrated storytelling while managing latency and safety controls. Multilingual voice agents required precise prompt tuning and audio optimization across five languages. Accomplishments that we're proud of Created a fully working MVP platform in under 30 days, combining essential school functions with AI enrichment. Successfully integrated real-time story illustration powered by kids’ storytelling voices. Built voice-based tutoring agents in chess, math, and languages that work cross-device and multilingual. Delivered 24/7 wellness and coaching agents for parents—bridging a gap no school payroll could afford. We’ve laid the groundwork for an open-source ecosystem where contributors can extend the platform with plugins and features specific to their region or school. What we learned Simplicity wins. Prioritizing clarity and usability helped us avoid replicating the overwhelming UX of traditional systems. Conversational AI can fill real resource gaps in education if implemented carefully and contextually. Being real users (parents) helped us avoid assumptions and shape a platform that people actually want to use. Parents need as much support as students —and they’re often underserved by traditional school platforms. What's next for Roots Student and teacher features : We plan to extend the platform with features tailored for students and teachers—such as grade tracking, personalized learning paths, and digital homework submission as well as lesson enrichment, communications, and evaluation tools. More subjects : science, history, financial literacy via new AI agents Community portal for collaborative parenting, student-to-student storytelling, and local events Government pilot : Prepare a case study and implementation proposal for a pilot program in collaboration with a Madrid-based school. Sponsored Challenges Roots will go for two challenges: Voice AI Challenge : we've integrated with ElevenLabs Conversational AI agents (6 in total) to bring features like student's progress interpretation and coaching for parents, tutors (math, chess, languages), story-telling and illustration building (combined with DALL-E APIs) and parent's wellness coach. All of them are multilingual and support the most commonly used languages in Madrid's public school where a fair amount of parents and students are coming from non-Spanish speaking countries. Deploy Challenge : we've deployed the full stack app usign Netlify. <div