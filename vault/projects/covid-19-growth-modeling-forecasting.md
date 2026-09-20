---
slug: "covid-19-growth-modeling-forecasting"
url: "https://devpost.com/software/covid-19-growth-modeling-forecasting"
title: "COVID-19 Forecasting"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 415
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "substrate/code_repository"
---

# COVID-19 Forecasting

> COVID-19 Growth Modeling/Forecasting with Logistic, Hill Equations and Prophet

[Devpost](https://devpost.com/software/covid-19-growth-modeling-forecasting) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**domain** [[health_clinical]] [[labor_employment]] [[supply_logistics]]
**user** [[patient_family]]
**substrate** [[code_repository]]

**stack** cloud, flask, javascript, numpy, oracle, pandas, prophet, python, scipy

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for covid-19 forecasting

## Body

COVID19 Forecast online app Inspiration COVID-19 is a hot topic these days. Healthcare workers are the first line of defense. If you are in IT you are part of the fight against the virus. I thought I should do my part and implement a method to forecast coronavirus growth and dates when the number of infections could stabilize. What it does The forecast is calculated daily based on the last available data, using logistic and Hill functions. Backtesting is done by forecasting for 5 days in the past. We provide a forecast for the next 20 days, along with backtesting data. Forecast helps to evaluate the situation and check how the country managing the virus outbreak. How we built it In the backend, we are calculating function parameters to describe virus cases growth in the given country. Using these parameters, future values are calculated. Backtesting is done following the same approach. Backtesting should inform how accurate the forecast is. If virus cases are above backtesting, it means the situation is getting worse. Otherwise, if a number of new cases is below the backtesting curve - this means a country is fighting virus effectively. We are using JavaScript to build UI, with the help of Oracle JET open-source toolkit for JavaScript development. The entire solution runs on top of Oracle Always Free Cloud tier. Data is fetched from public REST service. Challenges we ran into Initially, we implemented a forecast using a logistic function, but this approach wasn't accurate enough. In multiple scenarios, we saw that there could be a sudden increase or drop in new virus cases. It proved that the second approach we implemented with the Hill equation (another kind of logistic growth) could handle forecast with high ups/downs better. Accomplishments that we're proud of Application is live and we are receiving around 1000 API calls daily. Getting positive feedback through social networks. What we learned We learned that virus growth tends to follow the logistic curve. This made it possible to build a forecast app. Obviously the forecast could be adjusted if there will be sudden updates in new virus cases. Still, it gives a better understanding of the situation with the virus in each selected country. What's next for COVID-19 Forecasting We are planning to add a forecast correlation with the number of daily patient tests and the number of patients recovered daily. Source code : https://github.com/katanaml/covid19 Live app : https://app.katanaml.io/covid19/ Technical article I : https://bit.ly/2XHjL4P Technical article II : https://bit.ly/2RMB14V <div