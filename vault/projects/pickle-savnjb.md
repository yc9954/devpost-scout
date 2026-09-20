---
slug: "pickle-savnjb"
url: "https://devpost.com/software/pickle-savnjb"
title: "Pickle"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 484
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Pickle

> An intelligent group-travel assistant that uses over 300 travel attributes to find the group's next big destination

[Devpost](https://devpost.com/software/pickle-savnjb) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**substrate** [[structured_db]] [[video_visual]]

**stack** amazon-web-services, android-studio, bottle, clarifai, flickr, instagram, python, sklearn, united

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pickle
- business specific model

## Body

Login Beach Recommendation City Recommendation Rating United Airlines Integration Inspiration Our good friend Lisa has been traveling every year for the past 5 years with her friends' group during the summers. As a group, they always have trouble deciding their next destination. Our app, Pickle, helps Lisa and her friends decide their next destination tailored to everyone's preferences. What it does Pickle personalizes and ranks the group's recommended destinations based on the Instagram feeds of the individual members. The application achieves this by identifying key themes and attributes from all the group's Instagram images and compares it with extensive destinations attributes available within our database. How we built it For the top United Airlines destinations, we identified and extracted the top 250 images from Flickr using their API. For these images, we then identified the top concepts (using relevance scores) using models on Clarifai (general and travel) and stored the results of this analysis in a database hosted on AWS. Whenever a new group is created, we used the Instagram APIs to get the individual users' images and identified the group's top concepts by running them against the Clarifai models. Using the top concepts from each of United's destinations previously calculated, and those of the user group, we created the test and training dataset which we subsequently used to create the group-specific model. As more users joined the group, the model continuously re-ranks all available destinations against the user images. Architecture: Challenges we ran into We underestimated the United's API's ease of use. It wasn’t possible for us to fully integrate United APIs in such a short timeframe -- from when we were given access, to the hackathon deadline. We had to limit the number of destinations (images) we could process through Clarifai, as there was a cap of 5000 requests per account. Our model would have been much more intelligent if we had gotten access to more operations on Clarifai. Accomplishments that we're proud of PICKLE! The MVP is a perfect app that helps anyone in a pickle decide their next vacation. We are proud of our predictive model generates precise travel destination recommendations based on personal preferences. What we learned We learned a ton! Technology-wise, most of the tools we used were outside our comfort zone -- learning to use these new tools was both challenging and fun. What's next for Pickle More Destinations : Expand to more destinations with a greater number of curated images that represent more diversity in activities, food, and scenery in each location. More Preferences : Add dislikes for each user so that the custom model ignores these preferences when ranking destinations Chat & Ranking : A better way to communicate within groups. Business Specific Model Travel sites/ Businesses/ Destinations can develop paid custom models specific to their designations/deals. Partner with airline companies to provide new UI for identifying great fares and destinations eg. United Airlines <div