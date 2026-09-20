---
slug: "muse-z8e04y"
url: "https://devpost.com/software/muse-z8e04y"
title: "Muse"
hackathon: "HackMIT 2023"
organization: "HackMIT"
winner: true
words: 591
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Muse

> Using the newest LLMs, Muse aims to enhance one of the greatest open-learning libraries, MIT OCW, by offering curated video playlists by topic so you never have to look through a syllabus again.

[Devpost](https://devpost.com/software/muse-z8e04y) · hackathon [[HackMIT 2023]]

## Facets

**mechanism** [[retrieval_grounding]]
**user** [[researcher]]
**substrate** [[code_repository]] [[structured_db]] [[transcript_audio]]

**stack** chatgpt, lantern, next, openai, postgresql, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for muse

## Body

Inspiration Have you ever wanted to learn about something but didn't know where to start? The internet is full of spotty, inaccurate and unreliable information that might answer a single direct question, but won't cut it if you want to learn in way that is both holistic and relevant. Muse solves this by leveraging MIT's celebrated OpenCourseWare (OCW) platform, a compendium of academically rigorous, high-quality course materials, to provide an educational experience that is centered around your search query but provides the flexibility and structure of college courses. What it does Muse answers any question by guiding you to a curated playlist of videos and resources based on MIT's OCW platform. It pinpoints moments in lecture videos that are both relevant and focused around answering the user's query, and presents these video snippets in a seamless manner for the user to learn from. This also provides the flexibility of exploring surrounding or follow-up content very naturally. How we built it We took advantage of Lantern's optimized vector database technology to power our queries, making this platform both efficient and scalable. We used Prisma as an ORM to populate and interact with the database, which is an extension of PostgreSQL. OpenAI's GPT API was used to generate text embeddings, both for the query as well as for preprocessing our repository of course content. We aggregated lecture transcripts into minute-long segments to be embedded and persisted in the database. A query finds the closest match of the user's question to a given moment in a lecture, of which the top results are then presented to the user in order of closeness. We utilized NextJS for our framework, and experimented with different CSS effects and styling such as carousels, glassmorphism, and the dark-mode trend. We queried from our LLMs the closest videos in their vector embeddings to our input, fetched from our backend the videos necessary to display, and presented the videos through Youtube Embeds. Challenges we ran into A large part of the project was getting the vector embeddings from the data. We had to source for the course content in a format that was amenable to pre-processing, and we eventually settled on the lecture transcripts with timestamps, which we could design our own scripts for aggregating for our needs. It also took some initial setup to integrate our project with Lantern, because of how new the technology was, but once we got it working it made database nearest-neighbor queries very natural and efficient. Accomplishments that we're proud of Muse provides a unique and revolutionary new approach to combining the benefits of a formal, structured college-style education with the convenience and functionality of a search query. It leverages OpenAI's LLMs to obtain a more accurate result that is most relevant for the user's needs, and does so in a seamless user interface that is both easy to use and looks amazing. What we learned We learned how to use GPT to obtain state-of-the-art text embeddings and how to integrate this into a web-based service. We also explored vector databases and how they could be used to provide a more efficient solution for such applications with AI and embedding-based needs. What's next for Muse The future of Muse will include using GPT's chat functionality to gain better insight into the user's specific goals and ask clarifications, to ensure that the content shown is as relevant as possible. It will also encompass the entirety of the MIT OCW catalog, and further enhance the educational experience with links to lecture notes, problem sets and more. <div