---
slug: "whatsinstock"
url: "https://devpost.com/software/whatsinstock"
title: "WhatsInStock"
hackathon: "Pandemic Response Hackathon"
organization: "Datavant"
winner: true
words: 440
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# WhatsInStock

> Map that displays nearby stores and their inventories, so you know where to shop during the pandemic.

[Devpost](https://devpost.com/software/whatsinstock) · hackathon [[Pandemic Response Hackathon]]

## Facets

**domain** [[retail_commerce]] [[supply_logistics]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, aws-lambda, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that i'm proud of
- what's next for whatsinstock

## Body

Our data crowdsourcing web form pop-up when viewed on mobile. Target #3321 is currently out of hand sanitizer. We have data that covers New York City and other major cities. Note: Due to the severe situation in New York City, we'll be shifting our coverage to all of the surrounding areas of NYC instead of the downtown areas of ten cities throughout the US. We think that this'll allow us to provide better service to more people! Inspiration Because people are panic-buying necessities, tons of supermarkets are experiencing shortages of basic groceries. We want to make sure that people in coronavirus-heavy areas have groceries during this pandemic time, so we made a website that shows nearby stores and their grocery inventories. What it does WhatsInStock is a map that shows data about nearby stores and their inventories, so that people in coronavirus-heavy areas can know where to shop when they run low on food or other supplies. Although some stores have limited how many items people can buy to prevent hoarding, many stores still have inventory shortages due to the pandemic. With WhatsInStock, people can use our map to make sure that they are going to stores with ample in-stock goods for grocery shopping. Also, we request feedback from our users through pop-up a web form when we detect that they are in a grocery store, so that they can help us verify whether or not our listed "in stock", "low on stock", "out of stock" classifications are accurate. With crowdsourced inventory data, we can create a more up-to-date inventory count for essential goods, which may even help inform better grocery logistics during the pandemic! How we built it WhatsInStock is built on AWS using AWS Lambda, DynamoDB, S3, API Gateway, and SQS. It is hosted on a github repository as a github pages static site. The Front End is built with the Google Maps API. Accomplishments that I'm proud of In this project, we used Amazon S3 to save our data so that users would be able to get it very fast. Before, when we were using an API that would pull from a database and generate the data live, our website would load in 11-12 seconds. When we added in the S3 file as a "cache", the website now loads in 0.2 seconds. What's next for WhatsInStock We are looking to expand to cover more stores in more cities, so more people can use whatsinstock.github.io. Right now, we're limited by our expensive data collection process, so more time will make it more efficient, and more money will allow us to gather data on more cities and stores. <div