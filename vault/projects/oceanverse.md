---
slug: "oceanverse"
url: "https://devpost.com/software/oceanverse"
title: "Relay"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 873
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Relay

> Relay — community-verified accessibility, right on the map.

[Devpost](https://devpost.com/software/oceanverse) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[accessibility]] [[civic_government]] [[developer_tools]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** betterauth, drizzleorm, github, google-oauth, leaflet.js, next.js, node.js, openstreetmap, postgresql, react, render, supabase, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for relay

## Body

Interactive Accessibility Map Relay Accessibility Platform Volunteer Dashboard Accessibility Reporting & Community Map Crowdsourced Accessibility Reporting Inspiration Accessibility information is often difficult to find when people actually need it. A place may technically be accessible, but important details such as wheelchair ramps, accessible entrances, elevators, accessible restrooms, or obstacles may not be clearly available before someone visits. We wanted to build something that makes accessibility information local, visual, and community-driven . That idea became Relay — a crowdsourced accessibility map where people can report accessibility conditions around them and help others make more informed decisions about where they go. Our goal was simple: make accessibility information easier to discover and easier to contribute to. What it does Relay is an interactive accessibility mapping platform that allows users to discover and contribute accessibility information about real-world locations. Users can: 🗺️ Explore accessibility reports on an interactive map 📍 Find places using location search 🧭 Use their current location to explore nearby accessibility information ♿ Filter reports based on accessibility-related conditions 📝 Create accessibility reports for places they visit 👍 Upvote useful reports so reliable information becomes more visible 🔔 Receive notifications about relevant activity 👤 Create accounts and choose their role as an accessibility user, volunteer, or general user 📸 Add supporting images to reports 📊 View accessibility information in a visual and easy-to-understand way Instead of relying only on official information from businesses or organizations, Relay allows the community to continuously update the accessibility picture of an area. How we built it Relay was built as a modern full-stack web application. Frontend We used: Next.js React TypeScript Tailwind CSS Leaflet OpenStreetMap The frontend provides a responsive interface with an interactive map, accessibility report cards, filters, authentication screens, dialogs, notifications, and location-based features. Backend The backend uses: Next.js server-side functionality Drizzle ORM PostgreSQL Better Auth Our database stores users, sessions, authentication information, accessibility reports, notifications, and related data. Maps and location The core experience is built around Leaflet and OpenStreetMap . Users can search for locations, view accessibility reports as map markers, and use their current location to discover nearby information. Development approach We focused on building Relay as a real usable product rather than only creating a static hackathon prototype. We separated the application into reusable components and server-side actions so that features such as retrieving reports, creating reports, and upvoting reports could work with the database. Challenges we ran into One of our biggest challenges was getting the interactive map to work reliably inside a modern Next.js application. We encountered Leaflet rendering problems, including errors related to DOM elements and map initialization. Since Leaflet relies heavily on browser-side APIs, we had to carefully handle client-side rendering and component initialization. We also had to work through: PostgreSQL database configuration and connections Authentication configuration and origin errors Environment variable management Synchronizing frontend actions with database operations Location search and geocoding Current-location functionality Image upload integration Making the interface responsive Testing different user flows and edge cases These challenges forced us to understand how the different layers of a full-stack application communicate rather than treating the frontend and backend as separate pieces. Accomplishments that we're proud of We are proud that Relay evolved from an idea into a functional full-stack accessibility platform. Some of the things we are most proud of are: Building an interactive accessibility-focused map from scratch Connecting the map to real location and community-generated data Implementing user authentication and different user roles Creating a database-backed reporting system Adding community upvoting and notifications Designing a responsive interface around a socially meaningful problem Debugging complex Leaflet and Next.js integration issues Building the project as a foundation that can continue to grow beyond the hackathon Most importantly, Relay isn't just about displaying information. It creates a mechanism for people to contribute information that can help other people . What we learned Building Relay taught us that creating a useful product is much more than implementing individual features. We learned how important it is to think about the complete user journey — from discovering a location, to understanding its accessibility, to contributing a report, and eventually helping another person make a decision. Technically, we gained practical experience with full-stack development, database design, authentication, geolocation, interactive maps, API integration, and debugging client/server issues in Next.js. We also learned that seemingly small features, such as current-location detection or map markers, can involve significant engineering challenges when they need to work reliably across different browsers and devices. What's next for Relay Relay has the potential to become much more than a hackathon project. Our next steps would include: 🤖 Adding stronger AI-assisted accessibility analysis 📷 Automatically analyzing uploaded images for accessibility-related information 🧑‍🤝‍🧑 Building stronger volunteer and community contribution systems 📈 Adding accessibility trends and area-level statistics 🏢 Allowing organizations and businesses to verify their accessibility information 🌐 Expanding accessibility categories and location coverage 📱 Developing a dedicated mobile experience 🛡️ Improving report verification and moderation 🔄 Adding mechanisms to keep accessibility information up to date Our long-term vision is for Relay to become a living accessibility map , where communities continuously share, verify, and improve information about the places around them. Relay — helping people navigate the world with more confidence, one accessibility report at a time. <div