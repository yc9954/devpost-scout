---
slug: "geospatial-photo-gallery"
url: "https://devpost.com/software/geospatial-photo-gallery"
title: "Geospatial Photo Gallery"
hackathon: "ARCore Geospatial API Challenge"
organization: "Google"
winner: true
words: 284
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Geospatial Photo Gallery

> This app allows users to see the actual location where photos were taken. The app uses the Flickr API to find geotagged photos and uses the Geospatial API to place them at their geotagged location.

[Devpost](https://devpost.com/software/geospatial-photo-gallery) · hackathon [[ARCore Geospatial API Challenge]]

## Facets

**substrate** [[geospatial]] [[video_visual]]

**stack** c#, flickr, google-geocoding, google-maps, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for geospatial photo gallery

## Body

title use case Inspiration A photo captures a moment in time but seeing the photo at the actual location lets us link that moment to a place. I think it's a really poignant experience and not only makes the photos more meaningful but lets us appreciate the passing of time. I have made a number of prototypes that use AR to place historical photographs at the location where they were taken. Geotagged photos combined with the Google Geospatial API allows this process to be automatic. What it does This app creates a geolocated AR photo gallery, showing photos where they were actually taken. How we built it The app uses the Flickr API to search for geotagged photos close to the user. It then uses the Geospatial API to place the photos at their geotagged location. I made a similar AR gallery using the very first version of the Google Geospatial API but completely remade it with various improvements for this hackathon. Challenges we ran into The main problems we encountered were how to make the photos viewable at distance. We can search for photos up to 500 metres away from the user so making the photos far from the user visible required some attention. To solve this I created a function which keeps the photos at a standard size regardless of the distance from the camera. Accomplishments that we're proud of I feel the best feature of the app is converting the Flickr geotagging into Google Geospatial pose. What's next for Geospatial Photo Gallery I would like to expand this concept to more photo APIs, improve the UX and add the ability to select photos via the minimap and save favourite photos. <div