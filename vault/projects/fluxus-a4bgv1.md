---
slug: "fluxus-a4bgv1"
url: "https://devpost.com/software/fluxus-a4bgv1"
title: "Fluxus"
hackathon: "HackMIT 2023"
organization: "HackMIT"
winner: true
words: 1126
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/scientific_research"
  - "user/developer"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Fluxus

> Natural Language-Managed Medical Data Workspace

[Devpost](https://devpost.com/software/fluxus-a4bgv1) · hackathon [[HackMIT 2023]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[health_clinical]] [[labor_employment]] [[scientific_research]]
**user** [[developer]] [[patient_family]] [[researcher]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** ai, firebase, flask, gpt, integratedml, intersystems, llm, postresql, python, rabbitmq, sqlalchemy, vue.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fluxus

## Body

Product Logo Device Frames Main Dashboard of the App The Application Design Inspiration Our spark to tackle this project was ignited by a teammate's immersive internship at a prestigious cardiovascular research society, where they served as a dedicated data engineer. Their firsthand encounters with the intricacies of healthcare data management and the pressing need for innovative solutions led us to the product we present to you here. Additionally, our team members drew motivation from a collective passion for pushing the boundaries of generative AI and natural language processing. As technology enthusiasts, we were collectively driven to harness the power of AI to revolutionize the healthcare sector, ensuring that our work would have a lasting impact on improving patient care and research. With these varied sources of inspiration fueling our project, we embarked on a mission to develop a cutting-edge application that seamlessly integrates AI and healthcare data, ultimately paving the way for advancements in data analysis and processing with generative AI in the healthcare sector. What it does Fluxus is an end to end workspace for data processing and analytics for healthcare workers. We leverage LLMs to translate text to SQL. The model is preprocessed to specifically handle Intersystems IRIS SQL syntax. We chose Intersystems as our database for storing electronic health records (EHRs) because this enabled us to leverage their integratedML queries. Not only can healthcare workers generate fully functional SQL queries for their datasets with simple text prompts, they now can perform instantaneous predictive analysis on datasets with no effort. The power of AI is incredible isn't it. For example, a user can simply type in "Calculate the average BMI for children and youth from the Body Measures table." and our app will output "SELECT AVG(BMXBMI) FROM P_BMX WHERE BMDSTATS = '1';" and you can simply run it on the built in intersystems database. With Intersystems IntegratedML, with the simple input of "create a model named DemographicsPrediction to predict the language of ACASI Interview based on age and marital status from the Demographics table.", our app will output "CREATE MODEL DemographicsPrediction PREDICTING (AIALANGA) FROM P_DEMO TRAIN MODEL DemographicsPrediction VALIDATE MODEL DemographicsPrediction FROM P_DEMO SELECT * FROM INFORMATION_SCHEMA.ML_VALIDATION_METRICS;" to instantly create train and validate an ML model that you can perform predictive analysis on with integratedML's "PREDICT" command. It's THAT simple! Researchers and medical professionals working with big data now don't need to worry about the intricacies of SQL syntax, the obscurity of healthcare record formatting - column names and table names that do not give much information, and the need to manually dive into large datasets to find what they're looking for. With simple text prompts data processing becomes a no effort task, and predictive modelling with ML models becomes equally as effortless. See how tables come together without having to browse through large datasets with our DAG visualizations of connected tables/schemas. How we built it Our project incorporated a multitude of components that went into the development. It was both overwhelming, but also satisfying seeing so many parts come together. Frontend: The frontend was developed in Vue.js and utilized many modern day component libraries to give off a friendly UI. We also incorporated a visualization tool using third party graph libraries to draw directed acyclic graph (DAG) workflows between tables, showing the connection from one table to another that has been developed after querying the original table. To show this workflow in real time, we implemented a SQL parser API (node-sql-parser) to get a list of source tables used in the LLM generated query and used the DAGs to visually represent the list of source tables in connection to the newly modified/created table. Backend: We used Flask for the backend of our web service, handling multiple API endpoints from our data sources and LLM/prompt engineering functionality. Intersystems: We connected an IRIS intersystems database to our application and loaded it with a load of healthcare data leveraging intersystems libraries for connectors with Python. LLMs: We originally started looking into OpenAI's codex models and their integration, but ultimately worked with GPT-3.5 turbo which made it easy to fine-tune our data (to a certain degree) so our LLM could detect prompts and generate syntactically accurate queries with a high degree of accuracy. We wrapped the LLM and preprocessing of prompt engineering features as an API endpoint to integrate with our backend. Challenges we ran into LLMs are not as magical as they look. There was nothing for us to train the kind of datasets that are used in healthcare. We had to manually push entire database schemas for our LLM to recognize and to attempt to fine-tune on in order to get queries that were accurate. This was intensive manual labour and a lot of frustrating failures with trying to fine-tune on both current and legacy LLM models provided by OpenAI. Ultimately we came to a promising result that delivered a solid degree of accuracy with some fine-tuning. Integrating everything together - putting together countless API endpoints (honestly felt like writing production code at a certain point), hosting to our frontend, wrapping the LLM as an API endpoint. Ultimately there's definitely pain points that still need to be addressed, and we plan to make this a long term project that will help us identify bottlenecks that we didn't have time to address within these 24 hours, while simultaneously expanding on our application. Accomplishments that we're proud of We were all aware of how much we aimed to get done in a mere span of 24 hours. It seemed near impossible. But we were all on a mission, and had the drive to bring a whole new experience to data analytics and processing to the healthcare industry by leveraging the incredible power of generative AI. The satisfaction of seeing our LLM work, trying to fine-tune manually configured data hundreds of lines long and having it accurately give us queries for IRIS including integratedML queries, the frontend come to life, the countless API endpoints work and the integration of all our services for an application with high levels of functionality. Our team came together from different parts of the globe for this hackathon, but we were warriors that instantly clicked as a team and made the most of these past 24 hours by powered through day and night to deliver this product. What we learned Just how insane AI honestly is. A lot about SQL syntax, working with Intersystems, the highs and lows of generative AI, about all there is to know about current natural language to SQL processes leveraging generative AI thanks to like 5+ research papers. What's next for Fluxus Develop an admin platform so users can put in their own datasets Fine-tune the LLM for larger schemas and more prompts buying a hard drive <div