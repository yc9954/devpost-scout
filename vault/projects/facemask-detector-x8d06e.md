---
slug: "facemask-detector-x8d06e"
url: "https://devpost.com/software/facemask-detector-x8d06e"
title: "Facemask Detector"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 623
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Facemask Detector

> Real implementation of a facemask detection service powered by Azure ML, Function App and Azure API Management Service.

[Devpost](https://devpost.com/software/facemask-detector-x8d06e) · hackathon [[Azure AI Hackathon]]

## Facets

**domain** [[labor_employment]]
**user** [[government_staff]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]
  <sub>weak: regulation_legal_text</sub>

**stack** api, arduino, azure, azure-function, postman, python, raspberry-pi, react, tensorflow

## How they structured the write-up

- hardware tested with the api
- devices tested with the webapp
- we actually tested it in working businesses
- references

## Body

High level view Hardware Mobile Browser In a business In another business Welcome COVID-19 has changed our daily lives and continues to do so. Many retail stores and companies have gone out of business, unable to offer their services to their clients. However some others which have opted for the reopening of their businesses in turn have had to adapt to the times.This includes public institutions such as museums, libraries, etc. All these establishments have taken their precautionary measures, generating new regulations, such as forcing customers and / or visitors to wear face masks at all times (1). Given this new environment, businesses have had to create neew kinds of jobs or jobs to be done. One of these is to check the use of the mask and check the temperature of the customers before entering the establishment, risking not only the worker who is checking the temperature of the customers, but to the customers who enter the place. https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/when-and-how-to-use-masks?gclid=Cj0KCQjwlvT8BRDeARIsAACRFiX_NyUiqU0d44aUqMNK7LVrXMOQWMfqr0MUUo8TKrJLpObf91qRUcUaAjKbEALw_wcB Problem This job generates an annual cost per worker of at least $30,000 [1] and if that employee were to become ill with covid-19, by law (in the United States) they would have to pay him at least $511 a day [2]. These costs (both moneetary and health wise) for an employee who performs a repetitive task is excessive but necessary, because the solutions currently created are not yet sufficient to replace this position. The Xovis all-in-one solution - https://www.xovis.com/en/products/detail/face-mask-detection/ Only detection of the use of face masks, without temperature measurement, or access control. SecurOS™ Face Mask Detection - https://issivs.com/facemask/ Only detection of the use of face masks, without temperature measurement, or access control. Leewayhertz - https://www.leewayhertz.com/face-mask-detection-system/ Only detection of the use of face masks, without temperature measurement, or access control. Most of the devices on the market only detect the use of the mask, however this project seeks to generate a complete solution for access control. https://www.ziprecruiter.com/Salaries/Retail-Security-Officer-Salary https://www.dol.gov/sites/dolgov/files/WHD/posters/FFCRA_Poster_WH1422_Non-Federal.pdf Solution Connection Diagram AzureML Model Training For step by step instructions on how we set up this environment go this Github link: https://github.com/altaga/Azure-Facemask-Detector#azureml-model-training Azure API implementation Thanks to the fact that it is a service that can be consumed by API, we can practically use any HW or SW device to perform the implementation. In this case, we can show how we carry out this implementation in the following devices and platforms. Hardware Tested with the API Code: https://github.com/altaga/Azure-Facemask-Detector/tree/main/Devices%20Tested ESP32 Cam Video (Demo ESP32): Click on the image RPI4 with Camera Video (Demo Raspberry): Click on the image Devices Tested with the webapp WebpageCode: (The web page consumes directly from the same API, you can test the web page yourself in the following link): Web App Tested: https://polite-bush-0d957ae10.azurestaticapps.net/ Samsung Galaxy S10+ iPhone Desktop Video (Demo Smartphone): Click on the image Video (Demo Desktop): Click on the image Final Implemetations WE ACTUALLY TESTED IT IN WORKING BUSINESSES Icecream Shop: Make Up Shop: DEMO Video: Click on the image Closing The final PoC offers an alternative for access control for several kinds of businesses. This is a problem that nowadays affects everyone and will do for the near future. Most experts are expecting this kind of measures to be necessary for the foreseeable future. It is true that the vaccines have started to roll out, but for herd immunity and its effects to take place, it will take a couple years if not more. The problem of access control to businesses and institutions has to be automated without question, we have shown to have the proper technology to accomplish this and it should be done via creative use of bleeding edge technology such as the application here presented. Thank you for reading and supporting the project. References (1) https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/when-and-how-to-use-masks?gclid=Cj0KCQjwlvT8BRDeARIsAACRFiX_NyUiqU0d44aUqMNK7LVrXMOQWMfqr0MUUo8TKrJLpObf91qRUcUaAjKbEALw_wcB (2) https://www.dol.gov/sites/dolgov/files/WHD/posters/FFCRA_Poster_WH1422_Non-Federal.pdf (3) https://www.ziprecruiter.com/Salaries/Retail-Security-Officer-Salary (4) https://www.cdc.gov/coronavirus/2019-ncov/downloads/COVID-19_CAREKit_ENG.pdf <div