---
slug: "sql-murder-mystery-game"
url: "https://devpost.com/software/sql-murder-mystery-game"
title: "QueryHunt - SQL Murder Mystery Game"
hackathon: "TiDB Future App Hackathon 2024"
organization: "PingCAP"
winner: true
words: 576
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "substrate/structured_db"
---

# QueryHunt - SQL Murder Mystery Game

> Practise and learn SQL by solving engaging AI-generated crime mysteries.

[Devpost](https://devpost.com/software/sql-murder-mystery-game) · hackathon [[TiDB Future App Hackathon 2024]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[finance_payments]]
**substrate** [[structured_db]]

**stack** llama-index, pymysql, python, streamlit, tidb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for queryhunt - sql murder mystery game

## Body

Inspiration While text-to-SQL AI tools are impressive, SQL remains the top in-demand skill for the majority of tech roles. QueryHunt is a SQL game that uses modern AI technology to create an engaging and interactive playing and learning experience. The inspiration for this project came from the original SQL Murder Mystery game created by Joon Park and Cathy He. What It Does The game starts with an LLM generating a unique murder mystery story and inserting data into the tables. The objective is to explore the data by running various SQL queries to identify the correct murderer. Users can view the schema and run queries in a SQL editor. The LLM can provide relevant hints based on the user's previous queries. How We Built It QueryHunt is built using TiDB Serverless, the GPT-4 model, and a mix of open-source libraries. TiDB Serverless plays crucial role in the project due to its scalability and fast query response times. The ability to store relational data along with vector embeddings in the same database is a huge plus of TiDB. Below is a high-level overview of each technology and its role in the project: TiDB Serverless : Used for storing AI-generated temporary game data. The following tables are utilized in the game: Victim Suspects Evidence Alibis CrimeScene Murderer (admin-only) TiDB VectorSearch : When generating a story, the model references embeddings of the DBML schema stored in the vs_game_schema table. This ensures the model generates valid SQL INSERT queries with game data. Llama-Index : Handles main workflow orchestration with self-healing. The workflow steps are as follows: Generate story Generate data based on the story (outputs SQL INSERT queries) Validate queries (includes data cleaning and syntax checks) Self-correct (optional step if validation fails, repeated up to 3 times) Execute queries (insert data into TiDB tables for the game) Llama-Index is also used to query the TiDB VectorStore. Streamlit : Serves as the frontend of the app, using the custom component Streamlit-Ace for the SQL Editor. Challenges We Ran Into I encountered local issues with SSL certificates when trying to connect to the TiDB cluster, which took some time to resolve. There was an error when querying the vector index, but the issue was promptly resolved by Cheese Wong. Parsing the model's response into SQL queries was challenging at times, as the model occasionally added extra characters that failed the validation step. Accomplishments We're Proud Of I’m very proud of building this app in a relatively short time with no prior knowledge of TiDB or Llama-Index workflows. I’m also pleased that the game functions as expected during the ideation phase. What We Learned I learned how to use TiDB Serverless with relational databases and VectorSearch features. The experience was pleasant and straightforward due to the good documentation and technology platform. I had some prior experience with Llama-Index but decided to explore their new workflow features and apply them to this project. It was a bit challenging but a very rewarding learning experience. What's Next for QueryHunt - SQL Murder Mystery Game I already have multiple ideas for new features and improvements for the game, including: Level of Difficulty : Store previous user games in TiDB VectorStore and reference them to create progressively more difficult games. This way, users will never play the same game twice and will be continuously challenged. User Authentication : Log in and sign up functionality. AI-Generated Schema : Create a truly unique gaming experience for each user. <div