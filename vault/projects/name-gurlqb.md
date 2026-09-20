---
slug: "name-gurlqb"
url: "https://devpost.com/software/name-gurlqb"
title: "Heimer's Hackers Power Rankings"
hackathon: "Global Power Rankings Hackathon"
organization: "Amazon"
winner: true
words: 334
team_size: 7
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
---

# Heimer's Hackers Power Rankings

> We train machine learning models to predict game outcomes. Then, we use these models to create power rankings by simulating round robin style tournaments. Rankings are displayed on our web app.

[Devpost](https://devpost.com/software/name-gurlqb) · hackathon [[Global Power Rankings Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]

**stack** amazon-web-services, aws-athena, figma, javascript, lightgbm, next.js, numpy, pandas, python, react, sagemaker, scikit-learn, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for heimer's hackers power rankings

## Body

Homepage Team Ranking Search Tournament Ranking Search Global Ranking Results Tournament Ranking Results Inspiration We drew inspiration from modeling techniques and statistical methods in traditional sports. What it does Our project trains various classical machine learning models to predict individual League of Legends game outcomes using statistics from previous games. Our best gradient boosted tree models predict outcomes with 65% accuracy over all games from Worlds and MSI qualifying regions from 2022-2023. On Worlds and MSI games alone they make predictions with 70% accuracy. We then use these models to create League of Legends esports power rankings for different tournaments and sets of teams by simulating our own round robin tournaments. These rankings are displayed on a web app. Users can search for various power rankings using 3 different pages and a search bar. How we built it We used AWS Athena to query relevant statistics from the original data. Python libraries including Pandas, numpy scikit-learn, LightGBM and XGBoost are used for our data cleaning, feature engineering and modeling. The power rankings are the result of a LightGBM model predicting game outcomes for a simulated round robin tournament. A detailed description of our ranking methodology can be found here . The web app was built using Next.js deployed on AWS Amplify. Challenges we ran into Certain aspects of League of Legends are difficult to quantify. We specifically found it challenging to properly relate performances in different leagues. Selecting which features to train with was also hard because of how much time it took. Accomplishments that we're proud of We're proud of all the time and effort that went in to both our ranking method and web app. What we learned Over the last two months, we learned a great deal about sports statistics and AWS. We also gained a greater appreciation for how complex League of Legends is as a game. What's next for Heimer's Hackers Power Rankings There are some graph-based methods and deep learning models we might try in the future. <div