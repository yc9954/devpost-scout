---
slug: "ourblock"
url: "https://devpost.com/software/ourblock"
title: "ourBlock"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 268
team_size: 7
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# ourBlock

> A community safety app connecting civilians & police to simplify crime reporting using machine learning & blockchain

[Devpost](https://devpost.com/software/ourblock) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

  <sub>weak: government_staff</sub>
**substrate** [[geospatial]] [[structured_db]]

**stack** a*, amazon-web-services, blockchain, crypto, elasticsearch, ethereum, google-maps, graph-theory, javascript, machine-learning, natural-language-processing, objective-c, python, react-native

## How they structured the write-up

- how it works
- tech stack
- dependencies to run

## Body

An interactive heat map showing crimes in the city so civilians can stay safe. The police hub; automatically dispatches officers to the most urgent locations. Ethereum distributed network for storing messages; no scaling database costs Features include searching, reporting, and token balance Search results How It Works Reported crimes are geotagged and passed through a deep learning severity classification algorithm Live heat maps are populated based on the severity and the frequency per location using triangulation Messages are stored in a blockchain distributed network across user devices to prevent scaling database costs Civilians are incentivized to report with ethereum tokens awarded for reports that help solve crime The result is that civilians can avoid / navigate around danger, search for and be notified of crime that may potential involve them, and police can better allocate resources to tackle incidents by urgency at a minimal cost. The community is also transparent and closer than it ever has been with a "I scratch your back if you scratch mine" mentality. All of this is done with the automation provided by machine learning and the distributed blockchain system. Tech Stack Tensorflow classifier/spam filter was trained using a bag-of-words and stemming technique Messages posted to the Ethereum network using Web3 & Solidity GeoLocation is gathered using Google Maps API Safe paths to navigate around crime calculated using the A star algorithm Server side logic is hosted on AWS Lambda The Police Portal is built on a Flask framework The Civilian Mobile App is built on React-Native Implemented crime searching using Elasticsearch Dependencies to Run tensorflow tflearn pandas nltk numpy web3 flask <div