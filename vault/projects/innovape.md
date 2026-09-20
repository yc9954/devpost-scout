---
slug: "innovape"
url: "https://devpost.com/software/innovape"
title: "Innovape"
hackathon: "Hack the North 2019"
winner: true
words: 442
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "substrate/sensor_telemetry"
---

# Innovape

> A personalized solution to quitting smoking

[Devpost](https://devpost.com/software/innovape) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[mental_health]] [[security_privacy]]
  <sub>weak: general_public</sub>
**substrate** [[sensor_telemetry]]

**stack** arduino, expo.io, flask, juul, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for innovape

## Body

The Juul add-on. Our app. Consumer statistics. Inspiration Juul has not only taken over the e-cigarette industry, but also people's lives. Nicotine content in one Juul pod is equivalent to those in a pack of 10 cigarettes. Addiction thus becomes a serious health problem, in particular to children and teens who obtain Juuls secondhand. Juul marketing plays to their vulnerability with flavors such as watermelon and strawberry lemonade. What can we make in a weekend that can reduce nicotine dependence and allow smokers to quit smoking by transitioning using Juul? What it does We created an attachment to a Juul that allows users to control the nicotine vape rate in real time through the Innovape mobile app. Users are provided the option to start a quitting plan, with individualized goal setting and projected outcomes given user behavior. Our app stays with the user throughout their journey and asks for their emotional state. Their feedback allows us to deliver a personalized nicotine reduction algorithm for each user, with the goal that the user will not notice the reduced nicotine over time. Innovape is compatible with any Juul device. How we built it We attached an Arduino to the Juul in order to control the vaporization rate. The Arduino communicates with the mobile app through an EC2 instance, where the Arduino sends data when the user inhales, and the mobile app sends signals to control the flow rate. We used the React-native framework for the app with rapid design iteration cycles made possible by Expo. Challenges we ran into The biggest challenge was that Juul's proprietary device prevented easy communication between Juul and a mobile device. Research on nicotine replacement therapy does not show promising quit rates. Though Juul collects many metrics from their users, those data are unavailable. The lack of data posed a significant challenge on our personalized nicotine reduction algorithm. Accomplishments that we're proud of We're very proud of our user-focused design of the product, such as the beautiful user interface on the Innovape app. We managed to work with unfamiliar voltages, overcame the proprietary design of the Juul hardware, and managed to integrate hardware with software in a tight timeline. What we learned How to program Arduinos, build integrated circuitry, how to communicate between a mobile device to unrelated hardware, and apply Gaussian statistical reasoning. What's next for Innovape Integrate the hardware add-on to an embedded contraption on the Juul itself. Add more heuristics to analyze user data and trends. With more data, the diverse user data can be used to make inference on user's diseases remotely, applying machine learning on the edge, allowing for real time disease detection. <div