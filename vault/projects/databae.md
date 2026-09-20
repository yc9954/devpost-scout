---
slug: "databae"
url: "https://devpost.com/software/databae"
title: "Databae."
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 1154
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "user/developer"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Databae.

> Simplifying databases for everyone!

[Devpost](https://devpost.com/software/databae) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[multi_agent]]
**user** [[developer]] [[researcher]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** fastapi, gcp, google, groq, llm, next.js, pandas, python, react, uagents, visualizations

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for databae.

## Body

Databae's Front Page Database Connection Page SQL Data Analysis Result from a User Query SQL Database Schema Analysis from a User Query Loading Screen Showing All Agents' Processes Databae's Page Before The User Queries Anything Inspiration As the list of use cases grow for artificial intelligence (AI for short), we thought that it is important to use AI in order to bridge the gap between those who are tech-savvy and those who are non tech-savvy. We were inspired to create this project because we know people that are not knowledgeable in SQL; we know people who are not that knowledgeable in technology that is more on the complicated side. Not everyone is a data scientist. However, a database is an entity that most people often (but do not realize) interact with. In fact, people close to us such as our parents, often are not knowledgeable in SQL. That's where we thought of Databae. Why not just use a language that most people know (in the US) such as English and use that to provide insightful analysis and visualization to the user? What it does Let's introduce you to your new friend, Databae. It is your personal AI assistant when it comes to making queries to any database and providing insightful analysis on the dataset. Let's be honest. Not everyone wants to write SQL queries. Not everyone knows SQL. Not everyone knows how to use complicated technologies. That's where Databae comes in. We utilize AI in order to use human language to provide insights on the data in your database. Databae generates a SQL query, double checks the SQL query against the database schema and prompt to make sure that it is a valid query, execute the query, and analyze the result set in order to provide you visualizations (only table form is available for now) about data that exists in your database. We do not just generate SQL queries and execute them. That is boring!!! We provide analysis on your data. Your question does not have to have anything corresponding with an SQL statement. You can perhaps ask, "Which employee in the company is best suited for frontend development?," and Databae will make sure to provide you analysis on that rather than just generating a SQL query and getting the result set. How we built it Frontend: Next.js - Basically, the core of our frontend. It displays the front page, connection page, and dashboard. Shadcn/ui - We used certain components from Shadcn/ui such as the buttons. Framer Motion - Do you see the cool animations on our website? Well, Framer Motion allows us to display those cool animations to you. Backend: Python - This is the programming language that powers our backend. FastAPI - FastAPI powers our API endpoints and allows the frontend to request data to display on the frontend. Groq: We utilized Groq's LLaMA models to be able to generate SQL queries, check the SQL queries, and analyze the result set and provide insightful analysis and visualizations. uAgents: We utilized uAgents to create AI agents that are able to communicate with one another. uAgents powers our query generator, query checker, query executor, and query analyzer. AI Agents (part of our backend): Query Generator: The query generator receive the user's request, utilizing the LLaMA model to process the user's prompt, understand and determining if a tool is need or not. If an SQL query and AI tool is needed, it will send the query to the Query Checker. If not, the workflow stops there and it will provide the user with general knowledge related to the database or its schemas. Query Checker: The query checker checks whether the SQL query generated abides by the database schema and user's prompt. If the query checker approves of the SQL query, it will forward the query to the query executor. Otherwise, it will notify the user that the query generated cannot be executed due to the query being too vague or unrelated. Query Executor: The query executor executes the query, gets the dataset from the query, and forwards the dataset to the query analyzer along with the database schema and prompt. Query Analyzer: The query analyzer analyzes the result set, gives insightful results and visualizes the results in a clear and concise manner accordingly to the user's request. Challenges we ran into As our frontend has a lot of animations and other cool elements to it, it took a long time to be able to perfect and optimize the appearance of our frontend. Being able to finetune and prompt engineer the LLM models in order to provide the appropriate responses. We had to make lots of adjustments in the prompts in order for it to provide good analysis of the data. We had to figure out how to properly translate the LLM's response into a proper Pandas DataFrame (basically the table). Handling multi-agent communication in uAgents was also a struggle as we had to figure out how to make one agent talk to another that talks to another and vice versa. Accomplishments that we're proud of We are proud of being able to utilize Fetch.AI's AI agents in order to satisfy our workflow of generating a SQL query => checking the SQL query => executing the SQL query => analyzing the SQL query and providing proper visualizations. We are also proud of being able to use Groq's extremely fast LLMs in order to quickly provide quality but fast analysis of the data in the database. Our frontend was also an important aspect. We used many libraries in order to optimize and "perfect" the appearance of our website. It took us a long time to design the website in the first place. What we learned We learned about new amazing frameworks such as Fetch.AI's AI agents. With the assistance of many mentors in CalHacks, we were able to learn a lot about new technologies and techniques We also learned about Groq's LLMs; those were vital in providing those ultra quick responses to the user, and we see many other possible use cases for it. What's next for Databae. More tools: We intend to create more tools for Databae. Our application was designed to have many more tools such as a pie chart generator, prediction models, and other tools. For our use case, we decided to only generate our visualizations in table form, but it is able to scale up in order to be able to display it in many more forms such as pie charts, bar charts, etc. Cross database analysis: What if you want to analyze multiple databases and make correlations between multiple databases? We want to add this functionality. Integration with more databases: We want to be able to have Databae be able to be integrated into more databases such as PostgreSQL, MongoDB, and other DBs. Finetuning the prompts: We want to finetune the prompts in order to provide more insightful responses and visualizations. <div