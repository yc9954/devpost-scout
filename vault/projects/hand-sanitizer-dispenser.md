---
slug: "hand-sanitizer-dispenser"
url: "https://devpost.com/software/hand-sanitizer-dispenser"
title: "Hand Sanitizer Dispenser"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 364
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/geospatial"
---

# Hand Sanitizer Dispenser

> A non-contact hand sanitizer dispenser.

[Devpost](https://devpost.com/software/hand-sanitizer-dispenser) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**mechanism** [[sensor_fusion]]
**substrate** [[geospatial]]

**stack** arduino, arduino-nano

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges
- accomplishments
- what was learned
- next steps

## Body

Sanitizer Bottle with dispenser Lid closeup of circuit overhead shot closeup of hose holder Inspiration Covid-19 SUCKS! With everyone concerned about being clean, a perfect time to create something for people to use when visiting my office. What it does Pumps out hand sanitizer for 1/4 second: When the green LED is light, bring your hand close to the sensor and when the yellow LED turns on, wait for the red LED to turn on at which a pump of hand sanitzer will be pumped into your hand. After a short pump of sanitizer, the yellow LED will illuminate indicating it is verifying something is still close for dispensing. If nothing is there the green LED will come on indicating it is ready for next sensing, or if a hand is still present, it will pump another pump of sanitizer. How it was built Arduino IDE with a nano and a 6VDC pump and an HC-SR04 ultrasonic sensor for distance measuring. Challenges 1) After getting everything loaded and testing going well, something was funky with the sensor and was picking something up close. This was causing the pump to constantly pump out sanitizer. Had to put a failsafe in to only allow pump of four times before stopping the sensor for five minutes before re-sensing the distance to an object. 2) Had to figure out how to put it all together. It isn't the greatest looking dispenser, but it definitely shows off the geek-i-ness and I'm happy about that. 3) Finding a container that the immersible pump would fit in. Accomplishments Worked through the challenges of the failsafe and the logic necessary to make sure it worked correctly. What was learned Circuit design and mapping out using the software Fritzing. Learned how to create the schematic side of things. Working with an Arduino Nano and what was needed to change settings in the IDE to allow for connection. Next steps Change the pump out to an external pump that would allow me to drop a hose directly into the Hand Sanitzer bottle. As is right now, I'll have the bottle next to the dispenser to help people understand what is in the dispenser. <div