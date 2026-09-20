---
slug: "a-gl06rs"
url: "https://devpost.com/software/a-gl06rs"
title: "QuickTriage AI"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 660
team_size: 0
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/health_clinical"
---

# QuickTriage AI

> Bringing AI into Quick Base for customer support teams

[Devpost](https://devpost.com/software/a-gl06rs) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

  <sub>weak: vision_ocr</sub>
**domain** [[health_clinical]]
  <sub>weak: labor_employment, supply_logistics</sub>
  <sub>weak: patient_family</sub>
  <sub>weak: financial_record</sub>

**stack** ai, flask, machine-learning, natural-language-processing, node.js, scikit-learn

## Body

QuickTriage combines Quick Base, support agents, and AI QuickTriage learns from previously labelled customer support tickets QuickTriage predicts support ticket categories based on AI Overview QuickTriage is an app built on Quick Base which uses Artificial Intelligence to help customer support teams triage incoming support tickets in a responsive, fast, and accurate way. The problem: Ticket triaging is manual and time-intensive Customer support agents spend hundreds of hours manually categorizing support tickets (e.g. "Returns" vs. "Refunds", or "Urgent" vs. "Low Priority"). They do this by tediously reading through every single support ticket to make their best guess as to which category it belongs to. This process is extremely manual and keeps them away from doing more interesting and engaging work like actually responding to customer requests. QuickTriage helps these support teams by automating much of this ticket triaging, and it works directly within Quick Base! How it works QuickTriage learns from past support tickets QuickTriage pulls in all the tickets previously labeled (by customer support agents) from Quick Base, and uses Machine Learning to learn characteristics about those tickets to start making its own predictions. When new uncategorized tickets come in, QuickTriage makes its best guess at the right category Now whenever a new record comes into Quick Base, QuickTriage will make a prediction on that record, along with a score of how confident it is in its prediction. Now support agents can spend their time manually only looking at the tickets that QuickTriage was most unsure about. Each day, QuickTriage learns from the tickets that had to be corrected by a support agent Each day, QuickTriage pulls in (through the Quickbase API) any records that a support agent had to manually correct, and learns from those corrections on how to predict better next time. This way, QuickTriage keeps getting better everyday! The combination of support agents PLUS QuickTriage allows businesses to respond faster By augmenting support agents with QuickTriage, companies can reduce the number of tickets that agents need to manually read through, and instead allow those agents to respond back to customer issues and streamline the entire process of customer support. Technology QuickTriage consists of the following components: The Quick Base Application (hosted in Quick Base) A Flask python server that serves the machine learning model (and trains the model daily). This code uses a machine learning library called Scitkit-Learn to build and train its machine learning model A Node.js API server that communicates with Quick Base through the Quick Base RESTful API to pull in records, send them to the Flask server for predictions, and send the updated predictions back to Quick Base Scope and Impact (+ future plans) The technology behind QuickTriage is generally built to take in records, and predict a single field of that record given access to the values in other fields. QuickTriage can easily be transferred to multiple use cases that are important for Quick Base customers, such as: Sales teams : Helping sales teams prioritize which leads to reach out to, based on the frequency of contact and other information Supply Chain Optimization : Bucketing ERP transactions into categories or categorizes vendor emails into priorities Healthcare (including Covid-19) : For example in St. George's Hospital's use of Quick Base , QuickTriage could help health workers prioritize which patients have the highest likelihood of needing help with Covid symptoms Future Plans: Make QuickTriage a general add-on in Quick Base Since QuickTriage could be used for so many different Quick Base use cases, the next steps would be to abstract the machine learning code to make it available for any Quick Base user to use, with their own Quick Base application and tables. A Quick Base user could select the QuickTriage channel, and configure it to work with their own tables and fields. QuickTriage could be a stand-alone service (like the other products in the channels) and democratize the access to AI technology to any Quick Base user to super-charge their application. <div