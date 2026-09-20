---
slug: "align-sqzt8c"
url: "https://devpost.com/software/align-sqzt8c"
title: "aligned.ai"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 701
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "substrate/structured_db"
---

# aligned.ai

> Empowering Founder and VC Discovery and with You and Your Voice.

[Devpost](https://devpost.com/software/align-sqzt8c) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]] [[voice_speech]]
**substrate** [[structured_db]]

**stack** auth0, chromadb, cohere, fastapi, groq, llama, next, openai, python, react, websummit, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aligned.ai

## Body

Project Gallery Landing Page Homepage Audio Based Personality Assessment Matchmaking Page System Overview Diagram Inspiration Have you ever attended a networking event and felt overwhelmed by the sheer number of people, unsure of how to find the right connections? We've all been there, wishing for a more streamlined way to meet individuals who align with our goals and values. The inspiration for Aligned.ai comes from this common challenge—finding people who will empower you to do your life's best work. Our goal was to create a system that helps individuals build sustainable and long-lasting relationships in the startup space, whether it’s founder-to-founder or founder-to-VC. What it does Aligned.ai is a matchmaking platform designed to connect individuals in the startup ecosystem based on deep personality and goal alignment. Users engage in live, in-depth conversations with Aligned Voice, an AI-powered by Groq, which simulates a real human interaction. The system then generates a unique personality embedding using Cohere, which is stored in Chroma DB. Using powerful vector similarity algorithms, Aligned.ai ranks potential connections, presenting users with the best matches first. This way, users can find those who are not only aligned with their professional aspirations but also resonate with their personal values. How we built it Aligned.ai was developed with a focus on seamless integration across multiple technologies: Frontend: Built using Next.js, our frontend integrates Auth0 for tokenization and secure login. Data Collection: Once logged in, users create their matchmaking profiles, including data from their Web Summit profile, LinkedIn, GitHub, and more. Conversation with Aligned Voice: This core feature was powered by Groq, users engage in a live conversation that feels as natural as talking to a real person. We used Groq's integrations with Whisper for speech to text - then sent this info to our backend server for stateless requests to Groq's blazing fast llama 3 models. We experimented with various platforms but found Groq to give us the latency necessary for our needs Personality Embedding: This was the bread and butter of our app. The conversation data is processed by Cohere's Embed API to generate a personality embedding, which is stored in Chroma DB vector database. Matchmaking: Users can then search for others with similar profiles using vector similarity algorithms. This was all ran over Chroma DB's seamless and powerful interface with multiple integrations. Summaries of similarities are hosted using Groq and Cohere. The system ranks matches from most to least aligned, providing a curated list of potential connections. Reach Out: Once a match is found, users can reach out directly using the embedded social information. Challenges we ran into One of the main challenges we faced was prompt engineering—ensuring that the AI could generate meaningful and accurate personality embeddings from the conversations. Additionally, integrating the full tech stack from frontend to backend, while maintaining real-time AI performance, posed significant difficulties. Balancing the scale of integration with providing a clean and intuitive user experience was another key challenge we successfully navigated. Accomplishments that we're proud of MVP Completion: We successfully built and deployed a minimum viable product that effectively demonstrates the core functionality of Aligned.ai. Contribution to Open Source: We made a PR to improve one of the technologies we worked with, contributing back to the community. User-Centric Design: We invested significant time in UI/UX design to ensure that the user experience is as intuitive and enjoyable as possible. What we learned Through this project, we learned the immense potential of AI-driven systems to facilitate meaningful connections between individuals. The ability of autonomous agents to understand and simulate human interaction signals a new paradigm in networking and relationship-building. We also gained valuable insights into prompt engineering, real-time AI processing, and the importance of seamless integration across the tech stack. What's next for Aligned.ai The potential for Aligned.ai is vast. Moving forward, we plan to expand the action space of personality embedding and vector based search, integrating more powerful features to enhance the matchmaking process. We aim to refine the AI's ability to simulate even more nuanced human interactions and to improve the accuracy of our personality embeddings. As we continue to develop Aligned.ai, our goal is to make it the go-to platform for building meaningful, long-term relationships in the startup ecosystem. <div