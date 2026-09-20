---
slug: "pac-maps"
url: "https://devpost.com/software/pac-maps"
title: "Pac-Maps"
hackathon: "hack:now"
winner: true
words: 553
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/housing_homeless"
  - "substrate/geospatial"
---

# Pac-Maps

> Real-life Pac-Man game that promotes exercise, social distancing, and friendly competition!

[Devpost](https://devpost.com/software/pac-maps) · hackathon [[hack-now]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[housing_homeless]]
**substrate** [[geospatial]]

**stack** apple-maps, bluetooth, core-location, firebase, google-cloud, ibeacon, ios, mapkit, swift, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pac-maps

## Body

Inspiration We are living in an unprecedented time — where the world around us has come to a halt. And with the shelter-in-place, exercising regularly has become quite a challenge. Also, we're unable to interact or hang out with our friends. What it does Our tech-enhanced take on the classic arcade game brings you an exciting way to stay healthy, maintain a proper social distance, and have fun at the same time! We created a mobile application for iPhone and iPad which lets you play Pac-Man in the real world, right in your neighborhood! The app shows a map of your surroundings, along with other people (whom you should stay away from). You can select your walking / running path by adding waypoints, and this represents the coins that the you (the Pac-Man) will pick up as you exercise in your neighborhood. But you must stay away from other people (the ghosts) or you will lose lots of points! How we built it We used Swift and Xcode to develop our application for iPhones and iPads. We integrated technologies like MapKit to show the map around the user and plot the user’s exercise route. We also use Firebase to track the players’ points and their current locations. Combining Firebase and MapKit, we plot the points of ghosts (other users) nearby so that the user can maintain safe social distances from others. We use Bluetooth to generate iBeacons that detect if two users are too close, and alert the users to move away from each other, and this is reinforced by subtracting points from the user. We also designed a beautiful user-interface that pairs with the Taptic Engine to quickly alert the user if there is someone in their vicinity. Challenges we ran into It was a challenge to create the MapView and integrate the Pac-Man and ghost locations as well as allowing the user to create their own workout routes by selecting waypoints. Another hurdle was learning and integrating Firebase into our iOS app, but we were able to overcome it quickly. Communication was tough for us because we could not work side-by-side, so, we used Cisco Webex to always be in contact to clarify any questions and collaborate together. Accomplishments that we're proud of This mobile application allows users to stay healthy by exercising while complying with social distancing rules. This app uses bluetooth for close range communication and GPS location services to tell the user how many people are in a specific area and how close they may be to you. Using these technologies, we are able to provide a clean user interface and great user experience. What we learned We learned how to use Firebase and the potential it has for our app and other applications. We also developed a beautiful user interface that includes the MapView and the path plotting and tracking implementation, to follow the user in the physical world in real time. What's next for Pac-Maps In the future, our app could be used to help trace contacts in the case that a user is positive for COVID-19 or came into contact with someone who is / was positive for COVID-19. This would be an anonymous way for users to be alerted if they have been near or in contact with someone who had the virus. <div