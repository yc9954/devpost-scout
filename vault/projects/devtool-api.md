---
slug: "devtool-api"
url: "https://devpost.com/software/devtool-api"
title: "DevTool API"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 414
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# DevTool API

> Make DevOps's lives better!

[Devpost](https://devpost.com/software/devtool-api) · hackathon [[Cloud Native Hackathon]]

## Facets

**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** api, civo, datree, devtron, docker, kubernetes, python, sqlite, twilio

## How they structured the write-up

- inspiration
- what it does
- usage of the project
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for devtool api
- workflow of the project

## Body

Inspiration Developers go through a lot of problems and suffering for deployment Kubernetes manifest files into production and so we thought why no make an API service to make the work for the developers easier and also be able to get to know about the misconfigurations in the manifest files and be alerted to them via notification system. What it does Using Kubernetes production best policies to run the k8s manifest files through Datree.io to prevent Kubernetes misconfigurations from ever reaching production. Usage of the project This simplifies the job of the DevOps developers, who are working with misconfiguration and security of the k8s. And it can be used as a JSON datasource in Grafana. Inside the API we can populate the info of the datasources. There we can use the Datree CLI to analyze the k8s manifests and POST the report into the API to see the result in Grafana natively. How we built it Clusters are created using Kubernetes in Civo DevOps(Configurations, etc) Flask API integration Python runs Datree commands and POST request to API Metrics and logs of the configurations are checked using Grafana (Devtron) Challenges we ran into Had to get the fail.yaml file from the customized policies of the Datree using our API POST request argument. Integration of the Kubernetes Python Client with the local k8s clusters. Docker Image Build issue regarding the predefined ports. Accomplishments that we're proud of Being able to create custom policies to PR into the Datree.io . Build the metrics into Devtron using Grafana. What we learned Devtron being a good devops tool which can boost the development process. Also it contains not only CI/CD stuff but also allow to understand the performance of deployed services and make changes in Kubernetes cluster using Devtron UI. Datree is a tool which can help in analyzing Kubernetes manifests, not only before applying it but also for existing manifests as well. In Datree, you can use custom policy which allow you to cover any possible use-cases. Civo helped us to spin-up the k8s clusters faster and had predictable prices and we were able to spin-up the main and all needed service which we need and make our development make it all centralized in development instances for all the members. What's next for DevTool API Alert the developers to the misconfigurations that have happened against the custom policy through Twilio alert. Increase more options for Datree usage. More monitoring system. Security system enhancement. Workflow of the project <div