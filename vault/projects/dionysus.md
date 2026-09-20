---
slug: "dionysus"
url: "https://devpost.com/software/dionysus"
title: "Dionysus"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 655
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Dionysus

> Dionysis is a developer's tool for easier collaboration. It generates code documentation, helps you find code fast, and simplifies post-meeting questions.

[Devpost](https://devpost.com/software/dionysus) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
  <sub>weak: retrieval_grounding</sub>
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[transcript_audio]] [[video_visual]]

**stack** docker, docker-compose, github, langchain, nextjs, openai, pineconedb, python, trpc

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Dashboard Page AI Generated Documentation AI Answer using Retrieval Augmented Generation File Tree Visualisation Real-Time Contextual Meeting Search AI processed Meeting Minutes Question History Inspiration The inspiration behind Dionysus stemmed from the challenges we've all faced as developers when collaborating on code projects. We realized the need for a tool that simplifies the process, streamlines code understanding, and enhances teamwork. Dionysus was born out of this necessity to create a developer-friendly collaboration platform. What it does Dionysus is a powerful platform designed to simplify developer collaboration. It offers a range of features that make working on code projects more efficient and transparent: Automatic Code Documentation: Dionysus automatically generates detailed code documentation, making it easy for both newcomers and experienced developers to understand the project's structure and purpose. Codebase Search: With context-aware search capabilities, Dionysus helps you quickly locate specific code components, saving you valuable time and effort. Commit Message Summaries: Using AI, Dionysus summarizes commit messages, ensuring that you're always up to date with the latest changes in your repository. Meeting Transcription: Dionysus can transcribe your meetings, extracting key topics and providing a clear record of what was discussed. Real-Time Contextual Meeting Search: When you have questions about past meetings, Dionysus offers real-time contextual search, so you can easily find the answers you need. Collaborative Platform: Team members can work together within the platform, access documentation, review meeting summaries, and interact with codebase-related data, fostering a collaborative and efficient development environment. How we built it Dionysus was built using the following technology stack: We are using a microservice architecture . We have a frontend using NextJS and a Python backend API that handles all the AI workload. We relied on docker to containerize both our microservices so as to allow for easier development using docker-compose. We no longer need to run the microservices one by one when trying to develop. We can simply run docker-compose up and all our services are up and running. We pushed our Dockerfile to docker hub to https://hub.docker.com/repository/docker/elliottchong/dionysus-backend/general . We deployed our docker image to fly.io , which is an automated deployment platform. We set up a CI/CD pipeline such that it detects whenver a new version of the repo has been pushed and fly.io automatically deploys the new version of it. AI-powered tools for code analysis and document generation. Integration with GitHub for repository management. Meeting transcription services for accurate recording of discussions. Real-time contextual search to provide instant and relevant information. The development process involved the collaboration of a diverse team of developers, designers, and AI specialists who worked together to bring Dionysus to life. Challenges we ran into While building Dionysus, we encountered various challenges, including: Integrating AI and machine learning into the platform effectively. Ensuring real-time updates and accuracy in codebase search and meeting transcriptions. Implementing a user-friendly interface that is both powerful and easy to use. Accomplishments that we're proud of We're proud of what Dionyuis has become—a tool that simplifies the lives of developers and enhances collaboration. The accomplishments we're most proud of include: Successfully automating code documentation generation. Developing context-aware codebase search capabilities. Achieving real-time, AI-powered meeting transcription and contextual search. What we learned During the development of Dionysus, we learned valuable lessons about the power of AI in simplifying and enhancing the developer experience. We also gained insights into the importance of user-friendly design and seamless collaboration tools. What's next for Dionysus In the future, we plan to expand Dionysus's capabilities further. We aim to: Improve AI algorithms for even more accurate code documentation and search results. Add support for more code repository platforms to reach a broader audience of developers. Enhance the user interface for an even more intuitive and user-friendly experience. We're excited about the potential of Dionysus and the positive impact it can have on the developer community. Stay tuned for upcoming features and improvements! In the demo video I used the audio from the following video: https://www.youtube.com/watch?v=HKdOnFHB4Sg <div