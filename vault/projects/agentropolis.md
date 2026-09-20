---
slug: "agentropolis"
url: "https://devpost.com/software/agentropolis"
title: "Agentropolis"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 1133
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Agentropolis

> We replaced everyone in Toronto with their AI doppelgängers.

[Devpost](https://devpost.com/software/agentropolis) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[health_clinical]] [[transportation]]
  <sub>weak: patient_family</sub>
**substrate** [[geospatial]] [[video_visual]]

**stack** fastapi, mapbox, neon, next.js, python, react, typescript, uvicorn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we are proud of
- what we learned
- what is next for agentropolis

## Body

Landing page COVID-19 simulation Ingecting Financial Crisis event Profile Card of Hospitalized Patient in Tech during Pandemic + Ingected Financial Crisis Regions of Toronto + Demographics X/Twitter posts of people suffering when the TTC is down :( Inspiration We wanted to see what happens when you put thousands of AI agents into a real city and let them live their lives together. Cities are messy systems made of people, neighborhoods, jobs, transit, and opinions. We were inspired by urban simulations and agent based models, but wanted to build something that felt alive instead of abstract. So we picked Toronto as our sandbox. It is diverse, geographically distinct, and rich with public data. That made it a great place to ground agents in real neighborhoods, industries, and daily routines. The idea was simple: turn a real city into a living simulation where every dot on the map is an AI character with a home, a job, and things happening in their life. What it does Agentropolis is a society simulation running on a 3D map of Toronto. You can start a session and watch a city of AI characters come to life. Agents are seeded from archetypes based on demographics like industry, neighborhood, and lifestyle. Each archetype generates followers , which are individual characters with homes, workplaces, happiness levels, and personalities. Agents go about their day. They commute, work, eat, sleep, shop, exercise, socialize, attend events, and sometimes post tweets about it. They also react to things happening in the city. You can inject events like a transit strike or a heat wave and watch thousands of agents adjust their behavior in real time. The map itself is fully interactive. The frontend uses Mapbox GL with 3D buildings and terrain, so you can zoom around Toronto and watch agents move through neighborhoods. Updates stream in through WebSockets so the map stays in sync as the simulation clock advances. You can also join the simulation yourself. The avatar creator lets you design a character with skin tone, hair, outfit, and accessories. When you click Join simulation , your character becomes a new agent in the city and appears on the map alongside everyone else. In one sentence: Agentropolis is a living city simulation where thousands of AI agents move through Toronto, react to events, and you can drop yourself into the world with your own avatar. How we built it The backend is written in Python using FastAPI with REST endpoints and WebSockets. Data is stored in NeonDB (PostgreSQL) and managed with SQLAlchemy async and asyncpg. We use Alembic for migrations and Railtracks to orchestrate the LLM agents. Each simulation tick runs a two layer agent system. Archetype agents make one decision per demographic group, deciding what the group plans to do during the next period. Then follower variation agents personalize those plans for each individual agent. To keep the system fast, we pre fetch all the context an agent might need. Memories, events, locations, and relationships are gathered ahead of time and passed in one message to the LLM. That avoids slow tool call loops. The frontend is a Next.js application written in TypeScript with React and Zustand for state management. Mapbox GL renders the 3D Toronto map, building extrusion, and the cinematic landing flyover. Agents appear as dots on the map and update in real time through a WebSocket stream. We also built a procedural avatar system . Instead of storing images, each agent has either an avatar seed or avatar parameters. These control features like skin tone, hair style, and clothing. The same schema powers both generated agents and user created avatars, which keeps everything consistent and scalable to tens of thousands of characters. Challenges we ran into One challenge was latency . Even one LLM call per archetype per tick adds up when the simulation has many archetypes. Pre fetching context and running agents in parallel with a semaphore helped keep ticks reasonably fast. Another issue was keeping the simulation stable when LLM responses fail. We added a deterministic fallback so agents still produce valid actions if an LLM call errors out. That way one bad response cannot break the whole simulation. Making Toronto feel real also took effort. We built static datasets for neighborhoods, industries, and demographic mappings so agents could have plausible home and work locations. Getting those coordinates to line up with Mapbox and the WebSocket update stream required careful synchronization. The avatar system had its own design challenge. We wanted diverse characters without storing photos or labeling race. The solution was a procedural system with continuous skin tones, multiple hair textures, and flexible clothing parameters. Accomplishments we are proud of We built a full end to end pipeline that goes from Create session to a populated Toronto simulation running live on a 3D map. The two tier agent architecture works surprisingly well. Archetypes decide what the group does, while follower agents personalize the details. This keeps costs manageable while still giving each character variation. The simulation also feels grounded in a real place. Agents live in specific neighborhoods, commute to work districts, and react to events tied to actual parts of Toronto. The procedural avatar system is another highlight. It supports thousands of characters, works with both generated and user created agents, and avoids storing personal images. Finally, the deterministic fallback means the simulation keeps running even when LLM calls fail. That stability was important for demos and long sessions. What we learned Pre loading context is often faster than relying on tool calls for agent tasks that mostly read information. Orchestrating multiple agent layers requires careful scheduling and error handling so one failure does not block the whole system. Grounding agents in real geography dramatically improves the realism of their behavior. When agents know their neighborhood and workplace, their actions become more believable. Writing design docs before implementation also helped a lot. The procedural avatar specification kept the backend, API, and frontend aligned. What is next for Agentropolis We want to replace map dots with instanced 3D avatars that walk around the city using shared meshes and GPU instancing. We also plan to add richer city events such as policy changes, disasters, or economic shocks. Agents could react by protesting, moving neighborhoods, changing jobs, or shifting public opinion. Another direction is building a stronger social network between agents so posts, rumors, and moods spread through the population. We also want to make the user agent more playable. Instead of just joining the simulation, you could set goals or give commands and see how the rest of the city responds. Finally, we want easier ways to share simulations. Things like session links, public city runs, and prompts like “What do you want to simulate?” could make Agentropolis feel more like a platform for experimenting with cities. <div