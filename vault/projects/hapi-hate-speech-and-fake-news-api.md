---
slug: "hapi-hate-speech-and-fake-news-api"
url: "https://devpost.com/software/hapi-hate-speech-and-fake-news-api"
title: "HAPI"
hackathon: "Junction 2016"
winner: true
words: 579
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/media_journalism"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# HAPI

> Give us an URL, we will tell you if it is fake news.

[Devpost](https://devpost.com/software/hapi-hate-speech-and-fake-news-api) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[cross_origin_web]] [[vision_ocr]]
**domain** [[finance_payments]] [[media_journalism]]
**user** [[general_public]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** css3, django, html5, javascript, python, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hapi - hate speech and fake news api

## Body

HAPI - plan Chrome Extension in Action - highlights fake news links HAPI - API request an response in web browser Inspiration Disinformation is a threat to democracy. Hate speech hurts minorities. Fake news sites are at the heart of this all. They are known for spreading hate speech, committing fraud, copyright offenses, and most of all, creating confusion and distrust towards legitimate news outlets. If you do not trust anything you read anymore, you have fallen victim to fake news. We want to make you trust again. Fake news overpowering real news is a growing problem for social media giants. Facebook, Google, Twitter, etc. are searching for a solution how to tackle this problem. We want to provide a fact-checked, transparent, reliable, comprehensive, and up-to-date data on Fake News Sites through an API for everyone to use. We will recognize fake news for you. Our solution can be used to, for example, create apps for the consumer, or as supporting data source for building newsfeed algorithms in social media services. What it does We have created a service that recognizes fake news. You can give an URL (or URLs) of a webpage to our API, and it will tell you if it is a fake news article. The api calls are very simple: http://[server]/fakenews/?url=firsturl&url=secondurl The response also contains information on where the fake news classification originated from (which shows who/what classified it as fake and why it is fake). Reliability of the data, as well as transparency, are the key in providing this service. As important as it is knowing which are fake news, is why they are classifies as fake news. To showcase a possible use case for the fake news API we have also created a browser extension for Chrome. This extension will highlight and warn you of links that point to fake news sites, for example in your Facebook feed. How We built it We used Python and Django Rest Framework for providing the API. The Chrome extension was written on JavaScript. Challenges We ran into Bugs in the code created by ourselves. Accomplishments that We're proud of Teamwork! Also we felt that we created something meaningful, current, and possibly commercially viable. What We learned We have learned about the scale of the fake news and hate speech phenomenona, and how they are affecting our society. We have learned to use new technologies, neither of us had experience of Django Rest Framework or writing browser extensions. What's next for HAPI - Hate Speech and Fake News API We have now created a simple prototype that proves that the idea works. The big picture (see picture) is that we want to have a classification system based on machine learning that will suggest new possible fake news sites or hate speech sites that could be added to our database. What we have in line next: Improve the technological solution (it's a prototype, it ain't pretty) Commercialization of the API: Freemium model where a limited rate will be available for free for everyone to use, heavy duty use costs money. We could also provide a simple web page for consumers for checking single URL's. Investigate more data sources. Our database has been created from the fake news site listing in Fake News Watch website ( http://www.fakenewswatch.com/ ). Ideally we would want such a listing from every country in the world. Only fact checked data accepted. Implement sentiment analysis that can help identifying hate speech and fake news <div