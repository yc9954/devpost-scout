---
slug: "medxplanner"
url: "https://devpost.com/software/medxplanner"
title: "MedxPlanner"
hackathon: "Microsoft Teams App Development Challenge 2021"
organization: "Microsoft"
winner: true
words: 518
team_size: 6
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# MedxPlanner

> MedxPlanner is the ultimate Task Management tool for Healthcare workers. Tasks in the Electronic Medical Record (EMR) can linked to Planner and surfaced in Teams.

[Devpost](https://devpost.com/software/medxplanner) · hackathon [[Microsoft Teams App Development Challenge 2021]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[health_clinical]] [[labor_employment]] [[supply_logistics]]
**substrate** [[medical_record]] [[sensor_telemetry]] [[web_dom]]

**stack** activedirectory, angular.js, appservices, azure, fhir, functions, keyvault, mysql, node.js, planner, teams

## How they structured the write-up

- inspiration
- what it does
- how we built it
- try it out
- what's next for medxplanner

## Body

Logo MedxPlanner 1 MedxPlanner 2 MedxPlanner 3 Message Extension Inspiration Our healthcare customers needed a clinical task management system linked to the Electronic Medical Records (EMR) with a notification function to a mobile app. What it does MedxPlanner links Microsoft Teams and Planner to Electronic Medical Records via the FHIR API with the bi-directional interface using the Graph API How we built it Technologies used Teams Toolkit for Visual Studio Code. Node.js Bot Framework for bots and messaging extensions. Python 3 for running Cron job. Angular Framework for building front-end of tabs. HTML/SCSS for designing. Azure App Services to host the backend API services. Features MedxPlanner hold Our application is fully based on MS Teams . We have used several services of Microsoft to build the application. For authentication we have used AAD Authentication Flow AAD . This gives us the power to authenticate users and have secure access to web API's using tokens from the MS Identity platform. Our application mainly holds a Configurational Tab (channel tab) and most interestingly Message Extension . The MedxPlanner is a fully Angular project which is then embedded into the MS Teams configurational tab using manifest.json In this we added some personalized configuration: ... "configurableTabs": [{ "configurationUrl": "https://yourteamsapp.ngrok.io/configure", "canUpdateConfiguration": true, "scopes": [ "team" ] }], ... The most fascinating thing about our application is Adding a task to our Planner using message extension. We have built this in JavaScrip are using TeamsActivityHandler from botbuilder and for authentication, we have silent authentication. Here we are using two types of extensions: Search Commands and Action Commands . The action command help to generate add task form using an async function handleTeamsMessagingExtensionFetchTask which pop-up an Adaptive Card and, uses handleTeamsMessagingExtensionSubmitAction async function to submit the task. Search commands enable to see the task created and also, allow users to filter task based on task and notes. It is using an async function handleTeamsMessagingExtensionQuery to fetch the task and o365ConnectorCard to display. We are using Microsoft Azure for the deployment of services: Azure App Services , is used to host the application and allow us to build API's and makes infrastructure managing super simple. Azure Key Vault , helps us to enhance data protection and compliance. Along with that, it safeguards cryptographic keys and other secrets used by cloud app and services. Azure Monitoring , helps us to aggregates and stores telemetry in a log data store that's optimized for cost and performance. AAD , popularly known as Azure Active Directory, solves the issue of sign-in and access resources. It is basically an identity and access management service. Try it out For a complete setup guide, please email niall.rafferty@medxnote.com to request the getting started documentation. What's next for MedxPlanner The next thing on which our team has already started working on is Message Action This collaboration is more than messaging, it provides the user to take action right from ellipsis on the message in the chat, it uses message as a command in the manifest file. Here we are trying to fetch the information from the card and create a task based on that. <div