---
slug: "graph-map"
url: "https://devpost.com/software/graph-map"
title: "graphMap."
hackathon: "AWS Data Exchange Challenge"
organization: "Amazon"
winner: true
words: 572
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# graphMap.

> Analyze relations between multiple datasets with geo-location and network science

[Devpost](https://devpost.com/software/graph-map) · hackathon [[AWS Data Exchange Challenge]]

## Facets

**domain** [[health_clinical]] [[scientific_research]]
**substrate** [[genomic_bio]] [[geospatial]] [[structured_db]]

**stack** amazon-web-services, aws-athena, aws-dataexchange, aws-gateway, aws-lambda, networkx, node.js, python, vue.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for graphmap.?

## Body

Inspiration Network Science lets us understand “the whole picture” between related data points thanks to the structural properties of a graph dataset. Some graph dataset examples are relations on social networks, relations between proteins, and relations on words co-occurrence in multiple texts. In past years, Network Science brought advances in drug discovery and social science - from molecules interactions prediction to humans interaction analyses. With GraphMap, I would like to bring Network Science to the regular Data Analysis pipeline to reach insights, based on datapoints relationships. What it does With graphMap, you can use network science and geolocation visualization to analyze data points relations on territory. Insights are extracted from the plain text so the datasets don’t necessarily have to be of the same type. The Network Science calculations triggered on every GraphMap query, can be used to discover insights such as: Which niche markets are satisfied within a 100 km radius?, How many beds do hospitals have in this area? How far is this property from other high valuable Real Estate properties? What are the ingredients demand in the area? between others. An interactive Graph visualization, 3D maps, and word clouds are provided to understand insights. How I built it On-demand NetworkX analyses are performed taking advantage of AWS Athena, AWS S3, AWS API Gateway, and AWS Lambda services; NetworkX is a Python package for Network Science Research. The frontend is powered by Vue.js, Sigma.js, and deck.gl. It lets the user select a radius in a map and trigger a query to AWS Athena (through AWS Gateway and AWS Lambda) obtaining information from datasets stored in AWS S3; the data is processed with AWS Lambda and Python. Co-occurrence algorithms are used to process the “DESCRIPTION” field of each element returned from AWS Athena and a graph is generated with the words relations. As an example, the project uses datasets on a subscription basis from Kochava Collective, REARC and Relevant Data provided in the AWS Data Exchange service. These datasets were enriched and formatted for the application. Challenges I ran into The most noticeable challenge was to manage the time it takes to get data from AWS Athena and be able to return information through AWS Gateway after processing it in AWS Lambda in less than 30 seconds (the request timeout default). To solve the problem, I used chained requests; another approach could be to use the AWS SNS service. I was surprised at how easy is to setup the AWS Athena Service as long as all the .csv files stored in AWS S3 will have the same columns. Accomplishments that I'm proud of I am proud of running NetwokX algorithms on a serverless architecture such as in AWS Lambda. What I learned I learned the potential of data as a service in the AWS DataExchange platform. Also, I learned how well AWS Athena can be used to perform a serverless analysis of large datasets. AWS Athena was capable of retrieving data with simple SQL from multiple .csv files stored on the cloud. What's next for graphMap.? I would like to collaborate with AWS to build a service for co-occurrence graphs generation. It could be a similar service such as AWS LDA in AWS Comprehend. I would like to further develop the interface and develop plots for nodes properties such as nodes betweenness centrality, page rank, etc. I will try more heterogeneous data to better understand the scope of the technology. <div