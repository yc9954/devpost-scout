---
slug: "greenwise-6xs1fb"
url: "https://devpost.com/software/greenwise-6xs1fb"
title: "GreenWise"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 394
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# GreenWise

> Make GreenWise decisions through automatic AI analysis of your purchases, and smart recommendations of lower carbon footprint products.

[Devpost](https://devpost.com/software/greenwise-6xs1fb) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[climate_energy]] [[finance_payments]]
**user** [[general_public]] [[legal_professional]]
**substrate** [[financial_record]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** flask, intel, jinja, openai, python, requests

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what's next for greenwise

## Body

The top webpage displays graphs of your carbon emmissions, and how much you can save. At the left you can upload reciepts to process. Here is a list of transactions from your electronic email reciepts and physical reciepts. Links to alternative green products are suggested. Inspiration People are increasingly aware of climate change but lack actionable steps. Everything in life has a carbon cost, but it's difficult to understand, measure, and mitigate. Information about carbon footprints of products is often inaccessible for the average consumer, and alternatives are time consuming to research and find. What it does With GreenWise, you can link email or upload receipts to analyze your purchases and suggest products with lower carbon footprints. By tracking your carbon usage, it helps you understand and improve your environmental impact. It provides detailed insights, recommends sustainable alternatives, and facilitates informed choices. How we built it We started by building a tool that utilizes computer vision to read information off of a receipt, an API to gather information about the products, and finally ChatGPT API to categorize each of the products. We also set up an alternative form of gathering information in which the user forwards digital receipts to a unique email. Once we finished the process of getting information into storage, we built a web scraper to gather the carbon footprints of thousands of items for sale in American stores, and built a database that contains these, along with AI-vectorized form of the product's description. Vectorizing the product titles allowed us to quickly judge the linguistic similarity of two products by doing a quick mathematical operation. We utilized this to make the application compare each product against the database, identifying products that are highly similar with a reduced carbon output. This web application was built with a Python Flask backend and Bootstrap for the frontend, and we utilize ChromaDB, a vector database that allowed us to efficiently query through vectorized data. Accomplishments that we're proud of In 24 hours, we built a fully functional web application that uses real data to provide real actionable insights that allow users to reduce their carbon footprint What's next for GreenWise We'll be expanding e-receipt integration to support more payment processors, making the app seamless for everyone, and forging partnerships with companies to promote eco-friendly products and services to our consumers Join the waitlist for GreenWise! <div