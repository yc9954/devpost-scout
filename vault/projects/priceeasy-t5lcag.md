---
slug: "priceeasy-t5lcag"
url: "https://devpost.com/software/priceeasy-t5lcag"
title: "PriceEasy"
hackathon: "Hack the North 2020++"
winner: true
words: 402
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "substrate/structured_db"
---

# PriceEasy

> Online shopping has never been easier! PriceEasy provides you with the cheapest price of any product over multiple online retailers.

[Devpost](https://devpost.com/software/priceeasy-t5lcag) · hackathon [[Hack the North 2020-]]

## Facets

**domain** [[retail_commerce]]
**substrate** [[structured_db]]

**stack** android, android-studio, dropbase, java, parsehub

## Body

Home Screen Search Result (New Products) Search Result (Used Products) Project Description PriceEasy is an android app developed using APIs from Dropbase and Parsehub that allow the user to search for a product across multiple websites, including used marketplaces, to find the cheapest available price. Inspirations We were inspired by the surprising lack of an app that compares the prices of products over a wide range of online retailers. Although apps like Honey and AutoTrader already exist, they either heavily focus on a certain type of product or lack functionality to use on a daily basis. There is also no app for comparing prices across the major used marketplaces. About PriceEasy uses the Parsehub web scraping algorithm and API to obtain data from websites. This data is then run through our own refinement algorithm built on the Dropbase software, and is uploaded and downloaded from the Dropbase database using the Dropbase API. Features Our powerful result filtering algorithm built on Dropbase ensures the user finds exactly what they are looking for. PriceEasy is the only sales app with support for both new and used marketplaces. The simple UI make navigation easy and results are clearly displayed in a list. Technologies used The application is built in Android Studio using Java. The parsehub software is used to extract search results from websites, and their API is used to ingest the data into our workflow, in a csv file format. This file is then uploaded to our Dropbase database using the Dropbase API, where the data is processed and then sent back to the device. Challenges we ran into We ran into some issues with setting up the data flow between the Parsehub and Dropbase APIs as there were compatibility issues with the dropbase software and our computers. making it hard to test our application from search to display. What's next for PriceEasy? PriceEasy is built on an extremely scalable algorithm, and a main focus of development is to increase the number of marketplaces, as currently the application is focused on the technology sector. We plan to use our data processing algorithm in dropbase to add more convenient features such as storing search data to track the price of an item over time. We want to give the user more control over elements such as price range, how they see the results, and we want to add a feature for price alert notifications. <div