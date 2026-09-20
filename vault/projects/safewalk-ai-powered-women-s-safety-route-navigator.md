---
slug: "safewalk-ai-powered-women-s-safety-route-navigator"
url: "https://devpost.com/software/safewalk-ai-powered-women-s-safety-route-navigator"
title: "SafeWalk: AI-Powered Women's Safety Route Navigator"
hackathon: "Pixel Forge AI Hackathon ($18,000+ in Prizes)"
organization: "Pixel Forge"
winner: true
words: 989
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# SafeWalk: AI-Powered Women's Safety Route Navigator

> "SafeWalk shows women the safest walking route, not just the fastest — using real-time crowdsourced reports, live safety scores, and AI briefings for any city worldwide."

[Devpost](https://devpost.com/software/safewalk-ai-powered-women-s-safety-route-navigator) · hackathon [[Pixel Forge AI Hackathon -18-000- in Prizes-]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[civic_government]] [[developer_tools]] [[transportation]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]

**stack** folium, mapquest-nominatim-search, openstreetmap, overpass-openstreetmap, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safewalk: ai-powered women's safety route navigator

## Body

dashboard Inspiration In India, something as simple as walking home after dark is not simple at all if you're a woman. A friend, a sister, a classmate — almost every woman we know has a story about changing her route, calling someone just to "stay on the line" while walking, or straight up refusing to go out once it gets dark. Government data backs this up — a huge share of women in Indian cities say they avoid stepping out alone at night, not because they want to limit their own lives, but because there's no reliable way to know which street is safe and which one isn't. We kept coming back to one uncomfortable fact: Google Maps can tell you the fastest way home in half a second, but it has absolutely no idea whether that route is safe. That gap — between how good our navigation technology is and how little of it actually protects the people who need protection most — is what pushed us to build SafeWalk. What it does SafeWalk is a navigation platform that shows women the safest route between two points, not just the quickest one. Instead of one blue line, you get two: the fastest route and the safest route, each with a real safety score out of 100. That score isn't guesswork — it's built from real-time, crowdsourced incident reports (weighted so a report from an hour ago matters more than one from three months ago), streetlight and police-proximity data pulled live from OpenStreetMap, and the time of day you're walking. On top of that, a Gemini-powered AI generates a short, human safety briefing for your specific route and time — and if something goes wrong, an SOS feature drafts an emergency message instantly. How we built it We split the system into three layers that we could build in parallel as a team: The safety engine — a scoring function combining incident data, OpenStreetMap infrastructure signals (Overpass API), and time-of-day risk, feeding into OSRM for actual walkable routes. The Gen AI layer — LangChain + ChromaDB for a RAG pipeline grounded in real safety guidelines, and Gemini 1.5 Flash for generating briefings, processing free-text incident reports into structured data, and drafting SOS messages. The interface — a Streamlit app with a Folium map showing a live heatmap, side-by-side route comparison, and a reporting form where a woman can just type what happened in plain language. We deliberately avoided hardcoding any single city. Using Nominatim for geocoding and OSRM for routing meant the same codebase that works for Delhi also works for Tokyo or Lagos — a decision that mattered a lot to us, because safety shouldn't be a feature that only exists for one part of the world. The weighting formula for incident reports came from thinking about how Waze handles traffic: recent reports should dominate, old ones should fade. We modeled this as an exponential decay: $$𝑤(𝑡)=𝑒^(−𝜆𝑡)$$ where t is hours since the report and λ is tuned so a report loses about half its weight every 48 hours — giving the map a "memory" that behaves the way real risk actually does. Challenges we ran into Making "safety" a measurable number was the hardest problem of the whole project. Unlike distance or time, safety is subjective, contextual, and sensitive — we had to be very careful that our scoring didn't feel arbitrary or, worse, alarmist. We went through several iterations of the scoring formula before settling on one that felt honest rather than fear-mongering. Avoiding an empty map. A safety app with three data points on the map looks broken, not useful — so we had to pre-populate real incident data before we even had users, while being careful about sourcing this responsibly from public datasets rather than fabricating anything. Balancing urgency with responsibility. We didn't want the AI briefing to read like a warning label that scares women out of going anywhere. Getting Gemini's prompt to be direct and practical, not alarmist, took real trial and error. Making it global without losing local relevance. It would have been much easier to hardcode Delhi coordinates and call it done. Building the geocoding, routing, and OSM layers to work for any city, while still feeling locally aware, took more integration work than we expected in a hackathon timeframe. Accomplishments that we're proud of We're proud that SafeWalk isn't a static prototype — it's a system that gets smarter every time someone uses it, the same way Waze does for traffic. We're also proud that it works out of the box for any city in the world, not just the one we tested it in, and that the AI layer feels like a genuine safety companion rather than a gimmick bolted on for the hackathon. What we learned We learned that the hardest part of building "AI for safety" isn't the AI — it's designing a system that's honest about its limitations. A safety score with no local data yet is still a safety score, and we learned the importance of labeling AI-estimated guidance clearly instead of pretending we have more certainty than we do. We also learned a lot about combining multiple free, open data sources (OSM, OSRM, Nominatim) into one coherent real-time pipeline — and how much more powerful that becomes when a Gen AI layer sits on top to translate raw data into something a person can actually act on in the moment. What's next for SafeWalk: AI-Powered Women's Safety Route Navigator We want to add real-time news monitoring for breaking safety incidents, weather-based risk signals, and a lightweight mobile version so a woman can trigger the SOS feature without ever opening a laptop. Longer term, we'd love to partner with local safety initiatives like SafeCity to grow our verified incident data far beyond what a hackathon weekend could produce — because a tool like this is only as good as the community behind it. <div