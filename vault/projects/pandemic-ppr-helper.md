---
slug: "pandemic-ppr-helper"
url: "https://devpost.com/software/pandemic-ppr-helper"
title: "Pandemic-PPR Helper"
hackathon: "AWS Health AI Hackathon"
organization: "Amazon"
winner: true
words: 492
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Pandemic-PPR Helper

> Pandemic prevention, preparedness, and response (PPR) using AWS Health AI .EXPLORE -> DETECT -> RESCUE

[Devpost](https://devpost.com/software/pandemic-ppr-helper) · hackathon [[AWS Health AI Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** amazon-web-services, natural-language-processing, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pandemic-ppr helper

## Body

arch Inspiration World Health Organization announced The Financial Intermediary Fund (FIF) - link for Pandemic Prevention, Preparedness and Response finances critical investments to strengthen pandemic prevention, preparedness, and response capacities at national, regional, and global levels, with a focus on low- and middle-income countries. The devastating human, economic, and social cost of COVID-19 has highlighted the urgent need for coordinated action to build stronger health systems and mobilize additional resources for pandemic prevention, preparedness, and response. While there are many institutions and financing mechanisms that support pandemic prevention, preparedness, and response activities, none of them is focused solely on it. COVID-19 has highlighted the pressing need for action to build stronger health systems. “Investing now will save lives and resources for the years to come. What it does The main goal of this project is to build a single product that will help us to prepare for pandemic - Monkey Pox. MonkeyPox News Twitter Pandemic Situational Reports https://www.who.int/publications/m/item/multi-country-outbreak-of-monkeypox--external-situation-report--7---5-october-2022# Mpox-DETECT: The confirmatory Polymerase Chain Reaction (PCR) tests and other biochemical assays are not readily available in sufficient quantities. Mpox-Detect helps the user to Quickly detect the Monkey Pox disease and contact the hospital . 1.Firstly, User can Input the General Features like Country he is located ,Gender, Travel History and Symptoms he is facing like Rash, Lesions etc. and then we get the understand the stats from monkey pox cases confirmed data. 2 . Once user understands trends based on symptoms and general features, User can then upload the skin images and get the probability that user might have the disease based on skin images computer-aided monkeypox identification from skin lesion images .Monkeypox Skin Lesion Dataset (MSLD)" is created by collecting and processing images from different means of web-scrapping i.e., from news portals, websites and publicly accessible case reports. RESCUE: MonkeyPox Scientific Literature Dataset contains all available scientific knowledge published on the topic of Monkeypox scraped from PubMed, starting from as early as 1974 to 2022, up to the abstract level. We then extract the medical entities from the scientific Literature using AWS comprehend medical. Also, Semantic Search is done using Sentence Transformers. Then, Users can ask the questions related to issues they are facing and get the related answers from scientific literature. Also ,Emergency Management can monitor the issues people are facing ,get relevant answers from scientific literature for complex questions and respond to the patients. How we built it Researched about the all the required relevant data and Built Dashboard using Plotly Dash Challenges we ran into Installing TensorFlow ,TensorFlow libraries for Heroku due to size limit Accomplishments that we're proud of Combining all the data from multiple channels and building one product that solves end-to-end problem and save lives during pandemic What we learned Extracting Medical Entities AWS Comprehend Medical What's next for Pandemic-PPR Helper Making it scalable and real time system. Add many features like Virtual Appointment booking and chat bot using Amazon Lex. More on Network Analysis.snsni <div