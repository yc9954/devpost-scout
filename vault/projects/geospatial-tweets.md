---
slug: "geospatial-tweets"
url: "https://devpost.com/software/geospatial-tweets"
title: "Geospatial Tweets"
hackathon: "ARCore Geospatial API Challenge"
organization: "Google"
winner: true
words: 323
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Geospatial Tweets

> Automatically find and show things tweeted close to you in AR. This app uses the user's location provided by the Geospatial API to find tweets which were geotagged at locations close to the user.

[Devpost](https://devpost.com/software/geospatial-tweets) · hackathon [[ARCore Geospatial API Challenge]]

## Facets

**substrate** [[geospatial]] [[video_visual]]

**stack** c#, google-geocoding, twitter, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for geospatial tweets

## Body

Asakusabashi Tweet Inspiration I love taking walks around Tokyo and Japanese Twitter is usually quite interesting (with a heavy focus on food). I thought it would be nice to be able to see tweets from nearby as I walk around the city. Anchoring the sentiments and photos from Twitter to the areas where they were tweeted. What it does This application uses the Google Geospatial API to find the user's location. This location data is then used to search Twitter for geotagged tweets close to the user using the Twitter API. Once found the tweets are displayed in AR for the user. How we built it The application was built in Unity combining the Google ARCore extensions Geospatial API component and code which queries the Twitter API. Challenges we ran into One of the biggest challenges was attempting to place the tweets in the correct position. Tweets can have various different kinds of location data, from general data regarding the city to specific geospatial coordinates. To simplify things I limited the range of the search to very close to the user so tweets would be related to the area the user was in. Accomplishments that we're proud of I think this app is really good for finding tweets that we would never otherwise see. In my testing I found many tweets with interesting photos that I would have never otherwise seen. So I am most proud of how this app can be used to promote local exploration. What we learned I learned that even when limiting the area of a Twitter search to within less than 100 metres it can return way too many tweets to show. I think the next version will only show tweets with pictures attached to them. What's next for Geospatial Tweets I would like to add the ability to tweet from the app so we can go full circle, tweeting about finding interesting geolocated tweets in AR. <div