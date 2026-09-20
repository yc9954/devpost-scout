---
slug: "bikepals"
url: "https://devpost.com/software/bikepals"
title: "BikePals"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 467
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "user/educator_student"
---

# BikePals

> Challenge your friends to high-stakes bike races, compete for a high rank, and stay healthy & active, all while ensuring complete social distancing and no physical interaction.

[Devpost](https://devpost.com/software/bikepals) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[education]]
**user** [[educator_student]]

**stack** arduino, firebase, sensors, swift, xcode

## How they structured the write-up

- introduction
- issue/inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bikepals

## Body

BikePal Device Closeup Inside the BikePal Device BikePal Device Front Home Page Friends Page New Challenge Page In Competition Page Previous Races Page Improve Page Hall Effect Sensor Hall Effect Sensor Mounted on Rear Wheel Hall Effect Sensor Mounted on Rear Wheel Closeup Introduction We're two students from Canada currently in our 12th year of high-school who love solving real-world problems with the help of programming and technology Issue/Inspiration The pandemic has decreased average daily physical activity by half We can see this in our own lives as well - there is no more motivation for exercise Biking is a common, enjoyable, and non-strenuous exercise, but it is quite boring when done alone What if we renew interest in biking WITHOUT having people meet up, thus maintaining the COVID protocol and also increasing physical activity What it does BikePals is an all in one solution to biking with your friends from a safe distance It is a two-part solution BikePal Device BikePal App The BikePal device tracks your speed, pedal RPM, pulse, elevation, etc. and sends that information over to the app Through the app, you can challenge your friends to competitive bike rides You can set a distance and a time, and your goal is to bike that distance within the time limit and before your friend does Based on your wins, losses, and other factors, you are given a rank, ranging from bronze to supersonic! The app also uses your biking information to give you tips on how you can improve your biking technique and form How we built it iOS App XCode + Swift Firebase + Firestore Controls Entire Back-End Friends Network Real Time Synchronization User Profiles Friend Links Email and Password Control Form Improvement Tips Other Smaller Features BikePals Device Arduino Nano Bluetooth LE Chip Hall Effect Sensor 3-Axis Accelerometer 3-Axis Gyroscope 3-Axis Magnetometer Pulse Sensor Rechargable Battery Challenges we ran into Getting the hall effect sensor to output when it is faced with the magnet (forgot the pull-up resistor) Sending the data from the BikePal Device to the iOS App Making the outer physical enclosure Accomplishments that we're proud of Getting the entire project working in time! The pairing process, just tap to pair! We really feel that it is quite exciting and motivating We have high hopes that it will improve physical activity levels in the real world market To have made something for our bikes! Being in high school, it is our main mode of transportation What we learned How to use a hall effect sensor Sending raw data over BLE Arduino Interrupts Firebase User Management with Email Linking What's next for BikePals A PCB board for the electronics A 3D printed physical enclosure Enhancing the Firebase Security Rules Releasing the App to the App store and receiving feedback <div