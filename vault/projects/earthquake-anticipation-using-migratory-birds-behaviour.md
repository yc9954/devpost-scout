---
slug: "earthquake-anticipation-using-migratory-birds-behaviour"
url: "https://devpost.com/software/earthquake-anticipation-using-migratory-birds-behaviour"
title: "Migratory Birds for Earthquake Forecasting"
hackathon: "AWS Disaster Response Hackathon"
organization: "Amazon"
winner: true
words: 465
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/structured_db"
---

# Migratory Birds for Earthquake Forecasting

> Migratory birds are magneto-receptive. Geomagnetic changes are generated a few days prior to earthquakes. We believe that feeding a BLSTM with White Stork behaviour can lead to earthquake prediction.

[Devpost](https://devpost.com/software/earthquake-anticipation-using-migratory-birds-behaviour) · hackathon [[AWS Disaster Response Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[disaster_emergency]] [[finance_payments]] [[security_privacy]]
**substrate** [[structured_db]]

**stack** accelerater, accelerometer, blstm, movebank, python, r, randomforest, sagemaker, usgs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for earthquake anticipation using migratory birds behaviour

## Body

BLSTM Workflow Train/Val/Test Accuracy across 10 models Prototype of implementation using Fibonacci Sequence One of the model's performances across epochs Inspiration One of the team members was at a Safari during the Sri Lanka tsunami of December 2004. A few hours prior to the wave, the animals started acting differently (e.g. freezing, collective restlessness). In the literature, there have been many reports of Unusual Animal Behaviours before earthquakes since antiquity. Given that migratory birds have magnetoreception and that there are subtle local geomagnetic disturbances a few days prior to earthquakes, we believed that they were potentially able to feel these subtle changes and change their behaviour. What it does By looking at pre-labelled daily White Stork behaviour sequences, the model was able to discriminate with more than 80% accuracy if the sequence belonged to a 10-day temporal window before earthquakes magnitude > 6. How we built it We combined several White Storks datasets on the MoveBank database. We filtered by 10 days/300km Spatio-temporal proximity with earthquakes above magnitude 6. We labelled every 2 minutes of accelerometer data using pre-trained RandomForest. We grouped the obtained labels into ground/flight categories (0/1). We merged obtained labels into daily sequences per individual. We assigned EQ or Control label to the sequence. We split the data into training/validation/testing. We trained a BLSTM to predict EQ/Control label based on the sequence. Challenges we ran into Finding overlapping EQ & White-Stork spatio-temporal data for the BLSTM training. Pre-processing the data to feed the BLSTM. Accomplishments that we're proud of The study suggests that migratory animals might sense strong earthquakes a few days prior. The model is accurate enough to be implemented for a live trial phase on open-source data streams. What we learned Through this project, we learned that by protecting wildlife, we can learn a lot about ecosystems interactions. We learned to be humble and receptive to the collective wisdom of wildlife. Because, as for other animals, we are vulnerable when it comes to natural disasters. There is no more distinction between species when it comes to survival. Hence, we shall protect them and maybe they will protect us back. What's next for Earthquake anticipation using Migratory Birds behaviour We will work towards end-to-end automation of the workflow in order to have daily predictions per White Storks without human intervention. To increase temporal definition, a superlinear function will estimate earthquake risks based on a sequence of BLSTM outputs per individual. If multiples Storks are in the same area with EQ labelled daily behaviour sequences, we might be able to use triangulation to approximate the location of the upcoming earthquake. We can test the same methodology on different migratory birds or magneto-receptive animals in order to increase the probability of a tagged animal being in the vicinity of the upcoming earthquake. <div