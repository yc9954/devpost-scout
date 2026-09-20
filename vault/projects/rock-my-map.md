---
slug: "rock-my-map"
url: "https://devpost.com/software/rock-my-map"
title: "Rock My Map"
hackathon: "MongoDB World Hackathon"
organization: "MongoD"
winner: true
words: 324
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Rock My Map

> Grateful Dead Europe '72 tour on a map

[Devpost](https://devpost.com/software/rock-my-map) · hackathon [[MongoDB World Hackathon]]

## Facets

**substrate** [[geospatial]] [[video_visual]]

**stack** meteor.js, mongodb, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for rock my map

## Body

Grateful Dead Europe '72 Song Chart Show List Inspiration I love live music and going to shows, however have never had the luxury of "going on tour" with a band. But I can still dream and viewing a bands tour on a map could be the next best thing. I like mapping data and MongoDB works great for geospatial data sets like a bands tour. It could also be great for tour managers :) What it does You can search for any band and year and Rock My Map will plot all of the shows during that year, it will also show you the tours that happened during that year. The Grateful Dead Europe '72 tour is a classic and Rock My Map will even give you driving directions after plotting the shows, historical weather and setlists. How I built it I wanted to learn React and Meteor's pub/sub integration with MongoDB. I started by adding SetlistFM API queries and caching those in MongoDB. I then added historical weather from Dark Sky to help bring back some memories if it was a show you went to. Challenges I ran into Some band names or other data can have not common characters. I found MongoDB $text index and search solved a problem with querying on these, like the umlaut in Mötley Crüe . setlists.find({$text: { $search: props.band, $caseSensitive: false, $diacriticSensitive: false }}); Accomplishments that I'm proud of I ended up querying several APIs for data, SetlistFM for band tours, DarkSky for historical weather, LastFM for band images so getting this process flow and storing it all in MongoDB was a great accomplishment. What I learned MongoDB Charts, MongoDB $text index. What's next for Rock My Map I'd like to add the ability to search for a bands future tours that may not yet be on SetlistFM. I'd also like to add a geo nearSphere search to reveal shows within x miles of the user. <div