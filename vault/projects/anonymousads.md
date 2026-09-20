---
slug: "anonymousads"
url: "https://devpost.com/software/anonymousads"
title: "AnonymousAds"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 481
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# AnonymousAds

> A search engine that uses machine learning models to deliver targeted advertising, while at the same time safeguarding user privacy, through the use of fully homomorphic encryption and noise injection

[Devpost](https://devpost.com/software/anonymousads) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[privacy_tech]]
**substrate** [[financial_record]] [[web_dom]]

**stack** css, docker, flask, html, nltk, python, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- solution overview
- how we built it
- what's next for anonymousads

## Body

AnonymousAds Inspiration In this digital era, businesses have primarily relied on two revenue streams. The first is the age-old approach: users opening their wallets. The second, more modern method, involves users paying with their personal data – often at the cost of their privacy . But times are changing. Users are becoming increasingly privacy-conscious , and they yet remain reluctant to pay for services they've grown accustomed to receiving for free. This creates a seemingly unsolvable paradox . This is why we, Ete, are addressing Problem Statement 1: Innovating Privacy . We're excited to share with you how we've devised an approach that allows the serving of targeted advertising , while guaranteeing complete user privacy . What it does AnonymousAds leverages Fully Homomorphic Encryption (FHE) , noise injection , and machine learning algorithms to deliver relevant, targeted ads based on fully encrypted user data - ensuring complete user privacy . Our solution presents a proof of concept in the form of a search engine that uses machine learning models to deliver targeted advertising while safeguarding user privacy . Solution Overview AnonymousAds provides a secure method for serving targeted ads by ensuring complete user privacy . Here's how it works: Data Collection : Users input search queries into the search engine. For our proof of concept, these inputs correspond to search engine queries. Data Encryption : After every fifth query, this sensitive user query information undergoes word processing and local encryption , before secure transmission to our servers, maintaining user privacy. Predictive Modeling : The encrypted user data is processed through a machine learning model that predicts user interest categories , such as sports or culinary topics, based on keyword analysis from their search queries. This facilitates precise audience segmentation for targeted advertising . Decryption : The model generates an encrypted vector of ad category predictions , which is transmitted back to the client for local decryption . These predictions are then refined using Bayesian methods , incorporating previous data to enhance accuracy. Ads Serving : To further maintain user privacy, the client then requests ads from the server using a combination of genuine predicted categories and randomly generated ones . This obfuscation technique effectively masks the true predictions. The client then selectively displays the most relevant, targeted ads to the user, based on the authentic predictions. How we built it Technologies Used : Backend: Python, Flask Machine Learning: Concrete-ML, Scikit-learn Frontend: HTML, CSS, JS, Jinja Word Processing: NLTK Containerization: Docker What's next for AnonymousAds With this proof of concept, we aim to inspire corporations to adopt FHE , ensuring user privacy while benefiting from targeted advertising. Major platforms like YouTube and TikTok can continue using targeted ads while safeguarding user information . By demonstrating the effectiveness of AnonymousAds, we hope to redefine the relationship between user privacy and targeted advertising , showing that profit and privacy can coexist harmoniously . <div