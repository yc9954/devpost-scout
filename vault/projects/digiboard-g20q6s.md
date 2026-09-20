---
slug: "digiboard-g20q6s"
url: "https://devpost.com/software/digiboard-g20q6s"
title: "TARP - Target. Advertise. Revolutionalise. Promote."
hackathon: "Hack the North 2019"
winner: true
words: 603
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# TARP - Target. Advertise. Revolutionalise. Promote.

> Bringing user targeted advertisements via offline mechanism - Our technology benefits both advertisers and the viewers. It displays what the viewers want to see, and to whom advertisers want to reach.

[Devpost](https://devpost.com/software/digiboard-g20q6s) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
  <sub>weak: cross_origin_web</sub>
**domain** [[finance_payments]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** azure, azure-iot-suite, css, facebook-login-api, firebase, google-cloud, html, matplotlib, python, realtime-data, td

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tarp - target. advertise. revolutionalise. promote.

## Body

Advertisers' Portal JSON Data of Azure Cognitive Services Face API 4D Plots (5 Advertisements on LHS and 2 Centroids of Viewing Population i.e. 2 Billboards on RHS). Ads distribution on billboards. Image Output of Azure Cognitive Services Face API Firebase Realtime Database Payment Page using TD Da Vinci Payment API Login Page to Advertisers' Portal using Facebook Login API Inspiration Offline advertisements are random and passive in nature, thus both the viewers and advertisers are at a loss. No one wishes to view advertisements that are not meant for them. Moreover, we spend most of out time walking on streets, driving on roads, roaming around in malls, visiting cafes and restaurants - Digital Boards showcasing advertisements are present almost everywhere. Thus, there is an immense need of intelligent advertising on offline mechanisms. What it does It collects demographics of the viewing population via an image sensor, then it uses a matching algorithm to match the advertisements to display boards maximising user targeting and user suitability. The demographics taken into consideration at the moment are - gender, age group and eye moment to ensure long eye contact. The advertisements form a queue infront of each display board and are then displayed on the basis on realtime estimates via geometry and cost minimisation. How we built it PART - 1 : (Board to Advertisements) Matching and Queuing Technology Camera on Offline Advertising Spots generates the demographics of the viewing audience using Azure Cognitive Services Face API JSON Data obtained is processed, centroid of viewing population for each billboard is estimated. These Centroids are maintained in Firebase Realtime Database. Advertisements and Billboard Centroids are plotted on 4 Dimensional Graph and each advertisement searches for the nearest billboard and enters its queue. PART - 2 : Advertisers' Portal Login is done via Facebook Login API Advertisers can check the following details : Viewership Display Time of their Advertisements Amount Spent Relevant Viewership Advertisers can make Payments for future display of advertisements via the payment page. Payment Page uses TD Da Vinci API for Transfer of Funds Challenges we ran into The first challenge was to decide the factors that are prevalent for user targeting advertising. The demographic factors had to be streamlined to three for present working. Moreover, these factors were then processed via Microsoft Azure Cognitive Services Face API Handling Realtime databases is a tiring task, but Firebase Realtime Database simplified the process. Payment and User Login are considered to be very time consuming development tasks, usage of Facebook Login API and TD Payment API came to our rescue with these challenges. Accomplishments that we're proud of We are proud to share that TARP is capable of displaying user targeted advertisements to the most accurate viewing strata of population in realtime. Moreover, it ensures that advertisers pay a fair price as costing is based on display time of advertisements ( of highest priority level), Percentage of Interested Relevant Audience along with multipliers based on average footfall. What we learned We learnt how to approach critical problem statements in a structured manner and consider all the edge cases. We solved challenges that may arise in real time scenarios. We worked with the aim to make our solution on offline user-targeted advertising scalable and efficient. We adopted a business model that can bring stability to the dynamic pricing of offline advertising industry. What's next for TARP - Target. Advertise. Revolutionalise. Promote. Next TARP would be processing high quality realtime videos and optimise the time efficiency. Moreover, the factors that segregate viewership preferences can be enhanced by including financial status of the viewers, expression towards the advertisement etc. <div