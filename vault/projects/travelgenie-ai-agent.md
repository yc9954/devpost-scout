---
slug: "travelgenie-ai-agent"
url: "https://devpost.com/software/travelgenie-ai-agent"
title: "TravelGenie AI-Agent"
hackathon: "Global AI Agents League"
organization: "Fetch.ai"
winner: true
words: 717
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# TravelGenie AI-Agent

> TravelGenie is more than a travel planner—it's an intelligent agent ecosystem designed to make your journey planning seamless, enjoyable, and informative.

[Devpost](https://devpost.com/software/travelgenie-ai-agent) · hackathon [[Global AI Agents League]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[geospatial]]

**stack** agentverse, fetch.ai, gemini, google-cloud, google-geocoding, google-maps, langchain, llm, openweathermap, python, react-native

## How they structured the write-up

- ✨ inspiration
- what it does
- how we built it
- architecture
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for travelgenie ai-agent
- conclusion

## Body

TravelGenie Home - Where user can chat with TravelGenie to get trip itinerary Chat Interface- User Interaction with TravelGenie Once the trip is validated, TravelGenie Core intelligently coordinates with other agents to get trip itinerary Trip Planning- UI (Weather, Route & Flight Details) Popular places & Popular restaurants at destination city List of upcoming events at destination city GIF Architecture TravelGenie: AI-Powered Multi-Agent Travel Planner Global AI Agents League Fetch.ai Innovation Lab Hackathon 2025 Team Members: Rohit Kosamkar Sapna Chavan ✨ Inspiration While using various AI chatbots to plan trips, we noticed most platforms provide long, static, text-heavy responses. These are often hard to follow and lack the real-time data that modern travelers need. We imagined a platform that could function like a smart travel buddy—engaging, responsive, and visually interactive. Thus, TravelGenie was born—to make trip planning fun, intuitive, and intelligent. What it does TravelGenie is an AI-powered multi-agent system that helps users plan their trips interactively. Here's what it offers: Accepts natural language input from the user via chat (e.g., "Plan my trip from Boston to NYC for next weekend"). Extracts trip details and validates them. Coordinates with registered agents to fetch: Route Info (via Google Maps API) Weather Forecast (via OpenWeatherMap API) Flight Options (via Amadeus API) Popular Attractions (via Google Places) Top Restaurants (via Google Maps) Local Events (via Ticketmaster) Returns the complete itinerary on a beautifully styled dashboard with visual cards. Uses Langchain + Gemini 2.0 Flash for LLM-powered reasoning and orchestration. How we built it Frontend : React with Tailwind CSS for responsive UI. Backend : FastAPI for API management and agent coordination. Agents : Built using uAgents framework, each agent is modular and live on Agentverse. APIs Integrated : Amadeus, Google Maps, Google Places, Ticketmaster, OpenWeather. Agentverse : All agents deployed on Agentverse for public use. LLM Orchestration : Gemini 2.0 Flash + Langchain (ReAct) for parsing, planning, and intent classification. Dashboard UI : A visual transition from chat to interactive cards for itinerary breakdown. Architecture Web UI → User chat input Supervisor Agent → Intent classifier, trip detail extractor, memory tracker TravelGenie Core → Orchestrates API agents Agents : Weather Agent: Fetches weather forecasts using OpenWeatherMap API. Route Agent: Computes route and transport suggestions between cities. Flight Agent: Searches top flight options using the Amadeus API. Restaurant Agent: Retrieves top-rated restaurants using Google Maps API. Places Agent: Recommends popular places via Google Places API. Event Agent: Lists upcoming events using the Ticketmaster API. Summary Agent: Summarizes the itinerary with useful tips and prep advice using Gemini. Gemini 2.0 Flash → Intent classification & reasoning Langchain → Task planning and orchestration UI Output → Dynamic dashboard Challenges we ran into Agent Coordination : Syncing multiple agents with message sequencing and async logic. Selenium Flight Scraper : Initially tried scraping Kayak using Selenium but response time was too slow. Pivoted to the Amadeus API for faster, reliable flight data. Real-time Validation : Ensuring that trip inputs (source ≠ destination, dates are valid, duration ≤ 14 days). Agent Registration : Handling model serialization and decoding issues during registration on Agentverse. Accomplishments that we're proud of Deployed 6+ intelligent agents publicly on Agentverse. Designed a chat → dashboard experience that feels seamless and delightful. Integrated multiple real-time data sources and handled them modularly via agents. Built reusable agent codebases (Weather, Flights, Food, Events, etc.) that can be adapted for other ecosystems. What we learned Agent-oriented system design with uAgents . Fine-tuned usage of Langchain ReAct prompting and Gemini 2.0 Flash. Best practices in handling multiple APIs securely and efficiently. How to deploy, monitor, and manage autonomous agents via Agentverse. What's next for TravelGenie Ai-Agent User Login & Itinerary Save : Personalize and revisit past trips. Hotel Booking Agent : Integrate with lodging APIs. Budget Estimation Agent : Track costs and suggest optimizations. Voice Input Support : Make trip planning hands-free. Co-Planning with Friends : Share and collaborate on itineraries. Mobile App Version : Full native support for Android/iOS. Conclusion Building TravelGenie during this hackathon has been a transformative learning experience. From juggling agent communication and orchestrating real-time data to deploying a highly interactive frontend, we stretched our boundaries and embraced the power of agent-based design. More than a hackathon project, TravelGenie reflects our passion to simplify and elevate how people plan their journeys. <div