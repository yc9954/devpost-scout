---
slug: "pytorch-driving-guardian"
url: "https://devpost.com/software/pytorch-driving-guardian"
title: "Pytorch Driving Guardian"
hackathon: "PyTorch Annual Hackathon 2021"
organization: "Facebook"
winner: true
words: 690
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# Pytorch Driving Guardian

> Pytorch powered convolutional neural networks that monitor a driver alertness, emotional state and blind spots through an embedded device and cameras.

[Devpost](https://devpost.com/software/pytorch-driving-guardian) · hackathon [[PyTorch Annual Hackathon 2021]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]] [[civic_government]] [[transportation]]
**user** [[frontline_worker]]
  <sub>weak: legal_professional</sub>
**substrate** [[video_visual]]

**stack** pytorch

## How they structured the write-up

- theoretical support:
- full solution diagrams:
- models
- commentary:

## Body

Three networks for the solution. Neural Network architecture Complete setup blind spot monitor Setup Monitor LCD SMS system Hi! If you are a judge and want to review the models running in GoogleColab here are the notebooks. Drowsiness: https://github.com/altaga/Pytorch-Driving-Guardian/blob/main/Hardware%20Code/Jetson%20Code/Drowsiness/Drowsiness.ipynb Emotions: https://github.com/altaga/Pytorch-Driving-Guardian/blob/main/Hardware%20Code/Jetson%20Code/Emotion%20detection/Emotion.ipynb YoloV3: https://github.com/altaga/Pytorch-Driving-Guardian/blob/main/Hardware%20Code/Jetson%20Code/YoloV3/YoloV3.ipynb Introduction: Driving has become such a daily task for humans in the same level as eating, brushing our teeth or sleeping, however this in turn has become a task that can consume a large part of our day to day, in addition to being a potentially dangerous if certain safety rules are not followed. Problem: There are four very real and present dangers when driving: Being tired, sleepy or distracted. This could cause a crash by falling asleep or being distracted with the cell phone. Being in an irregular emotional state such as angry or sad. This can generate erratic or dangerous driving, triggering a much higher fuel consumption or even causing a crash. Not being able to pay attention to the blind spot of the vehicle. That when making a lane change or turning on a street a collision is caused or worse, injuring a person. Crashing and not being able to get quick help. That for any of the above reasons or external reasons we collide and when we collide we cannot notify our relatives or trusted contacts that we have collided and even more, where. Theoretical Support: The Center for Disease Control and Prevention (CDC) says that 35% of American drivers sleep less than the recommended minimum of seven hours a day. It mainly affects attention when performing any task and in the long term, it can affect health permanently [1] . According to a report by the WHO (World Health Organization) [2] , falling asleep while driving is one of the leading causes of traffic accidents. Up to 24% of accidents are caused by falling asleep, and according to the DMV USA (Department of Motor Vehicles) [3] and NHTSA (National Highway traffic safety administration) [4] , 20% of accidents are related to drowsiness, being at the same level as accidents due to alcohol consumption with sometimes even worse consequences than those. Also, the NHTSA mentions that being angry or in an altered state of mind can lead to more dangerous and aggressive driving [5] , endangering the life of the driver due to these psychological disorders. Solution: We built a prototype which is capable of performing these 3 monitoring reliably and in addition to being easy to install in any vehicle. This PoC uses a Jetson Nano 4gb in 5W mode as the main computer to maintain low consumption for continuous use in a vehicle. The Jetson Nano is a mini computer very similar to the RaspberryPi, with the difference that it has a Dedicated GPU enabled with CUDA, in order to run the Pytorch AI models on the GPU. To visualize the results, an M5core2 was used, which is an IoT device with a screen capable of displaying the data through MQTT. Full Solution Diagrams: This is the connection diagram of the system: The device mounted in the car would look like this. Models All the Computer Vision models powered by pytorch are step by step explained here: https://github.com/altaga/Pytorch-Driving-Guardian#drowsiness Commentary: I would consider the product finished as we only need a little of additional touches in the industrial engineering side of things for it to be a commercial product. Well and also a bit on the Electrical Engineering perhaps to use only the components we need. That being said this functions as an upgrade from a project that a couple friends and myself are developing and it was ideal for me to use as a springboard and develop the idea much more. This one has the potential of becoming a commercially available option regarding Smart Cities as the transition to autonomous or even smart vehicles will take a while in most cities. That middle ground between the Analog, primarily mechanical-based private transports to a more "Smart" vehicle is a huge opportunity as the transition will take several years and most people are not able to afford it. Thank you for reading. <div