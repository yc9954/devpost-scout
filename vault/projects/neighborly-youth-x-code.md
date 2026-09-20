---
slug: "neighborly-youth-x-code"
url: "https://devpost.com/software/neighborly-youth-x-code"
title: "Neighborly - Youth x Code"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 661
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Neighborly - Youth x Code

> Neighborly empowers communities with AI-audited shared budgets, crowdsourced safety alerts, and direct civic reporting. We build transparent, resilient neighborhoods through localized intelligence.

[Devpost](https://devpost.com/software/neighborly-youth-x-code) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]]
**user** [[general_public]]
**substrate** [[geospatial]] [[structured_db]]

**stack** css, gemini, html5, json, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neighborly - youth x code

## Body

Initial loading screen home screen Track any cautious activity in the neighborhood Community Board, you are able to see any opportunities in the community Introduction screen 1 Introduction screen 3 Inspiration With the rise of remote work and digital isolation, local neighborhoods often lack a unified, modern space to connect, share, and collaborate. We were inspired to build a platform that brings neighbors together—replacing fragmented social media groups with a dedicated, beautifully designed hub where people can help each other, report local issues, and foster a genuine sense of community. The project is intended to fit into paths one and three, since it not only serves a community but also helps the user manage their finances and income sustainability with advanced, AI-powered tools. What it does Community Hub is a comprehensive, real-time web application designed to centralize neighborhood interactions. It features: Community Board: A live feed where neighbors can post needs, offers, or general updates, complete with direct messaging and commenting. Civic Reporter & Neighborhood Watch: Tools for residents to report local infrastructure issues or safety alerts, tracking their resolution in real-time. Community Calendar: A shared space to manage and discover local events. Shared Financial Tools: Dedicated modules for community budgeting and personal finance tracking. AI Guide: An intelligent assistant powered by Google Gemini, designed to answer community-related questions and provide guidance. Real-Time Notifications: An integrated alert system that keeps users updated on messages, comments, and status changes. How we built it We architected the project as a full-stack application: Frontend: Built with React and TypeScript, styled using Tailwind CSS. We utilized motion/react for fluid, native-feeling animations and a dynamic glassmorphism design system that supports multiple themes (like Natural, Sunset, and Cosmic). Backend & Persistence: We integrated Firebase (Firestore and Authentication) to handle real-time data synchronization for posts, comments, and notifications. AI Integration: We built a custom Express.js (Node.js) backend server to securely proxy requests to the Google Gemini API (using the modern @google/genai SDK and the gemini-2.5-flash model), ensuring API keys remain hidden from the client. Deployment: The application is containerized and deployed on Google Cloud Run for scalable, secure hosting. Challenges we ran into Real-Time State Management: Designing a scalable Firestore schema that handles nested interactions—such as live comments, direct messages, and unread notification counts—while keeping UI state synchronized and performant. Secure AI Integration: Ensuring that our Gemini AI implementation was secure by proxying all requests through a custom Node.js server rather than exposing keys in the browser, which required setting up a robust full-stack development environment. Design Consistency: Managing multiple complex UI states and animations (like the parallax backgrounds and multi-theme switcher) while keeping performance high and code modular across a large feature set. Accomplishments that we're proud of Delivering a cohesive, highly polished user experience that feels premium. The fluid animations, glassmorphism UI, and dynamic theme switching make the app visually distinct. Successfully integrating real-time database capabilities (Firebase) alongside generative AI (Gemini) into a unified, server-backed React application. Building a robust notification and messaging system from scratch that instantly connects users when they want to offer help or share information. What we learned The importance of modular component design when scaling a React application with multiple distinct, feature-rich tabs. Best practices for integrating server-side AI (Google Gemini) securely into a full-stack application. Advanced Firestore querying and batch writing techniques, especially for managing real-time notifications and keeping the read/unread state perfectly synced across the app. What's next for Neighborly - Youth x Code Location Intelligence: Integrating Google Maps Platform to provide real map data for the Civic Reporter and Neighborhood Watch features. AI Moderation & Automation: Expanding the Gemini integration to automatically categorize civic reports, detect duplicate issues, or act as a smart moderator for the community board. User Reputation & Profiles: Building out richer user profiles and a trust/reputation system based on community helpfulness. Native Mobile Experience: Adding Progressive Web App (PWA) capabilities so neighbors can easily report issues or receive push notifications on the go. <div