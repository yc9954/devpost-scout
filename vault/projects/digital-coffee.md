---
slug: "digital-coffee"
url: "https://devpost.com/software/digital-coffee"
title: "Digital Coffee"
hackathon: "PennApps XII"
winner: true
words: 286
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
---

# Digital Coffee

> Glasses that wake you up when you drift off to sleep.

[Devpost](https://devpost.com/software/digital-coffee) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[sensor_fusion]]

**stack** arduino, c, c++, ionic, ir-sensor, javascript, pebble, photon

## How they structured the write-up

- what it does
- how it was built
- challenges we ran into
- what's next?

## Body

What it does DigitalCoffee wakes you up when you doze off. The glasses vibrate when your eyes close for too long, and also causes your Pebble watch to vibrate. How it was built DigitalCoffee was built with an arduino, photon, pebble, and android phone. The arduino processes all of the information, and the photon uploads the information to a server. The server sends data to your phone, which in turn forwards the data via bluetooth to the pebble. The IR sensors detect eye movement - blink frequency and duration. There is also a tilt sensor to detect head motion. The vibration motors trigger as long as the sensors detect signs of sleeping. The blink information is forwarded to the phone app for analytics; one can see when he/she is most sleepy. Lastly, the pebble app displays raw values and alerts you via vibration/notification. The glasses were designed and 3d printed. We used multiple breadboards, wires, and parts to do everything. Also included: a button to calibrate the IR sensors. Challenges we ran into Getting all the hardware to work properly. The biggest challenge was getting the photon to accept and transmit data from the Arduino Uno. We ran into some serious problems with transmission using RX and TX pins, but we were able to use I2C instead. It would have been much harder without Pennapps' great mentors. The hardware was also hard to calibrate as there were multiple issues with sensitivity. What's next? Minimizing the cables, making the entire module more wireless/light, more analytics and information, various smart options controlled via blinking. If this was designed as a product, it would be much less bulky, with a similar, if not smaller profile than Google Glass. <div