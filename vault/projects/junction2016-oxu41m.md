---
slug: "junction2016-oxu41m"
url: "https://devpost.com/software/junction2016-oxu41m"
title: "Look For Me!"
hackathon: "Junction 2016"
winner: true
words: 1159
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Look For Me!

> A virtual assistant for the blind!

[Devpost](https://devpost.com/software/junction2016-oxu41m) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[health_clinical]]
  <sub>weak: developer_tools</sub>
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** ai, android, android-studio, google-cloud-vision-api, ibeacons, java, object-recoginition, proximi.io, speech-recoginition, texttospeech-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for look for me!

## Body

Please note that this application is aimed for the blind, therefore this contains mainly debugginginformation Inspiration Erwin got the inspiration thinking about how new technology, e.g., advances in Artificial Intelligence and related computer vision developments, can have an impact on people's lives. For most people, advances in technology, especially in the mobile device sector, enhance comfort and deliver entertainment. However, for some, new technology can have a much greater impact on everyday life. We started a brainstorming session after we met, under the brainstorming we come up with the idea to develop an application to assist the blind. At the core, we aimed to create a solution which can “look around”, recognize objects, and store this information together with (indoor) location data for later use. Bundled with an easy-to-use voice interface, this would help the blind find the objects in their surroundings. Our idea further evolved after reading about the GE Healthcare challenge; voice commands and text-to-speech could also be useful for other groups such as children. At a hospital the children might feel lost or disoriented, we all know that the machines can look really frightening especially for children. We thought that if we made an app to show our young ones what the machines does they might be less frightening. What it does The application helps the bind people to find objects and their location, especially indoors, without the need for a cane. The only thing the blind person needs is his/her cellphone with our application installed. Currently, our application has these functions: Automatic object recognition. The user takes a photo via our app which then uses an Artificial Intelligence-enhanced vision API to detect objects in the scene. This data is saved together with the position (latitude/longitude as well as a human-readable room name) so that the user can later ask the app about his/her relative location to the seen objects. For our prototype, photos are taken with a manual click. Later, this would happen automatically to keep an up-to-date database of all relevant objects around the user. Look for Me (1). The user can ask questions like “Where is my guitar” and our app tells him/her the answer based on the previously recorded information, e.g, “In the Main Hall, about 10 meters left of you.” This helps the user in navigating to the desired object. Look for Me (2). The user can ask questions like “What is in front of me?” and our app tells him/her the answer. This is based on indoor beacons which could even allow for dynamic, complex objects like health machines where an object recognition using computer vision is unable to correctly recognize the object. Of course, this feature can help sighted people as well, e.g., children in the aforementioned hospital context with unknown objects. How we built it After our brainstorming session, we started to discuss how we should develop our application. Neither of the team had developed an application for iOS before, but both Christian and Erwin had written Android applications before so we decided to built our prototype on Android. We started by researching APIs for IPS (Indoor positioning system), Image/Object Recognition, voice-recognition, and Text-to-Speech on the first day of Junction 2016. On day two we started building our application. The first function we wrote was the object recognition function using Google’s Cloud Vision API together with proximi.io’s (indoor) positioning API. The second one was the voice interface using Android’s Speech Recognition and Text-To-Speech features. There, we also implemented functionality that calculated the relative position of an object to the user based on the location of the user and the orientation of his phone. Now one hour and 15 minutes before the submission we’re still trying to inprove our application but with no success. After some research we found out that the most common problem for a blind is to find their things. Another problem they often have is to navigate in their home, hotels, venues etc. Challenges we ran into Our biggest challenge was to get all the APIs and other data sources to collaborate with each other. We put in many hours to fix issues related to that. Also, the Android emulator wouldn’t run on Macs so we only had one physical device to prototype on. While the indoor positioning API provides high-accuracy results using beacons and even supports so-called departments, e.g., for rooms, it was unable to map location data to department/room names. Therefore, we had to implement our own mapping using polygon geofences for the known departments. Unfortunately, we did not manage to integrate Firebase into our project although we’d have loved to use it for our database. Another challenge was to convert between 0 to 360, -180 to 180 and -pi to pi angles with varying interpretations of what is clockwise/counterclockwise was surprisingly annoying. Accomplishments that we're proud of First and foremost, we actually managed to build a working prototype of our idea in just about 40 hours. The automatic object recognition via the vision API works rather well for the tested objects, also the (indoor) location data provides accurate enough data. Our voice interface is simple to use and, together with the relative location/distance computations, allows the app to “look” for the user and either tell him/her where a desired object is or, e.g., what an object in front of him/her is. We managed to work around some limitations of the proximi.io API after talking to their representatives here at Junction. Thanks for your help! What we learned Our team member Lauri had never used Java or developed for Android before so this was an ideal opportunity to learn the basics. We also have learned how to use the Google Cloud Vision API for Image/Object Recognition and Android’s voice features (Speech Recognition/Text-To-Speech). We did also learn about IPS (Indoor positioning system), and therefore wish to acknowledge proximi.io for this opportunity to work with IPS. What's next for Look For Me! Our prototype requires manual action to take photos which were then analyzed using the vision API. We’d like to build an efficient solution which continuously monitors the user’s surroundings to keep up-to-date information on all interesting objects around him/her. Additionally, we’d like to implement a local vision API for object recognition so that our app does not depend on an active Internet connection to work. Advances in AI-based object recognition are promising for such an approach. Although the indoor positioning has a rather good accuracy, often around 1 meter, we’d like to implement pin-point navigation by using the camera with object recognition continuously. For example, simple “left”/”right” commands near the searched object can allow the user to find it even easier and faster. Finally, we’d like to augment our results with further data. For example, if the user asks about the object in front of him/her, it’d be great if our app would not only tell the object’s name but also other information, e.g., a more detailed description or other (contextual) information. <div