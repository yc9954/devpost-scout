---
slug: "remote-elderly-home-care-via-privacy-preserving-surveillance-dano89"
url: "https://devpost.com/software/remote-elderly-home-care-via-privacy-preserving-surveillance-dano89"
title: "Remote Elderly Home Care via Privacy Preserving Surveillance"
hackathon: "COVIDathon - Decentralized AI Hackathon"
organization: "SingularityNet"
winner: true
words: 492
team_size: 27
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/sensor_fusion"
  - "domain/disaster_emergency"
  - "domain/elder_child_care"
  - "user/patient_family"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Remote Elderly Home Care via Privacy Preserving Surveillance

> COVID19 isolated at home many of us, including our elderly family members. Left unattended they are prone to risks such as falls, gas leaks, flooding, fire and others.

[Devpost](https://devpost.com/software/remote-elderly-home-care-via-privacy-preserving-surveillance-dano89) · hackathon [[COVIDathon - Decentralized AI Hackathon]]

## Facets

**mechanism** [[privacy_tech]] [[sensor_fusion]]
**domain** [[disaster_emergency]] [[elder_child_care]]
**user** [[patient_family]]
**substrate** [[video_visual]] [[web_dom]]

**stack** javascript, pwa, python, raspberry-pi, tensorflow, webrtc

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for remote elderly home care via privacy preserving surveillance

## Body

privacy preserving person face detection at home Plug and Play AI device discovery home page person detection indoors person detection outdoors Inspiration COVID19 isolated at home many of us, including our elderly parents and grandparents. Not being able to check on them regularly elevates the risks that they are exposed to such as falls, gas leaks, flooding, fire and others. What it does Ambianic.ai is an end-to-end Open Source Ambient Intelligence project that removes the stigma associated with surveillance systems by implementing privacy preserving algorithms in three critical layers: Peer-to-Peer Remote access Local device AI inference and training Local data storage Ambianic.ai observes a target environment and alerts users for events of interest. Data us only available to homeowners and their family. User data is never sent to any third party cloud servers. Here is a blog post that goes into the reasons why we started this project: https://blog.ambianic.ai/2020/02/05/pnp.html And here is a technical deep dive article published in WebRTCHacks. It clarifies that it is absolutely possible to build a privacy preserving surveillance system, despite popular cloud vendors making us believe that all user data belongs safely on their cloud servers: https://webrtchacks.com/private-home-surveillance-with-the-webrtc-datachannel/ How I built it Ambianic.ai has 3 main components: Ambianic.ai Edge: a Python application designed to run on an IoT Edge device such as a Raspberry Pi or a NUC. It attaches to video cameras and other sensors to gather input. It then runs inference pipelines using AI models that detect events of interest such as objects, people and other triggers. Ambianic.ai UI: A Progressive Web App written in Javascript using Vue.js and other front end frameworks to deliver an intuitive timeline of events to the end user. Ambianic.ai PnP: A plug-and-play framework that allows Ambianic UI and Ambianic Edge to discover each other seamlessly and communicate over secure peer-to-peer protocol using WebRTC APIs. Challenges I ran into Challenges include selecting high performance, high accuracy and low latency AI models to detect events of interest on resource constraint edge devices. Another challenge is taking into account user local data to fine tune AI models. Pre-trained models can perform reasonably well, but they can be improved with privacy preserving federated learning on unique new local data. Accomplishments that I'm proud of Ambianic.ai has been in public Beta for several weeks helping a number of users in their daily lives. Some users report success in keeping an eye on their elderly family members: https://twitter.com/mchapman671/status/1230931722650423299 What I learned Although the project sets ambitious goals, there seem to be sufficient enabling Open Source frameworks and community momentum to drive the ongoing success. What's next for Remote Elderly Home Care via Privacy Preserving Surveillance We need to work on these major areas: Recruit volunteers in the home care community to test the system and provide feedback Select more models to address open use cases such as fall detection, gas leaks and others Work on implementing Federated Learning infrastructure to fine tune initial pre-trained models. <div