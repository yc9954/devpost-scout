---
slug: "canary-lrg3ep"
url: "https://devpost.com/software/canary-lrg3ep"
title: "Canary"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 872
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/education"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Canary

> Satellite-enabled wireless sensor network for early wildfire detection.

[Devpost](https://devpost.com/software/canary-lrg3ep) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[climate_energy]] [[disaster_emergency]] [[education]]
**user** [[general_public]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** arduino, esp8266, gcp, iot, monogoto, murata, pandas, python, skylo, streamlit, udp, wifi

## How they structured the write-up

- inspiration 🔥
- our solution: canary 🐦🚨
- what sets canary apart 💡
- technology details 🖥️
- challenges and lessons 🗻
- what’s next for canary 🛰️

## Body

ESP8266 - Arduino sensor node At the beach! Monogoto Satellite NTN board Flowchart Inspiration 🔥 While on the way to CalHacks, we drove past a fire in Oakland Hills that had started just a few hours prior, meters away from I-580. Over the weekend, the fire quickly spread and ended up burning an area of 15 acres, damaging 2 homes and prompting 500 households to evacuate. This served as a harsh reminder that wildfires can and will start anywhere as long as few environmental conditions are met, and can have devastating effects on lives, property, and the environment. The following statistics are from the year 2020[1]. People: Wildfires killed over 30 people in our home state of California. The pollution is set to shave off a year of life expectancy of CA residents in our most polluted counties if the trend continues. Property: We sustained $19b in economic losses due to property damage. Environment: Wildfires have made a significant impact on climate change. It was estimated that the smoke from CA wildfires made up 30% of the state’s greenhouse gas emissions. UChicago also found that “a single year of wildfire emissions is close to double emissions reductions achieved over 16 years.” Right now (as of 10/20, 9:00AM): According to Cal Fire, there are 7 active wildfires that have scorched a total of approx. 120,000 acres. [1] - news.chicago.edu Our Solution: Canary 🐦🚨 Canary is an early wildfire detection system powered by an extensible, low-power, low-cost, low-maintenance sensor network solution. Each sensor in the network is placed in strategic locations in remote forest areas and records environmental data such as temperature and air quality, both of which can be used to detect fires. This data is forwarded through a WiFi link to a centrally-located satellite gateway computer. The gateway computer leverages a Monogoto Satellite NTN (graciously provided by Skylo) and receives all of the incoming sensor data from its local network, which is then relayed to a geostationary satellite. Back on Earth, we have a ground station dashboard that would be used by forest rangers and fire departments that receives the real-time sensor feed. Based on the locations and density of the sensors, we can effectively detect and localize a fire before it gets out of control. What Sets Canary Apart 💡 Current satellite-based solutions include Google’s FireSat and NASA’s GOES satellite network. These systems rely on high-quality imagery to localize the fires, quite literally a ‘top-down’ approach. Google claims it can detect a fire the size of a classroom and notify emergency services in 20 minutes on average, while GOES reports a latency of 3 hours or more. We believe these existing solutions are not effective enough to prevent the disasters that constantly disrupt the lives of California residents as the fires get too big or the latency is too high before we are able to do anything about it. To address these concerns, we propose our ‘bottom-up’ approach, where we can deploy sensor networks on a single forest or area level and then extend them with more sensors and gateway computers as needed. Technology Details 🖥️ Each node in the network is equipped with an Arduino 101 that reads from a Grove temperature sensor. This is wired to an ESP8266 that has a WiFi module to forward the sensor data to the central gateway computer wirelessly. The gateway computer, using the Monogoto board, relays all of the sensor data to the geostationary satellite. On the ground, we have a UDP server running in Google Cloud that receives packets from the satellite and is hooked up to a Streamlit dashboard for data visualization. Challenges and Lessons 🗻 There were two main challenges to this project. Hardware limitations: Our team as a whole is not very experienced with hardware, and setting everything up and getting the different components to talk to each other was difficult. We went through 3 Raspberry Pis, a couple Arduinos, different types of sensors, and even had to fashion our own voltage divider before arriving at the final product. Although it was disheartening at times to deal with these constant failures, knowing that we persevered and stepped out of our comfort zones is fulfilling. Satellite communications: The communication proved to be tricky due to inconsistent timing between sending and receiving the packages. We went through various socket ids and ports to see if there were any patterns to the delays. Through our thorough documentation of steps taken, we were eventually able to recognize a pattern in when the packages were being sent and modify our code accordingly. What’s Next for Canary 🛰️ As we get access to better sensors and gain more experience working with hardware components (especially PCB design), the reliability of our systems will improve. We ran into a fair amount of obstacles with the Monogoto board in particular, but as it was announced as a development kit only a week ago, we have full faith that it will only get better in the future. Our vision is to see Canary used by park services and fire departments in the most remote areas of our beautiful forest landscapes in which our satellite-powered sensor network can overcome the limitations of cellular communication and existing fire detection solutions. <div