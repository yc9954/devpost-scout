---
slug: "pasumai"
url: "https://devpost.com/software/pasumai"
title: "Pasumai"
hackathon: "monday.com climate change app challenge"
organization: "Monday.com"
winner: true
words: 331
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Pasumai

> An app to integrate weather, weather alert and pollution data to monday.com boards

[Devpost](https://devpost.com/software/pasumai) · hackathon [[monday.com climate change app challenge]]

## Facets

**substrate** [[geospatial]]

**stack** google-maps, node.js, react, weatherapi

## How they structured the write-up

- what it does
- how we built it
- what we learned
- what's next for pasumai

## Body

What it does Pasumai app lets you integrate current Weather data and Air Quality data into your board. Get notified of any weather alerts in the location you selected. View weather details in map. It has two integration apps, a board view and a item view. Current Weather - Integration It has recipes to update weather data to Boards. A recipe to automatically update weather data every 6 hours to the Board. A recipe to notify the user when a Weather Alert is issued to the given location. An update will be added to the item and a notification will be sent with the details on the alert as well. And multiple recipes to manually update weather data like Temperature, Wind Speed, Humidity, Precipitation etc., for selected location. Current Air Quality Index - Integration It has recipes to update air quality data to Boards. A recipe to automatically update air quality data every 6 hours to the Board. And multiple recipes to manually update weather data like Carbon Monoxide, PM2.5, EPA Index etc., of the selected location. Weather Map - Item View A weather map to look at multiple weather parameters in and around the selected location. Map View - Board View A Map View to plot the board data in map. How we built it The Pasumai app node.js + mongodb + react app. In backend uses https://www.weatherapi.com/ API to get weather data, air quality data and weather alert. For maps, windy.com and Google Maps are used. User tokens and subscription data are stored in mongodb. For auto update of weather and air quality data happens with a cron job which gets triggered every 6 hours and update the boards. What we learned Initially had some difficulties in understanding Custom Trigger and Item mapping, but finally I was able to understand it and built it. What's next for Pasumai To successfully publish the App in marketplace. Add additional recipes for Weather Forecast and Historical weather and Air quality data. <div