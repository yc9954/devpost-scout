---
slug: "vct-scout"
url: "https://devpost.com/software/vct-scout"
title: "VCT Scout"
hackathon: "VCT Hackathon: Esports Manager Challenge"
organization: "Amazon"
winner: true
words: 712
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
---

# VCT Scout

> VCT Scout is an AI assistant, powered by Amazon Bedrock. It streamlines team-building and player analysis, offering managers data-driven insights to optimize recruitment and strategy.

[Devpost](https://devpost.com/software/vct-scout) · hackathon [[VCT Hackathon- Esports Manager Challenge]]

## Facets

**mechanism** [[retrieval_grounding]]
  <sub>weak: realtime_stream</sub>
**domain** [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]]

**stack** amazon-api-gateway, amazon-athena, amazon-bedrock, amazon-bedrock-agents, amazon-cloud-formation, amazon-cloudfront-cdn, amazon-cognito, amazon-dynamodb, amazon-knowledge-bases, amazon-lambda, amazon-web-services, aws-cloudscape, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- key accomplishments
- lessons learned
- what's next for vct scout

## Body

final output with player and top map cards Worst Nightmare!!! helper prompts Upon LEFT Mouse clicking any Player Card chat interface without any cards complete session/chat history data admin dashboard to add additional text based data to the RAG (not visible to regular users) additional stats on a player Inspiration Each team member found a unique inspiration for VCT Scout. For some, it was the excitement of testing the boundaries of large language models (LLMs) in a complex, multi-tool chatbot system capable of synthesizing various data sources into cohesive, actionable insights. Others, as passionate Valorant players and skilled software engineers, saw this as the perfect blend of two interests. Together, we formed a team with the diverse skills necessary to tackle this challenge. What it Does VCT Scout is an AI assistant powered by Amazon Bedrock, designed to help users generate optimal Valorant teams through natural language queries. By analyzing comprehensive player stats and game insights, it streamlines team-building and player analysis, providing managers with data-driven insights for recruitment and strategy optimization. How We Built It Following AWS tutorials on Bedrock and Knowledge Bases, we set up a foundational RAG (Retrieval-Augmented Generation) system using Valorant-related data on agents, abilities, and basic gameplay knowledge. To manage the large volume of game data, we employed AWS Lambda and an SQS pipeline to convert JSON files into JSONL format for compatibility with AWS Athena. From there, we built efficient queries in Athena to create compact, query-friendly tables. Using Claude’s tool API, we linked these data tables to VCT Scout, enabling the chatbot to retrieve general information on Valorant, as well as specific player stats like kills and assists. A detailed system prompt orchestrates these tools for a seamless team-building experience. The frontend was developed in React, styled to mirror Valorant’s interface with custom themes. We used Vite for a streamlined development process, AWS Cognito for user authentication, and incorporated FontAwesome, React Router, and Cloudscape components to enhance the user experience. Challenges We Faced The biggest challenge was processing and structuring the game data for quick retrieval. Through numerous iterations of data structuring, joins, and aggregations, we eventually created a master table containing all essential stats. Complex Data Schema Definition Issue: Accurately defining Athena table schemas to parse intricate nested JSON structures was time-consuming and prone to errors. Solution: Iteratively refined the schema, ensuring all event types were correctly represented to prevent parsing issues. Managing Large Datasets and Query Performance Issue: Processing over 4,700 game files (for vct-challengers) led to long query execution times, exceeding Athena’s 30-minute limit. Solution: Split queries by tournament and created intermediate tables to manage and optimize data processing. Iterative Table Creation and Partitioning Issue: Refining table schemas and managing partitions required multiple iterations, slowing progress. Solution: Strategically organized data by tournaments and utilized partitioning to enhance query performance and manageability. Other challenges Handling Empty JSON Structures: Certain events, like gameEnded, were empty objects ({}), causing syntax errors in table definitions. Optimizing complex SQL queries: Complex joins and extensive use of CTEs resulted in inefficient queries that were difficult to execute within resource constraints. Accurate data mapping and agent identification: Mapping in-game player IDs to esports player IDs and associating actions with the correct agents was complex. and so on. Key Accomplishments We’re particularly proud of our success in integrating AWS tools to handle and query data at scale, and in designing an intuitive tool that assists users in building Valorant teams based on real stats. Lessons Learned While some of us were new to Valorant, we quickly got up to speed with the game mechanics, with a few even joining in on the gameplay! For others, the project was an opportunity to dive deeper into generative AI concepts and AWS Bedrock, expanding our knowledge of these powerful tools. Together, we sharpened our skills in crafting precise prompts for LLM agents, a crucial aspect of managing and optimizing complex data queries. What's Next for VCT Scout Our next steps include refining the UI/UX for enhanced usability, incorporating more robust data sources, and working toward a full production deployment. Test Login Credentials To access the VCT Scout tool, use the following test credentials: Username : me117.rs@gmail.com Password : P@ssword123! Additionally, invitations have been sent to the following email addresses: testing@devpost.com riot-esports-hackathon-rg@riotgames.com aws-riotgames-hackathons@amazon.com <div