---
slug: "nightdrive"
url: "https://devpost.com/software/nightdrive"
title: "ModCity: DRIFTERS"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 802
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "substrate/geospatial"
---

# ModCity: DRIFTERS

> Buy and drift cars on modular city roads in this remixable 90s Tokyo inspired world. This map showcases useful plug-and-play asset systems for custom vehicles, city-building, shopping... and more!

[Devpost](https://devpost.com/software/nightdrive) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**domain** [[retail_commerce]] [[transportation]]
**substrate** [[geospatial]]
  <sub>weak: video_visual</sub>

**stack** blender, horizon-worlds, substance-painter, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for modcity drifters

## Body

Skyview of City Modular Blocks Modular Roads Purchasable Physics Cars Scenic Racing Mountain Trim Sheets Modeling Cars Riding away into the sunset... Thumbnail Image Inspiration Our goal was to create a universally useful & engaging remixable world using custom plug-and-play assets. Cities are a common game environment location, but notoriously tedious to model, plan, and optimize. To solve this problem for Horizon creators, we decided to create a 100% from-scratch modular city block & road making asset pack: Modular City Blocks ! ModCity is our own city showcasing exactly this, taking design inspiration from games like GTA: San Andres. Of course, every city needs cars to drive around in! Because of this, we were inspired to create a custom configurable car controller called Physics Car . Creators can use this asset to swap in their own car meshes and use configurable parameters to emulate the physics of real-life cars. For ModCity Drifters, we designed 4 unique purchasable cars doing exactly this. We were highly inspired by Halo's Warthog while developing this system. The car driving reminded us of Japanese Franchises from the 90s such as Initial D and Tokyo Xtreme Racer. We reconstructed the real-life race track of Mount Haruna in Japan, which anime fans may recognize as the main racetrack featured in Initial D. (You may notice our car reference too!) To polish the experience, we added extra quality of life features to the world anyone can remix, even if not making a city or driving sim. There's a day/night cycle, login bonuses, shopping, weapons, item pooling, and more. What it does ModCity Drifters provides an open source template anyone can take, clone, and create their own cities and driving sim worlds with. Every asset set works independantly and can be edited or rearranged with ease. The world is intended to be 100% playable by regular users too, making it the perfect demo of what a final product using these templates could be like. Players can expect a full game loop that consists of driving, collecting money, buying new cars, and shopping for engaging side features like attachables and guns. How we built it Our original idea was to create a simple cops and robbers game in a modular city, with simple capture the flag mechanics. One of the things we really wanted to have in this world was a drivable car. When we got a car controller working it felt really good and we decided to pivot to centering the world around driving. But in the end it's still not too far off from our original idea. Our biggest goal was to make a high quality set of city themed building blocks, both from a performance and visuals standpoint, taking inspiration from the early 2000s era of gaming when vertex lighting (like horizons uses) was still in heavy use. And you can see from the results, both visual and as reported by the profiler, we didn't do too badly. Challenges we ran into Horizon Worlds physics are still early, so we had to find ways to implement extra calculations in-script. Vertex lighting also proved difficult, initially creating obtrusive seams between modular assets at first, taking many iterations to nail out. Accomplishments that we're proud of We are so proud of how intuiative and engaging our systems turned out. ModCity Drifters' game performance is better than we could have imagined considering the pure amount of 3D assets made for our asset pack. The world aesthetic turned out exactly as intended while still being optimized because of our focus on good topology and trimsheets. We think it turned out equally exciting for both world creators and regular users. 100% Human Made. No AI was used during production of ModCity. :) What we learned Solidified our understandings of the Horizon Worlds Networking model, improved our abilities writing gameplay systems, gained a greater understanding of physics and mathematical concepts, improved our modeling skills, exercised our project planning and scoping abilities, and ability to produce high quality content in a constrained system. What's next for ModCity Drifters It's goal now is to be used by the Horizons Community to make whatever they can imagine. Almost any world could benefit from the drop-in cars we provide, but even further then that the grid based environment assets we created our world from can be remixed and re-used to create many cities and roads of all shapes and sizes. If creators love ModCity, we'd want to create more modular asset pack themes and expansions. If players love ModCity, we'd want to add preset races, new items, more cars, skins, leaderboards, player combat, and monetization. There's a LOT we had planned and weren't able to implement in time. We truly hope you enjoy ModCity so we can continue to pour love into the project. Thank you for playing! <div