---
slug: "lighting-prediction-in-india-using-ml"
url: "https://devpost.com/software/lighting-prediction-in-india-using-ml"
title: "Thunderstorm Prediction using ML"
hackathon: "AWS Disaster Response Hackathon"
organization: "Amazon"
winner: true
words: 814
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "substrate/structured_db"
---

# Thunderstorm Prediction using ML

> By finding correlations between the atmospheric conditions at the time of the lightning strike, we were able to predict the occurrence of lightning and thunderstorms.

[Devpost](https://devpost.com/software/lighting-prediction-in-india-using-ml) · hackathon [[AWS Disaster Response Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[civic_government]] [[climate_energy]] [[disaster_emergency]]
**substrate** [[structured_db]]

**stack** pandas, python, sagemaker, sci-kit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for thunderstorm prediction using ml

## Body

Inspiration Lightning claims about 24,000 lives and injures 240,000 people globally every year. Inspite of being a leading cause of fatalities, there is a paucity of work on prediction of lightning to help save lives. Therefore, thunderstorms were chosen as the focal area for predicting disaster response. In order to do this, a team from various domains was brought together to work on the complex phenomenon of lightning. What it does Historical Data was collected over the years from open sources for wind-speed, wind direction, temperature, precipitation and humidity from Northern and Southern India and parts of the USA. Part of historical data was used to create the predictive model while the remainder of the data was used to validate the model (70/30). By recording and correlating the atmospheric conditions at the time of lightning strikes during thunderstorms, our Machine Learning Model predicts whether a dangerous lightning strike will occur within the next 3 hours. How we built it Initially, we focused on 12 districts of Northern India which reported a high frequency of lightning strikes. Referring to various global weather agencies, it was possible to isolate atmospheric conditions such as relative humidity, wind speed, wind direction, temperature, and precipitation of that location within a certain time frame. From Lightning Imaging Sensor (LIS), we were able to extract the time and frequency of lightning strikes within our specified time frame using open public sources. The temperature and pressure conditions on days of frequent instances of lightning were extracted. The problem was converted into binary classification by setting a threshold of 50 (0- not dangerous storm, 1 -dangerous storm). Exploratory data analysis showed a strong correlation between various factors followed by using an SVM Classification model giving us the highest accuracy as compared to four other models we validated. Challenges we ran into One of the main challenges was to find and collect clean and relevant datasets across parameters in the same time frame. The dangerous lightning strikes (encoded as 1) represented only 0.03%, leading to a biased dataset. To combat this, we first worked on one district alone, incrementally building the final model. Accomplishments that we're proud of Searching through repositories of datasets to find numerical data capable of being processed was time-consuming work, however, with due diligence and perseverance, we finally arrived upon exactly what we required. Sorting through the data was an exhaustive and intensive process. It took deliberation and discussion to segment and filter through years of comprehensive data to obtain the relationship between lightning-prone areas across the world and taking on board information from various domains of study. The generic model developed can be utilized for prediction of thunderstorms in other geographies. We have validated the results for Florida, USA, San Diego California, USA, Idukki, Kerala, India and 12 other districts in Northern and North East India with fairly good accuracy. We were able to explain the occurrence of lightning through mathematical machine learning models in these regions with relevant literature and understanding. This study gives ample time to people to communicate (three hours) so that they can move to safer places. What we learned If we want to increase our accuracy further, we need to lower our constraint for the number of flashes per hour. But that will take away the intensity of lightning which causes the disaster. An opportunity to test the model in different disaster situations and can be used as a prototype to predict future disasters. Learning to work together with people from different domains. Learning to work with ‘Sagemaker studio Lab’ from AWS, a very simple and user-friendly platform to run the machine learning models. Research and acquire the relevant open-source data. What's next for Thunderstorm Prediction using ML In the future, we hope to collaborate with various government and non-government agencies globally, to help mitigate the impact of disasters and aid in disaster risk reduction (DRR). We hope to incorporate real-time data and enable timely evacuation thus saving lives. Reducing fatalities will go a long way in saving precious lives and the biodiversity at large. The results provide us opportunities to scale up the model to other geographies and test the efficacy in other disaster contexts effectively helping us save many more lives. The model can also be made available for commercial use for wider dissemination. References: Global Hydrology Resource Center (2022, January 27). LIS Space Time Domain Search Holle, R. L. (2008). Annual rates of lightning fatalities by country [Paper presentation]. 20th International Lightning Detection Conference, Arizona, USA. Indian Meteorological Department (2022, January 27). IMD Kerala State Disaster Management Authority (2022, January 27). Kerala State Disaster Management Authority Shi, Z., Tan, Y., Liu, Y., Liu, J., Lin, X., Wang, M. and Luan, J., 2018. Effects of relative humidity on electrification and lightning discharges in thunderstorms. Terrestrial, Atmospheric & Oceanic Sciences, 29 (6). Uttar Pradesh State Disaster Management Authority (2022, January 27). UPSDMA <div