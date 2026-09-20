---
slug: "ecopet"
url: "https://devpost.com/software/ecopet"
title: "ecoPets"
hackathon: "Junction 2017"
winner: true
words: 473
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/regulation_legal_text"
---

# ecoPets

> Create energy awareness && have fun with the ecoPets.

[Devpost](https://devpost.com/software/ecopet) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[sensor_fusion]]
**substrate** [[regulation_legal_text]]

**stack** android, elasticsearch, golang, ios, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next for ecopet

## Body

Inspiration Focusing on the future of energy, we think that it's really important that children understand more about electricity and, specially, how to save it. What it does EcoPet is a mobile-friendly game that helps kids to learn how to save energy by reducing their energy consumption. There is a point awarding criteria in order to evolve your ecoPet and buy them food, new clothes and accessories. We have considered different ways to achieve those points in the app, and the kids will be thrilled as the points are accumulated by playing, discovering and being challenged. The minigames within the app focuses on teaching a “green” mindset through fun challenges and activities, such as a recycling and matching challenge, a shower timer for shorter showers and also allows the player to accumulate points through calculating steps. How we built it First it was necessary to understand the data from Fortum API and realise how to use it in a way that the users find it thrilling. The model calculates the energy consumption of the house and by knowing the outside temperature, electricity used for heating can be calculated. The electricity consumed by heating systems was not considered, as we do not want kids to turn off radiators recklessly. We had to dive into the theory, get some data from Finnish regulation and make some assumptions to estimate heat energy usage. However, with more data, values of the heating losses and thermal mass for each household can be calculated more accurately. Location, time of the year, size of the house and number of inhabitants were important parameters to consider so that the model adapts to the different conditions present in each household. All the game graphics were hand drawn from scratch using Adobe Illustrator, so the design is 100% original. Challenges we ran into We had problems to understand the such called API from Fortum, which is nothing more than access to data files. So to make the data easier to read, we created an backend API with ElasticSearch that made it easier to collect the average power consumption in any interval. Accomplishments that we are proud of We created a fully completed concept of the game and the logic behind it. Our product is the best we built and the it will work if it’s finished. What we learned Working together in a small team of people from different countries and business areas. Cooperation between our different skills as for most of us, it was our first hackathon. What's next for ecoPet The app should connect to IoT devices to get data not only over the internet for electricity. We could get data from smart lights, water dispenser and other smart devices. The game could not just for teaching how to save energy, it can also be for teaching to live healthier. <div