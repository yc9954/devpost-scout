---
slug: "edusphere-95goxk"
url: "https://devpost.com/software/edusphere-95goxk"
title: "EduSphere"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 428
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "substrate/structured_db"
---

# EduSphere

> Learn a language on the Apple Vision Pro

[Devpost](https://devpost.com/software/edusphere-95goxk) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]]
**substrate** [[structured_db]]

**stack** adobe-xd, alamofire, cockroachdb, cohere, flask, google-cloud, mvvm, nomad, python, realitykit, sql, swift, swiftui, visionos

## How they structured the write-up

- our inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

About Page Chatbot Game Immersion Learn Our Inspiration We were inspired by apps like Duolingo and Quizlet for language learning, and wanted to extend those experiences to a VR environment. The goal was to gameify the entire learning experience and make it immersive all while providing users with the resources to dig deeper into concepts. What it does EduSphere is an interactive AR/VR language learning VisionOS application designed for the new Apple Vision Pro. It contains three fully developed features: a 3D popup game, a multi-lingual chatbot, and an immersive learning environment. It leverages the visually compelling and intuitive nature of the VisionOS system to target three of the most crucial language learning styles: visual, kinesthetic, and literacy - allowing users to truly learn at their own comfort. We believe the immersive environment will make language learning even more memorable and enjoyable. How we built it We built the VisionOS app using the Beta development kit for the Apple Vision Pro. The front-end and AR/VR components were made using Swift, SwiftUI, Alamofire, RealityKit, and concurrent MVVM design architecture. 3D Models were converted through Reality Converter as .usdz files for AR modelling. We stored these files on the Google Cloud Bucket Storage, with their corresponding metadata on CockroachDB. We used a microservice architecture for the backend, creating various scripts involving Python, Flask, SQL, and Cohere. To control the Apple Vision Pro simulator, we linked a Nintendo Switch controller for interaction in 3D space. Challenges we ran into Learning to build for the VisionOS was challenging mainly due to the lack of documentation and libraries available. We faced various problems with 3D Modelling, colour rendering, and databases, as it was difficult to navigate this new space without references or sources to fall back on. We had to build many things from scratch while discovering the limitations within the Beta development environment. Debugging certain issues also proved to be a challenge. We also really wanted to try using eye tracking or hand gesturing technologies, but unfortunately, Apple hasn't released these yet without a physical Vision Pro. We would be happy to try out these cool features in the future, and we're definitely excited about what's to come in AR/VR! Accomplishments that we're proud of We're really proud that we were able to get a functional app working on the VisionOS, especially since this was our first time working with the platform. The use of multiple APIs and 3D modelling tools was also the amalgamation of all our interests and skillsets combined, which was really rewarding to see come to life. <div