---
slug: "ushould"
url: "https://devpost.com/software/ushould"
title: "uShould"
hackathon: "PennApps XII"
winner: true
words: 394
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
---

# uShould

> uShould is a hardware/mobile app combo that helps gently remind people to do things repeatedly. One use-case: pills

[Devpost](https://devpost.com/software/ushould) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[sensor_fusion]]

**stack** adafruit, android, hardware, imu, ios, particle, software, web

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for ushould

## Body

Inspiration Our inspiration comes from a great book called The Power Of Habit, which talks about the how humans need to fight bad habits and rewire their brains. We want to train people to form helpful habits which will improve their daily lives and health. What it does We have a sensor that a user can stick on anything with companion Android and iOS applications. When the sensor moves, the mobile app timer is reset (Congrats, you remembered to do something and are on your way to forming a habit!). If the sensor doesn't move after a certain period of time and the timers hit zero, the iOS and Android Apps send push notifications to the user telling them to do the required activity (and thus forming a habit). How we built it After the user inputs the time frame desired for habituation, they can put a Particle core (little tiny hardware gizmo) that connects to an Adafruit 9 DOF imu motion sensor onto anything they like. When the imu motion sensor is moved, the photon sends roll, pitch and heading information via http request to our server and then to our native iOS and Android apps. Both the iOS and Android apps process the information and if the imu has moved a certain amount in 3d space we send push notifications. Challenges I ran into -How the heck do we arrange these wires? -Running background activities in iOS and Android. -Building two mobile apps simultaneously while doing hardware and configuring a server. Accomplishments that I'm proud of We have never used hardware before and decided to just jump into it. Major props to Horatio Thomas from our team for being fearless about this new space and Harsh from Lutron for calming us down when we thought hardware was simply too hard. What I learned -What a breadbox is -how to program hardware! -how to build a mobile app under extreme time constraints What's next for uShould We want to find a way to make the device smaller. Eventually we want to use an Arduino Lilypad. We feel this product could have great impact in both the medical community (for remembering to take medication) and just recreationally. It only takes 30 days to form a habit and we want to study the science behind creating positive habits that can change people's lives. kickstarter <div