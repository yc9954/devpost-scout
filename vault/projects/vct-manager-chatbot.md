---
slug: "vct-manager-chatbot"
url: "https://devpost.com/software/vct-manager-chatbot"
title: "VCT Manager Assistant"
hackathon: "VCT Hackathon: Esports Manager Challenge"
organization: "Amazon"
winner: true
words: 1190
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# VCT Manager Assistant

> An AWS Bedrock powered Esports manager agent that analyzes VCT data to build optimal teams, evaluate player performance, and provide strategic roster recommendations.

[Devpost](https://devpost.com/software/vct-manager-chatbot) · hackathon [[VCT Hackathon- Esports Manager Challenge]]

## Facets

**mechanism** [[multi_agent]] [[retrieval_grounding]]
**domain** [[civic_government]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, aws-bedrock, aws-converse-api, aws-rds, particle, postgresql, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vct manager chatbot

## Body

Inspiration This hackathon presented an exciting opportunity to combine our interests in data engineering, intelligent agent systems, and VALORANT esports. As fans of Riot Games, we wanted to gain more experience with AWS and machine/deep learning technologies. What it does Our project is an AWS Bedrock AI-powered system that analyzes professional VALORANT player data to provide team composition recommendations and give player insights. The main goal was to provide a tool that could be helpful for a VCT manager. Team building prompts Analyzes the user input and recognizes any constraints (i.e., players from at least 3 regions) Selects the top players from each role, filtering players using specialized scores. More about this score can be seen later in this section Using the top candidates from each role, our agent system carefully constructs the team, selecting the duelist (the carry) of the team first, and building the team around them. It uses stats obtained from a tool call that runs an SQL query. More information about the retrieved data can be found later in this section Follow Up Prompts While our application often answers many of the required follow-up prompts for finalists in its team building response, our AI agent is capable of providing more information about any player from the constructed team or more information about the team itself (such as team composition and map pool) if prompted to do so. For the player replacement prompt, we decided to focus on choosing players that would synergize well with the player being replaced, while being proficient in the role of the player being replaced. Three player replacement candidates are chosen and given to the agent, and the agent reasons which player would be the best possible replacement based on their stats and potential fit for the team. Visualizations: Within our application we show several visualizations that include: Agent and map pool visualizations Tournament history performance graphs Recent tournament performance analysis Player site heatmaps for analyzing defensive setups and player positioning The agent uses all of this data to inform its player selection decisions and by complementing its responses with these visualizations, VCT managers can quickly identify what data the agent is referencing. Player Data When deciding on which players to select, we provide the agent with a comprehensive set of stats to base its reasoning and logic on. Here are a few examples of the data we provided it: General statistics (KDA, combat scores, agent pool, map experience, etc.) Granular statistics (first kill/death, econ kills, ability usage effectiveness, clutch performances, etc.) Tournament history and progression (ability to do well in high-pressure tournaments, overall performance trend, average ACS and KDA at each tournament) Recent Form (the player's performance on maps and agents during their last played tournament) In our application, we display this data clearly to the user for every player that the AI agent considered. This allows a VCT manager to get a more in-depth look at how the agent constructed the team and enables the manager to suggest replacements and perform more in-depth analysis into the team and specific players. Specialized Score As many VALORANT players know, metrics like KDA and average combat score do not tell the entire story of a player's performance, and different in-game roles cannot be evaluated the same. For example - it is much more important for duelists to get kills (trade kills, multi kills, etc.) than it is for a controller. A controller has a different kit than a duelist, which places more emphasis on utility ability usage. Therefore, for each game in our database, we graded players specifically on the role they played in that game, looking at statistics and features that are important for that role. When we select the top players for each role, this score allows us to do a more granular filtering of players, ensuring we're getting the best players for the team. How we built it Here's how we approached the development: Data Infrastructure We began by tackling the S3 bucket data, which provided a comprehensive foundation of player information and game statistics. After initial data exploration and preprocessing, we discovered the highly relational nature of the data, with numerous events and metadata. Rather than using OpenSearch, we opted for AWS RDS as our database solution, which proved both cost-effective and efficient. The data processing pipeline involved carefully parsing JSON files and designing a schema that captured essential information. Through multiple iterations, we refined our data model, occasionally supplementing it with additional player data scraped from vlr.gg. Our final RDS database occupied approximately 5GB of storage—well within AWS's free tier limit of 20GB. The richness of the game data ultimately eliminated the need for a vector database, resulting in significant cost savings for knowledge base management. AI Agent Architecture We leveraged AWS Labs' multi-agent orchestrator library and the Converse API to develop our AI agent system. The architecture consists of several specialized components: Agent Orchestrator : Analyzes user input to determine intent and routes queries to appropriate specialized agents Input Parser & Team Builder : The input parser extracts relevant constraints from user prompts The team builder agent queries our RDS database for top players and their statistics based on tournament type Team construction follows a strategic approach, starting with selecting a duelist carry and building complementary roles around them The agent considers map performance, role synergy, and statistical data while providing detailed visualizations and reasoning Player Information Agent : Handles specific player queries and follow-up questions Provides comprehensive player statistics to support its analysis and recommendations Offers detailed context for team-building decisions This architecture enables our system to provide data-driven insights while maintaining a user-friendly interface for team composition and player analysis. Challenges we ran into Understanding and processing the complex data structure took up the majority of our hackathon time Learning curve associated with first-time use of AWS Bedrock and related services Developing effective prompting strategies for consistent agent responses Balancing system complexity with cost efficiency Accomplishments that we're proud of Successfully completed a fully functional AI agent system Created agents capable of handling all example prompts with detailed reasoning Developed intelligent team building logic that considers multiple factors Implemented robust follow-up question handling Built efficient data processing pipelines while maintaining cost effectiveness What we learned The importance of strategic data preprocessing - not all available data points were necessary for meaningful team composition analysis, and selective preprocessing saved significant storage space The value of combining structured game data with supplementary sources like vlr.gg for a more complete picture The effectiveness of a role-based team building approach, starting with a core duelist and building outward The benefits of using a traditional relational database over more complex solutions when the data structure permits it The critical role of effective prompting, including the use of XML tags for section separation, descriptive tool documentation, and clear explanation of knowledge base data retrieval The importance of cost consideration in agent development and knowledge base creation How to use AWS services and build applications with them What's next for VCT Manager Chatbot Since this project was created for the sole purpose of entering this hackathon, there are no next steps. <div