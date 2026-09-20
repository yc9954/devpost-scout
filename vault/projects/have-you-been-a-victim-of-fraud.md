---
slug: "have-you-been-a-victim-of-fraud"
url: "https://devpost.com/software/have-you-been-a-victim-of-fraud"
title: "Kore.ai bot for the Office of National Statistics (ONS)"
hackathon: "Kore.ai Botathon"
organization: "Kore.ai"
winner: true
words: 1147
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/general_public"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Kore.ai bot for the Office of National Statistics (ONS)

> This is a bot for the Office of National Statistics (ONS), the national statistics agency for the UK. With this Korea.ai bot, you can inquire about any statistics of the UK with a simple question.

[Devpost](https://devpost.com/software/have-you-been-a-victim-of-fraud) · hackathon [[Kore.ai Botathon]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[education]] [[finance_payments]] [[health_clinical]] [[labor_employment]]
**user** [[educator_student]] [[general_public]] [[legal_professional]] [[researcher]]
**substrate** [[structured_db]] [[web_dom]]

**stack** javascript, kore.ai, ons-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- target audience
- accomplishments that we're proud of
- what we learned
- what's next for kore.ai bot for the office of national statistics (ons)
- disclaimer

## Body

Inspiration The Office for National Statistics (ONS) is the national statistics agency for the United Kingdom and provides a wide range of statistics relating to the country, covering everything from the inflation rate to Gross Domestic Product (GDP) through to the number of hospital admissions in a particular year. It is the official source for many statistics relating to the UK. Although I do not work at the ONS, I have had a long association with them due to my studies as an undergraduate in BSc Economics at Cardiff University ( please note: I have since graduated ). One of my first encounters back in around 2013/2014 with the ONS involved their attempt to revamp their website. Like many organisations, the ONS was a bit "slow" in making their materials accessible to the average person and so spoke to myself and other university students from economics/maths backgrounds about what could be done about it. They listened to our advice and took it onboard. Since 2014, their website has been much more easier to follow: datasets are usually accompanied with attractive diagrams, the contact details of the division lead (e.g. national statistics) are visible and there are comprehensive summaries of what the dataset entails and any disclaimers that might need to be heeded of. Despite this, navigating through the ONS is still difficult to those who are not familiar with the website, which includes many "people on the street". The reason for this is multiple. Firstly, because of the sheer volume of data and information that the ONS covers. It is easy for the average person to feel overwhelmed. For example, the ONS covers the inflation rate but this alone has many dimensions - are we talking about the inflation rate over the course of a year, quarterly or monthly? The inflation rate also can be measured in at least two ways, the Consumer Prices Index (CPI) as well as the Retail Prices Index (RPI). The average person does not typically understand what these are or even why the difference in which measure is used is important ( hint: it affects everything from your pension to the cost of a train fare ). Another subtle difficulty with the ONS is that for many datasets, you need to know the ID of the dataset. It is very unlikely that most people know about the ID of a particular dataset unless they are what we call a "power user" (one who uses a particular website or resource considerably). What we want is a bot that can help the "average person" navigate through the website of the ONS in response to a human query. Furthermore, we want a bot that can assist with indirect questions. For instance, if a person asks, "why are prices rising?" we should have a bot that is able to infer this is hinting at the inflation rate and provide them the latest inflation figure. We also want a bot that at least looks and feels human: statistics is a humdrum field, so we want a bot that is chatty and can captivate a user's attention by having some "small talk" about topics as far-ranging as the outcome of the 2022 World Cup through to the show Strictly Come Dancing (a very popular show here in the UK!) For the purposes of this hackathon, this project falls within the Education category. What it does This Kore.ai bot for Office of National Statistics uses the following features in the platform: Dialog Task - This is the basis of the Kore.ai platform. Small Talk - used to keep the user engaged. We use the default Small Task and have also created our own relating to the 2022 World Cup, given the popularity of football/soccer. Knowledge Graph - These are likened to "Frequently Asked Questions" or "FAQs". We use Knowledge Graphs in this project to quickly answer questions such as, What is the definition of inflation? or What does unemployment mean? as just two examples in this project. Alert Task - This fetches information relating to datasets provided by the ONS using JSON from the endpoint https://api.beta.ons.gov.uk/v1/datasets . Further information about navigating the API can be found here at the ONS website. Channels - We deployed this for email and web/mobile client. For the purposes of this hackathon, this bot deals with the following areas: Inflation Gross Domestic Product (GDP) Unemployment (a future edition can include more areas) How we built it This bot was built using Kore.ai as well as the ONS' API which is exposed for free and does not require an API key . It also uses JavaScript to handle custom queries by using a Service Intent. In the context of the Kore.AI platform, it uses Dialog Tasks, Small Talk, Knowledge Graph Challenges we ran into A challenge I ran into when developing this bot was that some tutorials on YouTube were outdated. For instance, there was a reference to using "Action Tasks" as well as "Information Tasks" which I later learned were deprecated in later editions of Kore.ai. Another difficulty I encountered was that some terms have changed. For instance, "Knowledge Tasks" are now called "Knowledge Graphs". A slightly embarassing challenge I ran into is forgetting to click "Train" after making some edits. Target Audience The target audience is the average person on the street. Professionals working as university lecturers, teachers, economists, sociologists, political scientists and historians may also find this bot helpful. Accomplishments that we're proud of I'm proud of building my first bot. Furthermore, this brings Natural Language Processing (NLP) to the ONS for the first time, and I can see it being extended further. What we learned I learned about Kore.ai for the first time, so it was an interesting experience. What's next for Kore.ai bot for the Office of National Statistics (ONS) I'll be presenting this to a key individual at the Office of National Statistics who may choose to integrate this into the organisation and deploy it so that people can find it easier to navigate material published by them. If it is deployed, it is possible something similar can be created for the Bank of England (BoE), the country's central bank and oldest central bank in the world. It is plausible that if the project is a success, institutions outside of the UK - think, in the USA, the Federal Reserve, the Centres for Disease Control and Protection (CDC), the Environmental Protection Agency (EPA), to name just a few - might start integrating bots on their website in order to help users navigate through it in response to human enquiries. Disclaimer * This project is not officially associated with the Office of National Statistics and is simply produced in a personal capacity. * I have had to direct a special link to the video to the judge(s) given the size of the upload and wanting to meet the deadline. <div