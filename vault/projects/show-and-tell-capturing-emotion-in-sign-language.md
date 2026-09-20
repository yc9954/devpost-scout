---
slug: "show-and-tell-capturing-emotion-in-sign-language"
url: "https://devpost.com/software/show-and-tell-capturing-emotion-in-sign-language"
title: "Show and Tell - Capturing Emotion in Sign Language"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 1040
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Show and Tell - Capturing Emotion in Sign Language

> Enabling emotion and expression for the hard of hearing. Through innovative wearable technology and LLM integration, Show and Tell tackles the issue of accessibility for the hard of hearing.

[Devpost](https://devpost.com/software/show-and-tell-capturing-emotion-in-sign-language) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]]
**substrate** [[financial_record]] [[video_visual]]

**stack** esp32, humeai, imu, openai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for show and tell - capturing emotion in sign language

## Body

Inspiration Our team focuses extensively on opportunities to ignite change through innovation. In this pursuit, we began to investigate the impact of sign-language glove technology on the hard of hearing community. In this, we learned that despite previous efforts to enhance accessibility, feedback from deaf advocates highlighted a critical gap: earlier technologies often facilitated communication for hearing individuals with the deaf, rather than empowering the deaf to communicate on their terms. After discussing this problem with a friend of ours who faces disabilities related to her hearing, we realized that this problem impacts many people's daily lives, significantly affecting their ability to engage with those around them. By focusing on human centered design and integrating feedback presented in numerous journals, we solve these problems by developing an accessible, easy to use interface that enables the hard of hearing and mute to converse seamlessly. Through integration of a wearable component and a sophisticated LLM, we completely change the landscape of interpersonal communications for the hard of hearing. What it does Our solution consists of two components, a wearable glove and a mobile video call interface. The wearable glove is meant to be utilized by a deaf or hard of hearing individual when conversing with another person. This glove, fitted with numerous flex sensors and an Inertial Measurement Unit (IMU), can discern what gloss (term for a word in ASL) the wearer is signing at any moment in time. From here, the data moves to the second component of the solution - the mobile video call interface. Here, the user's signs are converted into both text and speech during a call. The text is displayed on the screen while the speech is stated, ensuring to include emotional cues as picked up by the integrated computer vision model. This effectively helps users communicate with others, especially loved ones, in a manner that accurately represents their intent and emotions. This experience is one that is currently not offered anywhere else on the market. In tandem, both of these technologies enable us to understand body language, emotion, and signs from a user, and also help vocalize the feelings of a person who is hard of hearing. How we built it Two vastly different components call for drastically different approaches. However, we needed to ensure that these two approaches still stayed true to the same intent. We first began by identifying our design strategy, based in our problem statement and objective. From here, we moved forward with set goals and milestones. On the hardware side of things, we spent an extensive amount of time in the on-site lab fabricating our prototype. In order to ensure the validity of our design, we researched circuit diagrams and characteristics, ultimately building our own. We performed a variety of tests on this prototype, including practical use testing by taking it around campus while interacting with others. The glove withstood numerous handshakes and even a bit of rain! On the software side, we also had two problems to face - interfacing with the glove, and creating the mobile application. To interface with the glove, we began with the Arduino IDE for testing. After we ensured that our design was functional and gained test data, we moved to a python implementation that sends sensed words up to an API, which can later be accessed by the mobile application. Moving to the mobile application, we utilized SwiftUI for our design. From there, we used the StreamAPI to build a FaceTime style infrastructure. We prototyped and integrated between Figma designs and our prototype to best understand where we could increase capabilities and improve the user experience. Challenges we ran into This project was ambitious, and as such, was also chock full of complications. Initially, we faced extensive challenges on the hardware side. Due to the nature of the design, we have many components that are trying to draw power or ground from the same source. This provided increased complexity in our manufacturing process, as we had to come up with an innovative solution to a sleek design that maintained functionality. Even after we found our first solution, our prototype was inconsistent due to manufacturing flaws. On the last day, 2 hours before the submission deadline, we completely disassembled and rebuilt our prototype using a new methodology. This proved to be successful, minimizing the issues seen previously and resulting in an amazing product. On the software side, we also pursued ambitious desires that didn't distinctly align with our team's expertise. Due to this, we faced great difficulty when troubleshooting the numerous errors we faced in initial implementation. This set us back quite extensively, but we were able to successfully recover. Accomplishments that we're proud of We are proud of the magnitude of success we were able to show in the short frame of this hackathon. We came in knowing that we had ambitious and lofty goals, but were unsure if we would truly be able to achieve them. Thankfully, we complete this hackathon with a functional, viable MVP that clearly represents our goals and desires for this project. What we learned Because of the cross discipline nature of this project. All of our team members got the opportunity to explore new spaces. Through collaboration, we all learned about these fields and technologies from and with each other and how we can integrate them into our systems in the future. We also learned about best practices for manufacturing in general. Additionally, we were able to become more comfortable with SwiftUI and creating our own APIs for our video calling component. These valuable skills shaped our experiences at TreeHacks and will stick with us for many years to come. What's next for Show and Tell - Capturing Emotion in Sign Language We hope to continue to pursue this idea and bring independence to the hard of hearing population worldwide. In a market that has underserved the deaf population, we see Show and Tell as the optimal solution for accessibility. In the future, we want to flesh out the hardware prototype further by investing in custom PCB's, streamlining the production process and making it much more professional. Additionally, we want to build out functionality within the video calling app, adding in as many helpful features as possible. <div