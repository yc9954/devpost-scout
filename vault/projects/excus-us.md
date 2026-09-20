---
slug: "excus-us"
url: "https://devpost.com/software/excus-us"
title: "excus.us"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 874
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/government_staff"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
---

# excus.us

> Breaking barriers, building diverse networks - one event at a time.

[Devpost](https://devpost.com/software/excus-us) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[labor_employment]] [[transportation]]
**user** [[government_staff]]
**substrate** [[code_repository]] [[sensor_telemetry]]

**stack** chroma, claude, cloudflare, cohere, convex, cursor, databricks, defang, fastapi, flutter, groq, nextjs

## How they structured the write-up

- about excus.us
- how excus.us works
- technologies powering excus.us
- challenges and insights
- future roadmap
- booth interactions and footfall optimization

## Body

Excus.us: Fostering Diverse Connections Across Tech Events About Excus.us Excus.us is an innovative networking app designed to transform how professionals connect at tech events such as conferences and hackathons. Born from the observation that truly diverse interactions often lead to the most creative and impactful outcomes, Excus.us aims to break down social barriers and encourage connections between individuals with complementary yet different skills, interests, and backgrounds. Key Features Cross-Event Persistence : Unlike traditional event-specific apps, Excus.us stays with users across multiple events, building a comprehensive profile and network over time. AI-Assisted Diverse Matching : Utilizes Cohere's embedding model and Groq's reranking capabilities to connect participants with those who have different backgrounds and complementary skills. Real-Time Event Navigation : Helps users easily locate and meet their matches at crowded venues. Continuous Learning : The app refines its matching process based on user interactions and feedback. really...really fast user growth : Within a span of 4-5 hours there were 30 users actively using and chatting on the platform with 61 total registered hackers; just showing it's potential and value add in this space! How Excus.us Works Profile Creation : Users create a detailed profile highlighting their skills, interests, and background. AI Analysis : Excus.us uses Cohere's embedding model with R+ to create embeddings based on user bios and interests. Diverse Matching : The app uses Groq for quick reranking, utilizes Cohere's embeddings on Chroma to assist in matching users with those who have diverse profiles (based on their bios and interests) compared to their own. In-Event Connections : Users receive suggestions about potential matches and can use the app to locate and chat with them during the event. Cross-Event Networking : Excus.us maintains connections post-event, allowing users to build a diverse network that grows with each new event attended. Technologies Powering Excus.us Cohere's Embedding Model with R+ : Creates embeddings based on user bios and interests, and assists with translation when needed. Clerk : Authentication! Convex : Manages real-time chat and persistent user data across events. Also handles the auth tokens. Groq : Provides quick reranking capabilities for efficient diverse matching. ChromaDB : Stores and queries vector embeddings of user profiles for efficient matching. Mappedin : Provides real-time navigation within event venues. Next.js : Builds the responsive and intuitive user interface. FastAPI + Defang : Handles backend operations and API calls, with efficient deployment. Posthog & Databricks : Analyze user behavior and app performance for continuous improvement. Flutter : Powers the admin mobile app for managing user issues and communications. Cloudflare Workers : Used in conjunction with Resend for efficient email communications. Every time a match is made, a call is fired to the Cloudflare worker! Challenges and Insights Balancing Diversity and Relevance : Ensuring suggested matches are diverse yet still beneficial to users' professional growth. Cross-Event Data Management : Maintaining user data across multiple events while ensuring privacy and security. Real-Time Scaling : Managing the app's performance during high-traffic event periods. Encouraging Diverse Interactions : Designing features that motivate users to connect with individuals outside their usual professional circles. Future Roadmap Enhanced AI Assistance : Improving the AI's ability to suggest relevant diverse connections without generating content. Virtual and Hybrid Event Support : Expanding capabilities to cater to various event formats. Diversity Impact Metrics : Developing tools to measure and visualize the impact of diverse networking on professional growth. Multilingual Support : Leveraging Cohere's R+ for improved translation capabilities to facilitate connections across language barriers. Expanded Language Support : Introducing support for additional languages to cater to a global audience and foster international connections. Interactive Icebreakers : Implementing AI-generated conversation starters and questions tailored to each match, helping users initiate meaningful discussions. Booth-Attendee Matching : Developing a feature to connect attendees with relevant exhibitor booths based on interests and potential business opportunities. Post-Event Follow-up Assistance : Providing tools to help users maintain and nurture connections made during events. Booth Interactions and Footfall Optimization During our research, we discovered that exhibitors at tech events often struggle with inconsistent booth traffic and difficulty in attracting the right audience. To address this, Excus.us is expanding its functionality to include: Booth-Attendee Matching : Using our AI-powered matching system to connect attendees with booths that align with their interests and potential business needs. Booth Traffic Analytics : Providing real-time and post-event analytics on booth traffic, helping exhibitors optimize their strategies. Scheduled Booth Visits : Allowing attendees to book short meetings with booth representatives, ensuring a steady flow of interested visitors. Interest-Based Notifications : Sending targeted notifications to attendees about relevant booth presentations or demos. Virtual Queue Management : Implementing a virtual queuing system for popular booths to reduce crowding and improve the experience for both attendees and exhibitors. Feedback Loop : Collecting and analyzing attendee feedback on booth interactions to help exhibitors refine their approach for future events. By addressing both attendee networking and booth interaction challenges, Excus.us aims to create a more holistic and efficient event experience for all participants. Excus.us is committed to creating a more interconnected and diverse professional community, one event at a time. By leveraging advanced AI technologies to assist in fostering unexpected connections and optimizing event interactions, we aim to spark innovation, broaden perspectives, and create a more inclusive and efficient tech ecosystem. <div