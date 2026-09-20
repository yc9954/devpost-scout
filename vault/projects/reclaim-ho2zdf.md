---
slug: "reclaim-ho2zdf"
url: "https://devpost.com/software/reclaim-ho2zdf"
title: "RECLAIM"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 847
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/educator_student"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# RECLAIM

> Privacy-preserving identity recovery system - connecting document finders with owners securely

[Devpost](https://devpost.com/software/reclaim-ho2zdf) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[structural_withholding]] [[vision_ocr]]
**domain** [[civic_government]] [[developer_tools]] [[education]] [[finance_payments]] [[transportation]]
**user** [[educator_student]] [[frontline_worker]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css3, git, html5, javascript, node.js, npm, postgresql, react, react-router-dom, supabase, supabase-api, tesseract.js, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reclaim

## Body

Superbase Table Superbase Table 2 Inspiration The inspiration for RECLAIM came from a simple yet pervasive problem: every day, people lose important identity documents - national IDs, driver's licenses, voter cards, bank cards, student IDs, and more. The current solution is often posting photos of these documents on social media or community groups, which exposes the very personal information people are trying to protect. I've personally seen posts like "Found this ID card" with photos containing full names, ID numbers, addresses, and dates of birth. This widespread practice puts people at risk of identity theft, fraud, and privacy violations. There had to be a better, more secure way to return lost documents to their owners. This project was built entirely on an Android phone using Termux, proving that powerful applications can be built with accessible tools. What it does RECLAIMis a privacy-first platform that connects document finders with owners through a secure, anonymous matching system. Instead of publicly exposing sensitive information, RECLAIM offers two simple flows: I Lost a Document - Users submit details about their lost document (type, location, date, optional ID digits) 2.I Found a Document - Users upload an image of the found document (OCR automatically detects the document type) The dashboard provides real-time statistics and a history of all reports. When a lost and found document match, users can connect through a secure handoff process without revealing personal information. Key Features: 🔐 Privacy-First: Never exposes personal information publicly 📱 Simple Interface: Two clear actions - "I Lost" and "I Found" 📊 Dashboard: Track all reports with real-time statistics 🤖 OCR Integration: Automatically detects document types from uploaded images 🛡️ Secure Authentication: Powered by Supabase Auth 🌐 Live Demo: Deployed on Vercel for easy access How we built it Frontend (React + Vite) React 18 with functional components and hooks Vite for fast development and builds React Router DOM for navigation Custom CSS3 with gradient design and mobile-responsive layout Backend (Supabase) PostgreSQL database with three tables (lost_documents, found_documents, matches) Supabase Auth for secure user authentication Supabase Storage for document image uploads Row Level Security (RLS) for data protection OCR (Tesseract.js) Client-side text extraction from uploaded document images Automatic document type detection from OCR output Deployment Vercel for seamless deployment with environment variables Development Environment Entirely built on Android using Termux Git for version control Node.js and npm for package management Challenges we ran into Building this project entirely on an Android phone presented unique challenges: Mobile Development Constraints Limited screen space for coding and debugging No access to traditional IDEs Dependency management in Termux Supabase Integration Configuring Row Level Security policies Managing database permissions for anon and authenticated users Setting up storage buckets with correct policies Resolving CORS issues for production deployment OCR Integration Tesseract.js performance on mobile browsers Error handling for failed OCR attempts Fallback mechanisms when OCR fails Vercel Deployment Environment variable configuration Build optimization for production Permission Management Initially struggled with "permission denied" errors Eventually disabled RLS for testing, then created proper policies Accomplishments that we're proud of Built Entirely on Android Developed a complete full-stack application on a mobile phone Proves that powerful apps can be built with accessible tools Privacy-First Architecture Created a system that genuinely protects user privacy Documents are never publicly exposed Real-World Impact Solved a genuine problem affecting millions of people Potential to prevent identity theft and privacy violations Full-Stack Implementation Authentication, database, storage, and frontend all working together OCR integration adds intelligent document processing Successful Deployment Live demo available at reclaim-black.vercel.app Complete documentation with README and setup instructions Hackathon Ready Fully functional MVP with polished UI Comprehensive submission with screenshots and demo video What we learned Technical Skills: Building with Supabase (Auth, Database, Storage) Implementing OCR with Tesseract.js Deploying with Vercel Working with environment variables Managing Row Level Security policies Mobile Development: Android development using Termux Git and version control on mobile Node.js and npm in a mobile environment Problem Solving: Debugging permissions and policies Handling CORS issues Error handling and fallback mechanisms Building resilient applications Project Management: Planning an MVP in 5 days Prioritizing features for maximum impact Iterative development with continuous testing Security & Privacy: Importance of protecting personal information Implementing privacy-first design User authentication and data protection What's next for RECLAIM Short-term (1-3 months): Matching Algorithm : Implement advanced matching between lost and found documents Email Notifications: Automated alerts when potential matches are found Dark Mode: User preference for dark theme QR Code Integration: Generate QR codes for found documents with secure links Medium-term (3-6 months): React Native Mobile App: Native mobile experience for iOS and Android Push Notifications: Real-time alerts on match detection Document Verification: Enhanced security with document authenticity checks Community Reporting: Integration with local authorities and organizations Long-term (6-12 months): AI-Powered Matching: Machine learning for intelligent document matching Multilingual Support : Multiple languages for global accessibility Government Partnerships: Integration with national ID systems Blockchain Verification: Immutable proof of document recovery Business Potential: SaaS platform for universities and organizations API for third-party integration Premium features for institutions Built with ❤️ on an Android phone for the Build Beyond Hackathon** <div