---
slug: "headsup"
url: "https://devpost.com/software/headsup"
title: "HeadsUp"
hackathon: "PennApps XII"
winner: true
words: 632
team_size: 3
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/video_visual"
---

# HeadsUp

> Diagnose potential traumatic brain injuries quickly, cheaply, and conveniently.

[Devpost](https://devpost.com/software/headsup) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[video_visual]]

**stack** google-cardboard, javascript, led, node.js, opencv, particle, ps3-eye, rest, websockets

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for headsup

## Body

Inspiration Concussions suck - both I and my teammates have had many friends struggle through the aftermath of receiving one though their sport or an unfortunate circumstance. However, one may almost say they're lucky, as they were people who figured out the had concussions and were able to have them treated. Almost half of all athletes don't report feeling symptoms after receiving a concussive blow, and a total of 1.6-3.8 million concussions occur in the United States every year (estimated by the CDC)l In order to address the major problem of concussions in youth sports, adult sports, and the mayhem of everyday life, we realized that a better system was needed - one that could be close and accessible , affordable for all teams, and easy to use . What it does HeadsUp uses a common diagnostic methodology, the tracking of patient's eye movements in response to stimuli . The difference between HeadsUp and the cheapest hospital equipment? A factor of almost 100 . Commercial hospital equipment runs $5,000 at minimum, and can run up to $25,000, which would mean HeadsUp was a factor of almost 470x cheaper! The secret lies in the hardware used. How I built it Parts list: 1 Google Cardboard: $6.99 2 PlayStation Eye Cameras: $9.98 ($4.99/each) 1 Spark Core: $35.00 4 LED's: ~$2.00 Total: $53.97 Using excess cardboard and some glue, we mounted the PS Eye cameras in the Cardboard. Then, we soldered in the LED's to the Spark Core, and it was ready to go (sans software of course). While the hardware process sounds very simple, it required many iterations to get right, and features were added as we realized the specifications needed to be tightened up. To further reduce cost , one could easily use a cheaper micro controller (e.g., the Photon , for $20, bringing the total cost down to $38.97 ). On the software side, we used OpenCV to track the eyes of the person being evaluated. The OpenCV OS X application is passed a data source video recorded from the PS3 Eye cameras via Syphon , an open-source OS X framework that allows applications to share video between each other. The OS X application communicates with the Spark via WiFi , and triggers the LED's to turn on or off, resulting in user eye movements, which the OpenCV algorithm then processes. After the processing, the data is sent off to the cloud via WebSockets , where doctors can view the data, manage their patients, and start and stop tests. Challenges I ran into Tracking eyeballs and figuring out the position of the pupils in two dimensions is highly non-trivial, and it took significant amounts of time to develop an algorithm using OpenCV to build a proper eye tracking system that would tell us which direction the eyes were looking in. Integrating the OpenCV C++ app with WebSockets for the web-based "Doctor View" portion also proved somewhat difficult, though it was completed in the end. Our Spark also refused to connect to the WiFi for a while, so we lost some time trying to fix that. :) Accomplishments that I'm proud of The OpenCV algorithm is both quite impressive and surprisingly accurate . Since it also took a lot of work both in thinking about it and coding it, it makes the victory of making it work even more sweet. What I learned WebSockets, more about OpenCV, some hardware, Google Cardboard, the amazing value of the PS3 Eye cameras, and how to explode an LED (process: don't be careful). What's next for HeadsUp HeadsUp will add further (IR) LED's and continue to receive eye tracking algorithm improvements for better tracking. Ideally, it will also be tested at our local high school , but that is dependent upon the feeling of the administrators. <div