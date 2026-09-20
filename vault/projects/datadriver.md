---
slug: "datadriver"
url: "https://devpost.com/software/datadriver"
title: "DataDriver"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 589
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "substrate/geospatial"
---

# DataDriver

> DataPilot is an Agentic AI powered assistant that utilizes NVIDIA Nemotron to generate detailed step by step work plans, inspect real time inventory availability, and replan tasks when issues arise.

[Devpost](https://devpost.com/software/datadriver) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[frontline_worker]]
**substrate** [[geospatial]]

**stack** agents, ai, flask, langchain, mongodb, nemo, nemotron, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Inspiration Data center maintenance still utilizes clipboards and manual procedures. In the event of an issue arising, technicians often will have to waste time and resources to guess the correct steps or dig through old documentation for references. Our vision for this is to modernize this workflow and create a system that intelligently lead the future of data center operations. What it does DataDriver is an Agentic AI-powered copilot for data center technicians. The assistance creates detailed step by step maintenance workflows, checks inventory availability automatically, reroute the plan towards a different reaction when prompted an unexpected issue. Ultimately, this should give the technicians the ability to better allocate their resources towards higher priority tasks. How we built it In order to accomplish most of our technical goals, we had to settle on a stack quickly. For our backend, we spun up a quick Flask API to support basic REST API operations. To supplement our backend with data, we chose MongoDB for its ease of use, NoSQL methodology, and schemaless architecture (which allowed us to evolve as fast as possible). For our frontend, we chose React + Vite + TailwindCSS in order to prototype quickly, customize our look & feel, and maximize user responsiveness. For our Agentic ReAct model, we took advantage of NVIDIA's nemotron-nano-9b-v2 model combined with LangChain's agent framework. Challenges we ran into One of the biggest challenges we had initially with our backend was figuring out how to use agents. AI evolves incredibly quickly, and it is not always well-documented. We found a lot of older information about LangChain and NeMo, but we eventually got on the right track with LangChain's latest documentation. Furthermore, we had some issues with python versioning, since we were all using different environments. Most of this was solved using virtual environments, but we still had compatibility issues that we spent some time on. Accomplishments that we're proud of Although we had never built an agentic workflow before this Hackathon, we found it to be an incredibly rewarding experience. The best experiences come from the most challenging problems that you have not yet faced, and agents were one of those challenges. We are also proud of how the frontend came out, as it is a clean and responsive interface. Not to mention, we also competed in last year's hackathon, and we were super excited to see how much we have improved upon our skills in the past year. What we learned Overall, this hackathon was one of our biggest learning experiences for the entire year. We all got to work around every single aspect of the tech stack, and feed off of each other's expertise in each of our own areas. We love building skills together, and that is truly what brought us together for the past 28 hours! More specifically, we built skills in all of these areas/technologies React & Tailwind Python & Flask NeMo toolkit & Nemotron models Agentic reasoning and ReAct models Project management MongoDB & NoSQL ## What's next for DataDriver DataDriver has a TON of potential for future expansions. The agentic feedback loop opens it up to infinite possibilities in the future, from helping technicians automate more detailed tasks, more advanced Human-In-The-Loop functionality, and shortest path routing, to creating automated action plans for failures, assisting technicians with the latest hardware, and increasing observability for all actions taken by technicians. We are super excited to see what other creative projects are out there, and see how they inspire us to think of more improvements to our solution! <div