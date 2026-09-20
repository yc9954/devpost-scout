---
slug: "iot-desk-assistant"
url: "https://devpost.com/software/iot-desk-assistant"
title: "Study Desk Assistant"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 696
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# Study Desk Assistant

> Desk Assistant designed to make students more focused and productive.

[Devpost](https://devpost.com/software/iot-desk-assistant) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]]

**stack** arduino, ardunio-uno, c++, chatgpt, dht11, javascript, ky-037, node-red, photoresistor, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learnt
- what's next for study desk assistant
- ai tools disclosure
- team members

## Body

Code I have written in C++ that uses Serial Communication to take the sensor readings and parse them into a JSON format. Online computer dashboard of the Study Desk Assistant Top-down view of the hardware (DHT11, Photoresistor, KY-037, Arduino Uno R3, Breadboard) Inspiration Many students struggle with being focused and productive and unbeknownst to them, it can be tied back to their study environment. Barley any reliable tools have been make for student with the sole purpose of being able to notify students of their study environment with temperature, humidity, light and sound levels, whilst also sending notifications and giving tips on how ot better improve their environment. What it does The Study Desk assistant utilizes sensor readings (temperature, humidity, light, sound) and data and displays them to a dashboard easily accessible by the user to get a quick look at their environment, also sending phone notifications and emails to the user when there are major changes in the sensor readings to better alert them and giving tips on how their can improve their environment with the end goal of giving insight to the user and making them more productive and focused. How I built it I began by utilizing sensors, DHT11 for the temperature and humidity, Photoresistor for the light level, and a KY-037 for the sound level. I have connected these sensors to an Arduino Uno R3 and used Serial Communication to take the sensor readings and parse them into a JSON format in C++, which then was accessed by my Raspberry Pi 5. Using Node-Red on the Raspberry Pi and connecting my Arduino Uno to it, Node-Red was able to access the Serial Communication I had built earlier and used the parsed JSON format to extract specific sensor values which were outputted as clean graphs easily accessible by the user. I have also accessed a local server, which allowed me to send notifications to my phone and send emails about major changes in the environment whilst giving me tips. Challenges I ran into The one of the biggest challenge I had run into was the creation of the phone notification and email tips system. Learning how to properly access the sensor values in a way that would check them whilst also keeping track of major changes of the sensors over time to give proper tips that were not repetitive made me think outside the box so that I would not get extreme spammage of notifications just from an extremely small change detected. Accomplishments that I am proud of Though I had built multiple projects dealing with sensors and graphs, this was the first time I had properly incorporated all of them together into one seamless app. This was also my first time playing around with a notification and email system, and I am proud to say that it has worked much better than I could have ever expected, being able to access a server and give the user insight leverage this project to a whole nother level. What I learnt From this project, I have learnt many about seamless integration to multiple technologies towards one goal, seamlessly combining sensor readings onto a dashboard whilst also making a tips system giving the user a better insight. What's next for Study Desk Assistant I would love to add Alexa integration to this project, eliminating the need of the distraction of looking at another app in the middle of your work to get the sensor values of your room. Having an Alexa connected to this would allow someone to simply ask their Alexa for the sensor values and it can give them a quick summary so they can continue their work without being distracted. Notifications would also work much better, as an Alexa would eliminate the need of looking at your phone for update which could lead to another doom scroll session (I am very guilty of this). AI Tools Disclosure I have used ChatGPT to create the environment tips that I use when my program sends out a phone notification and email. Team Members I have built this project all by myself with aided external help for the generation of the tips from ChatGPT. <div