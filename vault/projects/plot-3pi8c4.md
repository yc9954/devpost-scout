---
slug: "plot-3pi8c4"
url: "https://devpost.com/software/plot-3pi8c4"
title: "Plot"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1234
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/housing_homeless"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Plot

> Plot delivers comprehensive insights on any location. Whether you're scouting investments or shaping skylines, Plot helps you shape your plot’s plot—making smarter decisions before you break ground.

[Devpost](https://devpost.com/software/plot-3pi8c4) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]] [[disaster_emergency]] [[education]] [[housing_homeless]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]]

**stack** langchain, mapbox, mistralai, next.js, openai, perplexity, react, recharts, typescript, zustand

## How they structured the write-up

- inspiration
- building the project
- challenges faced
- development tools & technologies
- what we learned
- conclusion

## Body

Opportunities Search Loading Landing Page Real Estate Deep Agent Loading Profile Page Portfolio View Perplexity Opportunities Search Perplexity Opportunities Search II Real Estate Deep Agent Results Inspiration This project was born out of our own personal pain points as students. Like many others, we’ve faced the challenges of searching for housing at school, for summer internships, full-time roles, and traveling. When planning my trip to Rome, I had no idea which area was safe to stay in for an Airbnb. I ended up spending hours on Reddit looking for reviews and suggestions, which felt inefficient and time-consuming. This made us realize that finding the right places to stay could be far more seamless with the right insights from the right sources. We saw a gap in the market for a platform that could quickly and accurately provide sentiment data on locations, helping people make informed decisions about housing, whether for short-term stays or long-term investments. What if we could make this process faster and more efficient? Building the Project Our first step was building a sentiment analysis engine, since we knew there was an abundance of social media data available to us. We could easily aggregate what people were saying about different places—whether it’s about the safety of neighborhoods, or the overall vibe of a city. Using AI agents, we orchestrated a workflow to perform searches and analyze sentiment across multiple data sources. Our initial goal was to build a simple map for sentiment analysis, but as we refined our approach, we realized that there’s a much broader context to consider when evaluating a location. Beyond social media data, factors like economic trends, natural disasters, and local events all impact people's perceptions of a place. This insight led us to expand our project to build a comprehensive property intelligence platform. We also worked closely with mentors and property developers who helped us understand the nuances of the industry. It became clear that our platform could be extremely valuable to property developers, who need to analyze many of the same factors as renters, but with a much longer-term view. This shift in perspective led us to add features specifically catered to property developers, such as real-time property data streams and a user profile page to inform the agentic search. Core Technology The core of our project lies in a swarm of AI agents that execute parallel tasks to gather, analyze, and update data in real time. The following are some notable components of this project. Core Architecture : The project is built as a Next.js application with TypeScript, focusing on real estate market analysis using sentiment analysis. The main components are organized in a modular structure with clear separation of concerns between UI, services, and data processing. Data Collection : The agentic workflow kicks off by scouring various data sources, including social media, news outlets, economic reports, and environmental data. The agents target specific factors that influence a location's desirability, such as crime rates, job market trends, housing prices, and local events. Sentiment Analysis : The SentimentAnalyzer class serves as the core engine for processing sentiment data. It evaluates the tone and context of online discussions—whether people are generally positive or negative about a particular area. Multiple data sources are supported through a pluggable architecture, and the analyzer processes text data in parallel. Results include sentiment scores, keyword extraction, and temporal analysis. Sentiment Dashboard Interface and Real-Time Updates : The SentimentDashboard acts as the main visualization interface. Its main features include multi-location analysis support, real-time sentiment scoring, interactive charts showing sentiment trends, keyword highlighting, and mention tracking. Risk Assessment : Parallel to sentiment analysis, other agents use the Federal Emergency Management Agency API to assess the risk factors of a location, such as history of natural disasters (e.g., floods, earthquakes), economic volatility, or crime rates. These agents pull data from global news, scientific studies, and financial reports to generate a comprehensive risk profile. Data Synthesis and Updates : As new information comes in, agents continuously update the platform (map, search results) in real time. If a major news event occurs or if sentiment shifts dramatically, the agents immediately re-analyze the data and adjust the results. This enables our users to have access to the most up-to-date information, helping them make decisions on the fly. The orchestration of these technologies allows us to gather and process a wide variety of data points quickly and efficiently, ensuring that the platform is always fresh and relevant. Challenges Faced One of the major challenges we faced was aligning the project’s goals with our different interests and backgrounds. We were all beginners at some aspects of the technologies we wanted to use, so balancing the desire to learn new things with the need to create something useful was tricky. However, the sentiment analysis aspect of the project—along with the real-world applications for both travelers and property developers—kept us focused and motivated. Another challenge was figuring out how to make the platform both effective and scalable. We needed to ensure the sentiment analysis could be done in real-time and that it could incorporate data from diverse sources. This is where our sponsors played a huge role in helping us streamline the process. Thanks to Langchain, Mistral AI, and Perplexity, we were able to perform high-efficiency searches and provide insights quickly. Development Tools & Technologies Throughout this journey, we leaned heavily on tools from our sponsors to improve efficiency and enhance our workflow: Perplexity was instrumental in answering queries and performing real-time searches, which helped us gather valuable insights quickly. The search integration within Perplexity Sonar made it ideal for our needs, and we frequently queried it during the project. Windsurf by Codeium became our go-to tool for boosting productivity. It helped us 10x our efficiency, thanks to its memory and model context protocol features, which were vital for informing Cascade to make useful code edits and suggestions. Langchain served as our foundation for building complex AI workflows. Its composable chains and agent frameworks helped us orchestrate our swarm of AI agents effectively, enabling seamless integration of different data sources and analysis tools into our pipeline. Mistral AI powered our core sentiment analysis engine with its robust language understanding capabilities. We leveraged its models for processing and analyzing text data from various sources, providing accurate sentiment scoring and context-aware analysis that formed the backbone of our real-time insights. What We Learned This project taught us a lot about the importance of balancing innovation with utility. While we were initially excited about the "cool" factor of sentiment analysis, it was only by catering to the needs of property developers that we were able to make it truly useful. Additionally, we learned how to work effectively as a team despite coming from different schools and backgrounds. We also gained a deeper understanding of how AI can be applied to solve real-world problems at scale—particularly in fields like property development, where data-driven decisions can make or break a project. Conclusion We’re incredibly proud of what we’ve built. We’ve created something unique that taps into the power of real-time, sentiment-driven property intelligence. By incorporating community sentiment, economic indicators, and real-time updates, our platform offers a truly comprehensive view of any location. There’s no other product on the market quite like ours, and we’re excited to see where it goes from here. We hope you enjoy exploring our project as much as we enjoyed building it! <div