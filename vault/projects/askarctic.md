---
slug: "askarctic"
url: "https://devpost.com/software/askarctic"
title: "AskBI"
hackathon: "THE FUTURE OF AI IS OPEN"
organization: "Snowflake"
winner: true
words: 956
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/retrieval_grounding"
  - "domain/supply_logistics"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# AskBI

> AskBI allows users to get actionable insights faster by combining the power of GenAI and Metadata, to use existing reports & dashboards and data warehouse effectively & removing knowledge barriers.

[Devpost](https://devpost.com/software/askarctic) · hackathon [[THE FUTURE OF AI IS OPEN]]

## Facets

**mechanism** [[cross_origin_web]] [[retrieval_grounding]]
**domain** [[supply_logistics]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** amazon-web-services, arctic, openai, pinecone, python, snowflake, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for askbi

## Body

Landing page Sample questions Results overview Interactive dashboard results SQL query generation and dataframe Visual report Narrative insights Follow-up question Inspiration When enterprises build data platforms along with business intelligence one of the primary considerations is to improve adoption and enable business users to consume insights and take decisions. However, there are many challenges that must be overcome before this becomes a reality. One such challenge is the sheer number of BI reports that are generated in an organization. Different stakeholders and different teams have their own set of reports. Each user may not be even aware of all the reports that are available. In the world of generative AI there are multiple techniques through which we can bridge the gap between what the user knows about a system and what is available in the system. At Neoware, we built an application that helps the business users get the insights they are looking for. We have named this application “AskBI”. What it does The application has a conversational interface where the user can ask a question. The application understands the user’s question, compares it with the list of available reports and dashboards within the BI system, and brings back the most appropriate match that helps answer the user’s question. It also generates a query based on its understanding of the question, runs the query against the underlying data warehouse, and displays the results for the user. The application creates a visual representation of the result, and looks for trends, anomalies, correlations and summarizes the narrative for the user. How we built it We chose Streamlit for AskBI as it was quick and easy to build an application in Streamlit and it provided all the necessary functionalities. The metadata from the BI reports and Snowflake tables is embedded using OpenAI embeddings model into a vector database, to enable accurate mapping of user queries to appropriate BI reports and dashboards. We start by embedding the user query. The query embedding is compared with the embeddings of existing dashboard reports to identify and display the most relevant match to help answer the user's question. It also generates a query using Snowflake Arctic, executes this query against the data in Snowflake, and presents the results to the user. The resulting data is displayed to the user. Beyond presenting interactive dashboards and detailed information from the SQL query, we employ the Arctic model to generate narratives and insights based on the retrieved data, significantly enhancing the user experience. The application also creates a supporting intuitive visual using Arctic to generate the code required to generate the visual. Challenges we ran into A few challenges that we ran into were reducing the hallucination of the LLM model. This we overcame by supplying the model with appropriate metadata. Additionally, we faced challenges in terms of retaining context and detecting a change in context, primarily while generating queries. This was overcome by finetuning the prompts. Accomplishments that we're proud of In customer implementations of AskBI, we have observed that it enhances the understanding of analytical systems within these organizations, boosts the use of business intelligence by business users, and fosters a culture of data-driven decision-making. The additional benefit of this co-pilot is the increased adoption of existing BI assets without having to excessively focus on training on specific technologies. In fact, some clients view it as a "GenAI Junior Data Analyst," which is like adding a youthful, sharp team member to their operations. This system increases IT’s understanding of the questions on the minds of business users (what they are looking to get answered from the data warehouse and BI systems) What we learned We have built this application using multiple LLMs to generate content. We have learnt the strengths and behaviors of the different language models in the function of query generation. Find below some insights into the accuracy of these LLMs Complexity Level Gemini OpenAI Anthropic Snowflake Arctic* Category 1 63.64 86.36 86.36 100.00 Category 2 71.43 92.86 92.86 60.00 Category 3 71.43 85.71 71.43 75.00 Category 4 61.54 76.92 92.31 75.00 Category Definitions : Category 1 - Require selecting specific columns, filtering rows based on certain criteria, or aggregating data using simple functions like COUNT, SUM, AVG, etc. Category 2 - Queries that require joining two tables together based on a common key or condition. Join operations such as INNER JOIN, LEFT JOIN, RIGHT JOIN, or FULL JOIN may be used to combine data from multiple tables. Category 3 - Queries involve performing mathematical calculations on existing data within a table or across multiple tables and creating a new column based on the result of these calculations. Category 4 - Queries that require joining three or more tables together. The queries may involve multiple levels of joins, subqueries etc. *The other LLMs have undergone rigorous testing on data from different domains, whereas for snowflake arctic, the accuracy numbers presented here are based on the current data that we have used in the demonstration. What's next for AskBI There is a robust roadmap for AskBI as a solution. The key features planned are: Expansion of the application into a mobile version equipped with audio support. Support for textual data like documents, contracts, manuals. Sharing/exporting results with different platforms. Ability to view past conversations. Clearing the context. Importing custom data into the session. Automated flow to update Tableau ToC with Iframe scripts. Expanded support for Qlik and Power BI. Ability to generate Tableau, Qlik and Power BI visuals dynamically A visual generation function capable of processing entire query results to create visuals, with the aim of mitigating hallucinations induced by LLMs. Function for identifying seasonal trends, anomalies, correlations, etc from the input data for generating insights. Formulating tailored prompts for open-source models. <div