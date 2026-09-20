---
slug: "roots-zovgf2"
url: "https://devpost.com/software/roots-zovgf2"
title: "Roots"
hackathon: "hack:now"
winner: true
words: 553
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Roots

> Decentralized crowd-funding for resilient communities

[Devpost](https://devpost.com/software/roots-zovgf2) · hackathon [[hack-now]]

## Facets

**domain** [[civic_government]]
**substrate** [[financial_record]] [[geospatial]]

**stack** api, blockstack, firebase, gcp, google-maps, java, javascript, objective-c, puma-browser, radar.io, react-native, ruby, starlark

## How they structured the write-up

- what is roots?
- how we built it
- challenges we ran into
- what we learned!
- next steps

## Body

Home Page for the Roots Web App Home page for the Roots mobile app Community Page for the Roots Web App Checkin' up some finances on the Roots mobile app Roots Decentralized crowd-sourcing for stronger communities. (Demo video link: https://drive.google.com/file/d/1c-OWnoF9iLU3LefG_q6OG9S6ceZyIyCV/view?usp=sharing ) What is Roots? Roots is a way for members within a community to offer financial donations to each other during a time of distress. Communities members are grouped together via Radar.io Geofences based on their locations, and micro-transactions are completed via Puma Brower's web API. We aim to strengthen these community connections through a decentralized system, whereby every individual in the network is empowered to aid their peers in need. How we built it There are two parts to Roots: a web interface and a react-native mobile app. The web app enables users to create accounts through either Blockstack's authentication API or Google Firebase. Users are prompted to provide a statement of immediate relief, which would immediately alert other members of their community to donate if possible. The signup page also includes a field for a Stronghold Wallet ID, which enables web based micro-transactions through Puma Browser's web API. Cloud firestore is also used to record user sign up information (such as wallet-id and immediate needs). Once they have signed in, the user is presented with a map showing them in their community. The visual aspect is achieved via a combination of GCP's Google Maps JS APIs as well as chart.js. The users are grouped into communities through Radar.io's Geofence APIs. When a user signs up, their location is used to generate a new Radar.io user for the app; we used Radar.io's Geofence search API to discover the closest Geofence/Community to their location. Each user is also presented with the ability to add donation requests, and we update the user's metadata field on Radar.io to reflect their needs. The metadata field enables us to quickly find all donation requests within a community through Radar.io's users in geofence API. The react-native app enables users to track their locations on the fly, discover nearby communities, as well as check up on their finances. This is all done via Google Cloud Platform's Google Maps ios API. Challenges we ran into One major problem we ran into was getting Radar.io working on the web app. We kept on running into a 401 authorization error, but we eventually discovered that it was because we did not attach the published/secret key to the header of our http requests. Another problem we faced was on the front of the react-native app. We decided to use Expo as a starting place for our app, since both of us are in the unfortunate position of owning both a windows computer as well as an iPhone. We initially wanted to include Radar.io on mobile as well, but eventually we had o abandon that idea since we cannot properly eject an Expo react-native app to native ios code without using Xcode (which is exclusive to Mac). What we learned! A whole heck lot! Cloud firestore (how to add and get data) Radar.io (first time using Geofences) Google maps custom overlays with popups Puma Browser web apis Blockstack authentication Next steps Improve community construction (factor in census data and physical geographical boundaries) Add a need-based system for processing donations (Also Beeeeeeeeeeeaaach Boooooooooooooys ) <div