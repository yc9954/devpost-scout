---
slug: "triple-a-s-project"
url: "https://devpost.com/software/triple-a-s-project"
title: "Quadruple Ace Flight Analysis"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 326
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/web_dom"
---

# Quadruple Ace Flight Analysis

> So how many planes did COVID ground?

[Devpost](https://devpost.com/software/triple-a-s-project) · hackathon [[Azure AI Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[web_dom]]

**stack** azure-automl, azureblobstorage, azuremachinelearning, azuremachinelearningstudio, matplotlib, python, rapidapi, react, visual-crossing-weather

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for quadruple ace project

## Body

Inspiration We love travel but have been grounded at home because of COVID. We were interested in how many US flights were also grounded as a result of the global pandemic. What it does We built an Azure-hosted web app that explores how COVID affected the number of flights leaving major airports in the US. It also estimates the number of flights impacted during the pandemic for Hartsfield Jackson International Airport in Atlanta, GA. Link to our web app: tripleacesstatic.z13.web.core.windows.net How we built it We used the Azure Web App service to host our web app. The Azure-hosted Web App was built using React Web, primarily using Reactstrap to use the bootstrap components to build the interface. The HTML file was stored it in Azure blob store. We created a static web app to host. All code is pushed into the repo and the app was built from the main branch React file. We used the Azure Python SDK and Azure AutoML Forecasting functionality to access data and build our models. For the visualizations, we used Pandas for data manipulation, Matplotlib for plotting, Seaborn for the visualizations color palette, and the Python SDK to upload the plots to blob storage. Challenges we ran into We had trouble figuring out how to share a workspace. For those of us using the Anaconda Python platform, we had trouble connecting to the Python SDK. We migrated to Visual Studio Code instead. Accomplishments that we're proud of Our web app was built very quickly! And we thought it was interesting to know how many flights were cancelled due to the pandemic. What we learned We learned about the Azure SDK for Python, and about the data storage options in Azure. We used Azure Workspaces and Datasets to share files and ensure that we were working off the same files. What's next for Quadruple Ace Project Cruise ship analysis? Or maybe we'll finally be able to take a flight somewhere! <div