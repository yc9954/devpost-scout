---
slug: "second-alert"
url: "https://devpost.com/software/second-alert"
title: "Second Alert"
hackathon: "AWS Artificial Intelligence Hackathon"
organization: "Amazon"
winner: true
words: 519
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Second Alert

> An AI tool developed to bring identity to lost people faces

[Devpost](https://devpost.com/software/second-alert) · hackathon [[AWS Artificial Intelligence Hackathon]]

## Facets

**domain** [[accessibility]] [[agriculture_food]] [[civic_government]]
**substrate** [[structured_db]] [[video_visual]]

**stack** amazon-web-services, node.js, vue

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for second alert
- online interface screenshots

## Body

Inspiration People get lost twice: first when they are reported and are being sought, and second when their disappearance end up pilled in a database. That is why we bring Second Alert, an AI software that brings an international identity to all those lost people who still cannot return with their families. What it does The technology, lets identify lost people from any web browser (including mobile phones). As examples: 1) It can be used to identify a possible hostage who is victim of human trafficking, 2) It can identify a lost child between thousands of lost children who do not remember/know their relatives names or home addresses or 3) It can identify an individual with mental disabilities who cannot return home. Second Alert, takes advantage of chatbot technologies in order to guide users in submitting a new report, see information about lost people and learn about the service How I built it The application was build using Node.js, AWS Lambda, AWS S3, AWS Dynamo DB, AWS SNS, AWS Rekognition, AWS Lex and AWS Comprehend. For the faces recognition, a front end interface was built using Vue.js in order to upload the image to AWS S3. As the image is loaded to S3 a AWS Lambda function call AWS Rekognition in order to check if the face is already in the Second Alert collection. At this moment, the Second Alert faces collection was created from official open lost people databases from the Mexican government; that information was processed through AWS Comprehend for future analysis. In order to submit a report, an AWS Lex chatbot was created and connected to the Second Alert Facebook page. Using the Messenger Chat, you can ask for information about the individuals registered in Second Alert, request a new report (and send a notification to Second Alert admins using AWS SNS), or simply get information about the service. Challenges I ran into I think the biggest challenge, was to understand a workflow that will be compatible for a future scale when faces from all around the world will be indexed. For this purpose, a proper data structure design was applied. Accomplishments that I'm proud of I like the way that I collect information using AWS Lex. At the beginning I was thinking about Mailchimp's service in order to get an email and then contact the people who is making requests. But I realized that I can do that with AWS Lex. With AWS Lex I was able to harvest that information and even send emails using AWS SNS all directly from Facebook Messenger. What I learned I learned a lot about how I can use AWS Lex for customer service and learn that we are at the point where IT technologies can make a great impact in human trafficking problems. What's next for Second Alert I am looking forward to collaborate with governmental institutions in order to reduce the data scraping efforts, increase the audience who knows Second Alert services and to use the Second Alert faces collection to search individuals using public cameras. Online interface screenshots Second Alert face recognition Second Alert Chatbot <div