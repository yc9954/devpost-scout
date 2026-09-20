---
slug: "rex-inywpb"
url: "https://devpost.com/software/rex-inywpb"
title: "Rex"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 781
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Rex

> If you can dream it, Rex will find it!

[Devpost](https://devpost.com/software/rex-inywpb) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[sensor_fusion]] [[voice_speech]]
**domain** [[health_clinical]]
**substrate** [[geospatial]] [[structured_db]]

**stack** 3d-printing, cad, elevenlabs, mappedin, python, raspberry-pi, react, supabase, typescript, voiceflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for rex

## Body

Introducing Rex CAD CAD Rex!!! Inspiration It takes over 9 months to train a guide dog. The issue is: dogs can't talk (sorry). What if your favorite furry friend could not only guide you, but also talk to you — and understand exactly where you need to go? This was the founding idea behind Rex. We were inspired to create a fantastically helpful pup, who could lead you anywhere you wanted to go. By combining "classic" robotics with cutting edge AI, we were able to bring this dream to reality. We hope, with this, to facilitate the next generation of accessibility support at malls, hospitals, and even hackathons! What it does Rex is a wayfinding bot with agentic functionality. They listen to your request — whatever it may be — and interprets that to be a location in the building you're in. For example, if you told it "I'm feeling hungry", it would lead you to the RBC Oasis tent for some snacks! Along the way, it will look out for obstacles in your path and avoid them if necessary. It focuses highly on accessibility. How we built it On the software side , we made extensive use of VoiceFlow and Mappedin. This provided a significant challenge since these services could not efficiently be run on a Raspberry Pi, so we created a mobile-friendly web application that takes care of human-computer interaction (text to speech, speech to text) as well as making API requests. We used a custom knowledge base on VoiceFlow to customize the agent to be very specific to the different rooms in E7 and point of interests at Hack the North. We used VoiceFlow's Supabase integration to log a request in the database to begin a trip in the database (that the Raspberry Pi picks up on). Through the app, we made calls to VoiceFlow's API to progress the user's conversation with the agent. For Mappedin, we rendered the map on a React Typescript application and made use of the Wayfinding endpoint to retrieve thorough directions. Not only are these directions displayed on the app, but they are sent to the Supabase database which the Raspberry Pi listens to for entries to trigger certain movements. Supabase was used to connect the Raspberry Pi, VoiceFlow Agent, and Mappedin wayfinding. We chose Supabase due to its realtime subscription abilities and also its compatibility with all three ends of Rex. On the firmware side , our hardware system involved multiple sensors and actuators such as a Gyroscope, accelerometer, ultra-sonic sensor, and 4 DC motors. Challenged with not having access to a GPS or motor encoders, we used the accelerometer to determine our current location with respect to the origin when navigating through some area, and used the Gyroscope to feed data into our PID controller to ensure we can travel straight and make accurate turns. We also used an ultra-sonic sensor for obstacle avoidance. Once we have received the directions to the requested destination from the database, we use these sensors and actuators to ensure you are able to get there safely. On the mechanical side , the dog-shaped cover, axles, and ears for this project were 3D printed. The cover was designed to resemble a Dachshund, serving as a protective casing for the wheels, MCU, and circuit components. Two axles were fabricated to hold the assembly together, with the lower axle specifically supporting the main microcontroller. One of the main challenges we encountered was the placement of the battery pack inside the dog’s head, which affected the balance. To counteract this, we added another axle vertically, connecting the base to the top of the robot dog to maintain stability. Challenges we ran into We ran into many significant challenges primarily in the realm of interfacing between all the different services and especially the fact that we had to package everything into a Raspberry Pi with real-world movement. We had to leverage a cloud database to communicate with all the different end devices. Moreover, not having a GPS receiver made us look at other solutions to maintain accuracy during movement. Lastly, some APIs didn't have support in certain languages which forced us to be creative with our implementations. Accomplishments that we're proud of We are proud of the way we were able to interconnect all these systems and put it into a compelling form factor. We truly learned a lot about various areas of engineering. What's next for Rex Using GPS for more accurate positioning Capability to traverse different elevations like stairs Increasing the capabilities of the agentic system Giving the user the ability to upload designs of their own areas directly within the application Making Rex look even cooler! <div