---
slug: "receipt-auto-record-system-by-gcp-ai"
url: "https://devpost.com/software/receipt-auto-record-system-by-gcp-ai"
title: "Receipt Auto Record System by GCP AI"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 440
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Receipt Auto Record System by GCP AI

> Effortlessly automate receipt recording with GCP AI: Let our AI-powered system do the work as it accurately identifies and records every line item and quantity from your receipts.

[Devpost](https://devpost.com/software/receipt-auto-record-system-by-gcp-ai) · hackathon [[Atlas Madness]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**substrate** [[document_pdf]] [[financial_record]] [[video_visual]] [[web_dom]]

**stack** express.js, gcp, mongodb, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for receipt auto record system by gcp ai

## Body

Inspiration Expense management becomes time-consuming when you have to manually input every detail on your receipt, so we came up with the idea of utilizing AI to identify texts on the receipt and record them in a table automatically for us. What it does It takes the user login credential and takes us to the user home page where we can upload our receipts and GCP AI helps us analyze the info on it and input it into the table. The table displays all the history receipts the user uploaded into the system. How we built it The front-end user interface is developed by React with Material UI component design. The back-end API service is programmed by Node.js with the Express.js framework. We store receipts and user information as separate collections in MongoDB Atlas. Receipts are analyzed by GCP Document AI. The front-end service is hosted by GCP App Engine, and the back-end API is hosted by GCP Compute Engine. Challenges we ran into The raw receipt data outputted from GCP AI is quite messy and needs to be further broken down and treated carefully to ensure the accuracy of data passed to the front end. The responses from analyzing different receipts can vary which requires back-end members to spend time coping with all different cases and consider the usage of useful data. Accomplishments that we're proud of We are able to well connect the GCP AI product to MongoDB storage and well utilize the GCP AI identifying texts feature to pass useful and accurate data to the front end for functional display. What we learned For the front end, we learned to use React.js to build a multi-page website including a user register/login page and data presenting page supporting user interaction. For the back end, we learned to build back-end service in Node.js with Cloud Storage, Document AI from Google Cloud, and perform CRUD operations with MongoDB Atlas. We also learned to deploy our front end and back end to the GCP app engine and compute engine. What's next for Receipt Auto Record System by GCP AI Reduce the size of the images before sending them to GCP DocumentAI to optimize the runtime Implement CI/CD for the project to avoid manual deploy Implement logic to clean up discarded receipts, e.g. when a user uploads the receipt to GCP Cloud Storage but decides to discard the record from MongoDB Enable the search bar, probably by using MongoDB Atlas Search to obtain a ranked result Allow users to filter their receipt list by date or by receipt expense Add more information inputs and value checking for the user registration process <div