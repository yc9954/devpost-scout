---
slug: "superman-navigation"
url: "https://devpost.com/software/superman-navigation"
title: "Superman Navigation"
hackathon: "Junction 2017"
winner: true
words: 433
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "substrate/geospatial"
---

# Superman Navigation

> Have you ever wondered how Superman flies around the world and knows exactly where to go? Well we can show you how!

[Devpost](https://devpost.com/software/superman-navigation) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]]
**substrate** [[geospatial]]

**stack** android-studio, google-directions, movesense

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for superman navigation

## Body

Inspiration The idea came from walking around in a new city. Always watching the phone seems a bit annoying for the user and is not as fun as it could be when navigating around. Or when you go walking or running without a phone and decide to wander around new destinations, and forgetting your way home. Then we had an idea, what if we could point to a direction , and the smartwatch would notify the user if the way is hot or cold from the actual way he or she wants to go. What it does Basically, we track the direction the sensor is aiming at. The more precise you are the more your watch vibrates . When your watch goes crazy, you know it's the right way to go. How we built it It is built by using an electromagnetic field sensor that is located in the sensor and also geolocation data from the web and a smartwatch. When the sensor senses the horizontal position (indicating that the user want help with navigation), the sensor starts to calculate it heading compared to the north. If the degree of the sensor heading and the destination are close, the device would start vibrating. Challenges we ran into Most of the challenges we faced were with the sensors and debugging , wondering why our data was not the same as the data on the test app. We also ran into trouble on how to calculate the correct direction from the user location to target location. The sensor needs calibration from time to time. At some point, all our data suddenly changed and we noticed that we can't work with previous data anymore. Ideally, the best results will come if the sensor sits perfectly horizontal . We did not get the best results indoors because the sensor and location services don't give most accurate data due to the disturbances in the force . Accomplishments that we're proud of A prototype that can sense in which direction a destination is from the user's current location as the crow flies . We managed to read complicated magnetometer data and use it to our advantage. What we learned Handling information about navigation is really complex when it comes down to it. Indoor tracking is more difficult than outdoor tracking. The metal around us messes up even the most awesome sensor's data. What's next for Superman navigation Standalone application Navigate through more complex areas of the city with Superman navigation Lessening the battery usage of the device Reduce noise in data Implement on a wearable, like a smartwatch <div