---
slug: "polis-ai"
url: "https://devpost.com/software/polis-ai"
title: "Polis AI"
hackathon: "MEGA Hackathon 2026"
organization: "MegaHackathonLeague"
winner: true
words: 733
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "substrate/sensor_telemetry"
---

# Polis AI

> A simulation platform that uses AI to model and analyze urban planning strategies

[Devpost](https://devpost.com/software/polis-ai) · hackathon [[MEGA Hackathon 2026]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[civic_government]] [[climate_energy]] [[developer_tools]]
**substrate** [[sensor_telemetry]]

**stack** next.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for polis ai

## Body

Logo Dashboard Inspiration Polis AI was inspired the En-Roads Climate Simulator and its ability to model various climate policies. Polis extends this concept to urban planning as a whole and incorportates AI to offer personlized advising to help real-world cities design their agendas. There are over 30 policies Polis can simulate, with each one being configurable to different budgets and timeframes. What it does Policy Simulation Polis uses a prediction engine to simulate the effects of a wide range urban policies on 4 core factors: Sustainability, Governence, Fiscal Stability and Public Approval. Polis predicts a number of metrics within these categories to over a comprehensive overview of how polcies affect a city as a whole. Visual Models The Polis Dashboard displays a variety of different statistics to offer a thorough overview of cities. It offers dyanmic graphs of key metrics such as the Carbon Dioxide level or Debt-to-GDP ratio of cities of time. Polis also shows exactly how each policy affects different statistics over time, offering in depth analysis of a city in an easy to understand format. AI Advisor Polis also includes an AI advisor that can offer insight on urban agendas. Users can have the AI analyze their policies and get personalized feedback on the strengths and weaknesses of the plan. Futhermore, Polis's AI is agentic, making it able to design its own agendas based off the goals of the user. By simpling outline the targets of the city, the AI will create a custom set of policies to meet those goals as best as possilbe. By working with the AI to refine and optimize policies, Polis is able to help governments design ideal urban agendas that best fit their goals. How we built it Polis is built using Next.js to deliver a responsive, intuitive frontend. The backend is written in typescript, using non-linear equations to create an accurate prediction engine that can model the impacts of different policies. Polis also uses the OpenAI SDK to communicate with the Featherless API for all AI related queries using GLM-5, the best open-source model currently available. Challenges we ran into The hardest part of the project was the prediction engine. We read thoroughly into the documentation of the En-ROADS model to design an algorithm that could accurately model the impacts of different policies. While some we were able to implement fairly easily as the were generally linear, we looked at a lot of real world data to design equations for certain policies that did not scale linearly with budget and/or touched on a variety of factors. Accomplishments that we're proud of The prediction engine we designed is the most impressive aspect of our project. It is able to model a large range of urban policies extremely accurately and effectively predict how their impacts scale with budget allocation. The engine is also very strong at estimating the diminshing marginal benefits of overlapping policies and does not simply add them up, instead evaluating the agenda as a whole to offer precise and thorough predictions. Although not 100% accurate to the real world, it provides a powerful simulation that can aid in offering insight to city governments and officials before enacting policies. What we learned We learned a lot about the working of Next.js and also some of the complicated modeling that goes into prediction models. We also learned much about proper UI design and how to balance intuitiveness with functionality to create a project that is both understandable and useful. What's next for Polis AI Improved City Support Polis currently supports 20 different cities that it can comprehensively simulate. However, in the future, we hope to add the ability to input custom parameters of the intial conditions of a city so that users and governments from around the world can use Polis to aid in their own urban planning. Language Support In line with Polis's goal as a global tool, adding support for additional languages beyond english will enable people from around the world to access and use Polis technology. Improved Model Although currently rather accurate, the prediction engine can make mistakes when trying to simulate policies with a very long timeframe. We hope to continue to fine tune and work on the engine, in conjuction with potential open source contributions, to improve the accuracy and precision of our model to allow to reach its potential as a real world tool for urban policy. <div