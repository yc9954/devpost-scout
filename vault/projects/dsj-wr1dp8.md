---
slug: "dsj-wr1dp8"
url: "https://devpost.com/software/dsj-wr1dp8"
title: "Sirius"
hackathon: "Kore.ai Botathon"
organization: "Kore.ai"
winner: true
words: 510
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Sirius

> Banks usually don't offer enough user interaction or customer service. They do not perform the requested service on time. Also user aren't able to trade stocks at ease, which is where SIRIUS comes in.

[Devpost](https://devpost.com/software/dsj-wr1dp8) · hackathon [[Kore.ai Botathon]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[code_repository]] [[financial_record]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, express.js, flask, machine-learning, mongodb, node.js, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- try our bot
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sirius

## Body

Complete flow chart of our chatbot Inspiration It draws inspiration from a variety of payment services and stock trading platforms , so we thought: why not implement it in a chatbot with a more simplified user experience? What it does An AI chatbot named SIRIUS integrated in our Website with which the user can get done all their bank and stock services at their home. The list of features are : User can easily transfer money from their account to another account and notified through email. With SMS and email OTP verification, authentication is securely handled. User can change their login pin if forgotten. With their stock trading and Dematerialization account user can buy and sell stocks. Users can view real time stock rate with time series visualization and can also see trending stock news. Users can check their eligibility to apply for loan( Machine Learning using Python Flask Framework ) Users can view their transaction statements of their latest transaction. Users can block or unblock his credit card. Users can view their nearest branches by typing in their Zip code. Calculator for foreign money exchange . User can move funds in both ways between trading and savings accounts . 12 Multilingual Bot( Spanish, German and English as NLU language) Multi channel deployment ( Telegram, Website) How we built it The whole solution is deployed into the website which is built using MERN (MongoDB, Express.js, React.js, Node.js) stack. The website is built using React.js hosted in NETLIFY and the microservices are built using Node.js hosted onto the Amazon Web Services (EC-2 instance) and database connected to MongoDB Atlas. GitHub is used as our version control and code repository tool We have implemented KANBAN and AGILE methodology for quicker development and deployment of our project and also REGRESSION testing method is implemented { "Website": "React.js", "Backend": "Node.js", "Database": "MongoDB", "Cloud": "Amazon-Web-Services", "Machine Learning": "Python", "Software Methodology": ["KANBAN", "AGILE"], "Version Control" : "GitHub", "Deployment": ["Telegram", "Website"] } Try our bot Account 1 { "Username": "James", "Pin": "1234", "Account Number": "1234", "IFSC code": "1234", "credit-card": "12345, "email": "james.chatbot.test@gmail.com", "email-pass": "testingourbot" } Account 2 { "Username": "Mary", "Pin": "1111", "Account Number": "12345", "IFSC code": "12345", "credit-card": "123456, "email":"mary.bankbot.test@gmail.com", "email-pass": "testingourbot" } Challenges we ran into Handling the edges cases and deploying our microservices in various cloud platform. Accomplishments that we're proud of Training our bot with nearly 700 utterances , deploying our microservice in AWS and integrating ML model into chatbot after training 25,000 datapoint What we learned The User Experience (UX) which we provide to the end-users who uses this bot should be up to the level and enjoyed developing the bot in the kore.ai XO platform. Learnt the different internal engines used for intent identification like Fundamental meaning engine, Machine Learning engine, Knowledge graph engine, Ranking and Resolver engine What's next for Sirius Next we plan to make this bot for accessible in more number of languages and also planning to move the payment services in a de-centralized manner using Blockchain techniques along with deep learning and solidity for data protection <div