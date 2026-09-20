---
slug: "tracks-criyp3"
url: "https://devpost.com/software/tracks-criyp3"
title: "Tracks"
hackathon: "Web5: Building the Decentralized Web"
organization: "TBD"
winner: true
words: 619
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Tracks

> Travel. Record. Share.

[Devpost](https://devpost.com/software/tracks-criyp3) · hackathon [[Web5- Building the Decentralized Web]]

## Facets

**mechanism** [[on_device_local]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** google-maps, node.js, react, typescript, web5

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tracks

## Body

Welcome screen Home screen Viewing Track after adding notes and photos Home screen showing Tracks that have been linked together Viewing a friend's Track Inspiration I did a lot of travelling in my formative years (pre-smart phone), and lost a lot of SD cards and memories along the way, and always thought how great it would be to have one central place you could record all your adventures and share them with friends - so started working on Tracks as a pet project. What it does Users have their own world map (using GoogleMapsReact/Google APIs) where they can add pins, or Tracks, to places they've travelled to. They can add images and notes to each Track as a record of their experiences. They can also link Tracks together to show journeys with multiple stops, and add friends so they can share their adventures. How we built it Tracks is a client-side app built using React and Nodejs, and it relies heavily on the Web5 and Google maps libraries. In its most recent iteration I was using Google Firebase for user authentication and data storage, but I was never comfortable with the idea of having access to users information and wanted to find a trust-minimised solution. Around the same time Jack Dorsey was tweeting about the web5 work TBD was doing and I've followed along ever since. Core web5 functionality Protocols configure set read/write/delete permissions for the Tracks Web5 connect called when the app loads to provide the web5 client and the user's DID Records write called to create the initial Track data after adding a Track to the map query called when the app loads and is filtered to display only the Tracks created by the user called when viewing a friends Tracks and is filtered to display only the Tracks created by the friend update called anytime Track details or images are modified send called to sync any updates made to a Track with the DWNs of all friends delete called to delete records stored by DWNs locally and remotely for the user, and remotely for the user's friends Challenges we ran into I found some of the stuff around protocols/permissions a challenge to work with, and think my current implementation is probably not optimal. The app is also not very performant when a user has more than a couple of friends (lots of calls to multiple DWNs), so I might need to rethink the architecture around that. Accomplishments that we're proud of I'm proud of being able to migrate Tracks from Firebase to Web5, getting closer to my goal of an app where the user's data is owned and controlled by them. I'm also pleased with the overall look and feel of the app! What we learned I've learned a lot around the workflow for using decentralised ID and data storage in the web5 framework. That side of tech doesn't come easily to me and I feel like I've barely scratched the surface but it feels like a good start to have an app up and running. What's next for Tracks There are dozens of improvements I would like to make in future, but key features would include: Moving away from using web5.connect() to a more persistent DID/DWN solution ie. a wallet Making it mobile friendly (currently only fit for desktop) Image handling optimisation Adding a short tutorial pop-up on first visit to explain how to use the app Individual Tracks being set to private by default (need to be made public for friends to see them) Being able to create collaborative Tracks (invite friends to add images and notes etc.) Enabling comments on photos Adding validations (for deleting Tracks etc.), and other general performance improvements <div