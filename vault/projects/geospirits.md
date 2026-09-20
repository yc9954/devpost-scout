---
slug: "geospirits"
url: "https://devpost.com/software/geospirits"
title: "GeoSpirits"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 909
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# GeoSpirits

> Resurrecting GeoCities.

[Devpost](https://devpost.com/software/geospirits) · hackathon [[Kiroween]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** kiro, nextjs, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

Inspiration Remember GeoCities? In the late '90s, it was a digital neighborhood where anyone could create a personal homepage and claim their corner of the internet. At its peak, it was the third most-visited site on the web, a place where creativity thrived, unpolished and authentic. Then it died. For Kiroween, we decided to resurrect that spirit - literally bringing dead tech back to life. GeoSpirits is GeoCities reborn, but instead of organizing pages by fictional neighborhoods, we anchor them to real places on Earth. Every page you create gets pinned to an actual location on an interactive 3D globe. It's the same democratized web publishing that made GeoCities magical, now enhanced with modern mapping technology, real-time 3D visualization, and the ability to explore the world through other people's stories. We're bringing back the joy of building your own corner of the internet, but this time, that corner has coordinates. And with Kiro, we could focus on the creative magic while it handled the heavy lifting: from natural conversation brainstorming to spec-driven implementation, Kiro helped us summon this project from the digital graveyard. We even added some spooky touches, flying ghost animations across pages, dark themes, and atmospheric effects - because what's a resurrection without a little haunting? What it does GeoSpirits is a location-based page publishing platform that anchors web pages to real places on an interactive 3D globe. Create & Publish: Build pages with a drag-and-drop builder featuring 10+ components (headings, text, images, galleries, buttons, custom HTML) Use AI to auto-generate page content and layouts instantly Customize everything—colors, fonts, spacing, themes (light/dark), header images Add interactive buttons with actions like links, confetti effects, and alerts Embed custom AI chatbots on any page for visitor interaction Pin your page to any location on Earth by clicking the 3D globe Get a unique shareable URL (e.g., /my-travel-blog) Explore & Discover: Browse all published pages as purple markers on the 3D Mapbox globe Click any marker to instantly visit that page Navigate with smooth animations, atmospheric fog, and starry effects Manage: View all your pages in a personal "My Sites" dashboard Edit pages anytime, update content, change locations, modify styles Delete pages with confirmation protection Secure authentication with Row Level Security using Supabase Special Features: Flying GIF animations across pages Spooky mode for Halloween vibes Server-side rendering for SEO and fast loads No login required to view published pages How we built it We built GeoSpirits with Kiro, the AI-powered IDE that made rapid development possible during this hackathon. Tech Stack: Frontend: Next.js 16 with React 19, TypeScript, and Tailwind CSS 3D Globe: Mapbox GL JS with globe projection, custom markers, and reverse geocoding Backend: Supabase for PostgreSQL database, authentication, and Row Level Security AI Features: OpenAI API integration for content generation and custom chatbot embedding Testing: Vitest for unit tests, fast-check for property-based testing Vibe Coding : We used conversational coding for rapid prototyping and iteration: "Create an interactive 3D globe with Mapbox that shows markers for published pages" "Build a drag-and-drop page builder with customizable components" The most impressive generation was the LocationPicker component-we described wanting users to click on a 3D globe to select coordinates, and Kiro generated the complete implementation including Mapbox event handlers, reverse geocoding API integration, coordinate state management, and UI feedback in one go. Spec-Driven Development: For complex features, we created structured specs with requirements, design, and tasks: AI Page Generator Spec: 10 user stories with 50 acceptance criteria 8 correctness properties like: "For any AI-generated component, the component must conform to the PageComponent type schema with all required fields and appropriate default styles" 15 implementation tasks with property-based tests (100+ iterations each using fast-check) Covered: AI mode, prompt engineering, OpenAI integration, error handling, regeneration, token tracking Globe Image Markers Spec: 5 user stories with 25 acceptance criteria 12 correctness properties like: "For any marker with valid location data, when clicked, the side panel should open and display the location details" 8 implementation tasks covering marker rendering, validation, styling, and side panel interactions Why Specs vs Vibe Coding: Specs for complex features: AI generation (external API, state management, security), authentication (RLS policies, session management), CRUD operations (validation, error handling) Vibe coding for rapid iteration: UI styling, simple components, quick fixes, visual design Hybrid approach: Prototype with vibe coding, create spec when complexity emerged Example - AI Generation: Vibe coding attempt: 30 min prototype, but no error handling, validation, or regeneration Spec-driven: 1 hour writing spec, 4 hours Kiro implementation, fully tested with property-based tests Result: Production-ready feature with comprehensive edge case coverage Kiro's Impact: Generated complete Supabase schemas with RLS policies Built entire Mapbox integration with 3D globe, marker clustering, atmospheric effects Created 20+ React components with TypeScript types and CSS modules Implemented all CRUD server actions with proper error handling Generated property-based tests validating correctness across 100+ random inputs Integrated OpenAI API with prompt engineering, response parsing, token tracking Challenges we ran into 3D Globe Interactions: Handling click events on a rotating 3D globe with accurate coordinate mapping and reverse geocoding AI Validation: Ensuring OpenAI responses matched our component schema without breaking the page builder State Management: Preserving manual edits during AI regeneration across multiple components RLS Policies: Balancing user-only editing with public page viewing in Supabase Accomplishments that we're proud of Resurrected GeoCities with modern tech-democratized publishing anchored to real places Property-based testing with 100+ iterations catching edge cases automatically Hybrid workflow mastery: Specs for complexity, vibe coding for speed <div