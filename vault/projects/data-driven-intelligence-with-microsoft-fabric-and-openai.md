---
slug: "data-driven-intelligence-with-microsoft-fabric-and-openai"
url: "https://devpost.com/software/data-driven-intelligence-with-microsoft-fabric-and-openai"
title: "Data-Driven Intelligence with Microsoft Fabric and OpenAI"
hackathon: "Microsoft Fabric and AI Learning Hackathon"
organization: "Microsoft"
winner: true
words: 506
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/structured_db"
---

# Data-Driven Intelligence with Microsoft Fabric and OpenAI

> Our project integrates Azure OpenAI and Microsoft Fabric to streamline multi-source data ingestion, transformation, and AI-driven insights, empowering fast, data-driven sales and marketing decisions.

[Devpost](https://devpost.com/software/data-driven-intelligence-with-microsoft-fabric-and-openai) · hackathon [[Microsoft Fabric and AI Learning Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[structured_db]]

**stack** api, azure, azure-fabric, crm, erp, lakehouse, medallion, onelake, openai, powerbi, pyspark, python, sql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for data-driven intelligence with microsoft fabric and openai

## Body

Power BI final report high level architecture full semantic model semantic model relationships Inspiration Our inspiration came from the ongoing challenge that companies face in making sense of data scattered across various SaaS platforms. Sales directors often struggle to extract clear insights from an overload of charts across sales, marketing, and customer relationship data—a process that can take days or even weeks to interpret. We saw an opportunity to streamline data management and empower businesses with faster, more informed decision-making through the capabilities of Microsoft Fabric and Azure OpenAI. What It Does Our project centralises data from multiple sources (HubSpot CRM, Azure SQL Database, AWS S3) into a unified platform using Microsoft Fabric. Leveraging Azure OpenAI's large language models (LLMs), it generates actionable insights, such as sales trends, performance drivers, and strategic recommendations, all presented through an intuitive PowerBI report. How We Built It We started by ingesting data from HubSpot CRM, ERP data in Azure SQL, and social media reviews from AWS S3, leveraging core features such as ETL pipelines, mirroring and shortcuts. We implemented Medallion Architecture in Microsoft Fabric’s Lakehouse, organising data from raw to refined stages. We started with Bronze for raw ingestion, moved to Silver for cleaned, structured data, and finished with Gold for analytics-ready insights. Azure OpenAI was then integrated to analyse sales and review data, generating AI-driven insights that is visualised in PowerBI. Challenges We Ran Into One of our main challenges was optimising Azure OpenAI's responses to ensure clarity and relevance. We also worked to find the right balance between refining data through specific queries and relying on the language model to sift through large amounts of raw data to produce meaningful insights. Accomplishments That We're Proud Of We’re proud of delivering a robust, scalable solution that simplifies data analysis for business users. Automating the flow of data and insights, our project produces valuable business insights in minutes—tasks that traditionally would have taken days, saving time and improving strategic agility. We maximised the potential of Fabric's built-in features to reduce time to market. What We Learned Through this project, we gained valuable insights into Microsoft Fabric's platform, particularly its low-code/no-code tools for data ingestion, processing, and modelling. We also explored the benefits of the Medallion Architecture and PySpark Notebooks for efficient data processing. Additionally, we experienced the capability of Azure OpenAI to analyse raw data and generate meaningful insights, highlighting its potential for comparative analysis. What's Next for Data-Driven Intelligence with Microsoft Fabric and OpenAI Looking ahead, we plan to expand the platform to support a wider range of data sources and industries, such as manufacturing and operations, and to explore analysing streaming data providing near real-time insights. Our goal is to make the solution increasingly configurable, allowing users greater flexibility in tailoring queries to meet specific requirements. Testing with larger datasets will be crucial for assessing scalability and performance. Furthermore, we plan to explore newer language models, such as GPT o1, to extract deeper insights from data while potentially reducing the need for extensive upfront data manipulation. <div