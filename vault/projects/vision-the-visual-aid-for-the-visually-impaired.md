---
slug: "vision-the-visual-aid-for-the-visually-impaired"
url: "https://devpost.com/software/vision-the-visual-aid-for-the-visually-impaired"
title: "Vision - the Visual Aid for the Visually Impaired"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 797
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Vision - the Visual Aid for the Visually Impaired

> Vision seeks to aid difficulties faced by the Visually impaired in understanding their surrounding. The solution’s main goal is to provide a sense of vision to the visually impaired.

[Devpost](https://devpost.com/software/vision-the-visual-aid-for-the-visually-impaired) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[structural_withholding]] [[voice_speech]]
**domain** [[accessibility]] [[transportation]]
**user** [[general_public]]
**substrate** [[geospatial]] [[video_visual]]

**stack** azure, azure-app-service, azure-computer-vision, azure-custom-vision, azure-face-api, azure-kubernetes-service, azure-maps, azure-speech, azure-translator, docker, javascript, python, react-native, tensorflow

## How they structured the write-up

- motivation for vision
- what vision does
- how we built vision
- challenges we ran into
- accomplishments that we're proud of
- future scope for vision

## Body

Vision - the Visual aid Team Intelli-Sense Vision Application UI Vision Architecture Motivation for Vision Our world currently has around 285 million population who are visually impaired out of which 40 million are totally blind. With the rapid growth of technology, advancements have been made in several fields of human interaction. However, there have not been many contributions towards the welfare of the visually impaired. This project seeks to aid the difficulties faced by the blind in perceiving and understanding their surroundings by harnessing the power of AI and revolutionary cloud technology especially in tougher situations such as crossing a road or reading a book. The proposed solution solves for the purpose by providing complete visual assistance with the help of a device that is readily accessible by them (their mobile phones). What Vision does The proposed solution uses a wide range of technologies to converge at the solution. The system uses Image Captioning, Optical Character Recognition, Text to Speech, Machine Language Translation provided by Microsoft Azure Cloud Services and Custom trained deep learning models. Image Captioning enables the conversion of image to relatable text, which in turn is converted into voice with the help of Text to Speech, thereby making blind to comprehend the visual surrounding, which in turn gives a sense of Vision. Optical Character Recognition enables the blind to understand the text without the help of a tactile writing system like braille. Machine language translation allows the conversion of text to any language seamlessly. The modules are integrated together as a single working mobile application powered by java-script (React native). The final solution would be a working mobile application that would be voice-enabled, to make it easier for the blind, and here are the things it would be able to accomplish • Able to click pictures with a single touch/tap • Describe the clicked picture in a comprehendible language (70+ language support) • Analyse text in the image and recite it to the user and ability to summarize long texts • Multiple language support (both regional and worldwide) currently supports 73 languages with native fluency in 30 languages • Ability to change languages with voice commands • In-depth image analysis for specific use cases like finding currency notes, walking on the road, etc • Get location assistance based on their current GPS position with respect to their nearest landmark How we built Vision Vision has been built extensively based on Azure cloud and Azure AI. Vision is an API-based mobile application that is built on the following architecture. Vision Architecture Challenges we ran into 1. The important challenge for us was that there are numerous solutions out there in the market which address the same problem. The most important question that we had to answer was, “How can vision stand out among its competitors”. 2. Since, we are dealing with a very sensitive use-case, we had to tick all the boxes right and assure 100% quality. A minute error in the application might cause a catastrophic impact. Hence, we have utilized cloud-hosted state-of-the-art models, models custom trained for visually impaired which are highly reliable and deliver accurate results. 3. Secondly, while creating a mobile app for visually impaired people, we need to ensure that it is usable and accessible by the consumer. To address this, we came up with a very minimalistic gesture-controlled UI design, which provides ease of access to the user. 4. Thirdly, catering to the needs of people in a country like India with such a diverse population is a challenge by itself. To solve this, we have added support of 70+ languages with native fluency in almost over 30 languages. 5. Most importantly, vision must be able to model the real world effectively. The feature that makes VISION stand out as unique is its ability to fit across custom situations such as currency note detection, traffic signal detection, etc., which can be integrated with the existing application seamlessly. 6. Hence, there were a lot of challenges we had to face in this 6-month long journey of developing vision. But, as a team, we came across all of it and were able to come up with a product that would change the lifestyle of millions of people. Accomplishments that we're proud of 1. Created a simple UI design for Visually impaired 2. Made it to work realtime without compromising on features 3. Provided support to 70+ languages. Future Scope for Vision 1. The application can be made personalized to the user to work according to the user’s context to give user-customized image description. 2. Use advanced geospatial coordinate indices to give location assistance to the user based on their needs. 3. Use of 3-d image mapping to completely assist the user when they are present outdoor or in harsh terrains. <div