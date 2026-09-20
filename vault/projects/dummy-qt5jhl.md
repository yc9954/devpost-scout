---
slug: "dummy-qt5jhl"
url: "https://devpost.com/software/dummy-qt5jhl"
title: "Covid Real Time"
hackathon: "Elastic Weekend with Code for Cause"
organization: "Code for Cause"
winner: true
words: 309
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Covid Real Time

> Interactive Visualization of Real Time Coronavirs Cases around the world!

[Devpost](https://devpost.com/software/dummy-qt5jhl) · hackathon [[Elastic Weekend with Code for Cause]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[document_pdf]] [[geospatial]] [[web_dom]]

**stack** bootstrap, elasticsearch, kibana, node.js, three.js, vite.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for covid real time

## Body

Front Page Dashboard Inspiration I have always wanted to make something useful to others and Kibana has given the exact tools and features that it has been made possible 😁 What it does It shows the real time data of coronavirus cases around the world, by countries cases, deaths, recoveries cases, recovered, active, deaths per million broadly divided by countries Kibana map visualization Size Frequency of countries by their new cases And all of these support filtering by elastic search, you can see info by specific countries too!! How I built it ELK stack is basically all a company or a user needs to enter, handle and present data all in real time! What I have done is, I index data into Elasticsearch using elasticsearchjs and then setting up the dashboard. The front page is designed with three.js with was really fun to implement. Challenges I ran into Logstash was a bit new and the pipelining syntax took some time to understand (not much documentation is given) The ElasticSearch documentation is a bit poor, there were a lot of times i felt like, there is no workaround for some problems such as the index mapping of elasticsearch (we cannot edit the mappings after indexing documents) but then had to redo sometimes. But in the end it all sorted out. What I learned In just 3-4 days, I have gathered a lot of knowledge about the basic structure of the ELK stack and how companies are using it, what features it provides, also threejs was new to me, I also learned about vitejs which is pretty great tool from development point of view. What's next for Covid Real Time Next, is clear I would include vaccination data and helplines so that my website would even help people in need!! Thanks Hackathon Organisers Code For Cause I had fun 😄 <div