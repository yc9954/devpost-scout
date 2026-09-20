---
slug: "climate-hours"
url: "https://devpost.com/software/climate-hours"
title: "Climate Hours"
hackathon: "monday.com climate change app challenge"
organization: "Monday.com"
winner: true
words: 500
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/geospatial"
---

# Climate Hours

> A tool to help companies and teams view and respond to real time threats by natural disasters affecting their team members.

[Devpost](https://devpost.com/software/climate-hours) · hackathon [[monday.com climate change app challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[developer_tools]] [[disaster_emergency]] [[labor_employment]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** google-geocoding, google-maps, monday-javascript-sdk, react, weather.gov

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for climate hours

## Body

Overview of the map and weather alert data alongside employee locations Split view of board and map data Adjusting climate hours via Info Window Inspiration As the climate changes there has and will continue to be an increase in both frequency and severity of natural disasters. Companies and teams will need to take them into consideration as they can not only be a threat to productivity, but primarily to the overall health of the team. Workers deserve more security in this changing world, and retaining team members is a problem that will get harder as workers become consistently threatened by the Climate Change. What it does Climate Hours aims to help companies and teams adapt to a changing climate by providing an integrated workflow that provides visibility into which employees or team members could be affected by impending weather events. By consuming active weather alerts, displaying them on a map alongside employee locations, and tracking Climate Hours that employees are taking, companies and teams can help their workers prepare for and react to these threats. How we built it We built a React application that uses the monday.com javascript SDK. Google Maps is used for the mapping functionality as it loads in a geojson file to populate the polygons on the map. The polygon data is from the National Weather Service as is the active alert information that gets displayed in the application. We built a moday.com template to go with the application to ensure columns are populated reliably. Challenges we ran into Creating a template was the simplest way to guarantee proper functionality of the application. It was a bit challenging to get different board constructions to work with our application, so adding the template is the best way to ensure a solid user experience. Accomplishments that we're proud of Successfully integrating google maps, National Weather Service active alerts, and monday.com board data was a huge accomplishment. This application implements the MVP features we wanted to include which was populating the map from different data sources as well as reading and writing monday.com board data. We think the style of the map fits perfectly into the monday.com framework, and most importantly, extends the map functionality that current exists on the platform. What we learned Technologically, we learned a lot about graphql queries as well as the monday.com api. The monday.com developer ecosystem is built to scale, and we definitely are open to continue developing on the platform in the future! Hopefully we learned that a simple tool can have a huge impact, and bringing visibility to the real time impacts of Climate Change can save lives. What's next for Climate Hours Climate Hours has plenty of expansion opportunities. For starters, consuming weather alerts from all over the world would be greatly beneficial. We also believe the application has the ability to consume historical weather data alongside future climate projections to generate risk profiles that provide more insight as to how weather might affect the worlds increasingly distributed teams. <div