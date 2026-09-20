---
slug: "mentor-bridge-nu9ivj"
url: "https://devpost.com/software/mentor-bridge-nu9ivj"
title: "Mentor Bridge"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 485
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/researcher"
---

# Mentor Bridge

> Empowering Students, One Connection at a Time.

[Devpost](https://devpost.com/software/mentor-bridge-nu9ivj) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[revocation_withdrawal]]
  <sub>weak: on_device_local, realtime_stream, simulation_digital_twin</sub>
**domain** [[education]] [[finance_payments]] [[labor_employment]]
  <sub>weak: developer_tools</sub>
**user** [[educator_student]] [[researcher]]
  <sub>weak: legal_professional</sub>
  <sub>weak: code_repository, document_pdf, structured_db</sub>

**stack** cursor, firebase, node.js, react, tailwindcss, vite

## Body

Inspiration As an Indian student, I often noticed how difficult it is to find strong mentorship and affordable tutoring outside school or test-focused coaching centers. Students lack trusted access to mentors, professionals, or seniors who can guide them through academics, exams, and career paths—especially if they’re introverted or new to a subject. We wanted to create a student-first platform, inspired by solutions like LifeBridge and community learning platforms, but squarely focused on problems students face in high school and college today. What it does MentorBridge lets students: Connect instantly with mentors, professionals, college students, or verified tutors Book sessions (chat or call) based on comfort, subject, or mentor style Pay tutors using tokens (no cash barriers at first, with easy top-up options) Receive free mentorship, motivation, and career guidance from seniors and professionals Track sessions, rates, reviews, and learning progress in a fun, student-friendly UI Mentors and tutors can: Offer help, set availability, and earn tokens Withdraw tokens as real money, creating a micro-earning stream for student tutors Build their resume, reputation, and impact by helping next-gen learners How we built it Frontend: React 19 with Tailwind CSS for a fast, clean, responsive UI Backend: Firebase (Auth, Firestore) for user/session management and real-time chat Payment/Tokenization: Simulated token economy, with withdrawal flows for tutors (stubbed for hackathon) Demo Data: Mock dataset for students, mentors, sessions, chat, and reviews using Cursor prompts Development: Rapid prototyping in Cursor, tested locally, with all flows seeded for easy demo and repo review Challenges we ran into Designing session and tutor flows to be friendly for both extroverted and introverted students Implementing token withdrawal and commission logic within time constraints Ensuring a safe, inclusive experience (privacy toggles, moderation tools) Seeding realistic demo data in time for hackathon submission Resolving Git conflicts after merging local and remote work, and streamlining deployment Accomplishments that we're proud of Built a full-stack mentorship & tutoring platform MVP in under 48 hours Created unique flows for matching, booking, pay-as-you-go, and review/ratings Included privacy features and flexible communication options for diverse student needs Enabled real revenue and resume-building for student tutors and college mentors Documented and tested all demo features so reviewers/Judges see a “live” experience What we learned The student mentorship market needs platforms that blend academic, career, and emotional guidance Peer-to-peer token economies lower barriers and boost engagement (over cash-only models) Real-world mentor/tutor feedback helps iterate on UI/UX much faster than design documents alone Git & codebase sync challenges happen—having good documentation and conflict resolution is critical Hackathon MVPs benefit hugely from seeded, realistic data and strong visual flows What's next for MentorBridge Integrate payments and direct withdrawals (UPI/Stripe) for live tutor revenue Extend group study, cohort, and community features for peer learning Pilot with schools and coaching centers to validate matching and earning flows Add AI-powered mentor matching and study recommendations Launch a production-ready app and scale to more subjects, languages, and regions <div