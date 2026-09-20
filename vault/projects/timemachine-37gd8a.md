---
slug: "timemachine-37gd8a"
url: "https://devpost.com/software/timemachine-37gd8a"
title: "SkyLine"
hackathon: "ARCore Geospatial API Challenge"
organization: "Google"
winner: true
words: 567
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "substrate/geospatial"
---

# SkyLine

> Unveil the future of your city's skyline though an interactive experience that allows you to travel through time to explore proposed high rises at full scale, superimposed within existing structures.

[Devpost](https://devpost.com/software/timemachine-37gd8a) · hackathon [[ARCore Geospatial API Challenge]]

## Facets

**mechanism** [[structural_withholding]]
**substrate** [[geospatial]]

**stack** arcore, c#, geospatialapi, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for skyline

## Body

One Park Lane proposed high rise highlighted looking south from Central Park Future skyline with all buildings including those with unknown completion dates looking south from Central Park Future skyline looking south from central park in 2026 Proposed buildings looking up Fifth Avenue from the New York Public Library Proposed high rise at 570 Fifth Avenue highlighted JP Morgan Chase World Headquarters currently under construction. Augmented reality overlay shows the extents of the building once topped out Inspiration My inspiration for the app came from my background as an architect. Before I got into developing augmented reality apps, my profession was in architecture, and I've always had a genuine interest in buildings. Living in New York, I'm constantly inspired looking at the city's amazing structures, and I wanted to create a lens to look to the city's future and understand how it will change over time. What it does SkyLine is an augmented reality app that shows the progression of the skyline in New York City over the next 10 years or so. The app displays proposed highrises in their correct locations, superimposed on existing buildings, and provides a glimpse into the future of the city's architecture. A timeline feature allows users to scrub back and forth through time based on each buildings expected completion date, and a map at the bottom of the screen serves as a reference for each building's exact location as well as an interface to select each one to learn more about it. How we built it The app was built out in Unity using AR Core and the Geospatial API. One feature of the API I made really good use of was the Terrain Anchors feature, which allowed me to place each building remotely at the correct elevation. Challenges we ran into One of my biggest challenges was time, I found out about this hackathon a bit late, and I only had about a week or so to come up with a concept and execute it. From the technical side, one big challenge was dealing with occlusion. Phones have difficulty detecting depth at the ranges I needed for this app, so I ended up writing a shader that fades from top to bottom, which in the end turned out to be better for the user experience, because more buildings were visible. Another challenge was incorporating a map on only half of the screen. because of the way maps work in Unity, this needed to be done using a render texture, and it was particularly challenging to set it up in a way that was easy to interact with. Accomplishments that we're proud of I'm really proud of the overall design of the app. I feel the design is really cohesive and feels well thought out. The 3D augmented reality elements and the 2D screen space elements really speak one story, and create a unified user experience that's intuitive and fun. What we learned I learned a lot about time management and prioritizing the most important features to get across the finish line. I also gained a better understanding of using terrain anchors in the Geospatial API. What's next for SkyLine My goal is to start compiling data to scale the app beyond NYC. It would be great to expand to other large cities like LA, Chicago, and San Francisco, or even go international with architectural hubs like Dubai and Singapore. <div