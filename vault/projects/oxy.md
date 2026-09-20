---
slug: "oxy"
url: "https://devpost.com/software/oxy"
title: "OXY"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 996
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/patient_family"
  - "substrate/video_visual"
---

# OXY

> A 9$ custom Oximeter + Mobile app and Web App that allows continuous and remote monitoring to prevent deaths due to Silent Hypoxia and falls.

[Devpost](https://devpost.com/software/oxy) · hackathon [[AWS Graviton Hackathon]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[elder_child_care]] [[health_clinical]] [[labor_employment]]
**user** [[patient_family]]
**substrate** [[video_visual]]

**stack** amazon-ec2, amazon-web-services, arduino, flutter, graviton

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for oxy

## Body

Inspiration During the second wave of covid in India, I witnessed the unthinkable amount of suffering unleashed on the people. During the peak, there were around 400,000 positive cases per day that were reported, according to various media reports a significant amount of positive cases went unreported. Images of piles of dead bodies being cremated almost everywhere around the country left me in shock. Since then I wanted to make/contribute to helping as much as I could. I took this problem as an inspiration to make an effort. Silent Hypoxia is when a patient does not feel shortness of breath, yet their oxygen level drops drastically, this is a very dangerous situation that has claimed many lives in this pandemic. To detect Silent Hypoxia, continuous monitoring of a patient's oxygen saturation is needed, unfortunately, general oximeters available in the market are manual and must be used at frequent intervals. This is a big problem, for one, due to the extreme shortage of healthcare workers particularly in India, individual attention to patients for measuring SPO2 every few minutes is impossible, which increases the chances of Silent Hypoxia going undetected. The solution is, continuous monitoring of oxygen saturation, this feature, unfortunately, is not offered by common affordable oximeters, taking it as a challenge, I came up with a prototype solution. When a person has advanced age, they are likely to experience a decrease in physical quality, one of the weaknesses (physical decline) experienced by the elderly is a weakness in their legs, which will make them more susceptible to fall. Falling is an event that causes a conscious subject to be on the ground unintentionally. Factors that cause falls are ill-informed like stroke, slippery or wet floors, holding places that are not strong or not easily held. These days’ falls have become a major health problem, particularly in the old aged ones. According to the statistics of WHO, 646,000 fatal falls are being recorded and 37.3 million falls that are not so fatal but which needs medical treatment have occurred existing solutions include computer vision to detect if the person falls, this process is highly susceptible to lighting conditions and is very restricted when it comes to covering a wide area. For example, a camera cannot detect fall in the bathroom because there is usually no camera What it does It also solves another problem, that is of network and communications, to explain, imagine there is a patient wearing the device, which uses wifi to connect to the internet and send data to dynamodb. But if the patient goes to the bathroom, for example, the wifi connection might get attenuated due to walls and physical obstructions, another situation, in developing and undeveloped countries wifi is still a luxury and very uncommon so due to these real-world conditions, depending on just wifi and Bluetooth like most smartwatches and fitness wearables do, is a bad idea and not reliable, for this reason, oxy, along with wifi also has a GSM module that connects to the internet via GPRS, the GPRS network is available almost everywhere on earth, vastly improving reliability. How I built it The device continuously monitors data from the SPO2 Sensor and Inertial Measurement Unit, and sends the data to dynamo db through an API gateway and lambda function, it can either use wifi or GPRS to connect to the API, the only difference between wifi and gprs is, gprs uses AT commands to connect to an intermediate gateway because the module i had at hand does not support SSL. so Once the device detects oxygen levels dropping below a certain point or physical fall, Smartphone app sends a notification, so if a patient needs 24/7 monitoring of SPO2 levels, you don’t have to take out an oximeter and measure manually every five minutes which can be exhausting for patient and caretaker, also, in India and other similar countries, there was an extreme shortage of healthcare workers who can be physically present nearby patient all the time to measure the oxygen levels, so, through the web app, which is hosted on the Graviton EC2 instance, they can add as many devices they want to monitor remotely, and medical history for emergency purpose of every patient is one click away, this, can allow them to keep monitoring patients’ spo2 while they tend to other important tasks. The parameters of notification on the app are customizable, you can adjust the time intervals and threshold values to trigger notifications. The device can be powered through a battery or USB, with the microcontroller esp8266 being the brain. The device can use inbuilt wifi to connect to the internet or it can do it through GPRS and SIM800L module, it also features onboard battery charging and discharging, with overcharge and overcurrent protection. And measurement is taken through an SPO2 sensor by Melexis. The cost of making the device prototype was around 9 USD, if mass-produced the price can come down significantly. Challenges I ran into The biggest challenge was to get data from the SPO2 sensor MAX30100, although there are libraries available for it, the bad schematic design of the breakout board made it impossible to get any data. I had to physically tinker around with the tiny SMD resistors on the sensor to make sure the I2C lines of the sensor work on a logic level of 3.3V. Accomplishments that I'm proud of For me, the proudest accomplishment is to have a working prototype of not only hardware but software too. What I learned The most important skill I learned is to connect the microcontroller to AWS DynamoDB through Lambda Gateway, and also how not to burn your fingers while desoldering teeny-tiny SMD components, ouch! that hurt 😂. What's next for oxy The hardware enclosure that houses the device is must be made clamp-like or strap-on, to make it a proper wearable device, I wanted to do it right now but I lost time trying to implement the device and app. <div