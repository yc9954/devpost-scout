---
slug: "covid-19-medical-justice"
url: "https://devpost.com/software/covid-19-medical-justice"
title: "Access and Equity: Health Vulnerability Mapper COVID-19"
hackathon: "AWS Data Exchange Challenge"
organization: "Amazon"
winner: true
words: 794
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Access and Equity: Health Vulnerability Mapper COVID-19

> We’re presenting an interactive map-based web application that highlights the relationships between socioeconomic disparity and COVID-19 across the U.S. in an intuitive, real-time, & tangible medium.

[Devpost](https://devpost.com/software/covid-19-medical-justice) · hackathon [[AWS Data Exchange Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[education]] [[security_privacy]] [[transportation]]
**user** [[educator_student]] [[general_public]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]
  <sub>weak: code_repository</sub>

**stack** amazon-cloud9, amazon-cloudwatch, amazon-ec2, amazon-elastic-beanstalk, amazon-lambda, amazon-web-services, animate.js, bootstrap, c3.js, d3.js, express.js, javascript, mapbox-gl-js, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the covid-19 health vulnerability mapper

## Body

Explore a whole range of social vulnerability and COVID-19 metrics and see the map dynamically change to reflect new correlations. Explore analytics and visualizations about each county and the relationship between disparity and COVID-19. All COVID-19 data updated daily. Search for any county, whether your own or across the country. As student activists ourselves, we recognize the severity of these issues and the timeliness of change. To help out, we’ve compiled a repository of resources to address health inequality in communities like McKinley & countless others. The COVID-19 Health Vulnerability Mapper – for the explorer and change maker in all of us. http://covid.shawsean.com/ Inspiration The idea for the Health Vulnerability Mapper was motivated by the apparent link between socioeconomic disparity and susceptibility to the COVID-19 pandemic in the United States. While there has been an abundance of media attention surrounding social disparity during this pandemic, we saw a lack of data-driven and interactive geographic tools that show people how this issue really plays out on the national stage. What it does The Health Vulnerability Mapper presents an easy and engaging way of exploring up-to-date COVID-19 data while directly visualizing the health disparities found in different communities. Once launched, the web app displays a 3D map of the US, with each county represented by a vertical bar whose height corresponds to the selected COVID metric (updated daily through AWS) and whose color corresponds to the selected vulnerability metric. The vulnerability statistics are based off of the CDC’s Social Vulnerability Index (SVI) and include census variables like income, demographic composition, and minority status, by percentile and percent. We’ve also included measurements like high school graduation rate and vehicle ownership, some of which have surprising correlations with COVID-19. By searching for a county, or by clicking on one of the bars on the map, users can access information about that county including its social vulnerability, its current COVID status, the relationship between these two metrics, and how both of these values compare to the rest of the county. All counties also include visualizations showing the frequency of mask use among its residents. How we built it We created the Health Vulnerability Mapper using several powerful technologies offered by AWS and relevant libraries. Our COVID statistics are updated daily from AWS Data Exchange, where we’ve leveraged every datapoint in the Enigma Daily COVID-19 U.S. Counties database. We used AWS Cloudwatch and Lambda to provide automated processing for the 400,000 lines of data we retrieve each day which we store through S3 and deliver to the user through our Elastic Beanstalk server. The final visualization is then powered through Mapbox and C3.JS. Challenges we ran into One of the major challenges we ran into while creating the web app was tied to data processing. Specifically, the two main datasets that we used -- the Enigma COVID database and the SVI dataset -- had different county organizations. To solve this issue, we ultimately had to write programs to pre-sort the datasets by county FIPS code and cross-check each line of data to get the corresponding COVID and SVI values for each county. Other challenges arose in designing an intuitive display and debugging the S3 automation process. Accomplishments that we're proud of As new college students, we undoubtedly faced challenges while harnessing technologies we hadn’t had much experience with before. For some of us, this was our first time using AWS services. Yet together, we managed to construct an interactive, real-time web app, complete with statistical visualizations and related resources. We’re proud of the individual successes, like finally getting a feature to work or finding a relevant dataset, but most of all, we’re proud to have a valuable tool to contribute to the evolving conversation surrounding social disparity and COVID-19. What we learned From a technical perspective, our team learned a lot about using AWS services and web development both on the front-end and back-end. From a teamwork perspective, we also learned quite a bit about leveraging the synchronous capabilities of AWS Cloud9 to work more effectively. From a data perspective, we found several important relationships between the SVI and COVID metrics. We found significant positive correlations between expected metrics like demographics, socioeconomic situation, living circumstance, and poverty – and more surprisingly, we also found trends between less obvious variables like vehicle ownership and education. What's next for The COVID-19 Health Vulnerability Mapper Going forward, we’re excited to use our tool to partner with nonprofits, county governments, and other organizations to identify and develop solutions for health inequity. To this end, we’re in the works of adding more analytical features, such as a time series illustrating COVID data over time. We’re also working on incorporating COVID and vulnerability data from multiple countries to expand our reach to a global scale. <div