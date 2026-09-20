---
slug: "around-nq3uhv"
url: "https://devpost.com/software/around-nq3uhv"
title: "ARound"
hackathon: "ARCore Geospatial API Challenge"
organization: "Google"
winner: true
words: 588
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ARound

> GPT-trained location-based virtual tour guide.

[Devpost](https://devpost.com/software/around-nq3uhv) · hackathon [[ARCore Geospatial API Challenge]]

## Facets

**domain** [[transportation]]
**substrate** [[geospatial]] [[video_visual]]

**stack** arcore, googlemapapi, node.js, openai, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for around

## Body

Inspiration Our mobile app was inspired by the new mode of travel emerging post-COVID, where less human contact is desired. We aimed to provide a contactless and safe solution for travelers through a virtual tour guide powered by AR and AI technology. Our goal is to make local discovery easy and fun while being safe What it does Our mobile app features a GPT-trained chatbot as a virtual tour guide, which appears in an AR mode when users open the app. The tour guide is location-based and works globally, introducing the area and providing information about nearby spots to discover. The app also has a backend connection where administrator users can manage and update the spots through a CMS. How we built it Our mobile app is built using Unity and the ARCore Geospatial API to manage location-based AR anchors. The chatbot feature is powered by OpenAI API and fine-tuned with location and tourism context. The training data for the chatbot was gathered from text descriptions of spots entered by users in the CMS, as well as web scraping for tourism conversational dialogue. We also utilized the Google Maps Reverse Geocoding API to retrieve human-readable addresses. The system architecture and user flow works as follows: To train the GPT model for answering questions in a tourism context, conversational data is scraped and manufactured behind the scenes. Administrator users input spot information such as latitude, longitude, and descriptions into the CMS. When end users open the mobile app, their current location is determined and nearby spots are displayed by querying the backend server. The chatbot is also initialized with location context. End users can engage in general conversation with the chatbot and also click on AR anchors for more information. Challenges we ran into Improving the development cycle is definitely challenging. Just like developing any mobile AR applications, figuring out an effective way to test it without the need to build and deploy to a mobile device is crucial. The Geospatial API is indeed pretty straight forward and easy to use, but testing it is a tough one especially when we are sitting in front of the computer in the office. Later on, we figured out a trick to trigger the anchors by faking devices' GPS location as well as showing google street view images in the monitor. Accomplishments that we're proud of One of our main achievements was to create a seamless and intuitive user experience that combines AR and AI technology. The virtual tour guide provided by the GPT-powered chatbot was able to provide accurate and relevant information about nearby spots and was able to engage in a natural conversation with users. What we learned Throughout the hackathon, we had the opportunity to learn and work with two powerful technologies, ARCore Geospatial API and GPT. With ARCore, we learnt how to create and manage location-based AR anchors. With GPT, we learnt how to fine-tune the language model for specific use cases, and how to integrate it into the mobile app to provide a virtual tour guide. We also learnt how to scrape and manufacture conversational data to train the model. What's next for ARound Our next steps for the app include adding a navigation feature to guide users to different locations and explore the cities. Integrating more data sources such as weather and traffic data to provide more comprehensive information for users. We also plan to improve the GPT-powered chatbot by incorporating more conversational data and fine-tuning the model for a more natural and engaging experience. <div