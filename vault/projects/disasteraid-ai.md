---
slug: "disasteraid-ai"
url: "https://devpost.com/software/disasteraid-ai"
title: "DisasterAid.ai"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 523
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# DisasterAid.ai

> Disasteraid.ai is an AI-powered platform consolidating trustworthy live updates about ongoing crises and packages them into summarized info-bites to enhance emergency response management.

[Devpost](https://devpost.com/software/disasteraid-ai) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[civic_government]] [[disaster_emergency]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[web_dom]]

**stack** anthropic, bedrock, claude, docker, google, huggingface, javascript, mapbox, maps, typescript, you.com

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for disasteraid.ai

## Body

UI for the software Answers from DisasterAid.ai upon asking "where should I go get food and stay safe" Software Architecture Diagram Inspiration The increasing frequency and severity of natural disasters such as wildfires, floods, and hurricanes have created a pressing need for reliable, real-time information. Families, NGOs, emergency first responders, and government agencies often struggle to access trustworthy updates quickly, leading to delays in response and aid. Inspired by the need to streamline and verify information during crises, we developed Disasteraid.ai to provide concise, accurate, and timely updates. What it does Disasteraid.ai is an AI-powered platform consolidating trustworthy live updates about ongoing crises and packages them into summarized info-bites. Users can ask specific questions about crises like the New Mexico Wildfires and Floods to gain detailed insights. The platform also features an interactive map with pin drops indicating the precise coordinates of events, enhancing situational awareness for families, NGOs, emergency first responders, and government agencies. How we built it Data Collection: We queried You.com to gather URLs and data on the latest developments concerning specific crises. Information Extraction: We extracted critical information from these sources and combined it with data gathered through Retrieval-Augmented Generation (RAG). AI Processing: The compiled information was input into Anthropic AI's Claude 3.5 model. Output Generation: The AI model produced concise summaries and answers to user queries, alongside generating pin drops on the map to indicate event locations. Challenges we ran into Data Verification: Ensuring the accuracy and trustworthiness of the data collected from multiple sources was a significant challenge. Real-Time Processing: Developing a system capable of processing and summarizing information in real-time requires sophisticated algorithms and infrastructure. User Interface: Creating an intuitive and user-friendly interface that allows users to easily access and interpret information presented by the platform. Accomplishments that we're proud of Accurate Summarization: Successfully integrating AI to produce reliable and concise summaries of complex crisis situations. Interactive Mapping: Developing a dynamic map feature that provides real-time location data, enhancing the usability and utility of the platform. Broad Utility: Creating a versatile tool that serves diverse user groups, from families seeking safety information to emergency responders coordinating relief efforts. What we learned Importance of Reliable Data: The critical need for accurate, real-time data in disaster management and the complexities involved in verifying information from various sources. AI Capabilities: The potential and limitations of AI in processing and summarizing vast amounts of information quickly and accurately. User Needs: Insights into the specific needs of different user groups during a crisis, allowing us to tailor our platform to better serve these needs. What's next for DisasterAid.ai Enhanced Data Sources: Expanding our data sources to include more real-time feeds and integrating social media analytics for even faster updates. Advanced AI Models: Continuously improving our AI models to enhance the accuracy and depth of our summaries and responses. User Feedback Integration: Implementing feedback loops to gather user input and refine the platform's functionality and user interface. Partnerships: Building partnerships with more emergency services and NGOs to broaden the reach and impact of Disasteraid.ai. Scalability: Scaling our infrastructure to handle larger volumes of data and more simultaneous users during large-scale crises. <div