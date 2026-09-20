---
slug: "elara"
url: "https://devpost.com/software/elara"
title: "Elara"
hackathon: "Square + Google AI Hackathon"
organization: "Square"
winner: true
words: 312
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Elara

> Intentional giving at the Point of Sell (POS) with Google's Vertex AI and Square API

[Devpost](https://devpost.com/software/elara) · hackathon [[Square - Google AI Hackathon]]

## Facets

**domain** [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** cloud, css, go, google, html, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for elara

## Body

Inspiration According to recent research, over 4.1 billion dollars were raised for charities in the past three decades through point-of-sale (POS) transactions. Donors have reported feeling "guilt" as the primary motivating factor behind their contributions [1]. However, this test project aims to change the giving dynamic by promoting shared understanding and appreciation instead of guilt. Implementing non-profit matching at the POS offers several advantages, including fostering a stronger bond and loyalty between merchants and their customers. What it does Matches a nonprofit to support based on what is included in customers' shopping carts at the POS. How we built it Trained an ML model using open data provided by Charity Navigator on Kaggle. The model is then hosted on Google's Vertex AI and linked to an endpoint. A Go-based three-tier application consumes the Vertex AI endpoint to match nonprofits with customers' current transactions at the POS. Challenges we ran into Even though data from Charity Navigator has a great selection of attributes, filtering out the attributes to use for training the AI model was a challenge. Sending the entire dataset and selecting columns to train on doesn't work well. The Vertex AI training process attempts to automatically select columns but often fails due to insufficient labels in the training dataset (e.g. missing column values for some rows) or inadequate resources to complete a training step in one case. Accomplishments that we're proud of Getting the PoC up and running on Google Cloud. What we learned Square API features Google Cloud Vertex AI offering and features ClourRun deployments and containerization for Google Cloud Terraform deployments in Google Cloud What's next for Elara A retrained ML model with additional labels such as nonprofit scoring based on publicly available financial figures. An option for nonprofit to finetune their settings per request (e.g. I want to match only nonprofits in the mid-Atlantic or West Coast). <div