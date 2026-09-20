---
slug: "time-to-say-goodbye"
url: "https://devpost.com/software/time-to-say-goodbye"
title: "Frame by Frame"
hackathon: "ARCore Geospatial API Challenge"
organization: "Google"
winner: true
words: 667
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Frame by Frame

> A location-based AR storytelling game about finding back memories and saying goodbye.

[Devpost](https://devpost.com/software/time-to-say-goodbye) · hackathon [[ARCore Geospatial API Challenge]]

## Facets

**substrate** [[geospatial]] [[video_visual]]

**stack** arcore, c#, google, google-geospatial-api, google-maps, unity

## How they structured the write-up

- inspiration
- what it does
- how it works
- how we used google geospatial api
- challenges we ran into
- accomplishments that we're proud of
- what's next for frame by frame

## Body

Poster Bryant Park Brooklyn Bridge Game Test UI Interface Inspiration We started with the idea of making an AR game that Explores the possibilities of AR storytelling Gives players the opportunity to go out and interact with the environment Provides tourists with a new way of exploring New York City Reveals hidden stories or memories with AR’s ability to “make the invisible visible” Evokes thoughts on memories - if we could erase memories, what kind of choices will people make? Is erasing painful memories a good thing? What it does Frame by Frame is a location-based AR narrative game made with Google Geospatial API. In this game, you play as Selena, who finds her old phone with corrupted photos inside. You'll need to go to the locations where the photos were taken and match them with the real-world environment to repair the photos and retrieve your lost memories. The truth unfolds as you collect different memory fragments and discover hidden information. How it works Entering the game, the player will see two apps—photo gallery and map—on the home screen. In the photo gallery, there are three corrupted photos, each of which was taken at a different location in New York. Using the map, the player can find out where the photos were taken and navigate to the spot in real life. If the player gets close to one of the locations, the corresponding memory fragment will be activated. The player will need to match the photo with the real-world environment to repair the photo. When succeeded, Selena's lost memories will reappear in the real life as 3d models. The player can interact with the models and obtain certain objects to discover hidden information. After repairing all the photos and collecting all the objects, the player will uncover the full story. How we used Google Geospatial API First, we went to Brooklyn Bridge, Bryant Park, and Rockefeller Center and took a photos at each location. We obtained the latitude, longitude, altitude, and rotation quaternion of the phone and used that data to place geospatial anchors in the real world. When the player is close to the anchor and holding their phone at a similar angle, the photo will be considered "matched" with its location in real life. We also placed 3d content using anchors so that when the matching process is completed, the player will see 3d models in front of them. Challenges we ran into The biggest challenge was that we had to frequently test and debug our game outdoors in New York's freezing cold weather. We couldn't feel our hands at the end of each day. Also, the sun sets pretty early in winter while the VPS system doesn't work well when it's dark, so we only have limited time for testing. The geospatial anchor is not very accurate when there are no buildings around, for example on the Brooklyn Bridge. We tried many times to place 3d content on the bridge at a specific spot, but the models will always be floating somewhere else, so eventually, we used AR Plane Detection to place models instead. Accomplishments that we're proud of This is our first time using Google Geospatial API. We're proud that we managed to make a complete AR narrative game using the API in less than one week. Since our project is location-based, we spent three days testing the game in New York and iterated the game several times. For example, we made the story more specific, optimized the player experience, and adjusted the gameplay according to the features of the Geospatial API. We are happy with the final product. What's next for Frame by Frame Add more locations. Now the story is based in New York, we’d like to add more locations in different cities so that people can play this game in different regions. Build a more complex smartphone system to make the game more immersive. We could add more apps for players to discover clues, such email, text messages, etc. <div