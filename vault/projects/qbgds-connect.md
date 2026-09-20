---
slug: "qbgds-connect"
url: "https://devpost.com/software/qbgds-connect"
title: "QBGDS Connect"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 286
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
---

# QBGDS Connect

> Connect a Quick Base table to Google Data Studio with QBGDS Connect.

[Devpost](https://devpost.com/software/qbgds-connect) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]

**stack** google-apps-script, google-data-studio, javascript, quickbase

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for qbgds connect

## Body

Configuration screen in Google Data Studio Side by side data screens Report embedded back (Google-hosted) Inspiration Lots of my clients gravitate towards free and open source business intelligence tools like Google Data Studio to merge and display data in new and exciting ways. With more business users creating new and exciting data sources in the form of Quick Base apps, I think it is critical that the underlying data they create fold into those existing data solutions. What it does Allows a table in Quick Base to be a native data source in Google Data Studio. How I built it It is built with custom Google App Script (javascript) in the Google App Script environment, leveraging the power of Quick Base's REST API system. Challenges I ran into Live usage of data can be a little slow, but I was able to leverage Google App Script's native cache store to keep data in memory, and not fetched from Quick Base for every single little change. Accomplishments that I'm proud of Works seamlessly in the Google Data Studio framework, and then opens all the realms of possibilities -- I especially like embedding Data Studio reports back into Quick Base. And, that opens to mixed and merged data from all of Data Studio's other data sources. What I learned There are over 270 partner data connectors, which means all of the data could now be available instantly on your homepage in a Quick Base app combined with the Quick Base data via this connector. What's next for QBGDS Connect I would like to publish it as an official partner connector, so everyone can use it! I also like to add support for the more complex relationship fields. <div