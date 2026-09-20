---
slug: "pandemic-spread-simulator-pass"
url: "https://devpost.com/software/pandemic-spread-simulator-pass"
title: "Pandemic Spread Simulator - PaSS"
hackathon: "Pandemic Response Hackathon"
organization: "Datavant"
winner: true
words: 733
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/labor_employment"
---

# Pandemic Spread Simulator - PaSS

> Web-based interactive virus communal spread simulation where you can adjust parameters such as virulence and shelter-in-place compliance to see the spread of the virus over time

[Devpost](https://devpost.com/software/pandemic-spread-simulator-pass) · hackathon [[Pandemic Response Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[health_clinical]] [[housing_homeless]] [[labor_employment]]
  <sub>weak: video_visual, web_dom</sub>

**stack** amazon-web-services, canvas.js, css, easljs, font-awesome, html, javascript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for pandemic spread simulator - pass

## Body

Screenshot of app Inspiration Stories inspire us and right now all of us are consumed with the COVID-19 story. But we all have different experiences and understandings of what we are going through. We had a different awareness of the severity of the pandemic than our friends in other places. We wanted to help visualize what it means to shelter in place and why it is important. What it does It models human behavior regarding sheltering during a pandemic in a simulated city. We want people to be able to create their own simulations. While it is not perfect, it solves our core mission - to get people thinking more seriously about shelter in place. How I built it Very quickly. It was definitely a team effort with lots of long hours. We started by trying to model basic human behaviour. We knew not everyone had the same tendencies to leave home, so we focused on a couple of key items - are they ill, an essential worker, and do they tend to follow rules like Shelter in place or are they a "rebel". We also took into account how strict the shelter rules were in the community, from no rules to marshall law. We used standard HTML5 stacks (all front end) served on our AWS s3 account. We used easljs for our animations and canvas library as well as canvas.js for our charts. And a shout out to font-awesome for free covid-19 icons. We researched human behavior and current available data regarding the spread and progression of the virus and illness. While we did our best with the data, we made sure that the user was able to change the settings. Challenges I ran into Not enough time. There never is. Right now we are all trying to understanding all of the factors in play and we had to dive deep into the science of the pandemic to try to simulate what we are all experiencing. Interpreting the data was a challenge. There are a lot of different values and not a single a source of truth. We are all trying to figure out this stuff at the same time. We really wanted to make this interactive AND scientifically accurate, and 72 hours is not quite enough time, but we are hopeful for the future. Accomplishments that I'm proud of "I learned JavaScript" - Sarah. This was a great opportunity for us to grow skills that we usually rely on others to help us with. And the model works! That was the most exciting to see our idea come to light even when we thought the obstacles were high. What I learned We have created other simulators and models before for clients and thought we could apply what we knew to the COVID crisis. While our backgrounds helped, it was sobering to start to dig into the complexities. "It was hard to create the simulation and test it by killing simulated people over and over. That was a surprise for me since it is just a computer program." - JT What's next for Pandemic Spread Simulator - PaSS Where do we want to go. First we would love to get a better UX and design. We would also like to get better data for our parameters, maybe have some pre-loaded templates and be able to save and share simulations. We would like to work on some more variable factors too and tighten up the algorithms a bit. We would like a better understanding of epidemiology and have a domain expert help us with the next version of our tool. We would like to include how an overwhelmed hospital effects the severity of the illness and the chance of survival. We would like to see it on a larger scale and learn from users what they like/dislike and what they may have learned. We would also like to create a World View. Each instance of the web simulation would report the results in real time to a centralized location. A World View would be able to show active simulations from others and maybe even allow for populations to mix. That part is actually pretty easy as we have built similar models before. We would like to be able to load presets for different parts of the world and APIs into real-time environments. It could highlight access to health care and other resources. <div