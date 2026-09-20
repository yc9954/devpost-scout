---
slug: "torch-drowsiness-monitor"
url: "https://devpost.com/software/torch-drowsiness-monitor"
title: "Torch Drowsiness Monitor."
hackathon: "Facebook Hackathon: AI"
organization: "Facebook"
winner: true
words: 1135
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

# Torch Drowsiness Monitor.

> Drowsiness and atention monitor for driving. Also detects objects at the blind spot via Pytorch-powered Computer Vision and the NVIDIA Jetson Nano.

[Devpost](https://devpost.com/software/torch-drowsiness-monitor) · hackathon [[Facebook Hackathon- AI]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]] [[civic_government]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[video_visual]]

**stack** arduino, jetpack, jetson-nano, mqtt, opencv, python, pytorch, twilio, yolo

## How they structured the write-up

- inspiration and introduction
- solution and what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned and what's next for torch drowsiness monitor.

## Body

Final Product Alertness detection Object detection Prototype installed Another angle Torch Drowsiness Monitor. Drowsiness and attention monitor for driving. Also detects objects at the blind spot via CV and the NVIDIA Jetson Nano. Inspiration and Introduction We will be tackling the problem of drowsiness when handling or performing tasks such as driving or handling heavy machinery and the blind spot when driving. With some features on the side. But let's take this on from the beginning we first have to state what the statistics show us: Road Injury is the 8th cause of death worldwide: More than most Cancers and on par with Diabetes. Huge area of opportunity, let's face it autonomy is still has a long way to go. A big cause is distraction and tiredness or what we call "drowsiness". The Center for Disease Control and Prevention (CDC) says that 35% of American drivers sleep less than the recommended minimum of seven hours a day. It mainly affects attention when performing any task and in the long term, it can affect health permanently. According to a report by the WHO (World Health Organization) (2), falling asleep while driving is one of the leading causes of traffic accidents. Up to 24% of accidents are caused by falling asleep, and according to the DMV USA (Department of Motor Vehicles) (3) and NHTSA (National Highway traffic safety administration) (4), 20% of accidents are related to drowsiness, being at the same level as accidents due to alcohol consumption with sometimes even worse consequences than those. Solution and What it does We createda system that is able to detect a person's "drowsiness level", this with the aim of notifying the user about his state and if he is able to drive. At the same time it will measure the driver’s attention or capacity to garner attention and if he is falling asleep while driving. If it positively detects that state (that he is getting drowsy or distracted), a powerful alarm will sound with the objective of waking the driver. Additionally it will detect small vehicles and motorcycles in the automobile’s blind spots. In turn, the system will have an accelerometer to generate a call to the emergency services if the car had an accident to be able to attend the emergency quickly. How we built it This is the connection diagram of the system: The brain of the project is the Jetson Nano, it will take care of running through both of the Pytorch-powered Computer vision applications, using a plethora of libraries in order to perform certain tasks. The two webcams serve as the main sensors to carry out Computer Vision and then Pytorch will perform the needed AI in order to identify faces and eyes for one application and objects for the other and will send the proper information through MQTT in order to emmit a sound or show an image in the display. As features we added geolocation and crash detection with SMS notifications. That done through twilio with an accelerometer. The first step was naturally to create the two Computer vision applications and run them on a Laptop or any PC for that matter before going to an embedded computer, namely the jetson nano: Performing eye detection after a face is detected: This is a video test of that done step by step (click on the image): And then testing Object detection for the Blind spot notifications on the OLED screen: After creating both of the applications it was time to make some hardware and connect everything: This is the mini-display for the object detection through the blind spot. The acceleromenter for crash detection. The finished prototype. Because it is primarily an IoT enabled device, some of the features like the proximity indicator and the crash detector are not possible to test remotely without fabricating your own. Having said that, the Pytorch-made computer vision drowsiness and attention detector that tracks eye and faces works on any device! Even the alarm. If you will be running it on a laptop our Github provides instruction as you need quite several libraries. Here is the link, you just have to run the code and it works perfectly (follow the github instructions): https://github.com/altaga/Torch-Drowsiness-Monitor/tree/master/Drowsiness You can find step by step documentation of how to do your own fully enabled Torch Drowsiness monitor, on our github: https://github.com/altaga/Torch-Drowsiness-Monitor Challenges we ran into At first we wanted to run Pytorch and do the whole CV application on a Raspberry Pi 3, which is much more available and an easier platform to use. It probably was too much processing for the Raspi3 as it wasn't able to run everything we demanded so we upgraded to an embeded computer specialized for ML and CV applications as it has an onboard GPU: the Nvidia Jetson Nano. With it we were able to run everything and more. Later we had a little problem of focus with certain cameras so we had to experiment with several webcams that we had available to find one that didn't require to focus. The one we decided for is the one shown in the video. Despite it's age and probably lack of resolution it was the correct one for the job as it mantained focus on one plane instead of actively switching. Accomplishments that we're proud of After finishing the prototype, the installation only took us about 10 minutes tops, which is a huge value proposition that puts us, talking about smart devices, on par with the time it takes to configure an Amazon Echo device or a Google home. Apart from that I think we can provide that "Smart" component to analog or "austere" vehiclesat a much lower price than their smart counterparts. Approxzimately 95% of cars on the streets are of these characteristics and it shows the huge opportunity and market of a proposition such as this one. What we learned and What's next for Torch Drowsiness Monitor. I would consider the product finished as we only need a little of additional touches in the industrial engineering side of things for it to be a commercial product. Well and also a bit on the Electrical engineering perhaps to use only the components we need. That being said this functions as an upgrade from a project that a couple friends and myself are developing and It was ideal for me to use as a springboard and develop the idea much more. This one has the potential of becoming a commercially available option regarding Smart cities as the transition to autonomous or even smart vehicles will take a while in most cities. That middle ground between the Analog, primarily mechanical-based private transports to a more "Smart" vehicle is a huge opportunity as the transition will take several years and most people are not able to afford it. Thank you for reading. <div