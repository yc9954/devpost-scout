---
slug: "tapped-in"
url: "https://devpost.com/software/tapped-in"
title: "Tapped In"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 652
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Tapped In

> Real-time map for community events around you.

[Devpost](https://devpost.com/software/tapped-in) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[finance_payments]] [[immigration_refugee]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]

**stack** creao, google-maps, maps, react, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for tapped in
- built with

## Body

Inspiration More than ever, we hear phrases like “loneliness epidemic,” “bed rotting,” and “doomscrolling.” These are real issues. Although we have advanced productivity apps for work or health, there isn’t a good solution to reduce friction in expanding our social comfort zones. Existing event apps just show lists. Calendars are private. After a busy day of college/work, finding the right, relevant, and timely social event requires too much effort and copy-pasting. Events are hidden in Instagram stories, spam emails, and word of mouth. We miss opportunities because information is convoluted and spread across too many platforms. To improve social productivity, we built Tapped In : a platform where finding in-person events is as easy as glancing at a map. Creating events is instant- hosts can effectively manage attendees, event logistics, and smart analytics. What it does Tapped In is a geo-spatial social productivity platform. It uses AI and custom APIs to instantly match users with location-based events, making both joining/hosting events effortless and effective. For Users: An intuitive map interface uses your location and preferences to visually filter your area for events relevant to you (e.g., career fairs, free food, hobby groups). Get automatic, customized Gmail and Google Calendar notifications that summarize your RSVPs. For Organizers: Submit a public event instantly. Our AI automatically suggests categorization tags, handles all RSVPs, and calendar management (including cancellation notices and attendee contact information). How we built it We used Creao, an AI-native tool building platform and implemented both built-in and custom API and MCP servers. Core: Use Creao to generate the entire front-end (Map UI, Carousel, Settings Panel) and the relational database schema (Users, Events, Preferences, RSVPs). Logic: Automatically scans the event description and title to suggest Event Type tags (e.g., "Concert," "Product Promotion"). Custom API Workflow: Connect Creao to GoogleMaps JavaScript API to handle geospatial view, add markers, and autofill addresses. OpenAI GPTChat handles generated email content and event labelling. Gmail and Google Calendar MCP integrations handle notifications on RSVP status. Challenges we ran into Understanding the tradeoffs between API and MCP servers. The provided MCP for GoogleMaps was not for our primary use case, requiring our to adapt our approach to integration to using API. Found that saving files within the Creao environment caused app functionality to be slow (delayed UI), as the system needed to validate the entire stack. Weren't able to manually edit code files on Creao. Needed to adapt prompts to include exact code file changes. Accomplishments We're Proud Of RSVP Notifications: Automatically removing canceled events from RSVP'd users' calendars and send an email notification. Friend Requests: Ability to add/remove friends and view their event RSVPs. Map UX: Creating a full-screen map-view mobile interface and achieving a UX that makes finding events fun by seeing friends' events. What We Learned We learned to be extremely specific and provide detailed examples in our Creao prompts to minimize validation time and guide the AI toward the intended architecture, helping mitigate the front-end latency we experienced. MCP vs. REST: We gained a better understanding of the difference between an API and an MCP server, as well as how a server connects to a service. For agentic workflows, custom logic must be built into an external service that conforms to the MCP standard. What's Next for Tapped In Exclusive Events: Events only appears for specific groups (eg. Berkeley Students, Companies) Increased Personalization: Recommend events based on prior event attendance and interactions. Add "Friend Recommendations" tab based on similarity of events attended. Monetization: Integrate a payment API (via another custom webhook) for organizers to promote events (eg. golden border on pins, shows up first in event carousel). Community Forums: Follow a event host and gain updates on their latest events. Gamification: Use the User Stats Page data to award badges and leaderboards for event creation and attendance. Built With Creao AI GoogleMaps JavaScript API OpenAI GPTChat API CreaoFileUpload API Google Calendar MCP Gmail MCP <div