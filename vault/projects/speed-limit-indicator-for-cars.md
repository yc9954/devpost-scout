---
slug: "speed-limit-indicator-for-cars"
url: "https://devpost.com/software/speed-limit-indicator-for-cars"
title: "SPEED LIMIT INDICATOR FOR CARS"
hackathon: "Technica"
organization: "ISTE-VIT"
winner: true
words: 255
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/transportation"
  - "user/frontline_worker"
---

# SPEED LIMIT INDICATOR FOR CARS

> A device to indicate speed limit on highways directly on the vehicle's dashboard, to avoid unnecessary accidents due to unnoticed speedlimit signboards & to avoid fine due to this ignorance

[Devpost](https://devpost.com/software/speed-limit-indicator-for-cars) · hackathon [[Technica]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[transportation]]
**user** [[frontline_worker]]

**stack** arduino, autodesk-fusion-360, c++

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned

## Body

Inspiration Traffic signals sometimes get ignored as they are place on the side of the road. And missing such signs might cause mishaps and also may lead the car driver/owner to pay heavy challans. We wanted to make something to avoid this. What it does Using radio frequency of 433Mhz. we plan to make a beacon which would keep on broadcasting the speed limit . This signal would be received by a receiver placed in the car. After receiving the signal, the internal circuit of our device would decrypt the data and show the speed limit on the dashboard of the car. How we built it We went through the dimensions of some of the shortest cars available in the market and some suvs. we concluded that keeping the beacon at a height of 80cm from the ground level would be optimum. A structure was designed keeping in mind that the signals should be transferred in a particular direction. Then we selected the components required to build the projects and coded the Arduino to perform the job. Challenges we ran into Initially we planned to use 2.4GHz modules for transmitting and receiving data. But, later it struck our minds that 2.4GHz is widely used in communication devices, and that there would be a lot of interference . And, this might even cause our system to fail, i.e., show no or wrong values. What we learned CAD designing in Fusion360. Types of Radio Frequencies and their uses. C++ for Arduino. Different ways of wireless communication. <div