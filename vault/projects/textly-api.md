---
slug: "textly-api"
url: "https://devpost.com/software/textly-api"
title: "Textly API"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 569
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# Textly API

> An all-in-one API for the grammar correction, spell check, sentiment analysis,Text Summary,Next word prediction, Neural Machine Translation (German to English).

[Devpost](https://devpost.com/software/textly-api) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** django, postman, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for textly api

## Body

Inspiration We got this idea of creating Textly-API from a previous hackathon that we've attended. We were trying to implement a text-analysis and text correction feature in our blog application but unfortunately we wouldn't find a free or open-source service that fulfills our purpose. That's why we created our own API to provide these services for free for which other companies like Grammarly might take a charge, because most of these services are paid. This API can be used for small scale projects and mobile applications. What it does It is an all-in-one API for grammar check, spell correction, sentiment analysis,Text Summary,Text Generation, Neural Machine Translation (German to English). Textly was build with Django-Rest-Framework and is based on Natural Language Processing. It uses many Deep Learning models like GPT2, BERT for text analysis. How we built it For Grammar Checking, we used CoLa (The Corpus of Linguistic Acceptability) dataset for training our model. We trained our model using BERT transformer in PyTorch that checks whether our text is grammatically correct or not. Similarly for sentiment analysis we used 1.6 million tweets dataset and trained it using BERT transformer in Pytorch that checks whether our text's sentiment is positive or negative. For spell correction we used text blob library in python. For next word prediction we used Open AI GPT-2. For neural machine translation we used Seq2Seq LSTM model built on PyTorch. For text summarisation we built abstractive summarisation using BART large CNN transformer. We used transformers for a deep learning as it provides state-of-the-art. API was built using Django Rest Framework and API testing is done by Postman . Challenges we ran into These model were relatively too big to be trained on a single GPU also size of dataset is quite large which takes lot of time in training. We didn't wanted to use AWS instance because we wanted our API to be fully customizable and wanted complete control over backend. Our model's size is too big so it was difficult to test it locally and also that's why we didn't deploy it. Our API uses many deep learning models for which we had to create many helper functions. To make our code more readable and avoid any ambiguity we stored models and their respective functions in their own modules. Accomplishments that we're proud of We're proud that we made an open source alternative of Grammarly with more functionalities. We are aware of the fact that currently our models are not highly accurate due to lack of resources but in future we can improve our models. What we learned This was the first time that we were trying to use these many deep learning models in a single API but Postman made this whole testing process a lot more easier for us and we learned how to create collection in the Postman which is great feature using which we can share our collection and API request with other developers that are working in the same team. We've learned how to implement transformers using PyTorch to get the state-of-the-art in the field of Natural Language Processing. What's next for Textly API *We are thinking of adding more than one language translation feature in the same API like currently we are doing for German - to - English. This API can be used small projects and mobile applications. Also we are thinking to create a Chrome Extension for Textly. <div