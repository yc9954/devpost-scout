---
slug: "adimpact-databot"
url: "https://devpost.com/software/adimpact-databot"
title: "AdImpact Databot"
hackathon: "THE FUTURE OF AI IS OPEN"
organization: "Snowflake"
winner: true
words: 815
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# AdImpact Databot

> Safely query a database schema using natural language. LLM-generated SQL statements are parsed, corrected, and checked for safety and security before being run and explained to the user.

[Devpost](https://devpost.com/software/adimpact-databot) · hackathon [[THE FUTURE OF AI IS OPEN]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]] [[researcher]]
**substrate** [[financial_record]] [[structured_db]] [[transcript_audio]]

**stack** amazon-web-services, arctic, cortex, foundationdb, java, python, snowflake, state-machine, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for adimpact databot
- about the team

## Body

Instance #1 of the databot looks at AdImpact political advertising data. It allows natural language query of complex datasets, and can explain the SQL statements it generates. Using Cortex's TRANSLATE() and SUMMARIZE() functions, we can extract short summaries of ad text to understand what politicians are saying. Instance #2 of the Databot looks at AdImpact automotive ads -- it takes just a minor configuration change to look at a different dataset. The state machine used by the agent to mediate among the user, the Arctic LLM, the SQL Analyzer, and the Snowflake Database. The AdImpact Databot Team: Michael, Daniel, Minita, and Joe. Inspiration The idea for AdImpact Databot was born out of the need to empower our analysts, who excel with Excel and Tableau but lack SQL expertise, to harness the full potential of our data. We recognized the potential of Large Language Models (LLMs) to bridge this gap by converting natural language instructions into working SQL statements. Our goal was to create a tool that not only answers queries but also educates users on SQL, ensuring secure and safe data interactions. What it Does AdImpact Databot enables users to query databases using natural language, translating these queries into SQL. It provides answers and explanations, guiding users through the nuances of SQL. The bot ensures security by parsing and validating SQL statements, restricting them to safe read-only operations. Users interact with the Snowflake Arctic LLM only through the SqlAgent mediator, which manages state transitions and ensures secure, meaningful responses. The version exposed for the contest has access to 2024 US political ad and spending information; pointing it at different tables would need only a simple configuration change. How We Built It We built the AdImpact Databot on top of Snowflake, Arctic, and Streamlit, plus our own leading-edge LLM agent code. Some key aspects of the tool: Configurability : Allows easy setup of new instances with minimal configuration changes, adapting to different data sets and user needs. SQL Agent with State Machine : Manages interaction states: awaiting input, prompting the LLM, running SQL commands, and sending output. SQL Parser and Validator : Ensures SQL statements are valid and read-only. Security Measures : Configured Snowflake users and roles to limit access and prevent security breaches. Performance Optimization : Improved response times through database tuning and session state maintenance. Challenges We Ran Into Security and Safety : Ensuring the LLM-generated SQL statements were secure and adhered to read-only operations. Performance Issues : Initial response times were slow, requiring extensive optimization. Testing and Usability : Designing and testing the chatbot required diverse user interactions to uncover potential issues and improve usability. Context Window Limitations : Dealing with the Arctic LLM’s token limit required careful prompt construction and metadata management. Accomplishments that We're Proud Of Security Architecture : Successfully implemented a robust security system to prevent SQL injection and unauthorized data access. Configurability and Scalability : Achieved a highly configurable system that can be easily adapted to different use cases with minimal effort. Data Enrichment : Used Cortex TRANSLATE() and SUMMARIZE() functions to turn ad transcripts, some in Spanish and some very long, into pithy English extracts. Performance Improvements : Significantly reduced response times, ensuring a smoother user experience. User Empowerment : Enabled non-technical users to interact with and understand complex data through natural language queries. What We Learned Importance of Diverse Testing : Engaging multiple testers revealed unexpected issues and improved the system’s robustness. Effective Metadata Utilization : Embedding database documentation in view creation statements enhanced the LLM’s ability to infer and explain data structures. Prompt Engineering : Providing sample results and focusing on reporting tables improved the LLM’s query accuracy and user comprehension. What's Next for AdImpact Databot Refinement of Capabilities : Experiment with different system prompts to elicit varied behaviors and further optimize performance. Integration with Existing Products : Embed AdImpact Databot’s capabilities into our existing products to provide faster, more accurate information to users. Enhanced User Training and Documentation : Develop comprehensive guides and training programs to maximize user engagement and understanding. Advanced Security Features : Implement real-time monitoring and dynamic access controls to further enhance security. Scalability and Load Management : Ensure the system can handle increased loads and implement load balancing techniques to distribute computational resources effectively. By continuing to refine and expand AdImpact Databot, we aim to create an indispensable tool that not only answers queries but also educates and empowers our users, making data interaction more intuitive and secure. About the Team AdImpact CTO Michael Schader uses his PhD in Swarm Robotics to turn everything into a multiagent system. Full Stack Developer Daniel Brewer hacks on LLMs and video processing pipelines just for fun. Database Manager Minita Surti created and maintains a logical data architecture that's easy for both humans and machines to work with. Database Analyst Joe Bieda makes it all make sense with his command of the data dictionaries. <div