---
slug: "canqnx"
url: "https://devpost.com/software/canqnx"
title: "QNXMobility"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 505
team_size: 3
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/housing_homeless"
---

# QNXMobility

> In a world where productivity is everything, every second counts, time spent away from the desk is time wasted. With, QNXMobility move around your workspace with ease, speed and greater efficiency.

[Devpost](https://devpost.com/software/canqnx) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[housing_homeless]]

**stack** o-drive, python, qnx

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for untitled

## Body

Inspiration Our team happened to have access to an a few hub motors used for bracket bots early in the competition. With our team being robotics enthusiasts, having access to these motors meant we had to build something that moves. We decided to build a swerve drive base as it allows driving in any direction and decided to put a chair on it as a swerve completely changes up how people can get from point to point without every having to get up. We wanted to implement a unique way of control which would let the user tilt in the direction they want to go to. The more they tilt, the faster they travel! What it does The control uses and IMU to get a reading of the users posture. A neutral position keeps the user in their location, but deliberate leaning starts to move the user slowly in the direction their choice. Each swerve module consists of a drive motor and a turn motor. The turn motor lets the module face in any direction, allowing for driving forward and backward, side to side and even at diagonals. The drive motor control the speed at which the user is moving. How we built it The drive base was built around a custom designed swerve drive module. The swerve drive module consisted of the hub motor, connected to the turn motor using a hex shaft. The housing for the motors and shafts were 3d printed and mounted on to a piece of aluminum extrusion which served as the body of the module. We copied this design 4 times, and build an aluminum extrusion frame for the hardware to mount on to. We CNC cut some plates out of aluminum which is where the modules mounted on to the frame. The hardware is controlled using o-drive FOC controllers for brushless materials, The core of the software was the QNX raspberry pi kit, which interfaced with an IMU which determined how the swerve would move. The pi would do some of the kinematics before sending commands to the o-drive controllers. Challenges we ran into Building this complex of a mechanical system in this amount of time was definitely the biggest challenge. Though we had our design down early, printing, manufacturing, and testing took many hours. We also needed to redesign some parts to be stronger to be able to take on the large loads it would be placed under, Interfacing this machine with QNX was also a challenge as it didn't natively have libraries built in for what we wanted. Accomplishments that we're proud of We are proud of the fact that we could build a working swerve. Building a swerve drive is a difficult to start with, but to build one to carry a person with limited metal machining and time is even harder. What we learned We learned to use QNX RTOS without hardware projects. This technology enabled our project to have professional aspects similar to what's used in the industry. What's next for Untitled <div