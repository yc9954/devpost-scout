---
slug: "fitops"
url: "https://devpost.com/software/fitops"
title: "FitOps"
hackathon: "Elastic Weekend with Code for Cause"
organization: "Code for Cause"
winner: true
words: 483
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# FitOps

> FitOps is a DevOps-oriented tool which democratizes your fitbit's data by capturing it in your personal elasticsearch store and cooks up fantastic grafana dashboards to provide insights around it!

[Devpost](https://devpost.com/software/fitops) · hackathon [[Elastic Weekend with Code for Cause]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** docker, elasticsearch, grafana, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fitops

## Body

Inspiration Fitbit is being used on a humongous scale and it takes away all your data and owns it. Technically, the company can choose to just stop providing you your data and your access to your fitness-oriented data which you captured over eons of time over your fitbit will be long own. Apart from that, you have to rely on the engineers of fitbit to be able to provide you "hopefully" good insights over your data via some bunch of dashboards. There is hardly any flexibility around tweaking the level and granularity of the insights which you'd possibly want to have, as those dashboards are majorly static. What it does FitOps targets towards accomplishing two goals: Democratization of your fitbit data - FitOps fetches your fitbit's data periodically and stores it under your roof making "you!" the owner and sole proprietar of your own data. The control and ownership of your data becomes completely yours! E2E control of the level and granularity of insights - FitOps cooks up a grafana dashboard at your disposal encompassing a fantastic set of panels to depict a holistic view of your fitbit-oriented health insights. And you can flexibly control the E2E mechanics of all those panels by tweaking the panels in any way you'd want ranging low-level to high-level granularity. How we built it We built it by making use of Docker a.k.a the beloved container tech. and Python. We are making use of the fantastic and well-intuitive API provided by Fitbit and capturing its data periodically. And speaking of how we are helping the end-users deploy and make use of FitOps with complete ease and just one-line of command, we bundled FitOps as a Docker image and are making it run over a Docker bridge alongside with two different containers of Elasticsearch and Grafana. Hence, wrapping the entire end2end setup of fitops to metric storage to metric observability under one roof of docker. Challenges we ran into Dealing with the convoluted initial setup of Fitbit dev account. Learning curve associated with Elasticsearch - CORS issues around Elasticsearch and resource constraints associated with it. Initially trying to deploy the setup over the host instead of dockerizing it wasted a lot of our time as well. Accomplishments that we're proud of The fitbit data is being successfully persisted over the user's host. The Grafana dashboard being cooked up is absolutely amazing and insightful and flexible to the user's control. What we learned Elasticsearch <3 Lucene Query Syntax Fitbit API interaction Improved knowledge around OAuth. What's next for FitOps Enhancing the setup by providing HA capabilities around it such as having a multiple-node Elasticsearch cluster. Deploying the entire over Kubernetes instead of relying on docker-compose for more mature management of the workloads due to the introduction of the container orchestration layer. Making FitOps more configurable - Like allowing the user to provide data retention period, period interval, etc. <div