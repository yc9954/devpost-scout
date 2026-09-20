---
slug: "pfmbot"
url: "https://devpost.com/software/pfmbot"
title: "PFMBot"
hackathon: "AWS Chatbot Challenge"
organization: "Amazon"
winner: true
words: 367
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# PFMBot

> What if you could talk to your bank account? Well now you can!

[Devpost](https://devpost.com/software/pfmbot) · hackathon [[AWS Chatbot Challenge]]

## Facets

**domain** [[finance_payments]]
**substrate** [[structured_db]] [[web_dom]]

**stack** aws-lambda, aws-lex, java, javascript, mysql, springboot

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pfmbot

## Body

Inspiration Our mission at MoneyLion is to improve the financial health of our customers. One of the ways we try to achieve this is by helping people to manage their personal finances. Besides providing people with visualizations of their personal financial health and showing them the numbers, we wondered whether it would be possible for people to talk to their bank accounts as if they were talking to their very own personal banker! Thus PFMBot was born. What it does Once a user signs up an account via the MoneyLion app or our website, the user has the option to link their bank accounts with our own internal APIs. Once that is done, the user will be able to login to their MoneyLion account and start having a conversation with the PFMBot based on information stored How it was built [End User] <-> [Chatbot UI using Javascript integration] <-> [Amazon Lex] <-> [Java-based Lambda functions] <-> [Java-based internal API on Springboot] <-> [MySQL db] Challenges we ran into Defining the appropriate intents Coming up with just the right amount of sample utterances to train Amazon Lex Defining the slots in each intent and coming up with just enough sample values to train Amazon Lex Learning to parse the built-in AMAZON slots and converting the values for built-in slot values Dealing with past datetimes since AMAZON datetime library is more biased towards present and future dates Accomplishments that we're proud of We are proud of the fact that were were able to quickly build a working chat bot prototype in a very short time and the proof-of-concept already shows great potential and value to our prospective users What we learned We learned about the construction of Amazon Lex intents and slots, how to integrate AWS lambda with our own internal APIs, and we learned how easy it was to integrate Amazon Lex using javascript What's next for PFMBot At the moment the chatbot is just a proof-of-concept. The next steps for this bot will be to incorporate it with our live, production database, which is using a combination of mongoDB and Amazon Red Shift, and integrate the chatbot interface in our mobile app and user web dashboard <div