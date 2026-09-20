---
slug: "drone-soundaware"
url: "https://devpost.com/software/drone-soundaware"
title: "Drone SoundAware"
hackathon: "AWS Lambda Hackathon"
organization: "Amazon"
winner: true
words: 403
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "user/government_staff"
  - "substrate/geospatial"
---

# Drone SoundAware

> An AWS Lambda based solution that allow drone operators to plan, assess and optimise their flight routes, reducing the noise impact on the community.

[Devpost](https://devpost.com/software/drone-soundaware) · hackathon [[AWS Lambda Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[transportation]]
**user** [[developer]] [[government_staff]]
**substrate** [[geospatial]]

**stack** amazon-cloudfront-cdn, amazon-dynamodb, apigateway, appsync, cdk, lambda, s3, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for drone soundaware

## Body

Drone SoundAware Application Inspiration We were promised a future where drones would deliver packages to our doorsteps, provide rapid medical aid, and reduce road traffic with fleets of zero-emission aircraft. Yet outside of limited trials, these visions remain largely unrealised. The challenge isn't technology or operator capability. My background is in UK Air Traffic Control and the UK aviation regulator, and while regulatory hurdles are significant, it's public acceptance that will ultimately enable large-scale drone operations. Noise is a major factor. Alongside privacy concerns, noise pollution is likely to be the biggest source of public resistance. So the question becomes: how do we get ahead of this, minimise community impact, and prove that drone operators are taking noise seriously? What it does Drone SoundAware is a tool that enables drone operators to plan, assess, and optimise their flights with a focus on reducing noise impact on local communities. How I built it From the ground up, assisted by Amazon Q Developer, the project has been built as a full-stack application using the Cloud Development Kit (CDK). The backend follows AWS best practices and is deployed using CDK. It uses a custom Lambda construct, integrates Powertools for structured logging, includes X-Ray tracing, and runs on Graviton for cost and performance efficiency. Challenges I ran into Partitioning data effectively in DynamoDB to support efficient, low-latency geospatial queries. This required several iterations of partitioning to get it right. Accomplishments that I'm proud of As part of the solution, a Lambda function is triggered by DynamoDB Streams when a new item is inserted, kicking off a route optimisation process based on a custom variant of the A* algorithm. I wanted to show that compute-intensive tasks can run efficiently at scale on Lambda. What I learned DynamoDB is a powerful and scalable option for geospatial data storage and real-time queries. By using multiple (and sparse) indexes, it is possible to have different resolution queries. Lambda is absolutely viable for compute-intensive workloads, especially when designed with event-driven architecture in mind. What's next for Drone SoundAware There are several options for continuing the development of Drone SoundAware: Enhance the routing algorithm and noise assessment methodology, including multi-threading and distributed Lambda execution. Integrate additional data sources such as commercial aircraft movements and restricted airspace information. Use of worldwide population data. Set up automated deployment pipelines. Improve authentication and login features (left out of hack-a-thon entry to streamline the demo experience). <div