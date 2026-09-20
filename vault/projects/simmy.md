---
slug: "simmy"
url: "https://devpost.com/software/simmy"
title: "Simmy"
hackathon: "Google’s Immersive Geospatial Challenge"
organization: "Google"
winner: true
words: 848
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Simmy

> AR project to turn the facade of MIT's Simmons Hall into a playable interface. Windows becomes buttons that play notes and launch 3D animations. The aim is to delight students and attract visitors.

[Devpost](https://devpost.com/software/simmy) · hackathon [[Google-s Immersive Geospatial Challenge]]

## Facets

**domain** [[developer_tools]] [[education]]
  <sub>weak: finance_payments</sub>
**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** adobe-aero, google-geospatial-creator

## How they structured the write-up

- inspiration
- what it does
- categories
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for simmy
- credits

## Body

Inspiration Simmons Hall at MIT is part undergraduate dormitory, part public art. The building has a memorable sponge-like structure with a large grid of pixel-like windows. Many students pass by it every day, and visitors to MIT often walk over to take photos of the dorm. I have always been struck by how the facade of Simmons resembles minimal button-grid controller interfaces: Monome Grid ( https://monome.org/docs/grid/ ) Yamaha Tenori-on ( https://www.yamaha.com/en/about/design/synapses/id_005 ) These elegant devices have no obvious mappings for their buttons and they are all the more inviting for us to tap and press to see what happens. For this hackathon, I decided to turn the Simmons facade into a playable interface. Powered by geospatial AR tools from Google and Adobe, Simmy places a digital layer precisely onto the building's surface, and the windows on the facade become tappable buttons that play notes and launch 3D animations. The aim is to delight students anew and attract more visitors by augmenting the striking architectural design. What it does 3 rows of square windows on the Simmons facade are turned into tappable square buttons. Each of the 3 rows of windows represents a different instrument. The 3 instruments are piano, guitar, and cello. When a window-button is tapped, a corresponding note is played, and a 3D animation of the note letter pops out and spins upwards into the sky. Piano notes are red, guitar yellow, and cello blue. Each row has 22 tappable windows to represent 3 octaves of C major scale. Different notes appear at different distances from the facade and rise to different heights depending on the note's instrument and octave. Categories I am submitting Simmy in the Travel & Local Discovery category. MIT is visited by many people every day from all over the world, and Simmons is one of the many wonderful pieces of public art and architecture on view around MIT campus. A broader goal for my project was to propose making the MIT campus tour a more interactive experience through AR - and making MIT a more memorable place to visit. I would also like to ask Simmy to be considered under the category of Entertainment & Events. The project transforms a building's surface into an audiovisual device that can be played live. I believe it fits under this category as well. How we built it Simmy was built with Google Geospatial Creator and Adobe Aero. First, I used Aero to build the grid of window-buttons. Each window-button has an associated sound sample of a note and 3D model of a letter. When a tap trigger occurs on a window-button, the different behaviors play the note and animate the 3D model. Next, when ready with the grid, I switched to the location anchor as powered by Geospatial Creator, and I spent some time on location at Simmons to refine the precise placement of the Aero app. Challenges we ran into I had trouble initially with the location anchor: it was difficult to get a consistent and stable anchored positioning for my objects. Moving the anchor away from the facade of the building some distance helped. Aero has no classes of objects, so I could not make one window-button from which I would instantiate. Instead, I had to build one window-button exactly as I wanted, and then duplicate it many times to put together the grid - all at the last minute. This made debugging and refining window-buttons time-consuming. Originally I had hoped to cover the entire Simmons facade with buttons. However, due to performance reasons, I had to scale back. Accomplishments that we're proud of I had always wanted to play with MIT's public art and architecture in AR, so I'm very happy to have done so for this hackathon. I'm happy to have made the project idea using Aero. I feel I have a better understanding of how to design and implement AR projects with Aero given its strengths, features, and encouraged work process. What we learned Objects in geospatial AR are difficult to design without iterating at the intended location. I learned that testing early and often would have saved me time, for example in determining the most suitable scale and speed of movement of my 3D objects. Geospatial AR is tough to test outside when it's winter. brr What's next for Simmy I want to see the 3D letters interact with both the building facade itself and each other. Letters bouncing off the facade or bumping into each other would be fun to try. Some type of networked multi-player feature would be fun. One can imagine more than one person playing at the same time, and others being able to both play and see the results of other people's playing. Credits All assets below were used under the CC Attribution license. Bubble Letters 3D models by rhcreations ( https://sketchfab.com/3d-models/bubble-letters-ef49e3ea68f04223b173d86991c77d1c ) Piano FF sound pack by jobro ( https://freesound.org/people/jobro/packs/2489/ ) real cello notes sound pack by flcellogrl ( https://freesound.org/people/flcellogrl/packs/12408/ ) Notes on nylon strings sound pack by Kyster ( https://freesound.org/people/Kyster/packs/7398/ ) Liquid 100.wav sound track by patchen ( https://freesound.org/people/patchen/sounds/20168/ ) <div