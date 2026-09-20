---
slug: "covid-inc"
url: "https://devpost.com/software/covid-inc"
title: "COVID Inc."
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 622
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# COVID Inc.

> Helping people understand COVID-19 by drawing parallels to the popular video game, Plague Inc.

[Devpost](https://devpost.com/software/covid-inc) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[health_clinical]]
**user** [[general_public]]
**substrate** [[geospatial]] [[structured_db]]

**stack** amazon-web-services, beautiful-soup, express.js, node.js, postgresql, python, selenium, socket.io

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for covid inc.

## Body

Close up of Europe News for March 24th Inspiration When we were trying to stay up-to-date with COVID-19, we found it really difficult to build a coherent picture of what’s going on because the numbers are changing so fast: the numbers yesterday might be completely different from the numbers today, which is what we'd expect from exponential growth. We came across a lot of data -- detailed breakdowns of cases per country, trendlines, and maps visualizing the current situation -- but we found it particularly difficult to draw relationships between the outbreak status today and, say, a week ago. This is a huge problem, as information is arguably the strongest weapon we have against this epidemic - keeping the public updated with easily-digestible information is critical to preventing the spread and flattening the curve worldwide. We wanted to provide the general public with the most intuitive interface that allows them to determine the current situation of the outbreak with nothing more than a glance. We thought about multiple ways to do this, and settled upon an interface everyone was familiar with: Plague Inc. What it does COVID Inc. is an interactive world map that allows you to track the outbreak since it was first discovered. The app provides an up-to-date visualization of total, new, active, recovered, and fatal cases per country. Using the controls on the top right, you can see the outbreak at different points in time and the news for that day. Clicking on the news bar will reveal a more detailed view of the news, with more detailed descriptions. How we built it For our data, we used BeautifulSoup and Selenium to scrape time-series data from Worldometers and Pharmaceutical Technology , and stored it on a PostgreSQL database hosted on Amazon RDS . We built REST API endpoints using AWS Lambda , which we then queried from a Node.js (Express) backend that communicates to the client using socket.io . We then deployed it on a VPS, setting up cronjobs to automate the data collection. The front-end is built on top of svgMap , which we customized to suit our needs. Challenges we ran into On the front-end side of things, making maps turned out to be very difficult!!! We ran into a lot of issues when setting up different layers for topography, color overlays, and data points. Getting zooming and panning to work and keeping the map mobile-friendly was also a challenge. On the back-end, scraping data proved to be a challenge as the layout of the site may change over time. We had to create multiple checks and tune the parameters accordingly. Accomplishments that we're proud of We're proud that we managed to find time and energy to work on such a project given the ongoing chaos. We had a lot of fun building the map, and we're especially proud of overcoming the technical challenges we faced and creating a project that has an impact on society. What we learned We learned a lot about designing for scalability: how to store and retrieve information efficiently from a relational database, how to utilize AWS as an infrastructure, and how to set-up pipelines for deployment, monitoring, and analytics. It was also our first times experimenting with cool algorithms like using ray-casting to display data points. What's next for COVID Inc. Our main goal is to get the site in the hands of the public as that's why we created this project in the first place. We're also planning to build two more tabs: one for disease info, to visualize the symptoms of the disease and its transmission factors, and the other for cure progression, which estimates the current progress on a cure and provides news on breakthroughs and initiatives. <div