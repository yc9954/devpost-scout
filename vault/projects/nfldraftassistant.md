---
slug: "nfldraftassistant"
url: "https://devpost.com/software/nfldraftassistant"
title: "NFLDraftAssistant"
hackathon: "TiDB Future App Hackathon 2024"
organization: "PingCAP"
winner: true
words: 1073
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# NFLDraftAssistant

> Dominate Your NFL Fantasy Draft with Smart Recommendations and Expert Insights, All Powered by AI and TiDB

[Devpost](https://devpost.com/software/nfldraftassistant) · hackathon [[TiDB Future App Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[researcher]]
**substrate** [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** flask, html, javascript, python, render, tidb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nfl draft assistant

## Body

TiDB NFL Fantasy Draft Assistant NFL Draft Assistant Inspiration As a passionate fantasy football player for the past 5 years, I've experienced the highs and lows of the game. Despite my dedication, the championship title has eluded me, with last year's semi-final loss being particularly heartbreaking. The root of my struggles often lay in suboptimal drafting strategies and the challenge of keeping up with preseason projections and player news. Balancing a busy work life with the extensive research required for fantasy football success became increasingly difficult. However, the competitive spirit in me couldn't bear the thought of letting my friends win again. I realized I could leverage my skills as a data scientist to create a tool that would consolidate all the necessary information in a simple, accessible manner. Recognizing that many other fantasy football enthusiasts face similar challenges, especially during the peak of draft season, I was inspired to create the NFL Draft Assistant. This tool aims to level the playing field, providing data-driven insights and recommendations to help players make informed decisions during their drafts. What it does The NFL Draft Assistant leverages TiDB Serverless Vector Search as its core technology to provide comprehensive fantasy football drafting support: Draft Chatbot (LangGraph Agent) : Utilizes TiDB Serverless Vector Search for lightning-fast retrieval of relevant fantasy football articles and player reports. The vector search capability allows for semantic understanding, enabling the chatbot to provide context-rich, accurate responses to draft-related queries. TiDB's efficient storage and retrieval power the Retrieval-Augmented Generation (RAG) process, enhancing the quality of real-time draft advice. YouTube Expert Chatbot : Leverages TiDB's vector search to perform channel-specific searches on vectorized YouTube video transcripts. TiDB's flexible filtering allows users to target advice from specific fantasy football experts, with vector search ensuring relevance and accuracy. The RAG process, powered by TiDB, enables the chatbot to synthesize insights from various YouTube sources quickly. Player Similarity Search : Harnesses TiDB's advanced vector search capabilities to find players with similar attributes and projections in milliseconds. The vector representations of player data stored in TiDB allow for nuanced comparisons beyond simple stat matching. TiDB's efficiency enables real-time similarity searches during drafts, aiding quick decision-making. Draft Recommendation Engine : Uses a reinforcement learning model in the background to provide you the best options to draft at every rounds with a reward score optimized on team balance, position depth, bench strength, maximum weekly team points etc. How we built it TiDB Serverless Vector Search was the cornerstone of our development process: Data Vectorization and Storage : We used advanced NLP tools from langchain and open source LLMs powered by Ollama to collect and convert fantasy football articles, player reports, and YouTube transcripts into high-dimensional vectors with gemini embedding model. These vectors were then efficiently stored in TiDB, leveraging its serverless architecture for scalability and cost-effectiveness. Vector Search Integration : We implemented custom Python functions to interface with TiDB's vector search capabilities, enabling semantic search across our datasets. TiDB's SDK was used to perform similarity searches, allowing us to find relevant content and similar players quickly. RAG Implementation : The Retrieval-Augmented Generation process was built around TiDB's vector search. We used it to fetch relevant context for our LLM, significantly improving the quality of generated responses. Backend Development : Our Flask backend was designed to make efficient calls to TiDB for vector searches, ensuring low-latency responses even under high load. We implemented connection pooling and query optimization to maximize TiDB's performance. Similarity Search Algorithm : We developed a custom algorithm that utilizes TiDB's vector search to find similar players based on multi-dimensional attributes. Data Pipeline : We created a pipeline to update our TiDB vector store with new articles, player updates, and YouTube content. This pipeline ensures that our vector database remains current, leveraging TiDB's ability to handle frequent updates efficiently on demand runs. Frontend-Backend Integration : The frontend was designed to make asynchronous calls to our Flask API, which in turn queries TiDB for vector search results. We implemented efficient data serialization to quickly transmit vector search results from TiDB to the frontend. Challenges we ran into UI/API Integration : The major challenge was getting the UI and JavaScript to interact seamlessly with Flask APIs. This required a deep dive into frontend-backend communication and asynchronous programming. Player Report Generation : Obtaining detailed player reports proved difficult as most sources keep this information unscrappable. To overcome this, we took an innovative approach by generating player reports from scratch for all 200 players using Llama 3.1 on a local Ollama setup. Accomplishments that we're proud of Successfully integrated TiDB Serverless Vector Database, leveraging its capabilities for efficient data storage and retrieval in a complex, real-world application. Created a user-friendly UI with JavaScript and HTML, stepping out of my comfort zone as a data scientist. Deployed a fully functional application from idea to project in less than two weeks, showcasing rapid development with cutting-edge technologies. Implemented a sophisticated LangGraph agent for the Draft Chatbot, enhancing its ability to provide context-aware responses through TiDB's vector search. Developed a novel approach to generate player reports using AI when traditional data scraping methods were not feasible, expanding our data sources. What we learned Gained practical experience in integrating TiDB Serverless Vector Database into a real-world application, understanding its powerful capabilities for semantic search and similarity matching. Improved skills in frontend development, particularly in creating interactive UIs and connecting them to backend services powered by vector databases. Deepened understanding of RAG techniques and their application in creating more intelligent chatbots, especially when combined with efficient vector storage and retrieval. What's next for NFL Draft Assistant Enhanced Player Recommendations : Improve the similar player recommendation system by incorporating more detailed projections and comprehensive player reports, leveraging TiDB's vector search for more nuanced comparisons. Real-time Data Updates : Implement a system for real-time updates of player news, injuries, and performance data during the draft season, taking advantage of TiDB's efficient update capabilities. Mobile App Development : Create a mobile version of the assistant for on-the-go access during live drafts, ensuring TiDB's vector search performance translates well to mobile platforms. Integration with Fantasy Platforms : Develop plugins or APIs to integrate directly with popular fantasy football platforms for seamless draft assistance, potentially using TiDB as a high-performance intermediary data layer. Community Features : Implement user accounts and community features to allow sharing of insights and strategies among users, possibly using TiDB to store and search user-generated content vectors. <div