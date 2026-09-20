---
slug: "pinboard_consulting"
url: "https://devpost.com/software/pinboard_consulting"
title: "TigerGraph for UN Data"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 1138
team_size: 6
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/education"
  - "domain/immigration_refugee"
  - "domain/media_journalism"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# TigerGraph for UN Data

> Connect the unconnected! Source, clean and load UN data for the environment, the economy, health, refugees, crops and more into a single graph and make it available for anyone to use.

[Devpost](https://devpost.com/software/pinboard_consulting) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[agriculture_food]] [[civic_government]] [[climate_energy]] [[education]] [[immigration_refugee]] [[media_journalism]] [[supply_logistics]]
**user** [[educator_student]] [[researcher]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** node.js, python, tigergraph

## How they structured the write-up

- the most amazing dataset in the world
- a tool for everyone
- the worst-best data in the world
- go big - go bigger - go biggest
- so proud - so nerdy
- the future
- appendix a: metrics

## Body

The Most Amazing Dataset in the World The United Nations collect and publish some of the most interesting, important, and relevant data in the world. Health, wealth, education, environment, tourism, pollution, demographics, crime, the list is almost endless; it is, however, very hard to use for data science, data analysis, journalism, teaching or research. ( http://data.un.org/ ) This is the core of our project, our challenge, and our submission: make this incredible resource accessible and easier to analyse for everyone on planet Earth using the power of TigerGraph! Never let it be said that we didn't aim high enough :-) A Tool For Everyone To meet our goal of making the UN data easier to access and easier to analyse we envision a tool in two parts: A graph database consisting of as many datasets as we can load, built in TigerGraph - the world's best graph database! A simple, web-based user interface which will allow people with no knowledge of graph or coding to be able to interact with, filter, download, and perform basic analysis on the UN data stored in our graph database. Having the UN data in a graph database will allow sophisticated users to perform deep graph analytics on the datasets: we see similiarity-analysis in particular as being a key area of graph investigation. Having a user friendly web front end will allow any user from any field to be able to see and interact with the data in a friendlier and more powerful way than the raw UN data website. The two-metric scatter plot in particular we hope will be a powerful, simple tool to enable non-technical users to instantly visualise their data-of-interest (see below). The Worst-Best Data in the World We knew before we started our build that the UN data was going to be hard to work with, but we didn't realise how hard. Each dataset had its own quirks, its own challenges and its own pitfalls - from missing years, to strange aggregations, to collapsed dimensions, to countries that no longer exist! But with some serious wrestling and wrangling we managed to get ourselves the most amazing set of data fully loaded, connected and available in TigerGraph: Total Vertices: 1,457,406 Years of data: 73 Countries: 259 Metric types: 729 Individual data points: 1,456,063 Total Edges: 15,441,320 We succeeded beyond what we thought was possible; just a small sample from our 729 metrics includes: Cause of death Crop yields Movement of refugees Homicide Pollution Tourism Childhood obesity Vaccination rates GDP Go Big - Go Bigger - Go Biggest We knew loading so many varied datasets would stretch TigerGraph, but we didn't anticipate just how much it would push the cloud servers! Like most entrants into this hackathon we started with the free instance, but as we loaded more and more datasets, and started to push the edge numbers higher and higher, we had to jump firstly to a larger instance with more RAM and more CPU, then finally to a much larger instance: Free: 2 vCPUS, 8GB RAM, 50GB Disk space Intermediate: 8 vCPUs, 32GB RAM. 128gb Disk space Current: 16 vCPUs, 128GB RAM. 366GB Disk space It was only when we got up to 128Gb of RAM that our interface between TigerGraph and the UI became stable and usable for all the different functions we wanted to be able to use - in particular the two metric, all country scatterplot (see below). So Proud - So Nerdy Although the bulk of our effort on this project was spent wrangling with the data, wrestling with GSQL, and building our API to the UI (no thanks to CORS restrictions!), we had always intended to provide our users with one killer app: an automatic scatter plot which would allow the comparison of any two metrics picked from the entire list. And we did it! We now have a tool which will allow anyone in the world to compare, for all countries and years where data is available: GDP vs carbon dioxide emmissions Refugee data vs homicide levels Apple production vs orange production (really!) Any metric in our data vs any other metric - no matter how crazy If you want to compare inbound tourism to blueberry crop yield, you can! If you want to see the impact of GDP on deaths from the plague, you can! Even though this was probably the simplest part of our build its the part that has (we think) the biggest potential to really open people's eyes to the power and potential of the UN data. The Future Our goal, first and foremost, for this project was to explore the power of TigerGraph and its capability to handle huge connected datasets. We already had some good skills in the team and were used to working with interesting schemas, but by deliberately tackling a huge dataset of very messy, but very interesting data we learnt so much more about what TigerGraph can do, its scale and power, and its ability to manage millions of vetrices with 10s of millions of edges. But what we found as we worked more and more with the UN data is that this project has potential far beyond this hackathon. What we built as a simple UI has real potential to open up the UN data in ways that just aren't accessible at the moment without a research team and some serious funding. If this tool could be industrialised and made available on a full time basis for anyone to use, the potential for journalists, economists, teachers, researchers, government departments and just about anyone with an interest in national data is extraordinary. There is so much more that an enhanced UI could offer: time series plotting, automatic correlation statistics and regression, graph algorithms - we are ending this hackathon with a huge backlog of amazing extensions we weren't able to build in time! And of course, there's always more data to load and connect. It's our hope that once this hackathon completes we can approach the UN themselves, show them what we've made, show its potential, and maybe with crowd-funding or even with UN funding, turn this seed of an idea into a resource that could benefit everyone in world. Appendix A: Metrics Metrics and data-source within the UN: Greenhouse Gas Inventory Data reported by United Nations Framework Convention on Climate Change (UNFCCC) World Tourism Data reported by World Tourism Organization (UNWTO) Homicide Statistics reported by United Nations Office on Drugs and Crime (UNODC) Refugee Data - UNHCR Statistical Database reported by United Nations High Commissioner for Refugees (UNHCR) Crop data reported by Food and Agriculture Organization (FAO) National Account Data reported by International Monetary Fund (IMF) Deaths by cause of death, age and sex (WHO data) reported by United Nations Statistics Division (UNSD) World Health Statistics reported by World Health Organization (WHO) <div