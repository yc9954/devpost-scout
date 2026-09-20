---
slug: "smart-sprout-ponbhq"
url: "https://devpost.com/software/smart-sprout-ponbhq"
title: "Smart Sprout"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 412
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/civic_government"
---

# Smart Sprout

> Smart Sprout uses real-time soil moisture data and an Arduino-powered motor to precisely deliver water to your plants, ensuring they thrive while giving you live readings of their moisture levels.

[Devpost](https://devpost.com/software/smart-sprout-ponbhq) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[civic_government]]

**stack** arduino, c++, sensorlogic

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smart sprout

## Body

Inspiration Our inspiration for Smart Sprout came from our passion for both technology and gardening. We wanted to create a solution that not only makes plant care more convenient but also promotes sustainability by efficiently using water resources. What it does Smart Sprout is an innovative self-watering plant system. It constantly monitors the moisture level in the soil and uses this data to intelligently dispense water to your plants. It ensures that your plants receive the right amount of water, preventing overwatering or underwatering. Additionally, it provides real-time moisture data, enabling you to track the health of your plants remotely. How we built it We built Smart Sprout using a combination of hardware and software. The hardware includes sensors to measure soil moisture, an Arduino microcontroller to process data, and a motorized water dispenser to regulate watering. The software utilizes custom code to interface with the hardware, analyze moisture data, and provide a user-friendly interface for monitoring and control. Challenges we ran into During the development of Smart Sprout, we encountered several challenges. One significant challenge was optimizing the water dispensing mechanism to ensure precise and efficient watering. The parts required by our team, such as a water pump, were not available. We also had to fine-tune the sensor calibration to provide accurate moisture readings, which took much more time than expected. Additionally, integrating the hardware with a user-friendly software interface posed its own set of challenges. Accomplishments that we're proud of The rotating bottle, and mounting it. It has to be rotated such that the holes are on the top or bottom, as necessary, but the only motor we could find was barely powerful enough to turn it. We reduced friction on the other end by using a polygonal 3d-printed block, and mounted the motor opposite to it. Overall, finding an alternative to a water pump was something we are proud of. What we learned As is often the case, moving parts are the most complicated, but we also are using the arduino for two things at the same time: driving the motor and writing to the display. Multitasking is a major component of modern operating systems, and it was interesting to work on it in this case here. What's next for Smart Sprout The watering system could be improved. There exist valves that are meant to be electronically operated, or a human designed valve and a servo, which would allow us to link it to a municipal water system. <div