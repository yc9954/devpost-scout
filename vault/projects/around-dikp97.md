---
slug: "around-dikp97"
url: "https://devpost.com/software/around-dikp97"
title: "ARound"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 556
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ARound

> ARound is a voice-driven augmented reality search, guide, discovery, and communication tool for the nearby world.

[Devpost](https://devpost.com/software/around-dikp97) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]]
**substrate** [[geospatial]] [[video_visual]]

**stack** agora, augmented-reality, ios, scenekit, swift, text-to-speech, tomtom, video-call, voice-recognition, xcode

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for around

## Body

Inspiration Augmented reality will impact the way we interact with the world. ARound is my attempt to bring today's AR technology to a common user with a voice interface, and useful tools powered by TomTom to discover the world around them. What it does The voice interface allows a user to simply query ARound with what they're interested in locating. For example, "pizza" will find local pizza restaurants. ARound uses TomTom to query the user's vicinity, and displays results as markers on an augmented reality view of the world. Tap a marker for additional information and interactive options like directions, calling, etc. The call button opens an in-app video chat with a user at the other end. This could be the hostess at a restaurant, or the owner of a store, for example. How I built it I used Xcode and wrote the app in Swift, integrating the TomTom SDK for searches and native coding for the AR view, text-to-speech, and voice-recognition interfaces. SceneKit is used to render pins/labels in the AR view, which are placed based on their distance and orientation to you. Challenges I ran into Getting a two-way voice / speech interface working in iOS has a lot of challenges as voice input and speech output collide using common resources. The TomTom SDK took a while to understand and interface with the info I needed. Mapping coordinates to spatial locations in the AR view was a difficult task, and orchestrating the virtual views (pins/labels) is still a challenge. The accuracy of determining North has lead to rotated coordinate spaces when the measurement is off. The video chat was also a challenge to integrate as there are many video properties / format options and signaling / initial condition and teardown considerations. Accomplishments that I'm proud of The whole service works fairly seamlessly and is relatively intuitive. There are no complex controls or menus for the user to deal with. Integrating all of these services was quite a challenge. What I learned A two-way audio interface (voice in / text-to-speech out) was very challenging to get working. It was very easy to crash the app due to hardware resource conflicts with no indication of the cause. It took me quite a while to find the right balance and methods to switch between the two. I think this is an area Apple could improve upon to better enable third-party voice assistants. I also learned how far off an iPhone can be from true north. Unfortunately it's not a simple measurement one can read. I'm still working on ways to calibrate the app while it's running to better lock-in the best value. What's next for ARound There are two active areas I'm looking at - directions and friend search. While I can pull walking directions from TomTom, translating those into a marked path in the AR space is still a work in progress. I'd also like to implement a person search for connecting with your friends / associates in the area. For example you might be meeting someone in the area, and ARound should be able to guide you to them, and provide a video chat if needed. Beyond those two, I'd like to enhance the venue information (perhaps with Yelp data on ratings, hours, or photos), and build out a recommendation engine and advertising platform. <div