---
slug: "ms-hackathon"
url: "https://devpost.com/software/ms-hackathon"
title: "LinkedIn Job Market Analysis in Sweden"
hackathon: "Microsoft Fabric and AI Learning Hackathon"
organization: "Microsoft"
winner: true
words: 621
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "domain/supply_logistics"
---

# LinkedIn Job Market Analysis in Sweden

> Struggling to find a job in Sweden? Want to accelerate your career path? Gain insights into the job market by analyzing LinkedIn posts to uncover key trends with the help of AI..

[Devpost](https://devpost.com/software/ms-hackathon) · hackathon [[Microsoft Fabric and AI Learning Hackathon]]

## Facets

**domain** [[labor_employment]] [[supply_logistics]]

**stack** elt, etl, https://api.scb.se/ov0104/v1/doris/sv/ssd/start/be/be0101/be0101a/befolkmanad, https://www.linkedin.com/jobs-guest/jobs/api/jobposting/{job-id}, https://www.linkedin.com/jobs-guest/jobs/api/seemorejobpostings/, json, openai, pyspark, python, requests, sparksql, sql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for linkedin jobs analysis

## Body

Architecture Inspiration This project is designed to assist individuals who are struggling to find jobs in Sweden by providing insights into the job market. By analyzing job postings, it reveals which tools, skills, and requirements are most in demand by employers, which is particularly beneficial for those who may not have a strong understanding of the market, such as new graduates or career changers. Additionally, the project offers city-level insights, which can be especially useful for newcomers or those considering relocating to Sweden. It provides a clearer picture of which cities have the most job opportunities, making it easier for job seekers to align their job search with current market trends. What it does This project is an in-depth analysis designed to derive insights from LinkedIn job posts within Sweden on an hourly basis. It utilizes a robust architecture integrating various technologies and services to capture, store, process, and analyze jobs posted on LinkedIn on an hourly basis. Additionally, it incorporates population data at the city level to provide a comprehensive view of the Swedish job market dynamics. How we built it The project leverages the medallion architecture using Microsoft Fabric service. It utilizes A fabric workspaces with two lakehouses—bronze and silver—and two main data pipelines. The Job Data Hourly pipeline extracts recent job posts from Sweden on an hourly basis, along with each company's follower count. This raw data is stored in the bronze data lakehouse, then cleaned, processed, and transferred to the silver data lakehouse. Using Azure OpenAI, we analyze each job post to identify tools, requirements, offers, and work types, which Power BI then uses for reporting. The Population Data Monthly pipeline retrieves monthly population data from SCB, including demographic details by city. This data is stored, cleaned, and refined in the data lakehouses and integrated into Power BI reports to provide city-level insights. Challenges we ran into Extracting information from LinkedIn proved more complex than we initially anticipated. Gathering accurate data on job posts and company follower counts required overcoming technical and logistical challenges, as LinkedIn data is not always easily accessible or structured for extraction. Additionally, ensuring the data was consistently reliable and up-to-date added another layer of complexity to the process. Accomplishments That We're Proud Of We successfully built a robust data pipeline capable of handling large volumes of data. We’re also proud of the detailed, interactive Power BI reports, which offer valuable insights to job seekers and stakeholders alike. We've familiarized ourselves with Microsoft Fabric with most of its different components. We've also got to work with data engineering principles hand on which is beneficial for our carriers. What we learned Throughout this project, we learned the importance of data accuracy and the challenges associated with using APIs and data integration. We gained experience in using Azure OpenAI for natural language processing and improved our skills in building and managing data pipelines. Used different dialect of spark and got them to play in the same notebooks. Additionally, we learned how to create effective visualizations in Power BI to communicate complex data insights clearly. What's next for Linkedin jobs analysis The next step is to provide job seekers with an advanced tool that finds job posts aligning with their experience and qualifications. We want to be able to integrate with Linkedin using it is newer API version so we can scale the solution into bigger markets and countries. This tool could include an advanced search feature allowing users to upload their CV, which would then be analyzed to match them with relevant job postings. The tool would provide a list of job opportunities that align closely with the user’s skills and experience, along with a probability score indicating the likelihood of securing each position. <div