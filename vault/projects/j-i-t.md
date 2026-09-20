---
slug: "j-i-t"
url: "https://devpost.com/software/j-i-t"
title: "J.I.T."
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 540
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# J.I.T.

> Scan a textbook. Meet your lil jit. Learn Just In Time with AI on the edge.

[Devpost](https://devpost.com/software/j-i-t) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** arkit, cloudinary, elevenlabs, embeddingsgemma-300m, fastapi, python, react, swift, upstash-redis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for j.i.t.

## Body

Home Page Summon Jit! Speak To Jit! Inspiration Textbooks are the foundation of academic knowledge, yet they remain one of the most static and intimidating ways to learn. We realized that students often struggle to stay engaged with dense blocks of text. We asked ourselves: What if the book could talk back? J.I.T. (Just-In-Time) was born from the desire to transform a silent, 500-page textbook into an interactive, 3D learning partner. We wanted to bridge the gap between physical media and digital intelligence, making education not just accessible, but genuinely fun. What it does J.I.T. is an AR-powered educational assistant. Users simply scan the ISBN barcode of any supported textbook. Instantly, a 3D avatar—J.I.T.—spawns directly on top of the physical book through their phone screen. Users can have a real-time voice conversation with J.I.T. about the book's content. Because J.I.T. is grounded in the specific knowledge of that textbook using RAG (Retrieval-Augmented Generation), the information provided is factually accurate, course-aligned, and far more engaging than a standard search engine. How we built it Our technical stack was designed for high performance and low-latency interaction: Frontend: Built with Swift, marking the first time our frontend team explored the language to create a native, fluid iOS experience. Backend: Powered by FastAPI to handle complex logic and asynchronous requests efficiently. Database & AI: We utilized MongoDB Atlas as our vector database. We built a custom RAG pipeline that uses an embedding model to convert textbook data into high-dimensional vectors. Search: We implemented cosine similarity to retrieve the most relevant context from the textbook to feed into our LLM, ensuring J.I.T.’s responses are always grounded in the source material. Challenges we ran into The biggest hurdle was latency. To keep the AR experience immersive, J.I.T. needs to respond near-instantly. We pivoted our system architecture three times to find the fastest route. Originally, we planned for the Swift frontend to communicate directly with MongoDB Atlas via App Services. However, upon discovering the service was deprecated, we had to quickly build and deploy a FastAPI middleman to bridge our frontend and database. Learning to navigate these shifts under a tight deadline was a massive test of our team's adaptability. Accomplishments that we're proud of Learning on the Fly: From zero experience in Swift to a functional AR app in 36 hours. Technical Rigor: Successfully building a complex RAG pipeline that accurately retrieves data from massive academic texts. Sponsor Integration: We are proud of how we integrated MongoDB Atlas Vector Search to solve a real-world educational problem. What we learned This hackathon was a masterclass in Vector Embeddings. We moved beyond the theory of AI to understand the mechanics of encoding inputs into vector space and using mathematical similarity to find answers. We also learned the importance of system flexibility—sometimes your first (or second) architecture plan isn't the one that makes it to the finish line. What's next for J.I.T. User-Uploaded Content: Allowing students to upload their own lecture notes or PDFs to create a "J.I.T." for any document. Multi-Modal AR: Enabling J.I.T. to "see" specific diagrams the user is pointing at in the book and explain them in real-time. Scaling the Library: Expanding our ISBN database to cover everything from technical manuals to classic literature. <div