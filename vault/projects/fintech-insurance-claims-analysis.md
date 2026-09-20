---
slug: "fintech-insurance-claims-analysis"
url: "https://devpost.com/software/fintech-insurance-claims-analysis"
title: "Claims ML based Subrogation Recovery Prediction"
hackathon: "AWS Data Exchange Challenge"
organization: "Amazon"
winner: true
words: 368
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Claims ML based Subrogation Recovery Prediction

> Get little closer to the reality !!!

[Devpost](https://devpost.com/software/fintech-insurance-claims-analysis) · hackathon [[AWS Data Exchange Challenge]]

## Facets

**domain** [[finance_payments]] [[transportation]]
**user** [[general_public]]
**substrate** [[geospatial]] [[structured_db]]

**stack** amazon-web-services, api, natural-language-processing, python, sagemaker, semantic-engines-semantic

## How they structured the write-up

- inspiration :
- what it does :
- how i built it :
- challenges i ran into :
- accomplishments that i'm proud of :
- what i learned :
- what's next for claims ml based subrogation recovery prediction :

## Body

Inspiration : Post Covid, impact of economic slowdown on auto insurance sector and particularly on uninsured claimants. Below are the key findings of the study done from USA. 32+ million uninsured vehicles on the road 35x spike in subrogation workload 15% missed opportunities of subrogation (deteriorating) 32% of recoverable paid claims are lost What it does : With the help of AWS data exchange, we augmented our claims data to uncover important aspects of the uninsured or underinsured claimant, and thus used those variables such as income levels, weather conditions and sales preference to build a machine learning model to understand his or her likelihood to pay the subrogation How I built it : We researched and finalized the below datasets to augment our solution Claims First Party Data (Synthetic) Epsilon – Insurance Consumer Data Insights (AWS Data Exchange) Enigma – Individual Tax by Zip Code (AWS Data Exchange) Weather Source – OnPoint Historical Weather Data ( AWS Data Exchange) Phase two – Implementation of the Solution Design data pipelines to feed models Perform ML experiments to train models Develop the UI & Visualizations Integrate & Deploy the model. Challenges I ran into : Bias in the data set of claims. Performance issue while processing and integration of datasets with size > 300 MB. Hosting of the application using AWS LightSail Accomplishments that I'm proud of : Completed this hackathon project with demanding timelines along with full time job. Achieved high accuracy of >98% and recall > 94% for model. Integration of model and UI screens built in Python flask through Amazon Light Sail, we never done that before. What I learned : Understand various datasets AWS data exchange offers and its potential use cases. Although not optimal, however learnt different AWS components features for end-to-end logical use case. What's next for Claims ML based Subrogation Recovery Prediction : We want to integrate various data sources and research possible ways to improve the model to the real life scenarios.\ Some of them at the top of our mind are Social Media posts (based on collision date time, location and vehicle description). Google Street View (based on collison date time & location) Digital Identity Mapping for the Claimant <div