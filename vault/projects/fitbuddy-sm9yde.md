---
slug: "fitbuddy-sm9yde"
url: "https://devpost.com/software/fitbuddy-sm9yde"
title: "FitBuddy"
hackathon: "Hack the North 2020++"
winner: true
words: 365
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
---

# FitBuddy

> Competitively exercise against your friends, push yourself for a high rank, and improve your form, all from the safety of your own home.

[Devpost](https://devpost.com/software/fitbuddy-sm9yde) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]

**stack** arduino, bluetooth, c++, firebase, mpu, swift, xcode

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for fitbuddy

## Body

The FitBuddy Logo FitBuddy Device on Wrist Enclosed FitBuddy Device FitBuddy Device Interior Challenge Page XCode App Design Inspiration Before the pandemic, I would often work out at my local gym after my Grade 11 Physics Class, during lunch break It then closed so I tried to start a routine of calisthenics at home I managed to maintain the routine for a week before I naturally became lazy and gave up I had no motivation So during this hackathon, I decided to set out and find a way to bring motivation into physical activity What it does You can challenge your friends to a workout battle (pushups, situps, squats, etc.) The FitBuddy Device on your wrist monitors your form and movement with its sensors It counts your reps and updates them in the app view You push yourself until either you or your opponent forfeit There is a ranking system (Bronze, Silver, Gold, Platinum, Diamond, Ultimate) Based on your wins, losses, form, and other variables, you are assigned a rank Keep pushing yourself and try to rank up! The app computes the motion numbers through a trained algorithm that gives you tips on how to improve your form How I built it iOS App XCode + Swift Firebase + Firestore Controls Entire Back-End Friends Network Real Time Synchronization User Profiles Friend Links Email and Password Control Form Improvement Tips Other Smaller Features FitBuddy Device Arduino Nano Bluetooth LE Chip 3-Axis Accelerometer 3-Axis Gyroscope 3-Axis Magnetometer Pulse Sensor 18650 Lithium Battery + Recharge Circuit Challenges I ran into Using Bluetooth with iOS and Swift, made me crazy haha Battery Circuit Voltage Dropout Every 5 seconds Creating Physical Enclosure Accomplishments that I'm proud of The App, looks well done design-wise The Pairing Process, just tap the phone to the device! The Physical Device, doesn't look half bad! What I learned How to use BLE with iOS + Arduino How to convert Acc+Gyro+Mag angles into an accurate angle reading How to use a pulse sensor What's next for FitBuddy PCB Design with all components Clean up the app and release it to the app store Create a 3D Printed physical enclosure Create User Security Rules in Firebase <div