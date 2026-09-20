---
slug: "pos-chair-r4j96f"
url: "https://devpost.com/software/pos-chair-r4j96f"
title: "Pos-Chair"
hackathon: "PennApps XII"
winner: true
words: 650
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
---

# Pos-Chair

> IoT seat cover that graphically helps users correct their posture in real-time, eradicating the problem of back pain

[Devpost](https://devpost.com/software/pos-chair-r4j96f) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[educator_student]]
  <sub>weak: web_dom</sub>

**stack** .co, canvas-js, google-chart, html/css, ios, javascript, jquery, linode, node.js, particle, photoshop, round-force-sensors, spark-api-for-node.js, swift

## How they structured the write-up

- inspiration
- what is pos-chair and how we built it
- personal connection
- obstacles
- our accomplishments
- what we learned
- what's next for pos-chair

## Body

Inspiration Pos-Chair is a seat cover with force sensors that interact with Sparkcore and our iOS and web applications in real time to graphically help people fix their posture to eliminate back pain, improving overall health. According to the NY Times article "Sit Up Straight. Your Back Thanks You," up to 80% of Americans experience back pain at some point in their lives, and each year 15% of all adults are treated for such problems as herniated discs, spinal stenosis or lumbar pain...Back pain is notoriously difficult, and expensive, to remedy. What is Pos-Chair and how we built it The Pos-Chair seat cover integrates force sensors to determine a person's weight distribution on the chair. Multiple Round Force Sensors strategically placed across the cover interface directly with the Particle Core IoT chip, which communicates with the iOS and Web app via Wi-Fi to provide force data for posture analysis. Depending on the weight distribution, the user will be able to monitor the quality of his/her posture through the real-time output on our Pos-Chair iOS app. The app was created with the Particle iOS Cloud SDK and communicates with a Particle Internet Button for rapid transfer of sensor information. We have also created a web application that provides a clean presentation of our product, and offers login service allowing users to view graphical real-time data from their Pos-Chair on the web as well as through our app. Personal connection Our inspiration for Pos-Chair comes from personal experiences and a need we see to decrease back pain associated with sitting long hours in the workforce. With Pos-Chair, people have access to the iOS app or web application which will notify them how to correct their sitting position. With practice, users can identify a correct sitting position, improve their posture long-term and decrease risk of pain and more serious back problems at a relatively low cost. Because Pos-Chair is a cover for a chair it can be used on any chair and is transportable. No sensors are attached to the person. Pos-Chair cover has application to help employees work better because with good back positioning they experience decreased discomfort and pain. As a team comprised of undergraduate and Ph.D students, we have identified application for Pos-Chair in any situation which requires the user to sit whether that be in a class lecture, at a research desk, at work, or at home. When people decide to use Pos-Chair, they are correcting their posture - reducing pain and risks such as herniated discs, spinal stenosis and lumbar pain - and improving their overall health with cutting edge technology at the forefront of ergonomics. Obstacles We experienced a number of unforeseen setbacks such as outdated API’s and malfunctioning hardware during our time at PennApps. Our most significant obstacle was compatibility between our distance sensor, an Adruino Uno, and our Sparkcore, which inhibited us from obtaining certain posture-related information. Our accomplishments There was a critical point during our project when we made the decision to abandon our relentless efforts with a particular distance sensor. However, our ability to work together as a team of innovators allowed us to bypass the problem by implementing other hardware in a unique way to obtain other valuable posture-related information. What we learned Over the past two days, we were extremely lucky to be able to interact with some of the best hackers in the world. From iOS to Particle to web server operations, each of us was able to pursue our own interests while creating a societally beneficial project with advice from both our peers and leading industry experts. What's next for Pos-Chair In order to make our cross-platform app more powerful, we plan to connect more sensors to our Particle IoT device. This would provide us with more information of the user’s long-term habits, needs, and progress, thus enabling the app to suggest improved ways in mitigating posture-related pain. <div