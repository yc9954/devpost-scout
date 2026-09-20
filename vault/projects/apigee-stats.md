---
slug: "apigee-stats"
url: "https://devpost.com/software/apigee-stats"
title: "Apigee stats"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 364
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Apigee stats

> Apigee traffic gives us useful information about the behavior of APIs and having a tool to visualice/monitor would be a powerful tool for product owners and developers let's have this in one click

[Devpost](https://devpost.com/software/apigee-stats) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[transportation]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** chartsjs, javascript, mock-servers, postman, postmanapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- we want to resolve this:
- accomplishments that we're proud of
- what we learned
- what's next for apigee stats

## Body

Inspiration Postman is a powerful collaboration platform for API development, and considering that ALL companies work with Web Services building API's to support their business, we see postman as a key tool to retrieve and understand the data. Access metrics collected by Apigee Edge that measure API consumption and performance , faster, metrics chart in real time, notifications in case of error and store your metrics in your own database. What it does Transform Apigee Analytics API responses to a Chart, that summarize the data by Product, Proxy, App, etc, additional post errors and statistics to a Postman API (Mock Server) to emulate saving the error data and traffic data. How we built it Built everything in Postman Platform, using the following: Collections API - OpenAPI 3.0 Postman Integrations - Microsoft Teams and Github Monitors Visualizations (javascript Chart-js, Material) Mock server Challenges we ran into "Data older than six months from the current date is not accessible by default. If you want to access data older than six months, contact Apigee Support." ( https://docs.apigee.com/api-platform/reference/policies/statistics-collector-policy#accessing-statistics ) "Note: Data delay interval After API calls are made to proxies, it may take up to 10 minutes for the data to appear in dashboards, custom reports, and management API calls." ( https://docs.apigee.com/api-platform/analytics/use-analytics-api-measure-api-program-performance ) We want to resolve this: We want to access to older data anytime. We want to access faster. We want notification in case of error. Accomplishments that we're proud of Successfully implemented Apigee stats on top of Postman Platform We got it !!! We created and API in Postman(StatsApi) to save metrics in our Mock server (emulate save metrics in database). Now you can access faster to your own Database and get stats that you need anytime. Plus: Analyze your metrics in real time: Charts Js and Material Components. Notifications: you will recibe a notifications in teams if there are an error in (is Error or Policy Error) What we learned Postman builtin integration with different tools like Microsoft Teams, Slack, Pager duty. Implemented Postman Monitors for our APIs Build API (Open API) and Mock Servers What's next for Apigee stats Build the framework, to easily integrate with postman Visualization, Monitors and Postman Integrations <div