---
slug: "loan-default-prediction-t1ahlj"
url: "https://devpost.com/software/loan-default-prediction-t1ahlj"
title: "Loan Default Prediction"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 292
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "user/general_public"
---

# Loan Default Prediction

> This project entails predicting potential loan default clients for financial institutions.

[Devpost](https://devpost.com/software/loan-default-prediction-t1ahlj) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[finance_payments]]
**user** [[general_public]]
  <sub>weak: sensor_telemetry</sub>

**stack** automl, azure, hyperdrive, mlops, onnx, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for loan default prediction

## Body

Enabling logging Application Insight Project workflow Comparing automl and hyperdrive model Deployment state Completed AutoML run Model deployment Details necessary for endpoint interaction AutoML run metrics Endpoint output Best hyperdrive model Endpoint response Deleting service after use Completed hyperdrive run Sample data to test endoint ONNX workflow Inspiration I have a strong background in banking and finance by having a degree in finance and working in the bank in the last couple of years. Over the years, I have also developed a passion in machine learning and AI. This here is my inspiration, finding myself in a field I have grown to love, combining knowledge of lending systems and this new machine learning passion. This project is about building intelligent tools that solve real-world challenges in financial institutions, one major one is loan default prediction. What it does The project identifies clients that are likely to default a loan credit. How we built it Project was built by training machine learning models on Azure ecosystem; leveraging tools such as automl, hyperparemeter tuning with hyperdrive, MLOps with pipelines, etc. Challenges we ran into Data privacy. Letting out clients information for the project was a challenge. A little simulation/editing of data was done to prevent valuable clients information from being released to the public. Accomplishments that we're proud of Project hit an accuracy of about 85% with AutoML. Model was deployed and consumed by exposing its RESTful endpoint API. Model was also converted to ONNX format, so it can be used on android and iOS devices What we learned There are so many resources on Azure to applicable to machine learning tasks. What's next for Loan Default Prediction Push it to the company's executive and see if it can be implemented in operations. <div