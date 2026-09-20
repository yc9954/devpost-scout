---
slug: "cleancue"
url: "https://devpost.com/software/cleancue"
title: "CleanCue"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 645
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/education"
  - "domain/elder_child_care"
  - "user/educator_student"
  - "substrate/video_visual"
---

# CleanCue

> From a spotless start to a messy counter chaos - we've all been there! Remember the days when mom's nagging was annoying but helpful? Introducing CleanCue - your secret to harmony in shared spaces!

[Devpost](https://devpost.com/software/cleancue) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[agriculture_food]] [[education]] [[elder_child_care]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** cuda, google-cloud, opencv, python, raspberry-pi, taipy, tcp, tts

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cleancue

## Body

CleanCue prototype attached to tripod CleanCue prototype Close up of the Raspberry Pi Camera Module used in the CleanCue Photo of the internals of the CleanCue Photo of the internals of the CleanCue Screenshot of the OpenCV object detection Screenshot of the OpenCV object detection Inspiration As most of our team became students here at the University of Waterloo, many of us had our first experience living in a shared space with roommates. Without the constant nagging by parents to clean up after ourselves that we found at home and some slightly unorganized roommates, many shared spaces in our residences and apartments like kitchen counters became cluttered and unusable. What it does CleanCue is a hardware product that tracks clutter in shared spaces using computer vision. By tracking unused items taking up valuable counter space and making speech and notification reminders, CleanCue encourages roommates to clean up after themselves. This product promotes individual accountability and respect, repairing relationships between roommates, and filling the need some of us have for nagging and reminders by parents. How we built it The current iteration of CleanCue is powered by a Raspberry Pi with a Camera Module sending a video stream to an Nvidia CUDA enabled laptop/desktop. The laptop is responsible for running our OpenCV object detection algorithms, which enable us to log how long items are left unattended and send appropriate reminders to a speaker or notification services. We used Cohere to create unique messages with personality to make it more like a maternal figure. Additionally, we used some TTS APIs to emulate a voice of a mother. Challenges we ran into Our original idea was to create a more granular product which would customize decluttering reminders based on the items detected. For example, this version of the product could detect perishable food items and make reminders to return items to the fridge to prevent food spoilage. However, the pre-trained OpenCV models that we used did not have enough variety in trained items and precision to support this goal, so we settled for this simpler version for this limited hackathon period. Accomplishments that we're proud of We are proud of our planning throughout the event, which allowed us to both complete our project while also enjoying the event. Additionally, we are proud of how we broke down our tasks at the beginning, and identified what our MVP was, so that when there were problems, we knew what our core priorities were. Lastly, we are glad we submitted a working project to Hack the North!!!! What we learned The core frameworks that our project is built out of were all new to the team. We had never used OpenCV or Taipy before, but had a lot of fun learning these tools. We also learned how to create improvised networking infrastructure to enable hardware prototyping in a public hackathon environment. Though not on the technical side, we also learned the importance of re-assessing if our solution actually was solving the problem we were intending to solve throughout the project and make necessary adjustments based on what we prioritized. Also, this was our first hardware hack! What's next for CleanCue We definitely want to improve our prototype to be able to more accurately describe a wide array of kitchen objects, enabling us to tackle more important issues like food waste prevention. Further, we also realized that the technology in this project can also aid individuals with dementia. We would also love to explore more in the mobile app development space. We would also love to use this to notify any dangers within the kitchen, for example, a young child getting too close to the stove, or an open fire left on for a long time. Additionally, we had constraints based on hardware availability, and ideally, we would love to use an Nvidia Jetson based platform for hardware compactness and flexibility. <div