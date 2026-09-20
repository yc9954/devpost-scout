---
slug: "edith-bvh014"
url: "https://devpost.com/software/edith-bvh014"
title: "Edith"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 928
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Edith

> Solving the accessibility crisis, one second pair of eyes at a time.

[Devpost](https://devpost.com/software/edith-bvh014) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]]
**substrate** [[geospatial]] [[video_visual]]

**stack** adafruit, gemini, numpy, pytorch, raspberry-pi, react, tailwind, typescript

## How they structured the write-up

- software
- hardware
- engineering and design considerations
- custom designed circuits
- our takeaways

## Body

Software With our software stack, we introduce a powerful any-3D-object segmentation architecture backed by several SoTA machine learning models. Many object segmentation models are trained on highly specific datasets such as COCO and hence lack generalizability, whereas VLMs like ChatGPT-4o lack a rich understanding of the 3D world. By parallelizing AI inference on 4 NVIDIA A100s, we computed and streamed accurate, realtime depth maps, segmentation maps, and point clouds to contextualize the richness of the 3D world for those visually impaired. With the live Gemini multimodal API, we prompt Gemini with the object heading and depth, from which it is able to obtain the precise location of any desired object from where the user is. The low latency communication between devices was a huge part of getting this to work in essentially real time. Our initial networking setup was built from a series of complicated websocket servers and clients on our various devices, including a Raspberry Pi, our laptops, and an NVIDIA A100 server. This setup enabled more granular communication and flow of data between devices, allowing us to pursue more ambitious ideas with our glasses. However, we ultimately decided on a much simpler architecture involving porting forward files and video streams across the network and simple HTTPs API routes. On the embedded software side, we wrote several scripts to program LEDs, and vibration motors and feed the camera stream to other devices. We programmed an IMU on the glasses to calculate the yaw, pitch, and roll to detect when someone has fallen. To elevate the user’s sense of spatial awareness, by coordinating our IMU with the vibration motors, we programmed a haptic feedback algorithm using complementary filtering to get the motors to vibrate with a decaying amplitude the closer they approach the desired object of interest, indicating to them when they are facing the object. Hardware To address the complex challenges faced by visually impaired individuals in navigating their environments safely and autonomously, we developed Edith—an actionable, adaptable, accessible assistant translating the visually rich world into forms that the blind can experience. Edith facilitates spatial awareness and object recognition, enabling users to interact with their surroundings with greater ease and confidence. Given the system’s technical demands, including real-time object detection, haptic feedback, and low-latency data processing, a robust hardware framework was imperative. The decision to implement a smart glasses-based system, rather than handheld or mobile alternatives, was driven by the need for an intuitive, ergonomic, and non-intrusive user experience. Smart glasses provide a seamless integration into daily life, avoiding the conspicuousness and inconvenience of handheld devices such as smartphones or external cameras. Engineering and Design Considerations Our primary engineering objective was to optimize the functionality and efficiency of the system while maintaining a lightweight and comfortable form factor. The hardware architecture centers around a Raspberry Pi Zero 2W, supplemented by an inertial measurement unit (IMU) for motion tracking, a high-resolution camera for real-time video processing, and haptic feedback motors to provide tactile sensory input. Additionally, an LED strip was incorporated to enhance night-time usability by acting as an auxiliary illumination source. To ensure prolonged operation, the glasses integrate lithium-polymer (Li-Po) batteries, managed by step-up voltage boost converters to maintain stable power delivery across all components. Modular Framework and Material Selection To facilitate rapid prototyping, adaptability, and scalability, we employed a modular design paradigm for the hardware assembly. The structural framework consists of 3D-printed components, allowing iterative design refinements and seamless modifications. The integration of heat-treated brass elements enhances durability and structural integrity, ensuring the device remains lightweight while offering sufficient rigidity to support embedded electronics. The modular design also enables the repositioning of different hardware modules, allowing iterative optimization of weight distribution and system balance. Through multiple design iterations, we identified the optimal layout for component placement, ensuring both ergonomic comfort and efficient power management. Custom Designed Circuits In addition to the CAD models used to develop and implement Edith, custom-built PCBs were designed to support the embedded hardware. Using perf boards, we developed small, compact tactile circuit boards that effectively integrate haptic feedback motors while efficiently utilizing the limited space available within our compact glasses. An example of the PCB we designed and implemented is presented below. While similar designs exist, our approach is particularly exciting as it was developed to be as small and compact as possible using only resources available at a university hackathon or makerspace. Our takeaways We entered this competition as four driven individuals with one goal in mind: to walk out with the greatest creation we could build in 36 hours. But beyond the project itself, what made this experience truly special was being surrounded by our closest friends—watching each other work with enthusiasm, dedication, and relentless determination was nothing short of inspiring. For 36 hours, we were confined within the walls of the David Packard Electrical Engineering Building, yet in that space, we found countless moments of growth. Each of us came into this hackathon with different backgrounds—whether in embedded systems, cutting-edge machine learning, or CAD design—but together, we played to each other’s strengths and, more importantly, pushed ourselves to learn. The challenges we faced were often outside our comfort zones, leaving us no choice but to adapt and grow. From interfacing with a Raspberry Pi for the first time to soldering custom PCBs on a perf board, every obstacle became an opportunity to expand our skill sets. By the end, each of us walked away not only with new technical expertise but also with memories that will last a lifetime. Oh, and about five empty Monster cans each! <div