---
slug: "ai-wonder-girls-disaster-response"
url: "https://devpost.com/software/ai-wonder-girls-disaster-response"
title: "AI Wonder girls: Disaster Response Assistant"
hackathon: "AWS Disaster Response Hackathon"
organization: "Amazon"
winner: true
words: 774
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# AI Wonder girls: Disaster Response Assistant

> And all women team doing AI for social good, one project at a time

[Devpost](https://devpost.com/software/ai-wonder-girls-disaster-response) · hackathon [[AWS Disaster Response Hackathon]]

## Facets

**domain** [[disaster_emergency]] [[finance_payments]] [[labor_employment]] [[supply_logistics]]
**substrate** [[structured_db]] [[web_dom]]
  <sub>weak: financial_record</sub>

**stack** python, sagemaker, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- the pillars of our project
- what's next for ai wonder girls disaster response

## Body

GIF An overview of the Earthquake Disaster Assistance Project Meet the team Our Problem Statement Our data sources Our Pipeline Strong points Analytics Module Disaster Relief Package Module Chatbot assistant Module Inspiration This projects addresses the topic of Disaster Response focusing on the case study of Earthquake response. When disaster strikes, both humanitarian organizations and local communities need to coordinate efforts to bring quick help to affected populations. World Health organization(WHO) Statistics shows that worldwide between 1998-2017, 125 million people were affected by earthquakes. From those, many are left in emergency situations or unfortunately perish due to the lack of assistance on time. In this project we introduce an AI for Disaster Assistant as a technology that aims to support humanitarian workers and civilians to achieve faster response in earthquake emergencies. Our all women and multiple times winner team - the AI Wonder Girls - brings to you another AI assist that helps users to make data-driven decisions based on reliable data sources. Our solution has the potential to help multiple groups of people dealing with emergencies and can be expended to other disaster types. What it does Our AI assistant is an application that combines multiple advanced AI techniques to help user during an earthquake emergency. Using machine learning models, our assistant is trained to estimates the number of affected people in an earthquake event, based on the data of multiple official databases (USGS.gov, EMDAT and World Bank indicators). The application utilizes WHO and disaster response guidelines combined with the number of affected estimations to build a package of food and non-food items necessary to supply the affected populations during the emergency. Our application also aims to support civilians and local authorities during earthquakes. By providing analytics on the topic, a newspapers news search about earthquakes and an integrated chatbot, users are able to receive reliable information on first aid and standard protocol for emergencies. We believe that our application can significantly improve the efficiency of humanitarian logistics operations and ultimately save lives. How we built it The AI for Disaster Assistant is built using a Streamlit front end web end application integrated to the AWS Sagemaker Lab via a continuous integration deployment, where different AI applications are trained. Details of implementation of each feature in the application are: Analytics Module: contains historical information summarized in visualizations to help the users to understand the global context of earthquake catastrophes. This feature is aimed to bring value to local authorities and support a data-driven decision making on mitigating actions. - Relief Package Module: implementation of state of the art machine learning models on a multiple context dataset, which connects earthquake, disaster management and socioeconomic contexts. Chatbot Module: implementation of a chatbot which assists users by answering questions about earthquakes and first aid practices. Earthquake News Module: scrapes articles about earthquakes from newspapers and Twitter and displays their information and URLs. Challenges we ran into Finding reliable data sources Identifying Open Source data Working across worldwide time-zones Identifying relevant variables to our model due to the lack of domain knowledge on seismology Accomplishments that we're proud of We are proud that in a short period of 6 weeks our all women team : Collected, cleaned and merged data from multiple official datasets Built a data-centric pipeline that encompasses advanced AI techniques Deployed the complete pipeline in a prototype application that can be later expanded to other disasters What we learned This project was a great opportunity to learn more about cloud and deployment, by building models on Sagemaker Lab and using its GitHub integration to a streamlit deployment. As always, we were glad to keep learning about team spirit and taking the opportunity to learn more about advanced techniques and the fascinating knowledge domain of disaster response. The pillars of our project Innovation: The application applies state of the art AI techniques to address a logistics problem from a data centric approach. Impact: The applications has two functionalities which helps engaging both the general public and disaster management professionals. And this approach is applicable to other disasters. Implementability: The UI application is built using Python, Streamlit and Opensource libraries, being a framework that can be maintained and expanded as a broad open source project, uniting the AI and Disaster Management communities. What's next for AI Wonder Girls Disaster Response This project is planned to be continued as an Open Source initiative in which both humanitarian agents and technical community (in the field of AI/Data Science/Software Development) can collaborate. Humanitarian workers can contribute by sharing data sources which can improve the AI models, while technical people can help with implementing new functionalities to the application. <div