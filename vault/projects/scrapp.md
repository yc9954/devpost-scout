---
slug: "scrapp"
url: "https://devpost.com/software/scrapp"
title: "Scrapp"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 874
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Scrapp

> Eliminate confusion with waste disposal using image recognition.

[Devpost](https://devpost.com/software/scrapp) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[education]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** flask, next.js, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scrapp
- ai usage

## Body

Homepage Waste Disposal Locator Inspiration At our school, we noticed that trash bins were often overfilled while recycling bins were nearly empty. This wasn’t because people didn’t care. Instead, they were often unsure of where to properly dispose of their items. That confusion inspired us to create Scrapp. We realized that small, everyday mistakes in waste disposal can collectively cause huge environmental problems. Learning how improper disposal contributes to pollution and resource loss motivated us to act. We wanted to make sustainable choices effortless by combining object detection with environmental awareness. Scrapp became our way to bridge that gap and make a real difference in our community. We imagined a tool that could instantly identify items through a photo and guide users to real drop-off centers. The idea that technology could create long-term habits and a cleaner future kept us motivated. Our next step is to partner with local recycling centers and nonprofits to bring Scrapp into real users’ hands. What it does Scrapp is a web and mobile app that simplifies recycling and waste disposal. Instead of guessing which bin to use, users can take a photo of any item, and the app instantly identifies it using a YOLOv8 object detection model. Once detected, Scrapp provides clear, location-specific guidance on how to responsibly dispose of it. After uploading an image, users receive three key outputs: The objects identified in the image. The disposal category for each object (recyclable, compostable, e-waste, etc.). A link to view nearby, verified disposal locations. This link opens an interactive map integrated with Google Maps. Users can sort results with tabs (e-waste, recycle, compost, donation) to find real, local facilities. The homepage educates users about improper waste disposal through case studies, such as how discarding batteries in curbside bins can cause fires. The clean, responsive layout makes Scrapp simple to use on any device—turning responsible waste management into something quick and accessible. How we built it We used Next.js for the frontend to build a clean, responsive user interface and Flask with Python for the backend. The AI model was implemented using YOLOv8 for object detection. To manage the full stack efficiently, we used Docker to containerize our app, making it easier to run on different devices. For training, we adapted the TACO (Trash Annotations in Context) dataset along with other image datasets to improve generalization. Our model identifies objects in images and connects them with local disposal information. Integrating this with our Google Maps-based system allowed us to show verified facilities nearby. Challenges we ran into The most difficult part was building the image recognition system. Our first attempt at training a model from scratch using TensorFlow failed due to the limited data that is generalizable to real-world irregularities. We then turned to the community and adapted YOLOv8, retraining it on curated datasets to fit our use case. Another challenge was converting raw predictions into meaningful user guidance. For example, translating “cup” into real-world disposal rules. We solved this by linking detection outputs to categorized disposal instructions. Accomplishments that we're proud of We’re proud that we were able to take an idea from scratch and turn it into a real, working app. Seeing Scrapp accurately recognize an item and show real recycling sites was a huge moment for our team. We’re also proud of how we overcame setbacks during training and integration, and how we built a system that incorporates technology with social impact. What we learned The Congressional App Challenge taught us much more than just coding. We learned how crucial teamwork and iteration are in real-world development. We started wanting everything perfect, but quickly discovered that testing, feedback, and constant improvement are what lead to success. Technically, we expanded our skills in Next.js, Flask, Python, and Docker, combining tools we had never used together before. But more importantly, we learned how to transform an idea into something tangible and impactful. The experience gave us insight into app design, AI deployment, and the real process of collaborative software development. What's next for Scrapp Our main goal for version 2.0 is to turn Scrapp into a native mobile app available on all major app stores. This would allow offline use and make the app easier to access. We also plan to fully integrate our AI model with real-time location services so that when a user scans an item, the app automatically shows directions to nearby disposal centers. Beyond that, we want to expand Scrapp into a platform for local businesses and services that handle waste pickups or donations. To make waste disposal more engaging, we’re exploring gamification. We are considering adding points, rewards, and community events so users stay motivated and make proper waste disposal seem fun. AI Usage AI was used to code certain components of the app's frontend; however, the core features, including image uploads and searching for locations, were created manually. On the backend, LLMs were used to perform research and locate potential datasets as well as generate sample code for testing out certain datasets; however, the core functionality (YOLO Object Detection) was not developed using AI-generated code. In other words, there was no "vibe coding" during the development of the app, but certain parts of it (outlined above) were developed using AI-assisted methods. <div