---
slug: "aquila-24osbt"
url: "https://devpost.com/software/aquila-24osbt"
title: "Aquila"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 375
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Aquila

> parametric forest fire insurance using Chainlink oracles

[Devpost](https://devpost.com/software/aquila-24osbt) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[agriculture_food]] [[finance_payments]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** amazon-web-services, moralis, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aquila

## Body

Inspiration heard Sergey mention forest fires in an insurance talk.. thought that was an interesting use case. I moved to BC ~1 year ago, and in August I noticed the effects of forest fire smoke rolling into my town :( I understood the severity of the problem and how devastating the effects were first hand. Then I connected the dots on how the application had a binary trigger point, by comparing satellite images of the fires against protected farm areas. What it does parametric forest fire insurance using Chainlink oracles. Aquila automates forest fire insurance claims through data driven (parametric) insurance How we built it we did not have an API for our data source, only a file. so we had to build the code to download, convert, and project the KML file for us. Then we needed a way to do the comparison of coordinates of fires/farms, so for that we utilized pre existing turf libraries (point vs poly and poly vs poly). Then we needed to get the data on-chain into our contract, for which we used Chainlink Challenges we ran into ran into some difficulties with creating the http get call.. had to edit the lambda to accept string, not array, and the 0.10.15 node expecting another format than we send to it from the adapter. needed to format the output from the api Accomplishments that we're proud of super proud of our amazing team, who put in countless hours of effort, was collaborative and knowledgable, and overall were sublime to work with What we learned we learned a lots along the way, such as using Moralis which none of us had worked with before, and integrating our front-end with backend using web3.js + Moralis. We were able to share skills, and understanding in different areas that we were individually good at.. e.g. myself explaining the adapter side of things and general idea, Hicham and Chuck sharing their vast knowledge of solidity, Anna sharing her skills in front-end. What's next for Aquila Our goal is to launch the first fully regulatory compliant forest fire insurance product in BC Canada, as well as expand to other parts of the world. To accomplish this we would like to partner with an open-insurance protocol <div