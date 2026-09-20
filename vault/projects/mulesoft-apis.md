---
slug: "mulesoft-apis"
url: "https://devpost.com/software/mulesoft-apis"
title: "Mulesoft APIs"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 199
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/sensor_telemetry"
---

# Mulesoft APIs

> Make mule the max dance to your tune with this API collection

[Devpost](https://devpost.com/software/mulesoft-apis) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[sensor_telemetry]]

**stack** collection, mulesoft, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for mulesoft apis

## Body

Functional FlowChart Inspiration We are doing a lot of routine tasks like doing health check, collecting metrics, managing and monitoring mule apps through Anypoint platform which is taking some time to do particularly when we need to do bulk restarts or updates. With the help of cloudhub api we can do this tasks in single API call. What it does Get the list of applications in your environment along with its runtime version and all associated details. Do bulk action for mule apps like UPDATE,START,STOP,RESTART and DELETE. Deploy application Get the log file for application List Alerts related to the application Get Alert History Get mule versions of your environment. List domain static ip's Get domain autoscalepolicies. Retrieve notifications List schedules for application Get users current permission Get Vcore usage How we built it We built a postman api collection with the help of this cloudhub api documentation . What's next for Mulesoft APIs Eventhough We develop this postman collection the consumption and feedback is the most important part to improve the API and customise it our needs. We can build similar collections to MQ API to leverage the rest api to do bulk retrieval of queue stats. <div