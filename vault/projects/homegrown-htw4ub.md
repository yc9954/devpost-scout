---
slug: "homegrown-htw4ub"
url: "https://devpost.com/software/homegrown-htw4ub"
title: "homegrown"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 528
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/structured_db"
---

# homegrown

> Every thought of growing your own plants? Start now! homegrown lets you grow your own mini garden from the comfort of your own phone (✿◠‿◠) 🪴🥬🥒 (｡◕‿◕｡)

[Devpost](https://devpost.com/software/homegrown-htw4ub) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[sensor_fusion]]
  <sub>weak: legal_professional</sub>
**substrate** [[structured_db]]

**stack** arduino, github, json, python, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for homegrown

## Body

The prototype we pitched to the judges Inspiration With the world producing more waste then ever recorded, sustainability has become a very important topic of discussion. Whether that be social, environmental, or economic, sustainability has become a key factor in how we design products and how we plan for the future. Especially during the pandemic, we turned to becoming more efficient and resourceful with what we had at home. Thats where home gardens come in. Many started home gardens as a hobby or a cool way to grow your own food from the comfort of your own home. However, with the pandemic slowly coming to a close, many may no longer have the time to micromanage their plants, and those who are interested in starting this hobby may not have the patience. Enter homegrown , an easy way for people anyone interested in starting their own mini garden to manage their plants and enjoy the pleasures of gardening. What it does homegrown monitors each individual plant, adjusted depending on the type of plant. Equipped with different sensors, homegrown monitors the plants health, whether that's it's exposure to light, moisture, or temperature. When it detects fluctuations in these levels, homegrown sends a text to the owner, alerting them about the plants condition and suggesting changes to alleviate these problems. How we built it homegrown was build using python, an arduino, and other hardware components. The different sensors connected to the arduino take different measurements and record them. They are then sent as one json file to the python script where they data is then further parsed and sent by text to the user through the twilio api. Challenges we ran into We originally planned on using CockroachDB as a data based but scrapped idea since dealing with initializing the database and trying to extract data out of it proved to be too difficult. We ended up using an arduino instead to send the data directly to a python script that would handle the data. Furthermore, ideation took quite a while because it was all out first times meeting each other. Accomplishments that we're proud of Forming a team when we've all never met and have limited experience and still building something in the end was something that brought together each of our respective skills is something that we're proud of. Combining hardware and software was a first for some of us so we're proud of adapting quickly to cater to each others strengths What we learned We learned more about python and its various libraries to build on each other and create more and more complex programs. We also learned about how different hardware components can interact with software components to increase functionality and allow for more possibilities. What's next for homegrown homegrown has the possibility to grow bigger, not only in terms of the number of plants which it can monitor growth for, but also the amount of data if can take in surrounding the plant. With more data comes more functionality which allows for more thorough analysis of the plant's conditions to provide a better and more efficient growing experience for the plant and the user. <div