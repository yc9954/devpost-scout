---
slug: "waterwaterwater-loolooloo"
url: "https://devpost.com/software/waterwaterwater-loolooloo"
title: "LooLooLoo"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 254
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# LooLooLoo

> After you "water, water, water" it's time to go to the "loo, loo, loo!" After you go to a water fountain, a text message will be sent to your phone detailing you the nearest washroom location.

[Devpost](https://devpost.com/software/waterwaterwater-loolooloo) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** bluetooth, css, html, node.js, react, typescript, vite, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for www.loolooloo.co

## Body

Inspiration www.loolooloo.co is inspired by the famous Waterloo chant—Water Water Water! Loo Loo Loo! And, of course, the natural consequence of drinking lots of water, water, water, being a visit to the loo, loo, loo! What it does www.loolooloo.co detects when you go to a water fountain, and sends you a text message with a custom link to an interactive map that gives you directions to the nearest bathroom. It also has a daily water tracker that incentivizes you to stay hydrated. How we built it We utilized the MappedIn API to implement an indoor navigation system for building maps. The front-end was developed using React, while the back-end was powered by Node.js. Twilio's API was integrated to enable SMS notifications with custom map links. Challenges we ran into Deploying a Bluetooth beacon to detect user proximity and send real-time requests to an HTTPS port proved to be a complex task, particularly in managing secure communications and ensuring reliable detection within a defined radius. Accomplishments that we're proud of We successfully built a fully functional system where the front and back ends work seamlessly together, delivering a real-time user experience by sending SMS directions to the nearest restroom whenever a user approaches a water fountain. What we learned We gained valuable experience in integrating proximity detection systems with cloud services, handling real-time data, and optimizing our full stack application for responsive and secure user interactions. What's next for www.loolooloo.co Future plans include enhancing the system's accuracy, and making the UI more user friendly. <div