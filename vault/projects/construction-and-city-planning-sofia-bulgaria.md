---
slug: "construction-and-city-planning-sofia-bulgaria"
url: "https://devpost.com/software/construction-and-city-planning-sofia-bulgaria"
title: "Construction and city planning - Sofia, Bulgaria"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 696
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Construction and city planning - Sofia, Bulgaria

> This maps is showing in fine detail how Sofia, Bulgaria would look like should all requested construction is fulfilled. It goes beyond the dry paperwork and allows you to look outside your window.

[Devpost](https://devpost.com/software/construction-and-city-planning-sofia-bulgaria) · hackathon [[Google Maps Platform Awards]]

## Facets

**domain** [[civic_government]]
**user** [[general_public]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** 3d, cesium, d3.js, geojson, google-maps, javascript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what i learned
- what's next for construction and city planning - sofia, bulgaria

## Body

Inspiration Process and paperwork in city planning are convoluted and nearly impossible to follow. Ordinary citizens and even activists familiar with the subject find it overwhelming to understand and visualize projects that may be problematic for the community, infrastructure or city planning as a whole. I felt this as I moved in Sofia, Bulgaria and wanted to understand where to settle, how the city would develop and what I can do about it. What it does This map is yet another step in my transparency efforts. I was inspired by Google's Photorealistic 3D map to show citizens how their city would look like should all planned and requested construction be fulfilled. People are thus able to see what will be built right in front of their windows or plan property investments better considering future construction, zoning and obstructed view. It puts 20 thousand outlines of possible buildings on the map with filtering by height. One can mark buildings for easy spotlight when screenshots are taken. Clicking on any place allows for quick search of the latest city planning documents on that spot and a link to the sister project - a map with hundreds of thousands of geocoded documents. How I built it I took a layer off the portal of city planning authority and extracted over 25 thousand polygons. Then I encoded their planned height and overlayed them on the photorealistic 3D tiles. There's also a crowdsourcing option where people can mark which of these is already in construction. Data is constantly being revised and added to as new permits and documents are issued. Challenges we ran into The source of the data is manually entered from submitted plans and outlines. The published layer thus has quite a few errors, which required a lot of manual work to resolve. As the Google 3D tiles are couple of years old, Sofia has changed quite a bit as infrastructure and some projects are built. There're I had to cross-reference what is on the tiles and what is in construction already to keep the visualization as accurate as possible. Performance has been a struggle. Due to the sheer amount of data, I had to segment the buildings and display these in sections as well as do other optimizations in the code. I'm currently reimplementing it with geojson-vt to simplify the buildings in the distance. Also due to some engine specifics, the map doesn't load on iPhone browsers. Works fine on other iOS devices. Accomplishments that we're proud of The map has been visited by over 10% of the population of Bulgaria's capital. It has triggered an extensive debate about transparency in city planning and how open data is being published. City officials and the mayor reached out for collaboration and I've created variations of this map for their site mapping out maximum construction height limits and new zoning discussions. The map is regularly referenced in media in past months and has drawn both praise by architects and urbanists as well as critique by investors and construction companies. What I learned I haven't worked with cesium before and picked it up due to its performance. I am constantly adding filters and features and have learned a great deal about city planning and the processes. Many architects have reached out as well as some members of the city council and parliament. We've discussed legislation, how to improve open data and how to enable this effort to be automated and scaled to other cities. We've learned a lot about local specifics, issues with the data and quality control over the model input a the source. What's next for Construction and city planning - Sofia, Bulgaria I'm optimizing the map to make it easier to see and available for all devices. I'm also reimplementing the map for Google map API instead of using the 3D tiles directly to see if it performs better in my usecase. I've already added some buildings in other cities where local officials and activists needed visuals for problematic projects. I'm adding a whole new city soon as well. I'm planning to publish the code of the map to allow for contributions and integration with other initiatives. <div