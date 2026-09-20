---
slug: "vision-app"
url: "https://devpost.com/software/vision-app"
title: "VisionNav"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 1140
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# VisionNav

> Helping the visually impaired navigate their daily life - through sound.

[Devpost](https://devpost.com/software/vision-app) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** gemini, python, speech, swift, text-to-speech, visionproject, xcode, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for visionnav

## Body

VisionNav uses YOLO to identify specific objects in view and guides the user to them using spatial audio VisionNav detects an obstacle and alerts the user through audio cues VisionNav uses efficient YOLO to identify various objects at a high frame rate. Inspiration VisionNav is built with a focus on aiding the visually impaired who are looking for an easily accessible way to navigate their daily lives. The reason behind creating such an app is most of our team knows someone in their family who may face difficulties with vision. With further research into this topic, we found that 7.3 million adults in the U.S. are classified as visually impaired, with 1 million fully blind, of which 70% are unemployed. This reality inspired us to create VisionNav as an affordable solution that not only simplifies everyday navigation but also fosters independence and empowers users with the confidence to thrive in their communities. What it does VisionNav utilizes the built-in phone camera and LIDAR in an iPhone to stream a real-time visualization of the user's surroundings, and uses sound within devices like the AirPods to navigate around the setting. Within this setting, VisionNav aims to accomplish three different categories of tasks. The Obstacle Avoidance mode is used to navigate to an object while simultaneously avoiding obstacles using 3D audio cues that go off in either the left or right AirPod, directing the user to move in that direction. The Hand Guidance mode enables the user to ask VisionNav to locate a specific item in a given scene. With the help of the Gemini, the command stated by the user is deciphered and processed into the YOLO model, which identifies the object based on the deciphered message. Once the object is confirmed to be in the frame, the user will need to raise their hand and the app will guide the user towards the target object. The AI Mode uses Gemini to perform miscellaneous tasks, such as checking your surroundings or reading a book. How we built it VisionNav operates with hardware as simple as an iPhone and AirPods. We built a native Swift app using Xcode to read the iPhone's camera and lidar sensor data and transmit this information through a local server hosted on the iPhone. We use a MJPEG stream for the camera picture data, and encode the lidar sensor data into a custom packet which is transmitted through WebSockets. This allows for near real-time video quality with negligible lag. Upon receiving the photo and depth information, we use OpenCV and Ultralytics YOLO to identify various objects in the scene. We divide the depth frame into 5 equal columns and compute the distance to the closest obstruction in each, allowing the user to identify a heading with the least obstruction. Furthermore, we use YOLO to identify specific objects in the scene (book, water bottle, laptop, etc), allowing for VisionNav to finely guide the user's hand towards desired items. All of this is done at a rapid rate of > 20 frames per second through optimizations such as Numpy vectorization. By varying the amplitude in the left and right AirPods according to a mathematical formula, we are able to spatially simulate the location of objects around the user in 360 degrees. Imagine playing a game of Marco Polo: your friend repeatedly claps their hands, and you find your friend by heading in the direction of the clapping. This is exactly how VisionNav works. When guiding the user around obstacles, a ticking sound plays from a safe direction. The user moves towards this direction. The frequency of the ticking conveys information regarding the distance of obstacles (faster tempo = closer obstacle), and a constant tone plays to urgently alert the user when they are imminently about to run into an obstacle. When guiding the user's hand towards objects, the spatial location of the audio is informed by the hand's position relative to the object (i.e. the user moves their hand towards the ticking sound). The audio changes pitch depending on the user's proximity to the object, letting the user know when they may extend their hand to grasp the object. When building VisionNav, user experience and comfort was our top priority. We experimented with various different frequencies and audio filters to create a pleasant and non-intrusive sound. Furthermore, we spent hours tuning our speech recognition method to boost accuracy and reduce frustration. Challenges we ran into The main challenge we faced during the implementation of VisionNav was navigating to an object while still handling obstacles. It was especially hard to switch between the needs of the user. Another struggle was the voice recognition accuracy of the Google speech-to-text program. Since we had limited knowledge of using this and there was limited documentation, it took a lot of time to get the accuracy high. Additionally, integrating all our features at the end was a big struggle because of the multiple juggling pieces. Accomplishments that we're proud of The main accomplishment we are proud of is the feature where we use the hand navigation to find a target object in a set frame based on the 3D audio cues which signify the left and right directions through the corresponding AirPod signal, and the aligned forward motion of the hand with a higher pitch with rapid ticking noise as the hand got closer to the target object, all of which was processed with the YOLO model's ability to locate and identify the target object in the set frame and mediapipe's ability to locate the hand. What we learned VisionNav was a project that provided valuable learning experiences. Starting with the sensing aspect, on Xcode using Swift, our team learned to activate and extract the data collected through the camera and lidar built into the iPhone. Our team also experimented with the use of depth data and distancing while using audio libraries from Python to connect the conditional situations of playing audio cues for the user. There was also the use of the YOLO model, a real-time object detection algorithm, which is vital in identifying objects present in a given frame. We also learned how to utilize Gemini which we had never used before. With all these functionalities present, we also had to learn how to efficiently combine all these components into one application, which resulted in VisionNav. What's next for VisionNav With the current implementation of VisionNav, we have created straightforward functionality that aims to make mobility easier for visually impaired users. We want to convert this into a startup. We would then make the product available for public use. We aim to enhance the accuracy of the audio cues by improving latency. We also want to integrate the app into wearable hardware, such as glasses with cameras which could make the viewing aspect of the app more natural while keeping costs low. <div