---
slug: "attendance-management-using-azure-cognitive-services"
url: "https://devpost.com/software/attendance-management-using-azure-cognitive-services"
title: "Attendance Management using Azure Cognitive Services"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 763
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/media_journalism"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Attendance Management using Azure Cognitive Services

> Still in my school taking manual attendance but they providing ID cards to every student, In this case, we are going to minimize the attendance management using Azure Cognitive Services

[Devpost](https://devpost.com/software/attendance-management-using-azure-cognitive-services) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[education]] [[media_journalism]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** azure, camera, computervision, customvision, iot, raspberry-pi, uwp, windows-10, windows-10-iot

## How they structured the write-up

- inspiration
- what it does
- how we built it
- why i used two cognitive services? we can archive the same thing using only custom vision, why you used azure computer vision
- challenges we ran into
- our mistakes
- accomplishments that we're proud of
- what we learned
- what's next for attendance management using azure cognitive services

## Body

Cover Photo Raspberry PI Setup With Camera Windows IoT OS Initialization Inspiration Still in my school, the attendance is taken manually. But they are providing id cards which becomes useless. Every period staff will be wasting time in taking attendance. In my office providing one ID card with RFID. In this, RFID is useless and RFID configuration to the Microcontrollers is creating complexity. So we have decided to build one attendance management project using Azure Custom Vision and Computer Vision. What it does User or student must show the ID card to the camera and Our Custom Vision will capture the current ID card validity. Because every company's Id card design is different. We will come to that later. Once the ID is valid, it will hit the Computer Vision to extract the texts from the ID card which will be sent to the server using an API call to record that the student is successfully logged in. How we built it First, we have created a Custom Vision Project at customvision.ai and taken 20 to 30 id card photos for the success case and taken 30 unknown ID card images for the failure case. Then we build a model and tested it quickly using the Quick Test option. After that, we extracted and downloaded the ONNX model. Once it downloaded created a new UWP project and added a reference for UWP IOT support. then we have added the ONNX model to the Assets folder. Then automatically it generates one model class with the same name as the ONNX model. Then created the CaptureVideo class to capture the video. Once the video is captured, the Frame arrived method will trigger for every frame arrival. Then we passed this frame to the model to predict the labels. With this, we would be getting a score with labels in which we are just checking the probability and tag a name if it's correct. If it is correct, we are also hitting a Computer Vision API to extract the texts from id card. To ensure correctness we are matching the pattern, as like my office id details has 3 lines of text there, which is set as a condition that if we got more than 3 lines from RecognizePrintedTextInStreamAsync API, then I know all details are found else I would be showing invalid ID text with a voiceover "Show correct ID". After this, we would be hitting an API to store the attendance details and reset the new frame arriving condition. Why I used two Cognitive Services? we can archive the same thing using only Custom Vision, Why you used Azure Computer Vision We can archive, but we can't get all ID cards to build the model. Just 30 to 50 ID cards are used to build a model to find, it the ID is valid or not. Then used the same camera frame to share into Computer Vision to Extract text and hit an API. In this way, we can convert the old users and new users without using RFID and manual attendance. Challenges we ran into Hard The exported ONNX model sometimes not creating a model class. While am creating a model with the "AzureCongitiveService.Prediction" option, I can't export the ONNX model. Easy Extracting the text using Computer vision is too easy Thanks to Microsoft and Team because you guys only make this too easy. When using OCR it is a very hard problem. our mistakes In this case, we bought the wrong camera module for Raspberry PI, so it did not work with Windows IoT Core. Accomplishments that we're proud of We have made our first ML Model without Code. Used Azure Custom Vision and Computer Vision. Build and Run First UWP IoT app to raspberry pi with Windows IoT Core OS. Really Custom Vision is awesome to build use. What we learned Build and Run First UWP IoT app to raspberry pi with Windows IoT Core OS. Learned some concepts in UWP and Windows IoT Core. Using Azure Custom Vision, build and exported our first no code ML Model and used it in our own project. Sometimes it not generating model class code, could you please fix it? We had struck nearly 1 week on this issue. Computer Vision and its services, In this project we have used only text extraction API. What's next for Attendance Management using Azure Cognitive Services Going to buy a new camera that supports Windows IoT Core. Then going to show it in our office and convince them to implement this in real-time for taking attendance. <div