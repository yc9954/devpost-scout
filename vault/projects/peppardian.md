---
slug: "peppardian"
url: "https://devpost.com/software/peppardian"
title: "Peppardian"
hackathon: "Junction 2017"
winner: true
words: 1043
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/labor_employment"
  - "substrate/video_visual"
---

# Peppardian

> Monitor streets and save people with a help of Pepper robot!

[Devpost](https://devpost.com/software/peppardian) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[labor_employment]]
**substrate** [[video_visual]]

**stack** bash, bottlepy, opencv, pepper, python, tensorflow

## How they structured the write-up

- motivation
- the solution
- practical design
- why not just put cctvs everywhere?
- the demo
- accomplishments that we're proud of
- what we have learned
- what's next for peppardian
- references

## Body

Example of situation where the classifier detected failed person. The robot will be instructed to go and offer some help. Example of situation where the classifier classified persons as not falling/failed. The robot will continue monitoring. Another example of situation where the classifier detected failed person. The robot will be instructed to go and offer some help. Motivation Nowadays cities are missing a required human force to monitor streets in real-time. Either budget consideration or simply an absence of qualified employees makes it impossible to detect and promptly react to such accidents like sudden health disorders, car crashes or criminal activities. Also it is very hard job for the human workers, because it involves long hours of walking and monitoring and being extremely careful about everything that is happening near the agent. People tend to become frustrated, feared or simply ignorant when encountering such events which prevents a particular person from notifying respective authorities immediately. Sometimes there are simply no witnesses of what is happening so the help can't arrive in time. The Solution We propose to compensate for a luck of personnel by using pre-trained robots and an optional net of sensors all over the city. Robots do not suffer from the same psychological issues as human beings and they can be deployed as needed with a minimal cost and no manual coaching. Robots can monitor streets reacting to a certain stimulus like a person falling down on a pavement, car accidents, explicit aggressiveness or gun-fire and quickly call a respective authorities (i.e. police, ambulance etc.) for help. Additional sensor nets (loudness, temperature etc) deployed in a city can guide robots to places when a particular disruption took place even quicker. Robots can use face identification algorithms and GPS sensors to provide some structured reports to the authorities about specific incident and if needed it will notify relatives. Practical Design All the hard-lifting like event recognition, analysis and determination of an action to make we propose to be done in a cloud. A distributed detection system will process image snapshots, determine any threats and instruct a particular robot on what actions they should take (like talk to a person, offer a help or make a warning or even call a police). Robots can be made quite cheap using affordable hardware components as they do not need to do any heavy processing on-spot. Basically, the requirements are: mobility, cameras, speaker and Internet connection. Why not just put CCTVs everywhere? At this point you may be asking: "Ok that's interesting, but how is it better then putting CCTV's everywhere?" Interactivity Robot can move and talk to people and this this gives to it huge power. They can collect information from witnesses and video recordings, analyze it and give the hottest parts to the authorities. It can also be accessible as an information point at time when everything looks ok on the street or on big touristic destinations. Mobility CCTVs are static and if we left some region of interest uncovered we will never be able to monitor it unless we put a new CCTV there, but robot can easily move there and analyze the current situation. CCTVs are not automatic CCTVs itself should have either human analyzing the stream from each of them, or be equipped with the same kind of classificators as we propose for the Robots ecosystem. The Demo We made a simple but handy demo (a.k.a. proof of work) where Pepper robot detects a human falling down and takes action. By asking "Are you all right?" robot requires a person to answer with a particular phrase to confirm a false-positive. If that person do not respond intact the robot calls an ambulance reporting an emergency: a human fall sick, needs help and is located at a certain spot in the city. We use a pre-trained TensorFlow model together with OpenCV library to detect a posture of a person. If the person is crouched, crippled or is laying on the ground the robot presumes an emergency and prompt for a confirmation from that person. In a case when a person do not respond as expected we use a 46Elks API to make a call to a test number reporting that a person at location X needs help. In this demo we try to minimize a load on a robot processing facilities while relying on a remote machine provided to do a detection part and our laptop to orchestrate the chain of actions. Accomplishments that we're proud of These 1.5 days we spend working as a team of 3 people. At first we were working on ideas about what and how we can do. We had multiple ideas, and in this post the final version of the idea is described. We learn better how to work in a team. We have distributed different tasks among 3 of us to achieve best results in a shortest periods of time. One of the major sources of the happiness that the thing that we were working on worked, we tested it and the Robot tried to call the fake emergency service and notify about accident. What we have learned We had an opportunity to work and learn Pepper robot API and write some applications using it which was very impressing, as it is the first such experience for all of us. Interacting with Pepper is fun. We worked with some totally new technologies to us as Azure and Bottle. And gain more knowledge about networking and how algorithmically hard tasks of computer vision can be solved using modern Deep Convolutional Network approaches. What's next for Peppardian Actually the thing that we developed is more valuable as an idea, because in 1 day it is hard to implement something powerful and robust, we concentrated on a small subset of the idea, to develop proof of the concept. So the potential future work should include: defining hardware architecture developing robust software layer design which will be easily scalable gathering data for all kind of classifiers that can be used setuping the Peppardian networks together with the clouds in some areas for fine tuning profit from the fact that hard human work was automated :) References Tensorflow pose estimation 1 Tensorflow pose estimation 2 Tensorflow pose estimation 3 <div