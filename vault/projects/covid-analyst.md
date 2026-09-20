---
slug: "covid-analyst"
url: "https://devpost.com/software/covid-analyst"
title: "COVID Analyst"
hackathon: "World Hackathon Day"
winner: true
words: 439
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# COVID Analyst

> AI-powered targeted analytics for the COVID-19 pandemic

[Devpost](https://devpost.com/software/covid-analyst) · hackathon [[World Hackathon Day]]

## Facets

**domain** [[civic_government]] [[health_clinical]] [[scientific_research]]
**user** [[researcher]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** dialogflow, google-cloud, node.js, places-api, puppeteer, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what's next for covid analyst

## Body

Our User Interface shown on a Laptop Heat Map with Risk Assessment making use of US Census Data Set Our main screen showing the Heat Map, News, and Chatbot Inspiration Specific, region-targeted information surrounding COVID-19 is hard to come by. At best, a search on Google can get you the number of reported cases for your state along with countless news articles with questionable accuracy. We wanted to create an information hub for everything you need to know about COVID-19 in your region. What it does COVID Analyst uses machine learning and spatial data analytics with a combination of reliable data sources and research publications to give you an address-level risk heatmap of COVID-19 in your area. In addition, it scrapes credible news outlets to give you a feed of news in your area and an AI-powered chatbot will answer any questions you may have about COVID-19. Key Features: A risk heat map of your region created using published statistics from WHO and APM Research Lab and data from JHU and the US Census through spatial data analytics and machine learning. A web scraper that provides the user with relevant, credible COVID-19 news in their region. A chat bot that answers questions pertaining to the website and COVID-19 using live data and can conduct a symptom-based screening. What separates us: Our map provides information on an address-by-address level. We were the first ones to receive and work with a dataset including race/gender/age information for the US from AMP Research Lab (American Public Media Lab). How I built it Using socio-economic information from Census Tracts (data such as poverty rate, education, race-ethnicity, population pyramid, proximity to health care, and old age, we produced heatmaps to find communities that are at higher risk for COVID-19. Data is extracted and stored in a spatial data model, and we use machine learning to evaluate the risk factor based on published statistics as weights. Our web app is fully integrated with Google Cloud, running on App Engine, and using Places API and Dialogflow for the chat AI. We used React.js/Node.js for our web stack and conducted scraping with Node.js using Puppeteer. Challenges I ran into We were faced with hardware limitations (it took much more time than expected to process the data), so our app is currently limited to Wake County, North Carolina. What's next for COVID Analyst We started this as a sample for Wake County North Carolina (population about 1.1 million) but this work can be easily scaled to the entire US with the appropriate resources and time. We can also create a native mobile application along with the web app. <div