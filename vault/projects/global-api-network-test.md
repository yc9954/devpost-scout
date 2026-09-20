---
slug: "global-api-network-test"
url: "https://devpost.com/software/global-api-network-test"
title: "Global API Network Information"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 589
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Global API Network Information

> Your API is deployed in several data centers, now you need to know what the rest of the world is experiencing when they make a call to it. Examine latency, DNS, traceroutes etc from around the world.

[Devpost](https://devpost.com/software/global-api-network-test) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-dynamodb, amazon-web-services, cdk, lambda, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for global api network test

## Body

Latency for cnn.com by AWS Region in seconds View WHOIS server updates for a domain Checking version discrepancies of a multi-region API Traceroute mapped to the globe Inspiration While taking on customers further afield from our data centers, I was wondering how the experience changed based on their location. Initially, I was looking at logs on the front end for performance metrics, but this was too reactive - identifying an issue after the customer has been impacted. I wanted to learn about potential issues as I roll changes out. What it does Given an endpoint, a series of network tests are performed in multiple regions across the world. The API assembles the complete data set, and the Postman Collections allow you to quickly visualize the information you are interested in. Maybe we want to see what latency customers are experiencing in the USA and in Asia as a simple bar chart. Or we want to validate that our geo-location routing policy is working correctly by examining the traceroute, with the individual hops illustrated on a map. How we built it Built out on AWS utilizing API Gateway, AWS Lambda, and DynamoDB. DynamoDB Global Tables are used to propagate the requests received in any one region across all other AWS regions. Each region then has a series of Lambda's trigged to retrieve specific networking data from that location. This data is saved back in another DynamoDB Global Table allowing users to retrieve the complete data set from anywhere. The API Key Management website is a React front end utilizing AWS Amplify to register and verify users. Challenges we ran into While AWS Lambda supports Docker images, the provided base images to do include the network tools that were needed. This required learning how to create a custom image with the Lambda RIC. We ran into multiple limitations, only certain regions supported container-based Lambdas, and even DynamoDB Global tables did not extend to every region. Once the application was expanded to the 16 regions that did support the global tables, CI-CD would become an issue when tearing down and rebuilding the entire API taking over 3 hours. API keys are also specific to a particular region, this required additional work to propagate an API key to each region and install it so that requests could be made from anywhere. Accomplishments that we're proud of The API is a globally distributed serverless application built with the AWS CDK, allowing anyone the ability to modify the configuration file and stand up their own version in as many regions as required. The API returns a large amount of data, which allowed us to really utilize the Visualizer in Postman in multiple ways. What we learned The visualization capabilities of Postman was the main learning point. Taking large data sets and being able to manipulate the data via a test and inject it into a template that could utilize D3js or Bootstrap to provide a visual that quickly highlights potential issues. What's next for Global API Network Test Currently the system runs in AWS, which doesn't return much data about its internal network. To attain better information on systems in AWS, we would deploy a similar system in Azure, allowing us to see how networks outside of AWS would process the requests differently. Try to leverage the Postman Workspace, to have people contribute requests/visualizations that gets data that they are most interested in. The aim was for api-network.info to return generic data and have the Postman Workspace highly interesting ways people could use it. <div