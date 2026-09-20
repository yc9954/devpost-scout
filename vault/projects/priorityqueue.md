---
slug: "priorityqueue"
url: "https://devpost.com/software/priorityqueue"
title: "<PriorityQueue>"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 851
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# <PriorityQueue>

> Democratizing information across the electric grid.

[Devpost](https://devpost.com/software/priorityqueue) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[civic_government]] [[climate_energy]] [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[regulation_legal_text]] [[structured_db]]

**stack** elastic, mapbox, mongodb, node.js, openai, react, tailwind

## How they structured the write-up

- inspiration 🌱
- what it does 💡
- how we built it 🛠️
- challenges we ran into 🌃
- what we learned 📝
- what's next? 🚀

## Body

Inspiration 🌱 The U.S. interconnection queue faces a massive backlog, with two terawatts of mostly clean energy projects waiting for grid access, more than the 1.25 terawatts currently online, causing delays of three to five years or more. High interconnection costs and uncertainty lead to frequent project dropouts, forcing restudies that further slow the process and subsequently the clean energy transition. The current transmission planning system is inefficient, requiring the next project in line to bear upgrade costs, discouraging development and creating cascading delays. While FERC Order 2023 introduces reforms like batch processing and penalties for delays, the lack of proactive regional transmission planning remains a major bottleneck. Driven by genuine climate interest and frustration about the lack of progress in the energy transition, our team was drawn by the unique challenges that the grid interconnection queue offered, an often overlooked reason for lack of progress in clean energy transition. Like many other climate-adjacent issues, it all comes down to regulation. In a brief published by the Federal Energy Regulatory Commission, the commission detailed the great need for an efficient and transparent queue management system. Highlighted customer insights can be found here . Without one, American energy goals cannot be met. The US is not the first to think about this issue. France, for example, has taken strides to streamline its grid connection processes, leveraging a centralized system to integrate renewable projects faster and ensure grid stability. Similarly, parts of Texas have piloted innovative approaches, such as distributed energy resource integration and priority queues for renewables, to accelerate clean energy deployment. These efforts reflect growing public and institutional support for systems that not only simplify bureaucracy but also unlock the potential for cleaner, more reliable energy. It’s clear that people want this change and believe it will help bridge the gap toward a sustainable energy future. What it does 💡 Our solution is a user-centric platform that visualizes geospatial data of generation stations, manages each developer’s projects, and organizes said projects into clusters using proprietary algorithms. Each developer has access to current energy generator information, energy generators in the grid interconnection queue, and their own projects. Developers can take part in a “bidding system”, which will be pooled towards fees associated with connecting to the grid as a cluster. Developers also have access to a RAG agent, Link the Energy Expert, who is contextualized by all of PQ’s data and understanding of the grid interconnection system, and can consult with Link to plan which clusters to join and more. Another user of our platform is the ISO manager, or government-affiliated project manager. This user has access to all project proposals, and has the ability to grant or reject said projects. How we built it 🛠️ Our infrastructure is centered around a web app model through NextJS that is both scalable and can easily work with large amounts of data as we use MongoDB as our database. We made extensive use of Elastic for our RAG model and geospatial analysis, along with OpenAI for open-ended location interpretation based on user prompts. Challenges we ran into 🌃 As beginner hackers, we were inexperienced in working with the tools we had access to at Treehacks, but we were eager to try out new software. Unfortunately, after spending a great deal of time working through a particular sponsor’s product, we realized that the product was not compatible with our web app, and the information could not be embedded into our final product. A drastic pivot had to be made and we tackled steep learning curves during the latter half of the hackathon. What we learned 📝 Many of our teammates have never built out a project of this scale at the speed we worked at during Treehacks. Moreover, we had varying degrees of experience with working with complex project files, so many of us learned an incredible amount about web app files and planning for larger project structures. Due to the research intensity of our project, we now know a significant amount about the nuances of the electric grid problem that we didn’t before. When working with niche pain points such as the interconnection queue, intuition for what our clients need will be built on a lot of painstaking research and prototyping through methods such as speaking with users. What's next? 🚀 PriorityQueue is far from finished. We envision a future where PQ works alongside government and regulation to promote transparency inter-developer and between the ISO and generators. Moreover, PQ currently sets up an environment in which developers can accurately assess the benefits to joining a cluster. However, by incorporating AI-facilitated decision making and analytics, PQ’s consulting service abilities could be bettered by tenfold. Imagine a platform that vertically integrates the energy project planning process, scrapes all the data that exists on which projects are currently being implemented, and can help developers make informed decisions about their business! We are inspired by the potential of PQ to: Foster collaboration and information trade between generators. Accelerate permitting reform & power the country. Develop a dynamic market for generators. Pitch deck can be found here . <div