---
slug: "artmap"
url: "https://devpost.com/software/artmap"
title: "ArtMap"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 589
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ArtMap

> Art Map

[Devpost](https://devpost.com/software/artmap) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** art-institute-of-chicago-api, google-maps, next, react, tailwind, three.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we overcame
- accomplishments we're proud of
- what we learned
- what's next for artmap

## Body

Inspiration As a museum enthusiast, I've always felt something was missing from traditional art viewing experiences. Standing before a masterpiece and reading its placard, which showed a distant place of origin, I found myself yearning to visit that location—to understand the cultural context that had shaped the artwork. What if we could bridge this gap? Instead of just observing color and texture in isolation, what if we could walk the very streets where these artworks were born? I envisioned an immersive experience where users could explore locations through Street View while browsing galleries of local artworks from different historical periods. The contrast between modern streetscapes and ancient art would create a uniquely compelling way to understand art in its geographical and cultural context. What It Does ArtMap transforms Google Maps into a comprehensive global art discovery platform. Users can: Search for and view artworks from different periods and locations worldwide Visit any place via Street View and browse locally-relevant artworks in a dynamic 3D gallery Experience art in its original cultural and geographical context Explore the relationship between place and artistic expression across time The platform creates a bridge between physical locations and their artistic heritage, making art appreciation both educational and experiential. How We Built It Our technical stack combines the following technologies: Frontend & Mapping: React-google-maps library for Map and Street View integration, Places API for searching cities and attractions, and Geocoding API for precise location targeting. Art Data: Art Institute of Chicago API for comprehensive artwork collections, with Elasticsearch for efficient querying of artworks by geolocation and time period. 3D Gallery Experience: React Three Fiber integrated with Google Street View, featuring a custom perspective mapping system that synchronizes 3D gallery orientation with Street View camera changes and adapts to different environments. Challenges We Overcame The most significant challenge was creating a seamless 3D gallery experience within Street View. Google Maps' native 3D shapes only work with 3D map view, not Street View, and each Street View location has unique angles and perspectives. The core problem was perspective synchronization. Three.js and Google Street View use different coordinate systems and camera tracking mechanisms. We had to reverse-engineer Google Street View's camera perspective calculation and develop custom transformation algorithms to convert Street View camera data into Three. js-compatible coordinates. After extensive experimentation and testing across different geographical locations, we built a responsive system that maintains natural gallery positioning while ensuring the 3D experience looks realistic for most places. Accomplishments We're Proud Of Pioneered a unique integration: Created interactive 3D galleries responsive to Google Street View perspective changes—a technique with no existing documentation online Achieved global scalability: Built a comprehensive artwork-geography mapping system that works anywhere in the world What We Learned Google Maps Expertise: Advanced features of the Google Maps ecosystem, including location finding, user geolocation, and the intricate mechanics of how Street View rendering works. 3D Development: Three.js fundamentals for creating interactive 3D environments, complex coordinate system transformations, and performance optimization for real-time rendering. Integration Architecture: How to bridge disparate APIs and rendering systems while maintaining smooth user experiences across various technology stacks. What's Next for ArtMap Immediate Goals: Deploy the application with a memorable URL for global users and optimize performance across different devices. Future Vision: Street Art Integration: Instead of floating galleries, paint artworks directly onto buildings as street art, creating a more immersive and contextually integrated experience Historical Timeline Mode: Allow users to "time travel" through different periods while staying in the same location Community Features: Enable users to contribute to local artwork collections <div