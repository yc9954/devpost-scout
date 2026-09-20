---
slug: "mykantaskypepregnancybot"
url: "https://devpost.com/software/mykantaskypepregnancybot"
title: "MyKantaPregnancyBot"
hackathon: "Junction 2016"
winner: true
words: 562
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# MyKantaPregnancyBot

> ChatBot that helps women through pregnancy using MyKanta data repository.

[Devpost](https://devpost.com/software/mykantaskypepregnancybot) · hackathon [[Junction 2016]]

## Facets

**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[code_repository]] [[structured_db]]

**stack** azure, bot, kanta, mysql, node.js, php

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mykantapregnancybot

## Body

Inspiration We wanted to try to implement MyKanta in a innovative way. Therefore we decided to combine AI and health tracks and create an AI bot interface for fetching data from Kanta. It can be used in many kind of purposes, but for the sake of simplicity, we made a user case example for pregnant women. What it does It will guide you thru pregnancy. You can ask to get your weight or latest lab tests from MyKanta. You can also use it to check your pregnancy state and important days based on dates found at MyKanta. You can also write medicines, symptoms and other stuff and it will give you information if there is something available. You can also type some simple sentences like "i am bleeding" or "i feel sick" and it tries to figure out what is happening. The bot already recognizes almost 200 words (about 120 lab values with baselines), some sentences, severe conditions and pregnancy stages. How we built it We created Microsoft bot in Azure environment. While Tuomas learned and developed the AI bot, Timo build a pregnancy database and integrated FHIR to the project. We used php + c# for programming, Mysql for data storage and our own servers for hosting. Also we sipped lots of Nocco. And coffee. Thanks to Microsoft's brilliant bot framework, the bot works on multiple platforms including Skype and FB. We generated our own chat-api that can be found at www.fudbot.com/chat-api.php Challenges we ran into Well, there is only two of us, so compared to many other teams, we needed to work extra hard. We also wanted to get some sleep and our apartment is at Westend, so timetable was tight for us. We also had some problems with Finnish FHIR server and final night we needed to switch to on in Canada ( http://fhirtest.uhn.ca/ ). Standards are still the same, but we needed to create our demo patient again. Also, FHIR and HL7 documentation is... all but logical and meant for humans. Accomplishments that we're proud of With team of two, we still managed to deliver a demo. We have never used Microsoft bots, Azure or even MyKanta before, but we managed to take over 'em all. We also made our own pregnancy knowledge database during weekend to use along MyKanta and other stuff. And nevertheless we ran out of time, we managed to learn our bot to had some actual AI. What we learned That if we want, we can achieve a lot during couple of days. However, we also learned that there is always problems when it comes to developing. Always. What's next for MyKantaPregnancyBot We would like to make the actual and full MyKanta implementation and expand this project for wider purposes. There is still a lot to do, for example, at this point you can't save thru bot. We wanted to make some data analytics but we simply didn't have time to do so. We do have some classes for predictive analysis already done so we can actually use this to lifestyle guidance purposes. We will also use this project as a demo of our service at Slush. We will integrate this to our own service among any others so we can generate risk models for gestational diabetes based on MyKanta data. And we would like to integrate Microsoft Face API for recognizing user. <div