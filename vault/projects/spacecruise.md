---
slug: "spacecruise"
url: "https://devpost.com/software/spacecruise"
title: "SpaceCruise"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 577
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/document_pdf"
---

# SpaceCruise

> Book a trip to space/visit MARS as easily as you would be able to book a cruise and receive updates on travel, food, and entertainment updates

[Devpost](https://devpost.com/software/spacecruise) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: finance_payments</sub>
**substrate** [[document_pdf]]

**stack** api, javascript, postman

## How they structured the write-up

- inspiration
- what it does
- how is it built
- challenges
- accomplishments
- lessons learnt
- what's next for spacecruise

## Body

Application Features APIs used Collection Runner run Event created and published automatically Automated event updates delivered via mail Credit: created by upklyak in freepik Inspiration POSTMAN Galaxy event itself was the inspiration. I wanted to create something fun and creative with NASA APIs and other cool publicly available, well-documented APIs. It can be a pain to manage events especially the ones that need regular updates based on some criteria or an event that needs to be created frequently based in schedule. Here, I am demonstrating the automating of such events using postman and a cool example. What it does SpaceCruise is an application that can one day be used to book your trip to outer space. It is a creative, futuristic, space application which is a tribute to the Galaxy-Themed POSTMAN hackathon itself as it is completely based on POSTMAN tool. SpaceCruise is a collection of different APIs painstakingly yet beautifully knit together to carry out the tasks: Creating and managing space events automatically Send automated weather forecasts via email Send real-time Travel updates to the passengers Apart from travel updates, the email also comes with A random Spotify playlist for the trip, shuffled every day for the trip based on category Menu for the day based on which day you are traveling Some pictures of outer space. By the end of the collection, if you have entered your email ID in the environment variable emailID, you will receive an actual email with all the updates as mentioned above. How is it built It is built with awesome features of the postman tool such as Collections, Collection Runner, Monitors, Mock Server, pm test scripts, environment and collection variables, and much more Monitor : To start the collection automatically at a scheduled time so that event gets created automatically and is published, updates are also received from various APIs and sent automatically to email of the passengers. Mock Server : used to dispense forecasted space travel updates Pre-request scripts : added to generate the day and time of event , to set collection variables etc., Test scripts : used to ensure the request passed and a response was received. Collection runner : to chain the requests and make them talk to each other via environment variable and collection variable and run requests in sequence. Challenges Finding well documented public APIs Understanding the API responses and extracting values from them Using the elements from the response body to set collection variables and basically stitch APIs together so the collection runs seamlessly Unavailblity of certain API - but quickly found a way to resolve it using mock servers Accomplishments To have successfully utilized most features of the POSTMAN tool To have successfully created a project of what hopefully is a unique concept To have successfully learned to document and write javascript snippets To have successfully managed to put together a collection that actually does something Lessons Learnt Use Monitors to schedule and trigger collection Take advantage of postman code snippets for validation Use collection variables to make requests talk to each other Use cURL to import requests in raw form Use mock serves to return sample data if API is not available yet Create and use environment variables Create docs with markdown and publish it Constant learning is the only way to go What's next for SpaceCruise Webhooks to intimate tickets bought More control over the Spotify playlist generated like using genre and category IDs set by the passenger <div